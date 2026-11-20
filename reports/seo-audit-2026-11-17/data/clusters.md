# Hapi (stayhapi.com): Content Architecture and Topic Cluster Plan

**Date:** 2026-11-17
**Scope:** 167 `/resources/*` URLs, 58 `/connections/*` URLs, 1 existing `/hub/*` page
**Method:** We crawled all 225 URLs with curl. 144 of 167 resource pages and 43 of 58 connection pages parsed cleanly. The server throttled the rest at a 7 to 90 second response time, so we classified those from the `/resources` listing labels and their slugs. We ran 16 SERP pulls covering the four seeds plus 12 expansion keywords. Overlap is the number of exact URLs shared in the returned top results.

---

## 1. Executive read

1. **stayhapi.com does not rank on its own domain for any of the four seed terms.** Where Hapi appears, it is through syndicated copies of its press and opinion pieces on hospitalitynet.org, hotel-online.com, hoteltechreport.com, traveldailynews.com and lodgingmagazine.com.
   - Hapi's own "Exploring MDM vs. CDP in Hospitality" ranks #1 to #3 for "hotel MDM vs CDP", but only as the syndicated copies. The original on stayhapi.com (2022, no title tag) does not appear.
   - The same is true for "Salesforce for hotels PMS integration": 9 of the top 20 results are Hapi press syndications, and none are stayhapi.com.
   - The authority is being earned, then routed to other domains.
2. **The resources library is mostly a newsroom.** About 47% is company news, people, awards and press. About 25% is integration, connectivity or API content, about 20% is guest data, CDP and CRM, and about 8% is AI and data readiness.
   - Only one topic hub exists: the Loyalty and Guest Recognition hub, roughly 600 words linking to 4 assets.
3. **Technical floor problems block any cluster from working.**
   - 90 of 144 parsed resource pages ship an empty `<title></title>` and no meta description.
   - 36 of 43 parsed connection pages also have an empty `<title>`.
   - 134 of 144 resource pages have **zero in-body links** to `/connections`, `/product`, `/hub` or other `/resources` pages.
   - The "Related Posts" module shows the same six recent posts on every page, so it is not topical. Internal linking is effectively flat.
   - About 12 "In The News" pages from 2026 are **empty shells**: the About, Challenge, Solution and Results headings have no text, and the "Originally published on" link goes to `#`.
   - The empty shells include `the-2026-pms-api-study`, `ai-ready-hospitality-data-framework`, `ai-orchestration-framework-for-hospitality`, `why-guest-data-still-fails-at-the-moment-it-matters-most`, `why-decision-velocity-...`, `hapi-ceo-shares-how-hotels-can-go-from-ai-ready-to-ai-enabled` and `connecting-data-to-elevate-guest-experiences-with-jeff-bzdawka`.
4. **The four seeds are four different SERPs.** They share 0 or 1 URLs with each other, so they cannot share one pillar.
   - "Hotel PMS integration" and "PMS API integration hotels" share 8 URLs, so they are the same post.
   - The right shape is **three hubs**, not one: data integration, PMS integration and API, and guest data platform. Loyalty folds into the guest data hub.
5. **Cloudbeds already runs this playbook.**
   - Its `/hotel-data-architecture/` hub ranks for "hotel data integration".
   - Its `/hotel-data-architecture/ai-readiness/` spoke ranks for "hotel data lakehouse AI ready".
   - Revinate owns "hotel guest data platform" and "hotel CDP" outright.
   - Stayntouch owns the "hotel PMS open API comparison" query that Hapi's empty 2026 PMS API study should be winning.

---

## 2. Existing /resources inventory

### 2a. By content type

These counts use the listing labels from the parsed pages, plus slug inference for the 23 pages the crawl could not fetch.

| Type | Count | Notes |
|---|---|---|
| Blog | ~68 | 11 are people spotlights. ~48 posts are dated before 2024, and most of those have no title tag. |
| Press Releases | ~47 | Includes 3 PMS-vendor "accelerates connectivity" releases and the Revinate partnership (×4, see cannibalization). |
| In The News | ~32 | ~12 from 2026 are empty shells with a dead `#` source link. |
| Customer Stories | ~13 | Full case studies of about 500 words, but no links to the connection or product pages they depend on. |
| Guides | ~5 | `recognition-over-rewards`, `the-future-of-hotel-data`, `loyalty-program-readiness-quiz` and `hapi-perspectives` have about 10 to 15 words of on-page body (gated or embed). |
| Videos | 1 | `the-future-of-hotel-data-webinar` |
| Unclear | 1 | `hapiness` |

### 2b. By topic

These are approximate assignments, and some URLs touch two topics.

