#!/usr/bin/env python3
"""Regenerate all remaining pages with v3 scaffold (new header/footer, no deco circles)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from _build import build_page

# =========================================================================
# ABOUT — gets blob-leaf accent + wildflower backdrop
# =========================================================================
about_content = """
  <section class="page-hero">
    <span class="blob-accent blob-accent--about" aria-hidden="true">
      <img src="assets/images/blob-leaf.jpg" alt="" loading="eager">
    </span>
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="index.html">Home</a><span>/</span><strong>About</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">About the practice</span>
        <h1 class="page-hero__title reveal">Therapy that feels like a <em>real conversation</em>.</h1>
        <p class="page-hero__lead reveal">No clipboards. No worksheets that look like the SAT. Just trained, trauma-informed people you can actually talk to — about the stuff that doesn't have easy words yet.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="two-col">
        <div class="two-col__media reveal">
          <img src="assets/images/soft-botanicals.jpg" alt="Dusty rose and mauve flowers with gentle slate-blue leaves arranged softly" loading="lazy">
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

  <section>
    <div class="container">
      <div class="pullquote reveal">
        <span class="pullquote__label">What we believe</span>
        <blockquote>
          Your nervous system isn't broken. It's been doing <em>exactly</em> what it was set up to do. The work isn't fixing it — it's helping it learn the danger is over.
        </blockquote>
      </div>
    </div>
  </section>

  <section class="section has-wildflowers">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">How we work</span>
        <h2>A few things we mean when we say <em>trauma-informed</em>.</h2>
      </div>

      <div class="card-grid card-grid--3">
        <div class="card card--cream reveal">
          <span class="roman--display">i.</span>
          <h4 style="font-size:1.25rem">Pace is yours</h4>
          <p>We never push faster than your system can integrate. If we hit a wall, we slow down or back up. That's the work, not a setback.</p>
        </div>
        <div class="card card--cream reveal">
          <span class="roman--display">ii.</span>
          <h4 style="font-size:1.25rem">Bodies count</h4>
          <p>Talk therapy alone doesn't always reach the places trauma lives. We work somatically and with EMDR when that's what's actually needed.</p>
        </div>
        <div class="card card--cream reveal">
          <span class="roman--display">iii.</span>
          <h4 style="font-size:1.25rem">Real over polished</h4>
          <p>You don't have to perform. You can swear, cry, blank out, change your mind mid-sentence. We've seen all of it. None of it scares us off.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--rose" style="justify-content:center">The team</span>
        <h2>Two clinicians. <em>Same posture.</em></h2>
        <p>Both trained in trauma-informed care. Both bring warmth, humor, and steady presence into the room. If you're not sure who to start with, we can help match you.</p>
      </div>

      <div class="team-grid">
        <article class="therapist-card reveal">
          <a href="team/katie-pasqualetto.html" class="therapist-card__img" aria-label="Read more about Katie">
            <img src="https://images.squarespace-cdn.com/content/v1/664bb8dbe6641260d9a4f5af/c2e1a1ca-b4d2-4994-8ea7-b73e70188509/%231.jpg?format=600w" alt="Katie Pasqualetto, licensed therapist and practice owner" loading="lazy">
          </a>
          <div class="therapist-card__body">
            <p class="therapist-card__role">Practice owner · LPC, EMDR-trained</p>
            <h3><a href="team/katie-pasqualetto.html" style="color:inherit">Katie Pasqualetto</a></h3>
            <p class="therapist-card__specialties"><strong>Works with:</strong> complex trauma, EMDR, dissociation, parts work, perfectionism, identity, the high-functioning version of "I'm fine."</p>
            <a href="team/katie-pasqualetto.html" class="btn-ghost">Meet Katie</a>
          </div>
        </article>

        <article class="therapist-card reveal">
          <a href="team/alissa-brown.html" class="therapist-card__img" aria-label="Read more about Alissa">
            <img src="assets/images/alissa-brown.jpg" alt="Alissa Brown, pre-licensed therapist" loading="lazy">
          </a>
          <div class="therapist-card__body">
            <p class="therapist-card__role">Pre-licensed therapist · LPCC</p>
            <h3><a href="team/alissa-brown.html" style="color:inherit">Alissa Brown</a></h3>
            <p class="therapist-card__specialties"><strong>Works with:</strong> kids and teens, anxiety, military families, parenting, school stress, the postpartum stretch nobody warned you about.</p>
            <a href="team/alissa-brown.html" class="btn-ghost">Meet Alissa</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner reveal">
        <h2 style="margin-top:0">Not sure who's the right fit?</h2>
        <p>Tell us a little about what you're hoping to work on. We'll pair you with the clinician whose training and style line up — or be honest if it's someone outside our practice.</p>
        <div class="cta-banner__ctas">
          <a href="contact.html" class="btn btn-rose">Book a free call</a>
        </div>
      </div>
    </div>
  </section>
