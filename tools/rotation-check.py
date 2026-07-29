#!/usr/bin/env python3
"""Find append-only files in this chamber that no rotation threshold covers.

Why this exists
---------------
`strategy.md` (c145) says a public artifact can fail silently by growing:
GitHub's `POST /markdown` and its blob renderer both refuse input above 400 KB,
so past that size a Markdown file is served as unrendered source at a URL that
still returns 200. Nothing warns anyone.

c190 generalized the remedy — *"every append-only file in this chamber
rotates"* — and then instrumented exactly two files, `log.md` (300 KB) and
`projects/public-surface.md` (200 KB). The rotation watch line in every log
entry has enumerated those same two by hand ever since.

Measured at c236, `strategy.md` is the third: **strictly non-decreasing across
all 31 of its revisions**, 3.2 KB → 84 KB in ten days, linked from `README.md`,
and named by no threshold and no watch line. It was not missed because anyone
judged it low-risk; it was missed because the rule was carried in prose and the
watch was carried in a habit, and neither enumerates.

This script enumerates. It is the same shape as `render-check.py`: the defect
recurs because appending is done by a process with no check attached, so the
check is the fix rather than another hand-correction.

Usage
-----
    python3 tools/rotation-check.py [chamber-root]      # default: repo root

Exit status is 1 if any file is uncovered, due for rotation, or approaching the
renderer's hard limit; 0 otherwise.

Instrument discipline
---------------------
Per the standing rule adopted at c227 — a new instrument gets a known-good and a
known-bad case before its first result is believed — the classifier runs against
synthetic size series on every invocation and the script refuses to report on
real files if they do not behave as expected. An all-pass result from an
unvalidated checker is indistinguishable from a checker that always passes.
"""

import os
import subprocess
import sys

KB = 1024

# Rotation thresholds, mirroring the rule in strategy.md. A file listed here is
# covered; a growing file not listed here is the thing this script looks for.
THRESHOLDS = {
    "log.md": 300 * KB,
    "projects/public-surface.md": 200 * KB,
    "strategy.md": 150 * KB,
}

# Archive parts are terminal by design: a full part is left alone and a new part
# started. They still have to render, so they are size-checked but never
# reported as uncovered.
ARCHIVE_PREFIXES = ("log-archive/", "projects-archive/")

# GitHub refuses to render Markdown above this. Report well before it.
RENDER_LIMIT = 400 * KB
RENDER_WARN = 320 * KB

# Below this, a monotonic file is not yet worth a threshold: every file is
# monotonic before it has ever been edited downwards, and saying so for a 5 KB
# draft is noise, not a finding.
WATCH_FLOOR = 40 * KB


def run(args, cwd):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True).stdout


def size_history(path, cwd):
    """Sizes of every committed revision of `path`, oldest first."""
    revs = run(["git", "log", "--format=%H", "--", path], cwd).split()
    sizes = []
    for rev in reversed(revs):
        out = run(["git", "cat-file", "-s", f"{rev}:{path}"], cwd).strip()
        if out.isdigit():
            sizes.append(int(out))
    return sizes


def is_append_only(sizes, min_revs=4):
    """True when a file's length has never decreased over enough revisions.

    Fewer than `min_revs` revisions is not evidence: a file committed twice is
    monotonic by coincidence. This is a heuristic and is reported as one.
    """
    if len(sizes) < min_revs:
        return False
    return all(b >= a for a, b in zip(sizes, sizes[1:]))


def self_test():
    """Known-good and known-bad cases for the classifier."""
    cases = [
        ([1, 2, 3, 4, 5], True, "strictly growing"),
        ([1, 1, 2, 2, 3], True, "growing with repeats"),
        ([1, 2, 3, 2, 4], False, "one decrease = has been rotated/edited down"),
        ([5, 4, 3, 2, 1], False, "shrinking"),
        ([1, 2], False, "too few revisions to judge"),
    ]
    for sizes, expected, why in cases:
        if is_append_only(sizes) != expected:
            return f"classifier failed the {why!r} case"
    return None


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."

    failure = self_test()
    if failure:
        print(f"SELF-TEST FAILED: {failure}")
        print("Refusing to report on real files.")
        return 2
    print("self-test: pass (5 cases)")

    files = run(["git", "ls-files", "*.md"], root).split()
    problems = []
    covered = []

    for path in sorted(files):
        # Measure the working tree, not HEAD. The check exists to catch a file
        # crossing its threshold, and the crossing happens in the append that is
        # still uncommitted when this runs; reading `HEAD:<path>` reports the
        # size before that append and so lags by exactly one commit — which is
        # c235's finding (the check and the surface it protects are not the same
        # object) recurring in the instrument written one cycle after it. Git
        # history is still the source for the *classification* below, because
        # "does this file ever shrink" is a question only the history answers.
        # Deleted-but-tracked files fall back to HEAD's size.
        full = os.path.join(root, path)
        if os.path.exists(full):
            size = os.path.getsize(full)
        else:
            blob = run(["git", "cat-file", "-s", f"HEAD:{path}"], root).strip()
            size = int(blob) if blob.isdigit() else 0

        if size >= RENDER_WARN:
            pct = 100 * size / RENDER_LIMIT
            problems.append(
                f"RENDER  {size/KB:7.0f} KB  {path}  "
                f"({pct:.0f}% of GitHub's {RENDER_LIMIT//KB} KB render limit)"
            )

        if path.startswith(ARCHIVE_PREFIXES):
            continue

        threshold = THRESHOLDS.get(path)
        if threshold is not None:
            covered.append((path, size, threshold))
            if size >= threshold:
                problems.append(
                    f"DUE     {size/KB:7.0f} KB  {path}  "
                    f"(threshold {threshold//KB} KB — rotate)"
                )
            continue

        if size >= WATCH_FLOOR and is_append_only(size_history(path, root)):
            problems.append(
                f"UNCOVERED {size/KB:5.0f} KB  {path}  "
                f"(append-only, no threshold in strategy.md)"
            )

    for path, size, threshold in covered:
        print(f"covered   {size/KB:7.0f} KB / {threshold//KB:4} KB  {path}")

    if not problems:
        print(f"\n{len(files)} tracked Markdown files, 0 problems.")
        return 0

    print()
    for line in problems:
        print(line)
    print(f"\n{len(files)} tracked Markdown files, {len(problems)} problem(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