| Topic | ~URLs | Strongest existing assets |
|---|---|---|
| **T1 Integration, connectivity, PMS, APIs** | ~35 | `beyond-the-pms-debate-...` (2026), `integration-layer-strategy-the-real-barrier-to-hotel-innovation`, `the-integration-layer-is-your-hedge-...`, `embracing-the-multi-pms-era-...` (2023), `why-custom-integrations-are-hurting-your-product-roadmap...`, `how-fragmented-hotel-tech-is-affecting-operations...` (1,226 words), `pms-the-heart-of-the-hospitality-operating-environment`, `all-about-apis-the-future-of-integrated-technology-f0e57` (2021), `new-hapi-sandbox-pms-makes-integration-testing-a-joy`, `contactless-demand-drives-new-hapi-opera-ows-integration`, `hapi-integration-platform-is-now-available-on-oracle-cloud-marketplace`, `next-generation-of-hapi-solves-for-hotel-data-integrations-at-scale`, `realtimedatastream`, `the-real-time-data-problem-in-hospitality...`, `hotel-m-a-navigating-technical-hurdles...`, plus the operto, realtime-reservation and urvenue PMS-connectivity releases |
| **T2 Guest data, CDP, CRM, Salesforce** | ~35 | `guest-identity-vs-crm-whats-the-difference` (2026), `data-lakehouse-vs-cdp-whats-the-difference-for-hotel-groups` (2026), `exploring-mdm-vs-cdp-in-hospitality` (2022, ranks only via syndication), `how-a-cdp-will-shape-the-future-of-hotel-marketing`, `4-tips-for-choosing-a-solution-to-optimize-your-guest-data`, `breaking-down-data-silos-in-hospitality-the-case-for-a-unified-data-layer`, `hospitality-crm-a-hoteliers-guide-to-learning-salesforce` (×2), `hospitality-crm-past-present-and-future`, `why-hapi-is-essential-for-implementing-salesforce-data-cloud...`, `8-best-crm-software-for-hotels-in-2025` (167 words), `hm-exclusive-nearly-50-of-hoteliers-struggle-to-access-critical-data`, and the future-of-hotel-data set |
| **T3 AI and data readiness** | ~14 | `ai-in-hospitality-2026-why-data-has-to-come-before-the-algorithm` (1,353 words), `why-cant-i-just-build-this-with-ai...` (1,288 words), `product-or-plumbing...`, `where-are-you-on-the-ai-grid`, `we-can-lead-your-ai-to-data...`, `ai-for-hotels-how-to-use-it...`, `ai-in-hospitality-why-data-matters-more-than-ever`, `how-hotels-can-make-ai-work-for-them...`, `driving-ai-in-the-hotel-industry...`, and the empty shells `ai-ready-hospitality-data-framework` and `ai-orchestration-framework-for-hospitality` |
| **T4 Loyalty and recognition** | ~9 | Hub `/hub/hospitality-loyalty-guest-recognition-hub`, `recognition-matters-...`, `recognition-over-rewards`, `loyalty-program-readiness-quiz`, `seven-best-practices-...`, `hapi-enhances-your-hotels-loyalty-program`, `laasie-hapi-connection-powers-modern-hotel-loyalty`, `unlocking-the-data-behind-ihgs-cutting-edge-loyalty-functionality` (×2), `how-centralized-data-powers-sonestas-award-winning-loyalty-program` |
| **T5 Guest experience, payments, contactless** | ~16 | `how-modern-hotel-payment-workflows-shape-the-guest-experience` (1,652 words), `hapi-launches-new-payment-automations`, `hapi-launches-folio-finder`, `hapi-and-upgrade-partner-...flex-pay`, `how-ihg-turned-checkout-...`, `powering-mobile-key-at-scale-...hyatt`, the 2020 contactless-era posts, and the Kipsu story |
| **T6 Customer proof** (overlaps T1 to T5) | ~25 | IHG (4 URLs), Nemacolin (4), Margaritaville (4), Sonesta (2), Hyatt (2), Rocco Forte (2), Crystalbrook (2), Great Wolf, Langham, Red Lion, iVvy |
| **T7 Company, people, awards, events** | ~40 | 11 people spotlights, about 8 exec appointments, about 8 awards, about 6 HITEC and event posts, about 5 growth announcements |

### 2c. /connections inventory (58)

**Categories, inferred from slugs and vendor descriptions:**
- **PMS (~15):** agilysys, asi-pms, aven-hospitality, hotelkey, infor, maestro, mews, oracle, oracle-opera-v5-pms, resort-data-processing-pms, stayntouch, visual-matrix, shiji, shiji-2, realtime-reservation
- **CRM, CDP and marketing (~9):** salesforce, revinate, treasure-data, capillary, horizon-cdp, clairvoyix, laso, flip-to, social
- **Guest messaging and experience (~14):** kipsu, canary-technologies, duve, helloshift, guesthub, hudini-mobile-app, loungeup, alliants, operto-guest-technologies, the-guest-book, eleven-wifi, purple-wifi, upsellguru, oaky
- **F&B, spa and activities (~6):** opentable, sevenrooms, sevenrooms-2, book4time, urvenue, saba-hospitality
- **Analytics, RMS and reputation (~7):** juyo-analytics, hotel-iq-decision-cloud, micrometrics, medallia, shiji-reviewpro, revinate-surveys, opstech-pro
- **Payments and infrastructure (~5):** securepay, aws, polyapi, rest, sms, amica

**What the template looks like:**
- 190 to 460 words, mostly boilerplate.
- The "About the Tech Vendor", "A Deeper Look", "Data Streams" and "Related Products" blocks render empty ("No items found").
- No link to any resource, case study or product page.
- 36 of 43 parsed pages have an empty `<title>`.
- `sevenrooms` and `sevenrooms-2`, and `shiji` and `shiji-2`, are duplicate vendor pages that each self-canonicalize.

**What they should be:** these are the natural spokes of the PMS integration hub. As built today they are 58 thin doorway pages.

---

## 3. SERP overlap matrix

**Keywords tested:**

| ID | Keyword | Intent |
|---|---|---|
| K1 | hotel data integration | Informational |
| K2 | hotel PMS integration | Informational |
| K3 | hospitality API | Informational / Developer |
| K4 | hotel guest data platform | Commercial |
| K5 | hotel integration platform middleware | Commercial |
| K6 | hotel API integration | Commercial (OTA supply, off-intent) |
| K7 | hotel customer data platform CDP | Commercial |
| K8 | PMS API integration hotels | Informational |
| K9 | hotel data silos unified data | Informational |
| K10 | hotel guest identity resolution single guest profile | Informational |
| K11 | OPERA Cloud integration OHIP third party | Informational / Technical |
| K12 | multi-PMS hotel portfolio data integration | Informational |
| K13 | Salesforce for hotels PMS integration | Commercial |
| K14 | hotel data lakehouse AI ready data | Informational |
| K15 | best hotel CRM software 2026 | Commercial (best-of) |
| K16 | hotel MDM vs CDP guest data | Commercial (comparison) |

**Thresholds:** 7 to 10 shared URLs means the same post, 4 to 6 means the same cluster, 2 to 3 means interlink, and 0 to 1 means separate pages.

