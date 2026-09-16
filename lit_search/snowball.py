#!/usr/bin/env python3
"""Step 4: citation-tree snowballing (backward = references of included papers, forward = papers citing them)
via OpenAlex, screened with the same rules as screen.py. Usage: snowball.py <run_ts> <round> [--seeds seeds.csv]
Round 1 seeds = the included rows of runs/<ts>/manual_screen_all_v3.csv (arXiv ids); later rounds seed from the
previous round's newly included set. Writes runs/<ts>/snowball_r<k>_{seeds,candidates}.json, snowball_r<k>.csv and
counts_snowball_r<k>.json (per-stage numbers for the paper)."""
import json, sys, csv, re, time, pathlib, urllib.request, urllib.parse, datetime
root = pathlib.Path(__file__).parent
KEY = (root / ".openalex_key").read_text().strip() if (root / ".openalex_key").exists() else None
cfg = json.load(open(root / "config.json")); S = cfg["screen"]
ts = sys.argv[1]; rnd = int(sys.argv[2]); run = root / "runs" / ts
seedfile = sys.argv[sys.argv.index("--seeds") + 1] if "--seeds" in sys.argv else None
SEL = "id,title,publication_date,publication_year,cited_by_count,primary_location,abstract_inverted_index,authorships,ids,doi,referenced_works"
nreq = 0
def get(params):
    global nreq
    p = dict(params); p.update({"api_key": KEY} if KEY else {}); url = "https://api.openalex.org/works?" + urllib.parse.urlencode(p)
    for attempt in range(4):
        try:
            nreq += 1
            return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "lit-survey/0.1"}), timeout=90).read())
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(4 * (attempt + 1))
    return {"results": []}
def abstract(inv):
    if not inv: return ""
    pos = {p: w for w, ps in inv.items() for p in ps}
    return " ".join(pos[i] for i in sorted(pos))
def rec(p, origin):
    loc = p.get("primary_location") or {}; src = loc.get("source") or {}
    return {"id": p["id"], "doi": p.get("doi"), "title": p.get("title"), "date": p.get("publication_date"), "year": p.get("publication_year"),
            "cites": p.get("cited_by_count"), "venue": src.get("display_name"), "url": loc.get("landing_page_url"),
            "authors": [a["author"]["display_name"] for a in (p.get("authorships") or [])[:3]],
            "abstract": abstract(p.get("abstract_inverted_index")), "refs": p.get("referenced_works") or [], "origin": origin}
# ---- 1. resolve seeds to OpenAlex works
if seedfile:
    seeds_in = [r for r in csv.DictReader(open(seedfile))]
else:
    seeds_in = [r for r in csv.DictReader(open(run / "manual_screen_all_v3.csv")) if r["decision"].lower().startswith("incl")]
seeds = {}
def add_seed(p, key):
    seeds[p["id"]] = rec(p, "seed"); seeds[p["id"]]["seed_key"] = key
ax = [r for r in seeds_in if r.get("arxiv_id", "").strip()[:1].isdigit()]
for i in range(0, len(ax), 40):
    chunk = ax[i:i+40]
    dois = "|".join(f"https://doi.org/10.48550/arxiv.{r['arxiv_id'].strip()}" for r in chunk)
    d = get({"filter": f"doi:{dois}", "per-page": 50, "select": SEL})
    got = {(p.get("doi") or "").lower(): p for p in d.get("results", [])}
    for r in chunk:
        p = got.get(f"https://doi.org/10.48550/arxiv.{r['arxiv_id'].strip()}".lower())
        if p: add_seed(p, r["arxiv_id"])
# title fallback for unresolved
unresolved = [r for r in seeds_in if r.get("arxiv_id", "") not in {v["seed_key"] for v in seeds.values()}]
for r in unresolved:
    t = re.sub(r"[^\w\s]", " ", r.get("title") or r.get("title_short") or "")[:200]
    d = get({"filter": f'title.search:{t}', "per-page": 3, "select": SEL})
    for p in d.get("results", []):
        if re.sub(r"[^a-z0-9]", "", (p.get("title") or "").lower())[:60] == re.sub(r"[^a-z0-9]", "", t.lower())[:60]:
            add_seed(p, r.get("arxiv_id") or t); break
