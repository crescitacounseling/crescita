#!/usr/bin/env python3
"""Crescita v4 — build ALL pages in one run."""
import os, json, re

SITE = "https://www.crescitacounseling.com"

# ── shared scaffold ──────────────────────────────────────────────────────────
def page(*, out, depth=0, title, desc, canonical, schema=None, body, nav=""):
    p = "../" * depth
    sd = f'<script type="application/ld+json">\n{json.dumps(schema,ensure_ascii=False)}\n</script>' if schema else ""
    def ac(t): return ' aria-current="page"' if nav==t else ""

    header = f"""<header class="site-header">
  <div class="container">
    <div class="site-header__inner">
      <a href="{p}index.html" class="brand" aria-label="Crescita Counseling">
        <span>Crescita</span><span class="brand__dot" aria-hidden="true"></span>
        <span class="brand__sub">counseling</span>
      </a>
      <nav class="nav" aria-label="Primary">
        <a href="{p}index.html" class="nav-link"{ac("home")}>Home</a>
        <a href="{p}about.html" class="nav-link"{ac("about")}>About</a>
        <div class="nav-item">
          <button class="nav-link" aria-haspopup="true">Services <span class="nav-link__caret">▾</span></button>
          <div class="nav-dropdown">
            <a href="{p}services/individual-therapy.html" class="nav-dropdown__link">Individual Therapy</a>
            <a href="{p}services/emdr-therapy.html" class="nav-dropdown__link">EMDR Therapy</a>
            <a href="{p}services/child-and-teen-therapy.html" class="nav-dropdown__link">Child &amp; Teen Therapy</a>
          </div>
        </div>
        <a href="{p}investment.html" class="nav-link"{ac("investment")}>Rates</a>
        <a href="{p}faq.html" class="nav-link"{ac("faq")}>FAQ</a>
        <a href="{p}contact.html" class="nav-link"{ac("contact")}>Contact</a>
      </nav>
      <div class="header-cta">
        <a href="{p}contact.html" class="btn btn-primary">Book a call</a>
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
    <a href="{p}index.html" class="mobile-nav__link"{ac("home")}>Home</a>
    <a href="{p}about.html" class="mobile-nav__link"{ac("about")}>About</a>
    <a href="{p}investment.html" class="mobile-nav__link"{ac("investment")}>Rates &amp; Insurance</a>
    <a href="{p}faq.html" class="mobile-nav__link"{ac("faq")}>FAQ</a>
    <a href="{p}contact.html" class="mobile-nav__link"{ac("contact")}>Contact</a>
  </div>
  <div class="mobile-nav__group">
    <p class="mobile-nav__heading">Services</p>
    <a href="{p}services/individual-therapy.html" class="mobile-nav__link">Individual Therapy</a>
    <a href="{p}services/emdr-therapy.html" class="mobile-nav__link">EMDR Therapy</a>
    <a href="{p}services/child-and-teen-therapy.html" class="mobile-nav__link">Child &amp; Teen Therapy</a>
  </div>
  <a href="{p}contact.html" class="btn btn-primary mobile-nav__cta">Book a free call</a>
</div>"""

    footer = f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <div class="footer__brand">
          <a href="{p}index.html" class="footer__logo" aria-label="Crescita Counseling">
            <img src="{p}assets/images/crescita-logo-md.png" alt="Crescita Counseling logo" width="80" height="80">
          </a>
          <span class="footer__wordmark">Crescita<span class="brand__dot" aria-hidden="true"></span></span>
        </div>
        <p class="footer__about">Trauma-informed therapy in Colorado Springs and online across Colorado. Quiet rooms, real conversations, slow work that holds.</p>
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
          <li><a href="{p}services/individual-therapy.html">Individual Therapy</a></li>
          <li><a href="{p}services/emdr-therapy.html">EMDR Therapy</a></li>
          <li><a href="{p}services/child-and-teen-therapy.html">Child &amp; Teen Therapy</a></li>
        </ul>
      </div>
      <div>
        <p class="footer__heading">About</p>
        <ul class="footer__list">
          <li><a href="{p}about.html">The practice</a></li>
          <li><a href="{p}team/katie-pasqualetto.html">Katie Pasqualetto</a></li>
          <li><a href="{p}team/alissa-brown.html">Alissa Brown</a></li>
          <li><a href="{p}investment.html">Rates &amp; insurance</a></li>
          <li><a href="{p}faq.html">FAQ</a></li>
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
<script src="{p}js/main.js"></script>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#A37580">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="Crescita Counseling">
<meta property="og:image" content="{SITE}/assets/images/meadow-flowers.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" type="image/png" sizes="64x64" href="{p}assets/images/crescita-logo-sm.png">
<link rel="apple-touch-icon" href="{p}assets/images/crescita-logo-md.png">
<link rel="stylesheet" href="{p}css/styles.css">
{sd}
</head>
<body>
<a href="#main" class="skip-link">Skip to content</a>
{header}
<main id="main">
{body}
</main>
{footer}
</body>
</html>"""
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out,"w") as f: f.write(html)
    print(f"  {out}")


# ── contact info reuse ────────────────────────────────────────────────────────
def contact_icons():
    return """<div style="display:flex;flex-direction:column;gap:1.1rem">
    <a href="mailto:info@crescitacounseling.com" style="display:flex;align-items:flex-start;gap:.85rem;color:var(--ink)">
      <span style="width:42px;height:42px;border-radius:50%;background:var(--blush-s);color:var(--rose-d);display:flex;align-items:center;justify-content:center;flex-shrink:0"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></span>
      <span><strong>Email</strong><br><span style="color:var(--slate)">info@crescitacounseling.com</span></span>
    </a>
    <a href="tel:+17192860011" style="display:flex;align-items:flex-start;gap:.85rem;color:var(--ink)">
      <span style="width:42px;height:42px;border-radius:50%;background:var(--blush-s);color:var(--rose-d);display:flex;align-items:center;justify-content:center;flex-shrink:0"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></span>
      <span><strong>Phone</strong><br><span style="color:var(--slate)">(719) 286-0011</span></span>
    </a>
    <a href="https://maps.google.com/?q=627+N+Weber+St+Suite+6+Colorado+Springs+CO+80903" target="_blank" rel="noopener" style="display:flex;align-items:flex-start;gap:.85rem;color:var(--ink)">
      <span style="width:42px;height:42px;border-radius:50%;background:var(--blush-s);color:var(--rose-d);display:flex;align-items:center;justify-content:center;flex-shrink:0"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
      <span><strong>Office</strong><br><span style="color:var(--slate)">627 N Weber St, Ste 6<br>Colorado Springs, CO 80903</span></span>
    </a>
  </div>"""

def cta_banner(link, headline, body_text, em="", btn_text="Book a call", bg_img="garden-gods-panoramic.jpg"):
    em_part = f" <em>{em}</em>" if em else ""
    return f"""<div class="cta-banner reveal">
  <div class="cta-banner__bg"><img src="assets/images/{bg_img}" alt="" loading="lazy"><div></div></div>
  <span class="eyebrow eyebrow--light" style="justify-content:center">&nbsp;</span>
  <h2 style="margin-top:.5rem">{headline}{em_part}</h2>
  <p>{body_text}</p>
  <div class="cta-banner__ctas">
    <a href="{link}" class="btn btn-rose">{btn_text}</a>
  </div>
</div>"""

def cta_banner_sub(link, headline, body_text, em="", btn_text="Book a call", bg_img="../assets/images/garden-gods-panoramic.jpg"):
    em_part = f" <em>{em}</em>" if em else ""
    return f"""<div class="cta-banner reveal">
  <div class="cta-banner__bg"><img src="{bg_img}" alt="" loading="lazy"><div></div></div>
  <h2 style="margin-top:0">{headline}{em_part}</h2>
  <p>{body_text}</p>
  <div class="cta-banner__ctas">
    <a href="{link}" class="btn btn-rose">{btn_text}</a>
  </div>