| Pair | Shared URLs | Verdict | Shared evidence |
|---|---|---|---|
| K2 to K8 | **8** | **Same post** | cloudbeds pms-integrations, revfine (×2), cloudbeds ?p=95995, priority-software, hoteza, roommaster, oxmaint |
| K2 to K12 | **5** | Same cluster | revfine (×2), servicechannel, priority-software, roommaster |
| K8 to K12 | **4** | Same cluster | revfine (×2), priority-software, roommaster |
| K3 to K5 | 2 | Interlink | oracle.com/hospitality/integration-platform (two locales) |
| K5 to K11 | 2 | Interlink | Oracle OHIP datasheet, "Changing the Game" |
| K4 to K7 | 2 (3 counting syndication) | Interlink, same hub | revinate /customer-data-platform (×2), plus the Revinate CDP guide syndicated on hospitalitynet |
| K10 to K14 | 2 | Interlink | Hapi Guest Identity launch (lodgingmagazine, hospitalitynet) |
| K9 to K10 | 1 to 2 | Interlink | hospitalitynet 4127923, 4127934 |
| K9 to K16 | 1 to 2 | Interlink | hospitalitynet 4127934, 4122491 |
| K1 to K9 | 1 | Separate | pedowitzgroup (the Hapi "breaking down silos" piece is syndicated in both under different URLs) |
| K1 to K12 | 1 | Separate | pedowitzgroup |
| K1 to K14 | 1 | Separate | cloudbeds /hotel-data-architecture/ |
| K1 to K3 | 1 | Separate | traveldailynews Hapi launch |
| K1 to K2 | 0 | Separate | none |
| K1 to K4 | 0 | Separate | none |
| K2 to K3 | 0 | Separate | none |
| K3 to K4 | 0 | Separate | none |
| K2 to K4 | 0 | Separate | none |
| K3 to K6 | 0 to 1 | Separate | Oracle in a different locale. K6 is OTA and bed-bank supply intent, so it is **excluded**. |
| K7 to K10 | 0 | Separate | Same vendors (Revinate, TrustYou), different URLs |
| K13, K15 vs all | 0 | Separate | K13 is dominated by Hapi press syndication. K15 is a listicle SERP. |

**How to read this:**
- These are fragmented, low-volume B2B SERPs. Only the PMS integration family reaches cluster-level overlap of 4 or more.
- Every other grouping below rests on interlink-level overlap of 2 to 3, plus topical and domain overlap: Revinate, TrustYou and hospitalitynet recur within a hub.
- This is a deliberate deviation from the "4 or more overlap to cluster peers" check, and it is flagged in the validation section.
- The four seeds are confirmed as separate pillars.

---

## 4. Proposed architecture: three hubs, product pages as money pages

**Rules:**
- Hubs are informational pillars at `/hub/*`, using the existing hub URL pattern.
- `/product/*` pages target the commercial "platform" terms, and every hub and spoke links to them.
- Pillars must not target the product keyword, which avoids product-versus-pillar cannibalization.

### HUB A: Hotel data integration

- **Pillar (new):** `/hub/hotel-data-integration`
- **Primary keyword:** hotel data integration
- **Template:** ultimate-guide, 3,000 to 4,000 words
- **Money page:** `/product/hapi-connectivity`, targeting "hotel integration platform"

| Cluster | Spoke URL | Status | Primary keyword | Template |
|---|---|---|---|---|
| A1 Integration layer | `/resources/integration-layer-strategy-the-real-barrier-to-hotel-innovation` | **Reuse, canonical.** Merge `the-integration-layer-is-your-hedge-...` into it with a 301. | hotel integration layer | explainer |
| A1 | **NEW** `/resources/hotel-integration-platform-vs-point-to-point` | New | hotel integration platform middleware (K5) | comparison |
| A1 | `/resources/beyond-the-pms-debate-why-connectivity-may-be-hospitalitys-biggest-innovation-challenge` | Reuse, add body links | hotel tech connectivity | explainer |
| A2 Data silos and fragmentation | `/resources/breaking-down-data-silos-in-hospitality-the-case-for-a-unified-data-layer` | **Expand** from 768 to 1,500 words. Absorbs `how-data-can-bridge-the-gap...` (301). | hotel data silos (K9) | explainer |
| A2 | `/resources/how-fragmented-hotel-tech-is-affecting-operations-and-guest-satisfaction` | Reuse | fragmented hotel tech | explainer |
| A2 | `/resources/the-real-time-data-problem-in-hospitality-and-why-it-matters` | Reuse. Absorbs `realtimedatastream` and `real-time-data-can-serve-as-a-differentiator...` (301). | real-time hotel data | explainer |
| A3 Portfolio and multi-PMS | `/resources/embracing-the-multi-pms-era-how-hapi-facilitates-seamless-data-integration-for-hotel-companies` | **Rewrite** from 696 to 1,500 words, retitle | multi-PMS hotel data integration (K12) | how-to |
| A3 | `/resources/hotel-m-a-navigating-technical-hurdles-and-driving-portfolio-growth` | Reuse | hotel M&A technology integration | how-to |
| A4 AI-ready data | **NEW, fill the empty shell** `/resources/ai-ready-hospitality-data-framework` | Publish the body | AI-ready hotel data (K14) | explainer and checklist |
| A4 | `/resources/ai-in-hospitality-2026-why-data-has-to-come-before-the-algorithm` | Reuse, canonical AI post. Absorbs `ai-in-hospitality-why-data-matters-more-than-ever`, `driving-ai-in-the-hotel-industry-the-importance-of-data` and `how-hotels-can-make-ai-work-for-them...` (301). | AI in hospitality data | explainer |
| A4 | `/resources/why-cant-i-just-build-this-with-ai-what-hotel-brands-need-to-know` | Reuse | build vs buy hotel integrations AI | explainer |

**Proof to embed in Hub A:** Sonesta (`behind-sonestas-rapid-expansion-...`), Rocco Forte, Red Lion.

### HUB B: Hotel PMS integration and APIs

- **Pillar (new):** `/hub/hotel-pms-integration`
- **Primary keyword:** hotel PMS integration. Also covers "PMS API integration", because the two share 8 URLs and must be one page.
- **Template:** ultimate-guide, 3,000 to 3,500 words
- **Directory hub:** `/connections`, upgraded with PMS, CRM, guest messaging, F&B and analytics category sections plus an intro.
- **Money pages:** `/product/hapi-connectivity` and `/who-we-serve/technology-providers`

