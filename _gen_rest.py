#!/usr/bin/env python3
"""Regenerate services + remaining pages with v3 scaffold."""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from _build import build_page

# =========================================================================
# INDIVIDUAL THERAPY
# =========================================================================
individual_content = """
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><strong>Individual therapy</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">Individual therapy · in person + virtual</span>
        <h1 class="page-hero__title reveal">A room where you can <em>actually exhale.</em></h1>
        <p class="page-hero__lead reveal">One-on-one therapy for adults who've held it together for everyone else and want fifty minutes a week to stop performing.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container-text prose reveal">
      <p>Most folks who come in for individual therapy aren't in crisis — they're just <em>tired</em>. Tired of overthinking, of saying yes when they mean no, of feeling like there's a version of themselves they keep almost reaching.</p>
      <p>This is the space to slow that down. To understand the patterns underneath the patterns. To get to know the parts of you that have been working overtime, and give them somewhere to set things down for a minute.</p>
      <p>No worksheets. No script. We follow what's loud, we get curious about what's quiet, and we go at the pace your nervous system can actually hold.</p>
      <p><a href="../contact.html" class="text-link">If that sounds about right, here's how to start.</a></p>
    </div>
  </section>

  <section class="section bg-cream-deep">
    <div class="container">
      <div class="two-col">
        <div class="reveal">
          <span class="eyebrow eyebrow--rose">In the room</span>
          <h2 style="margin:1rem 0 1.5rem">What this <em>actually</em> looks like</h2>
          <ul class="prose" style="margin:0">
            <li>Real conversation about what's loud this week and what's underneath it</li>
            <li>Getting curious about reactions that don't make logical sense</li>
            <li>Noticing the parts of you that step in when things get heavy</li>
            <li>Building enough safety to slow down and feel what you've been outrunning</li>
            <li>Naming things in plain English — yours, not therapy-speak</li>
            <li>Tools that fit your life, not tools that turn you into a project</li>
          </ul>
        </div>
        <div class="two-col__media reveal">
          <img src="../assets/images/mountain-peaks.jpg" alt="Soft snow-capped Colorado mountain peaks in muted slate and cream light" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="two-col two-col--reverse">
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
          <img src="../assets/images/water-ripples.jpg" alt="Gentle water ripples in muted slate-blue and cream tones" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="pullquote reveal">
        <span class="pullquote__label">A reminder</span>
        <blockquote>
          You don't need a diagnosis or a clear list of goals to start. Showing up with <em>"something feels off"</em> is enough.
        </blockquote>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">Looking for something else?</span>
        <h2>Two other ways in.</h2>
      </div>
      <div class="card-grid card-grid--2" style="max-width:880px;margin:0 auto">
        <article class="card card--cream reveal">
          <span class="roman--display">ii.</span>
          <h3>EMDR therapy</h3>
          <p>When old experiences keep showing up in present-day reactions — EMDR helps the brain finally finish processing them.</p>
          <a href="emdr-therapy.html" class="btn-ghost">More about EMDR</a>
        </article>
        <article class="card card--cream reveal">
          <span class="roman--display">iii.</span>
          <h3>Child &amp; teen therapy</h3>
          <p>Age-appropriate support for young people navigating anxiety, big feelings, and changes that don't have easy words yet.</p>
          <a href="child-and-teen-therapy.html" class="btn-ghost">More about child &amp; teen</a>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner reveal">
        <h2 style="margin-top:0">Ready when you are.</h2>
        <p>Twenty-minute call, free. We talk about what's bringing you in, you ask anything you want, and you decide if it feels like a fit.</p>
        <div class="cta-banner__ctas"><a href="../contact.html" class="btn btn-rose">Book the call</a></div>
      </div>
    </div>
  </section>
"""

build_page(
  filename="services/individual-therapy.html", depth=1,
  title="Individual Therapy in Colorado Springs | Crescita Counseling",
  description="Individual therapy for adults navigating anxiety, trauma, overwhelm, identity, and the stuck stuff. In-person Colorado Springs or online statewide.",
  canonical_path="/services/individual-therapy.html",
  schema={"@context":"https://schema.org","@type":"MedicalTherapy","name":"Individual Therapy","url":"https://www.crescitacounseling.com/services/individual-therapy.html","provider":{"@type":"MedicalBusiness","name":"Crescita Counseling"},"areaServed":{"@type":"State","name":"Colorado"},"description":"Individual therapy for adults navigating anxiety, trauma, overwhelm, and life transitions."},
  content=individual_content
)

