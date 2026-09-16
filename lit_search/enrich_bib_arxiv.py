#!/usr/bin/env python3
"""Step 4 (arXiv variant): fill full author lists via the arXiv API id_list endpoint, 25 ids per call."""
import re, sys, time, urllib.request, html
src=sys.argv[1]; txt=open(src).read(); ents=re.findall(r'@\w+\{[^\n]*\}\s*$', txt, re.M)
ids=[m.group(1) for e in ents for m in [re.search(r'eprint=\{(\d{4}\.\d{5})\}',e)] if m]
authors={}
for i in range(0,len(ids),25):
    chunk=ids[i:i+25]
    url="https://export.arxiv.org/api/query?id_list="+",".join(chunk)+"&max_results=25"
    for attempt in range(3):
        try:
            x=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"lit-survey/0.1"}),timeout=60).read().decode(); break
        except Exception as e: print("retry",e,file=sys.stderr); time.sleep(8); x=""
    for ent in re.findall(r"<entry>(.*?)</entry>",x,re.S):
        aid=re.search(r"<id>http[s]?://arxiv.org/abs/([\d.]+)v?\d*</id>",ent)
        if not aid: continue
        names=[html.unescape(n) for n in re.findall(r"<name>(.*?)</name>",ent)]
        authors[aid.group(1)]=names
    time.sleep(3.5)
out=[];n=0
for e in ents:
    m=re.search(r'eprint=\{(\d{4}\.\d{5})\}',e)
    if m and m.group(1) in authors and authors[m.group(1)] and not any(re.search(r'[^\x00-\x7f]',a) for a in authors[m.group(1)]):
        e=re.sub(r'author=\{[^}]*\}','author={'+' and '.join(authors[m.group(1)])+'}',e); n+=1
    out.append(e)
open(src,'w').write("\n".join(out)+"\n"); print("entries",len(ents),"ids",len(ids),"enriched",n)
