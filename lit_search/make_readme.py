#!/usr/bin/env python3
"""Generate the awesome-list README from the screening record (the README is fully generated; edit this script, not the README).
Usage: make_readme.py <README.md> [<master.csv>]   (default master = newest runs/20260916_v3/manual_screen_all_v*.csv)"""
import csv, re, sys, glob, pathlib, collections
root = pathlib.Path(__file__).parent
readme = sys.argv[1]
master = sys.argv[2] if len(sys.argv) > 2 else sorted(glob.glob(str(root / "runs/20260916_v3/manual_screen_all_v*.csv")), key=lambda p: int(re.search(r"_v(\d+)\.csv", p).group(1)))[-1]
rows = [r for r in csv.DictReader(open(master)) if r["decision"].lower().startswith("incl")]
# real titles, years and arXiv ids from the BibTeX files (the early keyword rows carry short names in `title`)
BIB = {}
for d in ("survey_tex", "paper_tex"):
    for b in glob.glob(str(root.parent / d / "*.bib")):
        if b.endswith(".full.bib"): continue
        txt = open(b).read()
        for m in re.finditer(r"@\w+\{([^,\s]+),", txt):
            key = m.group(1); nxt = txt.find("\n@", m.end()); body = txt[m.end(): nxt if nxt > 0 else len(txt)]
            f = {}
            for fm in re.finditer(r"\b(title|year|eprint|booktitle|journal)\s*=\s*\{", body):
                i = fm.end(); depth = 1; j = i
                while j < len(body) and depth:
                    depth += body[j] == "{"; depth -= body[j] == "}"; j += 1
                f.setdefault(fm.group(1).lower(), body[i:j-1])
            BIB.setdefault(key, f)
def clean(t): return re.sub(r"\s+", " ", re.sub(r"[{}]", "", t)).replace("\\&", "&").strip()
for r in rows:
    b = BIB.get(r["bibkey"])
    if b and b.get("title"):
        real = clean(b["title"])
        if len(real) > len(r["title"].strip()) or r["title"].strip().lower() == r["title_short"].strip().lower(): r["title"] = real
REPO = "https://github.com/jiminHuang/belief-state-survey"
SEC = [("3", "State term", "Where the belief lives and who writes it: context, external stores, probabilistic stores, external Bayesian filters, model-written beliefs, learned world models."),
       ("4", "Transition term", "How the belief is carried across an action and revised: triggers, mechanisms, and the four failure modes (failed stay, update, isolation, act)."),
       ("5", "Likelihood term as a learning signal", "Who scores what the agent produced, and which object the gradient reaches: output, trajectory, interaction, world-model loss, or the belief itself."),
       ("6", "Likelihood term as a choice of evidence", "Systems whose belief decides what to observe next."),
       ("7", "Likelihood term as a metric", "Belief-level evaluation and benchmarks: calibration, accuracy and revision, memory validity, Bayesian coherence, belief-action gap.")]
WHO = {"context": "context", "external memory": "store", "ext. memory": "store", "prob. memory": "probabilistic store", "ext. filter": "external filter", "written": "written", "world model": "world model"}
def norm_who(w):
    w = w.strip().lower()
    for k, v in WHO.items():
        if w.startswith(k): return v
    return ""
def norm_cred(c):
    c = c.strip().lower()
    for k, v in [("none", ""), ("n/a", ""), ("state", "state"), ("belief", "state"), ("interaction (memory", "memory op"), ("memory", "memory op"), ("interaction", "interaction"), ("action", "interaction"), ("trajectory", "trajectory"), ("step", "trajectory"), ("output", "output"), ("outcome", "output"), ("world", "world-model loss"), ("wm", "world-model loss")]:
        if c.startswith(k): return v
    return ""