# =========================================================================
# EMDR
# =========================================================================
emdr_content = """
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><strong>EMDR therapy</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">EMDR therapy · in person + virtual</span>
        <h1 class="page-hero__title reveal">When the past keeps showing up in the <em>present.</em></h1>
        <p class="page-hero__lead reveal">EMDR helps your brain finish processing the experiences that still steer today's reactions — gently, at your pace, without making you retell the worst parts.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container-text prose reveal">
      <p>You probably already know which moments we're talking about. The ones that come up in your body before your brain catches up. The reactions that feel three sizes too big for what's actually happening. The way certain people, places, or tones still hijack you, even when you <em>know</em> you're safe.</p>
      <p>EMDR is one of the few approaches built specifically for that. Not for processing your week. For helping the nervous system finally complete something it didn't get to complete the first time.</p>
      <p>It's structured. It's well-researched. And it works with how the brain actually stores hard experiences — not just how you talk about them.</p>
    </div>
  </section>

  <section class="section bg-cream-deep">
    <div class="container">
      <div class="two-col">
        <div class="reveal">
          <span class="eyebrow eyebrow--rose">What it is</span>
          <h2 style="margin:1rem 0 1.5rem">Not talk therapy. <em>Nervous system therapy.</em></h2>
          <p class="lead" style="margin-bottom:1.25rem">EMDR stands for Eye Movement Desensitization and Reprocessing. The technical name does it no favors.</p>
          <p style="color:var(--slate)">Here's the short version: using guided eye movements (or other forms of bilateral stimulation), EMDR activates the brain's natural processing system — the one that runs while you sleep. That lets old experiences get filed away properly instead of looping unresolved in the background.</p>
          <p style="color:var(--slate);margin-top:1rem">You don't have to retell every detail. You don't have to convince yourself you're over it. The work happens at a level underneath the story.</p>
        </div>
        <div class="two-col__media reveal">
          <img src="../assets/images/clouds-rose.jpg" alt="Soft slate-blue clouds with dusty rose light" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">Why folks pick it</span>
        <h2>EMDR works <em>differently</em> than what most people have tried.</h2>
      </div>
      <div class="card-grid card-grid--3">
        <div class="card card--blush reveal">
          <span class="roman--display">i.</span>
          <h4 style="font-size:1.2rem">It respects your pace</h4>
          <p>You're never pushed past what your system can hold. If we hit a wall, we slow down. That's part of the protocol, not a setback.</p>
        </div>
        <div class="card card--blush reveal">
          <span class="roman--display">ii.</span>
          <h4 style="font-size:1.2rem">It works with the body</h4>
          <p>Talk therapy circles the issue. EMDR goes underneath it — to where trauma actually lives, which is rarely just in language.</p>
        </div>
        <div class="card card--blush reveal">
          <span class="roman--display">iii.</span>
          <h4 style="font-size:1.2rem">The shifts tend to hold</h4>
          <p>Folks often describe relief that feels structural, not temporary. The memory doesn't disappear — but it stops driving the bus.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-slate">
    <div class="container-text prose reveal" style="color:rgba(244,238,229,.85)">
      <span class="eyebrow">The eight phases</span>
      <h2 style="color:var(--cream);margin:1rem 0 1.5rem">How EMDR <em>actually</em> goes.</h2>
      <p style="color:rgba(244,238,229,.78)">Every client is different, but EMDR has a structure. Knowing what's coming usually helps.</p>
      <ol style="color:rgba(244,238,229,.85)">
        <li><strong style="color:var(--cream)">History &amp; planning</strong> — getting clear on what you've been carrying and what you'd like help with.</li>
        <li><strong style="color:var(--cream)">Preparation</strong> — building grounding skills and trust before we go anywhere heavy.</li>
        <li><strong style="color:var(--cream)">Assessment</strong> — identifying a memory or pattern to work on.</li>
        <li><strong style="color:var(--cream)">Desensitization</strong> — using bilateral stimulation to take the emotional charge down.</li>
        <li><strong style="color:var(--cream)">Installation</strong> — reinforcing the more accurate belief that wants to take its place.</li>
        <li><strong style="color:var(--cream)">Body scan</strong> — checking where your body is still holding it.</li>
        <li><strong style="color:var(--cream)">Closure</strong> — making sure you leave grounded, not raw.</li>
        <li><strong style="color:var(--cream)">Reevaluation</strong> — checking progress and naming what's next.</li>
      </ol>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="two-col two-col--reverse">
        <div class="reveal">
          <span class="eyebrow">Who EMDR helps</span>
          <h2 style="margin:1rem 0 1.5rem">EMDR is effective for:</h2>
          <ul class="pill-list">
            <li>Trauma &amp; PTSD</li><li>Anxiety</li><li>Chronic stress</li>
            <li>Panic</li><li>Grief &amp; loss</li><li>Relationship wounds</li>
            <li>Childhood trauma</li><li>Triggers</li><li>Dissociation</li>
            <li>Low self-worth</li><li>Performance anxiety</li>
          </ul>
          <p style="margin-top:1.5rem;color:var(--slate)">Many folks who've felt stuck through other therapies find real movement here. Not because it's magic — because it's the right tool for what's actually getting in the way.</p>
        </div>
        <div class="two-col__media reveal">
          <img src="../assets/images/river-stones.jpg" alt="Smooth river stones in dusty rose, slate blue, and warm gray tones" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner reveal">
        <h2 style="margin-top:0">Curious if EMDR is a fit?</h2>
        <p>Book a free call and we'll talk through what's been happening. If EMDR's the right next step, we'll walk you through what that would look like.</p>
        <div class="cta-banner__ctas"><a href="../contact.html" class="btn btn-rose">Book a call</a></div>
      </div>
    </div>
  </section>
"""

