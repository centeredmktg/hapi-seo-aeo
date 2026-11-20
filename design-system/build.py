#!/usr/bin/env python3
"""Build a self-contained Hapi report: inline the DS stylesheet into a source page.

Usage: python3 design-system/build.py reports/<name>/report.src.html
Writes reports/<name>/dist/<name>.html, a single file you can email, drop in
Drive/Slack, or print to PDF.

Source pages are plain HTML using DS classes, plus directives:
  {{pagemap:data/file.txt}}  one dot per page from a title-check file
                             (lines: "TITLE_EMPTY|TITLE_OK ... <url>" or "FAIL <code> <url>")
"""
import html
import re
import sys
from collections import OrderedDict
from pathlib import Path

DS = Path(__file__).resolve().parent
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">')


def pagemap(src_dir: Path, rel: str) -> str:
    groups: "OrderedDict[str, list]" = OrderedDict()
    for line in (src_dir / rel).read_text().splitlines():
        parts = line.split()
        if not parts:
            continue
        url = parts[-1]
        state = "fail" if parts[0] == "FAIL" else ("empty" if parts[0] == "TITLE_EMPTY" else "ok")
        m = re.search(r"stayhapi\.com/([^/]+)/", url)
        section = "/" + (m.group(1) if m else "other")
        groups.setdefault(section, []).append((state, url))

    out = ['<div class="pagemap" role="group" aria-label="Every CMS page by title status">']
    for section, pages in groups.items():
        pages.sort(key=lambda p: {"empty": 0, "fail": 1, "ok": 2}[p[0]])
        empty = sum(1 for s, _ in pages if s == "empty")
        out.append('<div class="pagemap__group">')
        out.append(f'<div class="pagemap__label"><strong>{section}</strong>'
                   f'<span>{empty} of {len(pages)} with no title</span></div><div class="dots">')
        for state, url in pages:
            label = {"empty": "no title", "ok": "has title", "fail": "did not load"}[state]
            slug = html.escape(url.rsplit("/", 1)[-1])
            out.append(f'<span class="dot dot--{state}" title="{slug}: {label}"></span>')
        out.append("</div></div>")
    out.append('<div class="legend">'
               '<span><i class="dot dot--empty"></i>No title or description</span>'
               '<span><i class="dot dot--ok"></i>Has a title</span>'
               '<span><i class="dot dot--fail"></i>Did not load (rate limited)</span></div></div>')
    return "\n".join(out)


def build(src: Path) -> Path:
    page = src.read_text()
    page = re.sub(r"\{\{pagemap:([^}]+)\}\}", lambda m: pagemap(src.parent, m.group(1).strip()), page)
    css = (DS / "hapi-ds.css").read_text()
    page = page.replace("<!--DS-->", FONTS + "<style>\n" + css + "\n</style>")
    name = src.parent.name
    out = src.parent / "dist" / f"{name}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page)
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    print(build(Path(sys.argv[1]).resolve()))