</div>"""

# ── ① HOMEPAGE ────────────────────────────────────────────────────────────────
home = """
  <!-- HERO -->
  <section class="hero bg-cream" style="position:relative">
    <div class="blob blob--hero-br" aria-hidden="true">
      <img src="assets/images/blob-fern.jpg" alt="">
    </div>
    <div class="container">
      <div class="hero__grid">
        <div class="hero__content">
          <span class="eyebrow eyebrow--rose reveal">Colorado Springs · Online statewide</span>
          <h1 class="hero__title reveal">Healing starts with feeling <em>seen</em> first.</h1>
          <p class="hero__lead lead reveal">
            Trauma-informed therapy for adults, teens, and kids. EMDR, parts work, the kind of conversation where you don't have to perform. <em>No worksheets. No clipboards.</em> Just real work, at your pace.
          </p>
          <div class="hero__ctas reveal">
            <a href="contact.html" class="btn btn-primary">Book a free 20-min call</a>
            <a href="about.html" class="btn-ghost">Meet the team</a>
          </div>
          <ul class="hero__bullets reveal">
            <li>Virtual statewide</li><li>In-person downtown</li><li>Free consult</li>
          </ul>
        </div>
        <div class="hero__visual reveal">
          <div class="hero__img-wrap">
            <img src="assets/images/meadow-flowers.jpg" alt="Soft Colorado wildflowers in muted rose and slate tones" width="900" height="1125">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- BRAND MOMENT -->
  <section class="brand-moment">
    <div class="brand-moment__inner reveal">
      <div class="brand-moment__logo">
        <img src="assets/images/crescita-logo-md.png" alt="Crescita Counseling — morning glory logo" width="300" height="300">
      </div>
      <span class="brand-moment__label">cres · ci · ta</span>
      <p class="brand-moment__title">An Italian noun. <em>Growth.</em></p>
      <p class="brand-moment__text">The slow, unflashy version — the kind that happens when someone finally has the space to be honest. <em>That's what this is.</em></p>
    </div>
  </section>

  <!-- PAIN -->
  <section class="section bg-cream" style="position:relative">
    <div class="blob blob--pain-bl" aria-hidden="true">
      <img src="assets/images/blob-leaf.jpg" alt="">
    </div>
    <div class="container" style="position:relative;z-index:1">
      <div class="section-head reveal">
        <span class="eyebrow">If any of this sounds like you</span>
        <h2>You've already done <em>a lot</em> of the work.</h2>
        <p>Read the books. Tried the breathing. Held it together for the people who needed you to. If the tools aren't quite reaching what's underneath — that's not a failure. That's a nervous system asking for something deeper.</p>
      </div>
      <ul class="pain-list reveal">
        <li>"I'm fine" — except I'm clearly not.</li>
        <li>Calm on the outside, alarms going off on the inside.</li>
        <li>I keep snapping at people I love, and I don't know why.</li>
        <li>I shut down before I even know what I'm feeling.</li>
        <li>I've been to therapy before. It didn't quite land.</li>
        <li>Everything looks good on paper. Something's still off.</li>
      </ul>
      <p class="reveal" style="max-width:680px;font-size:1.05rem;color:var(--slate);margin-top:2rem">
        Therapy here looks more like a real conversation than a clinical assessment. We're trained, trauma-informed, and will happily nerd out about the nervous system with you — but mostly we'll just sit with you while you figure out what's actually going on.
      </p>
    </div>
  </section>

  <!-- SERVICES -->
  <section class="section bg-white">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">Three ways in</span>
        <h2>Pick the one that fits where you are <em>right now.</em></h2>
        <p>Not sure which? Reach out — we'll talk it through and point you to the clinician most likely to fit.</p>
      </div>
      <div class="card-grid card-grid--3">
        <article class="card card--blush reveal">
          <span class="roman--lg">i.</span>
          <h3>Individual therapy</h3>
          <p>One-on-one work for adults navigating anxiety, trauma, identity, overwhelm, or the kind of stuck that's hard to name out loud. At the speed your system can actually handle.</p>
          <a href="services/individual-therapy.html" class="btn-ghost">More about individual</a>
        </article>
        <article class="card card--blush reveal">
          <span class="roman--lg">ii.</span>
          <h3>EMDR therapy</h3>
          <p>When old stuff keeps showing up in today's reactions, EMDR helps the brain finally finish processing it. Often reaches what talk therapy can't.</p>
          <a href="services/emdr-therapy.html" class="btn-ghost">More about EMDR</a>
        </article>
        <article class="card card--blush reveal">
          <span class="roman--lg">iii.</span>
          <h3>Child &amp; teen therapy</h3>
          <p>A warm space for ages 7+. We meet kids where they are — through conversation, play, or whatever they need that day.</p>
          <a href="services/child-and-teen-therapy.html" class="btn-ghost">Child &amp; teen</a>
        </article>
      </div>
    </div>
  </section>

  <!-- PARALLAX PULL QUOTE -->
  <section class="parallax parallax--gods section">
    <div class="container">
      <div class="pullquote pullquote--dark reveal">
        <span class="pullquote__label">A note from us</span>
        <blockquote>You don't need to come in with the right words. You can show up <em>exactly</em> as you are — tired, foggy, mad, not sure where to start. We'll work with that.</blockquote>
      </div>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section class="section bg-cream">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">How this actually goes</span>
        <h2>Reach out · get to it · keep going.</h2>
        <p>The hardest part is usually the first message. After that, here's what happens.</p>
      </div>
      <div class="steps">
        <div class="step reveal">
          <span class="roman--lg">i.</span>
          <h4>The first call</h4>
          <p>Twenty minutes, free, no script and no pressure.</p>
          <ul>
            <li>You tell us what's loud and what you've already tried</li>
            <li>We tell you honestly if we're the right fit — or who is</li>
            <li>If we are, we'll book your first session right there</li>
          </ul>
        </div>
        <div class="step reveal">
          <span class="roman--lg">ii.</span>
          <h4>The actual work</h4>
          <p>Weekly or biweekly, in person or online — whatever fits your real life.</p>
          <ul>
            <li>First sessions build safety and trust, not pressure</li>
            <li>We name patterns together as they show up</li>
            <li>Goals in plain English, not therapy-speak</li>
          </ul>
        </div>
        <div class="step reveal">
          <span class="roman--lg">iii.</span>
          <h4>The keep-going</h4>
          <p>Every so often we zoom out and check the map against the territory.</p>
          <ul>
            <li>Recalibrate when life rearranges (it always does)</li>
            <li>Notice what's shifted, name what's still tender</li>
            <li>Graduate when you're ready — kit in hand, not in head</li>
          </ul>
        </div>
      </div>
      <div class="text-center mt-4 reveal">
        <a href="contact.html" class="btn btn-rose">Start with the free call</a>
      </div>
    </div>
  </section>

  <!-- WHAT WE WORK WITH -->
  <section class="section bg-slate">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow eyebrow--light">What we work with</span>
        <h2>Common reasons folks find <em>their way</em> in.</h2>
        <p style="color:rgba(244,238,229,.75)">Not an exhaustive list. Plenty of clients show up just knowing something feels off.</p>
      </div>
      <div class="card-grid card-grid--3">
        <div class="card card--slate reveal"><h4>Anxiety &amp; overwhelm</h4><p>The hum that won't quit. Tight chest. Mind racing at 2 a.m. We get curious about what's underneath, not just how to mute it.</p></div>
        <div class="card card--slate reveal"><h4>Trauma &amp; triggers</h4><p>Big-T or little-t, recent or ancient. The kind of thing that hijacks your reactions and you can't talk yourself out of.</p></div>
        <div class="card card--slate reveal"><h4>People-pleasing &amp; burnout</h4><p>Saying yes when you mean no. Running on fumes for everyone else. We'll look at where it started — and what it's costing.</p></div>
        <div class="card card--slate reveal"><h4>Feeling numb or distant</h4><p>Going through the motions but far from yourself. Disconnection isn't a personality trait — usually it's protection.</p></div>
        <div class="card card--slate reveal"><h4>Teen stress &amp; regulation</h4><p>Helping young people understand what they're feeling without making them perform it for an adult.</p></div>
        <div class="card card--slate reveal"><h4>Parts work &amp; dissociation</h4><p>The parts of you that step in when things get heavy — we get to know them instead of fighting them.</p></div>
      </div>
    </div>
  </section>

  <!-- FAQ PREVIEW -->
  <section class="section bg-white">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow" style="justify-content:center">Before you reach out</span>
        <h2>Things people <em>actually</em> wonder.</h2>
      </div>
      <div class="faq-section">
        <details class="faq-item reveal"><summary>What if I don't know what I want to work on?</summary><div class="faq-item__body"><p>Totally fine. A lot of folks come in knowing something's off without being able to name it. Part of our job is helping you find the language.</p></div></details>
        <details class="faq-item reveal"><summary>Do I need to be in a crisis to come to therapy?</summary><div class="faq-item__body"><p>Not even close. The best time to do this work is before things break down — when there's enough bandwidth to actually look at what's happening.</p></div></details>
        <details class="faq-item reveal"><summary>Is everything virtual or in person?</summary><div class="faq-item__body"><p>Both. Virtual is available to anyone in Colorado. In-person is downtown Colorado Springs. Many clients do a mix.</p></div></details>
        <details class="faq-item reveal"><summary>Can EMDR really help if other therapy hasn't?</summary><div class="faq-item__body"><p>Often, yes. EMDR works with the nervous system directly — it tends to reach things talk therapy can circle around but not quite land on.</p></div></details>
        <details class="faq-item reveal"><summary>How much does this cost?</summary><div class="faq-item__body"><p>Sessions range from $120–$250 depending on type and clinician. Sliding scale available. <a href="investment.html">See full rates →</a></p></div></details>
      </div>
      <div class="text-center mt-4 reveal">
        <a href="faq.html" class="btn btn-secondary">See all the questions</a>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section">
    <div class="container">
      """ + cta_banner("contact.html","A twenty-minute call.","No commitment. No pressure to book. Just a real conversation so you know what you'd be walking into.","That's it.") + """
    </div>
  </section>