build_page(
  filename="services/emdr-therapy.html", depth=1,
  title="EMDR Therapy in Colorado Springs | Crescita Counseling",
  description="EMDR therapy in Colorado Springs and online statewide. Evidence-based trauma reprocessing for anxiety, PTSD, and triggers that feel stuck.",
  canonical_path="/services/emdr-therapy.html",
  schema={"@context":"https://schema.org","@type":"MedicalTherapy","name":"EMDR Therapy","alternateName":"Eye Movement Desensitization and Reprocessing","url":"https://www.crescitacounseling.com/services/emdr-therapy.html","provider":{"@type":"MedicalBusiness","name":"Crescita Counseling"},"areaServed":{"@type":"State","name":"Colorado"},"description":"EMDR therapy in Colorado Springs and online across Colorado."},
  content=emdr_content
)

# =========================================================================
# CHILD & TEEN
# =========================================================================
child_content = """
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><strong>Child &amp; teen therapy</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">Child &amp; teen therapy · ages 7+</span>
        <h1 class="page-hero__title reveal">Where kids and teens get to <em>actually be kids.</em></h1>
        <p class="page-hero__lead reveal">A warm, age-appropriate space for the things they can't quite say at the dinner table yet — through conversation, play, or whatever helps the words come.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container-text prose reveal">
      <p>Kids and teens have inner lives just as full as ours. They just don't always have the vocabulary yet — and they almost never have a space where the adults aren't grading them.</p>
      <p>That's what this is: somewhere your child can talk freely, work things out at their own pace, and not have to perform "fine" for anyone. We work with what they show up with — conversation, play, art, silence, whatever helps that day.</p>
      <p>We also loop you in. <strong>You're not on the outside of this work</strong>. We share what's appropriate, give you context for what's happening, and help you respond at home in ways that line up with what's happening in the room.</p>
      <p><a href="../contact.html" class="text-link">If your kid needs a place to land — here's how to start.</a></p>
    </div>
  </section>

  <section class="section bg-cream-deep">
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
          <img src="../assets/images/garden-of-the-gods.jpg" alt="Garden of the Gods red rock formations against a soft Colorado sky" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">For caregivers</span>
        <h2>You don't have to figure this out <em>alone.</em></h2>
        <p>Parenting a kid in distress is exhausting in a very particular way. We don't just work with your child — we work with the system around them.</p>
      </div>

      <div class="card-grid card-grid--3">
        <div class="card card--blush reveal">
          <span class="roman--display">i.</span>
          <h4 style="font-size:1.2rem">Ages 7+</h4>
          <p>Our clinicians work with school-age kids, tweens, teens, and young adults. We'll match you with whoever's best suited to your kid's age and what's going on.</p>
        </div>
        <div class="card card--blush reveal">
          <span class="roman--display">ii.</span>
          <h4 style="font-size:1.2rem">Anxiety &amp; regulation</h4>
          <p>Big feelings, racing minds, perfectionism, school stress. We help young people understand what their bodies are doing and build tools that actually work.</p>
        </div>
        <div class="card card--blush reveal">
          <span class="roman--display">iii.</span>
          <h4 style="font-size:1.2rem">Real transitions</h4>
          <p>Moves, divorce, new schools, deployments, loss. The kind of things kids feel deeply and don't always have language for yet.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="pullquote reveal">
        <span class="pullquote__label">For the parent reading this</span>
        <blockquote>
          If you're not sure whether to reach out — <em>reach out.</em> The free call is for you too. We'll tell you honestly whether therapy is the right next step.
        </blockquote>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner reveal">
        <h2 style="margin-top:0">For your kid. For your family.</h2>
        <p>Book a free twenty-minute call. Ask anything. We'll help you figure out if this is the right move — and if it is, who's the right fit.</p>
        <div class="cta-banner__ctas"><a href="../contact.html" class="btn btn-rose">Reach out</a></div>
      </div>
    </div>
  </section>
"""

