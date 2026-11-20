# stayhapi.com: Content Quality and E-E-A-T Audit

**Date:** 2026-11-17
**Method:** Raw curl fetch of 244 of the 246 sitemap URLs. `/connections/mews` and `/connections/micrometrics` timed out on every attempt, most likely because our client was being throttled, so they were not assessed. Text, title, meta, headings and JSON-LD were parsed from the HTML. Word counts are main-content counts with nav, footer and form chrome removed. Resource body counts subtract a measured ~237-word template block (related posts plus forms), so they are approximate (±15 words). Metadata templating was checked with `metadata_template.py` on the 86 URLs that have both a title and a description.
**Scope:** all 166 /resources/* pages were parsed, and 16 were read in full; 55 /connections/* pages; the homepage; all /product/*; all /who-we-serve/*; /product-overview, /our-story, /connections, /resources, /hub/*, and /future-of-hotel-data-survey-2026.

## Scores

| Score | Value |
|---|---|
| **Content Quality** | **58 / 100** |
| **On-Page SEO** | **36 / 100** |
| AI Citation Readiness | 52 / 100 |
| E-E-A-T composite (internal weights) | 67 / 100 |

### E-E-A-T breakdown

| Factor (weight) | Score | Basis |
|---|---|---|
| Experience (20%) | 72 | IHG case study gives real numbers (3,600+ hotels live since Jan 2024; digital checkout success 90% → 97%). Product copy has operator-level detail ("One check-out on our side is roughly seven calls inside the source system"). Named customer quotes on the homepage. Weak spots: 4 of the 5 customer stories have no title/meta, and the "Why they chose Hapi" block is empty on all 55 connection pages. |
| Expertise (25%) | 62 | Our Story has substantive leadership bios (Amadeus, Newmarket, Hyatt, TravelClick, Accor). But 47 resources show no byline, 36 are credited to "Hapi", 1 to "Author 1", and 4 to "Guides". 2026 thought leadership is mostly bylined "Hapi" (the 3 newest blogs by Hapi are all unattributed). There are no author pages or bios on articles, and no Person schema. |
| Authoritativeness (25%) | 75 | Named testimonials from the IHG VP of Connected Property Platforms, the Nemacolin COO, and the former Sonesta CIO. Awards (HT Visionary 2024, HotelTechReport). Founder in the hospitality tech hall of fame. AHLA / HTNG roles. Real coverage from Hotel Business and others. |
| Trustworthiness (30%) | 60 | Legal entity is stated ("Data Travel, LLC (Hapi)"). Privacy, terms, SLO, and status pages exist. Claims are consistent: 15,000 hotels appears on home, product, and Tech Providers pages. Trust is dragged down by about 18 published empty pages, near-duplicate posts, a republished third-party article, "Originally published on" labels that never name a source, and a placeholder byline. |

## Findings

### Critical

**C1. Missing `<title>` and meta description on 60% of crawled URLs, including the best proof assets.**
- `/resources/*`: 103 of 166 have an empty `<title></title>`, `meta description` with `content=""`, and an empty `og:title`. Only the self-canonical is populated.
- `/connections/*`: 43 of 55 are empty, including both Oracle OPERA pages and OpenTable.
- The affected pages include the flagship customer stories and the newest bylined thought leadership:
  - https://www.stayhapi.com/resources/how-ihg-turned-checkout-into-a-smooth-contactless-moment-across-3-600-hotels
  - https://www.stayhapi.com/resources/how-nemacolin-unified-guest-data-to-deliver-truly-personalized-luxury-experiences
  - https://www.stayhapi.com/resources/the-integration-layer-is-your-hedge-against-an-unpredictable-future (CEO byline, 2026-10-16)
  - https://www.stayhapi.com/connections/oracle and https://www.stayhapi.com/connections/oracle-opera-v5-pms
- Fix: Webflow CMS SEO fields are bound to collection fields that are blank on these items. Bind the title to `{Name} | Hapi` and the description to the summary/excerpt field as a fallback, then hand-write titles for the customer stories first.

**C2. About 18 published resource pages have no body at all (empty rich-text field, `w-dyn-bind-empty`).**
Each is just an H1 and a date, with "Originally published on" followed by nothing. Most are "In The News" items whose external link was never filled in. Examples:
- https://www.stayhapi.com/resources/the-2026-pms-api-study (2026-10-01)
- https://www.stayhapi.com/resources/ai-ready-hospitality-data-framework
- https://www.stayhapi.com/resources/ai-orchestration-framework-for-hospitality
- https://www.stayhapi.com/resources/why-decision-velocity-is-the-only-metric-that-matters-in-the-ai-era
- https://www.stayhapi.com/resources/the-most-powerful-builders-in-travel-ezn10
- https://www.stayhapi.com/resources/what-hitec-2026-revealed-about-the-future-of-hotel-technology
- https://www.stayhapi.com/resources/why-guest-data-still-fails-at-the-moment-it-matters-most
- https://www.stayhapi.com/resources/hapi-ceo-shares-how-hotels-can-go-from-ai-ready-to-ai-enabled
- https://www.stayhapi.com/resources/top-floor-podcast---250-hitec-san-antonio-part-1
- https://www.stayhapi.com/resources/connecting-data-to-elevate-guest-experiences-with-jeff-bzdawka
- https://www.stayhapi.com/resources/direction-for-the-revolution-industry-groups-exchange-ideas-on-the-intelligent-use-of-ai-in-hospitality
- https://www.stayhapi.com/resources/hapi-and-revinate-report-finds-trends-in-how-hoteliers-manage-data
- Gated asset stubs with 4 to 41 words: /resources/the-future-of-hotel-data, /the-future-of-hotel-data-webinar, /recognition-over-rewards, /seven-best-practices-of-award-winning-hospitality-brands, /loyalty-program-readiness-quiz, /hapi-perspectives

13 of the 39 resources dated 2026 are in this empty bucket, which inflates the apparent 2026 output. "The 2026 PMS API study" is exactly the kind of original-research asset that earns citations, and it is published as a blank page.
- Fix: add a 150 to 300 word summary plus the outbound link to every In The News item, or set them to noindex. Give gated assets real landing copy covering what's inside, 3 to 5 key findings, and who it's for.

### High

**H1. Near-duplicate resource pairs, each self-canonical.** Word-sequence similarity measured on main text:
- 0.99: /resources/unlocking-the-data-behind-ihgs-cutting-edge-loyalty-functionality vs `...-b8a3c`
- 0.98: /resources/hapi-ceo-luis-segredo-named-chair-of-the-2025-ahla-global-technology-100 vs `...---also-cover-on-website`. A CMS working slug leaked into production.
- 0.97: /resources/hospitality-crm-a-hoteliers-guide-to-learning-salesforce vs `...-65f94`
- 0.84: /resources/hapi-and-nemacolin-resort-win-the-prestigious-2024-hospitality-technology-visionary-partnership-award vs `...-298fa`
- 0.79: /resources/hapi-and-revinate-team-up-to-enable-hoteliers-to-drive-direct-bookings-quickly-and-at-scale vs `...-a2506`
- The Revinate partnership also exists a third and fourth time (/hapi-and-revinate-partner, /hapi-partners-with-revinate-to-boost-hoteliers-direct-booking-capabilities). Two pairs share identical titles.
- Fix: 301 the suffixed duplicates to the originals.

**H2. Republished third-party content with no source named.** The "Originally published on" field is empty on every page checked. Examples:
- https://www.stayhapi.com/resources/8-best-crm-software-for-hotels-in-2025 republishes a Fit Small Business listicle ("We evaluated dozens of hospitality CRM systems...").
- https://www.stayhapi.com/resources/the-integration-layer-is-your-hedge-against-an-unpredictable-future is the full CEO byline from Hotel Business, republished with a self-canonical and no visible source.
- Fix: name the source with a link. Then either point `rel=canonical` to the original or replace the copy with an excerpt plus Hapi commentary.

**H3. The /connections/* marketplace is thin templated pages.** Across 55 pages:
- Unique content is a vendor blurb, median 62 words (range 26 to 119), often the vendor's own marketing copy. Example: /connections/salesforce opens with "The #1 AI CRM—where humans with agents drive customer success...".
- "Data Streams: No items found." appears on 36 of 55.
- "Why they chose Hapi" is empty on 55 of 55.
- An unfilled literal "Caption" placeholder appears on 55 of 55.
- Every page uses the same H2 skeleton ("About the" / "Tech Vendor" / "Data Streams").
- Examples: https://www.stayhapi.com/connections/kipsu, https://www.stayhapi.com/connections/aws, https://www.stayhapi.com/connections/oracle-opera-v5-pms
- These are exactly the pages that should rank for "[vendor] integration" and "[PMS] API" queries. Fix by priority: (1) fill data streams and the direction of data flow (read/write) for each connection, (2) add one concrete use case or customer per connection, (3) noindex the shells that can't be filled. See `seo-programmatic` for the template standard.
- Slug hygiene: /connections/sevenrooms-2 and /connections/shiji-2 are different products (SevenRooms Surveys, Shiji Infrasys POS) but carry numeric-suffix slugs.

**H4. Author attribution is weak on the content that matters most.**
- No byline: 47 resources. "Hapi": 36. "Author 1": 1 (https://www.stayhapi.com/resources/building-the-ultimate-guest-journey-how-rocco-forte-hotels-connects-data-across-properties-to-gain-insight). "Guides": 4.
- The newest posts are bylined "Hapi": /why-cant-i-just-build-this-with-ai-what-hotel-brands-need-to-know (2026-11-04), /data-lakehouse-vs-cdp-whats-the-difference-for-hotel-groups, /guest-identity-vs-crm-whats-the-difference.
- There are no author pages, no bios on articles, and no Article/BlogPosting or Person JSON-LD on any of the 166 resources (0 found).
- The leadership team has real credentials on /our-story, but none of that is connected to the articles.

**H5. Positioning and keyword targeting are not stated consistently.** The core query family (hotel data integration, PMS integration, hospitality API) is spread across five different self-descriptions:
- Home title: "Hospitality's Connectivity Partner"
- Home H1: "Hospitality's Data Infrastructure"
- Home description: "data-integrations platform that effectively improves the process of extracting, cleaning and normalizing data for a number of hospitality technology stakeholders through Open APIs". At 225 characters it is legacy copy and gets truncated.
- /product-overview title (109 chars): "Cloud Data Hub" / "Data-integration platform"
- /connections title: "PMS middleware"

The homepage title and H1 never use "hotel", "PMS", or "integration". The /product/* and /who-we-serve/* pages are tighter and more specific (for example "Hapi Connectivity | One Integration, Every System"), but /product-overview still carries the older positioning.
- Fix: choose one category term (for example "hotel data integration platform") and use it in the home title, H1, and meta, and in /product-overview.

### Medium

**M1. Template heading defects on every resource.**
- 164 of 166 resources render a second, empty `<h1>` (a hidden customer-story block); 2 render three H1s.
- 153 contain an empty or zero-width-joiner `<h2>` (`&zwj;`).
- Example: https://www.stayhapi.com/resources/hapiness

**M2. Every image on every page has an empty alt.**
- The homepage has 200 `<img>` tags, all with `alt=""`, including the customer and partner logo rail and the testimonial headshots.
- Customer logos are trust proof that search engines and AI systems currently can't read.
- The same pattern holds on all 244 pages crawled.

**M3. Publishing cadence is uneven, and real output is lower than the dated count suggests.**
- Dated items per year: 2019: 6, 2020: 10, 2021: 15, 2022: 11, 2023: 14, 2024: 9, 2025: 33, 2026: 39 (through 2026-11-04).
- Substantive (≥300 body words): 2025: 25; 2026: 25.
- There were no posts in April 2026, and 29 resources have no date at all, mostly customer stories and press releases (for example /how-langham-uses-data-to-provide-unmatched-luxury and /jeff-bzdawka-joins-hapi-as-president).
- No "updated" dates appear anywhere.
- Of the 166 resources, 11 are "people spotlight" posts and a large share are press releases: low search value, and they dilute the hub.

**M4. Missing meta descriptions or titles on key non-resource pages.**
- /future-of-hotel-data-survey-2026: no description.
- /hub/hospitality-loyalty-guest-recognition-hub: no description. The hub page itself is a good topical cluster, but it links mostly to the gated stubs in C2.
- /our-story: title is just "Our Story" (9 chars, no brand).
- 27 descriptions run over 160 characters, and 26 titles run over 60 characters.

**M5. Readability skews dense on press releases and case studies.**
Sampled bodies, scored on Flesch Reading Ease (FRE) and Flesch-Kincaid Grade Level (FKGL):
- Blogs: FRE 41 to 55 (FKGL 10 to 13). Fine for a B2B tech buyer.
- Press releases and case studies: FRE 19 to 22 (FKGL 16.6 to 18.5) with average sentence length 26 to 31 words. Examples: the IHG story and /hapi-eliminates-the-guesswork-by-connecting-guest-identity-across-hotel-systems.

### Low

**L1. Placeholder template copy in the DOM on every page.** A hidden mobile "Segments" dropdown contains "Bibendum amet at molestie mattis." three times, with `href="#"` links. It is not visible (class `none`), but crawlers and LLM scrapers read it.

**L2. Leaked CMS working slug.** `...---also-cover-on-website` (see H1).

**L3. Empty structured data on the site's strongest asset.** JSON-LD exists only as FAQPage on the 5 /product/* pages. The homepage, Who We Serve, Our Story, and Resources pages have no Organization, Article, or Person schema. See schema.md for detail.

## What is working (verified)

- **/product/* pages** (1,170 to 1,680 words each) are specific, differentiated, and quotable.
  - Concrete mechanics: "Retrieve, post, validate, update", "Ten hospitality data types", "nine years of per-system mapping work", no per-property charge.
  - Neutrality positioning: "Hapi does not sell a property management system...".
  - FAQPage schema on each.
- **Recent comparison posts use answer-first structure,** which is good for AI citation. For example /resources/data-lakehouse-vs-cdp-whats-the-difference-for-hotel-groups opens with "Quick answer: A CDP organizes data for marketing activation... A data lakehouse stores and normalizes the raw data underneath...".
- **/resources/why-cant-i-just-build-this-with-ai-what-hotel-brands-need-to-know** (1,266 words) is a strong objection-handling piece aimed at the real 2026 buyer question.
- **The IHG customer story has hard outcomes,** which makes it the single best citation asset on the site once it has a title.
- **Homepage social proof is named and specific:** IHG, Nemacolin, Sonesta, Kipsu, and HotelKey, each with name and title.
- **Templated metadata check:** `site_risk: low`, `templated_ratio: 0.0`, no `shared_cta_phrases` across the 86 pages that have both fields. Where metadata exists it is hand-written. The problem is absence, not templating.

