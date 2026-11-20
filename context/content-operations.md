# D6: Content operations

**The question:** how does content get from idea to published to measured, and what has the lack of a written process cost us?

**Current understanding:** there are a few high-level content pillars. There's no written process for drafting, review or publishing, and no target cadence.

**Status:** Open. The defect evidence below comes from the 2026-11-17 site audit; the process questions are still unanswered.

---

## What a missing process has already cost: defects back to missing controls

Each row is something the audit found on the live site, and the step that would have caught it.

| What's live today | Count | Missing control |
|---|---|---|
| Posts published with a headline and date but no body (including the 2026 PMS API Study) | ~18 | Publish gate: no body, no publish |
| Empty `<title>` and meta description | 146 pages | Required CMS fields + template fallback |
| Near-duplicate posts each claiming to be the original (Revinate x4, others x2) | 5+ pairs | Check for an existing page before creating one |
| CMS working note live as a URL (`...---also-cover-on-website`) | 1 | Slug review before publish |
| "Meta Title:" pasted into a live title | 1 | Preview / QA step |
| Byline "Author 1", "Guides", "Hapi", or none | 88 of 166 | Named author required |
| Third-party articles reposted with the source field empty | 2+ | Rights and attribution review |
| "Originally published on" with no link | ~12 | Required source URL for In The News items |
| Resources with no date | 29 | Required publish date |
| Our news ranking on other sites instead of ours | 4 of 6 queries tested | Publish-first, syndicate-later rule |
| Same 6 "Related Posts" on every article; 134 of 144 with no in-body links | site-wide | Internal linking step in the draft checklist |

**The read:** the writing isn't the problem. The product pages and recent comparison posts are good. What's missing is a gate between "drafted" and "live," and anyone who can publish to Webflow can ship anything.

## Output so far: volume vs substance

| Year | Dated items | Substantive (300+ body words) |
|---|---|---|
| 2024 | 9 | — |
| 2025 | 33 | 25 |
| 2026 (to Nov 4) | 39 | 25 |

There were no posts in April 2026. Of 166 resources, roughly 80 are press releases or "In The News" items and 11 are people spotlights. In practice, real output is about **two substantive pieces a month**, without a schedule. That's the honest baseline any cadence target should start from.

---

## Proposed system (draft, to test against how the team works today)

### Stages and gates

Each stage has an owner and a "done when" condition. A piece can't move forward until the condition is met.

| Stage | Done when | Owner (TBD) |
|---|---|---|
| 1. Brief | Pillar, target search or reader question, content type, the page it supports, and the SME are named | Marketing |
| 2. Draft | Body written in the content type's template, with 3+ internal links and a named author | Writer |
| 3. Expert review | Product/technical facts checked by the subject expert | SME |
| 4. Brand review | Category language, voice, claims with sources | Marketing |
| 5. Build | Entered in Webflow with every required field (below) | Marketing ops |
| 6. QA and publish | Pre-publish checklist passes; published on stayhapi.com first | Marketing |
| 7. Distribute | Syndication 3–7 days later with a link back; LinkedIn, sales enablement, email | Marketing |
| 8. Measure and refresh | 30/90-day check; refresh or merge anything that's decayed | Marketing |

Press releases and "In The News" items take a short path (1 → 4 → 5 → 6 → 7), but still pass the publish gate.

### Pre-publish checklist (every row maps to a defect above)

- [ ] Body present, at least the template minimum for its type
- [ ] SEO title (≤60 chars) and meta description (≤155 chars) filled in by hand
- [ ] Named author with a bio page; not "Hapi"
- [ ] Publish date set
- [ ] Slug is clean, with no `-2`, hash suffix or working notes
- [ ] Searched the CMS for an existing page on this topic (update it instead of duplicating)
- [ ] 3+ in-body links to product, connection or hub pages
- [ ] Third-party content: rights confirmed, source named and linked, canonical to the original
- [ ] In The News: summary plus a working source link
- [ ] Image alt text written
- [ ] Previewed on mobile

### Content types and their templates

| Type | Purpose | Required parts |
|---|---|---|
| Customer story | Proof for the revenue/ops buyer | Challenge, solution, a numeric result, a named quote, the products used, links to the matching connection pages |
| Integration (connection) page | The self-serve storefront | Data flows, use cases, customer proof, docs link, setup type |
| Comparison / explainer | Search and AI citation | Quick-answer paragraph up top, definitions, comparison table, author |
| Original research | Links, citations, sales conversations | HTML findings page plus a gated PDF; each statistic written to stand on its own |
| Press release | Announcements | Published here first; links to the relevant product page |
| In The News | Third-party coverage | 150–300 word summary, a link to the source, noindex if thin |