build_page(
  filename="services/child-and-teen-therapy.html", depth=1,
  title="Child & Teen Therapy in Colorado Springs | Crescita Counseling",
  description="Therapy for children and teens (ages 7+) in Colorado Springs and online statewide.",
  canonical_path="/services/child-and-teen-therapy.html",
  schema={"@context":"https://schema.org","@type":"MedicalTherapy","name":"Child and Teen Therapy","url":"https://www.crescitacounseling.com/services/child-and-teen-therapy.html","provider":{"@type":"MedicalBusiness","name":"Crescita Counseling"},"areaServed":{"@type":"State","name":"Colorado"}},
  content=child_content
)

# =========================================================================
# INVESTMENT
# =========================================================================
investment_content = """
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="index.html">Home</a><span>/</span><strong>Rates &amp; insurance</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">Investment</span>
        <h1 class="page-hero__title reveal">Transparent rates. <em>Real options.</em></h1>
        <p class="page-hero__lead reveal">Here's what therapy costs at Crescita, how insurance works, and what's available if cost is part of the equation.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Session rates</span>
        <h2>What it costs.</h2>
        <p>Straightforward fees, no surprises. Sliding scale available — just ask.</p>
      </div>

      <div class="pricing-grid">
        <div class="price-card price-card--feature reveal">
          <p class="price-card__title">Initial intake</p>
          <p class="price-card__price">$200<small>· up to 75 min</small></p>
          <p class="price-card__desc">A longer first session — we get to know you, you ask anything, and we map out what the work might look like.</p>
        </div>
        <div class="price-card price-card--feature reveal">
          <p class="price-card__title">Individual session</p>
          <p class="price-card__price">$150<small>· 50 min</small></p>
          <p class="price-card__desc">Standard weekly or biweekly therapy. Where most of the actual work happens.</p>
        </div>
        <div class="price-card price-card--feature reveal">
          <p class="price-card__title">EMDR session</p>
          <p class="price-card__price">$250<small>· 90 min</small></p>
          <p class="price-card__desc">Extended sessions for EMDR work, dissociation, or anything that needs more runway. The longer format helps your system land safely before we close.</p>
        </div>
        <div class="price-card price-card--feature reveal">
          <p class="price-card__title">Pre-licensed counselor</p>
          <p class="price-card__price">$120<small>· 50 min</small></p>
          <p class="price-card__desc">Reduced-fee sessions with a pre-licensed clinician on our team. Same relational, trauma-informed approach, supervised throughout.</p>
        </div>
      </div>

      <p class="form-note reveal" style="margin-top:1.5rem;max-width:760px">
        <strong>Sliding fee available.</strong> If cost is in the way, ask. We'd rather have the conversation than have you not reach out.
      </p>
    </div>
  </section>

  <section class="section bg-cream-deep">
    <div class="container">
      <div class="card-grid card-grid--2" style="max-width:920px;margin:0 auto">
        <div class="reveal">
          <span class="eyebrow eyebrow--rose">Payment</span>
          <h3 style="margin:1rem 0">How to pay</h3>
          <p style="color:var(--slate)">Cash, check, HSA/FSA cards, and all major credit cards. Card on file is required to schedule.</p>
        </div>
        <div class="reveal">
          <span class="eyebrow eyebrow--rose">Cancellation</span>
          <h3 style="margin:1rem 0">24-hour notice</h3>
          <p style="color:var(--slate)">Life happens — just give us a heads up. Cancellations inside 24 hours are charged the full session fee.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="two-col">
        <div class="reveal">
          <span class="eyebrow">Insurance</span>
          <h2 style="margin:1rem 0 1.5rem">In-network &amp; Medicaid</h2>
          <p style="color:var(--slate);font-size:1.05rem">We take insurance on a limited basis (including Medicaid), depending on clinician availability and the type of services you need. Coverage varies plan to plan.</p>
          <p style="color:var(--slate);font-size:1.05rem;margin-top:1rem">The simplest move: <a href="contact.html" class="text-link">send us a message</a> with your plan info. We'll check what's covered and walk you through next steps.</p>
        </div>
        <div class="reveal">
          <span class="eyebrow">Out of network</span>
          <h2 style="margin:1rem 0 1.5rem">Reimbursement made easier</h2>
          <p style="color:var(--slate);font-size:1.05rem">We've partnered with <strong>Mentaya</strong> to help clients use out-of-network benefits without the paperwork headache. Check eligibility in two clicks.</p>
          <a href="https://app.mentaya.com/public/practices/oMmOomBYnjxTXzgbI5gt/eligibility/widget" target="_blank" rel="noopener" class="btn btn-secondary" style="margin-top:1.25rem">Check Mentaya eligibility →</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-cream-deep">
    <div class="container-text reveal" style="text-align:center">
      <span class="eyebrow eyebrow--rose" style="justify-content:center">Required disclosure</span>
      <h3 style="margin:1rem 0">Good Faith Estimate</h3>
      <p style="color:var(--slate)">Under the No Surprises Act, you have the right to receive a Good Faith Estimate before scheduling. <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener" class="text-link">CMS has the full breakdown</a>.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner reveal">
        <h2 style="margin-top:0">Questions about cost?</h2>
        <p>Free call. We'll talk through what fits — including insurance, sliding scale, and pre-licensed options.</p>
        <div class="cta-banner__ctas"><a href="contact.html" class="btn btn-rose">Book a call</a></div>
      </div>
    </div>
  </section>
"""