## Prioritized fixes

1. Fill titles and descriptions on the 146 resource and connection items. Bind CMS fallbacks first, then hand-write the 5 customer stories and the top 10 connections (C1).
2. Add body copy and source links to the about 18 empty pages, or noindex them (C2).
3. 301 the 5 duplicate pairs and fill in the "Originally published on" source everywhere (H1, H2).
4. Rebuild the connection template: data streams, read/write direction, one use case per connection, and remove the "Caption" placeholder (H3).
5. Add real bylines, author bio blocks, and Article + Person schema, and replace "Hapi" and "Author 1" (H4).
6. Align the home title, H1, and meta to one category term (H5).

## Structured findings (audit-data.json, Content Quality category)

```json
{
  "category": "Content Quality",
  "scores": {"content_quality": 58, "on_page_seo": 36, "ai_citation_readiness": 52,
             "eeat": {"experience": 72, "expertise": 62, "authoritativeness": 75, "trustworthiness": 60, "composite": 67}},
  "findings": [
    {"id": "C1", "severity": "critical", "title": "Empty <title>/meta description on 103/166 resources and 43/55 connections", "evidence": ["https://www.stayhapi.com/resources/how-ihg-turned-checkout-into-a-smooth-contactless-moment-across-3-600-hotels", "https://www.stayhapi.com/connections/oracle"]},
    {"id": "C2", "severity": "critical", "title": "~18 indexable resources with empty body", "evidence": ["https://www.stayhapi.com/resources/the-2026-pms-api-study", "https://www.stayhapi.com/resources/ai-ready-hospitality-data-framework"]},
    {"id": "H1", "severity": "high", "title": "5 near-duplicate resource pairs, self-canonical", "evidence": ["https://www.stayhapi.com/resources/unlocking-the-data-behind-ihgs-cutting-edge-loyalty-functionality-b8a3c"]},
    {"id": "H2", "severity": "high", "title": "Republished third-party articles with empty source attribution", "evidence": ["https://www.stayhapi.com/resources/8-best-crm-software-for-hotels-in-2025"]},
    {"id": "H3", "severity": "high", "title": "Thin templated connection pages (median 62 unique words; 36/55 empty data streams)", "evidence": ["https://www.stayhapi.com/connections/kipsu"]},
    {"id": "H4", "severity": "high", "title": "Weak bylines ('Hapi', 'Author 1', none), no Article/Person schema", "evidence": ["https://www.stayhapi.com/resources/building-the-ultimate-guest-journey-how-rocco-forte-hotels-connects-data-across-properties-to-gain-insight"]},
    {"id": "H5", "severity": "high", "title": "Inconsistent category term across home/product-overview/connections titles", "evidence": ["https://www.stayhapi.com", "https://www.stayhapi.com/product-overview"]},
    {"id": "M1", "severity": "medium", "title": "Second empty H1 on 164/166 resources; empty H2 on 153", "evidence": ["https://www.stayhapi.com/resources/hapiness"]},
    {"id": "M2", "severity": "medium", "title": "All images alt=\"\" incl. customer logos", "evidence": ["https://www.stayhapi.com"]},
    {"id": "M3", "severity": "medium", "title": "Uneven cadence; 29 undated resources; 13/39 2026 items empty", "evidence": ["https://www.stayhapi.com/resources"]},
    {"id": "M4", "severity": "medium", "title": "Missing descriptions on survey + hub; 'Our Story' title", "evidence": ["https://www.stayhapi.com/future-of-hotel-data-survey-2026"]},
    {"id": "M5", "severity": "medium", "title": "Dense readability on press releases/case studies (FKGL 16-18)", "evidence": ["https://www.stayhapi.com/resources/hapi-eliminates-the-guesswork-by-connecting-guest-identity-across-hotel-systems"]},
    {"id": "L1", "severity": "low", "title": "Hidden lorem-ipsum nav placeholder on every page", "evidence": ["https://www.stayhapi.com"]},
    {"id": "L3", "severity": "low", "title": "No Organization/Article schema outside product FAQPage", "evidence": ["https://www.stayhapi.com"]}
  ],
  "metadata_template": {"site_risk": "low", "templated_ratio": 0.0, "shared_cta_phrases": {}, "pages_checked": 86},
  "not_assessed": ["https://www.stayhapi.com/connections/mews", "https://www.stayhapi.com/connections/micrometrics"]
}
```