"""

page(out="index.html", nav="home",
     title="Crescita Counseling | Trauma-Informed Therapy in Colorado Springs",
     desc="Trauma-informed therapy in Colorado Springs and online. EMDR, individual, child & teen counseling. Free 20-min consult.",
     canonical="/",
     schema={"@context":"https://schema.org","@graph":[{"@type":"LocalBusiness","name":"Crescita Counseling","url":"https://www.crescitacounseling.com/","telephone":"+1-719-286-0011","email":"info@crescitacounseling.com","address":{"@type":"PostalAddress","streetAddress":"627 N Weber St, Ste 6","addressLocality":"Colorado Springs","addressRegion":"CO","postalCode":"80903","addressCountry":"US"},"sameAs":["https://www.instagram.com/crescitameansgrowth/","https://www.facebook.com/people/Crescita-Counseling/61565442007671/"]},{"@type":"WebSite","url":"https://www.crescitacounseling.com/","name":"Crescita Counseling"}]},
     body=home)

# ── ② ABOUT ──────────────────────────────────────────────────────────────────
about = """
  <section class="page-hero page-hero--dark" style="min-height:440px;display:flex;align-items:flex-end">
    <div class="page-hero__img">
      <img src="assets/images/soft-botanicals.jpg" alt="" loading="eager">
    </div>
    <div class="container" style="padding-bottom:3rem">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="index.html">Home</a><span>/</span><strong>About</strong></nav>
        <span class="eyebrow eyebrow--light reveal">About the practice</span>
        <h1 class="page-hero__title reveal">Therapy that feels like a <em>real conversation</em>.</h1>
        <p class="page-hero__lead page-hero--dark reveal">No clipboards. No worksheets that look like the SAT. Just trained, trauma-informed people you can actually talk to.</p>
      </div>
    </div>
  </section>

  <section class="section bg-white" style="position:relative;overflow:hidden">
    <div class="blob blob--about-tr" aria-hidden="true"><img src="assets/images/blob-fern.jpg" alt=""></div>
    <div class="container" style="position:relative;z-index:1">
      <div class="two-col">
        <div class="two-col__media reveal">
          <img src="assets/images/abstract-watercolor.jpg" alt="Abstract watercolor shapes in dusty rose, taupe, and slate" loading="lazy">
        </div>
        <div class="prose reveal">
          <span class="eyebrow">Why we do this</span>
          <h2 style="margin-top:1rem">Crescita means <em>growth</em>.</h2>
          <p>The name's a nod to the slow, unflashy version of growth — the kind that happens when someone finally has the space to be honest. Not the kind that looks good on a graphic.</p>
          <p>We built this practice because most of our clients didn't need more coping skills. They'd read the books. They'd done CBT. They were exhausted from being <em>resilient</em>. What they needed was somewhere safe enough to put the armor down for fifty minutes a week.</p>
          <p>That's what this is.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="parallax parallax--flowers section">
    <div class="container">
      <div class="pullquote pullquote--dark reveal">
        <span class="pullquote__label">What we believe</span>
        <blockquote>Your nervous system isn't broken. It's been doing <em>exactly</em> what it was set up to do. The work isn't fixing it — it's helping it learn the danger is over.</blockquote>
      </div>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">How we work</span>
        <h2>A few things we mean when we say <em>trauma-informed</em>.</h2>
      </div>
      <div class="card-grid card-grid--3">
        <div class="card card--cream reveal"><span class="roman--lg">i.</span><h4>Pace is yours</h4><p>We never push faster than your system can integrate. If we hit a wall, we slow down or back up. That's the work, not a setback.</p></div>
        <div class="card card--cream reveal"><span class="roman--lg">ii.</span><h4>Bodies count</h4><p>Talk therapy alone doesn't always reach the places trauma lives. We work somatically and with EMDR when that's what's actually needed.</p></div>
        <div class="card card--cream reveal"><span class="roman--lg">iii.</span><h4>Real over polished</h4><p>You don't have to perform. You can swear, cry, blank out, change your mind mid-sentence. We've seen all of it. None of it scares us off.</p></div>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">The team</span>
        <h2>Two clinicians. <em>Same posture.</em></h2>
        <p>Both trained in trauma-informed care. Both bring warmth, humor, and steady presence. If you're not sure who to start with, we can help match you.</p>
      </div>
      <div class="team-grid">
        <article class="therapist-card reveal">
          <a href="team/katie-pasqualetto.html" class="therapist-card__img" aria-label="Read more about Katie">
            <img src="https://images.squarespace-cdn.com/content/v1/664bb8dbe6641260d9a4f5af/c2e1a1ca-b4d2-4994-8ea7-b73e70188509/%231.jpg?format=600w" alt="Katie Pasqualetto, licensed therapist and practice owner" loading="lazy">
          </a>
          <div>
            <p class="therapist-card__role">Practice owner · LPC, EMDR-trained</p>
            <h3><a href="team/katie-pasqualetto.html" style="color:inherit">Katie Pasqualetto</a></h3>
            <p><strong>Works with:</strong> complex trauma, EMDR, dissociation, parts work, perfectionism, identity, the high-functioning version of "I'm fine."</p>
            <a href="team/katie-pasqualetto.html" class="btn-ghost">Meet Katie</a>
          </div>
        </article>
        <article class="therapist-card reveal">
          <a href="team/alissa-brown.html" class="therapist-card__img" aria-label="Read more about Alissa">
            <img src="assets/images/alissa-brown.jpg" alt="Alissa Brown, pre-licensed therapist" loading="lazy">
          </a>
          <div>
            <p class="therapist-card__role">Pre-licensed therapist · LPCC</p>
            <h3><a href="team/alissa-brown.html" style="color:inherit">Alissa Brown</a></h3>
            <p><strong>Works with:</strong> kids and teens, anxiety, military families, parenting, school stress, the postpartum stretch nobody warned you about.</p>
            <a href="team/alissa-brown.html" class="btn-ghost">Meet Alissa</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">""" + cta_banner("contact.html","Not sure who's the right fit?","Tell us a little about what you're hoping to work on. We'll pair you with the right clinician — or be honest if it's someone outside our practice.","","Book a free call","garden-gods-panoramic.jpg") + """</div>
  </section>
"""

