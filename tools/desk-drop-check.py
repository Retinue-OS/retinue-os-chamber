#!/usr/bin/env python3
"""Report which issues left the owner's desk card while still open.

Why this exists
---------------
`docs/data/todo.json` is the owner's queue — the card on the public dashboard
that tells him what is owed. It is regenerated whole, once a day, by the
`aros-dashboard-refresh` job, from judgement rather than from a rule: the job
prompt says what a slot may contain and how long it may be, and says nothing
about which items must be in it.

Two instruments already watch that file and neither asks this question.
`delivery-check.py` asks whether the served copy matches disk and whether all
five cards carry one stamp (freshness). `card-budget-check.py` asks whether any
field is longer than its slot (length). A card can pass both while quietly
dropping a live item, because **the one state a missing item is
indistinguishable from is a resolved one** — the card simply gets shorter, and
nothing about reading it signals that something left.

Measured at c262 on the 2026-07-29T18:09:41Z generation, the first one written
under the length budgets: **seven open issues** that the 2026-07-28 generation
named — `retinue#28`, `#36`, `#37`, `#38`, `#39`, `#40` and `qlever-dir#10` — are
absent from it. The generation's own write-up describes the change as a
*rendering* fix ("one item, one line, no clipping on a phone"), which is what it
was for the items that stayed and is not what it was for these seven. Cutting
sixteen paragraphs to sixteen lines is length. Ending with a card that names
sixteen issues where the previous one named twenty-three is editorial, and no
record of this chamber mentions it. I counted five by hand before writing this
and the script found seven, which is the argument for the script.

One bound, stated because it decides what the number means: this counts
**references**, not slots. The previous card was prose, so one slot could name
three issues (`qlever-dir#8`, `#10`, …); the current card is an index, so a slot
names one. That is the right unit anyway — what a reader can see on the card is a
reference, not a slot — but it means "8 dropped" is not "8 items deleted".

The desk card is allowed to be an index rather than a complete list — 47 open
issues on one phone screen is a wall, and the same generation was right to prefer
a verdict plus an issue number to an argument. What it is not allowed to do is
drop an item **silently**. So this check makes the editorial choice visible: it
does not require any item to stay, it requires that a departure be seen.

What it checks
--------------
For every issue reference in the previous generation of `docs/data/todo.json`
that is absent from the current one, ask GitHub whether it is still open. An
open one is reported as `DROPPED-OPEN`. Closed or merged ones are the normal,
correct case and are counted, not printed.

Additions are printed as information: a generation that adds three items and
drops five is the shape worth seeing in one place.

Deliberately **not** in the pre-commit hook. The refresh job commits the card as
part of its run, and a hook that blocks it would trade a silent drop for a lost
generation — which the job's own prompt already ranks as the worse outcome. This
is an end-of-wake-up check, alongside the other four.

Usage
-----
    python3 tools/desk-drop-check.py [chamber-root]
    python3 tools/desk-drop-check.py --offline    # set difference only, no gh

Exit codes: 0 clean, 1 something open was dropped, 2 the self-test failed.
"""

import json
import os
import re
import subprocess
import sys

CARD = "docs/data/todo.json"

# Longest prefix first: `retinue-os-chamber#3` must not match `retinue` and
# leave `-os-chamber` behind.
REPOS = {
    "retinue-os-chamber": "retinue-os-chamber",
    "retinue-os-deployment": "retinue-os-deployment",
    "qlever-dir": "qlever-dir",
    "chamber": "retinue-os-chamber",
    "deployment": "retinue-os-deployment",
    "retinue": "retinue",
}
PREFIXES = sorted(REPOS, key=len, reverse=True)
REF = re.compile(r"(?:(" + "|".join(PREFIXES) + r")\s*)?#(\d+)")

OWNER = "Retinue-OS"


def refs_in(text):
    """Return (attributed, unattributed) refs found in one string.

    A bare `#27` inherits the repository named most recently *in the same
    string* — `retinue#26 + #27` is two references to the same repo — and a bare
    number with no prefix anywhere before it in that string is unattributed:
    reported as uncovered rather than guessed at.
    """
    attributed, unattributed, last = set(), set(), None
    for prefix, number in REF.findall(text):
        if prefix:
            last = REPOS[prefix]
        if last:
            attributed.add((last, int(number)))
        else:
            unattributed.add(int(number))
    return attributed, unattributed


def card_refs(card):
    """Every reference on one desk card, plus the count it could not attribute."""
    strings = []
    top = card.get("top") or {}
    if top.get("title"):
        strings.append(top["title"])
    for item in card.get("others") or []:
        if item.get("title"):
            strings.append(item["title"])
    attributed, unattributed = set(), set()
    for s in strings:
        a, u = refs_in(s)
        attributed |= a
        unattributed |= u
    return attributed, unattributed