print(f"seeds resolved {len(seeds)}/{len(seeds_in)}; requests {nreq}", file=sys.stderr)
# ---- 2. backward: references of seeds
ref_ids = sorted({w for s in seeds.values() for w in s["refs"]})
cands = {}
for i in range(0, len(ref_ids), 50):
    ids = "|".join(x.rsplit("/", 1)[-1] for x in ref_ids[i:i+50])
    d = get({"filter": f"openalex_id:{ids},from_publication_date:{cfg['date_from']}", "per-page": 50, "select": SEL})
    for p in d.get("results", []):
        if p["id"] in seeds: continue
        cands.setdefault(p["id"], rec(p, "backward"))["from"] = cands.get(p["id"], {}).get("from", 0) + 1
n_back = len(cands); print(f"backward refs {len(ref_ids)} -> in-window candidates {n_back}; requests {nreq}", file=sys.stderr)
# ---- 3. forward: works citing each seed
n_fwd_raw = 0
for sid, s in seeds.items():
    wid = sid.rsplit("/", 1)[-1]; page = 1
    while page <= 5:
        d = get({"filter": f"cites:{wid},from_publication_date:{cfg['date_from']}", "per-page": 200, "page": page, "select": SEL, "sort": "cited_by_count:desc"})
        res = d.get("results", []); n_fwd_raw += len(res)
        for p in res:
            if p["id"] in seeds: continue
            if p["id"] in cands:
                cands[p["id"]]["from"] += 1
                if cands[p["id"]]["origin"] == "backward": cands[p["id"]]["origin"] = "both"
            else:
                cands[p["id"]] = rec(p, "forward"); cands[p["id"]]["from"] = 1
        if len(res) < 200: break
        page += 1
    time.sleep(0.15)
print(f"forward raw {n_fwd_raw}; candidates total {len(cands)}; requests {nreq}", file=sys.stderr)
# ---- 4. rule screen (identical to screen.py) and dedup against prior screened set
prior = set()
for f in ["screened.csv", "manual_screen_all_v3.csv"]:
    if (run / f).exists():
        for r in csv.DictReader(open(run / f)): prior.add(re.sub(r"[^a-z0-9]", "", (r.get("title") or "").lower()))
c = {"timestamp": ts, "round": rnd, "seeds": len(seeds), "backward_refs_total": len(ref_ids), "backward_candidates_in_window": n_back,
     "forward_raw_hits": n_fwd_raw, "candidates_unique": len(cands), "already_screened_by_keyword_search": 0,
     "excluded_no_abstract": 0, "excluded_I1_not_llm": 0, "excluded_E1_offdomain": 0, "excluded_I2_topic": 0, "included": 0, "requests": nreq}
rows = []
for p in cands.values():
    tkey = re.sub(r"[^a-z0-9]", "", (p["title"] or "").lower())
    if tkey in prior: c["already_screened_by_keyword_search"] += 1; continue
    text = ((p["title"] or "") + " " + (p["abstract"] or "")).lower()
    if len(p["abstract"] or "") < S["min_abstract_chars"]: c["excluded_no_abstract"] += 1; continue
    if not any(k in text for k in S["must_any"]): c["excluded_I1_not_llm"] += 1; continue
    if any(k in text for k in S["exclude_any"]): c["excluded_E1_offdomain"] += 1; continue
    topics = [k for k in S["topic_any"] if k in text]
    if len(topics) < S["topic_min"]: c["excluded_I2_topic"] += 1; continue
    score = sum(w for k, w in S["core_weights"].items() if k in text) + len(topics) * 0.5 + min(p["from"], 5) * 1.0
    rows.append({"score": round(score, 1), "origin": p["origin"], "linked_seeds": p["from"], "title": p["title"], "date": p["date"], "year": p["year"],
                 "cites": p["cites"], "venue": p["venue"] or "", "topics": ";".join(topics), "url": p["url"] or p["doi"] or p["id"],
                 "authors": "; ".join(p["authors"]), "abstract": p["abstract"]})
c["included"] = len(rows); rows.sort(key=lambda r: (-r["score"], -(r["cites"] or 0)))
c["included_by_year"] = {}
for r in rows: c["included_by_year"][str(r["year"])] = c["included_by_year"].get(str(r["year"]), 0) + 1
json.dump(seeds, open(run / f"snowball_r{rnd}_seeds.json", "w"), indent=0)
json.dump(cands, open(run / f"snowball_r{rnd}_candidates.json", "w"), indent=0)
with open(run / f"snowball_r{rnd}.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(c, open(run / f"counts_snowball_r{rnd}.json", "w"), indent=1); print(json.dumps(c, indent=1))
