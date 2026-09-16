#!/usr/bin/env python3
"""Step 2: merge sources, rule-based screening (title+abstract), relevance scoring. Writes runs/<ts>/screened.csv,
shortlist_recent.csv and counts_screen.json (PRISMA-style numbers). Rules and weights live in config.json['screen']."""
import json, sys, csv, pathlib, re
root = pathlib.Path(__file__).parent
ts = sys.argv[1] if len(sys.argv) > 1 else sorted(p.name for p in (root / "runs").iterdir())[-1]
run = root / "runs" / ts
cfg = json.load(open(root / "config.json")); S = cfg["screen"]
json.dump(cfg, open(run / "config_snapshot.json", "w"), indent=1)
raw, c = {}, {"timestamp": ts, "sources": {}}
for f in ["raw.json", "raw_arxiv.json"]:
    if (run / f).exists():
        d = json.load(open(run / f)); c["sources"][f] = len(d)
        for k, v in d.items():
            key = (v.get("doi") or k).lower()
            if key in raw: raw[key]["hits"] += v["hits"]
            else: raw[key] = v
c["unique_after_dedup_all_sources"] = len(raw)
# title-level dedup (preprint + journal version)
seen, merged = {}, {}
for k, v in raw.items():
    t = re.sub(r"[^a-z0-9]", "", (v["title"] or "").lower())
    if t in seen: merged[seen[t]]["hits"] += v["hits"]; continue
    seen[t] = k; merged[k] = v
raw = merged; c["unique_after_title_dedup"] = len(raw)
c.update({"excluded_no_abstract": 0, "excluded_I1_not_llm": 0, "excluded_E1_offdomain": 0, "excluded_I2_topic": 0, "included": 0, "included_recent": 0})
rows = []
for p in raw.values():
    text = ((p["title"] or "") + " " + (p["abstract"] or "")).lower()
    if len(p["abstract"] or "") < S["min_abstract_chars"]: c["excluded_no_abstract"] += 1; continue
    if not any(k in text for k in S["must_any"]): c["excluded_I1_not_llm"] += 1; continue
    if any(k in text for k in S["exclude_any"]): c["excluded_E1_offdomain"] += 1; continue
    topics = [k for k in S["topic_any"] if k in text]
    if len(topics) < S["topic_min"]: c["excluded_I2_topic"] += 1; continue
    score = sum(w for k, w in S["core_weights"].items() if k in text) + len(topics) * 0.5 + len({h[1] for h in p["hits"]}) * 1.0
    secs = sorted({h[0] for h in p["hits"]})
    rows.append({"score": round(score, 1), "title": p["title"], "date": p["date"], "year": p["year"], "cites": p["cites"], "venue": p["venue"] or "",
                 "sections": ";".join(secs), "n_queries_hit": len({h[1] for h in p["hits"]}), "topics": ";".join(topics),
                 "url": p["url"] or p["doi"] or p["id"], "authors": "; ".join(p["authors"]), "abstract": p["abstract"]})
c["included"] = len(rows)
rows.sort(key=lambda r: (-r["score"], -(r["cites"] or 0)))
recent = [r for r in rows if r["year"] == cfg["recent_year"]]
c["included_recent"] = len(recent); c["included_by_section"] = {}
for r in rows:
    for s in r["sections"].split(";"): c["included_by_section"][s] = c["included_by_section"].get(s, 0) + 1
for name, data in [("screened.csv", rows), ("shortlist_recent.csv", recent)]:
    with open(run / name, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(data)
json.dump(c, open(run / "counts_screen.json", "w"), indent=1); print(json.dumps(c, indent=1))
