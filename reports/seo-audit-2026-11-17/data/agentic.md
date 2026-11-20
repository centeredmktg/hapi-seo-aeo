# Agent-readiness audit: https://www.stayhapi.com (2026-11-17)

Scope: Webflow + HubSpot B2B SaaS. Tools: lighthouse_agentic.py, agentic_check.py, agent_ux_check.py (homepage and /contact-us). No agent UA matrix run (not authorized).

## Scores
- Lighthouse Agentic Browsing: NOT RUNNABLE. PSI returned HTTP 429 (daily quota, no API key) for both mobile and desktop. No X/N reported. Fix: configure a Google API key (/seo google setup) and re-run.
- Agent-UX heuristic (separate from Lighthouse, status complete): homepage 72/100, /contact-us 80/100.
- Local agentic_check: no failures. Mostly absent optional layers.

## Agent-UX evidence
- Homepage: 1321 a11y nodes, 81 interactive, 7 unnamed interactive nodes, 2 inputs without label[for], 132 real anchors, 5 landmarks, 0 div-onclick widgets.
- /contact-us: 314 nodes, 41 interactive, 4 unnamed interactive nodes, 2 inputs without label[for].
- Contact page static HTML has only the footer Newsletter form (wf-form-Newsletter-form). Labels are mostly present, but the "Last Name" label has for="email" while its input is id="Last-Name" (wrong association; the "Name" input also has id="name", fine). Placeholders are empty.
- The demo/contact form is a HubSpot embed (hs-form-frame, data-form-id 3ec0712c-..., def1c2ee-...; hsforms.net embed). It is injected client-side and was not in the static HTML, so I could not verify its field labels or operability. Treat as unverified; needs a live a11y-tree check of the rendered HubSpot form (iframe vs. non-iframe embed matters for agents).

## Findings

### Critical
None found.

### High
1. Lighthouse not measured (PSI quota). Evidence: HTTP 429 x2. Fix: add API key, re-run, report X/N with version and form factor.
2. Unnamed interactive elements: 7 on homepage, 4 on /contact-us (-20 / -12 points). Agents click by accessible name; unnamed buttons/links (likely icon-only links, social, carousel controls) are invisible. Fix: add aria-label or visible text in Webflow element settings.
3. No developer docs / API discoverability from the marketing site. Homepage links point to product pages (/product/hapi-connectivity, hapi-autopilot, hapi-data-lakehouse, hapi-guest-identity) and case studies; no link to docs, API reference, developer portal or GitHub found in homepage links, and no api/docs/developers path in the sitemap. docs./developers./api. subdomains did not resolve in my probes (network was flaky, so verify manually). For an integration company this is the largest agent gap: an agent asked "does Hapi have an API for X PMS / what is the data model" has nothing to read. Fix: publish public docs or at least a public /developers page with the common data model, supported PMS/connector list, auth approach, and link it from nav and sitemap.

### Medium
4. Label defect: "Last Name" label for="email" does not match its input id Last-Name; also two fields labeled inconsistently ("Name" vs last name). Fix in Webflow form field IDs. (-8)
5. HubSpot demo form unverified for agents (see above). Add visible labels, required markers, and an accessible success/error state; consider a plain HTML fallback or a direct scheduling link.
6. Staging asset naming: CSS served from "staging-hapi-website2.webflow.shared..." files and robots.txt response carries x-robots-tag: noindex. The noindex on the robots.txt file itself is normal Webflow behavior and harmless; I could not re-verify homepage headers or meta robots (probe timed out), so confirm the homepage is not noindex.
7. robots.txt is a single "User-agent: *  Disallow:" group with a Sitemap line. No statement of policy for training vs search vs user agents. Not a defect, but there is no deliberate position.

### Low (opportunities, not defects)
8. No Content-Signal line (draft/proposal, Cloudflare Content Signals Policy; checked 2026-09-23). Optional, e.g. search=yes, ai-input=yes, ai-train=<your call>.
9. No /llms.txt or /llms-full.txt (404; Lighthouse drops the audit from the fraction when absent, a valid one would add a counted pass). Hapi has strong content to point at: product pages, case studies, connector list.
10. No Markdown delivery: Accept negotiation returns HTML (Vary: Accept present), no rel=alternate markdown, /index.md is 404.
11. No WebMCP (W3C CG draft, not a standard; WebKit opposes; checked 2026-09-23): 0 registerTool calls, 0 annotated forms. Only form in static HTML is the newsletter form. Do not annotate lead forms casually.
12. No ai-catalog.json (ARD 1.0 draft), api-catalog (RFC 9727), OAuth metadata, or A2A agent card in /.well-known (all 404, correctly N/A today). If Hapi publishes a public API or MCP server, api-catalog and ai-catalog.json become relevant.

### Passing
- Server-rendered: 2355 words without JS, no JS shell.
- robots.txt reachable (200); real 404 for unknown URLs (no soft-404); sitemap.xml 200.
- No AI crawler blocked.

## Access policy lines (all via the * group, Disallow empty = allow all)
- Training (GPTBot, ClaudeBot etc.): allowed, no stated preference.
- Search (OAI-SearchBot, Claude-SearchBot etc.): allowed.
- User-triggered (ChatGPT-User, Claude-User, Perplexity-User): allowed; vendor behavior varies (ChatGPT-User may not apply robots, Claude-User honours, Perplexity-User generally ignores).

## Standards status (checked 2026-09-23 per vendor-matrix)
WebMCP, Content-Signal, ai-catalog.json (ARD) are drafts/proposals. llms.txt is a community spec; Google Search ignores it. No ranking, citation or traffic effect is promised by any item here.

## Recommended order
1) PSI key and Lighthouse rerun. 2) Name the 7+4 unnamed controls. 3) Live-check HubSpot form accessibility. 4) Developer docs hub linked from nav. 5) llms.txt pointing at product, connector and docs pages. 6) Optional Content-Signal.
