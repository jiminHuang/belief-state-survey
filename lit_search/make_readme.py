#!/usr/bin/env python3
"""Regenerate the paper list in the GitHub README from the screening record.
Usage: make_readme.py <run_ts> <version> <README.md>  (keeps text before '## Paper list' and from '## Rerunning' on)."""
import csv, re, sys, pathlib
root = pathlib.Path(__file__).parent; ts, ver, readme = sys.argv[1:4]
rows = [r for r in csv.DictReader(open(root / "runs" / ts / f"manual_screen_all_{ver}.csv")) if r["decision"].lower().startswith("incl")]
old = open(readme).read()
head = old[:old.index("## Paper list")]; tail = old[old.index("## Rerunning"):]
# previous grouping for keyword-run rows: title -> section heading
prev = {}; sec = None
for line in old.splitlines():
    if line.startswith("### "): sec = line[4:].strip()
    m = re.match(r"\| \[(.*?)\]\(", line)
    if m and sec: prev[re.sub(r"[^a-z0-9]", "", m.group(1).lower())] = sec
SEC = {"3": "Belief representation (who maintains the belief)", "4": "Belief revision and failure modes", "5": "Learning signals by credited object",
       "6": "Belief-guided evidence acquisition", "7": "Evaluation and benchmarks"}
ORDER = list(SEC.values()) + ["Other"]
groups = {k: [] for k in ORDER}
for r in rows:
    key = re.sub(r"[^a-z0-9]", "", r["title"].lower())
    if r.get("source", "search") == "search" and key in prev: g = prev[key]
    else:
        s = r["survey_section"].split(";")[0].strip(); g = SEC.get(s, "Other")
    groups.setdefault(g, []).append(r)
n = len(rows); nP = sum(r["evidence"].strip().upper().startswith("P") for r in rows)
out = [f"## Paper list (full-text screened, {n} papers)\n",
       f"Columns: paper, year, who maintains the belief, credited object, evidence level (P = peer-reviewed, A = preprint), source (K = keyword search, S1--S4 = citation-tree round). {nP} papers are peer-reviewed. Entries are grouped by the survey section they support; the complete record with revision signal, metrics, and notes is `lit_search/runs/{ts}/manual_screen_all_{ver}.csv`.\n"]
for g in ORDER:
    rs = sorted(groups.get(g, []), key=lambda r: (r["date"][:4], r["arxiv_id"]))
    if not rs: continue
    out.append(f"### {g}\n"); out.append("| Paper | Year | Belief kept by | Credited | Ev. | Src |"); out.append("|---|---|---|---|---|---|")
    for r in rs:
        a = r["arxiv_id"].strip(); link = f"[{r['title'].strip()}](https://arxiv.org/abs/{a})" if a[:1].isdigit() else r["title"].strip()
        src = "K" if r.get("source", "search") == "search" else "S" + r["source"][-1]
        out.append(f"| {link} | {r['date'][:4]} | {r['who_maintains_belief']} | {r['credited_object']} | {r['evidence'].strip()[:1].upper()} | {src} |")
    out.append("")
open(readme, "w").write(head + "\n".join(out) + "\n" + tail); print(n, "papers,", nP, "peer-reviewed", file=sys.stderr)