build_page(
  filename="investment.html", depth=0, nav_active="investment",
  title="Therapy Rates & Insurance | Crescita Counseling Colorado Springs",
  description="Transparent therapy pricing in Colorado Springs. Rates for intake, individual, EMDR, reduced-fee sessions. Insurance, sliding scale, and out-of-network options.",
  canonical_path="/investment.html",
  schema={"@context":"https://schema.org","@type":"WebPage","name":"Therapy Rates & Insurance","url":"https://www.crescitacounseling.com/investment.html","offers":[{"@type":"Offer","name":"Initial Intake","price":"200","priceCurrency":"USD"},{"@type":"Offer","name":"Individual Session","price":"150","priceCurrency":"USD"},{"@type":"Offer","name":"EMDR Session","price":"250","priceCurrency":"USD"},{"@type":"Offer","name":"Pre-Licensed Counselor","price":"120","priceCurrency":"USD"}]},
  content=investment_content
)

# =========================================================================
# FAQ
# =========================================================================
faq_items = [
  ("Getting started", [
    ("How do I book my first appointment?", "Fill out the form on the <a href='contact.html'>contact page</a> — tell us a little about what you're hoping to work on. We'll respond within a business day and help you pick the right clinician and session type."),
    ("Do you offer a consultation before I commit?", "Yes — <strong>free 20-minute phone consultations</strong> with available clinicians. Ask anything. No pressure to book afterward. <a href='contact.html'>Request one here</a>."),
    ("How do I pick a therapist?", "If you're not sure, we'll help. Send us a note about what you're hoping to work on and we'll match you with the clinician whose training and style line up best."),
    ("I'm nervous about starting. Is that normal?", "Completely. You don't need to have the right words or a clean list of goals. We'll meet you where you are — that's literally the work."),
    ("How soon can I get in?", "Availability varies by clinician. When you reach out, we'll let you know who has openings and how soon."),
  ]),
  ("Logistics", [
    ("How fast do you respond?", "Within <strong>one business day</strong>, usually faster. If you reach out over a weekend, you'll hear from us Monday."),
    ("Do you do virtual sessions?", "Yes — secure virtual therapy is available to anyone in Colorado. Some EMDR, parts work, and child/teen sessions are virtual too, depending on the clinician."),
    ("What ages do you work with?", "Ages <strong>7 and up</strong>, depending on clinician. Mention your child or teen's age on the form and we'll route you to the right person. More on the <a href='services/child-and-teen-therapy.html'>child &amp; teen page</a>."),
    ("Why is the EMDR session longer than a regular one?", "EMDR needs more runway. A 50-minute slot is enough for processing the week — EMDR sessions are 90 minutes so we can prepare, work, and close out safely without rushing your system."),
    ("What's the cancellation policy?", "<strong>24 hours' notice</strong>. Cancellations after that get charged the full session fee."),
  ]),
  ("About therapy itself", [
    ("What even is therapy?", "A real conversation with a trained clinician, on purpose, on a regular basis. It's a space to look at what's actually happening — emotions, patterns, history — without performing for the person in the room."),
    ("Do I need a diagnosis or a crisis to come?", "No. Plenty of folks come in because something's just <em>off</em>. That's a perfectly good reason."),
    ("What happens in the first session?", "We get to know each other. You tell us what's bringing you in, your background, what's already been tried. There's no homework and no expectation to have it all figured out."),
    ("How long does therapy take?", "Depends on what you're working on. Some folks feel meaningful shifts in a few months. Others stay longer for deeper work. We talk about expectations as we go."),
    ("Can therapy help when nothing's technically wrong?", "Yes. Often that's exactly when it's most useful. There's more bandwidth to actually look at the thing."),
    ("Will EMDR help with my anxiety?", "Often, yes — particularly if there's stuff underneath the anxiety that talk therapy hasn't quite reached. <a href='services/emdr-therapy.html'>More on EMDR here</a>."),
    ("What's the difference between counseling and therapy?", "Honestly? We use the words interchangeably. Both mean the same thing here: showing up regularly with a trained person and doing the work."),
  ]),
]

