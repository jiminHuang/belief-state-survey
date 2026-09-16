#!/usr/bin/env python3
"""Step 1c: curated seed list for the 2020-2024 window. Keyword search over-weights generic LLM papers for
these years, so the foundations are enumerated by title and resolved through OpenAlex (venue, year, cites, ids).
Writes runs/<ts>/curated_2020_2024.csv. Titles come from config 'curated_titles'."""
import json, sys, csv, time, urllib.request, urllib.parse, pathlib
root=pathlib.Path(__file__).parent; KEY=(root/".openalex_key").read_text().strip()
ts=sys.argv[1]; cfg=json.load(open(root/"config.json"))
def abstract(inv):
    if not inv: return ""
    pos={p:w for w,ps in inv.items() for p in ps}; return " ".join(pos[i] for i in sorted(pos))
rows=[]
for t in cfg[sys.argv[2] if len(sys.argv)>2 else "curated_titles"]:
    url="https://api.openalex.org/works?"+urllib.parse.urlencode({"search":t,"per-page":3,"api_key":KEY,"select":"id,title,publication_year,publication_date,cited_by_count,primary_location,doi,ids,abstract_inverted_index,authorships"})
    try: d=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"lit-survey/0.1"}),timeout=40).read())
    except Exception as e: print("ERR",t,e,file=sys.stderr); continue
    best=None
    for r in d.get("results",[]):
        if r["title"] and t.lower().split(":")[0][:25] in r["title"].lower(): best=r; break
    if not best and d.get("results"): best=d["results"][0]
    if not best: print("MISS",t); continue
    loc=best.get("primary_location") or {}; src=loc.get("source") or {}
    rows.append({"query_title":t,"title":best["title"],"year":best.get("publication_year"),"date":best.get("publication_date"),"cites":best.get("cited_by_count"),
                 "venue":src.get("display_name"),"doi":best.get("doi"),"url":loc.get("landing_page_url"),"authors":"; ".join(a["author"]["display_name"] for a in (best.get("authorships") or [])[:3]),
                 "abstract":abstract(best.get("abstract_inverted_index"))[:600]})
    time.sleep(0.2)
out=root/"runs"/ts/(sys.argv[3] if len(sys.argv)>3 else "curated_2020_2024.csv")
with open(out,"w",newline="") as f: w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("resolved",len(rows),"of",len(cfg[sys.argv[2] if len(sys.argv)>2 else "curated_titles"]))
for r in rows: print(f"{r['year']} c={r['cites']:>5} {str(r['venue'])[:28]:<28} | {r['title'][:70]} | {(r['doi'] or r['url'] or '')[-32:]}")
