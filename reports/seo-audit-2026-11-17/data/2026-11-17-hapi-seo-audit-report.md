# stayhapi.com SEO Audit: Day-One Baseline

**Date:** 2026-11-17 · **Site:** https://www.stayhapi.com (Webflow + HubSpot) · **Type:** B2B SaaS, hospitality data integration
**Scope:** all 246 sitemap URLs. Eleven specialist passes: technical, content, on-page, schema, sitemap, performance, visual/mobile, AI search, agent readiness, search experience, backlinks, topic clusters.
**Limits:** No Search Console, GA4, or CrUX access yet. Performance numbers are lab measurements. Rankings come from Bing/DuckDuckGo and a search tool that is not live Google. Backlinks use free data only. Per-area detail with evidence URLs is in the sibling files in this folder.

---

## SEO Health Score: 49/100

| Category | Weight | Score | Driver |
|---|---|---|---|
| Technical SEO | 22% | 58 | Indexing basics pass. Empty CMS metadata, legacy /products links, missing security headers |
| Content Quality | 23% | 58 | Strong product copy and case studies. Empty-body posts, duplicates, reposts without attribution |
| On-Page SEO | 20% | 36 | 146 pages with empty `<title>` and meta description |
| Schema | 10% | 12 | No Organization, Article, or Product markup. Only FAQPage on /product |
| Performance (lab) | 10% | ~70 | Mobile 62–79, desktop 81–97. Lazy-loaded hero, 2.88MB GIF on product page, reCAPTCHA sitewide |
| AI Search Readiness | 10% | 49 | Brand name ambiguous, no quotable facts on product pages, empty flagship study |
| Images | 5% | 55 | Modern formats. Alt text empty on 100% of images, 63 oversized on homepage |

**One-line read:** Hapi doesn't have a positioning problem or a writing problem. It has an unfinished CMS. The two Webflow collection templates that produce 90% of the URLs were never finished, so most of the site is invisible or anonymous to search. That is good news: the biggest gains are configuration, not content.

---

## Why this matters beyond SEO

Any self-serve or partner-led motion needs a lane where a smaller hotel group can **find, connect, and pay** without a sales cycle. That lane's storefront is search plus the 57 `/connections` pages. Those pages are currently the weakest part of the site:

- 45 of 57 have no title or meta description.
- About 35 of each page's ~36 lines of content are template boilerplate.
- "Data Streams: No items found" appears on 36 of them.
- "Why they chose Hapi" is empty on all of them.
- The hub links to only 24 of the 57 in its HTML.

Fixing `/connections` is SEO cleanup and the first build step of the product-led motion. It also gives the 400-account enterprise motion a credible proof surface.

---

## Synthesis (what the eleven passes agree on)

**PERCEIVE.** Eleven independent passes converged on one root cause: CMS template debt. Four separately counted the empty-title problem and got 144–148 pages. Eleven agents hitting the same root cause independently is about as strong as evidence gets without first-party data.

**ANALYZE.** The damage compounds in a chain:
1. Empty titles mean Google writes its own titles from bare H1s like "Mews".
2. That suppresses click-through on the integration searches that carry the most buying intent.
3. Hapi's own press releases, republished on Hospitality Net, Hotel-Online and Hotel Tech Report, then outrank stayhapi.com for Hapi's own story. They show up for 4 of 6 target searches, and 9 of the top 20 results for "Salesforce for hotels PMS integration".
4. Hapi pays for content and other sites collect the rankings.

**Lateral connection.** Hotel Tech Report and hoteltech.review already rank Hapi #1 in category lists ("one of the most widely used hotel integration platforms"), but the citation never links to the site. Third parties have already granted the authority. The site just isn't positioned to receive it.

**VALIDATE.** One real contradiction:
- **The disagreement.** On Bing/DuckDuckGo, Hapi's own pages rank for the main search term: `/product-overview` is #1 for "hotel data integration platform". The other search tool found only republished copies.
- **Treatment.** Google position is **unknown** until Search Console. No claim in this report depends on Hapi being "invisible in search".
- **Excluded.** One agent reported "no thin content" because its word counts included the nav and footer. The body-only count found ~18 resource pages with no body at all, and that's the number used here.

