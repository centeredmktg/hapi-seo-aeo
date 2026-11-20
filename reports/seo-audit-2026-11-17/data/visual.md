# Hapi (stayhapi.com) visual and mobile audit, 2026-11-17

Pages: / , /product/hapi-connectivity , /connections , /resources/ai-ready-hospitality-data-framework
Screenshots: screenshots/{home,product,connections,resource}-{desktop,mobile}[-full].png
Gap: home-mobile capture FAILED (Chromium timed out 4x at 45-60s while desktop home and curl loaded); no home-mobile screenshot exists. Other mobile shots use iPhone 13 (product) or 375x812 (connections, resource).

## Above the fold
- Home (desktop): H1 "Hospitality's Data Infrastructure" visible (top 260px), subhead "Bringing fragmented hotel data together in real time...", CTA "Let's Connect" visible twice (nav pill + hero), logo strip (Hyatt, Wyndham, Starwood, Sonesta, Margaritaville) immediately below. 5-second test: a hotel tech buyer gets "data infrastructure for hotels" but the H1 is a category label, not an outcome. The subhead sits far right and below the H1 with a big gap. CTA "Let's Connect" is vague; no "Book a demo" or "See connections".
- Product /hapi-connectivity: strongest page. H1 "Connect once. Reach every system we support." plus plain-English subhead, CTA, and hotels/technology-provider routing links, illustration. Clear in 5 seconds.
- /connections: H1 "Hapi Connections" sits at 465px desktop (hero is mostly empty gradient); search box is below the fold on mobile (starts ~620px of 812). Primary utility (search for a connection) is not in first view.
- Resource article: H1 at 853px desktop and 464px mobile, i.e. pushed below the fold by a large hero/banner. There is also a second EMPTY H1 element (top 0).

## Interstitials
- Cookie banner is a bottom bar, dismissible (X). Not an intrusive modal. On mobile it covers ~20-25% of the viewport and overlaps the hero subhead text (product-mobile: subhead cut off by the banner) until dismissed. Medium.
- No newsletter popups or chat widgets observed in captured views.

## Mobile
- No horizontal overflow on connections (375/375), resource (375/375), product (390/390).
- Hamburger menu present. Mobile hero H1 is very large (product: 4 lines, ~65% of viewport) so CTA is below the fold on product-mobile; only the hero heading and the cookie banner are visible in first view. Home mobile H1/CTA position unverified.
- Tap targets: elements under 44px on a or button: connections 31/112 (28%), resource 31/96 (32%), product 32/87 (37%); desktop 36-50 of 87-133. Body font 14px on connections and resource pages (16px on the failed pages not measurable); below 16px base recommended.
- Cookie banner dismiss X is ~36px.

## Images
- Alt coverage: every img has an alt attribute but ALL are empty strings (alt=""): home 200/200, product 108/108, connections 131/131, resource 104/104. Empty alt is correct for decorative images only; logos (client logo strip, 130+ connection logos on /connections), hero illustration and article images need descriptive alt. Effectively 0% meaningful alt text.
- Volume: 100-200 <img> elements per page (heavy DOM; likely the cause of mobile home timeouts).
- Formats: AVIF dominant, plus WebP, SVG, PNG; JPG/JPEG still present on home and resource. Good modernization overall; residual PNG/JPG on home and article.
- Oversized: images with natural width over 2.2x rendered width: home 63, product 17, connections 20 (3 on mobile), resource 7 (4 on mobile). Home is the worst.
- Images score: 55/100 (modern formats good; alt text essentially absent; very high image count; oversized assets on home).

## Findings
### Critical
- C1. Intermittent origin/connection failures: Chromium on mobile profile timed out loading / (4 attempts) and /product/hapi-connectivity (once, then succeeded); curl returned HTTP 000 after 20s on / and the product page, then 200 in 3.1s minutes later. Crawlers and mobile users on slow networks may get timeouts. Needs server/CDN/TTFB investigation (3.1s TTFB observed on /).
### High
- H1. All image alt text empty on all four templates (see Images). Logos and the /connections directory (130+ logos) carry zero text signal for image search or integration-name queries.
- H2. Resource article H1 below the fold (853px desktop, 464px mobile) plus a stray empty second H1 element.
- H3. Mobile first view on product page is H1 plus cookie banner; CTA below fold; the cookie banner hides the subhead.
- H4. Home page weight: 200 img elements and 63 oversized images; likely cause of mobile load failures.
### Medium
- M1. Home H1 "Hospitality's Data Infrastructure" is category language; subhead is detached on the right. Add an outcome line and a more specific CTA ("See how it connects", "Book a demo").
- M2. /connections hero wastes first view; move the search box up (below fold on mobile).
- M3. Tap targets under 44px on roughly 30% of links/buttons on mobile; body text 14px.
- M4. Cookie banner covers 20-25% of mobile first view with no consent choice (single "you agree" notice, may matter for GDPR audiences).
### Low
- L1. Residual PNG/JPG on home and article pages; convert to AVIF/WebP.
- L2. Client logo marquee clips partial logos at both edges (decorative, minor).
- L3. Cookie dismiss button is ~36px.
