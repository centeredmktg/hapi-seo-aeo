# GEO / AI Search Readiness: stayhapi.com

Audit date: 2026-11-17. Scope: AI crawler access, llms.txt, passage citability, entity disambiguation, category-query visibility.
Method: raw HTML fetches (Webflow is server-rendered, so no JS render was needed), a crawl of all 223 /resources and /connections sitemap URLs (215 fetched, 8 timed out), and DuckDuckGo Lite SERPs (Bing-backed index). Google, Brave and Mojeek returned CAPTCHA or 429 to scripted requests, so they were not used.

## AI Search Readiness Score: 49 / 100

| Dimension | Weight | Score | Basis |
|---|---|---|---|
| Citability | 25% | 45 | Product pages are short taglines with no statistics. The flagship "2026 PMS API Study" page has no body. One FAQPage schema exists. |
| Structural readability | 20% | 50 | Every article carries hidden case-study H2s and duplicated H3 sets. Few question-form headings. |
| Multi-modal | 15% | 30 | All 200 homepage images have alt="". Video is almost absent (one iframe, on /who-we-serve/technology-providers). |
| Authority and brand | 20% | 45 | No bylines, no Organization schema, no sameAs. The "Hapi" name collides with other brands. Some independent third-party listings exist. |
| Technical accessibility | 20% | 70 | Server-rendered, and every AI crawler UA tested gets a 200. No llms.txt. Most CMS pages have an empty title. |
| **Weighted total** | | **49** | |

## AI crawler access (verified with UA spoofing from a non-bot IP)
robots.txt is `User-agent: * / Disallow:`, which allows everything. The site is behind Cloudflare and hosted on Webflow.
- HTTP 200: OAI-SearchBot, ChatGPT-User, GPTBot (OpenAI training), Claude-SearchBot, Claude-User, ClaudeBot (Anthropic training), PerplexityBot, Perplexity-User, Googlebot, Bingbot, Google-Extended, Applebot-Extended, CCBot, cohere-ai, meta-externalagent.
- HTTP 403: Bytespider. Some Cloudflare or Webflow bot rule is active, but it did not block any search-relevant AI crawler.
- Caveat: Cloudflare can treat verified-bot IPs differently from my spoofed UAs. Confirm with Cloudflare logs (AI Crawl Control).
- No llms.txt, llms-full.txt or RSL license.xml (all return 404).

## Category-query visibility (DuckDuckGo Lite, US-en, 2026-11-17)
| Query | stayhapi.com positions | Who else ranks |
|---|---|---|
| hotel data integration platform | #1 /product-overview, #3 home, #9 resource article | hoteltech.review 2026 listicle (#2), Cloudbeds, hotel-online.com/industry-resources/hapi (#5), Oracle OHIP, Hospitality Net (Ireckonu opinion piece), Asksuite |
| hotel PMS integration middleware | **Not in top 10** | Cloudbeds (2 URLs), Hotel Integr8 (2 URLs), TigerTMS, Roommaster, Priority, SiteMinder, CHAR PMSLINK, Cave Group |
| hospitality API integration platform | #4 home | Oracle (3 URLs at #1-3, #7), PLANEKS, Apaleo, PolyAPI, hoteltech.review |
| Hapi hotel data platform | #1, #2 | hotel-online, hotelmanagement.net (2), hospitalityupgrade.com, LinkedIn /company/hapicloud, Aquiva case study, hapi.dev (#9) |

Note that this differs from what the other agents reported. In this index, stayhapi.com's own pages rank directly for two of the three category queries, not only through syndicated copies. The middleware query is the real gap, even though /connections is titled "PMS middleware | ...".

The hoteltech.review 2026 listicle ("Hotel API Integration Platforms 2026") lists Hapi first: "Purpose-built for hospitality, Hapi is one of the most widely used hotel integration platforms." It calls the brand "Hapi (Hotel API)" and, per a WebFetch summary, gives no web address for it. The page lists Impala, Mews Marketplace, SiteMinder Exchange, Oracle OHIP and Zapier/Make next to Hapi. This is the kind of third-party passage AI engines quote.

## Entity disambiguation ("Hapi")
Bing SERP for "Hapi" and for "Hapi hotel" (scripted request, Bing likely served degraded results, so treat as indicative):
1. Hapi (LATAM US-stock investing app, 2 results)
2. Hapi (Nile god), Wikipedia
3. "HAPI" (unidentified)
4. **stayhapi.com at #5**
5. hapi.dev (Node.js framework), HAPI = hospital-acquired pressure injury (WCA), Hapi app, Hapi voice-notes Mac app, HAPI vibe-coding tool

