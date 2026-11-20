# Hapi SEO + AEO workspace

This repo holds the day-one SEO/AEO baseline for stayhapi.com and everything needed to move it forward. Read this file first, then `reports/seo-audit-2026-11-17/data/2026-11-17-hapi-seo-audit-report.md` for the full synthesis.

**Owner:** Danny Cox, Head of Marketing (started 2026-11-16).
**First assignment:** the AEO question: how Hapi shows up when buyers ask AI engines (ChatGPT, Perplexity, Google AI Overviews, Copilot) about hotel data and integration platforms.

---

## Where things stand (2026-11-17, outside-in)

- **SEO health: 49/100.** Eleven checks covering all 246 sitemap URLs. No Search Console, GA4 or HubSpot data yet; those come next.
- **Root cause:** two Webflow CMS templates (`/resources`, `/connections`) were never finished.
  - 146 of 223 CMS pages publish with an empty `<title>` and meta description.
  - The per-URL list is in `data/cms-title-check.txt`.
- **The site's writing and positioning are not the main problem.** The product pages are specific and quotable. The IHG customer story has hard numbers (3,600+ hotels, checkout success 90% → 97%), but it's one of the pages with no title.

## AEO findings (the first assignment)

From `data/geo.md` (AI search readiness 49/100) and `data/agentic.md`:

1. **Brand ambiguity.**
   - On Bing, "Hapi" ranks stayhapi.com #5, behind an investing app and the Egyptian god.
   - "stayhapi" surfaces an unrelated company (stay.hapibenefits.com).
   - The site has no Organization markup, so AI engines get no `alternateName` or `sameAs` signals.
   - The name appears as Hapi, HAPI, "Hapi (Hotel API)", Data Travel, and LinkedIn's "hapicloud".
2. **Nothing quotable on the money pages.** The product pages use taglines rather than "Hapi is X" definitions. There are no statistics and no 130–170-word answer blocks.
3. **The best citation asset is empty.** `/resources/the-2026-pms-api-study` publishes as a headline with no findings. Original data is what AI engines cite.
4. **Hapi's authority shows up on other people's domains.**
   - Syndicated press copies (Hospitality Net, Hotel-Online, Hotel Tech Report) appear for 4 of 6 category queries tested.
   - The hoteltech.review "Hotel API Integration Platforms 2026" list names Hapi first, with no link.
5. **The category language is split five ways:** connectivity partner, data infrastructure, data-integrations platform, cloud data hub, PMS middleware. AI answers need one consistent description to repeat. See `context/positioning.md`: this is an open decision, and Danny owns it.
6. **Crawler access is mostly fine.**
   - Search-relevant AI crawlers (OAI-SearchBot, Claude-SearchBot, PerplexityBot) get a 200.
   - Bytespider gets a 403, so confirm whether that's intentional.
   - There's no llms.txt and no stated AI policy in robots.txt.
7. **Not yet measured:** live answers in ChatGPT, Perplexity and AI Overviews. Search engines blocked the automated checks. Do this by hand or with a tracking tool.

**AEO work in order:**
- Bind the CMS titles.
- Add sitewide Organization JSON-LD (snippet in `data/schema.md`) and a "Hapi is…" first paragraph, once the category is decided.
- Publish the PMS API Study findings as HTML.
- Adopt a publish-first syndication rule.
- Write answer pages for "PMS middleware" and "integration platform" searches.
- Track a fixed prompt set in AI engines monthly.

## Rules for working here

- **Facts come from evidence.** Every number in the report traces to a file in `reports/seo-audit-2026-11-17/data/`. When Search Console or GA4 data arrives, it replaces estimates. Note what changed rather than silently overwriting.
- **Scope of edits.** Read the live site and Webflow freely. Changes to Webflow go in as drafts or staged changes and need Danny's approval. Never publish or delete CMS items.
- **Don't name employees outside leadership, and don't paste customer data into prompts** beyond what a task needs.
- **Writing:** plain verbs, sentence case, no em dashes, no hype. Run `humanizer` (hapi-kit) on anything team-facing.

## Tools

- **hapi-kit plugin (v1.4.1).** Skills for messaging, content QA and briefs. The ones used most here:
  - `cms-content-qa`: re-run the title and body check. Use sitemap mode now, and Webflow mode once there's a token.
  - `content-brief` and `content-draft`.
  - `fact-check` and `humanizer`.
- **seo-suite (claude-seo, via the hapi-kit marketplace).**
  - `/seo audit https://www.stayhapi.com` re-runs the full audit.
  - `/seo google` adds Search Console, CrUX and GA4 data once credentials are set.
  - `/seo drift baseline` snapshots the site so later changes can be measured.
- **Report design system (`design-system/`).** Hapi's colors and fonts, taken from the site's own CSS. See `design-system/README.md`.

### Rebuild the shareable report

```bash
python3 design-system/build.py reports/seo-audit-2026-11-17/report.src.html
# → reports/seo-audit-2026-11-17/dist/seo-audit-2026-11-17.html (single file; email, Drive, or print to PDF)
```

### Re-run the title check (from hapi-kit)

```bash
python3 -I <hapi-kit>/skills/cms-content-qa/scripts/cms_qa.py sitemap https://www.stayhapi.com \
  --include /resources/ --include /connections/ --workers 2
```

Keep workers low: stayhapi.com rate-limits bursts. That's also worth checking against Googlebot in Search Console crawl stats.

## Next steps when first-party data arrives

1. **Search Console.** Pull queries, pages, indexing, crawl stats and links. This settles:
   - where Hapi actually ranks on Google (Bing and the other tool disagreed);
   - whether Googlebot hits the same rate limits.
2. **GA4 and HubSpot.** Find which pages produce demo requests. Re-weight the fix list toward pages that convert.
3. **Update `report.src.html`.** Turn each "we'll know it worked" line into a numeric target, then rebuild.

## Files

| Path | What |
|---|---|
| `reports/seo-audit-2026-11-17/data/2026-11-17-hapi-seo-audit-report.md` | Full synthesis: scores, findings, 30/60/90 |
| `reports/seo-audit-2026-11-17/data/*.md` | One file per check: technical, content, schema (with JSON-LD), sitemap, sxo, clusters, geo, agentic, visual, performance, backlinks |
| `reports/seo-audit-2026-11-17/data/cms-title-check.txt` | Per-URL title/description status |
| `reports/seo-audit-2026-11-17/screenshots/` | Desktop and mobile captures, 2026-11-17 |
| `reports/seo-audit-2026-11-17/report.src.html` → `dist/` | Team-facing report |
| `context/positioning.md` | Category and positioning hypotheses (open decision) |
| `context/positioning-interview-guide.md` | Customer interview guide for the category question |
| `context/content-operations.md` | Content defects mapped to the missing process steps; draft SOP |
| `design-system/` | Report CSS and build script |
