# Crescita autopilot playbook

Two scheduled jobs run against this repo. Each run starts fresh, so everything a run needs is written here. Keep runs short: follow the steps, don't redesign anything, don't rewrite posts that are already in the queue.

Site: https://www.crescitacounseling.com (static HTML, deployed from `main`).
Owner of the work: Chad (web designer). Client: Katie Fortunato, LPC, Crescita Counseling.

## Job 1: Journal publisher (1st and 15th of each month)

1. `git fetch origin main` and check out `main`. If `main` does not contain `scripts/journal.py` yet, the site redesign hasn't been merged: run the same steps on branch `claude/crested-counseling-seo-wk5lhr` instead, and say so in the summary.
2. Run `python3 scripts/journal.py`. It publishes every post in `content/journal/` dated today or earlier, rebuilds `journal/index.html`, and refreshes the journal block in `sitemap.xml`. It prints each newly published post's URL and its Google Business Profile text.
3. If nothing new was published, stop and report "no post due".
4. Sanity check: the new page exists in `journal/`, has one `<h1>`, and no `—` in its `<main>`.
5. Commit with a message like `Journal: publish "<title>"` and push to the branch from step 1.
6. Summary (this is emailed to Chad), in this order:
   - Post title and live URL (live a minute or two after the push)
   - The Google Business Profile post text, ready to paste, plus the image to attach: `https://www.crescitacounseling.com/assets/images/<image>.jpg`
   - Next post in the queue: run `python3 scripts/journal.py --next`
   - If fewer than 4 posts remain, say "Queue is running low: add more posts."
   - Any blocker (push refused, script error), stated plainly with the fix.

Never edit post wording during this job. If a post has an obvious problem (broken link, typo in the title), fix only that and mention it.

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
