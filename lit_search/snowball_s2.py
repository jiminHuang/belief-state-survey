#!/usr/bin/env python3
"""Step 4 (Semantic Scholar variant): citation-tree snowballing from the included papers.
Backward = references of each seed, forward = papers citing each seed, via the S2 Graph API batch endpoint
(500 ids per request). Candidates are restricted to publication year >= cfg date_from, screened with the same
rules as screen.py, deduplicated against everything already screened, and written to
runs/<ts>/snowball_s2_r<k>.csv with per-stage counts in counts_snowball_s2_r<k>.json.
Usage: snowball_s2.py <run_ts> <round> [--seeds file.csv (columns arxiv_id,title)]"""
import json, sys, csv, re, time, pathlib, urllib.request
root = pathlib.Path(__file__).parent
cfg = json.load(open(root / "config.json")); S = cfg["screen"]; YMIN = int(cfg["date_from"][:4])
ts = sys.argv[1]; rnd = int(sys.argv[2]); run = root / "runs" / ts
seedfile = sys.argv[sys.argv.index("--seeds") + 1] if "--seeds" in sys.argv else None
API = "https://api.semanticscholar.org/graph/v1/paper/batch"
nreq = 0
def batch(ids, fields):
    global nreq; out = []
    for i in range(0, len(ids), 500):
        req = urllib.request.Request(API + "?fields=" + fields, data=json.dumps({"ids": ids[i:i+500]}).encode(),
                                     headers={"Content-Type": "application/json", "User-Agent": "lit-survey/0.1"})
        for attempt in range(6):
            try:
                nreq += 1; out += json.loads(urllib.request.urlopen(req, timeout=120).read()); break
            except Exception as e:
                print("retry", i, e, file=sys.stderr); time.sleep(10 * (attempt + 1))
        time.sleep(1.2)
    return out
if seedfile: seeds_in = list(csv.DictReader(open(seedfile)))
else: seeds_in = [r for r in csv.DictReader(open(run / "manual_screen_all_v3.csv")) if r["decision"].lower().startswith("incl")]
seed_ids = [f"ARXIV:{r['arxiv_id'].strip()}" for r in seeds_in if r.get("arxiv_id", "").strip()[:1].isdigit()]
F = "paperId,title,year,externalIds,referenceCount,citationCount,references.paperId,references.year,citations.paperId,citations.year"
seeds = [p for p in batch(seed_ids, F) if p]
seed_pids = {p["paperId"] for p in seeds}
cands = {}
def add(pid, yr, origin):
    if pid in seed_pids or not pid: return
    if yr is not None and yr < YMIN: return
    e = cands.setdefault(pid, {"origin": set(), "from": 0}); e["origin"].add(origin); e["from"] += 1
n_ref = n_cit = 0
for p in seeds:
    for r in p.get("references") or []: n_ref += 1; add(r.get("paperId"), r.get("year"), "backward")
    for c in p.get("citations") or []: n_cit += 1; add(c.get("paperId"), c.get("year"), "forward")
print(f"seeds {len(seeds)}/{len(seed_ids)} refs {n_ref} cites {n_cit} candidates(in window) {len(cands)} requests {nreq}", file=sys.stderr)
# metadata + abstracts for candidates
meta = batch(list(cands.keys()), "paperId,title,abstract,year,publicationDate,venue,citationCount,externalIds,authors")
prior = set()
import glob
for f in ["screened.csv"] + sorted(glob.glob(str(run / "manual_screen_all_v*.csv"))) + sorted(glob.glob(str(run / "snowball_s2_r*.csv"))) + sorted(glob.glob(str(run / "snowball_batch*.csv"))):
    f = run / f if isinstance(f, str) and "/" not in f else pathlib.Path(f)
    if f.exists():
        for r in csv.DictReader(open(f)): prior.add(re.sub(r"[^a-z0-9]", "", (r.get("title") or "").lower()))
c = {"timestamp": ts, "round": rnd, "source": "semantic_scholar", "seeds": len(seeds), "backward_refs_total": n_ref, "forward_cites_total": n_cit,
     "candidates_unique_in_window": len(cands), "already_screened": 0, "excluded_no_abstract": 0, "excluded_I1_not_llm": 0,
     "excluded_E1_offdomain": 0, "excluded_I2_topic": 0, "included": 0, "requests": nreq}
rows = []
for p in meta:
    if not p: continue
    e = cands[p["paperId"]]; title = p.get("title") or ""; ab = p.get("abstract") or ""
    tkey = re.sub(r"[^a-z0-9]", "", title.lower())
    if tkey in prior: c["already_screened"] += 1; continue
    text = (title + " " + ab).lower()
    if len(ab) < S["min_abstract_chars"]: c["excluded_no_abstract"] += 1; continue
    if not any(k in text for k in S["must_any"]): c["excluded_I1_not_llm"] += 1; continue
    if any(k in text for k in S["exclude_any"]): c["excluded_E1_offdomain"] += 1; continue
    topics = [k for k in S["topic_any"] if k in text]
    if len(topics) < S["topic_min"]: c["excluded_I2_topic"] += 1; continue
    score = sum(w for k, w in S["core_weights"].items() if k in text) + len(topics) * 0.5 + min(e["from"], 5) * 1.0
    ex = p.get("externalIds") or {}
    rows.append({"score": round(score, 1), "origin": "+".join(sorted(e["origin"])), "linked_seeds": e["from"], "title": title, "date": p.get("publicationDate"),
                 "year": p.get("year"), "cites": p.get("citationCount"), "venue": p.get("venue") or "", "arxiv_id": ex.get("ArXiv", ""), "doi": ex.get("DOI", ""),
                 "topics": ";".join(topics), "authors": "; ".join(a["name"] for a in (p.get("authors") or [])[:3]), "abstract": ab})
c["included"] = len(rows); c["requests"] = nreq; rows.sort(key=lambda r: (-r["score"], -(r["cites"] or 0)))
c["included_by_year"] = {}
for r in rows: c["included_by_year"][str(r["year"])] = c["included_by_year"].get(str(r["year"]), 0) + 1
c["included_by_origin"] = {}
for r in rows: c["included_by_origin"][r["origin"]] = c["included_by_origin"].get(r["origin"], 0) + 1
with open(run / f"snowball_s2_r{rnd}.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump({k: {"origin": sorted(v["origin"]), "from": v["from"]} for k, v in cands.items()}, open(run / f"snowball_s2_r{rnd}_candidates.json", "w"))
json.dump(c, open(run / f"counts_snowball_s2_r{rnd}.json", "w"), indent=1); print(json.dumps(c, indent=1))