def self_test():
    cases = [
        # (text, expected attributed, expected unattributed)
        ("chamber#1: create the accounts", {("retinue-os-chamber", 1)}, set()),
        ("retinue#26 + #27: the claim corrections",
         {("retinue", 26), ("retinue", 27)}, set()),
        ("retinue-os-chamber#3 and qlever-dir#8",
         {("retinue-os-chamber", 3), ("qlever-dir", 8)}, set()),
        ("Your own PRs #44 and #45 are open", set(), {44, 45}),
        ("Next issue may be filed 2026-07-30 06:08 UTC", set(), set()),
        ("retinue#15 and #19, the two security issues",
         {("retinue", 15), ("retinue", 19)}, set()),
    ]
    for text, want_a, want_u in cases:
        got_a, got_u = refs_in(text)
        if got_a != want_a or got_u != want_u:
            print(f"self-test FAIL on {text!r}: {got_a} / {got_u}", file=sys.stderr)
            return False

    # A whole-card fixture: one item drops, one arrives, one stays.
    prev = {"top": {"title": "chamber#1 oldest"},
            "others": [{"title": "retinue#28 on main"}, {"title": "qlever-dir#8 blank nodes"}]}
    cur = {"top": {"title": "chamber#1 oldest"},
           "others": [{"title": "chamber#8 w3id"}, {"title": "qlever-dir#8 blank nodes"}]}
    pa, _ = card_refs(prev)
    ca, _ = card_refs(cur)
    if pa - ca != {("retinue", 28)} or ca - pa != {("retinue-os-chamber", 8)}:
        print("self-test FAIL on the card fixture", file=sys.stderr)
        return False

    # The divergence fixture the real defect had: a card that is *shorter* but
    # loses nothing must be clean, so length alone never trips this check.
    short = {"top": {"title": "chamber#1"},
             "others": [{"title": "retinue#28"}, {"title": "qlever-dir#8"}]}
    sa, _ = card_refs(short)
    if sa != pa:
        print("self-test FAIL: shortening changed the reference set", file=sys.stderr)
        return False
    return True


def generations(root):
    """The current card, and the newest committed one carrying a different stamp."""
    path = os.path.join(root, CARD)
    current = json.load(open(path, encoding="utf-8"))
    stamp = current.get("generated")

    out = subprocess.run(["git", "-C", root, "log", "--format=%H", "--", CARD],
                         capture_output=True, text=True)
    if out.returncode != 0:
        return current, None, None
    for sha in out.stdout.split():
        blob = subprocess.run(["git", "-C", root, "show", f"{sha}:{CARD}"],
                              capture_output=True, text=True)
        if blob.returncode != 0:
            continue
        try:
            older = json.loads(blob.stdout)
        except json.JSONDecodeError:
            continue
        if older.get("generated") != stamp:
            return current, older, older.get("generated")
    return current, None, None


def state_of(repo, number, offline):
    if offline:
        return "unchecked"
    out = subprocess.run(
        ["gh", "api", f"/repos/{OWNER}/{repo}/issues/{number}",
         "--jq", '(if .pull_request then "pr-" else "issue-" end) + .state'],
        capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else "unreadable"


def main():
    args = [a for a in sys.argv[1:] if a != "--offline"]
    offline = "--offline" in sys.argv[1:]
    root = args[0] if args else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if not self_test():
        print("self-test FAILED — refusing to report on the real card", file=sys.stderr)
        return 2
    print("self-test: pass (6 reference cases, 1 card fixture, 1 shortening fixture)")

    current, previous, prev_stamp = generations(root)
    cur_refs, cur_unattributed = card_refs(current)
    if previous is None:
        print(f"  {CARD} @ {current.get('generated')}: {len(cur_refs)} references, "
              f"no earlier generation to compare against.")
        return 0
    prev_refs, prev_unattributed = card_refs(previous)

    dropped = sorted(prev_refs - cur_refs)
    added = sorted(cur_refs - prev_refs)

    print(f"  previous generation {prev_stamp}: {len(prev_refs)} references")
    print(f"  current  generation {current.get('generated')}: {len(cur_refs)} references")

    problems, closed = [], 0
    for repo, number in dropped:
        state = state_of(repo, number, offline)
        if state.endswith("open") or state in ("unreadable", "unchecked"):
            problems.append(f"DROPPED-{'OPEN' if state.endswith('open') else state.upper()}"
                            f"  {repo}#{number}: on the desk at {prev_stamp}, absent now, {state}")
        else:
            closed += 1

    for repo, number in added:
        print(f"  added    {repo}#{number}")

    uncovered = len(prev_unattributed | cur_unattributed)
    if uncovered:
        print(f"  {uncovered} bare reference(s) named no repository and were not checked")

    if not problems:
        print(f"\n{len(dropped)} dropped ({closed} resolved), {len(added)} added, 0 problems.")
        return 0

    print()
    for line in problems:
        print(line)
    print(f"\n{len(dropped)} dropped ({closed} resolved), {len(added)} added, "
          f"{len(problems)} problem(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