page(out="about.html", nav="about",
     title="About Crescita Counseling | Colorado Springs Therapy Practice",
     desc="A trauma-informed therapy practice in Colorado Springs. Real conversation, not clipboards. Meet the team behind Crescita.",
     canonical="/about.html",
     body=about)

# ── ③ KATIE ──────────────────────────────────────────────────────────────────
katie = """
  <section class="page-hero page-hero--dark" style="min-height:400px;display:flex;align-items:flex-end">
    <div class="page-hero__img"><img src="assets/images/creek-forest.jpg" alt="" loading="eager"></div>
    <div class="container" style="padding-bottom:3rem">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><a href="../about.html">About</a><span>/</span><strong>Katie</strong></nav>
        <span class="eyebrow eyebrow--light reveal">Practice owner · LPC, EMDR-trained</span>
        <h1 class="page-hero__title reveal">Hi — I'm <em>Katie.</em></h1>
        <p class="page-hero__lead page-hero--dark reveal">In-person in downtown Colorado Springs. Online anywhere in Colorado.</p>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="two-col">
        <div class="two-col__media reveal">
          <img src="https://images.squarespace-cdn.com/content/v1/664bb8dbe6641260d9a4f5af/fca2ce37-bed5-4f1e-b224-14843787272a/PHOTO-2024-07-09-19-34-07+2.jpg?format=900w" alt="Katie smiling on a couch with a pink mug and a plant" loading="lazy">
        </div>
        <div class="prose reveal">
          <p>Trauma therapist, EMDR enthusiast, owner of Crescita, dog mom to a Wheaten terrier named Keith (he knows he's the main character), fall person, British TV apologist.</p>
          <p>Before this I was a school counselor. I loved supporting kids and teens, but I kept craving the kind of conversation where someone could finally slow down — and really say the hard thing. Becoming a therapist gave me room to sit in those moments instead of running past them.</p>
          <p>Clients describe me as <em>funny, grounding, and weirdly calming</em>. I can sit with heavy things without making them heavier, and I'll use a bit of dark humor if it helps you feel less alone in the room. No judgment, no rushing. Whatever shows up — even "I don't know what I'm feeling" — we work with it.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container-t prose reveal">
      <h2>How I work</h2>
      <p>My main tools are <strong>EMDR, parts work, somatic awareness, and trauma-informed relational therapy</strong>. I work mostly with adults navigating childhood trauma, dissociation, perfectionism, identity stuff, and long-standing patterns that don't budge no matter how many books they've read.</p>
      <p>I'm especially good with folks who overthink, shut down, or use humor as a shield — trust me, you're in excellent company. The work usually starts with understanding why your nervous system is doing what it's doing, because once that makes sense, the rest gets a lot more workable.</p>
      <p>Outside of sessions: hiking, traveling (22 countries and counting), reading too much, picking up hobbies that rotate weekly, and being unreasonably excited about fresh snow.</p>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="two-col two-col--flip">
        <div class="reveal">
          <span class="eyebrow eyebrow--rose">Specialties</span>
          <h2 style="margin:1rem 0 1.5rem">What I love working on</h2>
          <ul class="pill-list">
            <li>EMDR therapy</li><li>Complex trauma</li><li>Dissociation</li>
            <li>Parts work · IFS-informed</li><li>Childhood wounds</li>
            <li>Perfectionism</li><li>People-pleasing</li><li>Anxiety &amp; overwhelm</li>
            <li>Identity &amp; self-worth</li><li>Relationship patterns</li>
            <li>Life transitions</li><li>Somatic awareness</li>
          </ul>
          <h3 style="margin-top:2rem;margin-bottom:.75rem;font-size:1.25rem">Credentials</h3>
          <ul class="prose" style="margin:0">
            <li>Licensed Professional Counselor (LPC)</li>
            <li>EMDR-Trained (EMDRIA Institute)</li>
            <li>M.A., Human Services &amp; Counseling — UCCS</li>
            <li>B.S., Sociology — UCCS · Former school counselor</li>
          </ul>
          <a href="../contact.html" class="btn btn-rose" style="margin-top:1.75rem">Book with Katie</a>
        </div>
        <div class="two-col__media reveal">
          <img src="https://images.squarespace-cdn.com/content/v1/664bb8dbe6641260d9a4f5af/2093881f-0d75-459b-8c49-4ad4faca5c83/%234.jpg?format=900w" alt="Katie in a blue blazer on the steps of a house, smiling" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">""" + cta_banner_sub("../contact.html","Let's see if we're a fit.","Free twenty-minute call. No pitch, no homework. Just a real conversation.","","Reach out","../assets/images/mountains-wide.jpg") + """</div>
  </section>
"""

page(out="team/katie-pasqualetto.html", depth=1,
     title="Katie Pasqualetto, LPC | EMDR & Trauma Therapy in Colorado",
     desc="EMDR and trauma therapy with Katie Pasqualetto, LPC. Practice owner at Crescita Counseling. In-person Colorado Springs, virtual statewide.",
     canonical="/team/katie-pasqualetto.html",
     body=katie)

# ── ④ ALISSA ─────────────────────────────────────────────────────────────────
alissa = """
  <section class="page-hero page-hero--dark" style="min-height:400px;display:flex;align-items:flex-end">
    <div class="page-hero__img"><img src="../assets/images/clouds-pink.jpg" alt="" loading="eager"></div>
    <div class="container" style="padding-bottom:3rem">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><a href="../about.html">About</a><span>/</span><strong>Alissa</strong></nav>
        <span class="eyebrow eyebrow--light reveal">Pre-licensed therapist · LPCC</span>
        <h1 class="page-hero__title reveal">Hi — I'm <em>Alissa.</em></h1>
        <p class="page-hero__lead reveal" style="color:rgba(244,238,229,.82)">In-person in downtown Colorado Springs. Online anywhere in Colorado.</p>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="two-col">
        <div class="two-col__media reveal">
          <img src="../assets/images/alissa-brown.jpg" alt="Alissa Brown smiling outdoors in soft afternoon light" loading="lazy">
        </div>
        <div class="prose reveal">
          <p>Therapist, school counselor, mom of four (twins included, yes really), and someone who genuinely believes the outdoors can do half a session's worth of work on a good day.</p>
          <p>A professor told me early on I was made for this work, and she was right. I started in school settings — especially with military-connected families — and kept noticing the moments where someone exhaled because they felt actually <em>heard</em>. Those stayed with me. They're what pulled me into therapy.</p>
          <p>Clients describe me as <em>warm, calm, and grounded</em>. I'm a listener first. I won't perform analysis at you — I'll just be in it with you while you sort through whatever's loud right now. Bring the mess. Bring the "I don't know." It's all welcome.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container-t prose reveal">
      <h2>How I work</h2>
      <p>I work systemically and humanistically, with play therapy techniques mixed in for younger clients, and a trauma-informed lens throughout. I support <strong>children, teens, and adults</strong> navigating anxiety, depression, identity, relationships, and the very particular pressures military families carry.</p>
      <p>I have a real soft spot for <strong>teenagers</strong> — their honesty is medicine — and for <strong>moms</strong> trying to remember who they are underneath the role. My hope is that you leave each session a little lighter, a little more recognizable to yourself.</p>
      <p>When I'm not in session: hiking Colorado trails, family time, and slowly easing back into backpacking after a long pause.</p>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <span class="eyebrow eyebrow--rose">Specialties</span>
      <h2 style="margin:1rem 0 1.5rem">What I love working on</h2>
      <ul class="pill-list reveal">
        <li>Children &amp; adolescents</li><li>Anxiety</li><li>Depression</li>
        <li>Military families</li><li>Parenting support</li><li>Family stressors</li>
        <li>School-related challenges</li><li>Emotional regulation</li>
        <li>Life transitions</li><li>Identity</li><li>Play-therapy techniques</li>
      </ul>
      <h3 style="margin-top:2rem;margin-bottom:.75rem;font-size:1.25rem">Credentials</h3>
      <ul class="prose reveal" style="margin:0 0 1.75rem">
        <li>Licensed Professional Counselor Candidate (LPCC)</li>
        <li>School Counselor</li>
        <li>M.A., Human Services &amp; Counseling — UCCS</li>
        <li>B.A., Sociology &amp; Communications Studies</li>
      </ul>
      <a href="../contact.html" class="btn btn-rose reveal">Book with Alissa</a>
    </div>
  </section>

  <section class="section">
    <div class="container">""" + cta_banner_sub("../contact.html","Let's start with a call.","Twenty minutes, free. We'll see if I'm the right fit for what you're carrying.","","Reach out","../assets/images/wildflower-scatter.jpg") + """</div>
  </section>
"""

