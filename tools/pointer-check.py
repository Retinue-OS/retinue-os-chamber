#!/usr/bin/env python3
"""Check that every write-up pointer in this chamber resolves, and resolves where it says.

Why this exists
---------------
`projects/public-surface.md` is an index (the register table) plus evidence
(per-cycle `##` write-ups), and the evidence rotates into `projects-archive/`
while the index stays (c216). So every register row carries a **pointer** to the
write-up holding its evidence, in one of two forms:

    Detail: §c213 below.
    Detail: §c213 in [archive part 2](../projects-archive/public-surface-c184-c210.md).

c215 wrote a check for these and c237 fixed its pattern. Both versions ask one
question — *does a write-up with this number exist anywhere?* — by `comm`-ing the
pointer numbers against the h2 headings of the live file **and** the archive parts
combined. That check was clean immediately before the c239 rotation and clean
immediately after it, while **26 rows in between said "below" about sections that
had just been moved into an archive part**. It could not have been otherwise: a
union tells you a section exists somewhere, and "below" is a claim about *where*.

c216 already named this blindness, in prose, in the file the rotation edits:
*"a distinction the check itself cannot make, since `comm` accepts the archive and
would have stayed empty while seventeen rows pointed the wrong way."* Three
rotations later the same 26 pointers were still being repaired by hand and found
by `grep`. That is c235's lesson for the fifth time — **a lesson recorded in prose
does not propagate to an instrument; only an edit to an instrument does** — so
this script is the edit.

What it checks
--------------
1. **Existence** (c215/c237's question, kept): every `Detail: §cNNN` resolves to
   a `##` write-up in the live file or in some archive part.
2. **Direction** (the half that was missing): a pointer saying *below* must
   resolve **in its own file**; a pointer naming an archive part must resolve
   **in that part**, and that part must exist.

Both failures are silent to a reader: a "below" pointer into a rotated section
renders as ordinary prose and sends someone scrolling to the end of a 112 KB file
for a section that left three days ago.

Usage
-----
    python3 tools/pointer-check.py [chamber-root]      # default: repo root

Exit status is 1 if any pointer dangles or points the wrong way, 0 otherwise.

Instrument discipline
---------------------
Per c227 — a new instrument gets a known-good and a known-bad case before its
first result is believed — the resolver runs against synthetic fixtures on every
invocation and the script **refuses to report on real files** if they do not come
out as expected. An all-pass result from an unvalidated checker is
indistinguishable from a checker that always passes.
"""

import os
import re
import subprocess
import sys

# "Detail: §c213 below." / "Detail: §c213 in [archive part 2](../path/to.md)."
POINTER = re.compile(
    r"Detail: §c(?P<cycle>\d+) (?:(?P<below>below)|in \[[^\]]*\]\((?P<link>[^)]+)\))"
)
# c215's invariant with c237's §-tolerant form: "## c211", "## §c224", "## Cycle 210"
HEADING = re.compile(r"(?m)^## §?(?:Cycle )?c?(\d+)\b")


def headings(text):
    return {int(n) for n in HEADING.findall(text)}


def check_text(path, text, load):
    """Yield problems for one file. `load(relpath) -> text or None` resolves links."""
    for m in POINTER.finditer(text):
        cycle = int(m.group("cycle"))
        if m.group("below"):
            if cycle not in headings(text):
                yield f"WRONG-WAY  {path}: §c{cycle} says 'below', not an h2 in this file"
            continue
        link = m.group("link")
        target = load(os.path.normpath(os.path.join(os.path.dirname(path), link)))
        if target is None:
            yield f"MISSING    {path}: §c{cycle} points at {link}, which does not exist"
        elif cycle not in headings(target):
            yield f"WRONG-WAY  {path}: §c{cycle} points at {link}, which has no such h2"


GOOD = "Detail: §c7 below.\n\n## c7 — a write-up\n"
BAD_BELOW = "Detail: §c7 below.\n\n## c8 — a different write-up\n"
BAD_LINK = "Detail: §c7 in [part 1](../a/gone.md).\n"


def self_test():
    ok = not list(check_text("f.md", GOOD, lambda p: None))
    bad1 = len(list(check_text("f.md", BAD_BELOW, lambda p: None))) == 1
    bad2 = len(list(check_text("f.md", BAD_LINK, lambda p: None))) == 1
    # a link that resolves to a part actually containing the h2 must pass
    ok2 = not list(
        check_text("x/f.md", "Detail: §c7 in [part 1](../a/p.md).", lambda p: "## c7 x")
    )
    return ok and ok2 and bad1 and bad2


def tracked_markdown(root):
    out = subprocess.run(
        ["git", "-C", root, "ls-files", "*.md"], capture_output=True, text=True
    )
    return [p for p in out.stdout.split("\n") if p]


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if not self_test():
        print("self-test FAILED — refusing to report on real files", file=sys.stderr)
        return 2
    print("self-test: pass (4 cases)")

    cache = {}

    def load(relpath):
        if relpath not in cache:
            full = os.path.join(root, relpath)
            try:
                cache[relpath] = open(full, encoding="utf-8").read()
            except OSError:
                cache[relpath] = None
        return cache[relpath]

    problems, pointers, files = [], 0, tracked_markdown(root)
    for path in files:
        text = load(path)
        if text is None:
            continue
        pointers += len(POINTER.findall(text))
        problems.extend(check_text(path, text, load))

    if not problems:
        print(f"{len(files)} tracked Markdown files, {pointers} pointers, 0 problems.")
        return 0

    print()
    for line in problems:
        print(line)
    print(f"\n{len(files)} tracked Markdown files, {pointers} pointers, {len(problems)} problem(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
