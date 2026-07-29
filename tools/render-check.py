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
    python3 tools/render-check.py --offline [path]   # no network, no `gh`

Exit status is 1 if any file's rendered row count differs from its source row
count, 0 otherwise.

Two detectors, not one
---------------------
The row-count comparison above needs the live renderer and answers *whether* a
file is broken. It does not answer *where*: at c245 it reported `expected 196,
rendered 195` on a 145 KB register and locating the blank line took a hand-written
scan. So there is a second, purely local detector — `orphan_runs()` — which finds
the signature directly: a contiguous run of pipe-lines carrying no `|---|`
delimiter is a table fragment that lost its header, which is what a blank line
inside a table produces. It reports `file:line`, needs no network, and measured
**zero** false positives across all 61 tracked Markdown files of this chamber at
c245.

That second detector is why `--offline` exists, and `--offline` is why the
pre-commit hook exists (`tools/install-hook.sh`). c245 was the third occurrence
of this defect in this file (c200, c227, c244) and the first *after* this script
was written to catch it: the instrument was never wrong, it was never run on the
wake-up that appended the row. A check that depends on remembering to run it has
the reliability of the memory, not of the check — so the local half runs from a
hook, where forgetting is not an available failure. The network half stays in the
survey, where an outage can only delay a report instead of blocking a commit.

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


def orphan_runs(text):
    """Locate table fragments with no header, without asking the renderer.

    Returns a list of (start_line, end_line, delimiter_count) for every
    contiguous run of pipe-lines that does not carry exactly one `|---|`
    delimiter row. A well-formed GFM table is exactly one such run with exactly
    one delimiter; a blank line inside one splits it into a good run and an
    orphan, and the orphan is what GitHub renders as a paragraph of pipes.
    """
    lines = text.split('\n')
    in_fence = False
    runs = []
    cur = None
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith('|'):
            cur = [number, number] if cur is None else [cur[0], number]
        elif cur is not None:
            runs.append(cur)
            cur = None
    if cur is not None:
        runs.append(cur)

    orphans = []
    for start, end in runs:
        delims = sum(1 for line in lines[start - 1:end]
                     if DELIM.match(line.strip()) and '-' in line)
        if delims != 1:
            orphans.append((start, end, delims))
    return orphans


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


def local_self_test():
    """Confirm the local detector separates a good table from a broken one.

    Same c227 discipline as the network half: an all-clear from an unvalidated
    checker is indistinguishable from a checker that always passes, and this one
    is the half that gates commits.
    """
    if orphan_runs(GOOD):
        return False, 'known-good fixture reported an orphan run'
    bad = orphan_runs(BAD)
    if len(bad) != 1 or bad[0][0] != 7:
        return False, 'known-bad fixture: expected one orphan at line 7, got %r' % (bad,)
    # A table inside a fenced code block is documentation, not markup.
    fenced = '```\n| A | B |\n\n| 1 | 2 |\n```\n'
    if orphan_runs(fenced):
        return False, 'fenced example reported as an orphan run'
    return True, '3 cases'


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
    argv = [a for a in sys.argv[1:] if a != '--offline']
    offline = '--offline' in sys.argv[1:]
    root = os.path.abspath(argv[0] if argv else
                           os.path.join(os.path.dirname(__file__), '..'))

    ok, detail = local_self_test()
    print('local self-test: %s (%s)' % ('pass' if ok else 'FAIL', detail))
    if not ok:
        print('refusing to report on real files with an unvalidated instrument')
        return 2

    if not offline:
        ok, detail = self_test()
        print('renderer self-test: %s (%s)' % ('pass' if ok else 'FAIL', detail))
        if not ok:
            print('refusing to report on real files with an unvalidated instrument')
            return 2

    failures = 0
    checked = 0
    scanned = 0
    for path in sorted(glob.glob(root + '/**/*.md', recursive=True)):
        if '/.git/' in path:
            continue
        with open(path, encoding='utf-8', errors='replace') as handle:
            text = handle.read()
        pipe, delim = source_rows(text)
        if pipe == 0:
            continue
        rel = os.path.relpath(path, root)
        scanned += 1

        for start, end, delims in orphan_runs(text):
            print('%s:%d-%d ORPHAN TABLE ROWS (%d delimiter rows in the run; a '
                  'blank line above line %d ends the table, so these render as '
                  'a paragraph of pipes)' % (rel, start, end, delims, start))
            failures += 1

        if offline:
            continue

        expected = pipe - delim
        got, err = rendered_rows(text)
        if got is None:
            print('%-55s render failed: %s' % (rel, err))
            failures += 1
            continue
        checked += 1
        if got != expected:
            print('%-55s MISMATCH expected %d rows, rendered %d'
                  % (rel, expected, got))
            failures += 1

    if offline:
        print('%d files with tables scanned locally, %d problem(s)'
              % (scanned, failures))
    else:
        print('%d files with tables checked, %d problem(s)' % (checked, failures))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
