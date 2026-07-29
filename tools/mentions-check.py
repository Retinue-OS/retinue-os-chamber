#!/usr/bin/env python3
"""Measure external mentions of this project on the part of the world GitHub sees.

Why this exists
---------------
"Stars and mentions" has been on the wake-up survey checklist since this chamber
existed. Stars have an instrument. Mentions did not: `WebSearch` is not permitted
in this deployment, and c183 recorded the check as *unavailable rather than
silently skipped* — correct, but every cycle since inherited that state.

c233 (2026-07-29) found a substitute for the GitHub-visible part and wrote the
queries down, together with the reason the queries alone are not the measurement:

    gh api "/search/issues?q=is:issue+%22retinue-os%22+-org:Retinue-OS" --jq .total_count

reads **2**, and both hits are `BSData/horus-heresy-2nd-edition` — a Warhammer
data repo where *retinue* is a common noun and *os* comes from an adjacent
`OS: Android` line. GitHub's index tokenizes `retinue-os` into `retinue` + `os`,
so a quoted phrase does not survive into the query it actually runs.

c233 recorded that discriminator **in prose**, in a register row. c235's lesson,
learned three times in four cycles, is that a lesson in prose does not propagate
to the next instrument or the next reader — only an edit to the instrument does.
This is that edit. Raw `total_count` is never the answer here; the answer is the
count that survives reading each hit.

What it measures, and what it does not
--------------------------------------
Measured: issues and pull requests outside the org that name this project;
repositories whose name matches; code outside the org that links to it.

c243 (2026-07-29) found that the first half of that sentence was a label rather
than a measurement. Both issue probes read `is:issue "<term>"`, which **excludes
pull requests** — so two probes announcing "issues and PRs" had never once looked
at a PR. The PR side is not empty: `is:pull-request "qlever-dir" -org:Retinue-OS`
returns **19 raw hits**, none of which any run of this script had ever read. They
all turn out to be the same tokenizer artefact (`qlever` + `dir` in QLever's own
ecosystem), so the reading does not move — but "the answer would have been the
same" is not a reason a probe may skip half its declared surface, and next month
the PR side is where a reference to this project would most plausibly appear.

The queries need the qualifier for a second reason, found the same day (c242):
`/search/issues` now returns **422 Query must include 'is:issue' or
'is:pull-request'** when neither is present. `gh` exits non-zero on that, so
`gh_search` reports it as a failed probe rather than a zero — verified, not
assumed. A caller that only tested for an empty item list would read a malformed
query as *nothing found*, which is the failure mode this whole file exists to
prevent.

**Not** measured: any forum, social platform, blog, aggregator, or search engine.
The honest form of a zero from this script is *"no external mention anywhere
GitHub can see"* — a property of what this script queries, not evidence about the
world. Print that sentence with the number or the number will be read as more
than it is.

*Corrected c266 (2026-07-29 22:3xZ).* Until this cycle the closing sentence gave
the **reason** for that gap as *"no forum, social platform, blog, aggregator or
search engine is reachable from this deployment"*. Measured rather than assumed:
`duckduckgo.com`, `html.duckduckgo.com`, `bing.com`, `lobste.rs` and
`news.ycombinator.com` all answer **200** through the `HTTP_PROXY` egress audit,
and DuckDuckGo's HTML endpoint returned real results for `retinue-os` and
`retinue-os-chamber` — the org page, `retinue-os-deployment`, the chamber repo
and its README are indexed. The gap is unwritten queries, not an unreachable
network, and the wrong reason mattered: it retired a whole measurement class
(reach off GitHub) that c258 separately reported as unmeasured. A limit stated as
a property of the environment must be probed like any other claim (guardrail 3
applied to my own instruments, c179).

Usage
-----
    python3 tools/mentions-check.py

Exit status
-----------
    0  every hit was read and rejected — a measured, genuine zero
    1  something needs a human read: a confirmed mention, an unclassifiable hit,
       or a probe that failed (a failed probe is never reported as zero)

Instrument discipline
---------------------
Per the standing rule adopted at c227, the classifier runs against known-good and
known-bad fixtures on every invocation and the script refuses to report on live
data if they do not come out as expected. The known-bad fixtures are the two real
false positives c233 found, quoted from the issues themselves — so this check
reproduces the defect it was written for rather than merely agreeing with itself.
"""

import json
import re
import subprocess
import sys

ORG = "Retinue-OS"

