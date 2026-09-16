#!/usr/bin/env python3
"""Step 4: replace truncated author lists in a .bib with full authorships from OpenAlex (lookup by arXiv id via
the works endpoint, filter ids.openalex / doi 10.48550/arxiv.<id>). Writes <bib>.full.bib and a report."""
import re, sys, json, time, urllib.request, urllib.parse, pathlib
KEY=(pathlib.Path(__file__).parent/".openalex_key").read_text().strip() if (pathlib.Path(__file__).parent/".openalex_key").exists() else None
src=sys.argv[1]; txt=open(src).read(); ents=re.findall(r'@\w+\{[^\n]*\}\s*$', txt, re.M)
def openalex_authors(arx):
    url="https://api.openalex.org/works?"+urllib.parse.urlencode({"filter":f"doi:10.48550/arxiv.{arx}","select":"authorships,title", **({"api_key": KEY} if KEY else {})})
    try:
        d=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"lit-survey/0.1"}),timeout=40).read())
        r=d.get("results",[])
        if r: return [a["author"]["display_name"] for a in r[0]["authorships"]]
    except Exception as e: print("ERR",arx,e,file=sys.stderr)
    return None
out=[]; rep=[]
for e in ents:
    m=re.search(r'eprint=\{(\d{4}\.\d{5})\}',e); 
    if not m: out.append(e); continue
    au=openalex_authors(m.group(1)); time.sleep(0.25)
    if au and not any(re.search(r'[^\x00-\x7f]',a) for a in au):
        e2=re.sub(r'author=\{[^}]*\}','author={'+' and '.join(au)+'}',e); rep.append((m.group(1),len(au))); out.append(e2)
    else: out.append(e)
open(src.replace('.bib','.full.bib'),'w').write("\n".join(out)+"\n")
print("entries",len(ents),"enriched",len(rep)); print(rep[:10])
