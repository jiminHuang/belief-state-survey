#!/usr/bin/env python3
"""Step 5: merge full-text-screened snowball batches into the master screening record.
Usage: merge_snowball.py <run_ts> <round> <in_version> <out_version>
Reads runs/<ts>/snowball_screen_b*.csv (round k), appends to manual_screen_all_<in>.csv -> manual_screen_all_<out>.csv,
adds column `source` (search | snowball_r<k>) and writes counts_snowball_merge_r<k>.json + a seed file for the next round."""
import csv, json, sys, re, glob, pathlib
root = pathlib.Path(__file__).parent; ts, rnd, vin, vout = sys.argv[1:5]; run = root / "runs" / ts
FIELDS = "arxiv_id,date,title_short,decision,who_maintains_belief,credited_object,revision_signal,belief_level_metrics,survey_section,role_in_survey,note,bibkey,first_author,title,venue,evidence".split(",")
norm = lambda t: re.sub(r"[^a-z0-9]", "", (t or "").lower())
base = list(csv.DictReader(open(run / f"manual_screen_all_{vin}.csv")))
for r in base: r.setdefault("source", "search")
seen_t = {norm(r["title"]) for r in base}; seen_a = {r["arxiv_id"].strip() for r in base if r["arxiv_id"].strip()}
seen_k = {r["bibkey"] for r in base}
new, dup, counts = [], 0, {"round": int(rnd), "batches": {}, "screened": 0, "included": 0, "duplicates_of_base": 0, "peer_reviewed_included": 0}
for f in sorted(glob.glob(str(run / ("snowball_screen_b*.csv" if int(rnd)==1 else f"snowball_r{rnd}_screen_b*.csv")))):
    rows = list(csv.DictReader(open(f))); inc = 0
    for r in rows:
        counts["screened"] += 1
        if norm(r["title"]) in seen_t or (r["arxiv_id"].strip() and r["arxiv_id"].strip() in seen_a): dup += 1; continue
        seen_t.add(norm(r["title"]))
        if not r["decision"].lower().startswith("incl"): continue
        inc += 1
        if r["bibkey"] in seen_k: r["bibkey"] += "b"
        seen_k.add(r["bibkey"])
        r["source"] = f"snowball_r{rnd}"; new.append({k: r.get(k, "") for k in FIELDS + ["source"]})
    counts["batches"][pathlib.Path(f).name] = {"rows": len(rows), "included_new": inc}
counts["included"] = len(new); counts["duplicates_of_base"] = dup
counts["peer_reviewed_included"] = sum(r["evidence"].strip().upper().startswith("P") for r in new)
by = {}
for r in new: by[r["date"][:4]] = by.get(r["date"][:4], 0) + 1
counts["included_by_year"] = dict(sorted(by.items()))
by = {}
for r in new: by[r["credited_object"]] = by.get(r["credited_object"], 0) + 1
counts["included_by_credited_object"] = by
by = {}
for r in new: by[r["role_in_survey"]] = by.get(r["role_in_survey"], 0) + 1
counts["included_by_role"] = by
out = base + new
with open(run / f"manual_screen_all_{vout}.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS + ["source"]); w.writeheader(); w.writerows(out)
with open(run / f"seeds_r{int(rnd)+1}.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["arxiv_id", "title"]); w.writeheader()
    w.writerows([{"arxiv_id": r["arxiv_id"], "title": r["title"]} for r in new if r["arxiv_id"].strip()[:1].isdigit()])
counts["total_included_after_merge"] = sum(r["decision"].lower().startswith("incl") for r in out)
counts["new_inclusion_rate_vs_seeds"] = round(len(new) / max(1, sum(r["decision"].lower().startswith("incl") for r in base)), 3)
json.dump(counts, open(run / f"counts_snowball_merge_r{rnd}.json", "w"), indent=1); print(json.dumps(counts, indent=1))
