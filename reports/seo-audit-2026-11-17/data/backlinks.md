# Backlink profile: stayhapi.com (free sources only)

Date: 2026-11-17. Tier 0 (Common Crawl + verify crawler; no Moz/Bing/DataForSEO/Keywords Everywhere keys).
**Health score: INSUFFICIENT DATA.** Fewer than 4 scoring factors have data, so no numeric score is given.

## Data limits (read first)
- No referring-domain list, anchor text, spam score, or link velocity is available. None of the free sources provide them. Everything about who links to Hapi is unobserved, not "zero".
- Common Crawl (domain-level, confidence 0.50):
  - stayhapi.com and www.stayhapi.com: NOT in crawl or rankings (release cc-main-2026-jan-feb-mar). Absence means too new or small to appear. It is not evidence of no links.
  - hapicloud.io (legacy/developer domain): in crawl, PageRank 2.4e-08 (rank 1,875,037), harmonic centrality rank 11,221,676, 6 hosts. The tool reported release cc-main-2025-oct-nov-dec for this lookup, so this is older data. Very low authority.
- Verify crawler needs a known-link list; none was supplied, so nothing was verified.
- Site facts below come from direct fetches of www.stayhapi.com (Parsed, confidence 0.95).

## Observed on-site facts
- Canonical host is www.stayhapi.com (Webflow). robots.txt allows all. Sitemap has 246 URLs, 57 of them under /connections/.
- Tracker stack on the page: GA4, HubSpot, Hotjar, RB2B.
- /connections lists about 27 partner detail pages in the HTML sampled (agilysys, alliants, amica, asi-pms, aven-hospitality, aws, book4time, canary-technologies, capillary, clairvoyix, duve, eleven-wifi, flip-to, guesthub, helloshift, horizon-cdp, hotel-iq-decision-cloud, hotelkey, hudini-mobile-app, infor, juyo-analytics, kipsu, laso, loungeup, and others). The sitemap shows 57, so the page likely lazy-loads more.
- External links from /connections are only 5: developers.hapicloud.io (x4), careers.aquivalabs.com/hapi, LinkedIn company page, AWS Partner page (partners.amazonaws.com), and mrgnt.de. No outbound links to any partner's own site.
- Copy claims "around 100 hospitality technology providers", which is a lot of potential link counterparties.
- Brand/domain split: developer docs live on hapicloud.io while marketing is on stayhapi.com. Links to the old domain and a parent/agency (aquivalabs, mrgnt.de) may not pass equity to stayhapi.com. Unverified.

## Findings

### Critical
- **No measurable link authority and no data source to size the gap.** stayhapi.com is absent from the Common Crawl graph and hapicloud.io ranks in the millions. Evidence: CC lookups above. Action: connect a Moz key (free, 2,500 rows/mo) or run Bing Webmaster verification for stayhapi.com, and get Ahrefs/Semrush or Google Search Console "Links" export from the Hapi team. Without one of these, no link claim in the audit can be higher than hypothesis.

### High
- **Partner pages on /connections are one-way.** About 27+ partner pages exist, and the page has zero outbound partner links. Every partner (Canary, Agilysys, Infor, Duve, Kipsu, Flip.to, etc.) has a reason to list Hapi back, but nothing on the page prompts it. Action: for each /connections/<partner> page, send a standard "link back + co-marketing" ask to the partner's integrations/marketplace/partners page, with a ready-made logo/blurb/URL kit. Verify returns with the verify crawler (`verify_backlinks.py --target https://www.stayhapi.com/connections/<slug> --links file`).
- **Domain split dilutes equity.** Developer docs (developers.hapicloud.io) are linked from /connections four times. Developer docs are a prime link magnet (integration guides cited by partners). Action: confirm whether hapicloud.io 301s or cross-links to stayhapi.com, and consider consolidating or ensuring rel-canonical and prominent links to stayhapi.com. Needs a redirect and referrer check (not run here).

### Medium
- **Directory/marketplace gaps typical for the category (hypotheses, unverified against Hapi's actual profile):**
  - Cloud marketplaces: AWS Partner page already linked (observed). AWS Marketplace listing and Google Cloud / Azure partner directories not checked.
  - Hospitality bodies: HTNG (member directory, partner showcase), Hospitality Technology Next Gen events, Hotel Tech Report, Skift/PhocusWire/Hospitality Net press and vendor directories, HFTP, Hotel Tech Awards.
  - PMS vendor marketplaces/partner programs: Oracle OPERA Cloud / OHIP, Mews Marketplace, Cloudbeds, Apaleo Store, Infor, Agilysys, StayNTouch, RoomKeyPMS. Check which Hapi already appears in.
  - Review/software directories: G2, Capterra, GetApp, TrustRadius, Crunchbase, Product Hunt, AlternativeTo.
- **Press/news section exists but is unmeasured.** /resources has Press Releases and In The News categories. Action: list the outbound-linked coverage and check each article links to stayhapi.com (not hapicloud.io). Not done here.
- **Customer stories do not appear to drive reciprocal links** (no partner external links seen on the connections page). Action: add "link to your story" to the publishing checklist.

### Low
- **Anchor text:** not measurable. Recommendation for outreach: brand and descriptive anchors ("Hapi PMS integration", "Hapi connectivity") rather than exact-match "PMS middleware" to keep the profile natural.
- **Toxic link ratio:** no data. No evidence of spam either way. Revisit after a real link export.
- **Link velocity and geography:** no source (DataForSEO only). Skipped.
- Cross-skill: for crawlability/indexing of the 57 partner pages run `/seo technical https://www.stayhapi.com`; for E-E-A-T of partner pages run `/seo content`.

## Link-gap opportunity checklist (per /connections partner)
1. Partner's integrations/marketplace page lists Hapi with a link to the matching /connections/<slug>.
2. Partner's blog or press release announces the integration (co-authored where possible).
3. Hapi page links out to partner (reciprocal links are low value, so prioritize partner-origin links).
4. Joint case study hosted on partner's domain.
5. Partner's developer docs reference Hapi (links from docs carry weight).

## Scoring factors
Scored: none. Skipped: all seven (referring domains, quality, anchors, toxicity, velocity, follow ratio, geography) due to no data source.

## Next-best-action
Get a Search Console Links export from Hapi (reversible, free, minutes) or add a Moz key; then rerun this audit at Tier 1 and verify the 27-partner backlink ask list.
