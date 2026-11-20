# Sitemap audit: www.stayhapi.com (2026-11-17)

Sitemap: https://www.stayhapi.com/sitemap.xml, 246 URLs, valid XML, single file (well under 50k/50MB). robots.txt: `Disallow:` (empty), declares sitemap.

## Pass
- Status: all 246 URLs return 200, zero redirects (HEAD/GET, redirects followed, 0 hops).
- Canonicals: 158 pages fetched cleanly in the second pass; every canonical matches the sitemap URL. No noindex found. (Remaining pages fetched flaky; the status check covered all 246.)
- No priority/changefreq tags. Sitemap uses an xhtml namespace but no hreflang links.
- Size OK, no location-page gate (see /connections below).

## Critical
None.

## High
1. **Missing title and meta description on templated CMS pages.** Direct fetch of /connections/amica, /connections/agilysys, /resources/the-2026-pms-api-study, /resources/nemacolin-testimonial-2 returns `<title>` empty and `<meta name="description" content="">`. In the 158-page sample: 45 of 57 /connections pages and 58 of 100 /resources pages have an empty title; 45 and 59 have an empty description. Only a few (e.g. /connections/canary-technologies) are filled. Fix: populate Webflow CMS SEO fields or bind a template (e.g. "{Partner} integration with Hapi"). These pages are in the sitemap, so Google is invited to index title-less pages.
2. **/connections (58 pages) is a programmatic set with near-identical body.** Across 57 fetched profile pages, about 35 of ~36 content lines per page are shared boilerplate; roughly 1 line per page (the partner blurb) is unique. Word counts 752-1106 are mostly template/nav text. Not city-swap doorway content, but it is a swap-the-partner-name template. Count is above the 50 hard-stop threshold, so it needs explicit justification: these are real partner integrations (Agilysys, Oracle Opera, Canary, AWS, Infor, etc.), which is legitimate and safe if each page carries unique setup/use-case content. Currently it does not. Fix: add per-partner content (what data flows, PMS/CRM types, use cases, docs link) and unique titles/descriptions; at least the ~60% unique target. Index page /connections links 24 profile slugs in static HTML (rest probably paginated/JS), so internal linking to the others needs checking.

## Medium
3. **lastmod is mostly stale, bulk-stamped.** All 246 URLs have lastmod (ISO 8601 with ms, valid W3C). But 34 share 2025-06-25T09:48:36Z and 18 share 2025-06-25T10:07:23Z (a CMS bulk publish), 48 of 58 /connections share 2026-01-20. Distribution: 61 in 2025-06, 18 in 2025-07, 27 in 2025-10, rest 2026. Home is 2026-11-16, so lastmod is likely driven by CMS publish events rather than content change; it is not obviously false, but low signal. Do not rely on it.
4. **Legal/utility pages in sitemap.** /terms-of-use (10.6k words), /htp-terms-of-use (9.5k), /hotel-terms-of-use, /privacy-statement, /cookie-notice, /acceptable-use, /service-level-objectives. No priority is set so there is no "prioritization" issue, but they dilute crawl focus and rank for nothing useful. Recommend removing from sitemap (keep indexable and linked in footer), or at least the three terms-of-use variants. Low risk either way.
5. **Testimonial stub pages exist in nav/footer links but not in sitemap, and are likely thin:** /resources/nemacolin-testimonial-2 and /resources/sonesta-testimonial-1 (both 200, empty title/desc, canonical self). Decide: noindex them or add content. (Another testimonial page /resources/new-hapi-sandbox... is in the sitemap, so the set is inconsistent.)
6. **/resources (167 URLs, 68% of sitemap) has duplicate/near-duplicate titles.** Pairs repeat across slugs (e.g. "How Hotels Can Overcome Legacy Systems to Unlock AI", "Sonesta Partners with Hapi to Centralize Guest Data for CDP"), plus several title-less ones. Review for duplicate articles on different slugs; consolidate or canonicalize.

## Low
7. Trailing-slash variant /resources/ returns 301 (to /resources); sitemap lists the clean form. Fine. Homepage listed without trailing slash, matches its canonical.
8. Coverage vs crawl: homepage has 56 hrefs; all internal nav/footer links except the two testimonial pages above are in the sitemap. External links (status.stayhapi.com, developers.hapicloud.io, careers) correctly excluded. Possible subdomain content (developers.hapicloud.io docs) is outside this sitemap; consider whether it has its own.
9. Sitemap structure: single flat file, no index; fine at 246 URLs. Consider splitting by section (connections/resources/core) in Webflow-independent sitemap only if you need per-section indexing reports in Search Console.
10. xhtml namespace declared but unused: harmless.

## Section breakdown
/resources 167, /connections 58, /product 5, /who-we-serve 3, legal 6, other core (/, /our-story, /hub, /contact-us, /product-overview, /future-of-hotel-data-survey-2026) 7.

Method note: raw crawl files are in the session scratchpad; title/description counts come from a 158-page sample of clean fetches and the spot-checks above (empty title confirmed via direct curl on 5 URLs).
