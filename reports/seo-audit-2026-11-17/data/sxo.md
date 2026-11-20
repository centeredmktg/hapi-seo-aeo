# Hapi (stayhapi.com): Search Experience (SXO) Analysis

**Date:** 2026-11-17
**Scope:** 6 target queries, SERP backwards analysis, page-type mismatch, persona scoring (3 personas), SXO Gap Score on 4 key pages
**Method:** Pages rendered with the claude-seo `render_page.py` (`--mode always`; `--mode never` raw fetch as a fallback). SERPs pulled with WebSearch (not a live Google SERP; see Limitations). Page types use the claude-seo page-type taxonomy.

> SXO Gap Score is a separate measure from the SEO Health Score. It measures how well a page matches what the SERP rewards. It does not measure technical health.

---

## The headline

**Hapi doesn't rank for its own category. Its press releases do.**

In all 6 query sets, no stayhapi.com URL came up. For "hotel data integration platform", "hospitality data platform", "Opera to Salesforce integration hotel" and "hotel data lakehouse", Hapi does show up, but only through syndicated press releases on hospitalitynet.org, hotel-online.com, hoteltechreport.com, traveldailynews.com and lodgingmagazine.com. A `site:stayhapi.com connections` query returned only third-party pages.

So the market already links Hapi to these topics. The problem is that the owned pages are the wrong type, or are empty templates, so third parties collect the clicks.

The single most important finding is that **the `/connections/*` integration pages are the pages that should win the high-intent long-tail ("[PMS] integration", "[PMS] to Salesforce"), and they ship with an empty `<title>`, no meta description, and in several cases empty "Data Streams" and "Why they chose Hapi" sections.**

---

## 1. Query-by-query SERP backwards analysis

### Q1. "hotel data integration platform"

| | |
|---|---|
| **What ranks** | Hapi press release syndicated 4x (hospitalitynet, hotel-online x2, hoteltechreport); traveldailynews launch story; integrate.io listicle "Best Data Integration Platform for Hospitality"; Airbyte industry page; Revinate Guest Data Platform page; Oracle Hospitality Integration Platform (OHIP) product page; iReckonu Integration Hub product page |
| **Page-type mix** | News/press 6 (~40% of slots, but it is effectively one story); Product/Hybrid vendor pages 4 (Revinate, Oracle, iReckonu, Airbyte); Comparison/listicle 1 (integrate.io) |
| **Consensus** | Among non-news results, **Hybrid (product + educational) vendor pages**, about 65% confidence. Google treats this as a commercial-investigation query and serves category-leader product pages. |
| **Hapi best match** | `/product/hapi-connectivity` (title "Hapi Connectivity, One Integration, Every System"; H1 "Connect once. Reach every system we support."; 1,583 words; FAQPage schema). The competing page is `/product-overview` (title "Hapi Data-integration platform, Integrate with the leading hotel PMS systems...", 2,406 words, no schema). |
| **Type match** | Type is ALIGNED (Hybrid). **Mismatch: MEDIUM.** The keyword sits in neither the title nor the H1 of `/product/hapi-connectivity`. The page that does carry "data-integration platform" in its title (`/product-overview`) still uses legacy product names (Hapi Data Streams, Hapi Finders, Hapi Guest CRM, Hapi Data Services) next to the new lineup (Connectivity, Autopilot, Guest Identity, Data Lakehouse). That splits the query across two pages and serves a mixed product story. |

### Q2. "PMS integration platform / hotel PMS API"