def entry(r):
    a = r["arxiv_id"].strip(); t = re.sub(r"\s+", " ", r["title"].strip()); name = r["title_short"].strip()
    link = f"[{t}](https://arxiv.org/abs/{a})" if a[:1].isdigit() else t
    venue = r["venue"].strip(); ev = r["evidence"].strip()[:1].upper()
    when = r["date"][:4] + (f", {venue}" if ev == "P" and venue.lower() not in ("", "arxiv") else "")
    tags = [x for x in (f"state: {norm_who(r['who_maintains_belief'])}" if norm_who(r["who_maintains_belief"]) else "", f"credit: {norm_cred(r['credited_object'])}" if norm_cred(r["credited_object"]) else "") if x]
    head = f"**{name}** — " if name and name.lower() != t.lower() else ""
    return f"- {head}{link} ({when})" + ("  " + " ".join(f"`{x}`" for x in tags) if tags else "")
by = collections.defaultdict(list)
for r in rows: by[r["survey_section"].split(";")[0].strip()].append(r)
surveys = [r for r in rows if "survey" in r["role_in_survey"].lower() or re.search(r"\bsurvey\b|\breview\b", (r["title"] + " " + r["title_short"]).lower())]
sk = {id(r) for r in surveys}
AT_A_GLANCE = [("xu2026should", "CBM", "symbolic verifier"), ("singh2026agent", "Agent-BRACE", "calibration target"), ("cui2026distilling", "BOND", "Bayesian teacher"), ("wu2025deltom", "DEL-ToM", "process belief model"),
               ("wang2025vagen", "VAGEN", "simulator state"), ("zou2025t3", "T3", "known hypothesis"), ("wang2025information", "IGPO", "known answer"), ("kong2026infopo", "InfoPO", "known answer"),
               ("hwang2026marbo", "MARBO", "ground-truth roles"), ("jiang2026pabu", "PABU", "teacher labels"), ("liu2026metacognitive", "MMPO", "own answer entropy (proxy)"),
               ("lidayan2025abbel", "ABBEL", "reconstruction of the agent's past observations"), ("lu2026policy", "PaW", "the agent's own next observation (prediction, not a claim)"),
               ("wang2026dark", "Dark Room", "the agent's own next observation (negative result: collapses under GRPO)"), ("tang2026rewarding", "ReBel", "**the agent's own next observation**")]
bk = {r["bibkey"]: r for r in rows}
n = len(rows); nP = sum(r["evidence"].strip().upper().startswith("P") for r in rows)
upd = (root / "UPDATES.md").read_text().strip() if (root / "UPDATES.md").exists() else ""
o = []
o += ["# Awesome Belief-State LLM Agents", "",
      f"[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![papers](https://img.shields.io/badge/papers-{n}-blue) ![updated](https://img.shields.io/badge/updated-monthly-brightgreen)", "",
      "A curated, monthly-updated list of papers on how language-model agents **construct, revise, and test what they believe** between decisions. It is the living companion of the survey",
      "", "> **From Memory to Belief: A Survey of State Maintenance and Belief Revision in LLM Decision Agents**  ",
      "> Jimin Huang, Yuyan Wang, Xueqing Peng, Sophia Ananiadou, Jun'ichi Tsujii. Preprint, 2026. [[PDF]](paper.pdf)", "",
      "A belief has three parts: a **state** (what is believed and how firmly), a **transition** (how it is carried across an action and revised), and a **likelihood** (how the next observation scores it). Every paper is placed by which of the three it supplies and where each comes from: written by the model, fixed by the designer, learned, or absent. Memory research gave agents a state, revision and post-training gave them a transition, and the likelihood is still mostly supplied from outside.", "",
      "## Contents", "", "- [Belief-level learning signals at a glance](#belief-level-learning-signals-at-a-glance)", "- [Surveys](#surveys)"]
o += [f"- [{t}](#{re.sub(r'[^a-z0-9 -]', '', t.lower()).replace(' ', '-')})" for _, t, _ in SEC]
o += ["- [Background](#background)", "- [Updates](#updates)", "- [How the list is maintained](#how-the-list-is-maintained)", "- [Contributing](#contributing)", "- [Citation](#citation)", ""]
o += ["## Belief-level learning signals at a glance", "", "Systems whose training signal reaches the belief itself, by where that signal comes from. The last rows are the ones that take it from the agent's own observations.", "", "| System | Signal comes from | Paper |", "|---|---|---|"]
for k, name, srcs in AT_A_GLANCE:
    if k in bk:
        r = bk[k]; a = r["arxiv_id"].strip(); o.append(f"| {name} | {srcs} | [{re.sub(r'\\s+', ' ', r['title'].strip())}](https://arxiv.org/abs/{a}) ({r['date'][:4]}) |")
