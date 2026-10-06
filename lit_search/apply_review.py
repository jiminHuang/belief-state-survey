#!/usr/bin/env python3
"""Step 9: apply the author's coding check (review_site/reviews.json) to the screening record.
Usage: apply_review.py <run_ts> <in_ver> <out_ver>
- include_ok == "no"  -> decision becomes "exclude: author check"
- <field>_ok == "no"  -> the field takes <field>_fix (who/cred/rev/metric)
- adds columns: author_check (done / corrected: ...), own_obs_test (criterion below)
own_obs_test = "yes" if the paper tests a belief the agent writes against observations the agent itself
receives in the episode, with no oracle, simulator state, or teacher; "yes-preLLM" for such a system that
is not a language-model agent; otherwise "no". Set from OWN_OBS below (decided per paper; the author's
key-claim answers in reviews.json are kept in author_own_obs)."""
import csv, json, sys, pathlib
root = pathlib.Path(__file__).parent; ts, vin, vout = sys.argv[1:4]
OWN_OBS = {"tang2026rewarding": "yes", "lidayan2025abbel": "yes"}  # author ruling 2026-10-04, checked against the full text
VENUE = {"xu2026should": ("P: EMNLP 2026", "EMNLP 2026")}  # accepted after screening (arXiv comment, checked 2026-10-06)
FIX = {"who": "who_maintains_belief", "cred": "credited_object", "rev": "revision_signal", "metric": "belief_level_metrics"}
rev = json.load(open(root.parent / "review_site" / "reviews.json"))
src = root / "runs" / ts / f"manual_screen_all_{vin}.csv"
rows = list(csv.DictReader(open(src))); fn = list(rows[0].keys()) + ["author_check", "author_own_obs", "own_obs_test"]
stats = {"checked": 0, "excluded": [], "changed": []}
for r in rows:
    r["own_obs_test"] = OWN_OBS.get(r["bibkey"], "no"); r["author_check"] = ""; r["author_own_obs"] = ""
    if r["bibkey"] in VENUE: r["evidence"], r["venue"] = VENUE[r["bibkey"]]
    if not r["decision"].lower().startswith("incl"): continue
    j = rev.get(r["bibkey"])
    if not j or j.get("status") != "done": r["author_check"] = "not checked"; continue
    stats["checked"] += 1; notes = []
    if j.get("include_ok") == "no":
        r["decision"] = "exclude: author check"; notes.append("excluded"); stats["excluded"].append(r["bibkey"])
    for f, col in FIX.items():
        if j.get(f + "_ok") == "no" and j.get(f + "_fix"):
            notes.append(f"{col}: {r[col]} -> {j[f+'_fix']}"); r[col] = j[f + "_fix"]; stats["changed"].append((r["bibkey"], col))
    r["author_own_obs"] = j.get("own_obs") or ""
    r["author_check"] = "corrected: " + "; ".join(notes) if notes else "done"
out = root / "runs" / ts / f"manual_screen_all_{vout}.csv"
w = csv.DictWriter(open(out, "w", newline=""), fieldnames=fn); w.writeheader(); w.writerows(rows)
inc = [r for r in rows if r["decision"].lower().startswith("incl")]
print(json.dumps({**stats, "included_after": len(inc), "peer_reviewed": sum(r["evidence"].strip()[:1].upper() == "P" for r in inc),
                  "own_obs_yes": [r["bibkey"] for r in inc if r["own_obs_test"].startswith("yes")]}, indent=1))