| | |
|---|---|
| **What ranks** | roommaster.com blog "Hotel PMS Integration: How It Works"; cloudbeds.com articles/pms-integrations; altexsoft "Opera PMS integration" guide; Stayntouch "What Is a Hotel PMS Open API? A 2026 Comparison Guide" and "Mobile PMS API Documentation: 2026 Developer's Guide"; callsphere.ai "hotel PMS API integration: Opera, Mews, Cloudbeds"; hoteza integrations page; Yeastar developer docs; Lodging Magazine feature; likemagic API page |
| **Page-type mix** | Blog/guide 6 (60%); Docs 2; Vendor integration pages 2 |
| **Consensus** | **Blog Post / long-form guide, ~60-70% confidence.** Informational and early-consideration. The guides that rank are 2026-dated comparison and how-it-works pieces written by PMS vendors. |
| **Hapi best match** | `/product/hapi-connectivity` (product) or `/connections` hub. Hapi already owns a strong informational asset, `/resources/the-2026-pms-api-study`, but it is gated or report-shaped (not assessed in depth) and did not appear in results. |
| **Type match** | **Mismatch: HIGH.** A product page is competing against a guide SERP. PMS vendors (Stayntouch, Cloudbeds, Mews) define the PMS API story for buyers, and the neutral middleware layer (Hapi) is absent. |

### Q3. "hotel CRM integration Salesforce PMS"

| | |
|---|---|
| **What ranks** | Mews blog "Why every hotel should connect their PMS and CRM" (EN and IT); Mews for Salesforce AppExchange press (4 syndications); hospitalitytech.com Mews/Salesforce story; Hapi-authored "Driving Revenue and Digital Guest Journeys Using Salesforce" opinion piece (hotel-online, hospitalitynet); Hapi "Maestro PMS and Hapi Streamline Salesforce Connectivity" press; Hotel Tech Report "Hapi for Salesforce" listing (gated for verified hoteliers) |
| **Page-type mix** | News/press 9; Blog explainer 2 (both Mews); Marketplace listing 1 |
| **Consensus** | Mixed. The click-earning **explainer (Blog Post)** slot belongs to Mews. Most of the rest is press. |
| **Hapi best match** | `/connections/salesforce`: H1 "Salesforce", **empty `<title>`**, **no meta description**, 848 words, lists 10 data streams (Availability, Reservations, Guest Profiles, Inventory, Customer Profiles, Blocks, Financial Transactions, Rates, Stays, Guest Activities). The "About the / Tech Vendor" heading is split across two H2s, and the opening copy is Salesforce's own boilerplate ("The #1 AI CRM..."). |
| **Type match** | **Mismatch: HIGH.** The searcher wants "how do I get PMS data into Salesforce, and who does it". Hapi's page is a vendor-directory card about Salesforce. It does not position Hapi's Salesforce solution (Hapi Connect / Hapi Guest on AppExchange), and it does not link the Hotel X, Margaritaville, Crystalbrook or Nemacolin Salesforce stories that already exist in `/resources/`. |

### Q4. "Opera PMS integration OHIP"

| | |
|---|---|
| **What ranks** | Vendor help-center setup docs (TripAround, Vouch x2, Trybe, Conduit x2, ResDiary x2, Optii, PayFacto); Book4Time OHIP solution brief PDF; Oracle "OHIP and Oracle Integration Cloud" page; altexsoft guide; Lodging Magazine (Sertifi); 10minhotel STAAH guide |
| **Page-type mix** | Docs/how-to 11 (~70%); Oracle product page 1; Guide 2; News 1 |
| **Consensus** | **Documentation / how-to, ~70% confidence.** Searchers are vendors and hotel IT teams setting up an OPERA Cloud connection: credentials, approval steps, data scope. |
| **Hapi best match** | `/connections/oracle-opera-v5-pms`: H1 "Oracle: Opera V5 PMS", **empty `<title>`**, **no meta description**, **Data Streams: "No items found"**, **"Why they chose Hapi": empty**, **Related Products: "No items found"**, 604 words that are almost all site chrome. The copy describes legacy OPERA 5, while the SERP is about OPERA Cloud and OHIP. `/connections/oracle` exists but repeatedly timed out during fetch. |
| **Type match** | **Mismatch: CRITICAL.** This is an empty CMS template on the highest-value PMS in the market. Even if it ranked, a CIO or vendor landing on it would bounce. OHIP's partner path for legacy OPERA 5 and Suite8 is approval-based, which is exactly the pain Hapi removes, and the page says nothing about it. |

