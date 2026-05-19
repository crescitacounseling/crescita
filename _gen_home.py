#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _build import build_page

home_content = """
  <!-- ========== HERO ========== -->
  <section class="hero">
    <span class="blob-accent blob-accent--hero" aria-hidden="true">
      <img src="assets/images/blob-fern.jpg" alt="" loading="eager">
    </span>
    <div class="container">
      <div class="hero__grid">
        <div class="hero__content">
          <span class="eyebrow eyebrow--rose reveal">Colorado Springs · Online statewide</span>
          <h1 class="hero__title reveal">
            Healing starts with feeling <em>seen</em> first.
          </h1>
          <p class="hero__lead reveal">
            Trauma-informed therapy for adults, teens, and kids. EMDR, parts work, the kind of conversation where you don't have to perform. <em>No worksheets. No clipboards.</em> Just real work, at your pace.
          </p>
          <div class="hero__ctas reveal">
            <a href="contact.html" class="btn btn-primary">Book a free 20-min call</a>
            <a href="about.html" class="btn-ghost">Meet the team</a>
          </div>
          <ul class="hero__bullets reveal">
            <li>Virtual statewide</li>
            <li>In-person downtown</li>
            <li>Free consult</li>
          </ul>
        </div>

        <div class="hero__visual reveal">
          <div class="hero__visual-img">
            <img src="assets/images/wildflowers.jpg" alt="Soft Colorado wildflowers in dusty rose and slate tones" width="900" height="1125">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========== BRAND MOMENT ========== -->
  <section class="brand-moment">
    <div class="brand-moment__bg" aria-hidden="true"></div>
    <div class="brand-moment__inner reveal">
      <div class="brand-moment__mark">
        <img src="assets/images/crescita-logo-md.png" alt="Crescita Counseling logo — purple morning glory bouquet in a green circle" width="280" height="280">
      </div>
      <span class="brand-moment__label">cres·ci·ta</span>
      <p class="brand-moment__title">A noun, from the Italian. <em>Growth.</em></p>
      <p class="brand-moment__text">The slow, unflashy version — the kind that happens when someone finally has the space to be honest. That's what this is.</p>
    </div>
  </section>

  <!-- ========== PAIN / SEEN ========== -->
  <section class="section">
    <div class="container">
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

      <p class="reveal" style="max-width:680px;font-size:1.08rem;color:var(--slate);margin-top:2rem">
        Therapy here looks more like a real conversation than a clinical assessment. We're trained, we're trauma-informed, and we'll happily nerd out about the nervous system with you — but mostly we'll just sit with you while you figure out what's actually going on.
      </p>
    </div>
  </section>

  <!-- ========== SERVICES ========== -->
  <section class="section bg-cream-deep">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">Three ways in</span>
        <h2>Pick the one that fits where you are <em>right now.</em></h2>
        <p>Not sure which? Reach out — we'll talk it through and point you to the clinician most likely to be a fit. Even if that's someone outside our practice.</p>
      </div>

      <div class="card-grid card-grid--3">
        <article class="card card--blush reveal">
          <span class="roman--display">i.</span>
          <h3>Individual therapy</h3>
          <p>One-on-one work for adults navigating anxiety, trauma, identity, overwhelm, or the kind of stuck that's hard to name out loud. We work at the speed your system can actually handle.</p>
          <a href="services/individual-therapy.html" class="btn-ghost">More about individual</a>
        </article>

        <article class="card card--blush reveal">
          <span class="roman--display">ii.</span>
          <h3>EMDR therapy</h3>
          <p>When old stuff keeps showing up in today's reactions, EMDR helps the brain finally finish processing it. Often reaches what talk therapy can't — without making you retell the worst parts.</p>
          <a href="services/emdr-therapy.html" class="btn-ghost">More about EMDR</a>
        </article>

        <article class="card card--blush reveal">
          <span class="roman--display">iii.</span>
          <h3>Child &amp; teen therapy</h3>
          <p>A warm space for ages 7+. We meet kids where they are — through conversation, play, or whatever they need that day — and loop caregivers in along the way.</p>
          <a href="services/child-and-teen-therapy.html" class="btn-ghost">More about child &amp; teen</a>
        </article>
      </div>
    </div>
  </section>

  <!-- ========== PULL QUOTE ========== -->
  <section>
    <div class="container">
      <div class="pullquote reveal">
        <span class="pullquote__label">A note from us</span>
        <blockquote>
          You don't need to come in with the right words. You can show up <em>exactly</em> as you are — tired, foggy, mad, not sure where to start.
        </blockquote>
      </div>
    </div>
  </section>

  <!-- ========== HOW IT WORKS ========== -->
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">How this actually goes</span>
        <h2>Reach out · get to it · keep going.</h2>
        <p>The hardest part is usually the first message. After that, here's what happens.</p>
      </div>

      <div class="steps">
        <div class="step reveal">
          <span class="roman--display">i.</span>
          <h4>The first call</h4>
          <p>Twenty minutes, free, no script and no pressure.</p>
          <ul>
            <li>You tell us what's loud and what you've already tried</li>
            <li>We tell you honestly if we're the right fit — or who is</li>
            <li>If we are, we'll book your first session right there</li>
          </ul>
        </div>
        <div class="step reveal">
          <span class="roman--display">ii.</span>
          <h4>The actual work</h4>
          <p>Weekly or biweekly, in person or online — whatever fits your real life.</p>
          <ul>
            <li>First sessions build safety and trust, not pressure</li>
            <li>We name patterns together as they show up</li>
            <li>Goals are written in plain English, not therapy-speak</li>
          </ul>
        </div>
        <div class="step reveal">
          <span class="roman--display">iii.</span>
          <h4>The keep-going</h4>
          <p>Every so often we zoom out and check the map against the territory.</p>
          <ul>
            <li>Recalibrate when life rearranges (it always does)</li>
            <li>Notice what's shifted, name what's still tender</li>
            <li>Graduate when you're ready — kit in hand, not in head</li>
          </ul>
        </div>
      </div>

      <div style="text-align:center;margin-top:3rem" class="reveal">
        <a href="contact.html" class="btn btn-rose">Start with the free call</a>
      </div>
    </div>
  </section>

  <!-- ========== HELPS WITH ========== -->
  <section class="section bg-slate">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">What we work with</span>
        <h2>Common reasons folks find <em>their way</em> in.</h2>
        <p style="color:rgba(244,238,229,.78)">Not an exhaustive list — and not a requirement. Plenty of clients show up just knowing something feels off.</p>
      </div>

      <div class="card-grid card-grid--3">
        <div class="card reveal" style="background:rgba(244,238,229,.06);border-color:rgba(244,238,229,.14)">
          <h4 style="color:var(--cream);font-size:1.2rem">Anxiety &amp; overwhelm</h4>
          <p style="color:rgba(244,238,229,.75)">The hum that won't quit. Tight chest. Mind racing at 2 a.m. We'll get curious about what's underneath, not just how to mute it.</p>
        </div>
        <div class="card reveal" style="background:rgba(244,238,229,.06);border-color:rgba(244,238,229,.14)">
          <h4 style="color:var(--cream);font-size:1.2rem">Trauma &amp; triggers</h4>
          <p style="color:rgba(244,238,229,.75)">Big-T or little-t, recent or ancient. The kind of thing that hijacks your reactions and you can't talk yourself out of.</p>
        </div>
        <div class="card reveal" style="background:rgba(244,238,229,.06);border-color:rgba(244,238,229,.14)">
          <h4 style="color:var(--cream);font-size:1.2rem">People-pleasing &amp; burnout</h4>
          <p style="color:rgba(244,238,229,.75)">Saying yes when you mean no. Running on fumes for everyone else. We'll look at where it started — and what it's costing.</p>
        </div>
        <div class="card reveal" style="background:rgba(244,238,229,.06);border-color:rgba(244,238,229,.14)">
          <h4 style="color:var(--cream);font-size:1.2rem">Feeling numb or distant</h4>
          <p style="color:rgba(244,238,229,.75)">Going through the motions but far from yourself. Disconnection isn't a personality trait — usually it's protection.</p>
        </div>
        <div class="card reveal" style="background:rgba(244,238,229,.06);border-color:rgba(244,238,229,.14)">
          <h4 style="color:var(--cream);font-size:1.2rem">Teen stress &amp; regulation</h4>
          <p style="color:rgba(244,238,229,.75)">Helping young people understand what they're feeling without making them perform it for an adult.</p>
        </div>
        <div class="card reveal" style="background:rgba(244,238,229,.06);border-color:rgba(244,238,229,.14)">
          <h4 style="color:var(--cream);font-size:1.2rem">Parts work &amp; dissociation</h4>
          <p style="color:rgba(244,238,229,.75)">The parts of you that step in when things get heavy — we get to know them instead of fighting them.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========== FAQ PREVIEW ========== -->
  <section class="section">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow" style="justify-content:center">Before you reach out</span>
        <h2>Things people <em>actually</em> wonder.</h2>
      </div>

      <div class="faq-section">
        <details class="faq-item reveal">
          <summary>What if I don't know what I want to work on?</summary>
          <div class="faq-item__body">
            <p>Totally fine. A lot of folks come in knowing something's off without being able to name it. Part of our job is helping you find the language.</p>
          </div>
        </details>
        <details class="faq-item reveal">
          <summary>Do I need to be in a crisis to come to therapy?</summary>
          <div class="faq-item__body">
            <p>Not even close. The best time to do this work is before things break down — when there's enough bandwidth to actually look at what's happening.</p>
          </div>
        </details>
        <details class="faq-item reveal">
          <summary>Is everything virtual or in person?</summary>
          <div class="faq-item__body">
            <p>Both. Virtual is available to anyone in Colorado. In-person is downtown Colorado Springs. Many clients do a mix.</p>
          </div>
        </details>
        <details class="faq-item reveal">
          <summary>Can EMDR really help if other therapy hasn't?</summary>
          <div class="faq-item__body">
            <p>Often, yes. EMDR works with the nervous system directly — it tends to reach things talk therapy can circle around but not quite land on.</p>
          </div>
        </details>
        <details class="faq-item reveal">
          <summary>How much does this cost?</summary>
          <div class="faq-item__body">
            <p>Sessions range from $120–$250 depending on type and clinician. Sliding scale available. <a href="investment.html">See full rates</a>.</p>
          </div>
        </details>
      </div>

      <div style="text-align:center;margin-top:2.5rem" class="reveal">
        <a href="faq.html" class="btn btn-secondary">See all the questions</a>
      </div>
    </div>
  </section>

  <!-- ========== CTA ========== -->
  <section class="section">
    <div class="container">
      <div class="cta-banner reveal">
        <span class="eyebrow" style="color:var(--rose-soft);justify-content:center">When you're ready</span>
        <h2 style="margin-top:1rem">A twenty-minute call. <em>That's it.</em></h2>
        <p>No commitment. No pressure to book. Just a real conversation so you know what you'd be walking into.</p>
        <div class="cta-banner__ctas">
          <a href="contact.html" class="btn btn-rose">Book the call</a>
          <a href="about.html" class="btn btn-light">Meet the team</a>
        </div>
      </div>
    </div>
  </section>
"""

