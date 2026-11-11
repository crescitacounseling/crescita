/**
 * Form handler for crescitacounseling.com
 * Cloudflare Pages Function: POST /api/contact
 *
 * Handles both site forms. The request's form_type picks which one:
 *   "contact"  the contact page (default)
 *   "careers"  the careers page application. Its subject starts with "[Careers]".
 *
 * Environment variables (Pages > Settings > Variables and Secrets, set for
 * both Production and Preview):
 *   RESEND_API_KEY    required, secret. Resend API key.
 *   TO_EMAIL          required. Where inquiries and applications land
 *                     (info@crescitacounseling.com).
 *   FROM_EMAIL        required. Verified Resend sender, either a bare address
 *                     (website@notify.crescitacounseling.com) or "Name <address>".
 *   HEALTH_TOKEN      optional, secret. Turns on the delivery check.
 *   HEALTH_TO         optional. Where delivery checks go (Chad only).
 *   TURNSTILE_SECRET  optional, secret. Turns on the Cloudflare Turnstile check.
 *
 * Optional binding:
 *   SUBMISSIONS       KV namespace. When bound, every real submission is saved
 *                     for 30 days before any email is sent, so nothing is lost
 *                     even if email delivery fails.
 *
 * Delivery check: POST with header "x-health-token: <HEALTH_TOKEN>" and any
 * valid name, email and message. It sends one email to HEALTH_TO with a
 * "[Delivery check]" subject, skips the confirmation email and the saved copy,
 * and never touches the practice inbox.
 */

const PRACTICE = 'Crescita Counseling';
const SITE = 'crescitacounseling.com';
const PHONE = '(719) 286-0011';
const PHONE_TEL = '+17192860011';
const PRACTICE_EMAIL = 'info@crescitacounseling.com';
const ADDRESS = '627 N Weber St, Ste 6 &middot; Colorado Springs, CO 80903';

// Contact form select values, mapped to the labels visitors see on the page.
const THERAPY_FOR = {
  myself: 'Myself',
  'my-child-teen': 'My child or teen',
  'myself-and-child': 'Myself and my child/teen',
  'someone-else': 'Someone else',
};
const FORMAT = {
  'no-preference': 'No preference',
  'in-person': 'In-person (Colorado Springs)',
  virtual: 'Virtual',
};
const INTEREST = {
  'not-sure': 'Not sure yet',
  individual: 'Individual therapy',
  emdr: 'EMDR therapy',
  'child-teen': 'Child & teen therapy',
};

// Site palette (css/styles.css).
const C = {
  page: '#F4EEE5', // --cream
  panel: '#EDDFD9', // --blush-s
  dark: '#3A4146', // --slate-d
  ink: '#2A2724', // --ink
  slate: '#50585D', // --slate
  rose: '#8C5E69', // --rose-d
  roseLight: '#DBB3BA', // --rose-s
  taupe: '#6E6361', // --taupe
  line: 'rgba(80,88,93,0.13)', // --line
};

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
  });

const esc = (s = '') =>
  String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const validEmail = (e) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(e || '').trim());

const clip = (v, max) => String(v == null ? '' : v).trim().slice(0, max);

// Checkbox groups can arrive as an array or a comma-separated string.
const list = (v) =>
  (Array.isArray(v) ? v : String(v || '').split(','))
    .map((s) => clip(s, 60))
    .filter(Boolean)
    .slice(0, 12)
    .join(', ');

