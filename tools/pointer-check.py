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
5. **Pointers that omit the `Detail:` label** (added c265). c263 keyed both the
   grammar and its own coverage check on that label, so a row writing the same
   claim without it was invisible to *both* — the c263 defect one level up,
   found the same way, by grepping the corpus instead of trusting the checker's
   *0 problems*. Measured at c265: **12 live register rows** ended in a bare
   `§cNNN below` whose write-up had rotated into an archive part three
   rotations earlier, and every rotation since c239 had repointed only the
   labelled rows because only those were ever reported. A and B are now parsed
   with or without the label — the location word (`below`, `in [link]`) is the
   claim, the label is decoration — and C/D/E, which have no such
   self-discriminator, are *reported* prefixless rather than guessed at.

   The general form, and it is c235's again: **an instrument's grammar is a
   claim about its corpus**, and the corpus is written by hand.
6. **Archive-index completeness** (added c286): every part in an archive
   directory is linked from the *Archive, oldest first* list of the file that
   rotates into it. Measured at c286: `projects/public-surface.md` listed 2 of
   its 6 parts, while `log.md` — same rule, same shape — listed all 5. The
   rotation produces two artifacts and only one of them is load-bearing for
   anything else, so the list is the half that drifts.

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
import tempfile

# The five pointer forms the register uses, in one pattern. Named groups say
# which one matched; `check_text` gives each its own resolution rule.
#
#   A  Detail: §c213 below.
#   B  Detail: §c213 in [archive part 2](../path/to.md).
#   C  Detail: [§c256 below](#c256--…).
#   D  Detail: [c39 write-up](../path/to.md).
#   E  Detail: [drafts/x.md](../drafts/x.md) §c257.
#
# The `Detail: ` prefix is **optional on A and B** (c265). It is a label, not the
# claim: what makes a cell a pointer is the location word — `below`, or `in
# [link]` — and eleven register rows write the same claim without the label.
# A and B carry that discriminator inside themselves, so dropping the prefix
# requirement cannot widen them onto prose. C/D/E have no such discriminator
# (a bare `[c39 write-up](x.md)` is indistinguishable from an ordinary link),
# so for those the prefix stays mandatory and `check_coverage` reports a
# prefixless one instead of guessing.
POINTER = re.compile(
    r"(?:Detail: )(?:"
    r"\[§?c(?P<c_cycle>\d+[a-z]*)[^\]]*\]\((?P<c_anchor>#[^)]+)\)"
    r"|\[§?c(?P<d_cycle>\d+[a-z]*)[^\]]*\]\((?P<d_link>[^)#]+)(?:#[^)]*)?\)"
    r"|\[[^\]]*\]\((?P<e_link>[^)#]+)(?:#[^)]*)?\)\s*§c(?P<e_cycle>\d+[a-z]*)"
    r")"
    r"|(?:Detail: )?(?:"
    r"§c(?P<a_cycle>\d+\w*) (?P<a_below>below)"
    r"|§c(?P<b_cycle>\d+\w*) in \[[^\]]*\]\((?P<b_link>[^)]+)\)"
    r")"
)
# Any `Detail:` at all, for the coverage check. If POINTER does not match at the
# same offset, the form is new and unchecked — which is the thing to report.
ANY_DETAIL = re.compile(r"Detail:")
# The C/D/E shapes as they look **without** the `Detail: ` label. These are
# location claims the grammar deliberately refuses to parse prefixless, so the
# coverage check reports them rather than skipping them (c265). `write-up` and
# the `§`/anchor forms are required so an ordinary link in a cell is not a hit.
UNLABELLED_CDE = re.compile(
    r"\[§c\d+[^\]]*\]\(#[^)]+\)"
    r"|\[§?c\d+[^\]]*write-up[^\]]*\]\([^)]+\)"
    r"|\[[^\]]*\]\([^)]+\)\s*§c\d+"
)
# c215's invariant with c237's §-tolerant form: "## c211", "## §c224", "## Cycle 210",
# plus (c263) the date-first form "## 2026-07-25 (cycle 166) — …".
HEADING = re.compile(r"(?m)^## §?(?:Cycle )?c?(\d+[a-z]*)\b")
HEADING_PARENTHETICAL = re.compile(r"(?mi)^## .*\(cycle (\d+[a-z]*)\)")
# A cycle number is a small integer. Without this bound "## 2026-07-25 (cycle 166)"
# contributes 2026 and the write-up it introduces is invisible — which is exactly
# how ten register rows dangled undetected until c263.
MAX_CYCLE = 999
# How a register row names a cycle: as a pointer (`§c299`) or in the *Last
# audited* column (`2026-07-30 (c299)`). Check 7 counts either as an index entry.
ROW_CYCLE = re.compile(r"(?:§c|\(c)(\d+[a-z]*)\)?")
# The files whose sections are indexed by a register table. Check 7 applies only
# here: `log.md` is chronological with no index, and a file with an incidental
# table would otherwise report every one of its entries as an orphan.
ROW_INDEXED_FILES = ("projects/public-surface.md",)
# The handover field, a double-quoted scalar in the frontmatter (may span lines).
NEXT_ACTION = re.compile(r"(?ms)^current_next_action:\s*\"(.*?)\"\s*$")
# Cycle numbers as they are written inside that field: "c250", "§c250".
CYCLE_REF = re.compile(r"\bc(\d{2,3})\b")