### Q5. "hospitality data platform"

| | |
|---|---|
| **What ranks** | hospitalitynet "Data platform 101: How a hotel data platform helps your business" (x2); phocuswire "Understanding hospitality data platforms"; hotel-yearbook "What is a data platform...in hospitality?"; Revinate CDP pages (x2); Cloudbeds "Hotel data platform"; GoodData, Snowflake, Semarchy industry pages; snapshot.travel "Hospitality's Data Platform"; Lighthouse DaaS; traveldailynews Hapi launch story |
| **Page-type mix** | Explainer/blog 5 (~40%); Vendor product/Hybrid 9 (~55%); News 2 |
| **Consensus** | **Hybrid**, ~55% confidence. Vendor product pages that carry real educational depth, plus "What is X" explainers. |
| **Hapi best match** | `/product/hapi-data-lakehouse`: title "Hapi Data Lakehouse, Hospitality Data Platform" (exact keyword), H1 "Clean data. Complete ownership.", 1,516 words, FAQPage schema, "How it works" plus a tech-provider section. |
| **Type match** | **ALIGNED (Low).** This is the best-built page on the site for its query. The gaps are depth (no "what is a hospitality data platform" definitional block, no Lakehouse vs CDP vs warehouse comparison on the page, although `/resources/data-lakehouse-vs-cdp-whats-the-difference-for-hotel-groups` exists) and proof (no named customer or connected-property count above the fold). |

### Q6. "hotel PMS middleware for technology vendors"

| | |
|---|---|
| **What ranks** | TigerTMS iLink (product page and PDF); hospitalitynet expert panels ("Can integration hubs save the day", "Plug-and-play...techno-mirage"); Hospitality Upgrade "Solving the Interface Puzzle"; Hotels mag "middleware isn't the sexiest tech"; Amadeus "A PMS Odyssey"; Cloudbeds; Priority Software FAQ; HotelREZ REZswitch; webrezpro and jengu guides |
| **Page-type mix** | Thought leadership/blog 8 (~55%); Vendor product 4; Guides 3 |
| **Consensus** | **Blog/thought leadership, ~55%**, with vendor middleware product pages (TigerTMS) in the commercial slots |
| **Hapi best match** | `/connections` hub (title "PMS middleware, Learn more about the suppliers using Hapi's data platform"; H1 "Hapi Connections"; 819 words; detected publish date 2015; no schema) and `/who-we-serve/technology-providers` (unreachable in 3 fetch attempts, so not scored) |
| **Type match** | **Mismatch: MEDIUM-HIGH.** The hub's title targets "PMS middleware", but the page itself is a logo grid with a search filter. It has no explanation of the vendor value proposition (build once, reach many PMSs; the 50+ property partner threshold; sandbox PMS), which is the content that ranks. The hub's rendered DOM linked 24 connection detail pages, while the sitemap lists about 57 (the gap may be lazy-load or pagination). |

### Adjacent signal: comparison intent belongs to Hotel Tech Report

The query "Hapi vs Ireckonu / Impala" returns only hoteltechreport.com pairwise pages (in 9 languages) plus SourceForge. The HTR listing uses the legacy product name "Hapi Guest" / "Hapi for Salesforce". Hapi has no owned comparison or alternatives page, and its HTR profile does not reflect the current product names.

---

## 2. User stories (derived from SERP signals)

