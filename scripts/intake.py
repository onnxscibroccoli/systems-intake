#!/usr/bin/env python3
"""Daily intake: read upstreams, write English briefs, fork when a token may."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ROOT / "intake" / "targets.json"
MIRRORS = ROOT / "mirrors"
DOCS = ROOT / "docs"
CATALOG = ROOT / "catalog"
API = "https://api.github.com"
NAME_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
PERMISSIVE = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "Unlicense", "CC0-1.0"}
CJK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af\u0400-\u04ff]")


def token() -> str:
    return os.environ.get("INTAKE_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""


def intake_token() -> str:
    return os.environ.get("INTAKE_TOKEN") or ""


def owner() -> str:
    return os.environ.get("OWNER") or "onnxscibroccoli"


def request(method: str, url: str, body: dict | None = None, tok: str | None = None, accept: str = "application/vnd.github+json"):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", accept)
    req.add_header("User-Agent", "systems-intake")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    auth = tok if tok is not None else token()
    if auth:
        req.add_header("Authorization", f"Bearer {auth}")
    if body is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as res:
            raw = res.read()
            if not raw:
                return {}
            text = raw.decode(errors="replace")
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                return text
    except urllib.error.HTTPError as err:
        detail = err.read().decode(errors="replace")[:500]
        raise RuntimeError(f"{method} {url} -> {err.code} {detail}") from err


def load_targets() -> dict:
    data = json.loads(TARGETS.read_text())
    for item in data["targets"]:
        if not NAME_RE.match(item["upstream"]):
            raise SystemExit(f"bad upstream name: {item['upstream']}")
    return data


def repo_meta(full: str) -> dict:
    return request("GET", f"{API}/repos/{full}")


def readme_text(full: str) -> str:
    try:
        payload = request(
            "GET",
            f"{API}/repos/{full}/readme",
            accept="application/vnd.github.raw",
        )
    except RuntimeError:
        return ""
    if isinstance(payload, str):
        return payload
    # raw accept sometimes still returns JSON depending on the server
    if isinstance(payload, dict) and "content" in payload:
        return base64.b64decode(payload["content"]).decode(errors="replace")
    return ""


def license_spdx(meta: dict, expected: str) -> str:
    lic = (meta.get("license") or {}).get("spdx_id") or "NONE"
    if lic in PERMISSIVE:
        return lic
    if expected in PERMISSIVE and lic in {"NOASSERTION", "NONE"}:
        # The target file recorded a license we already read from the LICENSE file.
        return expected
    return lic


def cjk_lines(text: str) -> list[str]:
    lines = []
    for line in text.splitlines():
        if CJK_RE.search(line):
            lines.append(line.strip())
    return lines[:40]


HAND_PHRASES = (
    ("中文介绍", "Chinese introduction"),
    (
        "二重スケジューリングを不要にする新しいExecutorとスケジューリング理論",
        "a new executor and a scheduling theory that removes the need to schedule the same work twice",
    ),
)


def hand_translate(lines: list[str]) -> list[dict]:
    blocks = []
    for line in lines:
        english = ""
        if "中文介绍" in line:
            english = (
                "Chinese introduction. The source line is a badge linking to a WeChat article. "
                "The original characters stay in the image address so the link still works."
            )
        else:
            english_line = line
            replaced = False
            for src, dst in HAND_PHRASES:
                if src == "中文介绍":
                    continue
                if src in english_line:
                    english_line = english_line.replace(src, dst)
                    replaced = True
            if replaced:
                english = english_line
        blocks.append({"source": line, "english": english})
    return blocks


def translate_lines(lines: list[str]) -> list[dict]:
    if not lines:
        return []
    known = hand_translate(lines)
    if all(block["english"] for block in known):
        return known
    key = os.environ.get("XAI_API_KEY", "").strip()
    if not key:
        return known
    pending = [block["source"] for block in known if not block["english"]]
    joined = "\n".join(pending)[:6000]
    body = {
        "model": "grok-4.5",
        "temperature": 0,
        "messages": [
            {
                "role": "system",
                "content": "Translate technical documentation into plain English. Preserve code, identifiers, URLs, and license names. Return only the translation.",
            },
            {"role": "user", "content": joined},
        ],
    }
    req = urllib.request.Request(
        "https://api.x.ai/v1/chat/completions",
        data=json.dumps(body).encode(),
        method="POST",
    )
    req.add_header("Authorization", f"Bearer {key}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=90) as res:
            payload = json.loads(res.read().decode())
        english = payload["choices"][0]["message"]["content"].strip()
    except (urllib.error.URLError, KeyError, TimeoutError, json.JSONDecodeError):
        return known
    # One reply covers the lines the glossary could not. Keep glossary hits as they are.
    attached = False
    merged = []
    for block in known:
        if block["english"] or attached:
            merged.append(block)
            continue
        merged.append({"source": block["source"], "english": english})
        attached = True
    return merged


def render_brief(item: dict, meta: dict, readme: str, translated: list[dict]) -> str:
    fork_name = item["upstream"].split("/", 1)[1]
    sha = (meta.get("pushed_at") or "") + " @ " + (meta.get("default_branch") or "")
    commit = (meta.get("pushed_at") or "unknown")
    head = ""
    if meta.get("default_branch"):
        head = meta["default_branch"]
    lines = [
        f"# English brief — {item['upstream']}",
        "",
        f"Upstream: https://github.com/{item['upstream']}",
        f"Fork: https://github.com/{owner()}/{fork_name}",
        f"License: {item['license']}",
        f"Default branch: {head or 'unknown'}",
        f"Upstream pushed: {commit}",
        "This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.",
        "",
        "## What it is",
        "",
        item["summary"],
        "",
        "## Plain English",
        "",
        item["plain"],
        "",
        "## Why it belongs here",
        "",
        item["use"],
        "",
        "## Do not",
        "",
        item["do_not"],
        "",
        "## Integration",
        "",
    ]
    for step in item["integrate"]:
        lines.append(f"### {step['repo']}")
        lines.append("")
        lines.append(step["how"])
        lines.append("")
    lines += [
        "## For someone else's agent stack",
        "",
        item["other_agents"],
        "",
        "## Values",
        "",
        "- Economic: run the work on hardware the person already has. Do not meter a local action.",
        "- Community: leave the license and the authors' names in place so the next person can fork too.",
        "- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.",
        "- Everyday: a person should be able to tell which step ran on their machine.",
        "",
        f"Values named for this upstream: {', '.join(item['values'])}.",
        "",
    ]
    if translated:
        lines += ["## Translated passages", ""]
        for block in translated:
            if block.get("english"):
                lines.append(block["english"])
                lines.append("")
                if block["english"] != block.get("source"):
                    lines.append("Source line:")
                    lines.append("")
                    lines.append(block["source"][:2000])
                    lines.append("")
            else:
                lines.append("Non-English lines were found. Set the XAI_API_KEY secret on this repository to translate them on the next run.")
                lines.append("")
                lines.append("```")
                lines.append(block["source"][:2000])
                lines.append("```")
                lines.append("")
    else:
        lines += ["## Translated passages", "", "No non-English lines in the README checked this run.", ""]
    lines += [
        "## README checked",
        "",
        f"Characters read: {len(readme)}.",
        "",
    ]
    return "\n".join(lines)


def search_candidates() -> list[dict]:
    queries = [
        "android accessibility service license:mit",
        "talkback accessibility service license:mit",
        "offline speech synthesis license:apache-2.0",
        "shizuku user service license:apache-2.0",
    ]
    seen = set()
    found = []
    keywords = ("accessib", "talkback", "screen reader", "speech", "shizuku", "termux", "voice", "a11y")
    for q in queries:
        url = f"{API}/search/repositories?q={urllib.parse.quote(q)}&sort=updated&per_page=5"
        try:
            payload = request("GET", url)
        except RuntimeError as err:
            found.append({"query": q, "error": str(err)[:200]})
            continue
        for repo in payload.get("items") or []:
            full = repo.get("full_name") or ""
            if full in seen or full.startswith(owner() + "/"):
                continue
            seen.add(full)
            desc = (repo.get("description") or "").lower()
            if not any(k in desc or k in full.lower() for k in keywords):
                continue
            found.append(
                {
                    "upstream": full,
                    "license": ((repo.get("license") or {}) or {}).get("spdx_id"),
                    "description": repo.get("description") or "",
                    "updated": repo.get("pushed_at"),
                    "stars": repo.get("stargazers_count"),
                    "forked": False,
                    "note": "Discovered for review. Not forked automatically.",
                }
            )
    return found


def ensure_fork(upstream: str) -> tuple[str, str]:
    """Return (status, detail). Uses INTAKE_TOKEN when set, else the caller's token."""
    name = upstream.split("/", 1)[1]
    dest = f"{owner()}/{name}"
    tok = intake_token() or token()
    try:
        meta = request("GET", f"{API}/repos/{dest}", tok=tok)
        if meta.get("fork"):
            return "exists", dest
        return "name-taken", f"{dest} exists and is not a fork"
    except RuntimeError as err:
        if "404" not in str(err):
            return "error", str(err)[:300]
    if not tok:
        return "skipped", "no token"
    # GitHub rejects a burst of fork creates. Existing forks return above.
    time.sleep(8)
    try:
        request(
            "POST",
            f"{API}/repos/{upstream}/forks",
            {"default_branch_only": True},
            tok=tok,
        )
    except RuntimeError as err:
        text = str(err)
        if "403" in text or "404" in text:
            return "denied", text[:300]
        if "202" in text or "Accepted" in text:
            pass
        else:
            # GitHub sometimes returns the repo JSON; RuntimeError means a real failure.
            return "error", text[:300]
    for _ in range(12):
        time.sleep(2)
        try:
            request("GET", f"{API}/repos/{dest}", tok=tok)
            return "created", dest
        except RuntimeError:
            continue
    return "pending", dest