def cyc_num(cid):
    """The numeric part of a cycle id. `292b` -> 292 (added c294).

    A cycle id is a number with an optional letter suffix: a wake-up that runs
    twice inside one tick labels the second `292b`, and until c294 every regex
    here required pure digits — so `## §c292b` registered as no heading at all
    and the register row pointing at it reported UNPARSED on every run. Ids are
    compared as strings and *ordered* by this function, since `99` sorts after
    `294` lexicographically.
    """
    return int(re.match(r"\d+", cid).group())


def cyc_key(cid):
    """Sort key: numeric part first, then the suffix (`292` before `292b`)."""
    return (cyc_num(cid), cid[len(str(cyc_num(cid))):])


def headings(text):
    """Cycle numbers introduced by an h2, under any of the heading forms in use.

    Numbers outside the plausible cycle range are dropped rather than trusted:
    a date-first heading otherwise contributes its year, and a year matches no
    pointer, so the write-up under it reads as missing.
    """
    found = HEADING.findall(text) + HEADING_PARENTHETICAL.findall(text)
    return {n for n in found if 0 < cyc_num(n) <= MAX_CYCLE}


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
    newest = max(heads, key=cyc_key)
    named = CYCLE_REF.findall(m.group(1))
    if not named:
        yield (
            f"STALE-PTR  {path}: newest write-up is §c{newest}, and "
            f"current_next_action names no cycle at all"
        )
    elif cyc_key(max(named, key=cyc_key)) < cyc_key(newest):
        yield (
            f"STALE-PTR  {path}: newest write-up is §c{newest}, "
            f"current_next_action stops at c{max(named, key=cyc_key)}"
        )


def check_text(path, text, load):
    """Yield problems for one file. `load(relpath) -> text or None` resolves links."""

    def resolve(link):
        return load(os.path.normpath(os.path.join(os.path.dirname(path), link)))

    for m in POINTER.finditer(text):
        # A / C: the claim is "in this file", with C also claiming an anchor.
        if m.group("a_below"):
            cycle = m.group("a_cycle")
            if cycle not in headings(text):
                yield f"WRONG-WAY  {path}: §c{cycle} says 'below', not an h2 in this file"
            continue
        if m.group("c_anchor"):
            cycle = m.group("c_cycle")
            if cycle not in headings(text):
                yield f"WRONG-WAY  {path}: §c{cycle} links within this file, which has no such h2"
            elif m.group("c_anchor")[1:] not in anchors(text):
                yield f"DEAD-LINK  {path}: §c{cycle}'s anchor {m.group('c_anchor')} matches no heading here"
            continue
        # B / D: the claim is "in that file, under that cycle's h2".
        for cyc, lnk in (("b_cycle", "b_link"), ("d_cycle", "d_link")):
            if m.group(cyc) is None:
                continue
            cycle, link = m.group(cyc), m.group(lnk)
            target = resolve(link)
            if target is None:
                yield f"MISSING    {path}: §c{cycle} points at {link}, which does not exist"
            elif cycle not in headings(target):
                yield f"WRONG-WAY  {path}: §c{cycle} points at {link}, which has no such h2"
            break
        # E: the evidence is a whole file (a held draft), and the cycle that
        # filed it is a write-up in *this* file. Both halves are claims.
        if m.group("e_link"):
            cycle, link = m.group("e_cycle"), m.group("e_link")
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
    """Yield a problem for any table-row pointer no pointer form parses.

    Two ways a row can make a location claim the resolver never sees: a
    `Detail:` in a form the grammar does not know (c263), and a C/D/E-shaped
    claim written without the `Detail:` label, which the grammar refuses to
    parse because prefixless those shapes are indistinguishable from an
    ordinary link (c265). Both are reported; neither is guessed at.
    """
    for lineno, raw in enumerate(text.split("\n"), 1):
        if not raw.lstrip().startswith("|"):
            continue
        line = mask_code_spans(raw)
        spans = [(m.start(), m.end()) for m in POINTER.finditer(line)]
        parsed = {s for s, _ in spans}
        for m in ANY_DETAIL.finditer(line):
            if m.start() not in parsed:
                yield (
                    f"UNPARSED   {path}:{lineno}: a register row's pointer matches "
                    f"no known form — {line[m.start():m.start() + 60].strip()!r}"
                )
        for m in UNLABELLED_CDE.finditer(line):
            if any(s <= m.start() < e for s, e in spans):
                continue
            yield (
                f"UNLABELLED {path}:{lineno}: a register row points at a write-up "
                f"without the `Detail:` label, so it is not resolved — "
                f"{m.group(0)[:60]!r}"
            )