1. **Consideration, hotel group CIO.** "As a CIO running OPERA plus 3 other PMSs after an acquisition, I want one integration layer that reads and writes to every PMS, so I stop paying for point-to-point rebuilds." *Signal:* Q6 Jonas/Ireckonu ESB snippets about acquiring chains plugging in a new PMS once; Q1 vendor integration-hub pages.
2. **Awareness, tech vendor partner manager.** "As a vendor going to market, I want to know which PMSs have truly open APIs and what OHIP approval takes, so I can scope my integration roadmap." *Signal:* Q2 Stayntouch "2026 comparison guide" and Cloudbeds "only 24 of 343 PMS vendors publish self-serve API docs"; Q4 OHIP approval-step docs.
3. **Decision, tech vendor.** "As a vendor, I want to see exactly which data streams Hapi exposes for OPERA, so I can confirm fit before I book a call." *Signal:* Q4 docs SERP (credentials, data scope, push/pull). Hapi's Opera page shows "No items found".
4. **Consideration, revenue/marketing leader.** "As a VP of Marketing on Salesforce, I want real-time PMS guest and stay data in Salesforce without a failed multi-year IT project." *Signal:* Q3 Hotel X case ("years on an OPERA-to-Salesforce project that stalled"); Mews "why connect your PMS and CRM".
5. **Awareness, CIO / data leader.** "As a data leader asked to make us AI-ready, I want to understand lakehouse vs CDP vs warehouse for hotel data." *Signal:* Q5 explainer dominance; "hotel data lakehouse AI-ready" SERP (Cloudbeds AI readiness, data warehouse guides).

Coverage: Awareness (2, 5), Consideration (1, 4), Decision (3).

---

## 3. SXO Gap Scores (key pages)

| Dimension (max) | `/product/hapi-connectivity` | `/product/hapi-data-lakehouse` | `/connections/salesforce` | `/connections/oracle-opera-v5-pms` |
|---|---|---|---|---|
| Page Type (15) | 10: Hybrid, but loses on guide-dominant Q2 | 12: matches Q5 Hybrid | 6: directory card vs solution/explainer | 3: empty template vs docs SERP |
| Content Depth (15) | 10: 1,583 words, How it works + FAQ | 10: 1,516 words; no definitional or comparison block | 7: 10 data streams listed, no Hapi solution narrative | 1: data streams, "why", and related all empty |
| UX Signals (15) | 10: single vague CTA "Let's connect"; no developer-portal or sandbox CTA in hero | 10: same CTA pattern | 6: no title, so the SERP snippet is auto-generated; "About the / Tech Vendor" heading split | 3: page visibly unfinished |
| Schema (15) | 7: FAQPage only; no Organization / SoftwareApplication | 7: FAQPage only | 0: none | 0: none |
| Media (15) | 9: imagery and video present (5 embeds), no architecture diagram for "connect, normalize, transact" | 9 | 6: logos only | 5: logos only |
| Authority (15) | 8: "Proven at Scale" section; Hyatt / IHG / Sonesta proof lives in resources, not inline | 7: new product, little proof on page | 5: Hotel X / Margaritaville / Crystalbrook / Nemacolin Salesforce cases not linked | 2: none |
| Freshness (10) | 8: 2026 copy | 9: Oct 2026 launch | 5 | 2: OPERA 5 framing on an OPERA Cloud / OHIP SERP |
| **SXO Gap Score** | **62 / 100** | **64 / 100** | **35 / 100** | **16 / 100** |

Homepage (not scored as a target page): H1 "Hospitality's Data Infrastructure", title "Hospitality's Connectivity Partner", and a meta description still on the old "data-integrations platform... Open APIs" positioning. Three different category claims sit in one SERP snippet. The page has no structured data at all (no Organization, no WebSite). Its persona tab block renders all 4 persona H3 pairs twice in the DOM.

---

## 4. Persona scoring

Personas are the three the brief specifies, each tied to SERP clusters. Scores are Relevance / Clarity / Trust / Action, 25 each.

**P1. Hotel group CIO / VP Technology.** Multi-PMS estate, M&A integration, AI-readiness mandate. *Evidence:* Q1, Q5, Q6 (ESB and acquisition snippets), lakehouse SERP.
**P2. Tech vendor partner / integrations manager.** Needs multi-PMS reach without per-PMS builds; checks API, data streams, sandbox. *Evidence:* Q2, Q4 (docs dominance), Q6 (TigerTMS, iLink).
**P3. Revenue / marketing leader.** Salesforce or CRM owner who wants real-time guest and stay data. *Evidence:* Q3 (Mews explainer, Hotel X), CDP SERP.

