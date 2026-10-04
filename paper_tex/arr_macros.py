"""Convert table environments to version-switchable macros (run after nature_tables.py / make_master.py).

  \\nattab\\tiny            -> \\nattab[\\tiny]           size used only in the preprint
  \\resizebox{W}{!}{%       -> \\tabfit[W]{%             preprint scales; ARR shrinks only if too wide
  first \\caption{...}      -> \\tcap{...}                caption above (preprint) or below (ARR)
  before \\label{tab...}    -> \\bcap                     emits the caption in the ARR version
Idempotent: files already converted are left unchanged.
Usage: python3 arr_macros.py sections/*.tex
"""
import re, sys
def convert_block(b):
    b = re.sub(r'\\nattab\\(tiny|scriptsize|footnotesize|small)\b', r'\\nattab[\\\1]', b)
    b = b.replace('\\resizebox{\\columnwidth}{!}{%', '\\tabfit{%').replace('\\resizebox{\\textwidth}{!}{%', '\\tabfit[\\textwidth]{%')
    if '\\tcap{' not in b and '\\caption{' in b:
        b = b.replace('\\caption{', '\\tcap{', 1)
        b = re.sub(r'(\n)(\\label\{tab)', r'\1\\bcap\n\2', b, count=1)
    return b
for f in sys.argv[1:]:
    s = open(f).read()
    out = re.sub(r'\\begin\{table\*?\}.*?\\end\{table\*?\}', lambda m: convert_block(m.group(0)), s, flags=re.S)
    if out != s:
        open(f, 'w').write(out); print('converted', f)
