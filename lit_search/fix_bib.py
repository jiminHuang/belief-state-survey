#!/usr/bin/env python3
"""Step 10: clean the survey bibs (review item 9).
- drop note={arXiv:N} when the entry also has eprint={N} (acl_natbib then prints the id twice)
- @inproceedings that carries journal= but no booktitle= becomes @article (venue was dropped)
- titles: protect acronyms / mixed-case names / proper nouns from lower-casing; unprotect plain
  hyphenated title-case words such as {Multi-Turn} (they should follow sentence case)
Usage: fix_bib.py file.bib ...   (in place; prints a per-file count)"""
import re, sys
PROPER = {"Bayes", "Bayesian", "Markov", "Gaussian", "Bellman", "Kalman", "Nash", "Monte", "Carlo", "Dirichlet", "Hawkes",
          "English", "Chinese", "Werewolf", "Minecraft", "Atari", "Wikipedia", "Transformer", "Transformers", "Pareto", "Kelly",
          "Dempster", "Shafer", "Gricean", "Theory-of-Mind"}
def needs(piece):
    w = re.sub(r"[^A-Za-z]", "", piece)
    if len(w) < 2: return False
    return sum(c.isupper() for c in w) >= 2 or any(c.isupper() for c in w[1:]) or w in PROPER or re.sub(r"s$", "", w) in PROPER
def protect_title(v):
    out, depth, tok = [], 0, ""
    def flush():
        nonlocal tok
        if tok:
            if re.fullmatch(r"[A-Z][a-z]+(-[A-Z][a-z]+)+", tok): out.append(tok)
            else:
                parts = re.split(r"(-|/)", tok)
                out.append("".join("{" + p + "}" if (p not in "-/" and "\\" not in p and "$" not in p and needs(p)) else p for p in parts))
            tok = ""
    i = 0
    while i < len(v):
        c = v[i]
        if c == "{":
            j, d = i, 0
            while j < len(v):
                d += v[j] == "{"; d -= v[j] == "}"
                if d == 0: break
                j += 1
            grp = v[i:j+1]; inner = grp[1:-1]
            if re.fullmatch(r"[A-Z][a-z]+(-[A-Z][a-z]+)+", inner) and not tok: out.append(inner)   # unprotect {Multi-Turn}
            else: flush(); out.append(grp)
            i = j + 1; continue
        if c in " :,;?!()." : flush(); out.append(c)
        else: tok += c
        i += 1
    flush(); return "".join(out)
def field_span(s, name):
    m = re.search(r"(?i)\b" + name + r"\s*=\s*\{", s)
    if not m: return None
    i, d = m.end() - 1, 0
    for j in range(i, len(s)):
        d += s[j] == "{"; d -= s[j] == "}"
        if d == 0: return m.start(), i, j
    return None
for f in sys.argv[1:]:
    txt = open(f).read(); n = {"note": 0, "type": 0, "title": 0}
    ents = re.split(r"(?=@\w+\s*\{)", txt); out = []
    for e in ents:
        if not e.startswith("@"): out.append(e); continue
        ep = re.search(r"(?i)\beprint\s*=\s*\{([^}]*)\}", e)
        if ep:
            e2 = re.sub(r"(?i),?\s*note\s*=\s*\{arXiv:\s*" + re.escape(ep.group(1)) + r"\}", "", e)
            n["note"] += e2 != e; e = e2
        if re.match(r"(?i)@inproceedings", e) and re.search(r"(?i)\bjournal\s*=", e) and not re.search(r"(?i)\bbooktitle\s*=", e):
            e = re.sub(r"(?i)^@inproceedings", "@article", e); n["type"] += 1
        sp = field_span(e, "title")
        if sp:
            a, i, j = sp; v = e[i+1:j]; nv = protect_title(v)
            if nv != v: e = e[:i+1] + nv + e[j:]; n["title"] += 1
        out.append(e)
    open(f, "w").write("".join(out)); print(f, n)