| Page | P1 CIO | P2 Vendor | P3 Rev/Mktg |
|---|---|---|---|
| `/product/hapi-connectivity` | 20/18/14/12 = **64** | 21/17/13/12 = **63** | 10/12/10/10 = **42** |
| `/product/hapi-data-lakehouse` | 21/17/12/12 = **62** | 15/14/10/10 = **49** | 15/13/10/10 = **48** |
| `/connections/salesforce` | 10/10/6/8 = **34** | 12/14/6/8 = **40** | 14/10/6/8 = **38** |
| `/connections/oracle-opera-v5-pms` | 6/4/3/6 = **19** | 8/4/3/6 = **21** | 3/3/3/5 = **14** |

**Recommendations, weakest persona first**

1. **P3 Revenue/marketing leader (weakest everywhere).** No page speaks in revenue language. Build `/solutions/salesforce` (or rebuild `/connections/salesforce`) with these sections: "Get OPERA, Mews, and Agilysys data into Salesforce in real time", the Hotel X before/after ("years stalled to streaming in months"), the Great Wolf "95% data refresh improvement", AppExchange badge and link, the data-stream table, and the CTA "See your PMS data in Salesforce". Link the 4 Salesforce case studies.
2. **P2 Vendor on connection pages.** Fill every `/connections/[pms]` template: a real title ("Oracle OPERA Cloud and OPERA 5 Integration via OHIP | Hapi"), meta description, populated data streams (read / write / webhook), "How to connect" steps (credentials, OHIP approval, time-to-live), a sandbox PMS link (`/resources/new-hapi-sandbox-pms-makes-integration-testing-a-joy` already exists), and a developer-portal CTA (`developers.hapicloud.io`). Hide or suppress any section that renders "No items found".
3. **P1 CIO trust.** Put named enterprise proof above the fold on Connectivity and Lakehouse (Hyatt mobile key, IHG checkout across 3,600 hotels, Sonesta). Add the connected-hotel count (third-party press cites 14,000-15,000+) and the connection count (100+). Add an "M&A / multi-PMS" section, which is the CIO scenario the Q6 SERP surfaces.

---

## 5. Findings by severity

### CRITICAL

**C1. Connection detail pages ship with an empty `<title>` and no meta description.**
Evidence: raw HTML `<title></title>` (empty) with no meta description on `/connections/oracle-opera-v5-pms`, `/connections/salesforce`, `/connections/mews`, `/connections/agilysys`, `/connections/infor`. That is 5 of 5 sampled pages that loaded; the others timed out. The sitemap lists about 57 `/connections/*` URLs. These are the site's only pages matching "[PMS/system] integration" long-tail intent. Google will auto-generate titles from H1s like "Mews" or "Salesforce", which have no "integration" modifier.

**C2. Flagship OPERA page is an empty template.**
Evidence: `/connections/oracle-opera-v5-pms` shows "Data Streams: No items found", an empty "Why they chose Hapi", and "Related Products: No items found". `/connections/mews` and `/connections/agilysys` also show "Data Streams: No items found". The OPERA copy covers legacy OPERA 5, while the Q4 SERP is 70% OPERA Cloud / OHIP setup docs. OPERA is the most-searched PMS integration, and Hapi has dedicated press on it (`/resources/contactless-demand-drives-new-hapi-opera-ows-integration`).

### HIGH

**H1. Owned pages absent from all 6 SERPs; press releases rank instead.**
Evidence: Hapi appears in Q1, Q3, Q5 and the lakehouse query only through hospitalitynet, hotel-online, hoteltechreport, traveldailynews and lodgingmagazine syndications. No stayhapi.com URL appeared in any result set, including a `site:` probe. Fix: every press release should link to the matching product or connection page with descriptive anchor text, so third-party authority flows to owned pages (verify whether current syndications link at all).

