# Schema.org audit: stayhapi.com

Audited 2026-11-17. Sample: homepage, /our-story, /contact-us, /product-overview, /product/* (5), /connections index plus 5 detail pages (salesforce, mews, oracle-opera-v5-pms, sevenrooms, revinate), /resources index plus 4 articles (the-2026-pms-api-study, hapi-launches-folio-finder, data-lakehouse-vs-cdp..., how-hyatt..., ai-ready-hospitality-data-framework). Method: raw HTML fetch (Webflow serves server-rendered HTML, so raw = rendered for schema). Playwright re-render timed out on a later attempt; curl raw fetch confirmed 0 `ld+json` blocks on the CMS pages, consistent with the first pass.

## Score: 12 / 100

| Area | Max | Score | Note |
|---|---|---|---|
| Entity foundation (Organization, WebSite) | 25 | 0 | None present |
| Product/software markup | 20 | 0 | None present |
| Content markup (Article/BlogPosting) | 20 | 0 | None on ~150 CMS articles |
| Navigation (BreadcrumbList) | 10 | 0 | None |
| Integration/partner pattern | 10 | 0 | None |
| Syntax validity of what exists | 10 | 10 | 5 FAQPage blocks parse cleanly, https context |
| Google-eligible value of what exists | 5 | 2 | FAQPage is valid but gives no SERP feature |

## Detection

| URL | JSON-LD | Microdata/RDFa |
|---|---|---|
| / | none | none |
| /our-story, /contact-us, /product-overview | none | none |
| /product/hapi-connectivity | FAQPage, 6 Q&A | none |
| /product/hapi-guest-identity | FAQPage, 6 Q&A | none |
| /product/hapi-data-lakehouse | FAQPage, 6 Q&A | none |
| /product/hapi-autopilot | FAQPage, 5 Q&A | none |
| /product/services | FAQPage, 5 Q&A | none |
| /connections, /connections/* (5 sampled) | none | none |
| /resources, /resources/* (4 sampled) | none | none |

Only 5 of ~21 sampled pages carry schema, all FAQPage, all on the product pages.

## Validation of existing blocks

| Block | Result |
|---|---|
| 5x FAQPage | Syntax PASS (@context https://schema.org, Question/acceptedAnswer/Answer structure correct, text matches visible FAQ copy). Value: none for Google. Google retired FAQ rich results for all sites on 2026-05-07. Keep as Info; no removal needed, no further investment. |

## Findings

### Critical

**C1. No Organization or WebSite entity anywhere.** Evidence: 0 JSON-LD on homepage, /our-story, /contact-us. Hapi's own knowledge-graph identity (legal name Data Travel, LLC dba Hapi, founders Luis Segredo and Nikolai Balba, 2017, LinkedIn `linkedin.com/company/hapicloud`) is on-page but unstructured. This is the anchor every other block references via @id. Fix: Snippet 1.

**C2. All ~150 CMS articles (/resources/*) have no Article markup, and the page head is empty.** Evidence on all 4 sampled articles (and the Mews connection page): `<title></title>`, `<meta name="description" content="">`, `<meta property="og:title" content="">`. The og:image is populated on some, empty on others. The page has a visible H1, a visible date ("October 1, 2026", "February 26, 2026") and a category (Blog / In The News / Press Releases / Customer Stories) but no byline. This is a Webflow CMS-template problem (SEO fields not bound to CMS fields), and it hits schema and basic SEO at once. Fix: bind the template SEO title/description to CMS fields, then add Snippet 4.

### High

**H1. No software/product entity on /product/* and /product-overview.** Five module pages (Connectivity, Autopilot, Guest Identity, Data Lakehouse, Services) have only FAQPage. Add SoftwareApplication per module (Snippet 3). No `offers` because pricing is "covered in a proposal"; do not fabricate prices. There is no Google software-app rich result for B2B platforms without ratings/offers, so the value here is entity clarity for AI/search understanding, not SERP decoration.

**H2. No BreadcrumbList on any page.** Visible navigation hierarchy exists (Resources > article, Connections > partner, Products > module); the connection page even has a "Go Back"/"Return to Tech Vendor Marketplace" link. Snippet 5.

**H3. /connections/* (~55 pages) have no structured pattern.** Each is a partner entity page (Mews: "PMS", "Producer", "12,500 customers in 85 countries"). Snippet 6.

### Medium

**M1. Placeholder lorem ipsum in the global nav mega-menu.** "Bibendum amet at molestie mattis." appears 3 times under Connections > Segments on every page, including inside the HTML Google indexes. Not schema, but it is placeholder text sitewide. Replace or delete. (Also fails the "no placeholder text" check should anyone mirror nav copy into schema.)

**M2. Missing `WebPage`-level typing on key pages.** /our-story could be `AboutPage`, /contact-us `ContactPage`. Snippet 7. Contact page exposes no phone/address, so do not invent ContactPoint values beyond the website form URL.

**M3. Organization `logo` source unconfirmed.** Favicon is `.../68457b2934000d9981f52aee_Logo.png`; no dedicated logo asset identified. Confirm a square-ish PNG/SVG >= 112x112 and substitute in Snippet 1.

**M4. Duplicate/near-duplicate CMS slugs create duplicate-entity risk.** e.g. `hapi-and-nemacolin-...-award` and `...-298fa`, `margaritaville-...-2`, `connections/sevenrooms` vs `sevenrooms-2`, `shiji`/`shiji-2`. Each carries its own canonical (self), so schema would duplicate. Consolidate or canonicalize before bulk-adding schema.

### Low

**L1. FAQPage on product pages: Info only.** No SERP benefit. Leave in place; any AI-visibility benefit is unconfirmed. Do not add FAQPage to new pages. (These pages are marketing FAQs, not user Q&A, so QAPage is not appropriate either.)

**L2. No `sameAs` beyond LinkedIn.** Add Crunchbase, G2/Hotel Tech Report profile, and X/YouTube if they exist (only LinkedIn confirmed on site).

**L3. Dates.** Visible dates render as "Month D, YYYY". Convert to ISO 8601 in the Webflow embed (see Snippet 4 note).

## Not recommended
- HowTo (deprecated). FAQPage additions (no Google SERP feature as of 2026-05-07). Review/AggregateRating on Hapi itself: site shows award mentions but no on-page reviews, and self-serving ratings are ineligible.
- Product schema with Offer for the modules: no public pricing.
- Person markup for the 9+ "Hapi People Spotlight" posts unless the page body is about the individual; optional.

## Implementation notes (Webflow)
- Site-wide: Project Settings > Custom Code > Head, or a Site-wide embed, for Snippet 1 (Organization + WebSite graph). Output once, not per page.
- CMS templates: add an HTML Embed inside the template, use "Add Field" to insert `{{ }}` values. Webflow's CMS embed fields are written as the field picker inserts them; below, tokens in `{{double braces}}` denote that. Quotes in CMS text must be handled: use plain-text fields without quotes, or the CMS "Plain text" field. For headlines containing `"`, strip or escape.
- Date format: Webflow outputs dates in the field's display format. Use a hidden CMS text field "Date ISO" (YYYY-MM-DD) or Webflow's `datetime` attribute embed if available; manually backfill once.
- After deploy, validate with Google Rich Results Test and validator.schema.org on one URL per template.

---

## Snippet 1: Organization + WebSite (site-wide, homepage or global head)

Confirm logo URL and any additional sameAs before publishing. SearchAction is omitted because the site has no internal search endpoint (Google dropped the sitelinks search box anyway).

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.stayhapi.com/#organization",
      "name": "Hapi",
      "legalName": "Data Travel, LLC",
      "alternateName": "Hapi - Hospitality's Connectivity Partner",
      "url": "https://www.stayhapi.com",
      "logo": {
        "@type": "ImageObject",
        "url": "https://cdn.prod.website-files.com/6831885d98a186b5fce7fe65/68457b2934000d9981f52aee_Logo.png"
      },
      "image": "https://cdn.prod.website-files.com/6831885d98a186b5fce7fe65/6881d1e30d85fded92bfb905_hapi.png",
      "description": "Hapi is a data-integrations platform that extracts, cleans and normalizes data for hospitality technology stakeholders through open APIs, connecting hotel PMS and the systems around them.",
      "foundingDate": "2017",
      "founder": [
        { "@type": "Person", "name": "Luis Segredo" },
        { "@type": "Person", "name": "Nikolai Balba" }
      ],
      "sameAs": [
        "https://www.linkedin.com/company/hapicloud/"
      ],
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "sales",
        "url": "https://www.stayhapi.com/contact-us"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://www.stayhapi.com/#website",
      "url": "https://www.stayhapi.com",
      "name": "Hapi",
      "publisher": { "@id": "https://www.stayhapi.com/#organization" },
      "inLanguage": "en"
    }
  ]
}
```

## Snippet 2: Platform entity (homepage and /product-overview)

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "@id": "https://www.stayhapi.com/#platform",
  "name": "Hapi Platform",
  "applicationCategory": "BusinessApplication",
  "applicationSubCategory": "Hospitality data integration",
  "operatingSystem": "Web",
  "url": "https://www.stayhapi.com/product-overview",
  "description": "Hapi connects hotel PMS and surrounding systems through one normalized hospitality data model, with read and write access.",
  "provider": { "@id": "https://www.stayhapi.com/#organization" },
  "hasPart": [
    { "@id": "https://www.stayhapi.com/product/hapi-connectivity#software" },
    { "@id": "https://www.stayhapi.com/product/hapi-data-lakehouse#software" },
    { "@id": "https://www.stayhapi.com/product/hapi-guest-identity#software" },
    { "@id": "https://www.stayhapi.com/product/hapi-autopilot#software" }
  ]
}
```

## Snippet 3: Product module (/product/*; shown for Connectivity, copy for the others)

Descriptions are lifted from each page's live meta description. Swap name/url/description per page. Keep the existing FAQPage block (harmless), or drop it.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "@id": "https://www.stayhapi.com/product/hapi-connectivity#software",
  "name": "Hapi Connectivity",
  "applicationCategory": "BusinessApplication",
  "applicationSubCategory": "Hospitality data integration",
  "operatingSystem": "Web",
  "url": "https://www.stayhapi.com/product/hapi-connectivity",
  "description": "Hapi Connectivity links your PMS and hotel systems through one two-way integration: normalized data, real transactions, no rebuild per system.",
  "isPartOf": { "@id": "https://www.stayhapi.com/#platform" },
  "provider": { "@id": "https://www.stayhapi.com/#organization" },
  "audience": { "@type": "BusinessAudience", "audienceType": "Hotel brands and hospitality technology providers" }
}
```

Per-page values:
- Guest Identity: `/product/hapi-guest-identity`, "Hapi Guest Identity unifies guest records across your PMS, spa, loyalty & survey tools into one verified profile, matched deterministically, never guessed."
- Data Lakehouse: `/product/hapi-data-lakehouse`, "Hapi Data Lakehouse unifies reservation, guest, stay & folio data into one governed, AI-ready model you own: open formats, full export, always yours."
- Autopilot: `/product/hapi-autopilot`, "Hapi Autopilot automates hotel workflows, from revenue recovery to checkout to inventory, by reading data, deciding, and writing it back to your PMS."
- Hapi Services (/product/services) is a service, not software. Use:

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://www.stayhapi.com/product/services#service",
  "name": "Hapi Services",
  "serviceType": "Hospitality technology project management and support",
  "url": "https://www.stayhapi.com/product/services",
  "description": "From strategy to execution, Hapi Services helps hospitality brands plan, build, and launch tech solutions that fit their business.",
  "provider": { "@id": "https://www.stayhapi.com/#organization" },
  "areaServed": "Worldwide"
}
```

## Snippet 4: Article template (/resources/* CMS template)

Type mapping by the CMS "category" value: Blog -> `BlogPosting`; Press Releases and In The News -> `NewsArticle`; Customer Stories -> `Article`. Author: no bylines are on the page, so author is the Organization (do not invent people). If a CMS "Author" field is added later (e.g. CEO-bylined posts), switch to `Person`. `dateModified` falls back to `datePublished` (Webflow does not expose a clean last-updated token; add a CMS field if you track edits). Verified live dates for reference: PMS API Study 2026-10-01; Folio Finder 2026-02-26.

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "https://www.stayhapi.com/resources/{{slug}}#article",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.stayhapi.com/resources/{{slug}}" },
  "headline": "{{Name}}",
  "description": "{{Summary or first 160 chars}}",
  "image": "{{Main image URL}}",
  "datePublished": "{{Date ISO, e.g. 2026-10-01}}",
  "dateModified": "{{Date ISO}}",
  "articleSection": "{{Category}}",
  "author": { "@id": "https://www.stayhapi.com/#organization" },
  "publisher": { "@id": "https://www.stayhapi.com/#organization" },
  "inLanguage": "en"
}
```

Concrete example (/resources/hapi-launches-folio-finder):

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "@id": "https://www.stayhapi.com/resources/hapi-launches-folio-finder#article",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.stayhapi.com/resources/hapi-launches-folio-finder" },
  "headline": "Hapi launches Folio Finder",
  "description": "Hapi introduces Folio Finder, a product that lets hotel brands and technology providers search and retrieve guest folios and invoice details across properties and compatible PMSs through a standard API.",
  "datePublished": "2026-02-26",
  "dateModified": "2026-02-26",
  "articleSection": "Press Releases",
  "author": { "@id": "https://www.stayhapi.com/#organization" },
  "publisher": { "@id": "https://www.stayhapi.com/#organization" },
  "inLanguage": "en"
}
```

For "In The News" items (republished from a trade outlet), add `"isBasedOn": "{{Original article URL}}"` if the CMS stores it; the page says "Originally published on: Hotel Business".

Prerequisite: the same template must output a real `<title>`, meta description and og tags (finding C2). Also add a populated image: Article image is recommended; many posts have an empty og:image, so set a fallback (the site hero image).

## Snippet 5: BreadcrumbList

Static pages (example /product/hapi-connectivity):

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.stayhapi.com" },
    { "@type": "ListItem", "position": 2, "name": "Products", "item": "https://www.stayhapi.com/product-overview" },
    { "@type": "ListItem", "position": 3, "name": "Hapi Connectivity", "item": "https://www.stayhapi.com/product/hapi-connectivity" }
  ]
}
```

Article template:

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.stayhapi.com" },
    { "@type": "ListItem", "position": 2, "name": "Resources", "item": "https://www.stayhapi.com/resources" },
    { "@type": "ListItem", "position": 3, "name": "{{Name}}", "item": "https://www.stayhapi.com/resources/{{slug}}" }
  ]
}
```

Connection template: same, with position 2 "Connections" -> `https://www.stayhapi.com/connections` and position 3 `{{Name}}` -> `https://www.stayhapi.com/connections/{{slug}}`.

## Snippet 6: Integration (/connections/*) pattern

Pattern: a `WebPage` whose `mainEntity` is the partner `Organization` (the partner is the subject of the page), linked to Hapi via `about`-style relation to the Hapi platform, plus `BreadcrumbList` (Snippet 5). Not Product/SoftwareApplication (Hapi does not sell the partner's product) and not Review. Webflow CMS fields to use: Name, slug, Category (PMS, etc.), Description, Logo, optional Website URL. Example for Mews, text taken from the live page:

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://www.stayhapi.com/connections/mews#webpage",
  "url": "https://www.stayhapi.com/connections/mews",
  "name": "Mews integration with Hapi",
  "description": "Mews is a property management system connected to Hapi. An innovative hospitality management cloud supporting over 12,500 customers in 85 countries.",
  "isPartOf": { "@id": "https://www.stayhapi.com/#website" },
  "about": { "@id": "https://www.stayhapi.com/connections/mews#partner" },
  "mainEntity": {
    "@type": "Organization",
    "@id": "https://www.stayhapi.com/connections/mews#partner",
    "name": "Mews",
    "description": "An innovative hospitality management cloud that empowers the modern hotelier to streamline operations, improve performance and maximize revenue. Mews supports over 12,500 customers in 85 countries.",
    "knowsAbout": "Hotel property management systems",
    "sameAs": "https://www.mews.com"
  },
  "mentions": { "@id": "https://www.stayhapi.com/product/hapi-connectivity#software" }
}
```

Template version: replace Mews values with `{{Name}}`, `{{slug}}`, `{{Description}}`, add `{{Category}}` into the page `name` (e.g. "{{Name}} {{Category}} integration with Hapi"). Only emit `sameAs` if the CMS has a verified partner URL (verify mews.com before use; Hapi's page does not state it). Optional second pass: a `/connections` index page as `CollectionPage` with `ItemList` of the partners.

## Snippet 7: AboutPage / ContactPage

```json
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "@id": "https://www.stayhapi.com/our-story#webpage",
  "url": "https://www.stayhapi.com/our-story",
  "name": "The Hapi Story",
  "isPartOf": { "@id": "https://www.stayhapi.com/#website" },
  "about": { "@id": "https://www.stayhapi.com/#organization" }
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "@id": "https://www.stayhapi.com/contact-us#webpage",
  "url": "https://www.stayhapi.com/contact-us",
  "name": "Contact Hapi",
  "isPartOf": { "@id": "https://www.stayhapi.com/#website" },
  "about": { "@id": "https://www.stayhapi.com/#organization" }
}
```

## Rollout order (highest leverage first)
1. Fix empty `<title>`/meta description/og:title on the Resources and Connections CMS templates (C2). Ships SEO value and unblocks everything.
2. Snippet 1 site-wide (Organization + WebSite).
3. Snippet 4 + 5 on the Resources template (covers ~150 pages in one edit).
4. Snippet 3 + 5 on 5 product pages, Snippet 2 on /product-overview.
5. Snippet 6 + 5 on the Connections template (~55 pages).
6. Snippet 7, then cleanup of M1/M4.

Expected score after steps 1-5: ~80 (loss for no ratings/offers, no author persons, undated modifications).
