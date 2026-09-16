#!/usr/bin/env python3
"""Step 6: build BibTeX entries for included papers that have no entry in the survey bibs yet.
Usage: make_bib.py <run_ts> <version> <out.bib> <existing.bib>...  (arXiv API id_list, 25 ids per call)"""
import csv, re, sys, time, html, pathlib, urllib.request
root = pathlib.Path(__file__).parent; ts, ver, out = sys.argv[1:4]; existing = sys.argv[4:]
have = set()
for b in existing:
    have |= set(re.findall(r"@\w+\{([^,]+),", open(b).read()))
    have |= set(re.findall(r"eprint=\{(\d{4}\.\d{4,5})\}", open(b).read()))
rows = [r for r in csv.DictReader(open(root / "runs" / ts / f"manual_screen_all_{ver}.csv")) if r["decision"].lower().startswith("incl")]
todo = [r for r in rows if r["bibkey"] not in have and r["arxiv_id"].strip() not in have and r["arxiv_id"].strip()[:1].isdigit()]
print(len(rows), "included;", len(todo), "need bib entries", file=sys.stderr)
meta = {}
ids = [r["arxiv_id"].strip() for r in todo]
for i in range(0, len(ids), 25):
    url = "https://export.arxiv.org/api/query?id_list=" + ",".join(ids[i:i+25]) + "&max_results=25"
    for attempt in range(4):
        try:
            x = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "lit-survey/0.1"}), timeout=60).read().decode(); break
        except Exception as e: print("retry", i, e, file=sys.stderr); time.sleep(15 * (attempt + 1))
    for ent in re.findall(r"<entry>(.*?)</entry>", x, re.S):
        aid = re.search(r"<id>http://arxiv.org/abs/([^v<]+)", ent).group(1)
        meta[aid] = {"title": html.unescape(re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", ent, re.S).group(1))).strip(),
                     "authors": [html.unescape(a) for a in re.findall(r"<name>(.*?)</name>", ent)],
                     "year": re.search(r"<published>(\d{4})", ent).group(1)}
    time.sleep(3.5)
def tex(s): return s.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
def prot(t): return re.sub(r"\b([A-Z][A-Za-z0-9\-]*[A-Z0-9][A-Za-z0-9\-]*|[A-Z]{2,})\b", r"{\1}", t)
ents = []
for r in todo:
    m = meta.get(r["arxiv_id"].strip())
    if not m: print("MISSING", r["arxiv_id"], r["title"][:60], file=sys.stderr); continue
    v = r["venue"].strip(); ev = r["evidence"].strip()
    pub = v if (ev.upper().startswith("P") and v.lower() not in ("arxiv", "")) else ""
    ents.append("@%s{%s,\n  title={%s},\n  author={%s},\n  year={%s},\n  %s\n  eprint={%s},\n  archivePrefix={arXiv}\n}" % (
        "inproceedings" if pub else "article", r["bibkey"], tex(prot(m["title"])), " and ".join(m["authors"]), m["year"],
        ("booktitle={%s}," % tex(pub)) if pub else "journal={arXiv preprint arXiv:%s}," % r["arxiv_id"].strip(), r["arxiv_id"].strip()))
open(out, "w").write("\n\n".join(ents) + "\n"); print(len(ents), "entries written to", out, file=sys.stderr)