| Cluster | Spoke URL | Status | Primary keyword | Template |
|---|---|---|---|---|
| B1 PMS APIs | **NEW, fill the empty shell** `/resources/the-2026-pms-api-study` | Publish the full study, with ungated summary findings | hotel PMS API comparison / PMS open API | explainer (data study) |
| B1 | **NEW** `/resources/opera-cloud-ohip-integration-guide` | New. Absorbs the angle of `contactless-demand-drives-new-hapi-opera-ows-integration`. | OPERA Cloud integration / OHIP (K11) | how-to |
| B1 | `/resources/pms-the-heart-of-the-hospitality-operating-environment` | Reuse, refresh | what is a hotel PMS integration | explainer |
| B2 For tech vendors | **NEW** `/resources/hospitality-api-one-integration-to-every-pms` | New | hospitality API (K3) | explainer, landing hybrid |
| B2 | `/resources/why-custom-integrations-are-hurting-your-product-roadmap---and-your-growth` | Reuse. Fix the slug's triple hyphen on refresh with a 301. | custom PMS integrations cost | explainer |
| B2 | `/resources/new-hapi-sandbox-pms-makes-integration-testing-a-joy` | **Expand** from 220 words | PMS sandbox integration testing | how-to |
| B3 Connection spokes | `/connections/oracle-opera-v5-pms`, `/connections/mews`, `/connections/infor`, `/connections/stayntouch`, `/connections/maestro`, `/connections/agilysys`, `/connections/salesforce` and the rest | **Template fix:** real title, use cases, data streams, a linked case study and a hub backlink | "[vendor] integration" | landing-page |

**Proof to embed in Hub B:** IHG checkout, Hyatt mobile key, HotelKey, and the Operto, RealTime Reservation and urVenue connectivity releases.

### HUB C: Hotel guest data platform

- **Pillar (new):** `/hub/hotel-guest-data-platform`
- **Primary keyword:** hotel guest data platform (K4) and hotel CDP (K7). They share 2 to 3 URLs, so they get one pillar with a CDP section.
- **Template:** ultimate-guide, 3,000 to 4,000 words
- **Money pages:** `/product/hapi-guest-identity` and `/product/hapi-data-lakehouse`
- **Loyalty:** the existing `/hub/hospitality-loyalty-guest-recognition-hub` becomes cluster C4 as a sub-hub. Keep the URL and add a link up to the pillar.

| Cluster | Spoke URL | Status | Primary keyword | Template |
|---|---|---|---|---|
| C1 Identity | **NEW** `/resources/hotel-guest-identity-resolution-golden-guest-record` | New | hotel guest identity resolution (K10) | explainer |
| C1 | `/resources/guest-identity-vs-crm-whats-the-difference` | **Expand** from 597 to 1,400 words | guest identity vs CRM | comparison |
| C1 | `/resources/why-guest-data-still-fails-at-the-moment-it-matters-most` | **Fill the empty shell** or 301 it to the C1 new page | guest data activation | explainer |
| C2 Architecture comparisons | `/resources/exploring-mdm-vs-cdp-in-hospitality` | **Refresh and add a title tag.** Set cross-domain canonical or "originally published" attribution on the syndications. | hotel MDM vs CDP (K16) | comparison |
| C2 | `/resources/data-lakehouse-vs-cdp-whats-the-difference-for-hotel-groups` | **Expand** from 582 to 1,400 words | hotel data lakehouse vs CDP | comparison |
| C2 | `/resources/how-a-cdp-will-shape-the-future-of-hotel-marketing` | Reuse. Absorbs `4-tips-for-choosing-a-solution-to-optimize-your-guest-data` (301). | hotel CDP marketing | explainer |
| C3 Salesforce and CRM | **NEW** `/resources/salesforce-for-hotels-pms-integration-guide` | New consolidation target. 301 `hospitality-crm-a-hoteliers-guide-to-learning-salesforce`, `-65f94`, `hapiconnectforsalesforce` and `hapis-connector-app-for-salesforce-goes-next-level` here. | Salesforce for hotels (K13) | how-to |
| C3 | `/resources/why-hapi-is-essential-for-implementing-salesforce-data-cloud-in-the-hotel-industry` | Reuse, retitle without the brand-first framing | Salesforce Data Cloud hotels | explainer |
| C3 | `/resources/8-best-crm-software-for-hotels-in-2025` | **Rebuild** from 167 words as a 2026 best-of, or 301 it to C3 | best hotel CRM software (K15) | best-of |
| C4 Loyalty (sub-hub) | `/hub/hospitality-loyalty-guest-recognition-hub` + `recognition-matters-...`, `recognition-over-rewards`, `loyalty-program-readiness-quiz`, `seven-best-practices-...`, `hapi-enhances-your-hotels-loyalty-program` | Reuse | hotel loyalty guest recognition | existing |

**Proof to embed in Hub C:** Nemacolin, Crystalbrook, Margaritaville, Great Wolf (95% data refresh improvement), Langham, Sonesta loyalty, IHG loyalty.

### Outside the hubs (leave as newsroom)

- T7 company, people, awards and event posts, about 40 URLs. Keep them, but `noindex` or consolidate the thin ones, such as people spotlights under 100 words.
- T5 payments: these form a possible future fourth hub ("hotel payment automation") once the Folio Finder and payment automation content grows beyond 4 to 5 substantive pages. Today it is 1 strong post (`how-modern-hotel-payment-workflows...`) plus press.

---

## 5. Cannibalization check