def check_orphan_writeups(path, text):
    """Yield a problem for a write-up section that no register row names.

    Added c300, on the third occurrence of the same slip (c241, c250, c299).
    Every other check in this file runs **rows -> sections**: given a pointer,
    does it resolve? None of them runs the other direction, so a cycle that
    appends its write-up and forgets its register row is silent — the write-up
    renders, every existing pointer still resolves, and the file's own index
    simply does not mention it. c299 went further and recorded *"register row,
    §c299"* in its log entry, so the record asserts a row that was never
    written.

    The failure has a deadline: once a rotation moves the section into an
    archive part, the only route to it was the row, and there is none. That is
    the same unreachability c286 found for whole archive parts, one level down.

    A row names a cycle as `§cN` (a pointer) or as `(cN)` (the *Last audited*
    column). Either counts as indexing it; whether the pointer itself is
    well-formed is checks 1 and 5's business, not this one's. Code spans are
    masked, so a row *documenting* the convention does not index anything.
    """
    rows = set()
    for raw in text.split("\n"):
        if not raw.lstrip().startswith("|"):
            continue
        rows.update(ROW_CYCLE.findall(mask_code_spans(raw)))
    for cid in sorted(headings(text), key=cyc_key):
        if cid not in rows:
            yield (
                f"ORPHAN     {path}: §c{cid} has a write-up and no register "
                f"row naming it — after the next rotation nothing points at it"
            )


def check_archive_index(root, live_relpath, archive_dirname, listing):
    """Yield a problem for any archive part not linked from the file it left.

    Added c286. The rotation rule produces two artifacts: a part in an archive
    directory, and a line in the live file's *Archive, oldest first* list. Only
    the first is load-bearing for anything else, so the second drifted: measured
    at c286, `projects/public-surface.md` listed 2 of its 6 parts — the four
    rotations after c216 each wrote a part and none appended a line — while
    `log.md`, running the same rule, listed all 5 of its own. Nothing signalled
    the gap, because a part stays reachable from whichever register rows point
    into it; the only reader who loses anything is one reading the list.

    `listing` is the live file's text, and the search is scoped to the bullet
    block under its `Archive, oldest first:` line — **not** to the whole file.
    The first version of this function searched the whole text and reported 1 of
    the 5 parts it was written to find: four of them are named elsewhere in the
    same file, inside register-row pointers of the
    `Detail: §c213 in [archive part 3](…)` form. A checker whose corpus is wider
    than its claim passes for the wrong reason, which is c263's finding turned on
    the checker written to answer it, one wake-up after c284 made the same
    mistake's cousin — so this one was run against the pre-fix copy of the file
    before it was believed.

    The claim being checked is one-way on purpose: every part on disk must appear
    in the list. A list entry for a part that does not exist is already caught by
    the B/D pointer forms if any row points at it, and a bare dead link in the
    list is `render-check`'s business, not this function's.
    """
    d = os.path.join(root, archive_dirname)
    try:
        parts = sorted(p for p in os.listdir(d) if p.endswith(".md"))
    except OSError:
        return
    block = archive_list_block(listing)
    for part in parts:
        if f"{archive_dirname}/{part}" not in block:
            yield (
                f"UNLISTED   {live_relpath}: {archive_dirname}/{part} exists but is "
                f"not in the file's archive list, so a reader of the list cannot find it"
            )


