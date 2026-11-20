# stayhapi.com performance audit (LAB DATA ONLY)

Date: 2026-11-17. Lighthouse 13.6.0, headless Chrome 150 (puppeteer chrome-headless-shell), simulated throttling, local machine. No CrUX/PSI field data (no API key; keyless PSI quota was exhausted). Lab numbers are not Google's pass/fail assessment. INP is not measurable in lab; TBT is the proxy.

**Lab performance score: ~70/100 (mobile-weighted).** Mobile 62-79, desktop 81-97.

## Results (Lighthouse score / LCP / TBT / CLS / transfer)

| Page | Mobile | Desktop |
|---|---|---|
| Home / | 78 / 4.1s / 190ms / 0.001 / 2.98MB | 93 / 1.6s / 0ms / 0.009 / 4.26MB |
| /product/hapi-guest-identity | 69, rerun 62 / 21.9s, rerun 18.0s / 200-360ms / 0.069, rerun 0.112 / 4.67MB | 81 (second run; first run NO_FCP, unreliable) / 3.5s / 0ms / 0.001 / 3.4MB images+ |
| /resources/the-integration-layer-... | 65 / 11.5s / 200ms / 0 / 1.61MB | 89 / 1.8s / 0ms / 0.001 / 2.52MB |
| /connections/agilysys | 67, rerun 79 / 12.4s, rerun 4.4s / 120-170ms / 0 / 1.60MB | 97 / 0.9s / 0ms / 0 / 1.62MB |

Caveats: mobile LCP swings wildly run to run (Agilysys 12.4s vs 4.4s) and observed LCP subparts total ~1-1.3s versus simulated 11-22s, so treat mobile LCP as directional. Only the product page's slowness (2.9MB GIF, CLS) repeated. Page counts: 1 per type, 1-2 runs each. Other /product, /resources, /connections pages are unmeasured. Desktop product first run failed (NO_FCP), consistent with the known origin timeouts under load.

## Core Web Vitals status (lab, indicative)
- LCP: mobile fail on product/resource/connections (>4s) in most runs; homepage borderline (4.1s). Desktop pass.
- INP proxy (TBT): mobile 120-360ms (needs improvement); desktop 0ms.
- CLS: pass everywhere except product page mobile (0.069-0.112; culprit `div#hotels.section_point`).
- TTFB: 18-77ms on CDN (good). Not a problem except intermittent origin timeouts reported elsewhere.

## Third-party cost (mobile, main-thread ms / transfer)
- Google reCAPTCHA (gstatic): 78-90ms main thread, ~394KB, loaded on every page including non-form pages. Largest 3P cost; bootup 490-550ms in throttled runs.
- Hotjar: 15-75ms, 64KB.
- Google Tag Manager/gtag (G-FPMZ1YCDKZ): ~27ms, 177KB.
- HubSpot (hs-scripts 45670509, hs-analytics, hsappstatic, usemessages chat): ~20+17+5ms, ~195+49+31KB combined ~275KB. Chat (usemessages) loads on all pages.
- jsDelivr swiper@11 (21 requests, ~83KB) plus unpkg swiper@9 on home: swiper loaded twice at two versions.
- Webflow chunk `webflow.schunk.a5b1...js`: 220-1900ms bootup (largest first-party script cost on home mobile).
- Total JS ~1.1MB transferred per page; ~600-650KB estimated unused.

## Findings

### Critical
1. LCP image is `loading="lazy"` with no `fetchpriority` on every page measured (home, product, resource, connections; Lighthouse lcp-discovery fails priorityHinted and eagerlyLoaded). Matches the known homepage finding. Fix: set hero/LCP image to eager + fetchpriority=high in Webflow image settings; keep lazy below the fold.
2. Product page ships a 2.88MB animated GIF (`Hapi_Guest_Identity_flow (1).gif`), ~2.8MB wasted; page 4.7MB, mobile LCP 18-22s, score 62-69. Replace with MP4/WebM (autoplay muted loop) or Lottie, ~90% smaller.

### High
3. Render-blocking resources on every page: webfont.js (Google), jQuery (cloudfront), two swiper builds (jsDelivr + unpkg), Webflow chunks and shared CSS. Lighthouse estimates 450-480ms savings desktop, 1.1-2.2s mobile. Fix: drop WebFont Loader for plain CSS `font-display: swap`, load swiper only on pages with sliders, remove duplicate swiper@9, self-host or defer.
4. Oversized PNGs: homepage `Tech Providers-min.png` 1.0MB (about 984KB wasted on desktop), `Frame 2147225990.png` 125KB; resource thumbnails 424KB, 300KB, 131KB PNG (~800KB wasted). Convert to AVIF/WebP and use the responsive variants Webflow generates (`-p-800`); desktop is serving originals. Aligns with the known 63 oversized images.
5. reCAPTCHA (~394KB, 80-90ms main thread) loads sitewide. Load only on pages with forms, or on first form interaction.
6. Product page CLS 0.069-0.112 (borderline fail on rerun); shift source `#hotels.section_point`. Reserve height/aspect-ratio; ties to the known 180 images missing width/height.

### Medium
7. Mobile TBT 120-360ms from Webflow chunk, reCAPTCHA, HubSpot analytics, Hotjar; INP risk on mobile. Delay Hotjar and HubSpot chat until after first interaction/idle; confirm GTM is not also loading duplicate HubSpot/GA tags.
8. ~600-650KB unused JavaScript and 70-90KB unused CSS per page (Webflow shared bundle). Limit site-wide interactions/libraries.
9. 20+ requests to jsDelivr per page (swiper modules?), plus 3 font hosts: consolidate, preconnect to cdn.prod.website-files.com and fonts.gstatic.com.
10. Cache policy: ~230-300KB flagged for short TTL (third-party scripts); Webflow assets are fine (immutable, 1 year, CF HIT).

### Low
11. Font display: 50-420ms estimated savings; use font-display swap/optional.
12. Small PNG/AVIF trust badges (PCI, SOC) 5-10KB each with ~95% waste; ship correctly sized.
13. Cookie banner (Finsweet) text causes micro shifts (<0.001): ignore.

## Not measured
Other product/resource/connection pages; field data (CrUX); real INP; repeat runs beyond noted; behavior under production load. Origin timeouts reported by others are consistent with the NO_FCP failures I saw twice (d-product, early home runs) and are a reliability risk beyond these numbers.