| Group | URLs | Action |
|---|---|---|
| Revinate partnership (×4) | `hapi-and-revinate-partner`, `hapi-partners-with-revinate-to-boost-hoteliers-direct-booking-capabilities`, `hapi-and-revinate-team-up-...-at-scale`, `...-at-scale-a2506` | Each self-canonicalizes, and two share the identical title "Hapi Partners with Revinate to Boost Direct Bookings". Keep one, 301 the other three, and link the survivor to `/connections/revinate`. |
| Nemacolin award (×2) | `hapi-and-nemacolin-resort-win-...-award` and `...-298fa` | 301 the `-298fa` copy. |
| IHG loyalty (×2) | `unlocking-the-data-behind-ihgs-cutting-edge-loyalty-functionality` and `...-b8a3c` | 301 the `-b8a3c` copy. |
| Salesforce CRM guide (×2) | `hospitality-crm-a-hoteliers-guide-to-learning-salesforce` and `...-65f94` (2,549 words in total HTML, retitled "How Salesforce helps hotels grow...") | Merge into the new C3 page. |
| AHLA chair (×2) | `hapi-ceo-luis-segredo-named-chair-of-the-2025-ahla-global-technology-100` and `...---also-cover-on-website` | The second slug is a CMS working note that leaked into production. 301 it. |
| Margaritaville (×2 + 2) | `margaritaville-partners-with-hapi-for-total-customer-data-strategy` and `...-2`, `maestro-pms-and-hapi-streamline-salesforce-connectivity...`, `hapi-joins-the-margaritaville-revenue-marketing-team...` | Keep the customer story as canonical and 301 `-2`. |
| Rocco Forte (×2) | `building-the-ultimate-guest-journey-how-rocco-forte-hotels-connects-data...` (blog, 2022) and `rocco-forte-building-the-ultimate-guest-journey` (story) | 301 the blog to the story. |
| Crystalbrook (×2) | `hapi-connects-sevenrooms-salesforce-to-drive-personalization-at-crystalbrook` (press) and `elevating-guest-experiences-how-crystalbrook-collection-uses-hapi...` (story) | Keep both, but the press release links to the story. Differentiate by intent. |
| Future of hotel data (×3 + survey) | `the-future-of-hotel-data`, `the-future-of-hotel-data-webinar`, `/future-of-hotel-data-survey-2026`, `hapi-and-revinate-report-finds-trends...` | Make `/future-of-hotel-data-survey-2026` the canonical research page, and link the webinar and report to it. |
| AI and data (×5) | See Hub A cluster A4 | 301 three thin 2023 to 2025 posts into the 2026 canonical. |
| Integration layer (×2) | `integration-layer-strategy-...` and `the-integration-layer-is-your-hedge-...` | Merge them (A1). |
| Sonesta (×2) | `behind-sonestas-rapid-expansion-...` and `how-centralized-data-powers-sonestas-award-winning-loyalty-program` | Differentiate: expansion goes to Hub A, loyalty to Hub C4. |
| Connections dupes | `sevenrooms` and `sevenrooms-2`, `shiji` and `shiji-2` | 301 the `-2` pages, or retitle them to distinct products (e.g. Shiji Infrasys POS vs Shiji Daylight PMS). |
| Product vs pillar | `/product/hapi-connectivity` vs Hub A pillar | Pillar targets "hotel data integration" (informational). Product page targets "hotel integration platform" (commercial). The new A1 comparison spoke targets "integration platform vs point-to-point". All three are distinct. |

**Off-site cannibalization:** syndicated copies outrank the originals. When posting to hospitalitynet and hotel-online, request a `rel=canonical` back to stayhapi.com, or at minimum an "originally published on stayhapi.com" link. Publish on stayhapi.com 3 to 7 days before syndicating.

---

## 6. Internal link matrix

### Mandatory (bidirectional)

- Each pillar links to every spoke in its hub, and every spoke links to its pillar.
- Each pillar links to its money page or pages.
- Pillar A ↔ Pillar B ↔ Pillar C, so all three hubs link to each other.
- `/resources` index gets a "Topic hubs" strip linking to all three pillars plus the loyalty hub.
- Main nav: add the hubs under Resources.

### Recommended (spoke to spoke within a cluster)

- **A1:** integration-layer-strategy ↔ hotel-integration-platform-vs-point-to-point ↔ beyond-the-pms-debate
- **A2:** breaking-down-data-silos ↔ how-fragmented-hotel-tech ↔ real-time-data-problem
- **A3:** multi-PMS rewrite ↔ hotel-m-a
- **A4:** ai-ready-framework ↔ ai-in-hospitality-2026 ↔ why-cant-i-just-build-this-with-ai
- **B1:** 2026-pms-api-study ↔ opera-cloud-ohip-guide ↔ pms-the-heart
- **B2:** hospitality-api ↔ why-custom-integrations ↔ sandbox-pms
- **B3:** each PMS connection page links to the B pillar, the 2026 PMS API study and 1 relevant case study. OPERA links to the OHIP guide.
- **C1:** identity-resolution ↔ guest-identity-vs-crm ↔ why-guest-data-still-fails
- **C2:** mdm-vs-cdp ↔ lakehouse-vs-cdp ↔ how-a-cdp-will-shape
- **C3:** salesforce-for-hotels ↔ salesforce-data-cloud ↔ best-hotel-crm, plus `/connections/salesforce`
- **C4:** existing loyalty hub links, plus a link up to the C pillar

### Optional (cross-cluster bridges, 0 to 1 per post)

- multi-PMS (A3) → 2026 PMS API study (B1)
- ai-ready framework (A4) → lakehouse-vs-cdp (C2)
- identity-resolution (C1) → breaking-down-data-silos (A2)
- salesforce-for-hotels (C3) → opera-cloud-ohip-guide (B1)
- hospitality-api (B2) → integration-platform-vs-point-to-point (A1)

### Template-level fixes that carry the links

1. Replace the global "Related Posts" module, which shows the same 6 links on every page, with tag-driven related posts filtered by hub.
2. Customer Story template: add "Systems connected" chips that link to the `/connections/*` pages named in the story.
3. Connection template: add a "Resources about this integration" collection list. Populate the Data Streams and Related Products fields that render empty today.

**Incoming-link check:** each spoke receives at least 4 links: pillar, 2 cluster siblings, and a connection page, case study or cross-cluster bridge. No orphans.

---

## 7. Top 10 new pages, prioritized

Priority weighs quick wins, pillar enablement, and keywords where Hapi already has the authority but no owned URL.