def put_file(dest_repo: str, path: str, content: str, branch: str, message: str) -> str:
    tok = intake_token() or token()
    url = f"{API}/repos/{dest_repo}/contents/{path}"
    sha = None
    try:
        current = request("GET", f"{url}?ref={urllib.parse.quote(branch)}", tok=tok)
        sha = current.get("sha")
        existing = base64.b64decode(current.get("content") or b"").decode(errors="replace")
        if existing == content:
            return "unchanged"
    except RuntimeError as err:
        if "404" not in str(err):
            return f"error {str(err)[:180]}"
    body = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": branch,
    }
    if sha:
        body["sha"] = sha
    try:
        request("PUT", url, body, tok=tok)
    except RuntimeError as err:
        return f"error {str(err)[:220]}"
    return "wrote"


SYNC_WORKFLOW = """name: sync-english
on:
  schedule:
    - cron: "45 11 * * *"
  workflow_dispatch:
permissions:
  contents: write
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Pull the English brief from systems-intake
        run: |
          mkdir -p intake
          curl -fsSL -o intake/ENGLISH.md "$MIRROR"
          git config user.name "systems-intake"
          git config user.email "304189395+onnxscibroccoli@users.noreply.github.com"
          git add intake/ENGLISH.md
          if git diff --staged --quiet; then
            echo "no change"
          else
            git commit -m "Sync English brief from systems-intake"
            git push
          fi
        env:
          MIRROR: __MIRROR__
"""