ARCHIVE_MARKER = re.compile(r"(?m)^Archive, oldest first:\s*$")


def archive_list_block(text):
    """The bullet list under `Archive, oldest first:`, or "" if there is none.

    A bullet may wrap onto indented continuation lines (both live files write
    them that way), so the block ends at the first line that is neither a
    bullet, a continuation, nor blank.
    """
    m = ARCHIVE_MARKER.search(text)
    if not m:
        return ""
    out = []
    for line in text[m.end():].split("\n")[1:]:
        if line.startswith("- ") or (line.startswith("  ") and line.strip()):
            out.append(line)
        elif not line.strip():
            if out:
                break
        else:
            break
    return "\n".join(out)


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
# c265: the same A/B claims with the `Detail:` label dropped. Resolved, not
# skipped — and still wrong when they are wrong.
BARE_A_GOOD = "| x | a verdict. §c7 below |\n\n## c7 — a write-up\n"
BARE_A_BAD = "| x | a verdict. §c7 below |\n\n## c8 — a different write-up\n"
BARE_B_BAD = "| x | a verdict. §c7 in [part 1](../a/gone.md) |\n"
# A cycle named in a cell without a location word is prose, not a pointer.
BARE_MENTION = "| x | the field named c186 with §c222 appended — 36 cycles. |\n"
# C/D/E without the label: reported by coverage, never guessed at.
UNLABELLED_C = "| x | see [§c7 below](#c7--a-write-up). |\n\n## c7 — a write-up\n"
UNLABELLED_D = "| x | see the [c7 write-up](../a/p.md). |\n"
# …while an ordinary link in a cell is not a pointer and must stay silent.
PLAIN_LINK_ROW = "| x | see [the README](../README.md) for context. |\n"

# c294: a cycle id with a letter suffix — a wake-up that ran twice inside one
# tick. Before c294 the heading regex required pure digits, so `## §c292b`
# registered as no heading and its own register row reported UNPARSED. The bad
# twin keeps the suffix load-bearing: `292b` must not resolve against `292`.
SUFFIX_GOOD = "| x | Detail: §c292b below |\n\n## §c292b — a write-up\n"
SUFFIX_BAD = "| x | Detail: §c292b below |\n\n## §c292 — a different write-up\n"

