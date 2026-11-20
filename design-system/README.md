# Hapi Report DS

A light design system for internal reports and plans. Tokens come from stayhapi.com's live Webflow stylesheet, so reports look like Hapi without anyone touching the website.

## Build a report

1. Create `reports/<yyyy-mm-dd-name>/report.src.html`. Copy `reports/seo-audit-2026-11-17/report.src.html` as the starting point.
2. Put `<!--DS-->` in `<head>`.
3. Run `python3 design-system/build.py reports/<name>/report.src.html`.
4. Share `reports/<name>/dist/<name>.html`. It's a single file: email it, drop it in Drive or Slack, or print it to PDF (the print styles are included).

## Tokens

| Token | Hex | Source in site CSS | Use |
|---|---|---|---|
| `--ink` | `#040447` | `--dark-blue` | Headings, critical, masthead |
| `--periwinkle` | `#9eb1e5` | `--light-green` (misnamed) | High severity, accents, focus ring |
| `--mist` | `#d3d9f1` | `--blue-light` | Medium severity, masthead text |
| `--mint` | `#c4efda` | `--blue` (button fill) | Done, good news, the one positive callout |
| `--paper` | `#fffdf8` | `--grey` (warm white) | Page background |

- **Type.** Gilroy (400/500/600) is loaded from Hapi's own Webflow CDN, with Instrument Sans from Google Fonts for body text.
- **Shape.** 32px corners on panels, 20px on blocks, pills for chips. The site uses the same.

**Severity is depth of blue:** ink (critical), periwinkle (high), mist (medium), outline (low), mint (done). Hapi's palette has no red, and these reports go to the people who built the thing being audited.

## Components

| Component | Class | What it's for |
|---|---|---|
| Masthead | `.masthead` | Navy band with the site's periwinkle glow. Write the headline as the finding, not a label. |
| Page map | `{{pagemap:data/file.txt}}` | One dot per page from a title-check file. Generalize the same pattern for any "N of M" finding. |
| Finding | `.finding.finding--critical` | Severity rail. `.finding__facts` holds effort, how we'll know it worked, and what it unblocks. |
| Scorecard | `.scores` + `.bar` | Score table with inline bars. |
| Facts row | `.facts` + `.fact` | At most one per report. |
| Phases | `.phases` + `.phase` | Real sequences only (30/60/90). The first phase is filled to mark "now". |
| Callout | `.callout`, `.callout--mint` | Mint is for the single most important insight. |

## Rules

- **Spend boldness once per report.** Use one signature visual and keep everything else quiet.
- **Number things only when they're a sequence.**
- **Write headlines as the claim, in sentence case.**
- **Copy:** plain verbs, no em dashes, no AI tells. Run humanizer on long text.
