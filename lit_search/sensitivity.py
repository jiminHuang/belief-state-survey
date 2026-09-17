#!/usr/bin/env python3
"""Step 8: peer-reviewed-subset sensitivity table for the five insight boxes.
Usage: sensitivity.py <run_ts> <version> <out.tex>"""
import csv, pathlib, sys
root = pathlib.Path(__file__).parent; ts, ver, out = sys.argv[1:4]
rows = [r for r in csv.DictReader(open(root / "runs" / ts / f"manual_screen_all_{ver}.csv")) if r["decision"].lower().startswith("incl")]
P = [r for r in rows if r["evidence"].strip()[:1].upper() == "P"]
def sec(r, k): return k in [s.strip() for s in r["survey_section"].split(";")]
def cnt(pred): return len([r for r in rows if pred(r)]), len([r for r in P if pred(r)])
def who(r, k): return r["who_maintains_belief"].strip().lower().startswith(k)
def cred(r, k): return r["credited_object"].strip().lower().startswith(k)
def metric_yes(r): return r["belief_level_metrics"].strip().lower().startswith("yes")
def own_obs(r): return cred(r, "state") and any(w in (r["revision_signal"] + " " + r["note"]).lower() for w in ["own observation", "own prediction", "next observation", "self-supervised likelihood"])
items = [
 ("1", "Structure is not testability", "state term written / filter / world model", [cnt(lambda r: who(r,"written")), cnt(lambda r: who(r,"ext. filter") or who(r,"external bayes") or who(r,"external poster") or who(r,"pomdp")), cnt(lambda r: who(r,"world") or who(r,"learned"))]),
 ("2", "Revision is triggered, not routed", "revision papers (\\S\\ref{sec:revision})", [cnt(lambda r: sec(r,"4"))]),
 ("3", "Credit has been getting denser, not deeper", "credited: interaction / state / state by own obs.", [cnt(lambda r: cred(r,"interaction")), cnt(lambda r: cred(r,"state")), cnt(own_obs)]),
 ("4", "Acquisition is a belief problem", "acquisition papers (\\S\\ref{sec:evidence})", [cnt(lambda r: sec(r,"6"))]),
 ("5", "Belief cannot be scored by outcome", "papers with a belief-level metric", [cnt(metric_yes)]),
]
o = ["\\begin{table}[h]", "\\centering\\scriptsize", "\\setlength{\\tabcolsep}{3pt}", "\\begin{tabular}{@{}clrr@{}}", "\\toprule",
     "\\# & Counts the insight rests on & All & P only \\\\", "\\midrule"]
for n, title, what, cs in items:
    o.append(f"{n} & {what} & {' / '.join(str(a) for a,_ in cs)} & {' / '.join(str(p) for _,p in cs)} \\\\")
o += ["\\bottomrule", "\\end{tabular}",
      "\\caption{Sensitivity of the five insights to preprint reliance: the counts each rests on, over all included papers and over the peer-reviewed subset alone. Every insight is a claim about a proportion or an absence, and each holds in the same direction on the peer-reviewed subset; the cell for state credit signed by the agent's own observation holds one paper, a preprint, in both.}",
      "\\label{tab:sensitivity}", "\\end{table}"]
open(out, "w").write("\n".join(o) + "\n")
for n, title, what, cs in items: print(n, title, what, cs, file=sys.stderr)