page(out="team/alissa-brown.html", depth=1,
     title="Alissa Brown, LPCC | Therapy for Kids, Teens & Military Families",
     desc="Therapy with Alissa Brown, LPCC — children, teens, military families, anxiety, and parenting support. Colorado Springs and virtual statewide.",
     canonical="/team/alissa-brown.html",
     body=alissa)

# ── ⑤ INDIVIDUAL THERAPY ─────────────────────────────────────────────────────
individual = """
  <section class="page-hero page-hero--dark" style="min-height:420px;display:flex;align-items:flex-end">
    <div class="page-hero__img"><img src="../assets/images/mountains-wide.jpg" alt="" loading="eager"></div>
    <div class="container" style="padding-bottom:3rem">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><strong>Individual therapy</strong></nav>
        <span class="eyebrow eyebrow--light reveal">Individual therapy · in person + virtual</span>
        <h1 class="page-hero__title reveal">A room where you can <em>actually exhale.</em></h1>
        <p class="page-hero__lead reveal" style="color:rgba(244,238,229,.82)">One-on-one therapy for adults who've held it together for everyone else and want fifty minutes a week to stop performing.</p>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container-t prose reveal">
      <p>Most folks who come in for individual therapy aren't in crisis — they're just <em>tired</em>. Tired of overthinking, of saying yes when they mean no, of feeling like there's a version of themselves they keep almost reaching.</p>
      <p>This is the space to slow that down. To understand the patterns underneath the patterns. To get to know the parts of you that have been working overtime, and give them somewhere to set things down.</p>
      <p>No worksheets. No script. We follow what's loud, get curious about what's quiet, and go at the pace your nervous system can actually hold.</p>
      <p><a href="../contact.html" class="text-link">If that sounds about right, here's how to start.</a></p>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container">
      <div class="two-col">
        <div class="reveal">
          <span class="eyebrow eyebrow--rose">In the room</span>
          <h2 style="margin:1rem 0 1.5rem">What this <em>actually</em> looks like</h2>
          <ul class="prose" style="margin:0">
            <li>Real conversation about what's loud this week and what's underneath it</li>
            <li>Getting curious about reactions that don't make logical sense</li>
            <li>Noticing the parts of you that step in when things get heavy</li>
            <li>Building enough safety to feel what you've been outrunning</li>
            <li>Naming things in plain English — yours, not therapy-speak</li>
            <li>Tools that fit your life, not tools that turn you into a project</li>
          </ul>
        </div>
        <div class="two-col__media reveal">
          <img src="../assets/images/water-ripples.jpg" alt="Gentle, calm water ripples in soft slate-blue light" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="two-col two-col--flip">
        <div class="reveal">
          <span class="eyebrow">Who finds their way in</span>
          <h2 style="margin:1rem 0 1.5rem">A few common reasons</h2>
          <ul class="pill-list">
            <li>Anxiety that won't quit</li><li>Old trauma in current life</li>
            <li>Feeling stuck or numb</li><li>People-pleasing</li>
            <li>Perfectionism</li><li>Dissociation</li>
            <li>Relationship patterns</li><li>Low self-worth</li>
            <li>Life transitions</li><li>Identity questions</li>
            <li>Overwhelm without a clear cause</li>
            <li>"I don't know what's wrong, exactly"</li>
          </ul>
        </div>
        <div class="two-col__media reveal">
          <img src="../assets/images/river-stones.jpg" alt="Smooth river stones in dusty rose, slate, and cream tones" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="parallax parallax--clouds section">
    <div class="container">
      <div class="pullquote pullquote--dark reveal">
        <span class="pullquote__label">A reminder</span>
        <blockquote>You don't need a diagnosis or a clear list of goals to start. Showing up with <em>"something feels off"</em> is enough.</blockquote>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">Looking for something else?</span>
        <h2>Two other ways in.</h2>
      </div>
      <div class="card-grid card-grid--2" style="max-width:860px;margin:0 auto">
        <article class="card card--blush reveal"><span class="roman--lg">ii.</span><h3>EMDR therapy</h3><p>When old experiences keep showing up in present-day reactions — EMDR helps the brain finally finish processing them.</p><a href="emdr-therapy.html" class="btn-ghost">More about EMDR</a></article>
        <article class="card card--blush reveal"><span class="roman--lg">iii.</span><h3>Child &amp; teen therapy</h3><p>Age-appropriate support for young people navigating anxiety, big feelings, and changes that don't have easy words yet.</p><a href="child-and-teen-therapy.html" class="btn-ghost">Child &amp; teen</a></article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">""" + cta_banner_sub("../contact.html","Ready when you are.","Twenty-minute call, free. We talk about what's bringing you in, you ask anything you want, and you decide if it feels like a fit.","","Book the call") + """</div>
  </section>
"""

page(out="services/individual-therapy.html", depth=1,
     title="Individual Therapy in Colorado Springs | Crescita Counseling",
     desc="Individual therapy for adults navigating anxiety, trauma, overwhelm, identity, and the stuck stuff. In-person Colorado Springs or online statewide.",
     canonical="/services/individual-therapy.html",
     body=individual)