// Constant-time compare so the token can't be guessed by timing.
function sameToken(a = '', b = '') {
  if (!a || !b || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

const SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif";
const SERIF = "Georgia, 'Times New Roman', serif";
const label = (text, top = 14) =>
  `<div style="font-family:${SANS};font-size:10px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;color:${C.taupe};margin:${top}px 0 4px;">${esc(text)}</div>`;
const value = (html) =>
  `<div style="font-family:${SANS};font-size:16px;color:${C.ink};line-height:1.45;">${html}</div>`;
const eyebrow = (text) =>
  `<div style="font-family:${SANS};font-size:11px;font-weight:600;letter-spacing:0.24em;text-transform:uppercase;color:${C.rose};margin-bottom:14px;">${esc(text)}</div>`;
const longText = (text) =>
  `<div style="font-family:${SERIF};font-size:17px;line-height:1.65;color:${C.ink};white-space:pre-wrap;">${esc(text)}</div>`;

function shell(inner, footerNote) {
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head>
<body style="margin:0;padding:0;background:${C.page};font-family:${SANS};color:${C.ink};">
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background:${C.page};padding:32px 16px;">
  <tr><td align="center">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="max-width:600px;width:100%;background:#FFFFFF;">
      <tr><td style="background:${C.dark};padding:28px 32px;">
        <div style="font-family:${SERIF};font-size:24px;font-weight:300;color:${C.page};line-height:1;">Crescita<span style="color:${C.roseLight};">.</span></div>
        <div style="font-family:${SANS};font-size:10px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;color:${C.roseLight};margin-top:8px;">Counseling &middot; Colorado Springs</div>
      </td></tr>
      ${inner}
    </table>
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="max-width:600px;width:100%;margin-top:18px;">
      <tr><td align="center" style="font-family:${SANS};font-size:11px;color:${C.taupe};padding:8px 16px;line-height:1.6;">${footerNote}</td></tr>
    </table>
  </td></tr>
</table>
</body></html>`;
}

function detailsPanel(rows) {
  const body = rows
    .filter(([, v]) => v)
    .map(([k, v], i) => label(k, i === 0 ? 0 : 14) + value(v))
    .join('');
  return `
      <tr><td style="padding:24px 32px 8px;">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background:${C.panel};border-left:3px solid ${C.rose};">
          <tr><td style="padding:18px 22px;">${body}</td></tr>
        </table>
      </td></tr>`;
}

function replyBlock(f, subject) {
  return `
      <tr><td style="padding:32px 32px 8px;">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0"><tr>
          <td style="background:${C.dark};">
            <a href="mailto:${esc(f.email)}?subject=${encodeURIComponent(subject)}" style="display:inline-block;padding:14px 28px;font-family:${SANS};font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:${C.page};text-decoration:none;">Reply to ${esc(f.first)}</a>
          </td>
        </tr></table>
        <div style="font-family:${SANS};font-size:12px;color:${C.taupe};margin-top:14px;line-height:1.5;">Hitting Reply in your inbox also works. It goes straight to ${esc(f.first)}.</div>
      </td></tr>
      <tr><td style="padding:24px 32px 36px;">
        <hr style="border:none;border-top:1px solid ${C.line};margin:0 0 16px;">
        <div style="font-family:${SANS};font-size:11px;color:${C.taupe};line-height:1.6;">Submitted ${esc(f.when)}<br>Via the ${f.careers ? 'careers page' : 'contact form'} at <a href="https://www.${SITE}" style="color:${C.rose};text-decoration:none;">${SITE}</a></div>
      </td></tr>`;
}

const emailLink = (f) =>
  `<a href="mailto:${esc(f.email)}" style="color:${C.rose};text-decoration:none;font-weight:600;">${esc(f.email)}</a>`;

function contactNotification(f) {
  const inner = `
      <tr><td style="padding:36px 32px 8px;">
        ${eyebrow('New message from the website')}
        <h1 style="margin:0;font-family:${SERIF};font-size:30px;font-weight:300;line-height:1.15;color:${C.dark};">${esc(f.name)} reached out.</h1>
      </td></tr>
      ${detailsPanel([
        ['Email', emailLink(f)],
        ['Phone', f.phone ? esc(f.phone) : ''],
        ['Therapy is for', esc(f.therapyFor)],
        ['Preferred format', esc(f.format)],
        ['Curious about', esc(f.interest)],
      ])}
      <tr><td style="padding:28px 32px 8px;">
        ${eyebrow("What's loud right now")}
        ${longText(f.message)}
      </td></tr>
      ${replyBlock(f, `Re: Your message to ${PRACTICE}`)}`;
  const text = [
    `${f.name} reached out through ${SITE}.`,
    '',
    `Email: ${f.email}`,
    f.phone ? `Phone: ${f.phone}` : null,
    `Therapy is for: ${f.therapyFor}`,
    `Preferred format: ${f.format}`,
    `Curious about: ${f.interest}`,
    '',
    "What's loud right now:",
    f.message,
    '',
    `Submitted ${f.when}`,
  ].filter((l) => l !== null).join('\n');
  return {
    html: shell(inner, 'Someone used the contact form on your website. Reply to this email to answer them directly.'),
    text,
  };
}

function careersNotification(f) {
  const license = f.license + (f.licenseNumber ? ` #${f.licenseNumber}` : '');
  const rows = [
    ['Email', emailLink(f)],
    ['Phone', f.phone ? esc(f.phone) : ''],
    ['License', esc(license)],
    ['States licensed', esc(f.states)],
    ['Certifications and trainings', esc(f.certifications)],
    ['Who they like to work with', esc(f.populations)],
    ['Format', esc(f.format)],
    ['Clients per week', esc(f.caseload)],
    ['Availability', esc(f.availability)],
    ['Earliest start', esc(f.startDate)],
    ['Insurance panels', esc(f.panels)],
    [
      'Résumé or LinkedIn',
      f.resumeLink
        ? `<a href="${esc(f.resumeLink)}" style="color:${C.rose};text-decoration:none;font-weight:600;word-break:break-all;">${esc(f.resumeLink)}</a>`
        : 'No link given. They may email it separately.',
    ],
  ];
  const inner = `
      <tr><td style="padding:36px 32px 8px;">
        ${eyebrow('New application from the careers page')}
        <h1 style="margin:0;font-family:${SERIF};font-size:30px;font-weight:300;line-height:1.15;color:${C.dark};">${esc(f.name)} applied.</h1>
      </td></tr>
      ${detailsPanel(rows)}
      <tr><td style="padding:28px 32px 8px;">
        ${eyebrow('Short bio')}
        ${longText(f.bio)}
      </td></tr>
      <tr><td style="padding:28px 32px 8px;">
        ${eyebrow('Why Crescita?')}
        ${longText(f.why)}
      </td></tr>
      ${replyBlock(f, `Re: Your application to ${PRACTICE}`)}`;
  const text = [
    `${f.name} applied through the careers page at ${SITE}.`,
    '',
    `Email: ${f.email}`,
    f.phone ? `Phone: ${f.phone}` : null,
    `License: ${license}`,
    `States licensed: ${f.states}`,
    f.certifications ? `Certifications and trainings: ${f.certifications}` : null,
    f.populations ? `Who they like to work with: ${f.populations}` : null,
    f.format ? `Format: ${f.format}` : null,
    f.caseload ? `Clients per week: ${f.caseload}` : null,
    f.availability ? `Availability: ${f.availability}` : null,
    f.startDate ? `Earliest start: ${f.startDate}` : null,
    f.panels ? `Insurance panels: ${f.panels}` : null,
    `Résumé or LinkedIn: ${f.resumeLink || 'No link given. They may email it separately.'}`,
    '',
    'Short bio:',
    f.bio,
    '',
    'Why Crescita?',
    f.why,
    '',
    `Submitted ${f.when}`,
  ].filter((l) => l !== null).join('\n');
  return {
    html: shell(inner, 'Someone applied through the careers page on your website. Reply to this email to answer them directly.'),
    text,
  };
}

const footer = `${PRACTICE} &middot; ${ADDRESS}<br><a href="https://www.${SITE}" style="color:${C.taupe};">${SITE}</a>`;
const para = (html, last = false) => `<p style="margin:0 0 ${last ? 0 : 16}px;">${html}</p>`;
const phoneLink = `<a href="tel:${PHONE_TEL}" style="color:${C.rose};">${PHONE}</a>`;
const mailLink = `<a href="mailto:${PRACTICE_EMAIL}" style="color:${C.rose};">${PRACTICE_EMAIL}</a>`;

function contactConfirmation(f) {
  const inner = `
      <tr><td style="padding:36px 32px 8px;">
        <h1 style="margin:0;font-family:${SERIF};font-size:28px;font-weight:300;line-height:1.2;color:${C.dark};">Thank you, ${esc(f.first)}. Your message came through.</h1>
      </td></tr>
      <tr><td style="padding:20px 32px 8px;font-family:${SERIF};font-size:17px;line-height:1.65;color:${C.ink};">
        ${para('We read every message and write back within one business day, usually faster. From there we can set up a free twenty-minute call and help you pick the right clinician.')}
        ${para(`If you don't hear back within one business day, please call ${phoneLink} or email ${mailLink}. Sometimes technology has other plans, and we'd hate to miss you.`)}
        ${para('Crescita Counseling', true)}
      </td></tr>
      <tr><td style="padding:24px 32px 36px;">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background:${C.panel};border-left:3px solid ${C.rose};">
          <tr><td style="padding:16px 20px;font-family:${SANS};font-size:13px;line-height:1.6;color:${C.ink};">
            If you're in crisis or need support right now, call or text <a href="tel:988" style="color:${C.rose};font-weight:600;">988</a>, any time, day or night. Email isn't the right place for an emergency.
          </td></tr>
        </table>
      </td></tr>`;
  const text = [
    `Thank you, ${f.first}. Your message came through.`,
    '',
    'We read every message and write back within one business day, usually faster. From there we can set up a free twenty-minute call and help you pick the right clinician.',
    '',
    `If you don't hear back within one business day, please call ${PHONE} or email ${PRACTICE_EMAIL}.`,
    '',
    'Crescita Counseling',
    '',
    "If you're in crisis or need support right now, call or text 988, any time, day or night. Email isn't the right place for an emergency.",
  ].join('\n');
  return { subject: `Thanks for reaching out to ${PRACTICE}`, html: shell(inner, footer), text };
}

function careersConfirmation(f) {
  const resume = f.resumeLink
    ? 'Thanks for including a link to your résumé or LinkedIn.'
    : "If you have a résumé to share, reply to this email with it attached and it'll go into your application.";
  const inner = `
      <tr><td style="padding:36px 32px 8px;">
        <h1 style="margin:0;font-family:${SERIF};font-size:28px;font-weight:300;line-height:1.2;color:${C.dark};">Thank you, ${esc(f.first)}. Your application came through.</h1>
      </td></tr>
      <tr><td style="padding:20px 32px 36px;font-family:${SERIF};font-size:17px;line-height:1.65;color:${C.ink};">
        ${para("Katie reads every application and will be in touch if it looks like a fit. Specific roles, caseload, and compensation are discussed during the interview.")}
        ${para(esc(resume))}
        ${para(`Questions in the meantime? Call ${phoneLink} or email ${mailLink}.`)}
        ${para('Crescita Counseling', true)}
      </td></tr>`;
  const text = [
    `Thank you, ${f.first}. Your application came through.`,
    '',
    'Katie reads every application and will be in touch if it looks like a fit. Specific roles, caseload, and compensation are discussed during the interview.',
    '',
    resume,
    '',
    `Questions in the meantime? Call ${PHONE} or email ${PRACTICE_EMAIL}.`,
    '',
    'Crescita Counseling',
  ].join('\n');
  return { subject: `We received your application to ${PRACTICE}`, html: shell(inner, footer), text };
}

async function send(env, payload) {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { authorization: `Bearer ${env.RESEND_API_KEY}`, 'content-type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const detail = await res.text().catch(() => '');
    throw new Error(`Resend ${res.status}: ${detail.slice(0, 300)}`);
  }
}

function readFields(data) {
  const careers = String(data.form_type || '').toLowerCase() === 'careers';
  let first = clip(data.firstName || data.first_name, 60);
  let last = clip(data.lastName || data.last_name, 60);
  if (!first && data.name) {
    const parts = clip(data.name, 120).split(/\s+/);
    first = parts.shift() || '';
    last = parts.join(' ');
  }
  const f = {
    careers,
    first,
    last,
    name: [first, last].filter(Boolean).join(' '),
    email: clip(data.email || data._replyto, 200),
    phone: clip(data.phone, 60),
    when:
      new Date().toLocaleString('en-US', { timeZone: 'America/Denver', dateStyle: 'full', timeStyle: 'short' }) + ' MT',
  };
  if (careers) {
    let resumeLink = clip(data.resumeLink, 500);
    if (resumeLink && !/^https?:\/\//i.test(resumeLink)) resumeLink = `https://${resumeLink}`;
    Object.assign(f, {
      license: clip(data.license, 80),
      licenseNumber: clip(data.licenseNumber, 60),
      states: clip(data.states, 200),
      certifications: clip(data.certifications, 2000),
      populations: list(data.populations),
      format: clip(data.format, 60),
      caseload: clip(data.caseload, 40),
      availability: list(data.availability),
      startDate: clip(data.startDate, 80),
      panels: clip(data.panels, 300),
      resumeLink,
      bio: clip(data.bio, 5000),
      why: clip(data.why, 5000),
    });
  } else {
    Object.assign(f, {
      therapyFor: THERAPY_FOR[data.who] || THERAPY_FOR.myself,
      format: FORMAT[data.format] || FORMAT['no-preference'],
      interest: INTEREST[data.interest] || INTEREST['not-sure'],
      message: clip(data.message, 5000),
    });
  }
  return f;
}

function problem(f, health) {
  if (!f.first || !validEmail(f.email)) return 'Please add your name and a valid email.';
  // A delivery check posts the simple contact shape, so it only needs a message.
  if (health) return f.careers || f.message ? '' : 'Please add a message.';
  if (f.careers) {
    if (!f.last || !f.license || !f.states || !f.bio || !f.why) {
      return 'Please fill in your name, email, license type, states, bio, and why Crescita.';
    }
    return '';
  }
  if (!f.last || !f.message) return 'Please add your first and last name, a valid email, and a message.';
  return '';
}

export async function onRequestPost({ request, env, waitUntil }) {
  let data;
  try {
    const ct = request.headers.get('content-type') || '';
    if (ct.includes('application/json')) {
      data = await request.json();
    } else {
      const fd = await request.formData();
      data = {};
      for (const [k, v] of fd.entries()) {
        if (k in data) data[k] = [].concat(data[k], v);
        else data[k] = v;
      }
    }
  } catch {
    return json({ ok: false, error: 'Could not read that submission.' }, 400);
  }
  if (!data || typeof data !== 'object') return json({ ok: false, error: 'Could not read that submission.' }, 400);

  // Honeypot: people never see this field, so anything in it is spam.
  if (data._gotcha || data.company) return json({ ok: true });

  // A delivery check with a wrong or missing token is refused outright, so a
  // misconfigured check can never land a test in the practice inbox.
  const healthHeader = request.headers.get('x-health-token');
  const health = healthHeader !== null && sameToken(healthHeader, env.HEALTH_TOKEN || '');
  if (healthHeader !== null && !health) return json({ ok: false, error: 'Unauthorized.' }, 401);

  const f = readFields(data);
  const issue = problem(f, health);
  if (issue) return json({ ok: false, error: issue }, 400);

  if (env.TURNSTILE_SECRET && !health) {
    const body = new FormData();
    body.append('secret', env.TURNSTILE_SECRET);
    body.append('response', data['cf-turnstile-response'] || '');
    const ip = request.headers.get('CF-Connecting-IP');
    if (ip) body.append('remoteip', ip);
    const v = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', { method: 'POST', body })
      .then((r) => r.json())
      .catch(() => ({ success: false }));
    if (!v.success) return json({ ok: false, error: 'The spam check didn’t go through. Please try again.' }, 400);
  }

  if (!env.RESEND_API_KEY || !env.TO_EMAIL || !env.FROM_EMAIL) {
    return json({ ok: false, error: 'Email is not configured yet.' }, 500);
  }
  if (health && !env.HEALTH_TO) {
    return json({ ok: false, error: 'HEALTH_TO is not set.' }, 500);
  }

  const from = /</.test(env.FROM_EMAIL) ? env.FROM_EMAIL : `${PRACTICE} <${env.FROM_EMAIL}>`;
  const kvTtl = { expirationTtl: 60 * 60 * 24 * 30 };

  // Save first, so the submission survives even if every email below fails.
  if (env.SUBMISSIONS && !health) {
    const key = `${f.careers ? 'application' : 'inquiry'}:${new Date().toISOString()}:${crypto.randomUUID().slice(0, 8)}`;
    try {
      await env.SUBMISSIONS.put(key, JSON.stringify({ ...f, delivered: false }), kvTtl);
      f.savedKey = key;
    } catch (err) {
      console.error('KV save failed', err);
    }
  }

  const note = f.careers ? careersNotification(f) : contactNotification(f);
  const subject = f.careers ? `[Careers] New application from ${f.name}` : `New inquiry from ${f.name}`;
  try {
    await send(env, {
      from,
      to: [health ? env.HEALTH_TO : env.TO_EMAIL],
      reply_to: f.email,
      subject: `${health ? '[Delivery check] ' : ''}${subject}`,
      html: note.html,
      text: note.text,
    });
  } catch (err) {
    console.error(err);
    const what = f.careers ? 'Your application' : 'Your message';
    return json({ ok: false, error: `${what} didn't go through. Please call ${PHONE} or email ${PRACTICE_EMAIL}.` }, 502);
  }

  if (f.savedKey) {
    const { savedKey, ...saved } = f;
    waitUntil(env.SUBMISSIONS.put(savedKey, JSON.stringify({ ...saved, delivered: true }), kvTtl).catch(() => {}));
  }

  // The confirmation email is a courtesy. If it fails, the submission still
  // reached the practice, so the visitor still sees success.
  if (!health) {
    const conf = f.careers ? careersConfirmation(f) : contactConfirmation(f);
    waitUntil(
      send(env, {
        from,
        to: [f.email],
        reply_to: env.TO_EMAIL,
        subject: conf.subject,
        html: conf.html,
        text: conf.text,
      }).catch((err) => console.error('Confirmation email failed', err)),
    );
  }

  return json({ ok: true });
}

export const onRequest = () => json({ ok: false, error: 'Method not allowed.' }, 405);
