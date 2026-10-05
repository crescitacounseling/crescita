#!/usr/bin/env python3
"""Build a private Netlify preview copy of the site.

Copies the site into a sibling folder (default: ../crescita-netlify-preview)
and makes it safe to share:
  - hidden from search engines (noindex header, meta robots, robots.txt)
  - Google Analytics tags removed, so preview visits don't count
  - CNAME removed, so it can never claim crescitacounseling.com
  - internal folders (.git, content, scripts, ops) left out

Usage:
  python3 scripts/build_preview.py
  python3 scripts/build_preview.py --out ~/Desktop/crescita-netlify-preview

Then drag the output folder onto the Netlify project's Deploys tab.
"""
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(os.path.dirname(ROOT), 'crescita-netlify-preview')
if '--out' in sys.argv:
    out = os.path.expanduser(sys.argv[sys.argv.index('--out') + 1])

SKIP = {'.git', 'content', 'scripts', 'ops', 'CNAME', 'README.md', 'PREVIEW-README.txt', 'preview.py', 'node_modules'}

if os.path.exists(out):
    shutil.rmtree(out)
shutil.copytree(ROOT, out, ignore=lambda d, names: [n for n in names if d == ROOT and n in SKIP])

with open(os.path.join(out, '_headers'), encoding='utf-8') as f:
    headers = f.read()
with open(os.path.join(out, '_headers'), 'w', encoding='utf-8') as f:
    f.write('# PREVIEW BUILD: keep this copy out of search results\n/*\n  X-Robots-Tag: noindex, nofollow\n\n' + headers)
with open(os.path.join(out, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write('User-agent: *\nDisallow: /\n')

gtag_block = re.compile(r'\s*(<!-- Google tag \(gtag\.js\) -->\s*)?<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>\s*<script>.*?</script>', re.S)
count = 0
for dirpath, _, files in os.walk(out):
    for name in files:
        if not name.endswith('.html'):
            continue
        path = os.path.join(dirpath, name)
        with open(path, encoding='utf-8') as f:
            html = f.read()
        html = gtag_block.sub('', html)
        html = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="noindex,nofollow">', html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Preview built: {out} ({count} pages, noindex, no Analytics, no CNAME)')