faq_html_groups = []
faq_schema_items = []
for group_title, items in faq_items:
  faq_lis = []
  for q, a in items:
    faq_lis.append(f"""        <details class="faq-item reveal">
          <summary>{q}</summary>
          <div class="faq-item__body"><p>{a}</p></div>
        </details>""")
    a_text = re.sub(r'<[^>]+>', '', a).replace('&nbsp;',' ').replace('&amp;','&').strip()
    q_text = re.sub(r'<[^>]+>', '', q).replace('&amp;','&').strip()
    faq_schema_items.append({"@type":"Question","name":q_text,"acceptedAnswer":{"@type":"Answer","text":a_text}})
  faq_html_groups.append(f"""      <div class="faq-group reveal">
        <h2 class="faq-group__title">{group_title}</h2>
{chr(10).join(faq_lis)}
      </div>""")

faq_content = f"""
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="index.html">Home</a><span>/</span><strong>FAQ</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">Common questions</span>
        <h1 class="page-hero__title reveal">Stuff people <em>actually</em> wonder.</h1>
        <p class="page-hero__lead reveal">Real answers to the questions that come up before reaching out. If we missed yours, <a href="contact.html" class="text-link">just ask</a>.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="faq-section">
{chr(10).join(faq_html_groups)}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner reveal">
        <h2 style="margin-top:0">Still wondering?</h2>
        <p>The free call is usually the fastest way to get a feel for how we work. Twenty minutes, no commitment.</p>
        <div class="cta-banner__ctas"><a href="contact.html" class="btn btn-rose">Reach out</a></div>
      </div>
    </div>
  </section>
"""