| # | Page | URL | Hub | Primary keyword | Intent / template | Words | Why now |
|---|---|---|---|---|---|---|---|
| 1 | **The 2026 PMS API Study (full body)** | `/resources/the-2026-pms-api-study` (empty today) | B | hotel PMS API comparison | Informational / data study | 1,800 to 2,500 | The URL is already in the sitewide Related Posts module, so it gets internal links on every page, yet it serves 15 words. Stayntouch ranks with "What Is a Hotel PMS Open API? A 2026 Comparison Guide". This is original data, the best link magnet Hapi has. |
| 2 | **Hotel PMS Integration: the complete guide** (pillar B) | `/hub/hotel-pms-integration` | B | hotel PMS integration + PMS API integration | Informational / ultimate-guide | 3,000 to 3,500 | The only seed with a real cluster (K2, K8 and K12 at 4 to 8 overlap). The SERP is vendor blogs (Mews, Cloudbeds, Revfine), all beatable with Hapi's 58 connections as proof. Turns `/connections` into spokes. |
| 3 | **Hotel Guest Data Platform guide: CDP, CRM, MDM, lakehouse and identity** (pillar C) | `/hub/hotel-guest-data-platform` | C | hotel guest data platform / hotel CDP | Commercial-informational / ultimate-guide | 3,000 to 4,000 | Revinate owns this SERP. Hapi already has 3 comparison posts (MDM, lakehouse, CRM) with nothing tying them together, and two new products (Guest Identity, Data Lakehouse) that need an informational feeder. |
| 4 | **Hotel Data Integration: the complete guide** (pillar A) | `/hub/hotel-data-integration` | A | hotel data integration | Informational / ultimate-guide | 3,000 to 4,000 | Brand-defining head term. Today only Hapi's syndicated press and Cloudbeds' architecture hub rank. Gathers about 35 T1 URLs. |
| 5 | **Hotel guest identity resolution: building the golden guest record** | `/resources/hotel-guest-identity-resolution-golden-guest-record` | C1 | hotel guest identity resolution | Informational / explainer | 1,400 to 1,800 | Hapi's Guest Identity launch already ranks for this query, but only via syndication. TrustYou, Improvado and Hospitality Upgrade own the explainer slot. Direct feeder to `/product/hapi-guest-identity`. |
| 6 | **Salesforce for hotels: connecting PMS data to Salesforce** | `/resources/salesforce-for-hotels-pms-integration-guide` | C3 | Salesforce for hotels / Salesforce hotel PMS integration | Informational / how-to | 1,600 to 1,800 | 9 of the top 20 for K13 are Hapi press syndications and none are stayhapi.com. Consolidates 4 legacy Salesforce posts (2019 to 2020). Mews is the competing owned page. |
| 7 | **OPERA Cloud integration via OHIP: a guide for hotel groups and vendors** | `/resources/opera-cloud-ohip-integration-guide` | B1 | OPERA Cloud integration / OHIP | Informational / how-to | 1,400 to 1,800 | A high-intent technical query. The SERP is vendor help docs (Civitfun, DialogShift, Conduit) and AltexSoft. Hapi is on the Oracle Cloud Marketplace and has OPERA connection pages with nothing to rank them. |
| 8 | **Hotel integration platform vs point-to-point vs PMS marketplace** | `/resources/hotel-integration-platform-vs-point-to-point` | A1 | hotel integration platform / hospitality middleware | Commercial / comparison | 1,400 to 1,800 | The K5 SERP is Oracle OHIP plus a hospitalitynet expert panel that names Hapi as an independent hub. It is the bottom-of-funnel bridge to `/product/hapi-connectivity`. |
| 9 | **AI-Ready Hospitality Data Framework (full body)** | `/resources/ai-ready-hospitality-data-framework` (empty today) | A4 | AI-ready hotel data / hotel AI readiness | Informational / explainer and checklist | 1,400 to 1,800 | Cloudbeds' `/hotel-data-architecture/ai-readiness/` ranks for K14. Hapi has 14 AI posts and an empty URL with this exact name. Fill it, then 301 the weak AI posts into the cluster. |
| 10 | **Hospitality API: one integration to every hotel PMS** (tech-vendor audience) | `/resources/hospitality-api-one-integration-to-every-pms` | B2 | hospitality API / hotel PMS API for vendors | Informational-commercial / explainer | 1,200 to 1,600 | The K3 SERP is Oracle docs, apitracker and Cloudbeds API. No owned page speaks to vendors who need many PMSs. Feeds `/who-we-serve/technology-providers` and developers.hapicloud.io. |

**Also queued, as rebuilds rather than new pages:**
- Expand `breaking-down-data-silos` (K9). Lighthouse's "data fragmentation tax" piece is the bar to beat.
- Rewrite `embracing-the-multi-pms-era` (K12).
- Expand `guest-identity-vs-crm` and `data-lakehouse-vs-cdp`.
- Rebuild `8-best-crm-software-for-hotels-in-2025` as the 2026 version, or 301 it.

---

## 8. Execution order

1. **Week 0, floor fixes (these make everything else work):**
   - Populate `<title>` and meta description on 90+ resource pages and about 50 connection pages. In Webflow this is a CMS SEO-field binding; check whether the collection template's SEO title is bound to an empty field.
   - Fix the "Originally published on" `#` links.
   - Run the 301 consolidations from section 5.
2. **Weeks 1 to 2:** Pages #1 (PMS API study) and #9 (AI framework). These fill existing empty URLs, so there is no new IA to build.
3. **Weeks 2 to 4:**
   - Pillars #2, #3 and #4.
   - Connection template upgrade.
   - Replace the Related Posts module.
   - Tag every resource to a hub.
4. **Weeks 4 to 8:** Spokes #5 to #8 and #10, then the rebuild queue.
5. **Ongoing:** Syndication policy (canonical-back or delay) for every hospitalitynet and hotel-online placement.

---

## 9. cluster-plan.json

The file follows the hub-spoke-architecture schema, with one entry per hub.

