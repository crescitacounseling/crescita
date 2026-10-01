#!/usr/bin/env python3
"""Build the Journal from content/journal/*.md.

Every post whose `date` is today or earlier gets its own page under journal/,
the Journal index is rebuilt, and the sitemap's journal block is refreshed.
Posts dated in the future stay unpublished until a later run.

Usage:
  python3 scripts/journal.py            # build for today
  python3 scripts/journal.py --today 2027-01-01
  python3 scripts/journal.py --next     # print the next unpublished post (date + title)

The script prints the posts it published on this run, plus each one's Google
Business Profile text, so a scheduled job can pass it along.
"""
import datetime as dt
import glob
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://www.crescitacounseling.com'
SHELL = os.path.join(ROOT, 'services', 'emdr-therapy.html')

AUTHORS = {
    'katie-fortunato': ('Katie Fortunato, LPC', '/team/katie-fortunato', 'Katie-Headshot.webp',
                        'Katie founded Crescita Counseling and focuses on EMDR, complex trauma, and parts work.'),
    'ebony-trotter': ('Ebony Trotter, LPC', '/team/ebony-trotter', 'ebony-trotter.webp',
                      'Ebony works with teens and adults on anxiety, depression, trauma, grief, and ADHD.'),
    'alissa-brown': ('Alissa Brown, LPCC', '/team/alissa-brown', 'alissa-brown.webp',
                     'Alissa works with children, teens, and military-connected families.'),
}


def parse_post(path):
    raw = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.S)
    if not m:
        raise SystemExit(f'{path}: missing front matter')
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or ':' not in line:
            continue
        k, v = line.split(':', 1)
        v = v.strip()
        if v.startswith('"') and v.endswith('"'):
            v = v[1:-1].replace('\\"', '"')
        meta[k.strip()] = v
    meta['body'] = m.group(2).strip()
    meta['slug'] = meta.get('slug') or os.path.splitext(os.path.basename(path))[0]
    meta['date'] = dt.date.fromisoformat(meta['date'])
    return meta


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" class="text-link">\1</a>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    return s