**H2. Guide-dominant SERPs (Q2, Q6) get product pages.**
Evidence: Q2 is ~60-70% blog/guide (Stayntouch, Cloudbeds, altexsoft) and Q6 is ~55% thought leadership. Hapi's matching assets (`/resources/the-2026-pms-api-study`, `/resources/beyond-the-pms-debate...`, `/resources/integration-layer-strategy...`) are not built as ranking guides. Build "Hotel PMS API Integration: 2026 Guide (OPERA/OHIP, Mews, Stayntouch, Agilysys, Infor)" from the PMS API study data, and link down to each `/connections/*` page.

**H3. `/connections/salesforce` is a directory card, not a Salesforce solution page.**
Evidence: the opening copy is Salesforce's own tagline ("The #1 AI CRM..."). There is no mention of Hapi's AppExchange app and no links to the 4 Salesforce customer stories in `/resources/`. Meanwhile Mews owns the PMS-to-CRM explainer slot in Q3.

**H4. Category and product-name fragmentation.**
Evidence: the homepage title says "Connectivity Partner", the H1 says "Data Infrastructure", and the meta says "data-integrations platform". `/product-overview` still sells Hapi Data Streams, Finders, Guest CRM and Data Services next to Connectivity, Autopilot, Guest Identity and Lakehouse. HTR comparison pages say "Hapi Guest" and "Hapi for Salesforce". `/product-overview` and `/product/hapi-connectivity` compete for "data integration platform". Pick one category term for the homepage and Connectivity page. Consolidate `/product-overview` (301 or rewrite) and update the HTR profile.

### MEDIUM

**M1. No structured data on homepage, hub, or connection pages.** FAQPage exists only on Connectivity and Lakehouse. Add Organization (homepage), SoftwareApplication (product pages), ItemList (`/connections`), and BreadcrumbList. Use `/seo schema` to generate them.

**M2. `/connections` hub is titled "PMS middleware" but built as a logo grid.** 819 words, H1 "Hapi Connections", detected date 2015, and 24 detail links in the rendered DOM against about 57 in the sitemap. Add a 300-500 word "PMS middleware for hotels and vendors" intro, category filters (PMS / CRM / POS / Payments) that render as crawlable links, and the partner threshold (50+ properties).

**M3. CTAs are generic and single-path.** Every page uses "Let's connect" / "Contact Us". Vendors (P2) need "Explore the API" / "Try the sandbox PMS" in the hero, and CIOs need "Talk to an architect". The developer portal link exists but sits at the bottom of connection pages.

**M4. No owned comparison/alternatives content.** HTR owns "Hapi vs Ireckonu" in 9 languages. Consider a single "Integration layer vs CDP vs PMS marketplace" page (Hapi vs Ireckonu vs TigerTMS vs OHIP-direct). Only compare against larger or adjacent players.

### LOW

**L1. Data Lakehouse page is well aligned.** Title carries "Hospitality Data Platform", the page is Hybrid with FAQ, and it is fresh. Add a definitional "What is a hospitality data platform" block and pull in the existing lakehouse-vs-CDP article to compete with the Q5 explainers.

**L2. Repeated persona tab content in the homepage DOM.** H3 pairs render twice, which is minor duplication.

**L3. Connection-page heading bug.** "About the" and "Tech Vendor" render as 2 separate H2s on every connection page, a template issue.

---

## 6. Limitations

