# Technical SEO Audit: www.stayhapi.com (2026-11-17)

Technical score: **58 / 100**

Method: all 246 sitemap URLs fetched (all return HTTP 200, none noindex, all self-canonical), plus redirect/variant/header probes. Counts below are from those fetches. Caveat: fetches ran from a sandbox with a rate-limited connection; 24 timeouts were retried and all returned 200.

## Category status
| Category | Status |
|---|---|
| Crawlability | PASS (robots.txt `Disallow:` empty, sitemap declared, valid urlset, 246 URLs, all with lastmod) |
| Indexability | FAIL (empty titles/descriptions on most CMS pages) |
| Security headers | PARTIAL (HSTS + nosniff only) |
| URL structure / redirects | PASS with minor issues |
| Mobile | PASS (viewport meta present) |
| Core Web Vitals (lab signals) | PARTIAL |
| Structured data | FAIL/thin (JSON-LD on 5 of 246 pages) |
| JS rendering | PASS (server-rendered Webflow, full content in raw HTML, 800-2,500 words/page) |
| Hreflang | N/A (none present, single-language site) |
| IndexNow | Not detected |

## Critical
1. **Empty `<title>` on most CMS pages.** Connections: 45 of 58 (45 of 57 detail pages; 12 titled). Resources: 103 of 167 (63 of 166 detail pages titled). Examples: /connections/asi-pms, /connections/mews, /connections/stayntouch, /connections/medallia, /resources/jeff-bzdawka-named-hapi-ceo, /resources/hapi-appoints-jaffrey-ali-as-chief-product-officer, /resources/new-hapi-sandbox-pms-makes-integration-testing-a-joy. Raw HTML shows `<title></title>`. Same pages also have empty meta description, empty `og:title`, empty `og:description`, empty `twitter:description` (45 connections, ~104 resources). Cause: Webflow CMS SEO fields bound to empty collection fields with no fallback. That is roughly 148 of 224 detail pages (about two-thirds of the sitemap) with no author-controlled title or description. Fix: in the Collection template, set the title to a default (`{Name} integration with Hapi | Hapi`), description to a fallback (summary field), and backfill the CMS fields.

## High
2. **Meta description missing on all non-CMS legal/utility pages and thin elsewhere.** No description on /contact-us, /future-of-hotel-data-survey-2026, /hub/hospitality-loyalty-guest-recognition-hub, /privacy-statement, /terms-of-use, /cookie-notice, /service-level-objectives, /htp-terms-of-use, /hotel-terms-of-use, /acceptable-use. The survey, contact, and hub pages are commercial pages and should have one. Hub page also lacks og tags.
3. **Homepage lacks Open Graph/Twitter title and description.** Only `og:image` and `twitter:image` present (grep of /: no og:title). Title and description exist (title "Hapi | Hospitality's Connectivity Partner", 225-char description, which will truncate; keep to ~155).
4. **Structured data nearly absent.** JSON-LD found on 5 pages only (/product/hapi-guest-identity, -data-lakehouse, -connectivity, -autopilot [FAQPage] and /product/services). Zero on homepage (no Organization/WebSite), 167 resources (no Article/BlogPosting, no author/datePublished), 58 connections, who-we-serve. Not validated against Rich Results; presence only.
5. **Security headers incomplete.** On /resources and /product/hapi-connectivity responses: `strict-transport-security: max-age=31536000` (no includeSubDomains/preload) and `x-content-type-options: nosniff` only. Missing: Content-Security-Policy, X-Frame-Options (or frame-ancestors), Referrer-Policy, Permissions-Policy. Served via Cloudflare in front of Webflow; headers can be added at Cloudflare (Transform Rules).
6. **All images have empty alt.** Homepage 200 of 200 `<img>` have `alt=""`; /product/hapi-connectivity 106/106; resource and connection pages same pattern (96/96 on /connections/asi-pms). Includes content imagery and partner logos. Lost image-search and accessibility signal; verify which are decorative in the Designer.

