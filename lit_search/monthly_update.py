#!/usr/bin/env python3
"""Monthly update, step 1: candidates for one calendar month.
Runs every keyword query of config.json on OpenAlex restricted to the month, plus a phrase search on Hugging Face Papers,
applies the same rule screen as screen.py, removes everything already screened, and writes
runs/updates/<YYYY-MM>/candidates.csv (+ counts.json). Full-text screening of the candidates is step 2 (see UPDATE.md).
Usage: monthly_update.py <YYYY-MM>"""
import json, sys, csv, re, time, glob, calendar, pathlib, urllib.request, urllib.parse
root = pathlib.Path(__file__).parent; ym = sys.argv[1]; y, m = map(int, ym.split("-"))
d0, d1 = f"{ym}-01", f"{ym}-{calendar.monthrange(y, m)[1]:02d}"
cfg = json.load(open(root / "config.json")); S = cfg["screen"]
KEY = (root / ".openalex_key").read_text().strip() if (root / ".openalex_key").exists() else None
out = root / "runs" / "updates" / ym; out.mkdir(parents=True, exist_ok=True)
HF_PHRASES = cfg.get("hf_phrases") or ["belief state LLM agent", "belief revision language model agent", "belief consistency reward", "belief-level supervision agent", "agent memory update stale",
              "world model LLM agent next observation", "state tracking long-horizon agent", "theory of mind belief tracking LLM", "calibration LLM agent trajectory", "credit assignment multi-turn agent belief"]
def get(url):
    for attempt in range(4):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "lit-survey/0.1"}), timeout=60).read())
        except Exception as e: print("retry", e, file=sys.stderr); time.sleep(5 * (attempt + 1))
    return None
def abstract(inv):
    if not inv: return ""
    pos = {p: w for w, ps in inv.items() for p in ps}; return " ".join(pos[i] for i in sorted(pos))
norm = lambda t: re.sub(r"[^a-z0-9]", "", (t or "").lower())
cand, counts = {}, {"month": ym, "openalex_hits": 0, "hf_hits": 0}
for sec, qs in cfg["queries"].items():
    for q in qs:
        p = {"search": q, "filter": f"from_publication_date:{d0},to_publication_date:{d1},type:" + "|".join(cfg["types"]), "per-page": 50,
             "select": "id,title,publication_date,primary_location,abstract_inverted_index,authorships,ids", **({"api_key": KEY} if KEY else {})}
        d = get("https://api.openalex.org/works?" + urllib.parse.urlencode(p)) or {"results": []}
        for w in d.get("results", []):
            counts["openalex_hits"] += 1; k = norm(w.get("title"))
            if not k or k in cand: continue
            url = ((w.get("primary_location") or {}).get("landing_page_url") or ""); am = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url)
            cand[k] = {"arxiv_id": am.group(1) if am else "", "title": w.get("title"), "date": w.get("publication_date"), "abstract": abstract(w.get("abstract_inverted_index")),
                       "authors": "; ".join(a["author"]["display_name"] for a in (w.get("authorships") or [])[:3]), "origin": "openalex"}
        time.sleep(0.3)
for q in HF_PHRASES:
    for it in get("https://huggingface.co/api/papers/search?" + urllib.parse.urlencode({"q": q})) or []:
        p = it.get("paper", it); date = (p.get("publishedAt") or "")[:10]
        if not (d0 <= date <= d1): continue
        counts["hf_hits"] += 1; k = norm(p.get("title"))
        if k and k not in cand:
            cand[k] = {"arxiv_id": p.get("id", ""), "title": re.sub(r"\s+", " ", p.get("title") or ""), "date": date, "abstract": p.get("summary") or "",
                       "authors": "; ".join(a.get("name", "") for a in (p.get("authors") or [])[:3]), "origin": "hf"}
    time.sleep(0.5)
prior = set(); seen_ids = set()
for f in glob.glob(str(root / "runs/20260916_v3/*.csv")) + glob.glob(str(root / "runs/updates/*/candidates.csv")):
    if pathlib.Path(f).parent == out: continue
    try:
        for r in csv.DictReader(open(f)):
            prior.add(norm(r.get("title"))); a = (r.get("arxiv_id") or "").strip()
            if a: seen_ids.add(a)
    except Exception: pass
counts.update(unique=len(cand), already_screened=0, no_abstract=0, I1_not_llm=0, E1_offdomain=0, I2_topic=0)
rows = []
for k, c in cand.items():
    if k in prior or (c["arxiv_id"] and c["arxiv_id"] in seen_ids): counts["already_screened"] += 1; continue
    text = (c["title"] + " " + c["abstract"]).lower()
    if len(c["abstract"]) < S["min_abstract_chars"]: counts["no_abstract"] += 1; continue
    if not any(x in text for x in S["must_any"]): counts["I1_not_llm"] += 1; continue
    if any(x in text for x in S["exclude_any"]): counts["E1_offdomain"] += 1; continue
    topics = [x for x in S["topic_any"] if x in text]
    if len(topics) < S["topic_min"]: counts["I2_topic"] += 1; continue
    c["score"] = round(sum(w for x, w in S["core_weights"].items() if x in text) + len(topics) * 0.5, 1); c["topics"] = ";".join(topics)
    c["read"] = "yes" if (c["score"] >= 10 or "belief" in text or ("world model" in text and c["score"] >= 7)) else ""; rows.append(c)
rows.sort(key=lambda r: (r["read"] != "yes", -r["score"])); counts["candidates"] = len(rows); counts["to_read"] = sum(r["read"] == "yes" for r in rows)
with open(out / "candidates.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["read", "score", "arxiv_id", "title", "date", "authors", "origin", "topics", "abstract"]); w.writeheader(); w.writerows(rows)
json.dump(counts, open(out / "counts.json", "w"), indent=1); print(json.dumps(counts, indent=1))
print(f"\nNext: read the candidates in full and write {out}/screen.csv (16 columns of the master record), then merge_update.py {ym}")
