#!/usr/bin/env python3
"""Step 7: regenerate the appendix master table (all included papers with a bib entry) from the screening record.
Usage: make_master.py <run_ts> <version> <out.tex> <bib files...>"""
import csv, re, sys, pathlib
root = pathlib.Path(__file__).parent; ts, ver, out = sys.argv[1:4]
keys = set()
for b in sys.argv[4:]: keys |= set(re.findall(r"@\w+\{([^,\s]+),", open(b).read()))
rows = [r for r in csv.DictReader(open(root / "runs" / ts / f"manual_screen_all_{ver}.csv")) if r["decision"].lower().startswith("incl")]
def tex(s): return s.replace("\\", "/").replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#").replace("$", "\\$").replace("^", "\\textasciicircum{}").replace("~", "\\textasciitilde{}").replace("<", "\\textless{}").replace(">", "\\textgreater{}").replace("|", "\\textbar{}")
WHO = {"context": "context", "context (free-form trace)": "context", "external memory": "ext. memory", "prob. memory": "prob. memory", "ext. filter": "ext. filter", "written": "written", "model-written": "written", "world model": "world model", "learned world model": "world model", "n/a": "--", "": "--"}
CRED = {"output": "output", "trajectory": "trajectory", "interaction (action)": "interaction", "interaction (memory op)": "memory op", "interaction": "interaction", "action/turn": "interaction", "memory op": "memory op", "state": "state", "belief state": "state", "world-model loss": "WM loss", "wm loss": "WM loss", "none": "--", "n/a": "--", "": "--"}
def short(t, n=38):
    t = re.sub(r"\s+", " ", t.strip()); return tex(t) if len(t) <= n else tex(t[:n-1].rstrip()) + "\\ldots"
def metric(m):
    m = m.strip().lower(); return "\\cmark" if m.startswith("yes") else ("\\pmark" if m.startswith("proxy") else "")
rows.sort(key=lambda r: (r["date"][:4], r["first_author"].split()[-1].lower() if r["first_author"] else ""))
lines = []; missing = []
for r in rows:
    if r["bibkey"] not in keys: missing.append(r["bibkey"]); continue
    wk = r["who_maintains_belief"].strip().lower()
    PW = [("evaluator", "--"), ("n/a", "--"), ("external bayes", "ext. filter"), ("external poster", "ext. filter"), ("pomdp", "ext. filter"), ("ext. filter", "ext. filter"), ("model-written", "written"), ("written", "written"), ("learned", "world model"), ("world model", "world model"), ("prob", "prob. memory"), ("external", "ext. memory"), ("inherited", "ext. memory"), ("context", "context")]
    who = next((v for k, v in PW if wk.startswith(k)), None) or WHO.get(wk, short(r["who_maintains_belief"], 16))
    ck = r["credited_object"].strip().lower()
    PC = [("none", "--"), ("n/a", "--"), ("step", "trajectory"), ("belief", "state"), ("state", "state"), ("outcome", "output"), ("output", "output"), ("action", "interaction"), ("interaction (memory", "memory op"), ("memory", "memory op"), ("interaction", "interaction"), ("trajectory", "trajectory"), ("world", "WM loss"), ("wm", "WM loss")]
    cred = next((v for k, v in PC if ck.startswith(k)), None) or CRED.get(ck, short(r["credited_object"], 14))
    lines.append(f"{short(r['title_short'] or r['title'], 34)} \\citep{{{r['bibkey']}}} & {r['date'][:4]} & {who} & {cred} & {short(r['revision_signal'], 40)} & {metric(r['belief_level_metrics'])} \\\\")
N = 52
chunks = [lines[i:i+N] for i in range(0, len(lines), N)]
o = []
for i, ch in enumerate(chunks):
    o.append("\\begin{table*}[t]\n\\centering\\tiny\n\\setlength{\\tabcolsep}{2.5pt}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{lcllll}\n\\toprule\nSystem & Year & State kept by & Credited & Revision trigger & Metric \\\\\n\\midrule\n" + "\n".join(ch) +
             "\n\\bottomrule\n\\end{tabular}}\n\\caption{" + ("Every paper included after full-text reading, ordered by year and first author" if i == 0 else f"Master table, continued ({i+1}/{len(chunks)})") +
             ". \\emph{Metric}: \\cmark\\ belief-level metric reported, \\pmark\\ proxy only.}\n\\label{tab:masterfull" + ("" if i == 0 else str(i+1)) + "}\n\\end{table*}\n")
open(out, "w").write("\n".join(o)); print(len(lines), "rows in", len(chunks), "tables;", len(missing), "without bib entry:", missing[:10], file=sys.stderr)
