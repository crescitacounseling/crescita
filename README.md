# crescitacounseling.com

Website for Crescita Counseling (Colorado Springs). Plain HTML, CSS and JS with no build step.

## Hosting

- Cloudflare Pages project `crescita`, connected to this repo. Every push to `main` deploys to www.crescitacounseling.com. The bare domain redirects to www with a Cloudflare redirect rule.
- Other branches get preview URLs on `*.crescita.pages.dev`.
- `_headers` sets caching and security headers and keeps working folders (`content/`, `scripts/`, `ops/`) out of search results. `_redirects` maps old Squarespace URLs to the new pages.
- GitHub Pages is turned off and is not used.

## Contact form (Resend)

The contact form (`/contact`) and the careers application (`/careers`) both post to `/api/contact`, a Cloudflare Pages Function in `functions/api/contact.js`. A `form_type` field tells them apart, and careers subjects start with `[Careers]`. Mail goes out through Resend from a verified subdomain, so it no longer depends on a Gmail sign-in and a password change can't break it.

What each submission sends:
- A branded notification to info@crescitacounseling.com. Hitting Reply answers the visitor or applicant.
- A confirmation email to the person who filled out the form. Contact: the one-business-day reply timeline, phone, email and the 988 line. Careers: worded for job applicants, with a note that they can reply with a résumé attached.

Cloudflare Pages > Settings > Variables and Secrets (set for Production and Preview):

| Name | What |
|---|---|
| `RESEND_API_KEY` | Secret. Resend API key for this domain |
| `TO_EMAIL` | `info@crescitacounseling.com` |
| `FROM_EMAIL` | Verified Resend sender, e.g. `website@notify.crescitacounseling.com` |
| `HEALTH_TOKEN` | Secret. Random string used by the delivery check |
| `HEALTH_TO` | Where delivery checks go (not the practice inbox) |
| `TURNSTILE_SECRET` | Optional. Turns on the Cloudflare Turnstile spam check |

Optional: bind a KV namespace as `SUBMISSIONS` and every inquiry and application is saved for 30 days before any email goes out, so nothing is lost if email delivery fails.

Delivery check: POST to `/api/contact` with header `x-health-token: <HEALTH_TOKEN>` and a name, email and message. It emails only `HEALTH_TO`, with a `[Delivery check]` subject, sends no confirmation email, and never touches the practice inbox. A wrong token gets a 401 and sends nothing.

To rotate the Resend key: create a new key in Resend, paste it into `RESEND_API_KEY`, redeploy, then delete the old key.

If either form ever shows an error, visitors get the phone number and email address directly, so no one is left without a way to reach the practice.

## Journal

- Posts live in `content/journal/*.md`; the schedule is in `content/journal/CALENDAR.md`.
- `scripts/journal.py` builds each post whose date has arrived, the Journal index, and the sitemap.
- Photo sources and photographers: `assets/images/CREDITS.md`.

## Making changes

When `css/styles.css` or `js/main.js` changes, bump the `?v=` value on their links in every page (and in `services/emdr-therapy.html`, which the Journal pages copy their header and footer from).
