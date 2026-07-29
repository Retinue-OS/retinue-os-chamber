#!/usr/bin/env python3
"""Check the served dashboard against its freshness bound — all five cards, not one.

Why this exists
---------------
Every wake-up runs a mandatory delivery check: fetch the published
`data/briefing.json` from the Pages site and compare its `generated` stamp
against a 26 h bound. The bound is a claim about *what a reader sees*, so the
check deliberately reads the served copy rather than the file on disk.

That much is right. What it is not is *complete*: the dashboard has five data
files, the check reads one of them, and one file has been standing proxy for
the class across every run since the rule was written. `strategy.md` has
already found this shape twice — c190 wrote "every append-only file rotates"
and then instrumented two, and c235 found that a lesson kept in prose does not
propagate to an instrument written later. This is the same error in the check
that is run most often.

Measured before writing this (2026-07-29, over all 22 commits that have ever
touched `docs/data/`):

  * **4 commits published a divergent stamp set** — 08fda04, 398646b, 3492991,
    5611265, all on 2026-07-19/20 — where some cards carried a newer
    `generated` than others. Partial regeneration is not hypothetical.
  * In **all four**, `briefing.json` happened to be among the *stale* files, so
    a briefing-only check would have caught them. The silent direction — a
    fresh `briefing.json` beside a stale `todo.json` — has never occurred.

So this is a latent gap, not a live defect, and it is reported as one. Nothing
prevents the silent direction: the refresh job writes the five sequentially
under a 900 s `SCHEDULER_JOB_TIMEOUT` that kills it with no partial result and
no notice, and `todo.json` — the owner's queue — is the card whose staleness
would matter most and whose staleness the current check cannot see.

The remedy is enumeration, not a longer rule. The file list comes from the
served directory's local mirror rather than a constant here, so a sixth card
added later is covered on the day it is added.

Usage
-----
    python3 tools/delivery-check.py [chamber-root]
    python3 tools/delivery-check.py --offline      # skip the network, disk only

Exit status is 1 if any card is past the bound, disagrees with its disk copy,
or disagrees with its siblings; 0 otherwise; 2 if the self-test fails.

Instrument discipline
---------------------
Per the standing rule adopted at c227, the classifier runs known-good and
known-bad cases on every invocation and the script refuses to report on real
files if they do not behave as expected. The known-bad cases include the exact
failure this instrument was written for — one fresh card beside four stale ones
— so it reproduces the defect rather than merely agreeing with the fix.
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

BASE = "https://retinue-os.github.io/retinue-os-chamber/data"
DATA_DIR = "docs/data"
BOUND = timedelta(hours=26)
TIMEOUT = 30


def parse(stamp):
    """`2026-07-28T17:54:59Z` -> aware datetime. None when unparseable."""
    try:
        return datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except (ValueError, TypeError):
        return None


def classify(now, served, disk):
    """Verdicts for one card. `served`/`disk` are `generated` strings or None.

    Attribution follows the rule the wake-up prompt states: a stale served copy
    is a *refresh* failure when the disk copy is stale too, and a *delivery*
    failure when the disk copy is fresh. Getting that the wrong way round sends
    the next wake-up to regenerate files that were already correct.
    """
    problems = []
    s, d = parse(served), parse(disk)

    if served is not None and s is None:
        problems.append(f"UNPARSED served stamp {served!r}")
    if disk is not None and d is None:
        problems.append(f"UNPARSED disk stamp {disk!r}")
    if served is None:
        problems.append("NOT SERVED (fetch failed or no `generated` key)")
    if disk is None:
        problems.append("NOT ON DISK")

    if s is not None and now - s > BOUND:
        age = now - s
        if d is not None and now - d > BOUND:
            problems.append(
                f"STALE {age} past the {BOUND} bound — disk copy is stale too: "
                "the refresh job did not complete. Regenerate the five files."
            )
        else:
            problems.append(
                f"STALE {age} past the {BOUND} bound — disk copy is fresh: "
                "the refresh ran and publication broke. Do not regenerate; "
                "check /pages and /pages/builds."
            )
    elif s is not None and d is not None and s != d:
        problems.append(
            f"LAG served {served} behind disk {disk} — a commit is unpublished "
            "or Pages has not built it yet. Both are inside the bound."
        )
    return problems


def self_test():
    now = datetime(2026, 7, 29, 12, 0, 0, tzinfo=timezone.utc)
    fresh, stale = "2026-07-29T06:00:00Z", "2026-07-27T06:00:00Z"
    cases = [
        (classify(now, fresh, fresh), False, "fresh and agreeing"),
        (classify(now, stale, stale), True, "both stale = refresh failure"),
        (classify(now, stale, fresh), True, "served stale = delivery failure"),
        (classify(now, fresh, stale), True, "served ahead of disk"),
        (classify(now, None, fresh), True, "not served"),
        (classify(now, "not-a-date", fresh), True, "unparseable stamp"),
    ]
    for got, expect_problem, why in cases:
        if bool(got) != expect_problem:
            return f"classifier failed the {why!r} case"
    # The failure this instrument exists for: one card fresh, the rest stale.
    # A briefing-only check passes here; enumeration must not.
    cards = {"briefing": fresh, "todo": stale, "agenda": stale,
             "messages": stale, "projects": stale}
    if classify(now, cards["briefing"], cards["briefing"]):
        return "known-good briefing case reported a problem"
    if not any(classify(now, v, v) for k, v in cards.items() if k != "briefing"):
        return "the four stale siblings were not detected"
    if len(set(cards.values())) < 2:
        return "divergence fixture is not divergent"
    return None


def fetch(name):
    try:
        with urllib.request.urlopen(f"{BASE}/{name}", timeout=TIMEOUT) as r:
            return json.loads(r.read()).get("generated")
    except Exception:
        return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    offline = "--offline" in sys.argv
    root = args[0] if args else "."

    failure = self_test()
    if failure:
        print(f"SELF-TEST FAILED: {failure}")
        print("Refusing to report on real files.")
        return 2
    print("self-test: pass (6 cases + the divergence fixture)")

    data_dir = os.path.join(root, DATA_DIR)
    names = sorted(f for f in os.listdir(data_dir) if f.endswith(".json"))
    if not names:
        print(f"no JSON files under {DATA_DIR} — nothing to check")
        return 1

    now = datetime.now(timezone.utc)
    problems, disk_stamps = [], {}

    for name in names:
        try:
            with open(os.path.join(data_dir, name)) as fh:
                disk = json.load(fh).get("generated")
        except Exception:
            disk = None
        served = None if offline else fetch(name)
        disk_stamps[name] = disk

        age = ""
        ref = parse(served if not offline else disk)
        if ref:
            age = f"  age {str(now - ref).split('.')[0]}"
        print(f"  {name:16} disk {disk}  served "
              f"{'(skipped)' if offline else served}{age}")

        for p in classify(now, disk if offline else served, disk):
            problems.append(f"{name}: {p}")

    # The cross-card check, which is the whole reason this file exists: five
    # cards from one regeneration carry one stamp. Two stamps means a partial
    # run reached the reader, and the card a single-file check happens to read
    # says nothing about the other four.
    distinct = {s for s in disk_stamps.values() if s}
    if len(distinct) > 1:
        problems.append(
            "DIVERGENT stamp set across cards — partial regeneration: "
            + ", ".join(f"{n}={s}" for n, s in sorted(disk_stamps.items()))
        )

    print()
    if not problems:
        print(f"{len(names)} cards, one stamp, 0 problems"
              + (" (offline: disk only)" if offline else ""))
        return 0
    for p in problems:
        print(p)
    print(f"\n{len(names)} cards, {len(problems)} problem(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