**ACCEPT.** This audit assumes Googlebot sees what curl sees. Every agent hit intermittent timeouts under parallel requests, and one URL that loaded at 9:41 failed at 9:50. If Googlebot meets the same rate limiting, crawl rate is a hidden ceiling on everything below. Search Console crawl stats settles it in week one.

---

## Critical (blocks visibility; fix this week)

### C1. Empty `<title>`, meta description and og tags on 146 CMS pages
- **Scope:** 101 of 166 /resources and 45 of 57 /connections pages. Evidence: `cms-title-check.txt`.
- **Pages affected include:** the IHG case study (3,600+ hotels, checkout success 90% → 97%), the Nemacolin story, both Oracle OPERA connection pages, and the CEO's 2026-10-16 article.
- **Fix:** In Webflow, open each Collection template's page settings. Bind SEO Title to `{Name} | Hapi`, or a dedicated SEO Title field with a fallback to Name. Bind Meta Description to the summary/excerpt field. Bind the og tags the same way.
- **Effort:** about 1 hour per template, two templates.
- **First principle (THINK):** a page with no title gives Google nothing to match or display, so it can't win a click.
- **Unblocks (CONNECT):** C2, H1, H3, H5, and all cluster work.
- **Failure check (ACCEPT):** 14 days after publishing, the `cms-title-check.txt` re-run shows 0 TITLE_EMPTY, and in Search Console "Page indexing" these URLs show Google's chosen title matching ours. If titles are present but impressions don't move in 6 weeks, the constraint is crawl or authority, not metadata.
- **Leading indicator (GROW):** Search Console impressions for `/connections/*` and `/resources/*`, weekly.

### C2. Flagship research and gated assets published with no body
- **Scope:** about 18 /resources pages are a heading and a date with an empty "Originally published on" line, including `/the-2026-pms-api-study` and `/ai-ready-hospitality-data-framework`. 13 of the 39 resources dated 2026 are these empty pages. Every page links to the PMS API Study through Related Posts, so a dead end is linked sitewide.
- **Fix:** Publish the study's findings as an HTML page, with each statistic written as a self-contained block that can be quoted, and keep the gated PDF as the conversion. Then do the same for the AI-ready framework. For the "In The News" stubs, fill in the source link or unpublish them.
- **Why it matters:** original data is the most citable asset for Google and AI engines, and Stayntouch's 2026 PMS API comparison is currently filling that slot.
- **Failure check:** the page gets referring domains and impressions for "PMS API" searches within 60 days. If it doesn't, the gate is hiding too much.

---

## High (fix within 2–3 weeks)

### H1. Rebuild the /connections template into real integration pages
For each partner, give the page:
- what data flows each way;
- 2–3 use cases;
- customer proof, linking to the existing case studies (Salesforce has 4: Hotel X, Margaritaville, Crystalbrook, Nemacolin);
- a link to the matching developers.hapicloud.io docs;
- a setup-time or auth-type statement (cloud credential vs. scoped project).

Also:
- Remove the partner's own marketing tagline. The Salesforce page currently opens with "The #1 AI CRM".
- Fix the OPERA page. It describes legacy OPERA 5 while searchers want OPERA Cloud / OHIP, so add an OPERA Cloud page.
- Hide empty "Data Streams" / "Related Products" / "Why they chose Hapi" blocks with Webflow's conditional visibility, rather than showing "No items found".
- Make the /connections hub link all 57 pages in plain HTML, with no pagination behind JavaScript.

**Sequence:** start with the 10 partners that have the most search demand and the most Hapi customers.
**Failure check:** these pages earn impressions for "[partner] integration" searches. If they don't within 8 weeks, the template is still too thin.

### H2. Make Hapi's own site the original source for its press
- **Rule:** publish on stayhapi.com first, and syndicate 3–7 days later.
- **Ask partners:** request `rel=canonical` back to the original from Hospitality Net, Hotel-Online and others where they allow it.
- **Every release:** links to the matching product or connection page.
- **Cheap win:** ask hoteltech.review to link its "#1 Hapi" mention to the site.

This turns existing PR spend into rankings for Hapi.