build_page(
  filename="faq.html", depth=0, nav_active="faq",
  title="Therapy FAQ | Crescita Counseling Colorado Springs",
  description="Real answers about therapy, insurance, EMDR, virtual sessions, and how to get started at Crescita Counseling.",
  canonical_path="/faq.html",
  schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":faq_schema_items},
  content=faq_content
)

# =========================================================================
# CONTACT
# =========================================================================
contact_content = """
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="index.html">Home</a><span>/</span><strong>Contact</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">Reach out</span>
        <h1 class="page-hero__title reveal">A twenty-minute call. <em>No pressure.</em></h1>
        <p class="page-hero__lead reveal">Fill out the form, email, or call. We read every message ourselves and write back within one business day — usually faster.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="two-col">
        <div class="reveal">
          <span class="eyebrow">Other ways to say hi</span>
          <h2 style="margin:1rem 0 1.5rem">Direct lines</h2>
          <div style="display:flex;flex-direction:column;gap:1.1rem;font-size:1.05rem">
            <a href="mailto:info@crescitacounseling.com" style="display:flex;align-items:flex-start;gap:.85rem;color:var(--ink)">
              <span style="width:42px;height:42px;border-radius:50%;background:var(--blush-soft);color:var(--rose-deep);display:flex;align-items:center;justify-content:center;flex-shrink:0">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              </span>
              <span><strong style="font-weight:600">Email</strong><br><span style="color:var(--slate)">info@crescitacounseling.com</span></span>
            </a>
            <a href="tel:+17192860011" style="display:flex;align-items:flex-start;gap:.85rem;color:var(--ink)">
              <span style="width:42px;height:42px;border-radius:50%;background:var(--blush-soft);color:var(--rose-deep);display:flex;align-items:center;justify-content:center;flex-shrink:0">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              </span>
              <span><strong style="font-weight:600">Phone</strong><br><span style="color:var(--slate)">(719) 286-0011</span></span>
            </a>
            <a href="https://maps.google.com/?q=627+N+Weber+St+Suite+6+Colorado+Springs+CO+80903" target="_blank" rel="noopener" style="display:flex;align-items:flex-start;gap:.85rem;color:var(--ink)">
              <span style="width:42px;height:42px;border-radius:50%;background:var(--blush-soft);color:var(--rose-deep);display:flex;align-items:center;justify-content:center;flex-shrink:0">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              </span>
              <span><strong style="font-weight:600">Office</strong><br><span style="color:var(--slate)">627 N Weber St, Ste 6<br>Colorado Springs, CO 80903</span></span>
            </a>
          </div>
          <div style="margin-top:2rem;padding:1.25rem;background:var(--blush-soft);border-radius:var(--r-md);border-left:3px solid var(--rose)">
            <p style="font-size:.93rem;color:var(--slate);margin:0;line-height:1.55"><strong style="color:var(--slate-deep)">Quick privacy note:</strong> please don't share detailed medical info through this form. Save that for our secure sessions.</p>
          </div>
        </div>

        <div class="form-card reveal">
          <form data-contact-form action="https://formspree.io/f/YOUR_FORMSPREE_ID" method="POST" novalidate>
            <div class="form-row form-row--2">
              <div class="form-group">
                <label for="firstName">First name <span class="req">*</span></label>
                <input type="text" id="firstName" name="firstName" required autocomplete="given-name">
              </div>
              <div class="form-group">
                <label for="lastName">Last name <span class="req">*</span></label>
                <input type="text" id="lastName" name="lastName" required autocomplete="family-name">
              </div>
            </div>
            <div class="form-row form-row--2">
              <div class="form-group">
                <label for="email">Email <span class="req">*</span></label>
                <input type="email" id="email" name="email" required autocomplete="email">
              </div>
              <div class="form-group">
                <label for="phone">Phone</label>
                <input type="tel" id="phone" name="phone" autocomplete="tel">
              </div>
            </div>
            <div class="form-row form-row--2">
              <div class="form-group">
                <label for="who">Therapy is for</label>
                <select id="who" name="who">
                  <option value="myself">Myself</option>
                  <option value="my-child-teen">My child or teen</option>
                  <option value="myself-and-child">Myself and my child/teen</option>
                  <option value="someone-else">Someone else</option>
                </select>
              </div>
              <div class="form-group">
                <label for="format">Preferred format</label>
                <select id="format" name="format">
                  <option value="no-preference">No preference</option>
                  <option value="in-person">In-person (Colorado Springs)</option>
                  <option value="virtual">Virtual</option>
                </select>
              </div>
            </div>
            <div class="form-group" style="margin-bottom:1rem">
              <label for="interest">What you're curious about</label>
              <select id="interest" name="interest">
                <option value="not-sure">Not sure yet</option>
                <option value="individual">Individual therapy</option>
                <option value="emdr">EMDR therapy</option>
                <option value="child-teen">Child &amp; teen therapy</option>
              </select>
            </div>
            <div class="form-group" style="margin-bottom:1rem">
              <label for="message">What's loud right now? <span class="req">*</span></label>
              <textarea id="message" name="message" required placeholder="A few sentences is plenty. We'll follow up to talk more."></textarea>
            </div>
            <label class="form-checkbox" style="margin-bottom:1.25rem">
              <input type="checkbox" name="consent" required>
              <span>I understand my submission will be reviewed by Crescita Counseling and that I shouldn't share detailed medical information through this form.</span>
            </label>
            <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px">
            <button type="submit" class="btn btn-rose" style="width:100%">Send message</button>
            <div class="form-status" data-form-status role="status" aria-live="polite"></div>
          </form>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-cream-deep">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">Where we are</span>
        <h2>Downtown Colorado Springs</h2>
        <p>Easy access from across the Pikes Peak region. Virtual everywhere else in Colorado.</p>
      </div>
      <div style="max-width:1080px;margin:0 auto;border-radius:var(--r-lg);overflow:hidden;border:1px solid var(--line)" class="reveal">
        <iframe src="https://www.google.com/maps?q=627+N+Weber+St+Suite+6+Colorado+Springs+CO+80903&amp;output=embed" width="100%" height="420" style="border:0;display:block" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Crescita Counseling location"></iframe>
      </div>
    </div>
  </section>
"""