def md_to_html(md):
    out = []
    for block in re.split(r'\n\s*\n', md.strip()):
        lines = block.strip().splitlines()
        first = lines[0]
        if first.startswith('### '):
            out.append(f'<h3>{inline(first[4:])}</h3>')
        elif first.startswith('## '):
            out.append(f'<h2>{inline(first[3:])}</h2>')
        elif first.startswith('> '):
            text = ' '.join(l[2:] if l.startswith('> ') else l for l in lines)
            out.append(f'<blockquote class="article__quote">{inline(text)}</blockquote>')
        elif all(re.match(r'^[-*] ', l) for l in lines):
            out.append('<ul>' + ''.join(f'<li>{inline(l[2:])}</li>' for l in lines) + '</ul>')
        elif all(re.match(r'^\d+\. ', l) for l in lines):
            items = [inline(re.sub(r'^\d+\. ', '', l)) for l in lines]
            out.append('<ol>' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>')
        else:
            out.append(f'<p>{inline(" ".join(lines))}</p>')
    return '\n      '.join(out)


def nice_date(d):
    return d.strftime('%B ') + str(d.day) + d.strftime(', %Y')


def read_minutes(md):
    return max(3, round(len(md.split()) / 220))


def page(shell, path_url, title, desc, graph, main, og_type='website', og_img='meadow-flowers'):
    url = f'{BASE}{path_url}'
    h = shell
    h = re.sub(r'<title>.*?</title>', f'<title>{html.escape(title)}</title>', h, count=1)
    h = re.sub(r'(<meta name="description" content=")[^"]*(">)', lambda m: m.group(1) + html.escape(desc) + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*(">)', lambda m: m.group(1) + html.escape(desc) + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*(">)', lambda m: m.group(1) + html.escape(title) + m.group(2), h, count=1)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*(">)', lambda m: m.group(1) + url + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*(">)', lambda m: m.group(1) + url + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:type" content=")[^"]*(">)', lambda m: m.group(1) + og_type + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:image" content=")[^"]*(">)', lambda m: m.group(1) + f'{BASE}/assets/images/{og_img}.jpg' + m.group(2), h, count=1)
    h = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', h, flags=re.S)
    h = h.replace('</head>', '<script type="application/ld+json">\n' + json.dumps(graph, indent=1, ensure_ascii=False) + '\n</script>\n</head>', 1)
    h = re.sub(r'<main id="main">.*</main>', lambda m: '<main id="main">\n' + main + '\n</main>', h, flags=re.S)
    # Journal is the current section in the menu
    h = h.replace('<a href="/journal/" class="nav-link">Journal</a>', '<a href="/journal/" class="nav-link" aria-current="page">Journal</a>', 1)
    return h


def picture(img, alt, extra=''):
    return (f'<picture><source srcset="../assets/images/{img}.webp" type="image/webp">'
            f'<img src="../assets/images/{img}.jpg" alt="{html.escape(alt)}" {extra}></picture>')


def build_post(shell, p):
    url = f"{BASE}/journal/{p['slug']}"
    name, author_url, headshot, bio = AUTHORS.get(p.get('author', 'katie-fortunato'), AUTHORS['katie-fortunato'])
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "@id": url + "#post", "headline": p['title'], "description": p['description'],
         "datePublished": p['date'].isoformat(), "dateModified": p['date'].isoformat(), "url": url, "mainEntityOfPage": url,
         "image": f"{BASE}/assets/images/{p['image']}.jpg",
         "author": {"@type": "Person", "name": name, "url": BASE + author_url},
         "publisher": {"@id": f"{BASE}/#business"}, "isPartOf": {"@id": f"{BASE}/journal/#blog"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Journal", "item": f"{BASE}/journal/"},
            {"@type": "ListItem", "position": 3, "name": p['title'], "item": url}]}]}
    service = ''
    if p.get('service'):
        service = (f'\n    <p class="article__related container-t">Related: <a href="{p["service"]}" class="text-link">'
                   f'{html.escape(p.get("service_name", "our services"))}</a></p>')
    from urllib.parse import quote
    u, t = quote(url, safe=''), quote(p['title'], safe='')
    share = f'''
    <div class="share container-t" data-share data-url="{url}" data-title="{html.escape(p['title'])}">
      <span class="share__label">Share this post</span>
      <button type="button" class="share__btn share__native" data-share-native hidden>Share&hellip;</button>
      <a class="share__btn" href="https://www.facebook.com/sharer/sharer.php?u={u}" target="_blank" rel="noopener">Facebook</a>
      <a class="share__btn" href="https://www.linkedin.com/sharing/share-offsite/?url={u}" target="_blank" rel="noopener">LinkedIn</a>
      <a class="share__btn" href="https://twitter.com/intent/tweet?url={u}&amp;text={t}" target="_blank" rel="noopener">X</a>
      <a class="share__btn" href="mailto:?subject={t}&amp;body={u}">Email</a>
      <button type="button" class="share__btn" data-share-copy>Copy link</button>
    </div>
    <script>
    (function(){{
      var box=document.querySelector('[data-share]'); if(!box) return;
      var url=box.getAttribute('data-url'), title=box.getAttribute('data-title');
      var nat=box.querySelector('[data-share-native]');
      if(navigator.share){{ nat.hidden=false; nat.addEventListener('click',function(){{ navigator.share({{title:title,url:url}}).catch(function(){{}}); }}); }}
      var cp=box.querySelector('[data-share-copy]');
      cp.addEventListener('click',function(){{
        var done=function(){{ cp.textContent='Link copied'; setTimeout(function(){{cp.textContent='Copy link';}},2000); }};
        if(navigator.clipboard){{ navigator.clipboard.writeText(url).then(done,function(){{window.prompt('Copy this link:',url);}}); }}
        else {{ window.prompt('Copy this link:',url); }}
      }});
    }})();
    </script>'''
    main = f'''
  <article class="article">
    <header class="article__header container-t">
      <nav class="breadcrumbs reveal"><a href="/">Home</a><span>/</span><a href="/journal/">Journal</a><span>/</span><strong>{html.escape(p['tag'])}</strong></nav>
      <span class="eyebrow eyebrow--rose reveal">{html.escape(p['tag'])}</span>
      <h1 class="article__title reveal">{html.escape(p['title'])}</h1>
      <p class="article__meta reveal"><time datetime="{p['date'].isoformat()}">{nice_date(p['date'])}</time> &middot; {read_minutes(p['body'])} min read &middot; {name}</p>
    </header>

    <figure class="article__hero container reveal">
      {picture(p['image'], p['image_alt'], 'width="1600" height="900" fetchpriority="high"')}
    </figure>

    <div class="article__body container-t prose">
      {md_to_html(p['body'])}
    </div>{share}{service}

    <aside class="article__author container-t">
      <img src="../assets/images/{headshot}" alt="{html.escape(name)}" width="96" height="96" loading="lazy">
      <div>
        <p class="article__author-name">{name}</p>
        <p>{bio} <a href="{author_url}" class="text-link">More about {name.split()[0]}</a></p>
      </div>
    </aside>
  </article>

  <section class="section">
    <div class="container"><div class="cta-banner reveal">
  <div class="cta-banner__bg"><img src="../assets/images/mountains-wide.jpg" alt="" loading="lazy"><div></div></div>
  <h2 style="margin-top:0">Want to talk it through?</h2>
  <p>A free 20-minute call. No pressure, no script. We'll tell you honestly whether we're the right fit.</p>
  <div class="cta-banner__ctas">
    <a href="/contact" class="btn btn-rose">Book a free call</a>
  </div>
</div></div>
  </section>
'''
    return page(shell, f"/journal/{p['slug']}", f"{p['title']} | Crescita Counseling", p['description'], graph, main, 'article', p['image'])


