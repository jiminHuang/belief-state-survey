#!/usr/bin/env python3
"""Step 1b (fallback for arXiv API rate limits): second OpenAlex pass restricted to the arXiv source
(OpenAlex source id S4306400194) and to the recent window, sorted by relevance. Same queries as config.json.
Writes runs/<ts>/raw_arxiv.json and counts_search_arxiv.json (same schema as search.py)."""
import json, sys, time, urllib.request, urllib.parse, pathlib
KEY=(pathlib.Path(__file__).parent/".openalex_key").read_text().strip() if (pathlib.Path(__file__).parent/".openalex_key").exists() else None
root = pathlib.Path(__file__).parent; cfg = json.load(open(root / "config.json"))
ts = sys.argv[1]; out = root / "runs" / ts; out.mkdir(parents=True, exist_ok=True)
recent_from = f"{cfg['recent_year']}-01-01"
def abstract(inv):
    if not inv: return ""
    pos = {p: w for w, ps in inv.items() for p in ps}; return " ".join(pos[i] for i in sorted(pos))
res, counts = {}, {"timestamp": ts, "source": "openalex_arxiv_only", "window_from": recent_from, "per_query": [], "raw_hits_total": 0}
for sec, qs in cfg["queries"].items():
    for q in qs:
        params = {"search": q, "filter": f"from_publication_date:{recent_from},primary_location.source.id:S4306400194", "per-page": cfg["per_page"], **({"api_key": KEY} if KEY else {}),
                  "select": "id,title,publication_date,publication_year,cited_by_count,primary_location,abstract_inverted_index,authorships,ids,doi"}
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params); d = {"results": []}
        for attempt in range(3):
            try: d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "lit-survey/0.1"}), timeout=60).read()); break
            except Exception as e: print("retry", q, e, file=sys.stderr); time.sleep(3 * (attempt + 1))
        n = len(d.get("results", [])); counts["per_query"].append({"section": sec, "query": q, "hits": n}); counts["raw_hits_total"] += n
        for p in d.get("results", []):
            pid = p["id"]
            if pid in res: res[pid]["hits"].append([sec, q]); continue
            loc = p.get("primary_location") or {}
            res[pid] = {"id": pid, "doi": p.get("doi"), "title": p.get("title"), "date": p.get("publication_date"), "year": p.get("publication_year"),
                        "cites": p.get("cited_by_count"), "venue": "arXiv", "url": loc.get("landing_page_url"),
                        "authors": [a["author"]["display_name"] for a in (p.get("authorships") or [])[:3]],
                        "abstract": abstract(p.get("abstract_inverted_index")), "hits": [[sec, q]]}
        print(f"{sec} | {q} -> {n} (unique {len(res)})"); time.sleep(0.3)
counts["unique_after_dedup"] = len(res)
json.dump(res, open(out / "raw_arxiv.json", "w"), ensure_ascii=False); json.dump(counts, open(out / "counts_search_arxiv.json", "w"), indent=1)
print("RUN", ts, "arxiv-only raw", counts["raw_hits_total"], "unique", len(res))