# ── ⑥ EMDR ───────────────────────────────────────────────────────────────────
emdr = """
  <section class="page-hero page-hero--dark" style="min-height:440px;display:flex;align-items:flex-end">
    <div class="page-hero__img"><img src="../assets/images/clouds-pink.jpg" alt="" loading="eager"></div>
    <div class="container" style="padding-bottom:3rem">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><strong>EMDR therapy</strong></nav>
        <span class="eyebrow eyebrow--light reveal">EMDR therapy · in person + virtual</span>
        <h1 class="page-hero__title reveal">When the past keeps showing up in the <em>present.</em></h1>
        <p class="page-hero__lead reveal" style="color:rgba(244,238,229,.82)">EMDR helps your brain finish processing the experiences that still steer today's reactions — gently, at your pace.</p>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container-t prose reveal">
      <p>You probably already know which moments we're talking about. The ones that come up in your body before your brain catches up. The reactions that feel three sizes too big for what's actually happening. The way certain people, places, or tones still hijack you, even when you <em>know</em> you're safe.</p>
      <p>EMDR is one of the few approaches built specifically for that. Not for processing your week. For helping the nervous system finally complete something it didn't get to complete the first time.</p>
      <p>It's structured. It's well-researched. And it works with how the brain actually stores hard experiences — not just how you talk about them.</p>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container">
      <div class="two-col">
        <div class="reveal">
          <span class="eyebrow eyebrow--rose">What it is</span>
          <h2 style="margin:1rem 0 1.25rem">Not talk therapy. <em>Nervous system therapy.</em></h2>
          <p class="lead" style="font-size:1.15rem;margin-bottom:1.25rem">Using guided eye movements or bilateral stimulation, EMDR activates the brain's natural processing system — the one that runs while you sleep.</p>
          <p style="color:var(--slate)">Old experiences get filed away properly instead of looping unresolved in the background. You don't have to retell every detail. You don't have to convince yourself you're over it. The work happens at a level underneath the story.</p>
        </div>
        <div class="two-col__media reveal">
          <img src="../assets/images/water-ripples.jpg" alt="Calm water surface in slate-blue and cream tones" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">Why folks pick it</span>
        <h2>EMDR works <em>differently</em> than what most people have tried.</h2>
      </div>
      <div class="card-grid card-grid--3">
        <div class="card card--blush reveal"><span class="roman--lg">i.</span><h4>It respects your pace</h4><p>You're never pushed past what your system can hold. If we hit a wall, we slow down. That's part of the protocol, not a setback.</p></div>
        <div class="card card--blush reveal"><span class="roman--lg">ii.</span><h4>It works with the body</h4><p>Talk therapy circles the issue. EMDR goes underneath it — to where trauma actually lives, which is rarely just in language.</p></div>
        <div class="card card--blush reveal"><span class="roman--lg">iii.</span><h4>The shifts tend to hold</h4><p>Folks often describe relief that feels structural, not temporary. The memory doesn't disappear — but it stops driving the bus.</p></div>
      </div>
    </div>
  </section>

  <section class="section bg-slate">
    <div class="container-t prose reveal" style="color:rgba(244,238,229,.85)">
      <span class="eyebrow eyebrow--light">The eight phases</span>
      <h2 style="color:var(--cream);margin:1rem 0 1.25rem">How EMDR <em>actually</em> goes.</h2>
      <ol>
        <li><strong style="color:var(--cream)">History &amp; planning</strong> — getting clear on what you've been carrying.</li>
        <li><strong style="color:var(--cream)">Preparation</strong> — building grounding skills and trust before we go anywhere heavy.</li>
        <li><strong style="color:var(--cream)">Assessment</strong> — identifying a memory or pattern to work on.</li>
        <li><strong style="color:var(--cream)">Desensitization</strong> — bilateral stimulation takes the emotional charge down.</li>
        <li><strong style="color:var(--cream)">Installation</strong> — reinforcing the more accurate belief that wants to take its place.</li>
        <li><strong style="color:var(--cream)">Body scan</strong> — checking where your body is still holding it.</li>
        <li><strong style="color:var(--cream)">Closure</strong> — making sure you leave grounded, not raw.</li>
        <li><strong style="color:var(--cream)">Reevaluation</strong> — checking progress and naming what's next.</li>
      </ol>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="two-col two-col--flip">
        <div class="reveal">
          <span class="eyebrow">EMDR is effective for:</span>
          <ul class="pill-list" style="margin-top:1rem">
            <li>Trauma &amp; PTSD</li><li>Anxiety</li><li>Chronic stress</li>
            <li>Panic</li><li>Grief &amp; loss</li><li>Relationship wounds</li>
            <li>Childhood trauma</li><li>Triggers</li><li>Dissociation</li>
            <li>Low self-worth</li><li>Performance anxiety</li>
          </ul>
          <p style="margin-top:1.5rem;color:var(--slate);font-size:1rem">Many folks who've felt stuck through other therapies find real movement here. Not because it's magic — because it's the right tool for what's actually in the way.</p>
        </div>
        <div class="two-col__media reveal">
          <img src="../assets/images/garden-gods-pine.jpg" alt="Pine tree growing from red rock in the Garden of the Gods, Colorado Springs" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">""" + cta_banner_sub("../contact.html","Curious if EMDR is a fit?","Book a free call and we'll talk through what's been happening. If EMDR's the right next step, we'll walk you through what that looks like.","","Book a call","../assets/images/mountains-wide.jpg") + """</div>
  </section>
"""

page(out="services/emdr-therapy.html", depth=1,
     title="EMDR Therapy in Colorado Springs | Crescita Counseling",
     desc="EMDR therapy in Colorado Springs and online statewide. Evidence-based trauma reprocessing for anxiety, PTSD, and triggers that feel stuck.",
     canonical="/services/emdr-therapy.html",
     body=emdr)

# ── ⑦ CHILD & TEEN ───────────────────────────────────────────────────────────
child = """
  <section class="page-hero page-hero--dark" style="min-height:420px;display:flex;align-items:flex-end">
    <div class="page-hero__img"><img src="../assets/images/garden-gods-window.jpg" alt="" loading="eager"></div>
    <div class="container" style="padding-bottom:3rem">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><strong>Child &amp; teen therapy</strong></nav>
        <span class="eyebrow eyebrow--light reveal">Child &amp; teen therapy · ages 7+</span>
        <h1 class="page-hero__title reveal">Where kids and teens get to <em>actually be heard.</em></h1>
        <p class="page-hero__lead reveal" style="color:rgba(244,238,229,.82)">A warm space for the things they can't quite say at the dinner table yet — through conversation, play, or whatever helps the words come.</p>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container-t prose reveal">
      <p>Kids and teens have inner lives just as full as ours. They just don't always have the vocabulary yet — and they almost never have a space where the adults aren't grading them.</p>
      <p>That's what this is: somewhere your child can talk freely, work things out at their own pace, and not have to perform "fine" for anyone. We work with what they show up with — conversation, play, art, silence, whatever helps that day.</p>
      <p>We also loop you in. <strong>You're not on the outside of this work</strong>. We share what's appropriate, give you context, and help you respond at home in ways that line up with what's happening in the room.</p>
      <p><a href="../contact.html" class="text-link">If your kid needs a place to land — here's how to start.</a></p>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container">
      <div class="two-col">
        <div class="reveal">
          <span class="eyebrow eyebrow--rose">Why it helps</span>
          <h2 style="margin:1rem 0 1.5rem">A few things therapy <em>actually</em> gives them</h2>
          <ul class="prose" style="margin:0">
            <li>A safe adult who isn't their parent or teacher</li>
            <li>Language for feelings they can't quite name yet</li>
            <li>Tools that fit their actual life, not just a worksheet</li>
            <li>Space to process changes that snuck up on them</li>
            <li>Less shame about being big, sensitive, anxious, or different</li>
            <li>Confidence that doesn't depend on performing</li>
          </ul>
        </div>
        <div class="two-col__media reveal">
          <img src="../assets/images/garden-gods-pine.jpg" alt="Pine tree on red rocks at Garden of the Gods, Colorado Springs" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">For caregivers</span>
        <h2>You don't have to figure this out <em>alone.</em></h2>
        <p>Parenting a kid in distress is exhausting in a very particular way. We don't just work with your child — we work with the system around them.</p>
      </div>
      <div class="card-grid card-grid--3">
        <div class="card card--blush reveal"><span class="roman--lg">i.</span><h4>Ages 7+</h4><p>School-age kids, tweens, teens, and young adults. We'll match you with whoever's best suited to your kid's age and what's going on.</p></div>
        <div class="card card--blush reveal"><span class="roman--lg">ii.</span><h4>Anxiety &amp; regulation</h4><p>Big feelings, racing minds, perfectionism, school stress. We help young people understand what their bodies are doing — and build tools that actually work.</p></div>
        <div class="card card--blush reveal"><span class="roman--lg">iii.</span><h4>Real transitions</h4><p>Moves, divorce, new schools, deployments, loss. The kind of things kids feel deeply and don't always have language for yet.</p></div>
      </div>
    </div>
  </section>

  <section class="parallax parallax--gods section">
    <div class="container">
      <div class="pullquote pullquote--dark reveal">
        <span class="pullquote__label">For the parent reading this</span>
        <blockquote>If you're not sure whether to reach out — <em>reach out.</em> The free call is for you too. We'll tell you honestly whether therapy is the right next step.</blockquote>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">""" + cta_banner_sub("../contact.html","For your kid. For your family.","Book a free twenty-minute call. Ask anything. We'll help you figure out if this is the right move.","","Reach out","../assets/images/wildflower-scatter.jpg") + """</div>
  </section>
"""