NEIGHBOURS = ["zhang2024memory", "hu2025memory", "luo2026storage", "wu2025rewards", "zheng2025prm", "zhang2025landscape", "zhang2026reasoning", "xia2025uncertainty", "lin2026uncertainty", "yehudai2025survey", "gao2025survey", "chen2026horizon", "xu2026llm", "dong2025finance", "li2026bridging"]
have = {r["bibkey"] for r in surveys}
extra = []
for k in NEIGHBOURS:
    b = BIB.get(k)
    if k in have or not b: continue
    a = b.get("eprint", ""); t = clean(b.get("title", k)); link = f"[{t}](https://arxiv.org/abs/{a})" if a[:1].isdigit() else t
    extra.append((b.get("year", ""), f"- {link} ({b.get('year', '')})"))
o += ["", "## Surveys", "", "Neighbouring surveys, each of which supplies one term of the belief (memory: state; uncertainty: confidence on the state; rewards and credit: transition and signal; world models: learned transition and likelihood).", ""]
o += [e for _, e in sorted([(r["date"][:4], entry(r)) for r in surveys] + extra, reverse=True)] + [""]
for code, title, blurb in SEC:
    rs = sorted([r for r in by.get(code, []) if id(r) not in sk], key=lambda r: (r["date"], r["arxiv_id"]), reverse=True)
    o += [f"## {title}", "", blurb, ""]
    year = None
    for r in rs:
        if r["date"][:4] != year:
            year = r["date"][:4]; o += ["", f"### {year}" if False else f"**{year}**", ""]
        o.append(entry(r))
    o.append("")
other = sorted([r for c, rs in by.items() if c not in {s[0] for s in SEC} | {"2"} for r in rs if id(r) not in sk], key=lambda r: r["date"], reverse=True)
o += ["## Background", ""] + [entry(r) for r in other] + [""]
o += ["## Updates", "", upd if upd else "- 2026-09: initial release.", ""]
o += ["## How the list is maintained", "",
      f"The list is generated from a screening record, not edited by hand: `lit_search/runs/20260916_v3/manual_screen_all_v*.csv` ({n} included papers, {nP} peer-reviewed) holds one row per paper with who maintains the belief, the credited object, the revision signal, whether a belief-level metric is reported, and notes. Each month `lit_search/monthly_update.py` runs the keyword queries on OpenAlex and a phrase search on Hugging Face Papers for the new month, applies the same rule screen, and removes everything already seen; the survivors are read in full, coded, merged with `merge_update.py`, and this README is regenerated with `make_readme.py`. The procedure is in [`UPDATE.md`](UPDATE.md); the search protocol behind the survey is in Appendix A of the paper.", "",
      "```bash", "cd lit_search", "echo YOUR_OPENALEX_KEY > .openalex_key      # not committed", "python3 monthly_update.py 2026-10            # candidates for one month", "python3 merge_update.py 2026-10              # after full-text screening", "python3 make_readme.py ../README.md", "```", ""]
o += ["## Contributing", "", "Missing a paper? Open an issue or a pull request with the arXiv link and one line saying which term of the belief it supplies (state, transition, or likelihood) and where that term comes from. Papers are included if they concern a language-model agent and construct, revise, test, learn, or evaluate an explicit state carried between decisions, or document a failure of such a state.", ""]
o += ["## Citation", "", "```bibtex", "@misc{huang2026frommemory,", "  title={From Memory to Belief: A Survey of State Maintenance and Belief Revision in LLM Decision Agents},", "  author={Huang, Jimin and Wang, Yuyan and Peng, Xueqing and Ananiadou, Sophia and Tsujii, Jun'ichi},", "  year={2026},", f"  howpublished={{\\url{{{REPO}}}}},", "  note={Preprint. Zenodo DOI: TBD}", "}", "```", ""]
open(readme, "w").write("\n".join(o)); print(n, "papers,", nP, "peer-reviewed ->", readme, file=sys.stderr)
