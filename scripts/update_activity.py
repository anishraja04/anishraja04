"""Refresh the live activity block and stat card in the profile README.

Pulls real data from the GitHub API and rewrites the region between the
HTML markers in README.md, plus a small SVG card. Writes nothing when the
content is unchanged, so this never manufactures contribution-graph
activity: a commit only lands when something real actually moved.

Run locally with a token:  GITHUB_TOKEN=... python scripts/update_activity.py
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

USER = "anishraja04"
ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CARD = ROOT / "assets" / "activity-card.svg"

START = "<!-- activity:start -->"
END = "<!-- activity:end -->"

API = "https://api.github.com"


def api(path: str, params: dict[str, str] | None = None) -> dict:
    url = f"{API}/{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-updater",
    })
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"GitHub API {e.code} on {path}: {e.read()[:300]!r}")


def is_public(repo: str, _cache: dict[str, bool] = {}) -> bool:
    """Whether a repository is public, cached per run.

    This runs with a token that can see private repositories, so the search
    results include work a visitor to the profile cannot and must not see.
    Private work here is contracted benchmark authoring: publishing a task
    title would leak the task itself and contaminate the benchmark it was
    written for. Anything not provably public is left out.
    """
    if repo not in _cache:
        try:
            _cache[repo] = not api(f"repos/{repo}").get("private", True)
        except SystemExit:
            _cache[repo] = False
    return _cache[repo]


def external_prs() -> list[dict]:
    """Public pull requests the user opened on repositories they do not own.

    Two filters, both deliberate. Self-PRs are not open-source contributions
    and padding the list with them is the kind of thing a reviewer notices.
    Private repositories are excluded for the confidentiality reason above.
    """
    found = api("search/issues", {
        "q": f"author:{USER} type:pr",
        "sort": "created",
        "order": "desc",
        "per_page": "100",
    })
    out, skipped = [], 0
    for item in found.get("items", []):
        repo = "/".join(item["repository_url"].split("/")[-2:])
        if repo.split("/")[0].lower() == USER.lower():
            continue
        if not is_public(repo):
            skipped += 1
            continue
        merged = bool(item.get("pull_request", {}).get("merged_at"))
        out.append({
            "repo": repo,
            "number": item["number"],
            "title": item["title"],
            "url": item["html_url"],
            "state": "MERGED" if merged else item["state"].upper(),
            "created": item["created_at"][:10],
        })
    if skipped:
        print(f"excluded {skipped} pull request(s) in private repositories")
    return out


def render_markdown(prs: list[dict]) -> str:
    by_repo: dict[str, list[dict]] = {}
    for pr in prs:
        by_repo.setdefault(pr["repo"], []).append(pr)

    merged = sum(1 for p in prs if p["state"] == "MERGED")
    open_ = sum(1 for p in prs if p["state"] == "OPEN")

    lines = [
        START,
        "",
        f"**{len(prs)} pull requests** to repositories I do not own "
        f"· {merged} merged · {open_} open",
        "",
    ]
    for repo, items in sorted(by_repo.items(), key=lambda kv: -len(kv[1])):
        lines.append(f"**[{repo}](https://github.com/{repo})**")
        lines.append("")
        for pr in sorted(items, key=lambda p: -p["number"]):
            lines.append(
                f"- [#{pr['number']} {pr['title']}]({pr['url']}) `{pr['state']}`")
        lines.append("")
    lines.append("<sub>Updated automatically from the GitHub API. "
                 "Self-authored pull requests are excluded.</sub>")
    lines.append("")
    lines.append(END)
    return "\n".join(lines)


def render_card(prs: list[dict], theme: str) -> str:
    merged = sum(1 for p in prs if p["state"] == "MERGED")
    open_ = sum(1 for p in prs if p["state"] == "OPEN")
    repos = len({p["repo"] for p in prs})
    stats = [(str(len(prs)), "pull requests"), (str(merged), "merged"),
             (str(open_), "open"), (str(repos), "repositories")]

    fg = "#e6edf3" if theme == "dark" else "#0f1012"
    dim = "#8b949e" if theme == "dark" else "#57606a"
    accent = "#3fb8af" if theme == "dark" else "#0b6477"

    cells = []
    for i, (value, label) in enumerate(stats):
        x = 20 + i * 150
        cells.append(
            f'  <text x="{x}" y="46" font-size="34" font-weight="700" '
            f'fill="{accent}" font-family="ui-monospace,monospace">{value}</text>\n'
            f'  <text x="{x}" y="70" font-size="13" fill="{dim}" '
            f'font-family="system-ui,-apple-system,Segoe UI,sans-serif">{label}</text>')

    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 92" width="620" '
        'height="92" role="img" aria-label="Open-source contribution summary">\n'
        f'  <title>{len(prs)} pull requests across {repos} repositories</title>\n'
        f'  <text x="20" y="20" font-size="12" fill="{fg}" letter-spacing="1.2" '
        'font-family="system-ui,-apple-system,Segoe UI,sans-serif">'
        'OPEN SOURCE</text>\n'
        + "\n".join(cells) + "\n</svg>\n")


def main() -> int:
    prs = external_prs()
    if not prs:
        print("no external pull requests found; leaving README untouched")
        return 0

    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        raise SystemExit(f"markers {START} / {END} missing from README.md")

    block = render_markdown(prs)
    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END), lambda _: block,
        readme, flags=re.S)

    changed = False
    if updated != readme:
        README.write_text(updated, encoding="utf-8")
        changed = True
        print(f"README updated with {len(prs)} pull requests")

    CARD.parent.mkdir(exist_ok=True)
    for theme in ("light", "dark"):
        path = CARD.with_name(f"activity-card-{theme}.svg")
        svg = render_card(prs, theme)
        if not path.exists() or path.read_text(encoding="utf-8") != svg:
            path.write_text(svg, encoding="utf-8")
            changed = True
            print(f"wrote {path.name}")

    if not changed:
        print("nothing changed; no commit needed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
