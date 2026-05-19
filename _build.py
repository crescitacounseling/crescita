#!/usr/bin/env python3
"""Crescita v3 builder — wordmark header, full logo in footer, no cheesy circles."""
import os, json

SITE_URL = "https://www.crescitacounseling.com"

def build_page(*, filename, depth=0, title, description, og_image=None,
               canonical_path, schema=None, content, nav_active="", body_class=""):
    prefix = "../" * depth
    canonical = f"{SITE_URL}{canonical_path}"
    og_image = og_image or f"{SITE_URL}/assets/images/wildflowers.jpg"
    schema_block = ""
    if schema:
        schema_block = f'<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False)}\n</script>'

    def aria(t): return ' aria-current="page"' if nav_active == t else ""

    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#A37580">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:site_name" content="Crescita Counseling">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" type="image/png" href="{prefix}assets/images/crescita-logo-sm.png">
<link rel="apple-touch-icon" href="{prefix}assets/images/crescita-logo-md.png">
<link rel="stylesheet" href="{prefix}css/styles.css">
{schema_block}
</head>
<body{(' class="' + body_class + '"') if body_class else ''}>

<a href="#main" class="skip-link">Skip to content</a>"""

    header = f"""
<header class="site-header">
  <div class="container">
    <div class="site-header__inner">
      <a href="{prefix}index.html" class="brand" aria-label="Crescita Counseling — Home">
        <span>Crescita</span>
        <span class="brand__dot" aria-hidden="true"></span>
        <span class="brand__sub">counseling</span>
      </a>
      <nav class="nav" aria-label="Primary">
        <a href="{prefix}index.html" class="nav-link"{aria("home")}>Home</a>
        <a href="{prefix}about.html" class="nav-link"{aria("about")}>About</a>
        <div class="nav-item">
          <button class="nav-link" aria-haspopup="true">Services <span class="nav-link__caret">▾</span></button>
          <div class="nav-dropdown">
            <a href="{prefix}services/individual-therapy.html" class="nav-dropdown__link">Individual Therapy</a>
            <a href="{prefix}services/emdr-therapy.html" class="nav-dropdown__link">EMDR Therapy</a>
            <a href="{prefix}services/child-and-teen-therapy.html" class="nav-dropdown__link">Child &amp; Teen Therapy</a>
          </div>
        </div>
        <a href="{prefix}investment.html" class="nav-link"{aria("investment")}>Rates</a>
        <a href="{prefix}faq.html" class="nav-link"{aria("faq")}>FAQ</a>
        <a href="{prefix}contact.html" class="nav-link"{aria("contact")}>Contact</a>
      </nav>
      <div class="header-cta">
        <a href="{prefix}contact.html" class="btn btn-primary">Book a call</a>
        <button class="nav-toggle" data-nav-toggle aria-expanded="false" aria-controls="mobileNav" aria-label="Open menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </div>
</header>

<div class="mobile-nav" id="mobileNav" data-mobile-nav data-open="false" aria-hidden="true">
  <div class="mobile-nav__group">
    <p class="mobile-nav__heading">Pages</p>
    <a href="{prefix}index.html" class="mobile-nav__link"{aria("home")}>Home</a>
    <a href="{prefix}about.html" class="mobile-nav__link"{aria("about")}>About</a>
    <a href="{prefix}investment.html" class="mobile-nav__link"{aria("investment")}>Rates &amp; Insurance</a>
    <a href="{prefix}faq.html" class="mobile-nav__link"{aria("faq")}>FAQ</a>
    <a href="{prefix}contact.html" class="mobile-nav__link"{aria("contact")}>Contact</a>
  </div>
  <div class="mobile-nav__group">
    <p class="mobile-nav__heading">Services</p>
    <a href="{prefix}services/individual-therapy.html" class="mobile-nav__link">Individual Therapy</a>
    <a href="{prefix}services/emdr-therapy.html" class="mobile-nav__link">EMDR Therapy</a>
    <a href="{prefix}services/child-and-teen-therapy.html" class="mobile-nav__link">Child &amp; Teen Therapy</a>
  </div>
  <a href="{prefix}contact.html" class="btn btn-primary mobile-nav__cta">Book a free call</a>
</div>"""

    footer = f"""
<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <div class="footer__brand">
          <span class="footer__brand__mark" aria-hidden="true">
            <img src="{prefix}assets/images/crescita-logo-md.png" alt="" width="72" height="72">
          </span>
          <span class="brand">
            <span>Crescita</span>
            <span class="brand__dot"></span>
          </span>
        </div>
        <p class="footer__about">Trauma-informed therapy in Colorado Springs and online across Colorado. Quiet rooms, real conversations, slow work that actually holds.</p>
        <div class="footer__social">
          <a href="https://www.instagram.com/crescitameansgrowth/" aria-label="Instagram" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37zM17.5 6.5h.01"/></svg>
          </a>
          <a href="https://www.facebook.com/people/Crescita-Counseling/61565442007671/" aria-label="Facebook" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
          </a>
        </div>
      </div>
      <div>
        <p class="footer__heading">Services</p>
        <ul class="footer__list">
          <li><a href="{prefix}services/individual-therapy.html">Individual Therapy</a></li>
          <li><a href="{prefix}services/emdr-therapy.html">EMDR Therapy</a></li>
          <li><a href="{prefix}services/child-and-teen-therapy.html">Child &amp; Teen Therapy</a></li>
        </ul>
      </div>
      <div>
        <p class="footer__heading">About</p>
        <ul class="footer__list">
          <li><a href="{prefix}about.html">The practice</a></li>
          <li><a href="{prefix}team/katie-pasqualetto.html">Katie Pasqualetto</a></li>
          <li><a href="{prefix}team/alissa-brown.html">Alissa Brown</a></li>
          <li><a href="{prefix}investment.html">Rates &amp; insurance</a></li>
          <li><a href="{prefix}faq.html">FAQ</a></li>
        </ul>
      </div>
      <div>
        <p class="footer__heading">Reach us</p>
        <div class="footer__contact">
          <a href="mailto:info@crescitacounseling.com">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            info@crescitacounseling.com
          </a>
          <a href="tel:+17192860011">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            (719) 286-0011
          </a>
          <a href="https://maps.google.com/?q=627+N+Weber+St+Suite+6+Colorado+Springs+CO+80903" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            627 N Weber St, Ste 6<br>Colorado Springs, CO 80903
          </a>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> Crescita Counseling · Colorado Springs, CO</span>
      <div class="footer__legal">
        <a href="https://app.getterms.io/view/M4VkD/privacy/en-us" target="_blank" rel="noopener">Privacy</a>
        <a href="https://app.getterms.io/view/M4VkD/tos/en-us" target="_blank" rel="noopener">Terms</a>
        <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">No Surprises Act</a>
      </div>
    </div>
  </div>
</footer>

<script src="{prefix}js/main.js"></script>
</body>
</html>"""

    full = head + header + "\n\n<main id=\"main\">\n" + content + "\n</main>\n" + footer
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, "w") as f:
        f.write(full)
    print(f"  wrote {filename}")