```json
{
  "version": "2.2.5",
  "site": "https://www.stayhapi.com",
  "created_at": "2026-11-17",
  "hubs": [
    {
      "seed_keyword": "hotel data integration",
      "pillar": {"title": "Hotel Data Integration: The Complete Guide for Hotel Groups", "keyword": "hotel data integration", "template": "ultimate-guide", "wordCount": 3500, "url": "/hub/hotel-data-integration", "status": "planned", "money_page": "/product/hapi-connectivity"},
      "clusters": [
        {"name": "Integration layer", "posts": [
          {"url": "/resources/integration-layer-strategy-the-real-barrier-to-hotel-innovation", "keyword": "hotel integration layer", "template": "explainer", "status": "written", "absorbs": ["/resources/the-integration-layer-is-your-hedge-against-an-unpredictable-future"]},
          {"url": "/resources/hotel-integration-platform-vs-point-to-point", "keyword": "hotel integration platform middleware", "template": "comparison", "wordCount": 1600, "status": "planned"},
          {"url": "/resources/beyond-the-pms-debate-why-connectivity-may-be-hospitalitys-biggest-innovation-challenge", "keyword": "hotel tech connectivity", "template": "explainer", "status": "written"}]},
        {"name": "Data silos and fragmentation", "posts": [
          {"url": "/resources/breaking-down-data-silos-in-hospitality-the-case-for-a-unified-data-layer", "keyword": "hotel data silos", "template": "explainer", "status": "expand", "absorbs": ["/resources/how-data-can-bridge-the-gap-between-technology-and-operations"]},
          {"url": "/resources/how-fragmented-hotel-tech-is-affecting-operations-and-guest-satisfaction", "keyword": "fragmented hotel tech", "template": "explainer", "status": "written"},
          {"url": "/resources/the-real-time-data-problem-in-hospitality-and-why-it-matters", "keyword": "real-time hotel data", "template": "explainer", "status": "written", "absorbs": ["/resources/realtimedatastream", "/resources/real-time-data-can-serve-as-a-differentiator-for-hotel-brands"]}]},
        {"name": "Portfolio and multi-PMS", "posts": [
          {"url": "/resources/embracing-the-multi-pms-era-how-hapi-facilitates-seamless-data-integration-for-hotel-companies", "keyword": "multi-PMS hotel data integration", "template": "how-to", "status": "rewrite"},
          {"url": "/resources/hotel-m-a-navigating-technical-hurdles-and-driving-portfolio-growth", "keyword": "hotel M&A technology integration", "template": "how-to", "status": "written"}]},
        {"name": "AI-ready data", "posts": [
          {"url": "/resources/ai-ready-hospitality-data-framework", "keyword": "AI-ready hotel data", "template": "explainer", "wordCount": 1600, "status": "planned-fill-empty-url"},
          {"url": "/resources/ai-in-hospitality-2026-why-data-has-to-come-before-the-algorithm", "keyword": "AI in hospitality data", "template": "explainer", "status": "written", "absorbs": ["/resources/ai-in-hospitality-why-data-matters-more-than-ever", "/resources/driving-ai-in-the-hotel-industry-the-importance-of-data", "/resources/how-hotels-can-make-ai-work-for-them-overcoming-legacy-system-challenges"]},
          {"url": "/resources/why-cant-i-just-build-this-with-ai-what-hotel-brands-need-to-know", "keyword": "build vs buy hotel integrations AI", "template": "explainer", "status": "written"}]}
      ]
    },
    {
      "seed_keyword": "hotel PMS integration",
      "pillar": {"title": "Hotel PMS Integration: APIs, Middleware and Multi-PMS Portfolios", "keyword": "hotel PMS integration", "secondary": ["PMS API integration"], "template": "ultimate-guide", "wordCount": 3200, "url": "/hub/hotel-pms-integration", "status": "planned", "money_page": "/product/hapi-connectivity", "directory": "/connections"},
      "clusters": [
        {"name": "PMS APIs", "posts": [
          {"url": "/resources/the-2026-pms-api-study", "keyword": "hotel PMS API comparison", "template": "explainer", "wordCount": 2200, "status": "planned-fill-empty-url"},
          {"url": "/resources/opera-cloud-ohip-integration-guide", "keyword": "OPERA Cloud integration OHIP", "template": "how-to", "wordCount": 1600, "status": "planned"},
          {"url": "/resources/pms-the-heart-of-the-hospitality-operating-environment", "keyword": "what is hotel PMS integration", "template": "explainer", "status": "refresh"}]},
        {"name": "For technology providers", "posts": [
          {"url": "/resources/hospitality-api-one-integration-to-every-pms", "keyword": "hospitality API", "template": "explainer", "wordCount": 1400, "status": "planned", "money_page": "/who-we-serve/technology-providers"},
          {"url": "/resources/why-custom-integrations-are-hurting-your-product-roadmap---and-your-growth", "keyword": "custom PMS integrations cost", "template": "explainer", "status": "written"},
          {"url": "/resources/new-hapi-sandbox-pms-makes-integration-testing-a-joy", "keyword": "PMS sandbox integration testing", "template": "how-to", "status": "expand"}]},
        {"name": "Connection spokes", "posts": [
          {"url": "/connections/oracle-opera-v5-pms", "keyword": "OPERA 5 integration", "template": "landing-page", "status": "template-fix"},
          {"url": "/connections/mews", "keyword": "Mews PMS integration", "template": "landing-page", "status": "template-fix"},
          {"url": "/connections/infor", "keyword": "Infor HMS integration", "template": "landing-page", "status": "template-fix"},
          {"url": "/connections/stayntouch", "keyword": "Stayntouch integration", "template": "landing-page", "status": "template-fix"}]}
      ]
    },
    {
      "seed_keyword": "hotel guest data platform",
      "pillar": {"title": "Hotel Guest Data Platforms: CDP, CRM, MDM, Lakehouse and Identity Explained", "keyword": "hotel guest data platform", "secondary": ["hotel CDP"], "template": "ultimate-guide", "wordCount": 3500, "url": "/hub/hotel-guest-data-platform", "status": "planned", "money_page": ["/product/hapi-guest-identity", "/product/hapi-data-lakehouse"]},
      "clusters": [
        {"name": "Guest identity", "posts": [
          {"url": "/resources/hotel-guest-identity-resolution-golden-guest-record", "keyword": "hotel guest identity resolution", "template": "explainer", "wordCount": 1600, "status": "planned"},
          {"url": "/resources/guest-identity-vs-crm-whats-the-difference", "keyword": "guest identity vs CRM", "template": "comparison", "status": "expand"},
          {"url": "/resources/why-guest-data-still-fails-at-the-moment-it-matters-most", "keyword": "guest data activation", "template": "explainer", "status": "fill-empty-url-or-301"}]},
        {"name": "Architecture comparisons", "posts": [
          {"url": "/resources/exploring-mdm-vs-cdp-in-hospitality", "keyword": "hotel MDM vs CDP", "template": "comparison", "status": "refresh"},
          {"url": "/resources/data-lakehouse-vs-cdp-whats-the-difference-for-hotel-groups", "keyword": "hotel data lakehouse vs CDP", "template": "comparison", "status": "expand"},
          {"url": "/resources/how-a-cdp-will-shape-the-future-of-hotel-marketing", "keyword": "hotel CDP marketing", "template": "explainer", "status": "written", "absorbs": ["/resources/4-tips-for-choosing-a-solution-to-optimize-your-guest-data"]}]},
        {"name": "Salesforce and CRM", "posts": [
          {"url": "/resources/salesforce-for-hotels-pms-integration-guide", "keyword": "Salesforce for hotels", "template": "how-to", "wordCount": 1700, "status": "planned", "absorbs": ["/resources/hospitality-crm-a-hoteliers-guide-to-learning-salesforce", "/resources/hospitality-crm-a-hoteliers-guide-to-learning-salesforce-65f94", "/resources/hapiconnectforsalesforce", "/resources/hapis-connector-app-for-salesforce-goes-next-level"]},
          {"url": "/resources/why-hapi-is-essential-for-implementing-salesforce-data-cloud-in-the-hotel-industry", "keyword": "Salesforce Data Cloud hotels", "template": "explainer", "status": "retitle"},
          {"url": "/resources/8-best-crm-software-for-hotels-in-2025", "keyword": "best hotel CRM software", "template": "best-of", "status": "rebuild-or-301"}]},
        {"name": "Loyalty (sub-hub)", "posts": [
          {"url": "/hub/hospitality-loyalty-guest-recognition-hub", "keyword": "hotel loyalty guest recognition", "template": "existing-hub", "status": "written"},
          {"url": "/resources/recognition-matters-bridging-the-loyalty-gap-in-hospitality", "keyword": "hotel guest recognition", "status": "written"},
          {"url": "/resources/hapi-enhances-your-hotels-loyalty-program", "keyword": "hotel loyalty program data", "status": "written"}]}
      ]
    }
  ],
  "serp_overlap": [
    {"a": "hotel PMS integration", "b": "PMS API integration hotels", "shared": 8, "verdict": "same-post"},
    {"a": "hotel PMS integration", "b": "multi-PMS hotel portfolio data integration", "shared": 5, "verdict": "same-cluster"},
    {"a": "PMS API integration hotels", "b": "multi-PMS hotel portfolio data integration", "shared": 4, "verdict": "same-cluster"},
    {"a": "hospitality API", "b": "hotel integration platform middleware", "shared": 2, "verdict": "interlink"},
    {"a": "hotel integration platform middleware", "b": "OPERA Cloud integration OHIP", "shared": 2, "verdict": "interlink"},
    {"a": "hotel guest data platform", "b": "hotel CDP", "shared": 2, "verdict": "interlink"},
    {"a": "guest identity resolution", "b": "hotel data lakehouse AI ready", "shared": 2, "verdict": "interlink"},
    {"a": "hotel data silos", "b": "guest identity resolution", "shared": 1, "verdict": "separate"},
    {"a": "hotel data integration", "b": "hotel PMS integration", "shared": 0, "verdict": "separate"},
    {"a": "hotel data integration", "b": "hospitality API", "shared": 1, "verdict": "separate"},
    {"a": "hotel data integration", "b": "hotel guest data platform", "shared": 0, "verdict": "separate"},
    {"a": "hotel PMS integration", "b": "hospitality API", "shared": 0, "verdict": "separate"},
    {"a": "hotel PMS integration", "b": "hotel guest data platform", "shared": 0, "verdict": "separate"},
    {"a": "hospitality API", "b": "hotel guest data platform", "shared": 0, "verdict": "separate"}
  ],
  "excluded_keywords": [{"keyword": "hotel API integration", "reason": "OTA and bed-bank supply intent (RateHawk, Hotelbeds), not Hapi's buyer"}]
}
```

---

## 10. Validation checklist

- [x] No two posts share a primary keyword. K2 and K8 are merged into one pillar; K4 and K7 are merged into one pillar with a CDP section.
- [x] Every spoke links to its pillar, and every pillar links to all of its spokes (section 6).
- [x] Every spoke has at least 3 incoming links planned, and there are no orphans.
- [x] Templates match intent. Comparisons go to the commercial "vs" terms, how-to to the OHIP and Salesforce guides, best-of to the CRM list, and landing-page to connections.
- [x] Word counts: pillars 3,000 to 4,000 and spokes 1,200 to 1,800. Exception: the PMS API study is a data asset at up to 2,500.
- [x] Cluster size: each hub has 3 to 4 clusters of 2 to 4 posts.
- [ ] **SERP overlap of 4 or more to cluster peers is met only in Hub B (PMS family).** The other clusters are grouped at interlink level (2 to 3 shared URLs) plus topical and vendor overlap. In fragmented, low-volume B2B hospitality SERPs, a strict reading would make every keyword its own island. Re-validate with volume data (DataForSEO or GSC) before writing spokes #5 to #10.
- **Caveat:** we have no search volume or GSC data. "Broadest keyword" for each pillar is judged by SERP breadth and topical coverage, not by measured volume.
