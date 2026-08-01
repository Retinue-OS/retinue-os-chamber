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

The reverse question, which nothing asked (c350)
------------------------------------------------
A departure is one of two ways this card wastes the owner's time, and it is the
milder one: a dropped item is work that stays undone. The other is an item that
**stays while its subject resolves** — the queue asking him to do something he
has already done. Nothing measured that until 2026-08-01.

Measured then, over the two copies that existed:

  * The **disk** card, stamp `2026-07-31T18:35:03Z`, 22 slots. Item 18 asks him
    to "merge or reject" PR #55; item 20 says PRs #49, #51, #53, #56 and #57 are
    open. All six were merged between 18:48:33Z and 19:44:08Z — **the first of
    them thirteen minutes after the card's own stamp.**
  * The **served** card, stamp `2026-07-30T02:37:42Z`, 19 slots — four already
    done: PRs #44/#45 ("open and unmerged", merged 2026-07-30), the branch
    `fix/restore-dropped-merges` ("awaits merge or deletion", merged as #55 and
    deleted, 404), a filing slot that opened two days earlier, and a held-queue
    count of three that is now one.

So the queue decays toward *instructions to redo finished work*, fastest in the
one card that exists to save the owner time — and it does so within the hour,
not within the day. That is not a delivery failure; the disk copy has it too.

