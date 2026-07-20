#!/usr/bin/env python3
"""Prepend a first-line AI-authorship disclosure to the issues Aros actually wrote.

Only issues carrying an explicit "Filed by Aros" signature are touched. Issues of
uncertain authorship are left alone: asserting Aros wrote something the owner
wrote would be the same misattribution in the opposite direction.
"""
import json
import subprocess
import sys

LINE = "**Written by Aros, the project's AI agent, from the owner's GitHub account — see [chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).**"

TARGETS = [
    ("Retinue-OS/retinue", 1),
    ("Retinue-OS/retinue", 2),
    ("Retinue-OS/qlever-dir", 3),
]


def api(args, retries=4):
    for attempt in range(retries):
        p = subprocess.run(["gh", "api"] + args, capture_output=True, text=True)
        if p.returncode == 0:
            return p.stdout
        if "503" in p.stderr or "No server is currently available" in p.stderr:
            continue
        sys.exit(f"failed: {p.stderr.strip()}")
    sys.exit("giving up after repeated 503s")


for repo, num in TARGETS:
    body = json.loads(api([f"repos/{repo}/issues/{num}"]))["body"]
    if body.startswith("**Written by Aros"):
        print(f"{repo}#{num}: already disclosed, skipped")
        continue
    if "Filed by Aros" not in body:
        print(f"{repo}#{num}: no Aros signature, NOT touching")
        continue
    api([
        "-X", "PATCH", f"repos/{repo}/issues/{num}",
        "-f", f"body={LINE}\n\n{body}",
    ])
    print(f"{repo}#{num}: disclosure prepended")
