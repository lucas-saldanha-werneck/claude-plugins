#!/usr/bin/env python3
"""Check that the catalog says the same thing as each plugin repo.

- Each marketplace entry's name and description equal the plugin.json on the repo's default branch.
- The README lists the same plugins, in the same order, as marketplace.json.
Uses the GitHub API (GITHUB_TOKEN if set). Exit 1 on any mismatch.
"""
import base64, json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
market = json.load(open(os.path.join(ROOT, ".claude-plugin", "marketplace.json")))
readme = open(os.path.join(ROOT, "README.md")).read()
token = os.environ.get("GITHUB_TOKEN")
errors = []


def plugin_json(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/contents/.claude-plugin/plugin.json",
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": "catalog-check",
                                          **({"Authorization": f"Bearer {token}"} if token else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(base64.b64decode(json.load(r)["content"]))


names = []
for e in market["plugins"]:
    names.append(e["name"])
    repo = e["source"]["repo"]
    try:
        pj = plugin_json(repo)
    except Exception as exc:  # network or missing file
        errors.append(f"{e['name']}: cannot read plugin.json from {repo}: {exc}")
        continue
    if pj.get("name") != e["name"]:
        errors.append(f"{e['name']}: plugin.json name is {pj.get('name')!r}")
    if pj.get("description") != e.get("description"):
        errors.append(f"{e['name']}: description differs\n  catalog: {e.get('description')}\n  plugin:  {pj.get('description')}")

plugin_part = readme.split("## Command-line tools")[0]
listed = re.findall(r"^- \*\*\[([a-z0-9-]+)\]", plugin_part, re.M)
if listed != names:
    errors.append(f"README order/list differs from marketplace.json\n  README:      {listed}\n  marketplace: {names}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: {len(names)} plugins match their repos and the README")
