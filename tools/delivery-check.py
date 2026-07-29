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

The shell is the other half of the same delivery
---------------------------------------------------
A fresh `generated` stamp is a claim about the *data*. What the reader opens is
the data **rendered by** `index.html`, `styles.css` and six web components —
eight files the card check never looked at, plus the icons and the provenance
example the front page links to. A served component older than its disk copy
renders a fresh card wrongly, and every stamp in this check still passes. So
the same enumeration argument applies one directory up: every file under
`docs/` that Pages serves is compared byte-for-byte against its disk copy, and
a mismatch is attributed rather than merely reported.

Attribution matters here for the same reason it does for the stamps. Pages
builds from `main:/docs`, so a served copy that differs from disk means either
*the commit has not been published* (disk equals `HEAD`) or *the edit has not
been committed* (disk differs from `HEAD`, and `HEAD` is what is served). Only
the first is a delivery failure; the second is a working tree mid-wake-up, and
calling it a defect would send the next cycle to inspect Pages for nothing.

Usage
-----
    python3 tools/delivery-check.py [chamber-root]
    python3 tools/delivery-check.py --offline      # skip the network, disk only

Exit status is 1 if any card is past the bound, disagrees with its disk copy,
or disagrees with its siblings, or if any served asset differs from the
committed copy behind it; 0 otherwise; 2 if the self-test fails.

Instrument discipline
---------------------
Per the standing rule adopted at c227, the classifier runs known-good and
known-bad cases on every invocation and the script refuses to report on real
files if they do not behave as expected. The known-bad cases include the exact
failure this instrument was written for — one fresh card beside four stale ones
— so it reproduces the defect rather than merely agreeing with the fix.
"""

import hashlib
import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

SITE = "https://retinue-os.github.io/retinue-os-chamber"
BASE = f"{SITE}/data"
DOCS_DIR = "docs"
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


def classify_asset(served, disk, head):
    """Verdicts for one served asset. Arguments are content digests or None.

    `served` is what the reader gets, `disk` the working tree, `head` the
    committed copy Pages builds from. Distinguishing the last two is the whole
    point: an uncommitted local edit is a wake-up in progress, not a broken
    delivery, and reporting it as one would send the next cycle to inspect
    Pages for a fault that is in this container.
    """
    problems = []
    if disk is None:
        problems.append("NOT ON DISK")
    if served is None:
        problems.append("NOT SERVED (fetch failed or 404)")
    if served is None or disk is None:
        return problems

    if served == disk:
        return problems
    if head is None:
        problems.append("UNTRACKED and differs from the served copy")
    elif disk == head:
        problems.append(
            "UNPUBLISHED — the committed copy is not what the site serves. "
            "Pages has not built it; check /pages and /pages/builds."
        )
    elif served == head:
        pass  # local edit, not yet committed. The site is correct for `main`.
    else:
        problems.append(
            "DIVERGED — served, disk and HEAD are three different files."
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

    # The asset half, both directions. `a`/`b`/`c` stand for three digests.
    a, b, c = "aaa", "bbb", "ccc"
    asset_cases = [
        (classify_asset(a, a, a), False, "served matches disk and HEAD"),
        (classify_asset(b, a, a), True, "committed copy unpublished"),
        (classify_asset(a, b, a), False, "uncommitted local edit"),
        (classify_asset(a, b, c), True, "served, disk and HEAD all differ"),
        (classify_asset(None, a, a), True, "asset not served"),
        (classify_asset(a, b, None), True, "untracked and divergent"),
    ]
    for got, expect_problem, why in asset_cases:
        if bool(got) != expect_problem:
            return f"asset classifier failed the {why!r} case"
    return None


def fetch(name):
    try:
        with urllib.request.urlopen(f"{BASE}/{name}", timeout=TIMEOUT) as r:
            return json.loads(r.read()).get("generated")
    except Exception:
        return None


def digest(data):
    return None if data is None else hashlib.sha256(data).hexdigest()[:12]


def fetch_bytes(path):
    try:
        with urllib.request.urlopen(f"{SITE}/{path}", timeout=TIMEOUT) as r:
            return r.read()
    except Exception:
        return None


def head_bytes(root, path):
    """The committed copy Pages builds from, or None when untracked."""
    try:
        out = subprocess.run(
            ["git", "-C", root, "show", f"HEAD:{DOCS_DIR}/{path}"],
            capture_output=True, timeout=TIMEOUT,
        )
        return out.stdout if out.returncode == 0 else None
    except Exception:
        return None


def walk_assets(docs_dir):
    """Every file Pages serves under `docs/`, except the data cards.

    Enumerated from the directory rather than listed here, so a component or
    an example added later is covered on the day it is added — the same reason
    the card list is not a constant.
    """
    for dirpath, dirnames, filenames in os.walk(docs_dir):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
        rel_dir = os.path.relpath(dirpath, docs_dir)
        parts = [] if rel_dir == "." else rel_dir.split(os.sep)
        if parts and parts[0] == "data":
            continue
        for fn in sorted(filenames):
            yield "/".join(parts + [fn])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    offline = "--offline" in sys.argv
    root = args[0] if args else "."

    failure = self_test()
    if failure:
        print(f"SELF-TEST FAILED: {failure}")
        print("Refusing to report on real files.")
        return 2
    print("self-test: pass (6 stamp cases + the divergence fixture, "
          "6 asset cases)")

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

    # The shell: the files that render those cards, plus everything else the
    # site serves. A stale component publishes a fresh stamp wrongly, and the
    # loop above cannot see it.
    assets = sorted(walk_assets(os.path.join(root, DOCS_DIR)))
    if not offline:
        print()
        for path in assets:
            try:
                with open(os.path.join(root, DOCS_DIR, path), "rb") as fh:
                    disk = digest(fh.read())
            except Exception:
                disk = None
            served = digest(fetch_bytes(path))
            head = digest(head_bytes(root, path))
            found = classify_asset(served, disk, head)
            mark = "  " if not found else "! "
            print(f"{mark}{path:42} disk {disk}  served {served}")
            for p in found:
                problems.append(f"{path}: {p}")

    print()
    counts = f"{len(names)} cards" + (
        "" if offline else f" + {len(assets)} assets")
    if not problems:
        print(f"{counts}, one stamp, 0 problems"
              + (" (offline: disk only)" if offline else ""))
        return 0
    for p in problems:
        print(p)
    print(f"\n{counts}, {len(problems)} problem(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