"""

build_page(
  filename="about.html", depth=0, nav_active="about",
  title="About Crescita Counseling | Colorado Springs Therapy Practice",
  description="A trauma-informed therapy practice in Colorado Springs. Real conversation, not clipboards. Meet the team behind Crescita.",
  canonical_path="/about.html",
  schema={"@context":"https://schema.org","@type":"AboutPage","url":"https://www.crescitacounseling.com/about.html","name":"About Crescita Counseling","mainEntity":{"@type":"Organization","name":"Crescita Counseling","url":"https://www.crescitacounseling.com/","employee":[{"@type":"Person","name":"Katie Pasqualetto","jobTitle":"Licensed Therapist & Practice Owner","url":"https://www.crescitacounseling.com/team/katie-pasqualetto.html"},{"@type":"Person","name":"Alissa Brown","jobTitle":"Pre-Licensed Therapist","url":"https://www.crescitacounseling.com/team/alissa-brown.html"}]}},
  content=about_content
)

# =========================================================================
# KATIE — unchanged content, regenerate with new scaffold
# =========================================================================
katie_content = """
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><a href="../about.html">About</a><span>/</span><strong>Katie</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">Practice owner · LPC, EMDR-trained</span>
        <h1 class="page-hero__title reveal">Hi — I'm <em>Katie.</em></h1>
        <p class="page-hero__lead reveal">In-person in downtown Colorado Springs. Online anywhere in Colorado.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="two-col">
        <div class="two-col__media reveal">
          <img src="https://images.squarespace-cdn.com/content/v1/664bb8dbe6641260d9a4f5af/fca2ce37-bed5-4f1e-b224-14843787272a/PHOTO-2024-07-09-19-34-07+2.jpg?format=900w" alt="Katie smiling on a couch with a pink mug and a potted plant beside her" loading="lazy">
        </div>
        <div class="prose reveal">
          <p>Trauma therapist, EMDR enthusiast, owner of Crescita, dog mom to a Wheaten terrier named Keith (he knows he's the main character), fall person, British TV apologist.</p>
          <p>Before this I was a school counselor. I loved supporting kids and teens, but I kept craving the kind of conversation where someone could finally slow down — and really say the hard thing. Becoming a therapist gave me room to sit in those moments instead of running past them.</p>
          <p>Clients describe me as <em>funny, grounding, and weirdly calming</em>. I can sit with heavy things without making them heavier, and I'll use a bit of dark humor if it helps you feel less alone in the room. No judgment, no rushing. Just honesty, curiosity, and enough room for whatever shows up — even if what shows up is "I don't know what I'm feeling."</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-cream-deep">
    <div class="container-text prose reveal">
      <h2>How I work</h2>
      <p>My main tools are <strong>EMDR, parts work, somatic awareness, and trauma-informed relational therapy</strong>. I work mostly with adults navigating childhood trauma, dissociation, perfectionism, identity stuff, and long-standing patterns that don't seem to budge no matter how many books they've read.</p>
      <p>I'm especially good with folks who overthink, shut down, or use humor as a shield (trust me, you're in good company). The work usually starts with understanding why your nervous system is doing what it's doing — because once that makes sense, the rest of it gets a lot more workable.</p>
      <p>Outside of sessions: hiking, traveling (22 countries and counting), reading too much, picking up hobbies that rotate weekly, and being unreasonably excited about fresh snow.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="two-col two-col--reverse">
        <div class="reveal">
          <span class="eyebrow eyebrow--rose">Specialties</span>
          <h2 style="margin:1rem 0 1.5rem">A few things I love working on</h2>
          <ul class="pill-list">
            <li>EMDR therapy</li><li>Complex trauma</li><li>Dissociation</li>
            <li>Parts work · IFS-informed</li><li>Childhood wounds</li>
            <li>Perfectionism</li><li>People-pleasing</li><li>Anxiety &amp; overwhelm</li>
            <li>Identity &amp; self-worth</li><li>Relationship patterns</li>
            <li>Life transitions</li><li>Somatic awareness</li>
          </ul>
          <h3 style="margin-top:2rem;margin-bottom:.75rem;font-size:1.3rem">Credentials</h3>
          <ul class="prose" style="margin:0">
            <li>Licensed Professional Counselor (LPC)</li>
            <li>EMDR-Trained (EMDRIA Institute)</li>
            <li>M.A., Human Services &amp; Counseling — UCCS</li>
            <li>B.S., Sociology — UCCS</li>
            <li>Former school counselor</li>
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
    <div class="container">
      <div class="cta-banner reveal">
        <h2 style="margin-top:0">Let's see if we're a fit.</h2>
        <p>Free twenty-minute call. No pitch, no homework. Just a real conversation.</p>
        <div class="cta-banner__ctas"><a href="../contact.html" class="btn btn-light">Reach out</a></div>
      </div>
    </div>
  </section>
