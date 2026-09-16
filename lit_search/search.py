#!/usr/bin/env python3
"""Step 1: keyword retrieval from OpenAlex. Reproducible: same config -> same query set; results are
snapshotted with a timestamp under runs/<ts>/raw.json plus per-query hit counts in runs/<ts>/counts_search.json."""
import json, sys, time, urllib.request, urllib.parse, datetime, pathlib
KEY=(pathlib.Path(__file__).parent/".openalex_key").read_text().strip() if (pathlib.Path(__file__).parent/".openalex_key").exists() else None
cfg = json.load(open(pathlib.Path(__file__).parent / "config.json"))
ts = sys.argv[1] if len(sys.argv) > 1 else datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
out = pathlib.Path(__file__).parent / "runs" / ts; out.mkdir(parents=True, exist_ok=True)

def abstract(inv):
    if not inv: return ""
    pos = {p: w for w, ps in inv.items() for p in ps}
    return " ".join(pos[i] for i in sorted(pos))

res, counts = {}, {"timestamp": ts, "source": "openalex", "per_query": [], "raw_hits_total": 0}
for sec, qs in cfg["queries"].items():
    for q in qs:
        params = {"search": q, "filter": f"from_publication_date:{cfg['date_from']},type:" + "|".join(cfg["types"]),
                  "per-page": cfg["per_page"], **({"api_key": KEY} if KEY else {}), "select": "id,title,publication_date,publication_year,cited_by_count,primary_location,abstract_inverted_index,authorships,ids,doi"}
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
        d = {"results": []}
        for attempt in range(3):
            try:
                d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "lit-survey/0.1"}), timeout=60).read()); break
            except Exception as e:
                print("retry", q, e, file=sys.stderr); time.sleep(3 * (attempt + 1))
        n = len(d.get("results", [])); counts["per_query"].append({"section": sec, "query": q, "hits": n}); counts["raw_hits_total"] += n
        for p in d.get("results", []):
            pid = p["id"]
            if pid in res: res[pid]["hits"].append([sec, q]); continue
            loc = p.get("primary_location") or {}; src = loc.get("source") or {}
            res[pid] = {"id": pid, "doi": p.get("doi"), "title": p.get("title"), "date": p.get("publication_date"), "year": p.get("publication_year"),
                        "cites": p.get("cited_by_count"), "venue": src.get("display_name"), "url": loc.get("landing_page_url"),
                        "authors": [a["author"]["display_name"] for a in (p.get("authorships") or [])[:3]],
                        "abstract": abstract(p.get("abstract_inverted_index")), "hits": [[sec, q]]}
        print(f"{sec} | {q} -> {n} (unique so far {len(res)})"); time.sleep(0.3)
counts["unique_after_dedup"] = len(res)
json.dump(res, open(out / "raw.json", "w"), ensure_ascii=False, indent=0)
json.dump(counts, open(out / "counts_search.json", "w"), indent=1)
json.dump(cfg, open(out / "config_snapshot.json", "w"), indent=1)
print("RUN", ts, "raw", counts["raw_hits_total"], "unique", len(res))
