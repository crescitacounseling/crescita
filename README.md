# crescitacounseling.com

Website for Crescita Counseling (Colorado Springs). Plain HTML, CSS and JS with no build step.

## Hosting

- Cloudflare Pages project `crescita`, connected to this repo. Every push to `main` deploys to www.crescitacounseling.com. The bare domain redirects to www with a Cloudflare redirect rule.
- Other branches get preview URLs on `*.crescita.pages.dev`.
- `_headers` sets caching and security headers and keeps working folders (`content/`, `scripts/`, `ops/`) out of search results. `_redirects` maps old Squarespace URLs to the new pages.
- GitHub Pages is turned off and is not used.

## Forms

The contact and careers forms send through EmailJS (service `service_zrkwriq`; templates `template_4ho9sxo` for contact, `template_careers` for careers). Both deliver to info@crescitacounseling.com.

## Journal

- Posts live in `content/journal/*.md`; the schedule is in `content/journal/CALENDAR.md`.
- `scripts/journal.py` builds each post whose date has arrived, the Journal index, and the sitemap.
- `.github/workflows/publish-journal.yml` runs that script every morning and pushes any new post to `main`, so publishing is automatic.
- Photo sources and photographers: `assets/images/CREDITS.md`.

## Ongoing work

`ops/AUTOPILOT.md` describes the publishing job and the monthly report.

## Making changes

When `css/styles.css` or `js/main.js` changes, bump the `?v=` value on their links in every page (and in `services/emdr-therapy.html`, which the Journal pages copy their header and footer from).