def build_index(shell, posts):
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": f"{BASE}/journal/#blog", "url": f"{BASE}/journal/", "name": "The Crescita Journal",
         "publisher": {"@id": f"{BASE}/#business"},
         "blogPost": [{"@id": f"{BASE}/journal/{p['slug']}#post"} for p in posts]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Journal", "item": f"{BASE}/journal/"}]}]}
    head = '''
  <section class="page-hero page-hero--uniform page-hero--journal">
    <div class="container" style="padding-bottom:3rem">
      <img class="journal-mark" src="../assets/images/crescita-logo-md.png" alt="" width="300" height="300" aria-hidden="true">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="/">Home</a><span>/</span><strong>Journal</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">The Crescita Journal</span>
        <h1 class="page-hero__title reveal">Notes from <em>the therapy room.</em></h1>
        <p class="page-hero__lead reveal">Short, plain-language pieces on trauma, anxiety, EMDR, grief, and raising kids through hard seasons. Written by the therapists at Crescita in Colorado Springs.</p>
      </div>
    </div>
  </section>'''
    if not posts:
        body = '<p class="lead">The first post is on its way.</p>'
    else:
        f = posts[0]
        body = f'''<article class="post-feature reveal">
        <a href="/journal/{f['slug']}" class="post-feature__img">
          {picture(f['image'], f['image_alt'], 'width="1200" height="1500" loading="eager"')}
        </a>
        <div class="post-feature__body">
          <span class="eyebrow eyebrow--rose">{html.escape(f['tag'])} &middot; Latest</span>
          <h2 class="post-feature__title"><a href="/journal/{f['slug']}">{html.escape(f['title'])}</a></h2>
          <p>{html.escape(f['description'])}</p>
          <p class="article__meta"><time datetime="{f['date'].isoformat()}">{nice_date(f['date'])}</time> &middot; {read_minutes(f['body'])} min read</p>
          <a href="/journal/{f['slug']}" class="btn-ghost">Read the post</a>
        </div>
      </article>'''
        if len(posts) > 1:
            cards = '\n'.join(f'''        <article class="post-card reveal">
          <span class="eyebrow">{html.escape(p['tag'])} &middot; {nice_date(p['date'])}</span>
          <h3 class="post-card__title"><a href="/journal/{p['slug']}" style="color:inherit">{html.escape(p['title'])}</a></h3>
          <p>{html.escape(p['description'])}</p>
        </article>''' for p in posts[1:])
            body += f'\n      <div class="post-grid">\n{cards}\n      </div>'
    main = head + f'''

  <section class="section bg-white" style="padding-top:clamp(2.5rem,5vw,4rem)">
    <div class="container">
      {body}
    </div>
  </section>
'''
    desc = 'Plain-language writing on trauma, anxiety, EMDR, grief, and parenting through hard seasons from the therapists at Crescita Counseling in Colorado Springs.'
    return page(shell, '/journal/', 'Journal | Crescita Counseling Colorado Springs', desc, graph, main)