def push_fork(item: dict, meta: dict, brief: str) -> dict:
    status, detail = ensure_fork(item["upstream"])
    result = {"fork": status, "detail": detail}
    if status not in {"exists", "created", "pending"}:
        return result
    name = item["upstream"].split("/", 1)[1]
    dest = f"{owner()}/{name}"
    branch = meta.get("default_branch") or "main"
    # A brand-new fork can 404 for a few seconds after ensure_fork returns pending.
    for _ in range(8):
        try:
            request("GET", f"{API}/repos/{dest}")
            break
        except RuntimeError:
            time.sleep(2)
    result["brief"] = put_file(dest, "intake/ENGLISH.md", brief, branch, "Add English operator brief")
    mirror = f"https://raw.githubusercontent.com/{owner()}/systems-intake/main/mirrors/{item['upstream']}/ENGLISH.md"
    workflow = SYNC_WORKFLOW.replace("__MIRROR__", mirror)
    result["workflow"] = put_file(
        dest,
        ".github/workflows/sync-english.yml",
        workflow,
        branch,
        "Sync the English brief daily",
    )
    return result


def write_pages(data: dict, reports: list[dict], discovered: list[dict], generated: str) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    cards = []
    for item, report in zip(data["targets"], reports):
        name = item["upstream"].split("/", 1)[1]
        fork = f"https://github.com/{owner()}/{name}"
        ups = f"https://github.com/{item['upstream']}"
        steps = "".join(
            f"<li><code>{esc(step['repo'])}</code> — {esc(step['how'])}</li>" for step in item["integrate"]
        )
        cards.append(
            f"""<article class="card">
  <p class="kicker">{esc(item['license'])} · {esc(', '.join(item['values']))}</p>
  <h2><a href="{fork}">{esc(name)}</a></h2>
  <p class="quiet">Upstream <a href="{ups}">{esc(item['upstream'])}</a></p>
  <p>{esc(item['summary'])}</p>
  <p>{esc(item['use'])}</p>
  <p class="quiet">Do not: {esc(item['do_not'])}</p>
  <ul>{steps}</ul>
  <p class="quiet">Other agent stacks: {esc(item['other_agents'])}</p>
  <p class="quiet">Fork step: {esc(report.get('push', {}).get('fork', 'not run'))}. Brief: {esc(str(report.get('push', {}).get('brief', 'catalog only')))}.</p>
</article>"""
        )
    owned = "".join(
        f"<li><a href=\"https://github.com/{owner()}/{esc(row['repo'])}\"><code>{esc(row['repo'])}</code></a> — {esc(row['role'])}</li>"
        for row in data["owned"]
    )
    skipped = "".join(
        f"<li><code>{esc(row['upstream'])}</code> — {esc(row['reason'])}</li>" for row in data["not_forked"]
    )
    found = "".join(
        f"<li><a href=\"https://github.com/{esc(row.get('upstream',''))}\">{esc(row.get('upstream','search error'))}</a> — {esc(row.get('description') or row.get('error') or '')}</li>"
        for row in discovered
        if row.get("upstream") or row.get("error")
    ) or "<li>No new candidates this run.</li>"
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Systems intake</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,560&display=swap" />
  <style>
    :root {{ color-scheme: dark; --bg:#0e1210; --surface:#171d1a; --fg:#e7eee9; --muted:#93a399; --accent:#d6b25e; --line:#2c3833; }}
    body {{ margin:0; background:var(--bg); color:var(--fg); font-family:"IBM Plex Sans",sans-serif; line-height:1.55; }}
    main {{ width:min(46rem, calc(100% - 2rem)); margin:0 auto; padding:2.5rem 0 4rem; }}
    h1,h2 {{ font-family:"Source Serif 4",Georgia,serif; letter-spacing:-0.02em; }}
    h1 {{ font-size:clamp(2rem,5vw,3rem); line-height:1.15; }}
    a {{ color:var(--accent); }}
    .kicker {{ letter-spacing:.16em; text-transform:uppercase; color:var(--accent); font-size:.75rem; }}
    .quiet {{ color:var(--muted); }}
    .card {{ background:var(--surface); border:1px solid var(--line); border-radius:.875rem; padding:1rem 1.1rem; margin:0 0 .75rem; }}
    ul {{ padding-left:1.1rem; }}
    code {{ color:var(--fg); }}
  </style>
</head>
<body>
<main>
  <p class="kicker">Daily GitHub Action · {esc(generated)}</p>
  <h1>Forks, English briefs, and where they fit.</h1>
  <p class="quiet">Permissive upstreams only. The action refuses a fork when the license is missing or copyleft. Economic value means the work runs on a machine the person already has. Community value means the license stays attached. Disability support means the accessibility tree and a local voice come before a vendor screenshot. Everyday means a person who is not a lab can tell what ran.</p>
  <p><a href="https://github.com/{owner()}/systems-intake">Repository</a> · <a href="https://onnxscibroccoli.github.io/digest/">Systems Digest</a> · <a href="https://onnxscibroccoli.github.io/">Half a Mile</a></p>
  <h2>Repositories this account already runs</h2>
  <ul>{owned}</ul>
  <h2>Forked this intake</h2>
  {''.join(cards)}
  <h2>Not forked, on purpose</h2>
  <ul>{skipped}</ul>
  <h2>Search, not yet forked</h2>
  <p class="quiet">The daily job searches public repositories for accessibility, speech, and Shizuku-related tools. It records them. It does not fork them until a person adds them to intake/targets.json.</p>
  <ul>{found}</ul>
</main>
</body>
</html>
"""
    (DOCS / "index.html").write_text(html)


def esc(value: str) -> str:
    amp = chr(38)
    return (
        value.replace(amp, amp + "amp;")
        .replace("<", amp + "lt;")
        .replace(">", amp + "gt;")
        .replace('"', amp + "quot;")
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fork", action="store_true", help="Create missing forks when the token can")
    parser.add_argument("--push-forks", action="store_true", help="Write ENGLISH.md onto each fork")
    args = parser.parse_args()
    data = load_targets()
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    reports = []
    for item in data["targets"]:
        meta = repo_meta(item["upstream"])
        spdx = license_spdx(meta, item["license"])
        if spdx not in PERMISSIVE:
            reports.append({"upstream": item["upstream"], "skipped": f"license {spdx}"})
            continue
        readme = readme_text(item["upstream"])
        if not isinstance(readme, str):
            readme = ""
        translated = translate_lines(cjk_lines(readme))
        brief = render_brief(item, meta, readme, translated)
        mirror = MIRRORS / item["upstream"]
        mirror.mkdir(parents=True, exist_ok=True)
        (mirror / "ENGLISH.md").write_text(brief)
        report = {
            "upstream": item["upstream"],
            "license": spdx,
            "pushed": meta.get("pushed_at"),
            "readme_chars": len(readme),
            "translated_blocks": len(translated),
        }
        if args.fork or args.push_forks:
            report["push"] = push_fork(item, meta, brief)
        reports.append(report)
        print(item["upstream"], report.get("push") or "mirrored")
    discovered = search_candidates()
    CATALOG.mkdir(parents=True, exist_ok=True)
    catalog = {
        "generated": generated,
        "reports": reports,
        "discovered": discovered,
        "not_forked": data["not_forked"],
    }
    (CATALOG / "latest.json").write_text(json.dumps(catalog, indent=2) + "\n")
    write_pages(data, reports, discovered, generated)
    print("wrote", CATALOG / "latest.json")


if __name__ == "__main__":
    main()