build_page(
  filename="contact.html", depth=0, nav_active="contact",
  title="Contact Crescita Counseling | Therapy in Colorado Springs",
  description="Get in touch with Crescita Counseling to schedule a free 20-minute consult or ask anything about therapy, EMDR, or child & teen work.",
  canonical_path="/contact.html",
  schema={"@context":"https://schema.org","@type":"ContactPage","url":"https://www.crescitacounseling.com/contact.html","mainEntity":{"@type":"LocalBusiness","name":"Crescita Counseling","telephone":"+1-719-286-0011","email":"info@crescitacounseling.com","address":{"@type":"PostalAddress","streetAddress":"627 N Weber St, Ste 6","addressLocality":"Colorado Springs","addressRegion":"CO","postalCode":"80903","addressCountry":"US"}}},
  content=contact_content
)

# =========================================================================
# 404
# =========================================================================
build_page(
  filename="404.html", depth=0,
  title="Page Not Found | Crescita Counseling",
  description="The page you're looking for isn't here.",
  canonical_path="/404.html",
  content="""
  <section class="error-page">
    <div>
      <div class="num">404.</div>
      <p>This page wandered off. Let's get you somewhere useful.</p>
      <div style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap">
        <a href="index.html" class="btn btn-primary">Back to home</a>
        <a href="contact.html" class="btn btn-secondary">Contact us</a>
      </div>
    </div>
  </section>
"""
)

print("All remaining pages done.")