page(out="services/child-and-teen-therapy.html", depth=1,
     title="Child & Teen Therapy in Colorado Springs | Crescita Counseling",
     desc="Therapy for children and teens (ages 7+) in Colorado Springs and online statewide. Anxiety, emotional regulation, school stress, and big transitions.",
     canonical="/services/child-and-teen-therapy.html",
     body=child)

# ── ⑧ INVESTMENT ─────────────────────────────────────────────────────────────
investment = """
  <section class="page-hero page-hero--dark" style="min-height:380px;display:flex;align-items:flex-end">
    <div class="page-hero__img"><img src="assets/images/river-stones.jpg" alt="" loading="eager"></div>
    <div class="container" style="padding-bottom:3rem">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="index.html">Home</a><span>/</span><strong>Rates &amp; insurance</strong></nav>
        <span class="eyebrow eyebrow--light reveal">Investment</span>
        <h1 class="page-hero__title reveal">Transparent rates. <em>Real options.</em></h1>
        <p class="page-hero__lead reveal" style="color:rgba(244,238,229,.82)">Here's what therapy costs at Crescita, how insurance works, and what's available if cost is part of the equation.</p>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Session rates</span>
        <h2>What it costs.</h2>
        <p>Straightforward fees, no surprises. Sliding scale available — just ask.</p>
      </div>
      <div class="pricing-grid">
        <div class="price-card price-card--f reveal"><p class="price-card__title">Initial intake</p><p class="price-card__price">$200<small> · up to 75 min</small></p><p>A longer first session — we get to know you, you ask anything, we map out what the work might look like.</p></div>
        <div class="price-card price-card--f reveal"><p class="price-card__title">Individual session</p><p class="price-card__price">$150<small> · 50 min</small></p><p>Standard weekly or biweekly therapy. Where most of the actual work happens.</p></div>
        <div class="price-card price-card--f reveal"><p class="price-card__title">EMDR session</p><p class="price-card__price">$250<small> · 90 min</small></p><p>Extended sessions for EMDR, dissociation, or anything that needs more runway. The longer format helps your system land safely before we close.</p></div>
        <div class="price-card price-card--f reveal"><p class="price-card__title">Pre-licensed counselor</p><p class="price-card__price">$120<small> · 50 min</small></p><p>Reduced-fee sessions with a pre-licensed clinician. Same relational, trauma-informed approach, supervised throughout.</p></div>
      </div>
      <p class="form-note reveal" style="margin-top:1.5rem;max-width:760px"><strong>Sliding fee available.</strong> If cost is in the way, ask. We'd rather have the conversation than have you not reach out.</p>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container">
      <div class="card-grid card-grid--2" style="max-width:880px;margin:0 auto">
        <div class="reveal"><span class="eyebrow eyebrow--rose">Payment</span><h3 style="margin:1rem 0">How to pay</h3><p style="color:var(--slate)">Cash, check, HSA/FSA cards, and all major credit cards. Card on file required to schedule.</p></div>
        <div class="reveal"><span class="eyebrow eyebrow--rose">Cancellation</span><h3 style="margin:1rem 0">24-hour notice</h3><p style="color:var(--slate)">Life happens — just give us a heads up. Cancellations inside 24 hours are charged the full session fee.</p></div>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="two-col">
        <div class="reveal">
          <span class="eyebrow">Insurance</span>
          <h2 style="margin:1rem 0 1.25rem">In-network &amp; Medicaid</h2>
          <p style="color:var(--slate)">We take insurance on a limited basis (including Medicaid), depending on clinician availability and the type of services you need. Coverage varies plan to plan.</p>
          <p style="color:var(--slate);margin-top:.85rem">Simplest move: <a href="contact.html" class="text-link">send us a message</a> with your plan info. We'll check what's covered and walk you through next steps.</p>
        </div>
        <div class="reveal">
          <span class="eyebrow">Out of network</span>
          <h2 style="margin:1rem 0 1.25rem">Reimbursement made easier</h2>
          <p style="color:var(--slate)">We've partnered with <strong>Mentaya</strong> to help clients use out-of-network benefits without the paperwork headache. Check eligibility in two clicks.</p>
          <a href="https://app.mentaya.com/public/practices/oMmOomBYnjxTXzgbI5gt/eligibility/widget" target="_blank" rel="noopener" class="btn btn-secondary" style="margin-top:1.25rem">Check Mentaya eligibility →</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-cream" style="text-align:center">
    <div class="container-t reveal">
      <span class="eyebrow eyebrow--rose" style="justify-content:center">Required disclosure</span>
      <h3 style="margin:1rem 0">Good Faith Estimate</h3>
      <p style="color:var(--slate)">Under the No Surprises Act, you have the right to receive a Good Faith Estimate before scheduling. <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener" class="text-link">Learn more from CMS</a>.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">""" + cta_banner("contact.html","Questions about cost?","Free call. We'll talk through what fits — insurance, sliding scale, pre-licensed options.","","Book a call") + """</div>
  </section>
"""

page(out="investment.html", nav="investment",
     title="Therapy Rates & Insurance | Crescita Counseling Colorado Springs",
     desc="Transparent therapy pricing in Colorado Springs. Rates for intake, individual, EMDR, and reduced-fee sessions. Insurance, sliding scale, and out-of-network options.",
     canonical="/investment.html",
     body=investment)

# ── ⑨ FAQ ─────────────────────────────────────────────────────────────────────
faq_items = [
  ("Getting started",[
    ("How do I book my first appointment?","Fill out the form on the <a href='contact.html'>contact page</a>. We'll respond within a business day and help you pick the right clinician and session type."),
    ("Do you offer a consultation before I commit?","Yes — <strong>free 20-minute phone consultations</strong>. Ask anything, no pressure to book afterward. <a href='contact.html'>Request one here</a>."),
    ("How do I pick a therapist?","Send us a note about what you're hoping to work on and we'll match you with the clinician whose training and style line up best."),
    ("I'm nervous about starting. Is that normal?","Completely. You don't need the right words or a clean list of goals. We'll meet you where you are."),
    ("How soon can I get in?","Availability varies. When you reach out, we'll let you know who has openings and how soon."),
  ]),
  ("Logistics",[
    ("How fast do you respond?","Within <strong>one business day</strong>. If you reach out over a weekend, you'll hear from us Monday."),
    ("Do you do virtual sessions?","Yes — secure virtual therapy is available to anyone in Colorado, including some EMDR, parts work, and child/teen sessions."),
    ("What ages do you work with?","Ages <strong>7 and up</strong>. Mention your child or teen's age on the form and we'll route you to the right person. More at the <a href='services/child-and-teen-therapy.html'>child &amp; teen page</a>."),
    ("Why is the EMDR session longer?","EMDR needs more runway — 90 minutes lets us prepare, work, and close safely without rushing your system. A 50-minute slot isn't enough."),
    ("What's the cancellation policy?","<strong>24 hours' notice</strong>. Cancellations after that are charged the full session fee."),
  ]),
  ("About therapy",[
    ("What is therapy, really?","A real conversation with a trained clinician, on purpose, regularly. A space to look at what's happening — emotions, patterns, history — without performing for the person in the room."),
    ("Do I need a diagnosis to come?","No. Plenty of folks come in because something's just <em>off</em>. That's reason enough."),
    ("What happens in the first session?","We get to know each other. You tell us what's bringing you in, your background, what's already been tried. No homework, no pressure."),
    ("How long does therapy take?","Depends on what you're working on. Some folks feel meaningful shifts in a few months. Others stay longer for deeper work. We talk about expectations as we go."),
    ("Can therapy help when nothing's technically wrong?","Yes. Often that's exactly when it's most useful — there's more bandwidth to actually look at the thing."),
    ("Will EMDR help with anxiety?","Often, yes — particularly if there's something underneath the anxiety that talk therapy hasn't quite reached. <a href='services/emdr-therapy.html'>More on EMDR</a>."),
    ("What's the difference between counseling and therapy?","We use the words interchangeably. Both mean the same thing here: showing up regularly with a trained person and doing the work."),
  ]),
]

