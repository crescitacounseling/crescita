# Crescita Counseling — Static Site (v2)

A complete static rebuild of crescitacounseling.com. Editorial design, dusty-rose/slate palette, Whitney-inspired voice, real Crescita logo, real photo assets.

## Stack

- 10 HTML pages (plus 404), plain HTML5
- Single stylesheet (`css/styles.css`, ~22KB)
- Single JS file (`js/main.js`, ~3KB) — mobile nav, reveal-on-scroll, form handler
- Fonts: Newsreader (display, variable opsz) + Manrope (body) via Google Fonts
- Form: Formspree (placeholder ID — replace before launch)
- Schema.org JSON-LD on every page

## Design tokens

```
--rose:       #C6919C    (primary pop)
--rose-deep:  #A37580    (rose hover/emphasis)
--taupe:      #6E6361    (secondary text)
--slate:      #50585D    (primary text / dark surfaces)
--slate-deep: #3A4146    (CTA banner + footer)
--blush:      #E0D0CC    (soft accent)
--cream:      #F4EEE5    (default background)
--cream-deep: #EAE2D5    (section variation)

--font-display: 'Newsreader' serif (variable optical size)
--font-body:    'Manrope' sans
```

## File structure

```
crescita-counseling/
├── index.html
├── about.html
├── investment.html
├── faq.html
├── contact.html
├── 404.html
├── team/
│   ├── katie-pasqualetto.html
│   └── alissa-brown.html
├── services/
│   ├── individual-therapy.html
│   ├── emdr-therapy.html
│   └── child-and-teen-therapy.html
├── assets/
│   └── images/
│       ├── crescita-logo.png         (800×800 brand mark)
│       ├── crescita-logo-sm.png      (400×400 header/favicon)
│       ├── alissa-brown.jpg          (new high-res replacement)
│       ├── wildflowers.jpg           (homepage hero)
│       ├── soft-botanicals.jpg       (about hero)
│       ├── mountain-peaks.jpg
│       ├── water-ripples.jpg
│       ├── clouds-rose.jpg
│       ├── river-stones.jpg
│       ├── garden-of-the-gods.jpg
│       ├── garden-gods-window.jpg
│       ├── creek-stream.jpg
│       └── wood-grain.jpg
├── css/styles.css
├── js/main.js
├── sitemap.xml
├── robots.txt              (CURRENTLY BLOCKS — staging)
├── robots.production.txt   (rename at launch)
└── llms.txt
```

## Deployment

### GitHub Pages (staging)

1. Push directory to a GitHub repo
2. Settings → Pages → Source: `main` branch, root
3. Live at `https://<username>.github.io/<repo-name>/`
4. **No CNAME file included** — intentional for staging
5. All paths are relative, works in subdirectory deployment

### Cloudflare Pages

1. Connect repo in CF Pages dashboard
2. Build command: *(none)*
3. Build output: `/`
4. Deploy

## Pre-launch checklist

- [ ] Drop a `CNAME` file with `crescitacounseling.com`
- [ ] Delete staging `robots.txt`, rename `robots.production.txt` → `robots.txt`
- [ ] Replace `YOUR_FORMSPREE_ID` in `contact.html` with your real Formspree ID
- [ ] Replace **Katie's photo** — currently still references Squarespace CDN URLs in `about.html` and `team/katie-pasqualetto.html`. Get high-res files and save as `assets/images/katie-pasqualetto.jpg` + `katie-pasqualetto-2.jpg`, then update the three `<img src>` references.
- [ ] Test contact form submission end-to-end
- [ ] Submit `https://www.crescitacounseling.com/sitemap.xml` to Google Search Console + Bing Webmaster
- [ ] Verify Mentaya widget URL on `investment.html` is still active
- [ ] Update DNS at registrar

## Formspree setup

1. Sign up at formspree.io
2. New form → set destination email → `info@crescitacounseling.com`
3. Copy the form ID (e.g. `xqzkpwxy`)
4. In `contact.html`, replace `YOUR_FORMSPREE_ID` with the real ID
5. Test before launch

Form already has honeypot spam protection, native HTML5 validation, async submission with loading/success/error states.

## Voice & content notes

Copy was written to sound like a real person, not a marketing department — fragments allowed, asides in parentheses, italic single-word emphasis for warmth. Modeled loosely on the tone of `losmanzanos.github.io/whitney`. If a client wants to tighten or warm any section further, the content lives directly in each `.html` between `<main id="main">` tags.

## SEO included

- `<title>` + `<meta description>` per page
- Canonical URLs
- Open Graph + Twitter Card meta
- Schema.org JSON-LD: LocalBusiness, MedicalBusiness, MedicalTherapy, Person, FAQPage, ContactPage, WebSite
- `sitemap.xml`
- `robots.txt` (staging blocks; production allows)
- `llms.txt` for AI crawler guidance
- Semantic HTML, proper landmarks, skip link, ARIA on interactives
- All images have descriptive alt text

## Performance

- No build step, no JS framework
- CSS: ~22KB · JS: ~3KB
- Images compressed and properly sized (1600px max width, JPEG quality 82)
- Font preconnect hints
- Lazy-loaded below-fold images
- Should hit 95+ Lighthouse out of the box

## Editing without the build scripts

The site is plain HTML — open any `.html` file and edit content inside `<main id="main">`. Header and footer are duplicated across files. For site-wide nav changes, search & replace, or regenerate via the included `_build.py` / `_gen_*.py` scripts.

The build scripts are not required for the site to run. Safe to delete after launch.

---

Built by Chad · therapistweb.design
# katie