- **SERPs came from WebSearch, not a live Google results page.** Positions, ads, PAA boxes, AI Overviews and featured snippets could not be observed. Page-type mix and "Hapi absent" are directional. Confirm with Search Console query data (impressions by page) before prioritizing.
- **Site reachability.** About 40% of fetch attempts to stayhapi.com timed out (connect timeout) or were refused (WebFetch: ECONNREFUSED), from 2 separate tools. `/who-we-serve/technology-providers`, `/product/hapi-guest-identity`, `/connections/oracle`, `/connections/stayntouch`, `/connections/shiji` and `/connections/sevenrooms-2` were never retrieved, so they are not scored. This may be a WAF or rate limit (Webflow-hosted) rather than an outage. Worth checking in GSC Crawl Stats in case Googlebot sees the same behavior.
- **`/product-overview` rendered DOM was nearly empty (39 chars).** It was analyzed from raw HTML.
- Not assessed: Core Web Vitals, backlink profile, gated asset content (PMS API study, survey), analytics or conversion data, and international or localized SERPs.

## Cross-skill follow-ups

- `/seo schema`: Organization, SoftwareApplication, ItemList, and Breadcrumb for the templates
- `/seo page`: run on the `/connections/*` CMS template (title and meta bindings, empty-state suppression)
- `/seo content`: E-E-A-T and depth pass on the PMS API study before converting it to a ranking guide

Generate a PDF report? Use `/seo google report`.

---

## Sources (SERP evidence)