def update_sitemap(posts):
    path = os.path.join(ROOT, 'sitemap.xml')
    s = open(path, encoding='utf-8').read()
    entries = [f'  <url>\n    <loc>{BASE}/journal/</loc>\n    <lastmod>{(posts[0]["date"] if posts else dt.date.today()).isoformat()}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.7</priority>\n  </url>']
    for p in posts:
        entries.append(f'  <url>\n    <loc>{BASE}/journal/{p["slug"]}</loc>\n    <lastmod>{p["date"].isoformat()}</lastmod>\n    <changefreq>yearly</changefreq>\n    <priority>0.6</priority>\n  </url>')
    block = '  <!-- journal:start -->\n' + '\n\n'.join(entries) + '\n  <!-- journal:end -->'
    if '<!-- journal:start -->' in s:
        s = re.sub(r'  <!-- journal:start -->.*?<!-- journal:end -->', lambda m: block, s, flags=re.S)
    else:
        s = s.replace('</urlset>', block + '\n\n</urlset>')
    open(path, 'w', encoding='utf-8').write(s)


def main():
    args = sys.argv[1:]
    today = dt.date.today()
    if '--today' in args:
        today = dt.date.fromisoformat(args[args.index('--today') + 1])
    posts = sorted((parse_post(p) for p in glob.glob(os.path.join(ROOT, 'content', 'journal', '*.md'))
                    if not os.path.splitext(os.path.basename(p))[0].isupper() and not os.path.basename(p).startswith('_')),
                   key=lambda p: p['date'], reverse=True)
    live = [p for p in posts if p['date'] <= today]
    if '--next' in args:
        upcoming = sorted((p for p in posts if p['date'] > today), key=lambda p: p['date'])
        print(f"{upcoming[0]['date']}  {upcoming[0]['title']}" if upcoming else 'No posts left in the queue.')
        return
    shell = open(SHELL, encoding='utf-8').read()
    os.makedirs(os.path.join(ROOT, 'journal'), exist_ok=True)
    new = []
    for p in live:
        out = os.path.join(ROOT, 'journal', p['slug'] + '.html')
        html_text = build_post(shell, p)
        if not os.path.exists(out) or open(out, encoding='utf-8').read() != html_text:
            if not os.path.exists(out) or 'sample-banner' in open(out, encoding='utf-8').read():
                new.append(p)
            open(out, 'w', encoding='utf-8').write(html_text)
    open(os.path.join(ROOT, 'journal', 'index.html'), 'w', encoding='utf-8').write(build_index(shell, live))
    update_sitemap(live)
    print(f'Live posts: {len(live)} of {len(posts)}')
    for p in new:
        print(f"\nPUBLISHED: {p['title']}\nURL: {BASE}/journal/{p['slug']}\nGOOGLE BUSINESS PROFILE POST:\n{p.get('gbp', '').strip()}")


if __name__ == '__main__':
    main()