## Medium
7. **Legacy `/products/*` internal links (plural) redirect or 404.** /product-overview links to `/products/services` which returns **404**. Others 301: /products/hapi-finders -> /product/hapi-autopilot (8 links), /products/hapi-data-streams -> /product/hapi-connectivity (6), /products/hapi-guest-crm -> /product/hapi-guest-identity, /products/hapi-data-services -> /product/hapi-data-lakehouse. Update links to the final URLs; fix the 404.
8. **Title/description hygiene on titled pages.** CMS title leak: /resources/hapi-people-spotlight-micaela-lara title is `Meta Title: Meet Micaela Lara: Living Hapi's "Together We Win" Value`. Duplicate titles across two Revinate pages: "Hapi Partners with Revinate to Boost Direct Bookings" (x2, /resources/hapi-and-revinate-partner and a sibling) and "Hapi and Revinate Partner to Boost Direct Bookings and Guest Experience for Hotels" (x2), a likely duplicate-content pair, including slug `...-a2506`. Over-length: 21 resources titles >60 chars and 23 descriptions >160; /product-overview title is 109 chars.
9. **Duplicate-looking slugs with suffixes** (Webflow collision artifacts): /connections/shiji-2, /connections/sevenrooms-2, /resources/margaritaville-partners-with-hapi-for-total-customer-data-strategy-2, and hash suffixes on /resources/hospitality-crm-a-hoteliers-guide-to-learning-salesforce-65f94 (plus an unsuffixed twin), ...-5fd24, ...-f0e57, ...-b8a3c, ...-298fa, ...-a2506. Check for duplicates and consolidate with 301s.
10. **Image CWV risk.** Homepage 200 images, all `loading="lazy"` (no eager/fetchpriority for a hero/LCP image), 180 without width/height attributes (CLS risk). Pages are 76-204 KB HTML. 22-27 scripts per page (9-12 external: HubSpot, HS Forms, GTM/gtag, Hotjar, jsdelivr, unpkg, ajax.googleapis, a cloudfront script); one render-blocking script in `<head>`. INP/LCP not measured (lab-only inspection); run PageSpeed/CrUX to confirm.
11. **Resources pages carry an extra empty `<h1>`** (`<h1 class="guide_title w-dyn-bind-empty"></h1>`): 164 of 167 resources have 2 h1 elements; the second is empty. Cosmetic for crawlers, but conditionally hide it.
12. **Staging fingerprint in production.** Stylesheet is `.../css/staging-hapi-website2.webflow.shared....min.css` on the live site. No noindex observed, so low risk, but confirm no staging domain (*.webflow.io) is indexable and that it noindexes.
13. **Internal links to http://www.stayhapi.com** on 5 pages (76 http link instances counted) each cost a redirect hop; use https.

## Low
14. **Listing pages paginate via query params** (`/resources?3079d758_page=2`, `/connections?5128500c_page=N`, ~48-57 items per page). Individual article/connection pages are mostly reachable only through these (homepage-sourced crawl showed 101 resources and 33 connections with no contextual in-content inbound link). Ensure paginated URLs are crawlable (they are plain hrefs) and add contextual links from product/solution pages to relevant connection pages.
15. Home canonical is `https://www.stayhapi.com` (no trailing slash), consistent with the sitemap and redirect behavior. OK.
16. 404 page is a bare minimal template (906 bytes, title "404 - Page not found", correct 404 status). Add nav and links.
17. /favicon.ico is 404 (a `rel=shortcut icon` PNG is declared, so fine for most clients). No /llms.txt, /.well-known/security.txt.
18. Sitemap includes non-money utility URLs (legal pages, /hub, /future-of-hotel-data-survey-2026). Harmless; consider excluding legal pages.

## Verified passes
- http://stayhapi.com -> https://www.stayhapi.com/ in 2 hops (200); http://www -> https://www 1 hop; https://stayhapi.com -> https://www 1 hop (301 chain to a single www canonical).
- Trailing slash: /resources/ and /product/hapi-connectivity/ 301 to non-slash. No internal links with trailing slash.
- Case: /Resources and /connections/ASI-PMS return 404 (no duplicate-case URLs).
- robots.txt: `User-agent: *` / `Disallow:` (allow all), sitemap at www host; `sitemap_discovery.py` validated /sitemap.xml as valid urlset (200). No AI-crawler-specific rules.
- 246/246 sitemap URLs return 200, self-canonical on the www host, no noindex, no X-Robots-Tag, no canonical mismatches. Content depth: smallest page 601 words (/contact-us); every connection page 750+ words and every resource 800+ words. No thin content.
- Intentional noindex working: /resources/nemacolin-testimonial-2 and sonesta-testimonial-1 (200, noindex, not in sitemap).
- HTTPS + HSTS, viewport meta `width=device-width, initial-scale=1`, server-rendered HTML (no SPA shell), single language, no hreflang needed. HTTP/2, HTTP/3 advertised, Cloudflare CDN with cache HIT.
- Lighthouse-style signals: preconnect to CDN and fonts, preloaded CSS.

## Score rationale (58)
Crawl/redirect/canonical foundations are strong (about 85-90), but the empty title/description/OG on about two-thirds of the indexable URLs, near-absent schema, empty alts, and weak security headers pull the total down. Fixing item 1 alone (CMS template defaults) should lift the score into the high 70s.

## Fix order
1. CMS template fallbacks for title/description/OG, then backfill 148 pages (Critical 1).
2. Add descriptions to commercial pages, homepage OG tags (2, 3).
3. Add Organization/WebSite on the homepage, Article on resources (4).
4. Cloudflare response headers (5); image alt text (6).
5. Fix /products/* links and the 404 (7); title leak and duplicates (8, 9).
