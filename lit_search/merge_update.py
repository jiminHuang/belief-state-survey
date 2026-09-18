#!/usr/bin/env python3
"""Monthly update, step 3: merge runs/updates/<YYYY-MM>/screen.csv into the master record (next version), write BibTeX for the
new entries via the arXiv API, regenerate the README, and add a line to UPDATES.md.
Usage: merge_update.py <YYYY-MM>"""
import csv, re, sys, glob, subprocess, pathlib
root = pathlib.Path(__file__).parent; ym = sys.argv[1]; run = root / "runs/20260916_v3"
FIELDS = "arxiv_id,date,title_short,decision,who_maintains_belief,credited_object,revision_signal,belief_level_metrics,survey_section,role_in_survey,note,bibkey,first_author,title,venue,evidence".split(",")
masters = sorted(glob.glob(str(run / "manual_screen_all_v*.csv")), key=lambda p: int(re.search(r"_v(\d+)\.csv", p).group(1)))
vin = int(re.search(r"_v(\d+)\.csv", masters[-1]).group(1)); vout = vin + 1
base = list(csv.DictReader(open(masters[-1]))); norm = lambda t: re.sub(r"[^a-z0-9]", "", (t or "").lower())
seen_t = {norm(r["title"]) for r in base}; seen_a = {r["arxiv_id"].strip() for r in base if r["arxiv_id"].strip()}; seen_k = {r["bibkey"] for r in base}
new = []
for r in csv.DictReader(open(root / "runs/updates" / ym / "screen.csv")):
    assert all(k in r for k in FIELDS), f"screen.csv must have the 16 master columns; got {list(r)}"
    assert r["evidence"].strip()[:1].upper() in ("P", "A") and " " not in r["bibkey"], f"bad row: {r['title'][:60]}"
    if norm(r["title"]) in seen_t or r["arxiv_id"].strip() in seen_a: continue
    if r["bibkey"] in seen_k: r["bibkey"] += "b"
    seen_k.add(r["bibkey"]); seen_t.add(norm(r["title"])); r["source"] = f"update_{ym}"; new.append({k: r.get(k, "") for k in FIELDS + ["source"]})
inc = [r for r in new if r["decision"].lower().startswith("incl")]
with open(run / f"manual_screen_all_v{vout}.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS + ["source"]); w.writeheader(); w.writerows(base + new)
print(f"v{vin} -> v{vout}: {len(new)} screened, {len(inc)} included")
tex = root.parent / ("survey_tex" if (root.parent / "survey_tex").exists() else "paper_tex")
bibs = [b for b in sorted(glob.glob(str(tex / "*.bib"))) if not b.endswith(".full.bib")]
subprocess.run([sys.executable, str(root / "make_bib.py"), "20260916_v3", f"v{vout}", str(tex / f"update_{ym.replace('-', '_')}.bib")] + bibs, check=False)
names = ", ".join(r["title_short"] or r["title"][:40] for r in inc[:6]) + (" and others" if len(inc) > 6 else "")
upd = root / "UPDATES.md"; old = upd.read_text() if upd.exists() else ""
upd.write_text(f"- **{ym}** — {len(inc)} papers added ({names}).\n" + old)
readme = root.parent / "README.md" if (root.parent / "README.md").exists() else root.parent / "release/repo/README.md"
subprocess.run([sys.executable, str(root / "make_readme.py"), str(readme)], check=False)