faq_groups_html = []
faq_schema_list = []
for group, items in faq_items:
    lis = []
    for q,a in items:
        lis.append(f'<details class="faq-item reveal"><summary>{q}</summary><div class="faq-item__body"><p>{a}</p></div></details>')
        qt = re.sub(r'<[^>]+>','',q).replace('&amp;','&').strip()
        at = re.sub(r'<[^>]+>','',a).replace('&amp;','&').replace('&nbsp;',' ').strip()
        faq_schema_list.append({"@type":"Question","name":qt,"acceptedAnswer":{"@type":"Answer","text":at}})
    faq_groups_html.append(f'<div class="faq-group reveal"><h2 class="faq-group__title">{group}</h2>{"".join(lis)}</div>')

faq_body = """
  <section class="page-hero page-hero--dark" style="min-height:380px;display:flex;align-items:flex-end">
    <div class="page-hero__img"><img src="assets/images/wildflower-scatter.jpg" alt="" loading="eager"></div>
    <div class="container" style="padding-bottom:3rem">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="index.html">Home</a><span>/</span><strong>FAQ</strong></nav>
        <span class="eyebrow eyebrow--light reveal">Common questions</span>
        <h1 class="page-hero__title reveal">Stuff people <em>actually</em> wonder.</h1>
        <p class="page-hero__lead reveal" style="color:rgba(244,238,229,.82)">Real answers to the questions that come up before reaching out. If we missed yours, <a href="contact.html" style="color:var(--rose-s)">just ask</a>.</p>
      </div>
    </div>
  </section>
  <section class="section bg-white">
    <div class="container">
      <div class="faq-section">""" + "".join(faq_groups_html) + """</div>
    </div>
  </section>
  <section class="section">
    <div class="container">""" + cta_banner("contact.html","Still wondering?","The free call is usually the fastest way to get a feel for how we work. Twenty minutes, no commitment.","","Reach out") + """</div>
  </section>
"""

page(out="faq.html", nav="faq",
     title="Therapy FAQ | Crescita Counseling Colorado Springs",
     desc="Real answers about therapy, EMDR, insurance, virtual sessions, and how to get started at Crescita Counseling.",
     canonical="/faq.html",
     schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":faq_schema_list},
     body=faq_body)

# ── ⑩ CONTACT ─────────────────────────────────────────────────────────────────
contact_body = f"""
  <section class="page-hero page-hero--dark" style="min-height:380px;display:flex;align-items:flex-end">
    <div class="page-hero__img"><img src="assets/images/garden-gods-panoramic.jpg" alt="" loading="eager"></div>
    <div class="container" style="padding-bottom:3rem">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="index.html">Home</a><span>/</span><strong>Contact</strong></nav>
        <span class="eyebrow eyebrow--light reveal">Reach out</span>
        <h1 class="page-hero__title reveal">A twenty-minute call. <em>No pressure.</em></h1>
        <p class="page-hero__lead reveal" style="color:rgba(244,238,229,.82)">Fill out the form, email, or call. We read every message and write back within one business day — usually faster.</p>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="two-col">
        <div class="reveal">
          <span class="eyebrow">Other ways to say hi</span>
          <h2 style="margin:1rem 0 1.5rem">Direct lines</h2>
          {contact_icons()}
          <div style="margin-top:2rem;padding:1.25rem;background:var(--blush-s);border-radius:12px;border-left:3px solid var(--rose)">
            <p style="font-size:.93rem;color:var(--slate);margin:0;line-height:1.55"><strong style="color:var(--slate-d)">Quick privacy note:</strong> please don't share detailed medical info through this form. Save that for our secure sessions.</p>
          </div>
        </div>

        <div class="form-card reveal">
          <form data-contact-form action="https://formspree.io/f/YOUR_FORMSPREE_ID" method="POST" novalidate>
            <div class="form-row form-row--2">
              <div class="form-group"><label for="fn">First name <span class="req">*</span></label><input type="text" id="fn" name="firstName" required autocomplete="given-name"></div>
              <div class="form-group"><label for="ln">Last name <span class="req">*</span></label><input type="text" id="ln" name="lastName" required autocomplete="family-name"></div>
            </div>
            <div class="form-row form-row--2">
              <div class="form-group"><label for="em">Email <span class="req">*</span></label><input type="email" id="em" name="email" required autocomplete="email"></div>
              <div class="form-group"><label for="ph">Phone</label><input type="tel" id="ph" name="phone" autocomplete="tel"></div>
            </div>
            <div class="form-row form-row--2">
              <div class="form-group"><label for="who">Therapy is for</label><select id="who" name="who"><option value="myself">Myself</option><option value="my-child-teen">My child or teen</option><option value="myself-and-child">Myself and my child/teen</option><option value="someone-else">Someone else</option></select></div>
              <div class="form-group"><label for="fmt">Preferred format</label><select id="fmt" name="format"><option value="no-preference">No preference</option><option value="in-person">In-person (Colorado Springs)</option><option value="virtual">Virtual</option></select></div>
            </div>
            <div class="form-group" style="margin-bottom:1rem"><label for="svc">What you're curious about</label><select id="svc" name="interest"><option value="not-sure">Not sure yet</option><option value="individual">Individual therapy</option><option value="emdr">EMDR therapy</option><option value="child-teen">Child &amp; teen therapy</option></select></div>
            <div class="form-group" style="margin-bottom:1rem"><label for="msg">What's loud right now? <span class="req">*</span></label><textarea id="msg" name="message" required placeholder="A few sentences is plenty. We'll follow up to talk more."></textarea></div>
            <label class="form-checkbox" style="margin-bottom:1.25rem"><input type="checkbox" name="consent" required><span>I understand my submission will be reviewed by Crescita Counseling and that I shouldn't share detailed medical information through this form.</span></label>
            <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px">
            <button type="submit" class="btn btn-rose" style="width:100%">Send message</button>
            <div class="form-status" data-form-status role="status" aria-live="polite"></div>
          </form>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">Where we are</span>
        <h2>Downtown Colorado Springs</h2>
        <p>Easy access from across the Pikes Peak region. Virtual everywhere else in Colorado.</p>
      </div>
      <div style="max-width:1080px;margin:0 auto;border-radius:20px;overflow:hidden;border:1px solid var(--line)" class="reveal">
        <iframe src="https://www.google.com/maps?q=627+N+Weber+St+Suite+6+Colorado+Springs+CO+80903&output=embed" width="100%" height="400" style="border:0;display:block" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Crescita Counseling location"></iframe>
      </div>
    </div>
  </section>
"""

page(out="contact.html", nav="contact",
     title="Contact Crescita Counseling | Colorado Springs Therapy",
     desc="Get in touch with Crescita Counseling to schedule a free 20-minute consult or ask anything about therapy, EMDR, or child & teen work.",
     canonical="/contact.html",
     schema={"@context":"https://schema.org","@type":"ContactPage","url":"https://www.crescitacounseling.com/contact.html","mainEntity":{"@type":"LocalBusiness","name":"Crescita Counseling","telephone":"+1-719-286-0011","email":"info@crescitacounseling.com","address":{"@type":"PostalAddress","streetAddress":"627 N Weber St, Ste 6","addressLocality":"Colorado Springs","addressRegion":"CO","postalCode":"80903","addressCountry":"US"}}},
     body=contact_body)

# ── ⑪ 404 ────────────────────────────────────────────────────────────────────
page(out="404.html",
     title="Page Not Found | Crescita Counseling",
     desc="This page wandered off. Head back to Crescita Counseling.",
     canonical="/404.html",
     body="""<section class="error-page">
  <div>
    <div class="error-num">404.</div>
    <p>This page wandered off into the mountains. Let's get you back.</p>
    <div style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap">
      <a href="index.html" class="btn btn-primary">Back to home</a>
      <a href="contact.html" class="btn btn-secondary">Contact us</a>
    </div>
  </div>
</section>""")

print("All 11 pages done.")
