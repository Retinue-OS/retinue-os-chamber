#!/usr/bin/env python3
"""Check that every Markdown table in this chamber survives GitHub's renderer.

Why this exists
---------------
A blank line inside a GFM table terminates it. The rows after the blank have no
header, so GitHub renders them as a paragraph of pipe characters. Nothing about
this failure is visible from the outside: the URL still returns 200, the file
still looks like a table in an editor, `grep` still finds every row, and the
triple-store converter still emits its triples.

It has happened twice in this chamber, in the same file, in three days:

  * c200 (2026-07-26) — 12 blank lines split the surface register into
    fragments; 47 of 70 rows arrived as prose. Fixed by hand.
  * c227 (2026-07-28) — 2 blank lines, added with the c223 and c224 rows;
    5 of 107 rows arrived as prose. Fixed by hand.

Both fixes removed the blank lines and neither removed the cause, which is that
appending a row to a long table is done by a process (me, at 03:00, near the end
of a wake-up) with no check attached. This script is the check. Run it before
committing anything that appends to a table.

Usage
-----
    python3 tools/render-check.py [path]      # default: the chamber root

Exit status is 1 if any file's rendered row count differs from its source row
count, 0 otherwise.

Instrument discipline
---------------------
Per the standing rule adopted at c227 — a new instrument gets a known-good and a
known-bad case before its first result is believed — this script runs both
fixtures against the live renderer on every invocation and refuses to report on
real files if the fixtures do not behave as expected. An all-pass result from an
unvalidated checker is indistinguishable from a checker that always passes.

Requires an authenticated `gh` (POST /markdown). The endpoint rejects input
above 400 KB, which is a second failure this reports rather than hides — see the
rotation rule in strategy.md.
"""

import glob
import json
import os
import re
import subprocess
import sys

DELIM = re.compile(r'^\s*\|?[\s:\-|]+\|[\s:\-|]*$')

GOOD = "# Good\n\n| A | B |\n|---|---|\n| 1 | 2 |\n| 3 | 4 |\n"
BAD = "# Bad\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n| 3 | 4 |\n"


def source_rows(text):
    """Count table rows in the source, ignoring fenced code blocks.

    Returns (pipe_lines, delimiter_lines). A well-formed table renders
    pipe_lines - delimiter_lines <tr> elements: the `|---|---|` separator is
    markup rather than a row.
    """
    in_fence = False
    pipe = delim = 0
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_fence = not in_fence
            continue
        if in_fence or not stripped.startswith('|'):
            continue
        pipe += 1
        if DELIM.match(stripped) and '-' in stripped:
            delim += 1
    return pipe, delim


def render(text):
    """Return the rendered HTML, or None plus an error string."""
    proc = subprocess.run(
        ['gh', 'api', '-X', 'POST', '/markdown', '--input', '-'],
        input=json.dumps({'mode': 'gfm', 'text': text}).encode(),
        capture_output=True)
    if proc.returncode != 0:
        return None, proc.stderr.decode('utf-8', 'replace').strip()[:200]
    return proc.stdout.decode('utf-8', 'replace'), None


def rendered_rows(text):
    html, err = render(text)
    if html is None:
        return None, err
    return html.count('<tr>'), None


def self_test():
    """Confirm the instrument separates a good table from a broken one."""
    good, err = rendered_rows(GOOD)
    if good is None:
        return False, 'renderer unreachable: %s' % err
    bad, err = rendered_rows(BAD)
    if bad is None:
        return False, 'renderer unreachable: %s' % err
    # Both fixtures have 4 pipe lines and 1 delimiter, so both *claim* 3 rows.
    if good != 3:
        return False, 'known-good fixture rendered %d rows, expected 3' % good
    if bad >= 3:
        return False, 'known-bad fixture rendered %d rows — the check is blind' % bad
    return True, 'good=%d bad=%d' % (good, bad)


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else
                           os.path.join(os.path.dirname(__file__), '..'))

    ok, detail = self_test()
    print('instrument self-test: %s (%s)' % ('pass' if ok else 'FAIL', detail))
    if not ok:
        print('refusing to report on real files with an unvalidated instrument')
        return 2

    failures = 0
    checked = 0
    for path in sorted(glob.glob(root + '/**/*.md', recursive=True)):
        if '/.git/' in path:
            continue
        with open(path, encoding='utf-8', errors='replace') as handle:
            text = handle.read()
        pipe, delim = source_rows(text)
        if pipe == 0:
            continue
        expected = pipe - delim
        got, err = rendered_rows(text)
        rel = os.path.relpath(path, root)
        if got is None:
            print('%-55s render failed: %s' % (rel, err))
            failures += 1
            continue
        checked += 1
        if got != expected:
            print('%-55s MISMATCH expected %d rows, rendered %d '
                  '(likely a blank line inside a table)' % (rel, expected, got))
            failures += 1

    print('%d files with tables checked, %d problem(s)' % (checked, failures))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
