#!/usr/bin/env python3
"""Check that this public chamber does not name the organisation's private
repositories.

Why this exists
---------------
Guardrail 5: nothing about the owner gets published beyond what he has already
made public.  A repository he keeps private is, by construction, not public —
its name is not visible to anyone outside the org, and naming it here would
publish it.  Cycle 176 found the five generated dashboard documents doing
exactly that and removed the name from all five.  Cycles 222, 223 and 229 then
wrote it into `log.md`, because the fix had been applied where the defect was
found and nothing stopped the next wake-up from re-introducing it.  This is the
same shape as `render-check.py`: a remedy that is a check, not a hand fix.

The list of names is **derived at run time** from the GitHub API, never stored.
Committing a list of private repository names into a public repo in order to
grep for them would be the defect wearing a hat.

Output is **masked by default** (`<private-repo-1>`), because this script's own
output is the thing most likely to be pasted into the public log.  `--show-names`
prints them for interactive use.

Scope, and why it has two halves
--------------------------------
* **Forward surfaces** — everything except the append-only record.  Any
  occurrence is a failure (exit 1); these files are edited and regenerated, so
  they can simply be corrected.
* **The append-only record** (`log.md`, `log-archive/`) — reported as a count
  only.  Rewriting a public log is worse than the leak it would repair, the
  names are in git history regardless, and that history decision has sat with
  the owner since 2026-07-19 (dashboard thread `78b64be7…`).  What the count is
  for is noticing whether the *next* entry adds one.

  **That noticing is mechanical since cycle 313, because it was not before.**
  The sentence above left the comparison to a reader who remembers yesterday's
  number, and a cold-start agent remembers nothing: c313 appended a private
  repository's name to `log.md`, the check reported it as `history … 1
  (informational)`, and only the *forward*-surface copy of the same sentence
  raised an error.  Had the handover not carried it too, a new leak would have
  been printed as a routine line and committed.  So the history half now
  compares its **total across all history files** against the same total at
  `HEAD`: a rotation moves occurrences between those files and leaves the total
  unchanged, while an append raises it.  An increase is a failure; the record is
  still never rewritten, and the fix is to redact the sentence being written now.

Usage
-----
    python3 tools/private-name-check.py [--show-names] [--org ORG]

Runs a known-good / known-bad self-test first and refuses to report on real
files if the fixtures do not separate (strategy.md, cycle 227: an all-pass from
an unvalidated checker is indistinguishable from a checker that always passes).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HISTORY = ("log.md", "log-archive/")


def sh(args: list[str], cwd: Path | None = None) -> str:
    return subprocess.run(
        args, cwd=cwd, check=True, capture_output=True, text=True
    ).stdout


def private_repo_names(org: str) -> list[str]:
    out = sh(
        [
            "gh", "repo", "list", org, "--limit", "200",
            "--json", "name,visibility",
        ]
    )
    return sorted(
        r["name"] for r in json.loads(out) if r["visibility"].upper() == "PRIVATE"
    )


def scan(root: Path, files: list[str], names: list[str]) -> dict[str, dict[str, int]]:
    """{relative path: {name: count}} for every tracked text file that names one."""
    pats = {n: re.compile(re.escape(n), re.IGNORECASE) for n in names}
    hits: dict[str, dict[str, int]] = {}
    for rel in files:
        p = root / rel
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
            continue
        found = {n: len(pat.findall(text)) for n, pat in pats.items()}
        found = {n: c for n, c in found.items() if c}
        if found:
            hits[rel] = found
    return hits


def history_grew(working: int, baseline: int) -> bool:
    """Did the append-only record gain an occurrence since `HEAD`?

    A negative baseline means there is no `HEAD` to compare against, which is
    never reported as growth — an unmeasurable baseline is not evidence.
    """
    return baseline >= 0 and working > baseline


def history_total_at_head(root: Path, names: list[str]) -> int:
    """How many times the private names appear across history files at `HEAD`.

    The invariant this defends (c313): a rotation *moves* whole entries between
    `log.md` and a `log-archive/` part, so the total is preserved; only a new
    append can raise it.  Files added since `HEAD` therefore contribute nothing
    here, which is exactly right for a freshly cut archive part.
    """
    pats = [re.compile(re.escape(n), re.IGNORECASE) for n in names]
    total = 0
    try:
        tracked = sh(["git", "ls-tree", "-r", "HEAD", "--name-only"], cwd=root).splitlines()
    except subprocess.CalledProcessError:
        return -1  # no commit yet; caller treats a negative baseline as "unknown"
    for rel in tracked:
        if not is_history(rel):
            continue
        try:
            text = sh(["git", "show", f"HEAD:{rel}"], cwd=root)
        except subprocess.CalledProcessError:
            continue
        total += sum(len(p.findall(text)) for p in pats)
    return total


def self_test() -> bool:
    """A file that names the fixture must be flagged; one that does not must not.

    Plus the c313 cases on the history baseline: a rotation that moves an
    occurrence between two history files must stay silent, and an append that
    adds one must not.
    """
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "bad.md").write_text("the fixture-private-repo is named here\n")
        (root / "good.md").write_text("this file names no private repository\n")
        hits = scan(root, ["bad.md", "good.md"], ["fixture-private-repo"])
        basic = list(hits) == ["bad.md"] and hits["bad.md"]["fixture-private-repo"] == 1

    # History-baseline arithmetic, on counts rather than on a git fixture: the
    # comparison the real run makes is `working total > HEAD total`.
    rotation = not history_grew(2, 2)    # an occurrence moved between two history files
    append = history_grew(3, 2)          # a new entry names it once more
    redaction = not history_grew(1, 2)   # a removal is not a failure
    unknown = not history_grew(5, -1)    # no baseline (no commit yet) is never a failure
    return basic and rotation and append and redaction and unknown


def is_history(rel: str) -> bool:
    return any(rel == h or rel.startswith(h) for h in HISTORY)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--org", default="retinue-os")
    ap.add_argument(
        "--show-names",
        action="store_true",
        help="print the private repository names instead of masking them",
    )
    args = ap.parse_args()

    if not self_test():
        print("self-test FAILED — fixtures do not separate; refusing to report")
        return 2
    print("self-test pass (known-good clean, known-bad flagged, 4 history-baseline cases)")

    root = Path(sh(["git", "rev-parse", "--show-toplevel"]).strip())
    names = private_repo_names(args.org)
    if not names:
        print(f"{args.org}: no private repositories — nothing to check")
        return 0

    mask = {
        n: (n if args.show_names else f"<private-repo-{i + 1}>")
        for i, n in enumerate(names)
    }
    print(f"{args.org}: {len(names)} private repositor{'y' if len(names) == 1 else 'ies'}")

    files = sh(["git", "ls-files"], cwd=root).splitlines()
    hits = scan(root, files, names)

    forward = {f: c for f, c in hits.items() if not is_history(f)}
    history = {f: c for f, c in hits.items() if is_history(f)}

    for rel, counts in sorted(history.items()):
        total = sum(counts.values())
        print(f"  history   {rel}: {total} (informational; the record is not rewritten)")

    # c313: the count above is only useful against yesterday's count, and no
    # cold-start reader has one. Compare the history total to the same total at
    # HEAD — a rotation preserves it, an append raises it.
    hist_now = sum(sum(c.values()) for c in history.values())
    hist_head = history_total_at_head(root, names)
    grew = history_grew(hist_now, hist_head)
    if grew:
        print(
            f"  PROBLEM   append-only record: {hist_head} -> {hist_now} occurrence(s) "
            f"since HEAD — an entry being written now names a private repository"
        )

    if not forward and not grew:
        print(f"{len(files)} tracked files checked, 0 problems on forward surfaces")
        return 0

    for rel, counts in sorted(forward.items()):
        for n, c in sorted(counts.items()):
            print(f"  PROBLEM   {rel}: names {mask[n]} {c}x")
    print(
        f"{len(files)} tracked files checked, "
        f"{len(forward) + (1 if grew else 0)} problem(s)"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