home_schema = {
  "@context":"https://schema.org",
  "@graph":[
    {
      "@type":"LocalBusiness","@id":"https://www.crescitacounseling.com/#business",
      "name":"Crescita Counseling",
      "image":"https://www.crescitacounseling.com/assets/images/crescita-logo.png",
      "url":"https://www.crescitacounseling.com/",
      "telephone":"+1-719-286-0011","email":"info@crescitacounseling.com",
      "priceRange":"$$",
      "address":{"@type":"PostalAddress","streetAddress":"627 N Weber St, Ste 6","addressLocality":"Colorado Springs","addressRegion":"CO","postalCode":"80903","addressCountry":"US"},
      "geo":{"@type":"GeoCoordinates","latitude":38.8409,"longitude":-104.8197},
      "areaServed":{"@type":"State","name":"Colorado"},
      "sameAs":["https://www.instagram.com/crescitameansgrowth/","https://www.facebook.com/people/Crescita-Counseling/61565442007671/","https://www.psychologytoday.com/profile/1221118"]
    },
    {"@type":"MedicalBusiness","name":"Crescita Counseling","medicalSpecialty":["Psychiatry","Counseling"],"url":"https://www.crescitacounseling.com/"},
    {"@type":"WebSite","url":"https://www.crescitacounseling.com/","name":"Crescita Counseling"},
    {"@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":"What if I don't know what I want to work on?","acceptedAnswer":{"@type":"Answer","text":"Totally fine. A lot of folks come in knowing something's off without being able to name it. Part of our job is helping you find the language."}},
      {"@type":"Question","name":"Do I need to be in a crisis to come to therapy?","acceptedAnswer":{"@type":"Answer","text":"Not even close. The best time to do this work is before things break down."}},
      {"@type":"Question","name":"Is everything virtual or in person?","acceptedAnswer":{"@type":"Answer","text":"Both. Virtual is available to anyone in Colorado. In-person is downtown Colorado Springs."}},
      {"@type":"Question","name":"Can EMDR really help if other therapy hasn't?","acceptedAnswer":{"@type":"Answer","text":"Often, yes. EMDR works with the nervous system directly."}}
    ]}
  ]
}

build_page(
  filename="index.html", depth=0, nav_active="home",
  title="Crescita Counseling | Trauma-Informed Therapy in Colorado Springs",
  description="Trauma-informed therapy in Colorado Springs and online across Colorado. EMDR, individual, child & teen counseling. No worksheets. Real conversation. Free 20-min consult.",
  canonical_path="/",
  schema=home_schema, content=home_content
)

print("Homepage v3 done.")