# c300: check 7, sections -> rows. A row may name the cycle as a pointer or in
# its date column; a row that only *quotes* the convention indexes nothing.
ORPH_OK = "| x | Detail: §c7 below |\n\n## §c7 — a write-up\n"
ORPH_BAD = ORPH_OK + "\n## §c8 — a write-up nothing indexes\n"
ORPH_DATE_COL = "| a surface | 2026-07-30 (c8) | a verdict |\n\n## §c8 — a write-up\n"
ORPH_CODE_ONLY = "| `Detail: §c7 below` | 14 | yes |\n\n## §c7 — a write-up\n"
# No table at all in a file declared row-indexed: both sections really are
# unreachable, so silence would be wrong. Reported, not skipped.
ORPH_NO_TABLE = "## §c7 — a write-up\n\n## §c8 — another\n"

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
    # c265: prefixless A/B are resolved like their labelled twins …
    bare_ok = not list(check_text("f.md", BARE_A_GOOD, lambda p: None))
    bare_bad = len(list(check_text("f.md", BARE_A_BAD, lambda p: None))) == 1
    bare_b = len(list(check_text("x/f.md", BARE_B_BAD, lambda p: None))) == 1
    # … a cycle mentioned without a location word is not a pointer at all …
    bare_prose = not list(check_text("f.md", BARE_MENTION, lambda p: None)) and not list(
        check_coverage("f.md", BARE_MENTION)
    )
    # … and prefixless C/D are reported rather than resolved or skipped.
    unl_c = len(list(check_coverage("f.md", UNLABELLED_C))) == 1
    unl_d = len(list(check_coverage("f.md", UNLABELLED_D))) == 1
    unl_plain = not list(check_coverage("f.md", PLAIN_LINK_ROW))
    suffix_ok = not list(check_text("f.md", SUFFIX_GOOD, lambda p: None))
    suffix_bad = len(list(check_text("f.md", SUFFIX_BAD, lambda p: None))) == 1
    suffix_cov = not list(check_coverage("f.md", SUFFIX_GOOD))
    suffix_ord = cyc_key("292b") > cyc_key("292") and cyc_key("99") < cyc_key("294")
    # c286: check 6, both directions, against a real directory rather than a
    # mocked listing — the defect it exists for was a file on disk that no line
    # of prose mentioned, so the fixture has to have files on disk.
    with tempfile.TemporaryDirectory() as td:
        os.mkdir(os.path.join(td, "arch"))
        for name in ("p1.md", "p2.md"):
            open(os.path.join(td, "arch", name), "w").close()
        head = "Archive, oldest first:\n\n"
        both = head + "- [x](arch/p1.md)\n- [y](arch/p2.md)\n  wrapped continuation.\n\nprose.\n"
        one = head + "- [x](arch/p1.md)\n\nprose.\n"
        # The false pass the first version of this function returned: the missing
        # part named in a register row *outside* the list must still be reported.
        elsewhere = one + "\n| a surface | Detail: §c9 in [part 2](arch/p2.md). |\n"
        idx_ok = not list(check_archive_index(td, "live.md", "arch", both))
        idx_bad = len(list(check_archive_index(td, "live.md", "arch", one))) == 1
        idx_scope = len(list(check_archive_index(td, "live.md", "arch", elsewhere))) == 1
        idx_none = not list(check_archive_index(td, "live.md", "nosuchdir", ""))
        # No marker at all: nothing to check against, and silence is wrong — the
        # parts exist and no list names them.
        idx_nomarker = len(list(check_archive_index(td, "live.md", "arch", "prose only.\n"))) == 2
    # c300: check 7, the sections -> rows direction, both ways round.
    orph_ok = not list(check_orphan_writeups("f.md", ORPH_OK))
    orph_bad = len(list(check_orphan_writeups("f.md", ORPH_BAD))) == 1
    orph_date = not list(check_orphan_writeups("f.md", ORPH_DATE_COL))
    orph_code = len(list(check_orphan_writeups("f.md", ORPH_CODE_ONLY))) == 1
    orph_none = len(list(check_orphan_writeups("f.md", ORPH_NO_TABLE))) == 2
    return all(
        [
            ok, ok2, bad1, bad2, fresh, stale, unnamed, prose,
            c_ok, c_bad, d_ok, d_bad, e_ok, e_bad, date_ok, date_bad,
            cov_bad, cov_prose, cov_header, cov_ok, cov_code,
            bare_ok, bare_bad, bare_b, bare_prose, unl_c, unl_d, unl_plain,
            idx_ok, idx_bad, idx_scope, idx_none, idx_nomarker,
            suffix_ok, suffix_bad, suffix_cov, suffix_ord,
            orph_ok, orph_bad, orph_date, orph_code, orph_none,
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
        "self-test: pass (4 pointer cases + 12 form/heading cases "
        "+ 5 coverage cases + 7 label cases + 4 handover-field cases "
        "+ 5 archive-index cases + 5 orphan-write-up cases)"
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
        # Check 7 (c300): the sections -> rows direction, on the files that keep
        # a register table.
        if path in ROW_INDEXED_FILES:
            problems.extend(check_orphan_writeups(path, text))

    # Check 6 (c286): each rotating file's archive directory against its own
    # *Archive, oldest first* list.
    indexes = [
        ("projects/public-surface.md", "projects-archive"),
        ("log.md", "log-archive"),
    ]
    for live, archive in indexes:
        problems.extend(check_archive_index(root, live, archive, load(live) or ""))

    if not problems:
        print(
            f"{len(files)} tracked Markdown files, {pointers} pointers, "
            f"{len(indexes)} archive indexes, 0 problems."
        )
        return 0

    print()
    for line in problems:
        print(line)
    print(f"\n{len(files)} tracked Markdown files, {pointers} pointers, {len(problems)} problem(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