- [hospitalitynet: Next Generation of Hapi](https://www.hospitalitynet.org/news/4117274.html), [hotel-online](https://www.hotel-online.com/news/next-generation-of-hapi-solves-for-hotel-data-integrations-at-scale), [hoteltechreport](https://hoteltechreport.com/news/next-generation-of-hapi-data-integrations)
- [integrate.io hospitality listicle](https://www.integrate.io/blog/data-integration-platform-hospitality/), [Airbyte hospitality](https://airbyte.com/industries/hotels-restaurants-leisure), [Oracle OHIP](https://www.oracle.com/sg/hospitality/integration-platform/), [iReckonu Integration Hub](https://ireckonu.com/middleware/integration-hub/), [Revinate GDP](https://www.revinate.com/de/the-guest-data-platform-built-for-hoteliers)
- [roommaster PMS integration](https://www.roommaster.com/blog/hotel-pms-integration), [Cloudbeds PMS integrations](https://www.cloudbeds.com/articles/pms-integrations/), [altexsoft Opera integration](https://www.altexsoft.com/blog/opera-pms-integration), [Stayntouch PMS open API guide](https://www.stayntouch.com/articles/?p=215), [callsphere PMS API](https://callsphere.ai/blog/hotel-pms-api-integration-opera-mews-cloudbeds)
- [Mews: why connect PMS and CRM](https://mews.com/en/blog/why-every-hotel-should-connect-their-pms-and-crm), [Mews for Salesforce](https://www.mews.com/en/press/mews-announces-mews-for-salesforce-on-salesforce-appexchange-the-worlds-leading-enterprise-cloud-marketplace), [Hotel X / Hapi](https://www.hospitalitynet.org/news/4121397/hotel-x-supercharges-marketing-with-automation-and-dynamic-content), [Maestro + Hapi](https://www.hotel-online.com/news/maestro-pms-and-hapi-streamline-salesforce-connectivity-for-margaritaville-hotel), [HTR Hapi for Salesforce](https://hoteltechreport.com/marketing/hotel-crm/hapi-for-salesforce)
- [TripAround OPERA Cloud](https://help.triparound.com/en/articles/15421196-how-the-pms-integration-with-opera-cloud-works), [Vouch OHIP](https://ava-docs.vouchconcierge.com/settings/essentials/pms-integration-opera), [Trybe OHIP](https://help.try.be/en/articles/360486-opera-ohip-integration), [Conduit OPERA Cloud](https://docs.conduit.ai/setting-up-conduit/connect-pms/opera-cloud), [Oracle OHIP + OIC](https://www.oracle.com/hospitality/integration-platform/ohip-and-oracle-integration-cloud-hospitality/)
- [hospitalitynet Data platform 101](https://www.hospitalitynet.org/explainer/4114045.html), [phocuswire](https://www.phocuswire.com/Understanding-hospitality-data-platforms), [Revinate CDP](https://www.revinate.com/customer-data-platform/), [snapshot.travel](https://www.snapshot.travel), [traveldailynews Hapi launch](https://www.traveldailynews.com/hotels-lodging/the-hospitality-industry-becomes-a-hapi-er-place-with-the-launch-of-hapis-integrated-data-platform/)
- [TigerTMS](https://tigertms.com/?p=9727), [hospitalitynet integration hubs panel](https://www.hospitalitynet.org/panel/information-technology/can-integration-hubs-save-the-day), [Hospitality Upgrade](https://hospitalityupgrade.com/techTalk/June-2022/Definitely-Doug-6-3-22), [Hotels mag middleware](https://hotelsmag.com/news/middleware-software-isnt-the-sexiest-tech-but-it-plays-a-pivotal-role-bridging-gaps-between-product-services-that-allows-hotels-to-run-effectively/)
- [HTR Hapi Guest vs Ireckonu](https://hoteltechreport.com/compare/hapi-for-salesforce-vs-ireckonu), [hospitalitynet Hapi growth](https://www.hospitalitynet.org/news/4127691.html), [lodgingmagazine lakehouse launch](https://lodgingmagazine.com/hapi-debuts-two-solutions-designed-to-connect-guest-data-across-systems/)

---

## Structured findings (audit-data.json, Search Experience category)

```json
{
  "category": "Search Experience",
  "sxo_gap_scores": {
    "/product/hapi-connectivity": 62,
    "/product/hapi-data-lakehouse": 64,
    "/connections/salesforce": 35,
    "/connections/oracle-opera-v5-pms": 16
  },
  "findings": [
    {"id": "C1", "severity": "critical", "title": "Connection pages have empty <title> and no meta description", "evidence": "5/5 sampled /connections/* pages: <title></title>, no meta description; ~57 such URLs in sitemap"},
    {"id": "C2", "severity": "critical", "title": "OPERA connection page is an empty template on an OHIP-docs SERP", "evidence": "Data Streams 'No items found', 'Why they chose Hapi' empty, OPERA 5 framing; Mews/Agilysys also empty data streams"},
    {"id": "H1", "severity": "high", "title": "Owned pages absent from all 6 SERPs; syndicated press ranks instead", "evidence": "hospitalitynet/hotel-online/HTR/traveldailynews/lodgingmagazine results only"},
    {"id": "H2", "severity": "high", "title": "Guide-dominant SERPs served by product pages", "evidence": "PMS integration SERP ~60-70% guides; middleware SERP ~55% thought leadership"},
    {"id": "H3", "severity": "high", "title": "/connections/salesforce is a directory card, not a solution page", "evidence": "Salesforce boilerplate copy, no AppExchange or case-study links; Mews owns explainer slot"},
    {"id": "H4", "severity": "high", "title": "Category and product-name fragmentation / cannibalization", "evidence": "Home title/H1/meta make 3 different claims; /product-overview mixes legacy and new products; HTR uses 'Hapi Guest'"},
    {"id": "M1", "severity": "medium", "title": "No structured data outside FAQPage on 2 product pages"},
    {"id": "M2", "severity": "medium", "title": "/connections hub titled 'PMS middleware' but is a thin logo grid", "evidence": "819 words, 24 rendered links vs ~57 sitemap"},
    {"id": "M3", "severity": "medium", "title": "Generic single-path CTAs; no developer/sandbox CTA for vendors"},
    {"id": "M4", "severity": "medium", "title": "No owned comparison content; HTR owns 'Hapi vs' queries"},
    {"id": "L1", "severity": "low", "title": "Data Lakehouse page aligned; add definitional + comparison depth"},
    {"id": "L2", "severity": "low", "title": "Duplicate persona tab content in homepage DOM"},
    {"id": "L3", "severity": "low", "title": "Connection template splits 'About the / Tech Vendor' into two H2s"}
  ]
}
```
