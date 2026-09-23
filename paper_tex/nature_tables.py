#!/usr/bin/env python3
"""Restyle LaTeX tables to the Nature look used in the main text.

For every table / table* environment in the given files:
  - \\centering\\<size>  ->  \\nattab\\<size>   (thin rules, sans, row spacing)
  - caption moved above the table; its first sentence becomes the bold title,
    the rest becomes a \\tabnote under the table
  - header row (the line after \\toprule) set in bold
  - a hairline (\\rr) after every body row except the last
Idempotent: tables that already use \\nattab are left alone.
Run again after make_master.py regenerates tab_master_full.tex.

Usage: nature_tables.py file.tex [file.tex ...]
"""
import re
import sys


def balanced(s, i):
    """Return index just past the brace group starting at s[i] == '{'."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == '{':
            depth += 1
        elif s[j] == '}':
            depth -= 1
            if depth == 0:
                return j + 1
    raise ValueError('unbalanced braces')


def split_title(cap):
    """Split a caption at the first sentence end outside braces."""
    depth = 0
    for k, ch in enumerate(cap):
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
        elif ch == '.' and depth == 0 and (k + 1 == len(cap) or cap[k + 1] == ' '):
            before = cap[max(0, k - 4):k]
            if before.endswith(('e.g', 'i.e', ' al', 'vs', 'Fig', 'Eq')):
                continue
            return cap[:k + 1].strip(), cap[k + 1:].strip()
    return cap.strip(), ''


def convert(env):
    if '\\nattab' in env:
        return env
    env = re.sub(r'\\centering\\(tiny|scriptsize|footnotesize|small)', r'\\nattab\\\1', env, count=1)
    if '\\nattab' not in env:
        env = env.replace('\\centering', '\\nattab', 1)
    # caption -> title above, note below
    c = env.find('\\caption{')
    title, note = '', ''
    if c >= 0:
        e = balanced(env, c + len('\\caption'))
        cap = env[c + len('\\caption{'):e - 1]
        title, note = split_title(cap)
        env = env[:c] + env[e:]
        env = re.sub(r'\n\s*\n', '\n', env)
    # insert title before \resizebox or \begin{tabular}
    anchor = min([p for p in (env.find('\\resizebox'), env.find('\\begin{tabular}')) if p >= 0])
    if title:
        env = env[:anchor] + '\\caption{\\textbf{' + title + '}}\n' + env[anchor:]
    # header bold
    t = env.find('\\toprule')
    if t >= 0:
        hs = env.index('\n', t) + 1
        he = env.index('\\\\', hs)
        cells = [x.strip() for x in env[hs:he].split('&')]
        cells = [('\\textbf{%s}' % x if x and not x.startswith('\\textbf') else x) for x in cells]
        env = env[:hs] + ' & '.join(cells) + ' ' + env[he:]
    # hairlines after body rows
    m = env.find('\\midrule')
    b = env.find('\\bottomrule')
    if m >= 0 and b > m:
        body = env[m:b]
        lines = body.split('\n')
        rows = [i for i, l in enumerate(lines) if l.rstrip().endswith('\\\\')]
        for i in rows[:-1]:
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
            if nxt.startswith('\\midrule'):
                continue
            lines[i] = lines[i].rstrip() + ' \\rr'
        env = env[:m] + '\n'.join(lines) + env[b:]
    # note after the tabular (after the resizebox brace if there is one)
    if note:
        end = env.find('\\end{tabular}')
        end += len('\\end{tabular}')
        if env[end:end + 1] == '}':
            end += 1
        env = env[:end] + '\n\\tabnote{' + note + '}' + env[end:]
    return env


def process(path):
    s = open(path).read()
    out, pos = [], 0
    for m in re.finditer(r'\\begin\{(table\*?)\}', s):
        if m.start() < pos:
            continue
        kind = m.group(1)
        end = s.index('\\end{%s}' % kind, m.end()) + len('\\end{%s}' % kind)
        out.append(s[pos:m.start()])
        out.append(convert(s[m.start():end]))
        pos = end
    out.append(s[pos:])
    new = ''.join(out)
    if new != s:
        open(path, 'w').write(new)
        print('restyled', path)


if __name__ == '__main__':
    for p in sys.argv[1:]:
        process(p)
