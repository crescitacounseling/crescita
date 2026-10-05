# Crescita Journal: publishing calendar

Four posts a month, on the 1st, 8th, 15th and 22nd, starting October 2026. Every post below is written, has its photo, and is waiting in this folder.

Publishing is automatic. A GitHub Action (`.github/workflows/publish-journal.yml`) runs `scripts/journal.py` every morning at about 7 am Mountain time. Any post dated today or earlier gets its page, the Journal index and sitemap are rebuilt, and the change is committed to `main`, which Cloudflare Pages deploys. You can also run it by hand from the repo's Actions tab (Publish journal posts, then Run workflow).

To change the order, edit the `date:` line at the top of a post. To add one of Katie's own posts, add a new `.md` file with the same header fields and give it a date.

| # | Publish date | Title | Topic | Image | Status |
|---|---|---|---|---|---|
| 1 | 2026-10-01 | What an EMDR Session Actually Feels Like | EMDR | `garden-gods-pine` | published |
| 2 | 2026-10-08 | What to Expect at Your First Therapy Session in Colorado Springs | Individual Therapy | `pikes-peak-forest-lake` | scheduled |
| 3 | 2026-10-15 | Is It Anxiety or Is It Burnout? | Anxiety | `creek-stream` | scheduled |
| 4 | 2026-10-22 | Questions to Ask on a Therapist Consultation Call: A Simple Checklist | Individual Therapy | `foothills-pine-ridge` | scheduled |
| 5 | 2026-11-01 | Why the Holidays Can Stir Up Old Family Stuff | Trauma | `pikes-peak-moonrise-city` | scheduled |
| 6 | 2026-11-08 | People-Pleasing Isn't a Personality Trait | Anxiety | `pikes-peak-overlook` | scheduled |
| 7 | 2026-11-15 | Grief in the First Holiday Season After a Loss | Grief | `garden-gods-winter-fence` | scheduled |
| 8 | 2026-11-22 | Perfectionism and the Fear of Getting It Wrong | Anxiety | `balanced-rock-snow` | scheduled |
| 9 | 2026-12-01 | When Winter Break Isn't a Break: Supporting Stressed Teens | Child & Teen | `garden-gods-snow-sun` | scheduled |
| 10 | 2026-12-08 | Panic Attacks: What's Happening in Your Body | Anxiety | `manitou-creek-bridge` | scheduled |
| 11 | 2026-12-15 | Why New Year's Resolutions Fail When You're Running on Empty | Individual Therapy | `garden-gods-first-snow` | scheduled |
| 12 | 2026-12-22 | Your Body Remembers: Somatic Awareness in Trauma Therapy | Trauma | `red-rock-canyon-quarry` | scheduled |
| 13 | 2027-01-01 | Online Therapy in Colorado: What to Expect From Your First Video Session | Online Therapy | `mountains-wide` | scheduled |
| 14 | 2027-01-08 | What "Parts Work" Means, in Plain English | Parts Work | `garden-gods-rock-spires` | scheduled |
| 15 | 2027-01-15 | EMDR vs. Talk Therapy: How to Choose | EMDR | `garden-gods-formation` | scheduled |
| 16 | 2027-01-22 | Dissociation: When You Feel Far Away From Your Own Life | Dissociation | `pikes-peak-haze` | scheduled |
| 17 | 2027-02-01 | Complex Trauma: When It Wasn't One Big Thing | Trauma | `garden-gods-panoramic` | scheduled |
| 18 | 2027-02-08 | Signs Your Child Might Benefit From Therapy | Child & Teen | `garden-gods-window` | scheduled |
| 19 | 2027-02-15 | Helping Military Kids Through a PCS Move | Military Families | `pikes-peak-highway-snow` | scheduled |
| 20 | 2027-02-22 | Grieving Someone Who's Still Here | Grief | `red-rock-canyon-sunrise` | scheduled |
| 21 | 2027-03-01 | Coming Home: The Hidden Adjustment After Deployment | Military Families | `pikes-peak-reservoir` | scheduled |
| 22 | 2027-03-08 | How to Know If a Therapist Is a Good Fit | Individual Therapy | `manitou-incline-boulder` | scheduled |
| 23 | 2027-05-01 | Mental Health Awareness Month: Small Steps That Count | Individual Therapy | `pikes-peak-meadow` | scheduled |
| 24 | 2027-06-15 | Summer Without Structure: Supporting Anxious Kids | Child & Teen | `manitou-deer-crossing` | scheduled |
| 25 | 2027-08-01 | Back-to-School Anxiety: A Parent's Guide | Child & Teen | `downtown-colorado-springs` | scheduled |
| 26 | 2027-09-01 | Suicide Prevention Month: How to Check In on Someone You're Worried About | Mental Health | `garden-gods-evening-light` | scheduled |

## Gaps to fill

Weekly posts run through March 8, 2027. After that only the seasonal posts remain (May 1, June 15, August 1, September 1). Roughly 24 more posts are needed to keep four a month through September 2027. Katie's Drive folder (`ops/katie-blog-ideas.md`) is the first place to look for new topics.