# The discriminator. A hit counts only if it carries a token that cannot be
# produced by the tokenizer splitting an unrelated word: the hyphenated org
# name, one of the repo paths, the Pages host, or a project-unique repo name.
#
# Deliberately strict. "retinue" alone is a common English noun (and a Warhammer
# keyword); "retinue os" with a space is ambiguous and is rejected. A false
# negative here costs one missed mention that the next probe will see again; a
# false positive puts a Warhammer bug report on a public dashboard as interest in
# this project.
CONFIRM_RE = re.compile(
    r"""(
          retinue-os                    # the org name, hyphen intact
        | retinue[-_]os\.github\.io     # the Pages host
        | github\.com/retinue           # any link into the org or its repos
        | qlever-dir                    # project-unique repo name, hyphen intact
        | retinue-os-chamber
        | retinue-os-deployment
    )""",
    re.IGNORECASE | re.VERBOSE,
)

# Fixtures. The two bad ones are verbatim excerpts of the real false positives.
KNOWN_BAD = [
    # BSData/horus-heresy-2nd-edition#2982, 2023-11-06
    "Phoenix Terminators are still available as a retinue despite pg 107 ... "
    "Retinue tag must be disabled when Legiones Hereticus option is selected\n"
    "OS: Android\nApp: Battlescribe",
    # BSData/horus-heresy-2nd-edition#2340, 2022-09-09
    "Centurion Delegatus no longer has access to a retinue ... "
    "Device and data\n - OS: Android\n - BattleScribe version: v2.03.25.338",
    # The shape a lazy discriminator would accept: right words, no project.
    "We run a retinue of agents on this OS and index them with a dir of qlever "
    "files.",
]

# Word-level matchers for the label check below. Written as regexes with real
# boundaries because the first version of that check split the label on
# whitespace and looked for the token "pr" — which does not match "PRs", the
# exact wording of the two probes it was written to catch. It passed the
# pre-c243 probe set on the first replay. A guard that agrees with the fix but
# not with the defect is decoration.
PR_WORD_RE = re.compile(r"\b(prs?|pull[- ]requests?)\b", re.IGNORECASE)
ISSUE_WORD_RE = re.compile(r"\bissues?\b", re.IGNORECASE)

KNOWN_GOOD = [
    "Saw this in https://github.com/Retinue-OS/retinue — the sidecar gateway "
    "design is worth a read.",
    "Their converter contract (retinue-os/qlever-dir) turns frontmatter into "
    "triples.",
    "Docs are at https://retinue-os.github.io/retinue-os-chamber/",
]


def self_test():
    """Refuse to report if the classifier does not reproduce c233's finding."""
    failures = []
    for text in KNOWN_BAD:
        if CONFIRM_RE.search(text):
            failures.append(f"known-bad accepted: {text[:60]!r}")
    for text in KNOWN_GOOD:
        if not CONFIRM_RE.search(text):
            failures.append(f"known-good rejected: {text[:60]!r}")
    return failures


def probe_test():
    """Check each probe's label against the query it actually runs (c243).

    A classifier fixture cannot catch a probe that searches the wrong half of a
    surface: the hits it never receives are the ones it cannot misclassify. The
    defect this reproduces is the real one — two probes labelled *"issues and
    PRs"* running `is:issue`, which excludes every pull request.

    Two rules, both structural:

    1. A `/search/issues` query must carry `is:issue` or `is:pull-request`, or
       GitHub answers 422 (c242) — a probe that cannot run is worse than one that
       runs wrong, because its zero looks identical.
    2. The label must name the half the qualifier selects. A label is a claim
       about what was measured; it is published in this script's output and
       copied into log entries, so it is read by people who never see the query.
    """
    failures = []
    for label, endpoint, query, _extractor, _accept in PROBES:
        if endpoint != "issues":
            continue
        is_issue = "is:issue" in query
        is_pr = "is:pull-request" in query
        low = label.lower()
        if not (is_issue or is_pr):
            failures.append(f"probe {label!r}: no is:issue/is:pull-request — 422")
            continue
        if is_issue and is_pr:
            failures.append(f"probe {label!r}: both qualifiers, GitHub takes one")
            continue
        if is_issue and PR_WORD_RE.search(low):
            failures.append(f"probe {label!r}: label claims PRs, query is is:issue")
        if is_pr and ISSUE_WORD_RE.search(low):
            failures.append(f"probe {label!r}: label claims issues, query is PRs")
    return failures