### Cadence: set by capacity, not by wishes

Start with what the team can sustain, then raise it once the gates hold for a quarter.

- **Proposed floor:** 2 substantive pieces a month (today's real output, made predictable), plus 2 refreshes or merges of existing pieces a month.
- **Publish news when it happens**, through the short path.
- **Pick the first quarter's topics from the PMS integration hub plan** (`reports/seo-audit-2026-11-17/data/clusters.md`), so every piece adds to one cluster instead of spreading thin.

<!-- TODO(Danny): set the floor once you know who actually writes.
     2/month assumes roughly one writer-day a week. Adjust to match real capacity. -->

### Make the gates cheap to enforce

- **Webflow:** make SEO title, meta description, author and publish date required fields in both Collections, and add template fallbacks. This prevents defects instead of catching them later.
- **Weekly site check:** a script that crawls `/resources` and `/connections` and flags empty titles, empty bodies, duplicate titles, odd slugs and missing authors. It starts from the existing page check and runs on a schedule without anyone touching it. Its output feeds a monthly content health page in the Hapi report format.
- **One tracker:** use whatever the team already uses for tasks. Each piece is a card that moves through the 8 stages.

---

## Other ways to add value fast

- **Clean up the backlog before writing anything new.** Merge the duplicates, fill or unpublish the empty posts, and give the 5 customer stories real titles. That's an immediate quality jump with no new writing.
- **Make the customer stories do more work.** IHG (3,600+ hotels, 90% → 97% checkout success) and Nemacolin are the strongest proof Hapi has. Each can become a connection-page proof block, a sales one-pager, a LinkedIn series and a quote on the homepage.
- **Turn experts into authors.** Luis and Jeff have hall-of-fame and Hyatt/TravelClick credibility, but bylines say "Hapi." A 30-minute monthly interview with each, turned into a draft by marketing, gives real bylines without taking their writing time.
- **Separate news from expertise.** Move press releases and spotlights out of the main resources feed (or into a newsroom), so the expertise library isn't buried under announcements.
- **Write the research findings up once and reuse them everywhere.** The PMS API Study can feed a page, a webinar, sales talk tracks and a year's worth of posts, if it's published as findings and not only a PDF.

---

## Seed (not now): Claude + Webflow MCP to raise volume safely

Idea (2026-11-17): Hapi has Claude and Webflow has an MCP server, so the gates above could become skills. Then volume goes up without the quality going down.

**Rough shape, to design once the manual process has held for a few weeks:**
- **Checks that are rules belong in scripts, not Claude.** Empty title, missing author, odd slug, duplicate title: a scheduled script run against the Webflow API. It's cheap, consistent, and doesn't spend Claude usage.
- **Checks that need judgment are skills.** Brief from a hub plan; draft in the content-type template; review against brand/category language and claims; suggest internal links; write titles, descriptions and alt text.
- **Webflow MCP writes drafts only.** Claude creates and updates CMS items as drafts; a person publishes. Publishing stays a human gate until the error rate earns trust.
- **Build order:** the pre-publish checker first, since it pays off on the existing backlog. Then brief → draft, then the refresh finder (decayed pages from Search Console).

**Built (2026-11-20):** generic versions are in hapi-kit v1.4.0: `cms-content-qa`, `content-brief` and `content-draft`. They're licensed to Hapi like the rest of the kit. Hapi-specific setup stays in this workspace: `context/content-qa.json` (collection IDs, required fields) and the category language in `context/company.md`.

**Before first use at Hapi:**
- Send the hapi-kit notice covering v1.4.0.
- Check the Webflow MCP's permission scopes (draft vs publish).
- Find out who holds the Webflow API token.

## Discovery questions (answer before finalizing the process)

1. Who writes today? In-house, an agency, freelancers, executives?
2. Who can publish to Webflow, and who approves today, formally or informally?
3. Where do the content pillars live, and who set them? Are they tied to the new product suite?
4. Is there legal or PR review for press, customer names and third-party content?
5. What do agreements with syndication partners (Hospitality Net, Hotel-Online, Hotel Tech Report) allow?
6. What tools does the team use for tasks and approvals (Asana, Notion, Slack)?
7. Does sales use any of this content? Which pieces do they actually send?
8. What happened in April 2026, and with the empty 2026 posts? (Ask without blame: it tells us where the process breaks.)

## Output

- A one-page content operating procedure covering the stages, the checklist, content types and cadence.
- Required fields configured in Webflow.
- The weekly site check running.
- A cleaned backlog.

It goes into the roadmap as the first 30-day item, because every later content investment depends on it.
