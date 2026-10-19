#!/usr/bin/env python3
"""
Generate README.md and language SVG distribution cards from README.template.md and data/projects.json.
Modeled after the build pipeline of yenharvey/yenharvey.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "README.template.md"
OUTPUT = ROOT / "README.md"
PROJECTS = ROOT / "data" / "projects.json"
CACHE = ROOT / "data" / "stats.json"

TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")

# Language color mappings matching GitHub linguist colors
LANG_COLORS = {
    "Rust": "#dea584",
    "C++": "#f34b7d",
    "C": "#555555",
    "Kotlin": "#A97BFF",
    "Python": "#3572A5",
    "Shell": "#89e051",
    "PowerShell": "#012456",
    "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Dockerfile": "#384d54",
    "Other": "#8b949e",
}

def log(msg: str) -> None:
    print(f"[build_readme] {msg}", file=sys.stderr, flush=True)

def api_get(endpoint: str) -> dict | list | None:
    url = f"https://api.github.com{endpoint}" if endpoint.startswith("/") else endpoint
    headers = {"User-Agent": "pinchiu-profile-generator", "Accept": "application/vnd.github.v3+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            link = resp.headers.get("Link", "")
            data = json.loads(resp.read().decode("utf-8"))
            return data, link
    except Exception as exc:
        log(f"API request failed for {url}: {exc}")
        return None, ""

def fmt_number(n: int) -> str:
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}k"
    return str(n)

def collect_stats(cache: dict) -> dict:
    if not PROJECTS.exists():
        return cache

    projects_config = json.loads(PROJECTS.read_text(encoding="utf-8"))
    stats_projects = cache.get("projects", {})
    stats_languages = cache.get("languages", {"repos": 0, "bytes": {}})

    lang_bytes_total: dict[str, int] = {}
    repos_counted = set()

    for proj_id, info in projects_config.items():
        log(f"Processing project: {proj_id}")
        commits_sum = 0
        proj_repos = info.get("repos", [])

        for repo in proj_repos:
            repos_counted.add(repo)
            # 1. Fetch commits count
            data, link = api_get(f"/repos/{repo}/commits?per_page=1")
            commit_count = 1
            if link and "rel=\"last\"" in link:
                m = re.search(r"[?&]page=(\d+)[^>]*>;\s*rel=\"last\"", link)
                if m:
                    commit_count = int(m.group(1))
            commits_sum += commit_count

            # 2. Fetch language breakdown
            lang_data, _ = api_get(f"/repos/{repo}/languages")
            if isinstance(lang_data, dict):
                for lang, b in lang_data.items():
                    lang_bytes_total[lang] = lang_bytes_total.get(lang, 0) + b

        if commits_sum > 0:
            stats_projects[proj_id] = {
                "commits": commits_sum,
                "scale": info.get("scale", f"{commits_sum} commits"),
            }

    if lang_bytes_total:
        stats_languages = {
            "repos": len(repos_counted),
            "bytes": lang_bytes_total,
        }

    return {
        "projects": stats_projects,
        "languages": stats_languages,
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }

def render_language_card(langs: dict, dark: bool) -> str:
    """Renders a standalone responsive SVG card showing language distribution."""
    fg = "#e6edf3" if dark else "#1f2328"
    muted = "#8b949e" if dark else "#59636e"
    bg = "#161b22" if dark else "#f6f8fa"
    border = "#30363d" if dark else "#d0d7de"

    bytes_map = langs.get("bytes", {})
    total = sum(bytes_map.values()) or 1
    sorted_items = sorted(bytes_map.items(), key=lambda kv: -kv[1])

    top = sorted_items[:7]
    other_bytes = total - sum(n for _, n in top)
    if other_bytes > 0:
        top.append(("Other", other_bytes))

    width, pad = 860, 28
    bar_w = width - pad * 2
    rows = (len(top) + 1) // 2
    height = 95 + rows * 28 + 15

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-sans-serif, -apple-system, \'Segoe UI\', Helvetica, Arial, sans-serif">',
        f'<rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="12" fill="{bg}" stroke="{border}"/>',
        f'<text x="{pad}" y="38" font-size="18" font-weight="700" fill="{fg}">Languages &amp; Code Distribution</text>',
        f'<text x="{width-pad}" y="38" font-size="13" text-anchor="end" fill="{muted}">{langs.get("repos", 7)} public repositories · {fmt_number(total)} bytes analyzed</text>',
        f'<clipPath id="lang-bar"><rect x="{pad}" y="54" width="{bar_w}" height="12" rx="6"/></clipPath>'
    ]

    # Stacked progress bar
    curr_x = float(pad)
    for lang, n in top:
        seg_w = max(bar_w * (n / total), 2.0)
        color = LANG_COLORS.get(lang, "#8b949e")
        out.append(f'<rect x="{curr_x:.1f}" y="54" width="{seg_w:.1f}" height="12" fill="{color}" clip-path="url(#lang-bar)"/>')
        curr_x += seg_w

    # Legend items (2 columns)
    col_w = bar_w // 2
    for i, (lang, n) in enumerate(top):
        col = i % 2
        row = i // 2
        lx = pad + col * col_w
        ly = 98 + row * 28
        color = LANG_COLORS.get(lang, "#8b949e")
        pct = (n / total) * 100
        out.append(f'<circle cx="{lx+6}" cy="{ly-4}" r="5.5" fill="{color}"/>')
        out.append(f'<text x="{lx+22}" y="{ly}" font-size="13" font-weight="600" fill="{fg}">{lang}</text>')
        out.append(f'<text x="{lx+160}" y="{ly}" font-size="13" fill="{muted}">{pct:.1f}%</text>')
        out.append(f'<text x="{lx+240}" y="{ly}" font-size="13" fill="{muted}">{fmt_number(n)}B</text>')

    out.append("</svg>\n")
    return "\n".join(out)

def render_template(stats: dict) -> str:
    template_text = TEMPLATE.read_text(encoding="utf-8")
    replacements: dict[str, str] = {
        "updated_at": stats.get("updated_at", datetime.now(timezone.utc).strftime("%Y-%m-%d")),
        "languages.repos": str(stats.get("languages", {}).get("repos", 7)),
    }

    projects_stats = stats.get("projects", {})
    for proj_id, pdata in projects_stats.items():
        replacements[f"{proj_id}.commits"] = str(pdata.get("commits", 0))
        replacements[f"{proj_id}.scale"] = str(pdata.get("scale", ""))

    def replace_match(m: re.Match) -> str:
        key = m.group(1).strip()
        return replacements.get(key, "—")

    return re.sub(r"\{\{\s*([\w.]+)\s*\}\}", replace_match, template_text)

def main() -> int:
    cache: dict = {}
    if CACHE.exists():
        try:
            cache = json.loads(CACHE.read_text(encoding="utf-8"))
        except Exception as e:
            log(f"Failed to read cache: {e}")

    if "--from-cache" in sys.argv and cache:
        log("Rendering from existing cache...")
        stats = cache
    else:
        stats = collect_stats(cache)

    CACHE.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Render README.md
    if TEMPLATE.exists():
        rendered = render_template(stats)
        OUTPUT.write_text(rendered, encoding="utf-8")
        log(f"Successfully generated {OUTPUT.name}")

    # Render Dark & Light Language Cards
    langs_info = stats.get("languages", {})
    if langs_info and "bytes" in langs_info:
        dark_card = render_language_card(langs_info, dark=True)
        (ROOT / "assets" / "languages-dark.svg").write_text(dark_card, encoding="utf-8")
        light_card = render_language_card(langs_info, dark=False)
        (ROOT / "assets" / "languages-light.svg").write_text(light_card, encoding="utf-8")
        log("Successfully rendered assets/languages-dark.svg and assets/languages-light.svg")

    return 0

if __name__ == "__main__":
    sys.exit(main())