"""

build_page(
  filename="team/katie-pasqualetto.html", depth=1,
  title="Katie Pasqualetto, LPC | EMDR & Trauma Therapy in Colorado",
  description="EMDR and trauma therapy with Katie Pasqualetto, LPC. Practice owner at Crescita Counseling. In-person Colorado Springs, virtual statewide.",
  canonical_path="/team/katie-pasqualetto.html",
  schema={"@context":"https://schema.org","@type":"Person","name":"Katie Pasqualetto","honorificSuffix":"LPC, EMDR-T","jobTitle":"Licensed Professional Counselor & Practice Owner","worksFor":{"@type":"Organization","name":"Crescita Counseling","url":"https://www.crescitacounseling.com/"},"alumniOf":{"@type":"CollegeOrUniversity","name":"University of Colorado, Colorado Springs"},"knowsAbout":["EMDR Therapy","Trauma-Informed Care","Dissociation","Parts Work","Somatic Awareness"],"url":"https://www.crescitacounseling.com/team/katie-pasqualetto.html"},
  content=katie_content
)

# =========================================================================
# ALISSA — unchanged content
# =========================================================================
alissa_content = """
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs reveal"><a href="../index.html">Home</a><span>/</span><a href="../about.html">About</a><span>/</span><strong>Alissa</strong></nav>
        <span class="eyebrow eyebrow--rose reveal">Pre-licensed therapist · LPCC</span>
        <h1 class="page-hero__title reveal">Hi — I'm <em>Alissa.</em></h1>
        <p class="page-hero__lead reveal">In-person in downtown Colorado Springs. Online anywhere in Colorado.</p>
      </div>
    </div>
  </section>

  <section class="section">
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

  <section class="section bg-cream-deep">
    <div class="container-text prose reveal">
      <h2>How I work</h2>
      <p>I work systemically and humanistically, with play therapy techniques mixed in for younger clients, and a trauma-informed lens throughout. I support <strong>children, teens, and adults</strong> navigating anxiety, depression, identity, relationships, and the very particular pressures military families carry.</p>
      <p>I have a real soft spot for <strong>teenagers</strong> — their honesty is medicine — and for <strong>moms</strong> who are trying to remember who they are underneath the role. My hope is that you leave each session a little lighter, a little more recognizable to yourself.</p>
      <p>When I'm not in session: hiking Colorado trails, family time, and slowly easing back into backpacking after a long pause.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="reveal">
        <span class="eyebrow eyebrow--rose">Specialties</span>
        <h2 style="margin:1rem 0 1.5rem">What I love working on</h2>
        <ul class="pill-list">
          <li>Children &amp; adolescents</li><li>Anxiety</li><li>Depression</li>
          <li>Military families</li><li>Parenting support</li><li>Family stressors</li>
          <li>School-related challenges</li><li>Emotional regulation</li>
          <li>Life transitions</li><li>Identity</li><li>Play-therapy techniques</li>
          <li>Systems-informed work</li>
        </ul>
        <h3 style="margin-top:2rem;margin-bottom:.75rem;font-size:1.3rem">Credentials</h3>
        <ul class="prose" style="margin:0">
          <li>Licensed Professional Counselor Candidate (LPCC)</li>
          <li>School Counselor</li>
          <li>M.A., Human Services &amp; Counseling — UCCS</li>
          <li>B.A., Sociology &amp; Communications Studies</li>
        </ul>
        <a href="../contact.html" class="btn btn-rose" style="margin-top:1.75rem">Book with Alissa</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner reveal">
        <h2 style="margin-top:0">Let's start with a call.</h2>
        <p>Twenty minutes, free. We'll see if I'm the right fit for what you're carrying.</p>
        <div class="cta-banner__ctas"><a href="../contact.html" class="btn btn-light">Reach out</a></div>
      </div>
    </div>
  </section>
"""

build_page(
  filename="team/alissa-brown.html", depth=1,
  title="Alissa Brown, LPCC | Therapy for Kids, Teens & Military Families",
  description="Therapy with Alissa Brown, LPCC — children, teens, military families, anxiety, and parenting support. Colorado Springs and virtual statewide.",
  canonical_path="/team/alissa-brown.html",
  schema={"@context":"https://schema.org","@type":"Person","name":"Alissa Brown","honorificSuffix":"LPCC","jobTitle":"Pre-Licensed Therapist","worksFor":{"@type":"Organization","name":"Crescita Counseling","url":"https://www.crescitacounseling.com/"},"knowsAbout":["Child Therapy","Teen Therapy","Anxiety","Military Families","Play Therapy"],"url":"https://www.crescitacounseling.com/team/alissa-brown.html"},
  content=alissa_content
)

print("About + team done.")
