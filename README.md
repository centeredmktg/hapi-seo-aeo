# Hapi SEO + AEO

The day-one search baseline for stayhapi.com (2026-11-17), the team-facing report, and the working notes for the next phase: AI answer engine visibility.

- **Read the report:** open `reports/seo-audit-2026-11-17/dist/seo-audit-2026-11-17.html` in a browser.
- **Working with Claude:** start Claude Code in this folder. It reads `CLAUDE.md` first.
- **Rebuild the report after edits:** `python3 design-system/build.py reports/seo-audit-2026-11-17/report.src.html`

## Setup on a new machine

```bash
git clone <this repo> hapi-seo-aeo && cd hapi-seo-aeo
# Skills: hapi-kit (includes the seo-suite marketplace entry)
git clone --branch v1.4.1 https://github.com/centeredmktg/hapi-kit.git ~/hapi-kit
claude plugin marketplace add ~/hapi-kit
claude plugin install hapi-kit@hapi-kit
claude plugin install seo-suite@hapi-kit    # for /seo audit, /seo google, /seo drift
```

The audit needs only Python 3 (standard library). The `/seo` tools set up their own runtime on first use (`/seo setup`).

Owner: Danny Cox, Head of Marketing.
