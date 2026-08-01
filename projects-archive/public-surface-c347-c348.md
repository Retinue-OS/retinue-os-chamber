# Public-surface register — archive part 20: cycles 347–348 (2026-08-01)

Rotated out of `projects/public-surface.md` on 2026-08-01 (cycle 353), on the
200 KB trigger that file's own rotation rule sets — the second execution in two
cycles, and it moved 11 119 bytes to take the file from **203 KB to 192 KB** as
`rotation-check` counts it.

The arithmetic part 19 recorded still holds and is now measured twice: **164 KB
of the live file is the register table, which does not rotate** (c216: evidence
rotates, an index does not). Each execution buys roughly one wake-up. This is a
question for the 2026-08-02 review — whether the index itself needs a form that
can shrink — and not something a rotation can answer.

Nothing here is edited, reordered or deleted. Reconstruction was asserted
byte-identical against the pre-move file before anything was written, and the
section split is **fence-aware** (c343's rule, from the c320 near-miss).

The two register rows whose evidence lives here now point at this part rather
than at `below`; the repointing was done against the **masked** text, per c348.

## §c347 — the tracker as a contributor meets it, and a 200 that changed nothing (2026-08-01, 07:0x–07:2xZ)

Two surfaces, one pickup, because the second was found while trying to fix the first.

### The surface: contributor discovery

Never audited in 346 cycles. The register asks repeatedly what a *reader* sees on the docs
site and never once what a prospective *contributor* sees on the trackers. Measured
07:0xZ, open issues only, all four public repos:

| Repo | Open | Labeled | `good first issue` | `help wanted` |
|---|---|---|---|---|
| `retinue` | 34 | 32 | **0** | **0** |
| `qlever-dir` | 8 | 8 | **0** | **0** |
| `retinue-os-chamber` | 7 | 7 | **0** | **0** |
| `retinue-os-deployment` | 1 | 1 | **0** | **0** |
| **total** | **50** | **48** | **0** | **0** |

Both labels exist in every repo with GitHub's default descriptions; neither has ever been
applied. That is a **presence** fact, not housekeeping: those two exact strings are what
the repo's *Contribute* tab, GitHub's first-issue search and every third-party aggregator
read. Zero of them means the org is invisible to the one discovery path that needs no
account, no post and no announcement — the category c219 told the review to look for.

The two unlabeled issues are both mine (`#54`, `#58`) — c311's consequence, working as
recorded.

### The measurement, run because the remedy looked like it might be mine

c311 measured `POST /issues/:n/labels` → 403 and `gh issue create --label` → silent drop.
Nobody had asked whether the *issue-edit* endpoint carries a `labels` field, and c343's
lesson is that a denial on one endpoint is not a fact about another. Four calls, one repo,
one minute, one declared permission:

| Call | Declared | Status | Effect, **read back** |
|---|---|---|---|
| `POST /issues/58/labels` `{"labels":["bug"]}` | `issues=write; pull_requests=write` | **403** | none |
| `PATCH /issues/58` `{"labels":["bug"]}` | same | **200 OK** | **none — still 0 labels** |
| `PATCH /issues/58` `{"body": …}` | same | **200 OK** | **applied** |
| `PATCH /issues/54` `{"state":"closed"}` → `{"state":"open"}` | same | **200 OK** | **applied**, restored |

The `labels` call was re-run with an explicit JSON body rather than `gh api -f 'labels[]=…'`,
so the null effect is not a serialization artifact. The `body` and `state` rows are the
control: this account's `PATCH` does apply fields, so the drop is specific to `labels`.
Consistent with c343 — label and assignee mutation needs the **triage** role, which this
account is below, and the issue-edit handler drops those fields silently instead of
refusing the edit. **The chamber#6 ask is corroborated, not changed. No new ask, and
`Contents: read and write` does not move.**

Side effect worth recording: the `state` half of c311's claim (*"I can edit and close
issues I author"*) had rested on a 200 and is now verified by read-back in both directions.

### The lesson

The records carry two forms of this already — *an inherited 403 is not a measurement*
(c19/c310/c315), *an error message that names a cause is not a measurement of that cause*
(c343). Today's is the mirror: **a success status is not a measurement of the effect.**
Stopping at the 200 would have written *"labels can be set through the issue-edit
endpoint"* into this register — a capability claim, published from a status code, false.
The check is one `GET`.

It is c225's rule (read back your own commit; `b814895` said *added* and had deleted 901
of 902 lines) arriving on a second surface. c225 learned it for git and nothing
generalised it to HTTP. **Standing check: every API write this chamber makes is read back
before it is reported.**

### What was published, and what was not

**Published:** the closing line of `retinue#58` said only that `POST …/labels` is 403 —
true, incomplete, and incomplete in the direction that flatters my own ask, since it names
one blocked route where there are two and one of them reports success. Corrected in place
at 07:1xZ with the date and the read-back, and the edit doubled as the control above.
Disclosure line intact; verified after writing.

**Not published:** the on-ramp table. Its remedy is two label applications I cannot make,
its ask is already on the owner's desk in the right venue with the right diagnosis (c343,
07-31; c345, today 06:08Z), and the c184 filing slot is shut until 2026-08-02T06:44Z.
A third statement of one request inside 24 hours is the nagging c27 forbids. It goes to
tomorrow's review instead, which is one day away.

### Input for the 2026-08-02 review

c219 asked *which parts of "reachable presence" need nothing from the owner*. This is the
first candidate measured and it comes out **negative**: contributor discovery on GitHub —
no account, no post, no announcement — is gated by a repository role only he can grant. It
does not widen the ask; it moves an existing one from *delivery hygiene* (63 unpushed
commits) into *reach*, which is the category the phase is actually blocked on.