def gh_search(endpoint, query, accept=None):
    """Run one search. Returns (items, error). An error is never a zero."""
    cmd = ["gh", "api", "-X", "GET", f"/search/{endpoint}", "--field", f"q={query}"]
    if accept:
        cmd += ["-H", f"Accept: {accept}"]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, str(exc)
    if out.returncode != 0:
        return None, out.stderr.strip().splitlines()[-1] if out.stderr else "gh failed"
    try:
        payload = json.loads(out.stdout)
    except json.JSONDecodeError as exc:
        return None, f"unparseable response: {exc}"
    return payload.get("items", []), None


def text_of_issue(item):
    return f"{item.get('title') or ''}\n{item.get('body') or ''}"


def text_of_repo(item):
    return (
        f"{item.get('full_name') or ''}\n"
        f"{item.get('description') or ''}\n"
        f"{item.get('homepage') or ''}"
    )


def text_of_code(item):
    # Code hits carry no content without a text-match media type; the repo/path
    # pair is all that is reliably present, so a code hit that the path does not
    # settle is reported as unclassified rather than guessed at.
    frags = " ".join(
        m.get("fragment", "") for m in item.get("text_matches", []) or []
    )
    repo = (item.get("repository") or {}).get("full_name", "")
    return f"{repo}\n{item.get('path') or ''}\n{frags}"


def url_of(item):
    return (
        item.get("html_url")
        or item.get("url")
        or (item.get("repository") or {}).get("html_url", "")
    )


PROBES = [
    (
        "issues naming the org",
        "issues",
        f'is:issue "retinue-os" -org:{ORG}',
        text_of_issue,
        None,
    ),
    (
        "PRs naming the org",
        "issues",
        f'is:pull-request "retinue-os" -org:{ORG}',
        text_of_issue,
        None,
    ),
    (
        "issues naming qlever-dir",
        "issues",
        f'is:issue "qlever-dir" -org:{ORG}',
        text_of_issue,
        None,
    ),
    (
        "PRs naming qlever-dir",
        "issues",
        f'is:pull-request "qlever-dir" -org:{ORG}',
        text_of_issue,
        None,
    ),
    (
        "repositories matching the org name",
        "repositories",
        "retinue-os",
        text_of_repo,
        None,
    ),
    (
        "code linking to the Pages site",
        "code",
        f'"retinue-os.github.io" -org:{ORG}',
        text_of_code,
        "application/vnd.github.text-match+json",
    ),
    (
        "code linking into the org",
        "code",
        f'"Retinue-OS/retinue" -org:{ORG}',
        text_of_code,
        "application/vnd.github.text-match+json",
    ),
]


def main():
    failures = self_test() + probe_test()
    if failures:
        print("self-test: FAIL — refusing to report on live data")
        for line in failures:
            print(f"  {line}")
        return 1
    print(
        f"self-test: pass ({len(KNOWN_GOOD) + len(KNOWN_BAD)} classifier cases, "
        f"{len(PROBES)} probes label-checked)"
    )

    confirmed, unclassified, errors = [], [], []
    total_raw = 0

    for label, endpoint, query, extractor, accept in PROBES:
        items, error = gh_search(endpoint, query, accept)
        if error is not None:
            errors.append((label, error))
            print(f"  ERROR    {label}: {error}")
            continue
        total_raw += len(items)
        kept = []
        for item in items:
            # Own-org hits are excluded by the query, but repository search has
            # no -org qualifier, so filter them here too.
            owner = (item.get("full_name") or url_of(item) or "").lower()
            if f"{ORG.lower()}/" in owner or owner.startswith(
                f"https://github.com/{ORG.lower()}/"
            ):
                continue
            text = extractor(item)
            if CONFIRM_RE.search(text):
                kept.append(item)
                confirmed.append((label, url_of(item)))
            elif endpoint == "code":
                unclassified.append((label, url_of(item)))
        print(f"  {len(items):3d} raw  {len(kept):2d} confirmed  {label}")

    print()
    print(f"raw hits {total_raw}, confirmed {len(confirmed)}, "
          f"unclassified {len(unclassified)}, failed probes {len(errors)}")

    for label, url in confirmed:
        print(f"  CONFIRMED    {url}   ({label})")
    for label, url in unclassified:
        print(f"  UNCLASSIFIED {url}   ({label})   — read it before counting it")

    if errors:
        print("\nA failed probe is not a zero. Re-run before recording a reading.")
        return 1
    if confirmed or unclassified:
        return 1

    print(
        "\nNo external mention anywhere GitHub can see. This covers GitHub only —\n"
        "this script queries no search engine, so the wider web is unmeasured by\n"
        "IT, not unmeasurable: general HTTPS egress works from this deployment and\n"
        "a search engine answered on 2026-07-29 (c266). Reachability is not the\n"
        "reason for the gap; nobody has written the queries yet."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
