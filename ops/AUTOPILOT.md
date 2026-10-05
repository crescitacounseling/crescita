# Crescita autopilot playbook

Two scheduled jobs run against this repo. Each run starts fresh, so everything a run needs is written here. Keep runs short: follow the steps, don't redesign anything, don't rewrite posts that are already in the queue.

Site: https://www.crescitacounseling.com (static HTML, deployed from `main`).
Owner of the work: Chad (web designer). Client: Katie Fortunato, LPC, Crescita Counseling.

## Job 1: Journal publisher (automatic, no Claude run needed)

Publishing is handled by GitHub Actions, not by a scheduled Claude job. `.github/workflows/publish-journal.yml` runs every morning at 13:05 UTC (about 7 am Mountain). It runs `python3 scripts/journal.py` for today's date in America/Denver, and if a post was due it commits the new page, `journal/index.html` and `sitemap.xml` to `main` as github-actions[bot]. Cloudflare Pages deploys the push in a minute or two.

Schedule: four posts a month, on the 1st, 8th, 15th and 22nd. See `content/journal/CALENDAR.md`.

To check a run: GitHub, then the repo's Actions tab, then "Publish journal posts". Each run's summary shows what was published and the Google Business Profile text for it. To publish by hand: same page, "Run workflow".

If a run fails, the usual causes are a malformed post header (fix the `.md` file) or Actions write permission turned off (repo Settings, Actions, General, Workflow permissions: "Read and write").

Google Business Profile posts still need to be posted by hand (or by a scheduled Claude job if Chad sets one up). The text for each post is the `gbp:` line in its `.md` file and in the Action's run summary; attach `https://www.crescitacounseling.com/assets/images/<image>.jpg`.

## Job 2: Monthly report (3rd of each month)

Data comes from the Google Sheet named **Crescita Monthly Analytics** in Chad's Google Drive. It's refreshed automatically on the 1st by two Sheets add-ons: *GA4 Reports Builder for Google Analytics* (tab `GA4`) and *Search Analytics for Sheets* (tab `Search Console`).

1. Find the sheet with the Google Drive connector (search the title). Read last month's and the previous month's rows.
2. If the sheet is missing or stale, still send the summary: list what was published last month (from `git log --since` on `content/journal` and `journal/`), and include the setup steps from "Analytics setup" below.
3. Write the report for Chad with: users, sessions, top 5 pages, top 10 Google search queries, total Google clicks and impressions, average position, contact-page visits, and month-over-month change for each. Also list the posts published that month.
4. Write a short email Chad can forward to Katie. It should be 150 to 250 words, plain language, warm and specific. Lead with the clearest win. Explain any dip honestly with context (seasonality, a new page still settling). End with what's coming next month. No jargon without a one-line explanation.
5. Summary (emailed to Chad): the report first, then the email for Katie under the heading "Email to Katie".

## Voice rules (posts and emails)

- Plain, warm, specific. Short and long sentences mixed. Concrete over abstract.
- No em dashes. US English.
- Avoid: journey, navigate/navigating, holistic, safe space, hold space, meet you where you are, tailored, empower, transformative, delve, unlock, crucial, vital, furthermore, moreover.
- Never make clinical promises or invent statistics. Crisis topics include 988 and 911 and say Crescita is not a crisis service.

## Analytics setup (one time, about 15 minutes)

1. In Chad's Google Drive, create a Google Sheet named exactly **Crescita Monthly Analytics**.
2. Extensions → Add-ons → install **GA4 Reports Builder for Google Analytics**. Create a report on a tab named `GA4` for the Crescita property: last month, metrics `totalUsers`, `sessions`, `screenPageViews`; dimension `pagePath`. Schedule it to run monthly on the 1st.
3. Install **Search Analytics for Sheets**. Set up a monthly backup to a tab named `Search Console` for `https://www.crescitacounseling.com/`, grouped by query and page.
4. Optional, for Katie: a free Looker Studio report on the same data, scheduled to email her a PDF on the 1st.