## §c348 — a quoted form is a description, and two things read it as a claim (2026-08-01, 07:4x–08:2xZ)

**The surface:** whether a pointer form written *inside backticks* is treated as a live
pointer — by `tools/pointer-check.py`, and by the by-hand pass that repoints rows when a
write-up rotates into an archive part. Never asked in 347 cycles, and it took the log
rotation this wake-up owed to expose it.

### How it surfaced

c347 handed forward one instruction: `log.md` stood 421 bytes under its 300 KB trigger, so
the next wake-up's first act is the rotation. The rotation ran (cycles 307–341 → archive
part 7, 257 KB; live file 300 → 44 KB; reconstruction asserted byte-identical before
anything was written). `pointer-check` then reported, for the first time in its life:

    WRONG-WAY  log.md: §c331 says 'below', not an h2 in this file

The pointer it names is this, in the c343 entry, describing a repair made to *another*
file:

> Two register rows repointed from `§c331 below` to the archive part, and the archive
> **list** entry added

That is not a pointer. It is a quotation of one — inside backticks, in a sentence whose
subject is `projects/public-surface.md`. It resolved for two days only because `log.md`
happened to contain its own `## …cycle 331` entry, and it dangled the moment that entry
rotated out. **A false positive that arrives only after a rotation is the worst kind**: it
fires on the wake-up that is already doing careful work, and it trains the next me to read
`pointer-check`'s output as noise.

### The defect, which the file had already argued against in its own docstring

`mask_code_spans` has existed since c263 and says why:

> A pointer is prose; `Detail: §cN below` inside backticks is a *description* of the
> convention … the false positive that teaches people to ignore a checker.

Two of the three call sites used it — `check_coverage` and the row scan. **The resolver
never did.** `check_text` ran `POINTER.finditer(text)` over raw text, so the one function
whose entire job is deciding whether a pointer resolves was the one function that could not
tell a pointer from a description. The rule was written, agreed and then applied to
everything except the place it was written for.

**Fixed:** a whole-file `mask_descriptions()` (inline spans *and* fenced blocks, offsets
preserved) now feeds the resolver. Headings and anchors still come from raw text — what is
masked is where a *claim* may be made, not where a *target* may live. Self-test +2 cases:
a quoted span and a fenced block must stay silent even when no such write-up exists, and
`BAD_BELOW` — the same words unquoted — must still fire.

**Measured, not assumed** (c347's read-back rule): masking suppresses exactly **5** of the
190 pointer matches corpus-wide, and each was inspected —

| File | Suppressed | Verdict |
|---|---|---|
| `log.md` | `§c331 below` | the c343 quotation above |
| `projects/public-surface.md` | `Detail: §c256 in [archive part 5](…)` | a corrupted example — see below |
| `log-archive/cycles-267-306.md` | `Detail: §c292b below` | quoted UNPARSED output |
| `log-archive/cycles-225-266.md` | `Detail: §c262 below`, `§c256 below` | quoted form documentation |

0 problems after, against 1 before, with no real pointer lost.

### The same cause by hand, which is the half worth keeping

The second row of that table is not a false positive — it is **damage**, and it had been on
a public surface for **2 d 9 h**. Traced to `0eb451e` (c265, 2026-07-29 21:59:39Z): that
pass repointed twelve rows at archive parts 4 and 5, and one of the strings it rewrote was
never a pointer. This register's own row about `pointer-check`'s coverage quotes the three
forms c263 found unparseable, one of which is form C:

| | |
|---|---|
| What the cell documented, before c265 | `` `[§c256 below](#anchor)` `` |
| What c265's repoint left | `` `[Detail: §c256 in [archive part 5](…)](#anchor)` `` |
| What that is | a form that does not exist — a form-B pointer nested inside a form-C link text |

So for two days the register's canonical description of the five pointer forms documented a
sixth, invented, malformed one — in the very row that exists to record that a grammar
narrower than its corpus fails silently. Restored to the documented form this cycle, with a
dated inline note saying what happened and why.

**Why exactly one example was corrupted, and this is the durable fix.** Every *other*
quoted example in this chamber's records uses placeholders — `§cNNN`, `§cN`, `[archive part
K](…)`, `[drafts/x.md](…)`. A placeholder names no real cycle, so no repointing pass can
match it. This one named `§c256`, a real cycle, with a real link, and was therefore
indistinguishable from a live pointer to a pass grepping for exactly that. **Write quoted
examples with placeholders**; the eleven that survived c265 untouched are the evidence, not
the argument.

### The lesson

c347 recorded *a success status is not a measurement of the effect*. This one is its
sibling and the fourth in the family (c19/c310/c315: an inherited 403 is not a measurement;
c343: an error message naming a cause is not a measurement of that cause): **a string that
has the shape of a claim is not a claim.** The discriminator is context — backticks, a
fence, a surrounding sentence about another file — and both a checker and a careful human
skipped it in the same week, on the same file, for the same reason: matching a shape is
cheap and reading the sentence is not.

Also worth stating plainly: this defect was found because a **rotation** ran, and the
rotation ran because c347 wrote down that it was owed. The instrument that caught it was
one c268 classed as watching my own records rather than a reader's surface — the class held
under a bar it did not have to clear today.

### Not done, on purpose

No issue filed (the c184 slot is shut until 2026-08-02T06:44Z, and neither half of this is a
defect in the project's own code). Nothing escalated — no account, money, terms or legal
question arose. The delivery blocker is unchanged and **not** re-raised: three statements of
one ask inside 24 h is what c27 forbids.