More collisions:
- The query "stayhapi" returns stay.hapibenefits.com ("stayhapi" MyHub) at #3. Another company uses the exact domain-brand string.
- Brand strings are inconsistent: "Hapi", "HAPI", "Hapi (Hotel API)" (third party), the legacy name "Data Travel" (hotelmanagement.net and the site's own press releases), and the LinkedIn slug "hapicloud".
- **No JSON-LD on the home, our-story, product-overview or connections pages.** There is no Organization schema, no sameAs, no legalName or alternateName ("Data Travel"), and no foundingDate. The only JSON-LD found in the pages sampled is the FAQPage on /product/hapi-connectivity.

## Passage citability (raw-HTML paragraph analysis)
- Home, product-overview, Connectivity, Connections, Our Story and Technology Providers pages: no paragraph exceeds 117 words, and 0 paragraphs fall in the 130-170-word range. None of these pages contains a single % statistic. The copy is taglines ("Connect once. Reach every system we support."), not answerable definitions.
- The home H3s are duplicated: the four persona blocks render twice (likely a desktop/mobile or carousel duplicate).
- /product-overview still has H2s for legacy products ("Hapi Data Streams", "Hapi Finders", "Hapi Guest CRM") next to the current four products. This gives an AI system conflicting product facts.
- /resources/the-2026-pms-api-study is the flagship research asset, but the page is effectively blank. It has an empty title and description, the H1 plus "October 1, 2026 / Hapi In The News / Originally published on" with no outbound link, and no findings at all. It has zero citable content.
- Every resource article includes hidden template H2s ("About / The Challenge / The Solution / The Results", `w-condition-invisible`) and the CTA H2 "Simplify the complex hotel tech landscape" up to three times. These add noise to the heading outline that crawlers see.
- Strongest page: /resources/data-lakehouse-vs-cdp-whats-the-difference-for-hotel-groups. It has a question-form H1, definitional H2s ("What a CDP is built to do"), and a date. It still has no byline and no statistics.
- No resource page sampled has an author byline. Dates are present on articles.
- The IHG case study (3,600+ hotels, "90%") has the most citable stats on the site, but it is one of the pages with an empty title and meta description.

## Findings

### Critical
1. **Empty title and meta description on most CMS pages.** I found 144 of 215 fetched pages with an empty `<title>` (99 resources, 45 connections). This includes the IHG case study, the PMS API Study and all /connections/* pages. The coordinator's figure is 146. AI engines and SERPs fall back to the H1 or skip these pages.
2. **The flagship research page (the 2026 PMS API Study) has no content.** There is nothing for an AI engine to cite on Hapi's most citable asset type (original data).

### High
3. **The brand name is not disambiguated.** "Hapi" ranks #5 on its own name behind an investing app, an Egyptian god and hapi.dev. There is no Organization/sameAs/alternateName schema to tie stayhapi.com, LinkedIn "hapicloud", "Data Travel" and "Hapi (Hotel API)" together. Fix: add Organization JSON-LD sitewide with sameAs, alternateName ["Hapi", "Data Travel", "Hapi Cloud"], and a one-sentence definitional H1 or intro of the form "Hapi is a hospitality data integration platform that...".
4. **No visibility for the "hotel PMS integration middleware" query** (not in top 10), even though /connections is titled for it. Cloudbeds, Hotel Integr8 and TigerTMS hold the answer slots. Fix: write a definitional page ("What is hotel PMS middleware?") with a comparison table, supported PMS count and two-way transaction scope.
5. **Product pages have no extractable facts.** There are no numbers (PMS count, hotels connected, uptime, latency), no "X is Y" definitions and no comparison tables.

### Medium
6. Legacy product H2s on /product-overview conflict with the current product names.
7. Hidden template H2s and duplicated H3s on every article and on the homepage.
8. No author bylines or Person schema on resources. The CEO and staff exist (people spotlights) but are not linked as authors.
9. All homepage images (200) have empty alt text, and video is almost absent (one iframe).

### Low
10. No llms.txt (low impact. It's a cheap addition that lists the 4 product pages, /connections and the best resources).
11. Bytespider gets a 403. Fine as a training-only block, but confirm the rule is intentional and not a broader bot-fight setting.
12. sitemap.xml is served with `Content-Type: application/rss+xml`. It is valid sitemaps XML, but the type should be `application/xml`.

## Top 5 changes (effort)
1. Bind the CMS title and description fields in the Webflow collection templates (resources, connections) to Name/Summary. This is about 1 hour and fixes 144+ pages.
2. Publish the 2026 PMS API Study findings as an HTML page, with key statistics in self-contained 130-170-word blocks, a methodology section and a date. About 1-2 days.
3. Add sitewide Organization JSON-LD (sameAs LinkedIn/Instagram/Crunchbase, alternateName, logo, foundingDate) and a definitional first paragraph on the homepage and /product-overview. About 2 hours.
4. Build "PMS middleware" and "hotel integration platform" answer pages with FAQPage schema and comparison tables (Hapi vs point-to-point vs OHIP/marketplaces). About 2-3 days.
5. Clean up the templates: remove legacy product sections, remove the hidden case-study H2s from blog posts, dedupe the persona H3s, add bylines. About half a day.

## Platform notes (directional, not measured)
- Bing/Copilot and ChatGPT search (Bing-backed index): stayhapi already ranks for 2 of 3 category queries in the DDG/Bing index. Fixing titles and entity schema has direct upside here.
- Google AIO: not measured (Google blocks scripted requests).
- Perplexity: not measured (no API access in this session).

## Not verified
- Wikipedia/Wikidata entity for Hapi the company: requests failed or timed out, so its presence is unknown.
- Reddit and YouTube brand mentions: Reddit returned 403 and the reddit MCP was not loaded. Unverified.
- Live ChatGPT/Perplexity/Google AIO answers for the category queries: not measured. DataForSEO was not available.
- Cloudflare treatment of real verified-bot IPs (only UA spoofing was tested).