### H3. Consolidate duplicates and leaked CMS slugs
Add 301s from each duplicate to the canonical page:
- Revinate partnership: 4 copies.
- Two copies each of the Nemacolin, IHG loyalty, Salesforce guide, AHLA chair, Margaritaville and Rocco Forte pages.
- `sevenrooms-2` and `shiji-2`.
- Hash-suffix slugs.
- `...---also-cover-on-website`, a CMS working note that went live.
- The Micaela Lara page title that contains "Meta Title:".

Full list in `clusters.md` and `content.md`.

### H4. Organization + WebSite schema, plus one name for the company
- **Markup:** add sitewide Organization JSON-LD with `alternateName` (HAPI, Data Travel, Hapi (Hotel API)) and `sameAs` (LinkedIn, Crunchbase, developers.hapicloud.io). Snippet in `schema.md`; confirm the logo URL first.
- **Why:** on Bing, a search for "Hapi" ranks stayhapi.com #5, behind an investing app and the Nile god.
- **Pick one category name.** The site currently uses five: "Connectivity Partner" (homepage title), "Data Infrastructure" (H1), "data-integrations platform" (meta description), "Cloud Data Hub" (/product-overview), "PMS middleware" (/connections). This is a positioning decision before it's an SEO task, and it's yours to make.

### H5. Article schema + real bylines on /resources
- 47 posts have no byline, and one says "Author 1".
- Attribute posts to real people with author pages; /our-story already has strong leadership bios.
- Add BlogPosting / NewsArticle / Article by CMS category, using the snippets in `schema.md`.

### H6. Attribution on reposted third-party articles ⚠️ handle internally first
`/8-best-crm-software-for-hotels-in-2025` is a Fit Small Business listicle, and the CEO's Hotel Business article is reposted in full, both with an empty source field. Before changing anything, find out what permission exists. The fix is attribution plus a canonical tag pointing to the original, or unpublishing. This is a brand and legal question more than an SEO one.

### H7. Image alt text and homepage weight
- **Alt text:** 100% of images have empty alt. Start with the 130+ partner logos (alt = partner name) and the customer logos.
- **Homepage weight:**
  - 200 images, 63 of them more than 2× their rendered size.
  - Every image is lazy-loaded, including the hero.
  - 180 images have no width/height.
  - Fix: set the hero to eager loading with `fetchpriority=high`, add dimensions, and resize.
- **Product page GIF:** /product/hapi-guest-identity ships a 2.88MB animated GIF. Mobile LCP is 18–22s in lab and CLS is borderline (0.07–0.11). Replace it with MP4/WebM.
- **Third-party scripts:**
  - reCAPTCHA (~394KB) loads on every page. Load it on form pages only.
  - swiper loads twice, from jsDelivr and unpkg.
  - Defer Hotjar and HubSpot chat until the page is idle. Mobile TBT of 120–360ms is the main INP risk.

---

## Medium (within 30–45 days)

- **Legacy product links.**
  - `/product-overview` links to `/products/services`, which returns 404.
  - 14 internal links go to old plural `/products/*` URLs that redirect.
  - `/product-overview` still sells Data Streams, Finders and Guest CRM next to the current four products. Retire it or rewrite it as the platform page.
- **Placeholder text sitewide.** "Bibendum amet at molestie mattis." appears 3 times in the Connections menu on every page.
- **Template headings.**
  - A second, empty `<h1>` on 164 of 166 resources.
  - Hidden headings for the case-study template (About / Challenge / Solution / Results) on every article.
  - Homepage persona headings rendered twice.
- **Orphaned pages.** 101 resources and 33 connections pages have no links from other pages' content, only pagination. The "Related Posts" module shows the same 6 posts everywhere: switch it to same-category.
- **Missing descriptions and social tags.** /contact-us, the 2026 survey page, the loyalty hub and the homepage have no og:title/og:description. The homepage meta description is 225 characters.
- **Accessibility for AI agents.** 7 clickable elements on the homepage and 4 on /contact-us have no accessible name. The newsletter form's "Last Name" label points at the email field.
- **Mobile above the fold.**
  - The product page CTA sits below the cookie banner.
  - The /connections hero is mostly empty gradient.
  - 28–37% of mobile tap targets are under 44px.