One bound, and it is the same shape as the one above: this flags **references**,
not asks. An item may legitimately name a merged PR as evidence ("chamber#3:
substance done — retinue#54 and PR retinue#55 are mine"). The check does not
decide whether the reference was presented as pending; it requires that a
resolved reference on the queue be *seen*.

The coverage gap this exposed
-----------------------------
Both stale items on the disk card are written without a repository prefix —
`PR #55 (mine)`, `Your PRs #49, #51, #53, #56, #57 are open` — so the extractor
below, which refuses to guess, files them as unattributed and never resolves
them. The two items the check most needed to see were the two it could not. The
fix is in the card, not here: a desk item that names a PR should name its repo.
Until then the count of unattributed references on the current card is printed
as a coverage figure rather than left silent.

What it cannot see, stated because its clean line is misleading without it
-------------------------------------------------------------------------
Run against the served card on 2026-08-01 it reports **0 resolved still on the
queue**, and four of that card's items are finished work. All four sit outside
what a reference check can reach:

  * `Your own PRs #44 and #45 are open and unmerged` — bare numbers, uncovered;
  * `Branch fix/restore-dropped-merges awaits merge or deletion` — a **branch**,
    not an issue. `GET /repos/…/branches/<name>` → 404 answers it, and this
    check does not ask. The next hand at this file should add it: the case is
    real, measured, and one line of the four;
  * `Next issue may be filed 2026-07-30 06:08 UTC` — a **date** in the past;
  * `Three findings are written up and held` — a **count** of this chamber's own
    drafts, which is one.

Branches, added c355
--------------------
The second bullet above is now asked. A branch resolves the other way round from
an issue: an issue is finished when it **closes**, a branch is finished when it
**stops existing**, so `GET /repos/…/branches/<name>` → 404 is the resolved case
and 200 is the item that is still owed. Both questions this file already asks
apply unchanged — a resolved branch still on the card is `STALE-RESOLVED`, a live
branch that left the card is `DROPPED-LIVE` — because the machinery was never
about issues, it was about references whose state can be looked up.

Two deliberate under-detections, both the same choice c262 made for repositories:

  * a name counts only after the word *branch*, and
  * only when it carries a `/`.

Neither is how branches must be named; both are how this card has named them
(`chamber#7: merge or reject branch claude/aros-issues-triage-goei5k`,
`Branch fix/restore-dropped-merges awaits merge or deletion`). A looser matcher
would have to decide that some bare word is a branch name, which is the guess
this file exists not to make. A missed branch is counted nowhere and claimed
nowhere; a guessed one would be reported as a measurement.

Repository attribution follows the issue rule, but positionally: a branch
inherits the repository named most recently **before it in the same string**, so
the first example above resolves against `retinue-os-chamber` and the second,
naming no repository anywhere, is uncovered and enters the coverage figure
rather than being resolved against a guess. First reading, 2026-08-01: the disk
card's one branch reference is attributed and **live** (200) — clean; the served
card's is unattributed, which is precisely the item that has been finished since
2026-07-31 and is why the card names its repository from now on (c354's rule).

So the summary line prints coverage beside the verdict, and says in words that
an incomplete coverage is not a clean bill. A check that reports what it looked
at is worth more than one that reports what it found.

What it checks
--------------
For every issue reference in the previous generation of `docs/data/todo.json`
that is absent from the current one, ask GitHub whether it is still open. An
open one is reported as `DROPPED-OPEN`. Closed or merged ones are the normal,
correct case and are counted, not printed.

For every reference **present** on the current card, ask the same question and
report the resolved ones as `STALE-RESOLVED`.

Additions are printed as information: a generation that adds three items and
drops five is the shape worth seeing in one place.

Which copy
----------
The disk card by default, which is what the next generation is written against.
`--served` fetches the published copy instead — what the owner actually opens.
The two are the same file whenever `delivery-check.py` passes, and while it
fails the served card is the older and worse of the two, so the flag exists to
make that difference readable rather than assumed.

Deliberately **not** in the pre-commit hook. The refresh job commits the card as
part of its run, and a hook that blocks it would trade a silent drop for a lost
generation — which the job's own prompt already ranks as the worse outcome. This
is an end-of-wake-up check, alongside the other four.

Usage
-----
    python3 tools/desk-drop-check.py [chamber-root]
    python3 tools/desk-drop-check.py --offline    # set difference only, no gh
    python3 tools/desk-drop-check.py --served     # read the published card

Exit codes: 0 clean, 1 something open was dropped or something resolved is
still on the queue, 2 the self-test failed.
"""

import json
import os
import re
import subprocess
import sys
import urllib.request

CARD = "docs/data/todo.json"
SERVED = "https://retinue-os.github.io/retinue-os-chamber/data/todo.json"

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

# A branch name is recognised only after the word "branch" and only when it
# carries a `/`. Both bounds under-detect on purpose — see the docstring.
BRANCH = re.compile(r"branch\s+`?([\w.\-]+/[\w.\-/]+?)`?(?=[\s,.;:)]|$)", re.I)

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


def branch_refs_in(text):
    """Return (attributed, unattributed) branch references found in one string.

    A branch inherits the repository named most recently *before it* in the same
    string — `chamber#7: merge or reject branch claude/…` is a branch of
    retinue-os-chamber — and one with no repository named before it anywhere in
    that string is unattributed: reported as uncovered rather than guessed at.
    """
    marks = [(m.start(), REPOS[m.group(1)]) for m in REF.finditer(text) if m.group(1)]
    attributed, unattributed = set(), set()
    for m in BRANCH.finditer(text):
        repo = None
        for pos, named in marks:
            if pos < m.start():
                repo = named
        if repo:
            attributed.add((repo, m.group(1)))
        else:
            unattributed.add(m.group(1))
    return attributed, unattributed


def card_strings(card):
    """The title of every slot on one desk card."""
    strings = []
    top = card.get("top") or {}
    if top.get("title"):
        strings.append(top["title"])
    for item in card.get("others") or []:
        if item.get("title"):
            strings.append(item["title"])
    return strings


def card_refs(card):
    """Every reference on one desk card, plus the count it could not attribute."""
    attributed, unattributed = set(), set()
    for s in card_strings(card):
        a, u = refs_in(s)
        attributed |= a
        unattributed |= u
    return attributed, unattributed


def card_branches(card):
    """Every branch reference on one desk card, attributed and not."""
    attributed, unattributed = set(), set()
    for s in card_strings(card):
        a, u = branch_refs_in(s)
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

    # The reverse question (c350), on a fixture reproducing the real reading:
    # one merged PR still on the queue, one open issue that must stay silent,
    # and two bare references that must be counted as uncheckable rather than
    # guessed at. Resolution is injected, so this case needs no network.
    card = {"top": {"title": "chamber#6: the role grant"},
            "others": [{"title": "retinue#55: merge or reject"},
                       {"title": "retinue#1: projects card returns no rows"},
                       {"title": "Your PRs #49, #51 are open"}]}
    fake = {("retinue-os-chamber", 6): "issue-open",
            ("retinue", 55): "pr-closed",
            ("retinue", 1): "issue-open"}
    attributed, unattributed = card_refs(card)
    stale = sorted(r for r in attributed if fake[r].endswith("closed"))
    if stale != [("retinue", 55)]:
        print(f"self-test FAIL: stale set was {stale}", file=sys.stderr)
        return False
    if unattributed != {49, 51}:
        print(f"self-test FAIL: uncovered set was {unattributed}", file=sys.stderr)
        return False

    # Branch references (c355), on the two forms this card has actually used:
    # one attributed by a repository named earlier in the same string, one
    # naming none. The negative cases matter as much — a slashless word after
    # "branch", and a path-looking token with no "branch" before it, are both
    # things this matcher must decline to call a branch.
    branch_cases = [
        ("chamber#7: merge or reject branch claude/aros-issues-triage-goei5k",
         {("retinue-os-chamber", "claude/aros-issues-triage-goei5k")}, set()),
        ("Branch fix/restore-dropped-merges awaits merge or deletion",
         set(), {"fix/restore-dropped-merges"}),
        ("retinue#55 merged branch `docs/link-provenance-piece`, deleted since",
         {("retinue", "docs/link-provenance-piece")}, set()),
        ("the branch policy has three tiers", set(), set()),
        ("docs/data/todo.json is regenerated daily", set(), set()),
        # Attribution is positional: a repository named *after* the branch does
        # not claim it, because the card writes `<repo>#<n>: … branch <name>`.
        ("Branch fix/x-y is stuck; see retinue#55", set(), {"fix/x-y"}),
    ]
    for text, want_a, want_u in branch_cases:
        got_a, got_u = branch_refs_in(text)
        if got_a != want_a or got_u != want_u:
            print(f"self-test FAIL on branch case {text!r}: {got_a} / {got_u}",
                  file=sys.stderr)
            return False

    # The stale-resolved question in its branch form, resolution injected.
    bcard = {"top": {"title": "chamber#7: merge or reject branch claude/triage-x"},
             "others": [{"title": "retinue#1: still open"},
                        {"title": "Branch fix/restore-dropped-merges awaits merge"}]}
    bfake = {("retinue-os-chamber", "claude/triage-x"): "branch-gone"}
    battr, bunattr = card_branches(bcard)
    bstale = sorted(r for r in battr if bfake[r] == "branch-gone")
    if bstale != [("retinue-os-chamber", "claude/triage-x")]:
        print(f"self-test FAIL: stale branch set was {bstale}", file=sys.stderr)
        return False
    if bunattr != {"fix/restore-dropped-merges"}:
        print(f"self-test FAIL: uncovered branch set was {bunattr}", file=sys.stderr)
        return False
    return True


def served_card():
    """The published desk card — what the owner opens, not what is on disk."""
    with urllib.request.urlopen(SERVED, timeout=30) as fh:
        return json.loads(fh.read().decode("utf-8"))


def generations(root, current=None):
    """The current card, and the newest committed one carrying a different stamp."""
    if current is None:
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


_STATE_CACHE = {}


def state_of(repo, number, offline):
    """`issue-open`, `issue-closed`, `pr-open`, `pr-closed`, or a failure word.

    Cached: the dropped set and the present set overlap in the general case, and
    a resolved reference costs the same call in both.
    """
    if offline:
        return "unchecked"
    key = (repo, number)
    if key in _STATE_CACHE:
        return _STATE_CACHE[key]
    out = subprocess.run(
        ["gh", "api", f"/repos/{OWNER}/{repo}/issues/{number}",
         "--jq", '(if .pull_request then "pr-" else "issue-" end) + .state'],
        capture_output=True, text=True)
    state = out.stdout.strip() if out.returncode == 0 else "unreadable"
    _STATE_CACHE[key] = state
    return state


_BRANCH_CACHE = {}


def branch_state(repo, name, offline):
    """`branch-live`, `branch-gone`, or a failure word.

    Inverted relative to `state_of` on purpose: a branch is *finished* when it
    stops existing, so 404 is the resolved case and 200 is the item still owed.

    But **not every 404 here is a missing branch**, and the difference is the
    whole reliability of the inversion. Measured 2026-08-01 against the live
    API, the endpoint returns two distinguishable 404s:

        missing branch  ->  {"message": "Branch not found", ...}
        missing repo    ->  {"message": "Not Found", ...}

    and the second is also what an unreadable *repository* answers — which in
    this deployment includes a permission denial, the failure this chamber has
    now misread three times (c19, c310, c343). So only the first is read as
    `branch-gone`; everything else returns `unreadable`, which both callers
    report as a problem rather than as an answer. A first draft of this
    function collapsed both and reported a nonexistent repo's branch as
    resolved.
    """
    if offline:
        return "unchecked"
    key = (repo, name)
    if key in _BRANCH_CACHE:
        return _BRANCH_CACHE[key]
    out = subprocess.run(
        ["gh", "api", f"/repos/{OWNER}/{repo}/branches/{name}", "--jq", ".name"],
        capture_output=True, text=True)
    body = out.stdout + out.stderr
    if out.returncode == 0:
        state = "branch-live"
    elif "404" in body and "Branch not found" in body:
        state = "branch-gone"
    else:
        state = "unreadable"
    _BRANCH_CACHE[key] = state
    return state


def main():
    flags = {"--offline", "--served"}
    args = [a for a in sys.argv[1:] if a not in flags]
    offline = "--offline" in sys.argv[1:]
    served = "--served" in sys.argv[1:]
    root = args[0] if args else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if not self_test():
        print("self-test FAILED — refusing to report on the real card", file=sys.stderr)
        return 2
    print("self-test: pass (6 reference cases, 1 card fixture, 1 shortening fixture, "
          "1 stale-resolved fixture, 6 branch cases, 1 stale-branch fixture)")

    if served:
        try:
            card = served_card()
        except Exception as exc:                       # noqa: BLE001 — report, don't crash
            print(f"served card unreadable ({exc}) — nothing measured, NOT reported as clean",
                  file=sys.stderr)
            return 2
        print(f"  reading the SERVED card ({SERVED})")
    else:
        card = None

    current, previous, prev_stamp = generations(root, card)
    cur_refs, cur_unattributed = card_refs(current)
    cur_branches, cur_unattributed_branches = card_branches(current)
    problems = []

    # The reverse question: what is still on the queue although it is finished?
    stale = []
    for repo, number in sorted(cur_refs):
        if state_of(repo, number, offline).endswith("closed"):
            stale.append((repo, number))
    for repo, number in stale:
        problems.append(f"STALE-RESOLVED  {repo}#{number}: on the desk at "
                        f"{current.get('generated')}, and it is closed or merged")

    # The same question of a branch, which resolves by ceasing to exist.
    for repo, name in sorted(cur_branches):
        state = branch_state(repo, name, offline)
        if state == "branch-gone":
            stale.append((repo, name))
            problems.append(f"STALE-RESOLVED  {repo}:{name}: on the desk at "
                            f"{current.get('generated')}, and the branch is gone (404)")
        elif state == "unreadable":
            problems.append(f"UNREADABLE      {repo}:{name}: the branch endpoint "
                            f"answered neither 200 nor 404 — not read as either")

    if served:
        # The drop check compares *consecutive generations*, which is a git
        # concept and belongs to the disk copy. While delivery is broken the
        # served card is older than the newest committed one, so the same
        # comparison would report the disk card's own additions as served
        # drops — backwards, and confidently so. Measured on the first run of
        # this flag (c350): `DROPPED-OPEN retinue#46, #54`, both of which had
        # in fact just *arrived* on disk. So in served mode this reports the
        # two questions that are well defined without a predecessor.
        print(f"  served card @ {current.get('generated')}: {len(cur_refs)} "
              f"attributed reference(s), {len(cur_branches)} attributed branch(es); "
              f"no generation comparison in this mode")
        dropped, added, closed, prev_unattributed = [], [], 0, set()
        prev_unattributed_branches = set()
    elif previous is None:
        print(f"  {CARD} @ {current.get('generated')}: {len(cur_refs)} references, "
              f"no earlier generation to compare against.")
        dropped, added, closed, prev_unattributed = [], [], 0, set()
        prev_unattributed_branches = set()
    else:
        prev_refs, prev_unattributed = card_refs(previous)
        prev_branches, prev_unattributed_branches = card_branches(previous)
        dropped = sorted(prev_refs - cur_refs)
        added = sorted(cur_refs - prev_refs)

        # A branch that left the card while it still exists is the branch form
        # of DROPPED-OPEN: the item is unfinished and no longer visible.
        for repo, name in sorted(prev_branches - cur_branches):
            state = branch_state(repo, name, offline)
            if state == "branch-live":
                problems.append(f"DROPPED-LIVE    {repo}:{name}: on the desk at "
                                f"{prev_stamp}, absent now, and the branch still exists")
            elif state in ("unreadable", "unchecked"):
                problems.append(f"DROPPED-{state.upper()}  {repo}:{name}: on the desk "
                                f"at {prev_stamp}, absent now, {state}")
        for repo, name in sorted(cur_branches - prev_branches):
            print(f"  added    {repo}:{name} (branch)")

        print(f"  previous generation {prev_stamp}: {len(prev_refs)} references")
        print(f"  current  generation {current.get('generated')}: {len(cur_refs)} references")

        closed = 0
        for repo, number in dropped:
            state = state_of(repo, number, offline)
            if state.endswith("open") or state in ("unreadable", "unchecked"):
                problems.append(
                    f"DROPPED-{'OPEN' if state.endswith('open') else state.upper()}"
                    f"  {repo}#{number}: on the desk at {prev_stamp}, absent now, {state}")
            else:
                closed += 1

        for repo, number in added:
            print(f"  added    {repo}#{number}")

    uncovered = sorted(prev_unattributed | cur_unattributed)
    if uncovered:
        print(f"  {len(uncovered)} bare reference(s) named no repository and were not "
              f"checked: {', '.join('#%d' % n for n in uncovered)}")

    uncovered_branches = sorted(prev_unattributed_branches | cur_unattributed_branches)
    if uncovered_branches:
        print(f"  {len(uncovered_branches)} branch(es) named no repository and were "
              f"not checked: {', '.join(uncovered_branches)}")

    # Coverage is part of the reading, not a footnote. A queue whose PR items
    # are written without a repository prefix yields "0 resolved still on the
    # queue" while carrying several — which is how the served card reads today.
    # Branches count in the same figure: they are references whose state can be
    # looked up, and one of the served card's four blind spots was exactly one.
    resolvable = len(cur_refs) + len(cur_branches)
    total = resolvable + len(cur_unattributed) + len(cur_unattributed_branches)
    coverage = f"coverage {resolvable}/{total} reference(s) resolvable"

    tail = (f"{len(dropped)} dropped ({closed} resolved), {len(added)} added, "
            f"{len(stale)} resolved still on the queue, {coverage}")
    if not problems:
        verdict = "0 problems" if not (cur_unattributed or cur_unattributed_branches) else (
            "0 problems FOUND — but the unresolvable references above are unmeasured, "
            "so this is not a clean bill")
        print(f"\n{tail}, {verdict}.")
        return 0

    print()
    for line in problems:
        print(line)
    print(f"\n{tail}, {len(problems)} problem(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
