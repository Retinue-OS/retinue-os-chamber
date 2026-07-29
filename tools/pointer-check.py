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

Except that those are two of **five** forms the register actually uses, which is
what c263 measured (c262 named the gap and did not start it). The other three:

    Detail: [c39 write-up](../projects-archive/public-surface-c033-c183.md).
    Detail: [§c256 below](#c256--2026-07-29-151x-154xz--the-budgets-were…).
    Detail: [drafts/updater-reports-dispatch-not-result.md](../drafts/…) §c257.

The pattern below matched neither, so 35 of the register's 89 pointer rows were
**skipped in silence** while the script printed *0 problems*. Ten of those 35
were dangling. A checker that parses part of a corpus and reports on the whole
of it is the c241/c262 defect in a third costume — the property that had an
instrument (the two canonical forms) was maintained; the property that did not
(everything else) drifted. So this script now (a) knows all five forms and
(b) **reports any `Detail:` in a register row it cannot parse**, so the next
form invented is loud on its first use rather than invisible until someone
greps.

The ten dangling pointers were the same story one level down: their write-ups
exist, under a heading form — `## 2026-07-25 (cycle 166) — …` — that the
heading pattern read as cycle **2026**. A grammar narrower than its corpus fails
open on both sides of the same comparison, so the cycle numbers a heading yields
are now filtered to a plausible range and the `(cycle N)` form is parsed.

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
3. **Freshness of the handover field** (added c252): a project file's
   `current_next_action` must name a cycle at least as recent as the newest
   cycle-numbered `##` section in the same file.
4. **Coverage of the check itself** (added c263): every `Detail:` appearing in a
   table row of a tracked Markdown file must parse as one of the five pointer
   forms. An unparsed one is reported as a problem, because the alternative —
   skipping it — is how 35 rows went unchecked for eight cycles. Scoped to table
   rows on purpose: prose legitimately *discusses* the convention
   (`Detail: §cNNN below`, with letters where the digits go), and a checker that
   flags a sentence about itself teaches people to ignore it.

The first two failures are silent to a reader: a "below" pointer into a rotated
section renders as ordinary prose and sends someone scrolling to the end of a
112 KB file for a section that left three days ago.

The third is silent in a worse way, because its reader is the next wake-up.
`current_next_action` is the field a cold agent reads to learn where a thread
stands (`.retinue/agents/aros.md`: *check `log.md`, `projects/` and `drafts/` so
you don't redo what a previous you already did*). When a cycle appends its
write-up and forgets the field, what stays behind is not an empty slot but a
well-formed, recent-looking, **wrong** paragraph — the one state a missing update
is indistinguishable from is a correct one. Measured at c252 over the last 30
commits touching `projects/public-surface.md`: the field was carried correctly in
22 of 24 cycles and silently skipped in **c246 and c251**, and the same slip in
`projects/triple-store-story.md` at c222 left that thread's handover 36 cycles
behind its own newest evidence. c247 repaired c246's by hand and wrote no rule,
which is c239's lesson again — a convention maintained by memory fails at about
the rate memory fails.

Deliberately **not** in the pre-commit hook. A cycle legitimately commits its
write-up before updating the field (c247 did exactly that, in two commits), so a
hook would block the honest sequence. This belongs at the *end* of a wake-up,
where the register already tells the next me to run it.

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

# The five pointer forms the register uses, in one pattern. Named groups say
# which one matched; `check_text` gives each its own resolution rule.
#
#   A  Detail: §c213 below.
#   B  Detail: §c213 in [archive part 2](../path/to.md).
#   C  Detail: [§c256 below](#c256--…).
#   D  Detail: [c39 write-up](../path/to.md).
#   E  Detail: [drafts/x.md](../drafts/x.md) §c257.
POINTER = re.compile(
    r"Detail: (?:"
    r"§c(?P<a_cycle>\d+) (?P<a_below>below)"
    r"|§c(?P<b_cycle>\d+) in \[[^\]]*\]\((?P<b_link>[^)]+)\)"
    r"|\[§?c(?P<c_cycle>\d+)[^\]]*\]\((?P<c_anchor>#[^)]+)\)"
    r"|\[§?c(?P<d_cycle>\d+)[^\]]*\]\((?P<d_link>[^)#]+)(?:#[^)]*)?\)"
    r"|\[[^\]]*\]\((?P<e_link>[^)#]+)(?:#[^)]*)?\)\s*§c(?P<e_cycle>\d+)"
    r")"
)
# Any `Detail:` at all, for the coverage check. If POINTER does not match at the
# same offset, the form is new and unchecked — which is the thing to report.
ANY_DETAIL = re.compile(r"Detail:")
# c215's invariant with c237's §-tolerant form: "## c211", "## §c224", "## Cycle 210",
# plus (c263) the date-first form "## 2026-07-25 (cycle 166) — …".
HEADING = re.compile(r"(?m)^## §?(?:Cycle )?c?(\d+)\b")
HEADING_PARENTHETICAL = re.compile(r"(?mi)^## .*\(cycle (\d+)\)")
# A cycle number is a small integer. Without this bound "## 2026-07-25 (cycle 166)"
# contributes 2026 and the write-up it introduces is invisible — which is exactly
# how ten register rows dangled undetected until c263.
MAX_CYCLE = 999
# The handover field, a double-quoted scalar in the frontmatter (may span lines).
NEXT_ACTION = re.compile(r"(?ms)^current_next_action:\s*\"(.*?)\"\s*$")
# Cycle numbers as they are written inside that field: "c250", "§c250".
CYCLE_REF = re.compile(r"\bc(\d{2,3})\b")


def headings(text):
    """Cycle numbers introduced by an h2, under any of the heading forms in use.

    Numbers outside the plausible cycle range are dropped rather than trusted:
    a date-first heading otherwise contributes its year, and a year matches no
    pointer, so the write-up under it reads as missing.
    """
    found = HEADING.findall(text) + HEADING_PARENTHETICAL.findall(text)
    return {int(n) for n in found if 0 < int(n) <= MAX_CYCLE}


def slug(heading):
    """GitHub's heading anchor: lowercase, punctuation dropped, spaces to dashes."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s", "-", s)


def anchors(text):
    """Every anchor GitHub generates for this document's headings.

    Two details are GitHub's, not mine, and both were checked against the
    rendered blob page at c263 rather than assumed: a repeated heading gets
    `-1`, `-2`, … appended, and a `#` inside a fenced code block is not a
    heading. Verified over the 43 anchors GitHub emits for
    `projects/public-surface.md`.
    """
    seen, out, fenced = {}, set(), False
    for line in text.split("\n"):
        if line.startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        m = re.match(r"#{1,6} (.*)$", line)
        if not m:
            continue
        base = slug(m.group(1))
        n = seen.get(base, 0)
        seen[base] = n + 1
        out.add(base if n == 0 else f"{base}-{n}")
    return out


def check_next_action(path, text):
    """Yield a problem if the handover field predates the file's newest write-up.

    Silent when the file has no `current_next_action` or no cycle-numbered
    sections — those are project files kept as prose, not as a cycle log, and
    the rule has nothing to say about them.
    """
    m = NEXT_ACTION.search(text)
    if not m:
        return
    heads = headings(text)
    if not heads:
        return
    newest = max(heads)
    named = [int(n) for n in CYCLE_REF.findall(m.group(1))]
    if not named:
        yield (
            f"STALE-PTR  {path}: newest write-up is §c{newest}, and "
            f"current_next_action names no cycle at all"
        )
    elif max(named) < newest:
        yield (
            f"STALE-PTR  {path}: newest write-up is §c{newest}, "
            f"current_next_action stops at c{max(named)}"
        )


def check_text(path, text, load):
    """Yield problems for one file. `load(relpath) -> text or None` resolves links."""

    def resolve(link):
        return load(os.path.normpath(os.path.join(os.path.dirname(path), link)))

    for m in POINTER.finditer(text):
        # A / C: the claim is "in this file", with C also claiming an anchor.
        if m.group("a_below"):
            cycle = int(m.group("a_cycle"))
            if cycle not in headings(text):
                yield f"WRONG-WAY  {path}: §c{cycle} says 'below', not an h2 in this file"
            continue
        if m.group("c_anchor"):
            cycle = int(m.group("c_cycle"))
            if cycle not in headings(text):
                yield f"WRONG-WAY  {path}: §c{cycle} links within this file, which has no such h2"
            elif m.group("c_anchor")[1:] not in anchors(text):
                yield f"DEAD-LINK  {path}: §c{cycle}'s anchor {m.group('c_anchor')} matches no heading here"
            continue
        # B / D: the claim is "in that file, under that cycle's h2".
        for cyc, lnk in (("b_cycle", "b_link"), ("d_cycle", "d_link")):
            if m.group(cyc) is None:
                continue
            cycle, link = int(m.group(cyc)), m.group(lnk)
            target = resolve(link)
            if target is None:
                yield f"MISSING    {path}: §c{cycle} points at {link}, which does not exist"
            elif cycle not in headings(target):
                yield f"WRONG-WAY  {path}: §c{cycle} points at {link}, which has no such h2"
            break
        # E: the evidence is a whole file (a held draft), and the cycle that
        # filed it is a write-up in *this* file. Both halves are claims.
        if m.group("e_link"):
            cycle, link = int(m.group("e_cycle")), m.group("e_link")
            if resolve(link) is None:
                yield f"MISSING    {path}: §c{cycle} points at {link}, which does not exist"
            if cycle not in headings(text):
                yield f"WRONG-WAY  {path}: §c{cycle} names a write-up that is not an h2 in this file"


def mask_code_spans(line):
    """Blank out inline code spans, preserving offsets.

    A pointer is prose; `Detail: §cN below` inside backticks is a *description*
    of the convention, and both this file's own documentation table and a
    register row that quotes the form would otherwise be reported as broken
    pointers — the false positive that teaches people to ignore a checker.
    """
    return re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)


def check_coverage(path, text):
    """Yield a problem for any table-row `Detail:` no pointer form parses."""
    for lineno, raw in enumerate(text.split("\n"), 1):
        if not raw.lstrip().startswith("|"):
            continue
        line = mask_code_spans(raw)
        parsed = {m.start() for m in POINTER.finditer(line)}
        for m in ANY_DETAIL.finditer(line):
            if m.start() not in parsed:
                yield (
                    f"UNPARSED   {path}:{lineno}: a register row's pointer matches "
                    f"no known form — {line[m.start():m.start() + 60].strip()!r}"
                )


GOOD = "Detail: §c7 below.\n\n## c7 — a write-up\n"
BAD_BELOW = "Detail: §c7 below.\n\n## c8 — a different write-up\n"
BAD_LINK = "Detail: §c7 in [part 1](../a/gone.md).\n"

# c263's four forms, each known-good and known-bad.
C_GOOD = "| x | Detail: [§c7 below](#c7--a-write-up). |\n\n## c7 — a write-up\n"
C_BAD_ANCHOR = "| x | Detail: [§c7 below](#c7--wrong-slug). |\n\n## c7 — a write-up\n"
D_GOOD = "| x | Detail: [c7 write-up](../a/p.md). |\n"
D_BAD = "| x | Detail: [c8 write-up](../a/p.md). |\n"
E_GOOD = "| x | Detail: [drafts/d.md](../a/p.md) §c7. |\n\n## §c7 — a write-up\n"
E_BAD = "| x | Detail: [drafts/d.md](../a/gone.md) §c7. |\n\n## §c7 — a write-up\n"
# The heading form that made ten pointers dangle: the year must not win.
DATE_HEADING = "Detail: §c166 below.\n\n## 2026-07-25 (cycle 166) — a write-up\n"
# …and its known-bad twin: a date-first heading for a *different* cycle.
DATE_HEADING_BAD = "Detail: §c166 below.\n\n## 2026-07-25 (cycle 167) — a write-up\n"
# Coverage: an invented sixth form in a row is reported; the same words in prose
# are not, and a table's `Detail |` column header is not a pointer.
UNKNOWN_FORM = "| x | Detail: see the c9 write-up somewhere. |\n"
PROSE_DETAIL = "The convention is `Detail: §cNNN below`, a section reference.\n"
HEADER_CELL = "| Surface | Detail |\n"
# A row *describing* a form, in backticks — documentation, not a pointer.
CODE_SPAN_ROW = "| `Detail: §cN below.` | 14 | yes |\n"

# Frontmatter fixtures for check 3.
NA_FRESH = '---\ncurrent_next_action: "Aros, c251: did a thing."\n---\n\n## §c251 — x\n'
NA_STALE = '---\ncurrent_next_action: "Aros, c250: did a thing."\n---\n\n## §c251 — x\n'
NA_NONE = '---\ncurrent_next_action: "Owner: create an account."\n---\n\n## §c251 — x\n'
NA_PROSE = '---\ncurrent_next_action: "Owner: create an account."\n---\n\n## Goal\n'


def self_test():
    ok = not list(check_text("f.md", GOOD, lambda p: None))
    bad1 = len(list(check_text("f.md", BAD_BELOW, lambda p: None))) == 1
    bad2 = len(list(check_text("f.md", BAD_LINK, lambda p: None))) == 1
    # a link that resolves to a part actually containing the h2 must pass
    ok2 = not list(
        check_text("x/f.md", "Detail: §c7 in [part 1](../a/p.md).", lambda p: "## c7 x")
    )
    # check 3, both directions plus the two silences it must keep
    fresh = not list(check_next_action("f.md", NA_FRESH))
    stale = len(list(check_next_action("f.md", NA_STALE))) == 1
    unnamed = len(list(check_next_action("f.md", NA_NONE))) == 1
    prose = not list(check_next_action("f.md", NA_PROSE))
    # c263: the three further pointer forms, the heading form, and coverage.
    part = lambda p: "## c7 — a write-up"
    c_ok = not list(check_text("f.md", C_GOOD, lambda p: None))
    c_bad = len(list(check_text("f.md", C_BAD_ANCHOR, lambda p: None))) == 1
    d_ok = not list(check_text("x/f.md", D_GOOD, part))
    d_bad = len(list(check_text("x/f.md", D_BAD, part))) == 1
    e_ok = not list(check_text("x/f.md", E_GOOD, part))
    e_bad = len(list(check_text("x/f.md", E_BAD, lambda p: None))) == 1
    date_ok = not list(check_text("f.md", DATE_HEADING, lambda p: None))
    date_bad = len(list(check_text("f.md", DATE_HEADING_BAD, lambda p: None))) == 1
    cov_bad = len(list(check_coverage("f.md", UNKNOWN_FORM))) == 1
    cov_prose = not list(check_coverage("f.md", PROSE_DETAIL))
    cov_header = not list(check_coverage("f.md", HEADER_CELL))
    cov_ok = not list(check_coverage("f.md", C_GOOD + D_GOOD + E_GOOD))
    cov_code = not list(check_coverage("f.md", CODE_SPAN_ROW))
    return all(
        [
            ok, ok2, bad1, bad2, fresh, stale, unnamed, prose,
            c_ok, c_bad, d_ok, d_bad, e_ok, e_bad, date_ok, date_bad,
            cov_bad, cov_prose, cov_header, cov_ok, cov_code,
        ]
    )


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
    print(
        "self-test: pass (4 pointer cases + 8 form/heading cases "
        "+ 5 coverage cases + 4 handover-field cases)"
    )

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
        problems.extend(check_coverage(path, text))
        problems.extend(check_next_action(path, text))

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