- **Sitemap.** Remove the 7 legal pages. Make lastmod reflect real content changes rather than bulk publishes. The sitemap is served as `application/rss+xml`.
- **Security headers.** Add CSP, X-Frame-Options, Referrer-Policy and Permissions-Policy. These don't affect ranking, but hotel security teams check them in vendor reviews.
- **Developer docs on a separate domain.** developers.hapicloud.io is linked from the homepage but sits on another domain, so authority it earns doesn't flow to stayhapi.com. Cross-link it from every /connections page and from a /developers landing page.

## Low (backlog)

- Add llms.txt and an explicit AI crawler policy in robots.txt.
- Bytespider gets a 403 while other AI crawlers get through. Confirm that's intentional.
- Fix the 2-hop http-to-https redirect on the apex domain.
- Replace the bare 404 page.
- Add favicon.ico and security.txt.
- Fix the 5 internal links that point to http://.
- Leave the existing FAQPage blocks in place. They give no Google rich result since May 2026, so don't add more.
- Rewrite press releases currently at grade 16–18 reading level.

---

## Content architecture (after Critical + High)

From `clusters.md`. The search-result evidence is strong for the first hub; the other two need search-volume data first.

1. **Hub B: `/hub/hotel-pms-integration`.** Strongest evidence: "hotel PMS integration" and "PMS API integration" share 8 top-ranking URLs, so they belong on one page. Its spokes are the 57 /connections pages, the PMS API Study, and a new OPERA Cloud/OHIP guide. **Build this one first.**
2. **Hub C: `/hub/hotel-guest-data-platform`.** Absorbs the 3 lakehouse/CDP/MDM comparison posts, the loyalty hub and the Salesforce guides. Revinate is the incumbent.
3. **Hub A: `/hub/hotel-data-integration`.** The brand's main term. Cloudbeds' data-architecture hub is the competitor.

Also planned: a comparison page, "integration platform vs point-to-point vs PMS marketplace", for the "PMS middleware" searches where Hapi is absent from the top 10 on Bing.

---

## 30 / 60 / 90

**Days 1–30: Unblock (configuration, no new content)**
- Access: Search Console + GA4 + HubSpot, the Search Console Links export, and Webflow editor rights.
- Pull Search Console crawl stats, to settle whether rate limiting affects Googlebot.
- C1: bind the template metadata, about 2 hours.
- H3: duplicate 301s. H4: Organization schema.
- Placeholder text, legacy /products links, homepage hero image loading.
- Decide the single category name.
- Start the syndication rule (H2).
- Take an SEO drift baseline after the fixes ship, so the next 60 days are measured against today.

**Days 31–60: Rebuild the storefront**
- C2: publish the PMS API Study as HTML.
- H1: /connections template v2 for the top 10 partners.
- H5: bylines and Article schema. H7: alt text and image weight.
- Hub B built.

**Days 61–90: Compound**
- Roll the /connections v2 template out to all partners.
- Hubs C/A, if search-volume data supports them.
- Partner link-back kit for the 57 integration partners (backlinks).
- A partner-marketplace listing audit: Mews, Cloudbeds, Apaleo, OHIP, AWS Marketplace, G2 / Hotel Tech Report.

**Scoreboard:**

| Metric | Source | Target |
|---|---|---|
| Pages with empty titles | `cms-title-check.txt` re-run | 146 → 0 |
| Impressions on /connections + /resources | Search Console, weekly | Track trend |
| Referring domains | Search Console Links | Track trend |
| Demo/contact conversions from organic | GA4 + HubSpot | Track trend |

---

## Files in this folder

| File | Contents |
|---|---|
| `technical.md` | Crawl, redirects, headers, internal links |
| `content.md` | E-E-A-T, empty-body pages, duplicates, authorship |
| `schema.md` | 7 ready-to-paste JSON-LD snippets + rollout order |
| `sitemap.md` | 246-URL status check, programmatic-page quality check |
| `sxo.md` | Search-result analysis on 6 queries, persona scores |
| `clusters.md` | Inventory, search-result overlap, 3-hub plan, top 10 new pages |
| `geo.md` | AI search readiness, brand disambiguation |
| `agentic.md` | Accessibility tree for AI agents, discovery files |
| `visual.md` + `screenshots/` | Above-the-fold, mobile |
| `backlinks.md` | Free-tier link data and its limits, partner link plan |
| `performance.md` | Lab CWV |
| `cms-title-check.txt` | Per-URL title/description status for all CMS pages |
