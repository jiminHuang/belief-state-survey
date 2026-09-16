#!/usr/bin/env python3
"""Step 1b: keyword retrieval from the arXiv API (main venue for 2025-26 agent work). Same config queries.
Respects arXiv's rate limit (>=3s between calls). Appends to runs/<ts>/raw_arxiv.json + counts_search_arxiv.json."""
import json, sys, time, urllib.request, urllib.parse, re, html, pathlib, datetime
root = pathlib.Path(__file__).parent; cfg = json.load(open(root / "config.json"))
ts = sys.argv[1]; out = root / "runs" / ts; out.mkdir(parents=True, exist_ok=True)
res, counts = {}, {"timestamp": ts, "source": "arxiv", "per_query": [], "raw_hits_total": 0, "max_results": cfg["per_page"]}
def get(url):
    for attempt in range(5):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "lit-survey/0.1"}), timeout=60).read().decode()
        except Exception as e: print("retry", e, file=sys.stderr); time.sleep(15 * (attempt + 1))
    return ""
for sec, qs in cfg["queries"].items():
    for q in qs:
        terms = " AND ".join(f'all:"{t}"' if " " in t else f"all:{t}" for t in [q])  # phrase-free: use all:word AND ...
        terms = " AND ".join(f"all:{w}" for w in re.findall(r"[a-zA-Z\-]+", q))
        url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": terms, "start": 0, "max_results": cfg["per_page"], "sortBy": "submittedDate", "sortOrder": "descending"})
        x = get(url); entries = re.findall(r"<entry>(.*?)</entry>", x, re.S); n = 0
        for e in entries:
            aid = re.search(r"<id>(.*?)</id>", e).group(1).strip(); pub = re.search(r"<published>(.*?)</published>", e).group(1)[:10]
            if pub < cfg["date_from"]: continue
            n += 1
            if aid in res: res[aid]["hits"].append([sec, q]); continue
            t = html.unescape(re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", e, re.S).group(1))).strip()
            ab = html.unescape(re.sub(r"\s+", " ", re.search(r"<summary>(.*?)</summary>", e, re.S).group(1))).strip()
            au = re.findall(r"<name>(.*?)</name>", e)[:3]
            res[aid] = {"id": aid, "doi": None, "title": t, "date": pub, "year": int(pub[:4]), "cites": None, "venue": "arXiv", "url": aid, "authors": au, "abstract": ab, "hits": [[sec, q]]}
        counts["per_query"].append({"section": sec, "query": q, "hits_in_window": n, "returned": len(entries)}); counts["raw_hits_total"] += n
        print(f"{sec} | {q} -> {n}/{len(entries)} (unique {len(res)})"); time.sleep(4.0)
counts["unique_after_dedup"] = len(res)
json.dump(res, open(out / "raw_arxiv.json", "w"), ensure_ascii=False); json.dump(counts, open(out / "counts_search_arxiv.json", "w"), indent=1)
print("RUN", ts, "arxiv raw", counts["raw_hits_total"], "unique", len(res))
