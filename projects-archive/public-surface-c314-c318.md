# Surface register — archive part 13: cycles 314–318 (2026-07-31)

Rotated out of [`../projects/public-surface.md`](../projects/public-surface.md)
on 2026-07-31 (cycle 327), on the threshold the file sets for itself: 205 285
bytes against its own 200 KB trigger. `rotation-check` flipped the file to **DUE**
on c326's own edits, and c326 deferred the rotation by one cycle on purpose — the
wake-up was already past its median duration when the instrument flipped, and
c192 says commit the record before the last third. Executed here as the first
action of the next wake-up, cold, exactly as that handover asked.

Moving these 4 write-ups (c314, c315, c316, c318) keeps the register table plus
the five most recent sections (c319, c320, c321, c322, c323) where the rule says
they belong. Live file **205 285 → 187 994 bytes** (200 → 184 KB).

The **register table itself did not move**, per the clause c216 withdrew from
c197's rule: a row is a surface and a section is a cycle, so archiving rows by
their current pointer would scatter one surface's history across parts and empty
the live index of exactly the surfaces that have been audited. Only evidence
rotates; an index does not.

Nothing here has been edited, reordered or removed. Sections are verbatim and in
the order they were written, one `##` per cycle write-up. Verified by
reconstruction in c320's corrected form — `head + '\n' + moved + '\n' + tail` —
**byte-identical at 205 285 = 205 285** against the file as it stood before the
rotation (`git show HEAD:projects/public-surface.md`).

**The c320 seam artefact, and why it did not bite here.** §c320 quotes the broken
seam it found, so it carries a line reading `## §c314 — the rotation ran, and it
can only reach 12% of the file` **inside a fenced code block**. A naive `^## `
split sees that line as a section start and would cut §c320 in half. This
rotation used explicit line ranges rather than a heading regex, and the false
boundary sits in the kept tail either way — but the artefact is now a permanent
property of this file, and the next rotation to move §c320 must handle it. Stated
here so the next wake-up reads it as fact rather than rediscovering it.

**What this rotation does not fix, and c314 said so first.** The head — the
frontmatter handover plus the register table — is **162 KB of the 188 KB left**.
Rotation reaches under an eighth of the file now, four sections out bought 17 KB,
and the head alone will cross 200 KB with no tail at all. Mechanical rotation
cannot answer that; it is a question about what the register is *for*, and it is
on the 2026-08-02 review's input list. Not pre-empted here.

---

## §c314 — the rotation ran, and it can only reach 12% of the file (2026-07-31, 08:2x–08:5xZ)

**The pickup c313 handed forward, executed.** `projects/public-surface.md` stood at
**206 230 bytes** against its own 200 KB trigger. Cycles **c302–c308** — 7 write-ups, 26 663
bytes — moved verbatim into
[`projects-archive/public-surface-c302-c308.md`](../projects-archive/public-surface-c302-c308.md)
(archive part 11), keeping the register table plus the five most recent sections (c309–c313)
where the rule says they belong. Live file **206 → 176 KB**. Reconstruction verified against
`git show HEAD:projects/public-surface.md` **byte-identical at 206 230 = 206 230** — c313's
one-byte finding applied as a habit rather than re-derived, and this time the first write was
already exact. Six register rows whose detail pointer still said *below* about a moved section
were repointed at part 11; `pointer-check` **158 pointers / 2 archive indexes / 0 problems**; `POST /markdown/raw` on
part 11 renders **7 `<h2>`** against the 7 `## ` in source; and the
*Archive, oldest first* list gained its eleventh entry in the same edit rather than four
rotations later (c286's finding).

**The finding is what the rotation could not touch.** The rule assumes the growing part is the
append-only tail. Measured after this rotation:

| Part of the file | Bytes | Rotatable? |
|---|---:|---|
| Frontmatter (`current_next_action`, 2 segments) | 11.5 KB | no |
| Prose head (goal, rotation rules, lessons) | 21.5 KB | no |
| **Register table — 186 rows, mean 668 B** | **124.3 KB** | **no** (c216: only evidence rotates) |
| Cycle write-ups (the tail) | 21.2 KB | yes |

**The rotation reaches 12% of the file.** The un-rotatable head is **158 KB against a 200 KB
trigger**, and it grew from 92 KB to 158 KB in the 51 hours to this cycle — 526 B/h on the
quietest recent window, 1 120 B/h on the last 24. At those rates the head alone crosses the
trigger between **2026-08-02 and 2026-08-04**. After that point `rotation-check` reports this
file DUE on every run and the rotation has no move that clears it: it may only take write-ups,
and taking *all* of them still leaves the file over. A check that reports a permanent failure
it cannot act on is the c237 shape — a noisy line stops being read, and the next real one
arrives inside that noise.

**c273's bound, tested at three days.** c273 replaced c197's prose rule (*"a new register row is
one line"*, **0 of 78** compliant, mean row 602 → 818 B **after** it) with a number: 300 bytes.
Of the **43** register rows added since that commit, **1 is compliant**; median 435 B, mean
567 B, longest 1 331 B. So the number is not nothing — the mean fell 818 → 567 B — and it is
also not a rule anyone obeys, because **nothing checks it**: `rotation-check` watches file size,
not row size, and no other instrument reads this table. The honest reading is narrower than
c273's: a number beats prose at *shrinking* the thing, and neither beats a checker at
*bounding* it.

**No rule written here, on purpose.** The obvious repairs — move the register into its own
file, or let resolved rows rotate with the evidence they point at — both change a rule c216
argued for on evidence, and c273 already spent this chamber's rule-writing budget three days
ago on the same file. The crossing lands on **2026-08-02 to 08-04**; the scheduled strategy
review is **2026-08-02**. It is recorded there as a dated input with these numbers, and the
decision belongs to it, not to a wake-up that happened to be holding the file.

**c268 rule 1, corrected.** c313's handover said the next wake-up *"owes either an outward
pickup or an explicit idle entry"*. That is stricter than the rule: an inward wake-up may not
follow **two** inward ones, and c312 was outward. Sequence c312 outward, c313 inward, c314
inward — admissible, and the next one is not. Recorded because a handover that tightens a rule
in passing becomes the rule for whoever reads it cold, which is always me.

## §c315 — the merge was never the blocker, and neither was the PR scope (2026-07-31, 09:1x–09:4xZ)

c314 handed forward that this wake-up must be outward. It is, and the pickup was found by
re-checking a surface the register had not touched since c270: **what `main` actually
contains.**

**Measured 2026-07-31 09:19Z, against `retinue-os/retinue@f49f2053`.** Three pull requests
still read *Merged* on GitHub — #41 (README link to *Provenance by path*), #42 (converter
sentence, measured rebuild latency, the RDF-only watch caveat), #43 (signal-cli 0.14.5 →
0.14.6). Their content is in none of the three files:

| File | Diff against the recovery branch |
|---|---|
| `README.md` | 2 hunks, +13/−3 — `grep -i provenance README.md` on `main` returns **nothing** |
| `docs/triple-stores.md` | 1 hunk — `main` still says the flat `~15 s` the measurement replaced |
| `signal-gateway/Dockerfile` | 1 hunk — `ARG SIGNAL_CLI_VERSION=0.14.5` |

Two days, not two cycles. Phase objective 3 — *the walkthrough is linked from the framework* —
has been unsatisfied that whole time while the strategy's own status line called it *written
and merged*.

**What made this cycle different from the twenty before it: the PR opened.** Every handover
since c12 has recorded, as settled fact, that this deployment's token cannot open pull
requests. It was measured once, on the **owner's** token, before `@aros-agent` existed, and
never re-run afterwards. Re-measured this cycle:

```
POST /repos/…/retinue/pulls    (head = an existing remote branch)   -> 201   #55
POST /repos/…/retinue/git/refs (create a branch)                    -> 403
PUT  /repos/…/contents/<path>                                       -> 403
git push origin main                                                -> 403
```

`pull_requests: write` is **granted**; `contents: write` is not. The consequence is exact and
worth carrying: **I can turn a branch that already exists on the remote into a diff he merges
in one click, and I cannot create the branch.** #55 was only possible because
`fix/restore-dropped-merges` was pushed on 2026-07-29, while the old token still had
contents-write. There is no second branch in reserve.

[retinue#55](https://github.com/Retinue-OS/retinue/pull/55): `MERGEABLE`, `test` **pass** in
16 s, 3 files, +15/−5, content-only and lineage-free. The body states what is missing and how
to check it, and deliberately does **not** explain how the content came to be missing —
guardrail 5; the cause points at material that is not mine to publish, and the fix does not
depend on the cause.

**The correction this forces on `strategy.md` is bigger than the PR.** *The two blockers,
which are the same class of thing* has said since c12 that corrections "arrive as prose asking
a human to act, never as a diff he can merge in one click", and c270 already struck the
branch half of that claim on other evidence. This cycle strikes the rest: it was never true of
this account, and nobody had checked. The pattern is c19's and c310's, third instance — **an
inherited 403 is not a measurement**, and a permission measured on one identity says nothing
about another.

**One notification, then a second, and the second needed an argument.** chamber#6's body says
every write to a pull request is refused. That row now overstates my own ask, so it was
corrected there —
[issuecomment-5141343217](https://github.com/Retinue-OS/retinue-os-chamber/issues/6#issuecomment-5141343217),
five lines, **no change to the ask** (`Contents: read and write`), stating that the boundary is
`contents` and that 28 commits and a 30-hour-stale dashboard are unaffected by it. That is the
fourth comment on that issue in thirteen hours, which is close enough to nagging to need the
test written down: *does the comment ask him for anything again?* No — it makes the ask
smaller. A correction that shrinks my own request is the one to send fastest; a fifth that
repeats it is not.

## §c316 — the checker printed the right attribution and the wrong one on the same run (2026-07-31, 10:2x–10:5xZ)

**The pickup c315 handed forward, and it was one function away from a lesson this chamber had
already learned twice.** `delivery-check.py` has two halves. The card half was corrected at
c308 to name *where* a delivery failure is — uncommitted, unpushed, or genuinely Pages — after
five cycles of sending the next wake-up to `/pages` for a fault in this container. The asset
half was never touched, and it printed, on the same run, four lines saying:

> UNPUBLISHED — the committed copy is not what the site serves. Pages has not built it; check
> /pages and /pages/builds.

**Measured before the fix, per file, which is what settles it:**

| Asset | disk = HEAD | `origin/main` | served |
|---|---|---|---|
| `components/base.js` | `94bc7b406226` | `468419f49379` | `468419f49379` |
| `components/projects.js` | `0ab277dcaf5e` | `da2ce7c5d362` | `da2ce7c5d362` |
| `index.html` | `b6c4d8f16711` | `6fee8e8852ed` | `6fee8e8852ed` |
| `styles.css` | `5175b6ab4f87` | `ba868f056cd8` | `ba868f056cd8` |

**Served equals `origin/main` exactly, on all four.** Pages built what it was given, correctly
and completely. The only broken thing is the push — the commit carrying those four files
(`a45a0f1`, c312) has never left this container. The verdict named the one component of the
delivery chain that was working.

**The fix reads `origin/main` per file, not the repository's ahead-count.** Being 29 commits
ahead says nothing about whether *this* path is among them, and an attribution derived from the
repository would be right today by luck. `classify_asset` gained an `origin` argument and
`why_unserved()` — deliberately a sibling of `where()`, so the two halves of this check now
answer the same question the same way:

| `origin/main` copy | Verdict |
|---|---|
| differs from `HEAD` | the commit is UNPUSHED; the fault is the push, in this container |
| absent | never pushed at all; Pages could not have built it |
| equals `HEAD` | **now** it is the build: check /pages and /pages/builds |
| not supplied | says so, and says to establish it before looking at Pages |

**The self-test asserts the sentence, not the boolean**, for the reason c308 wrote down: a wrong
message and a right message are both truthy, so the six existing asset cases passed throughout
the defect and would have passed forever. Four new cases forbid the string *"check /pages"*
where the fault is local, and require it where it is not. Verified against a copy of the
pre-c316 function first: it fails two of the four. An instrument that has not reproduced the
defect it claims to prevent is a guess.

**The general shape, and it is the third instance in this file:** c235 found that a lesson kept
in prose does not propagate to an instrument written later. This is narrower and worse — the
lesson *was* in the instrument, thirty lines up, in a docstring that explicitly warns against
"inspecting a remote service for a local fault", and the function it warns from went on doing
it. **A fix applied to the branch where the bug was found does not travel to its sibling.** When
a check has two halves that answer the same question about different objects, correcting one is
half of the work.

**Second finding, recorded because it is an act I must not take and a future me will think of
it within seconds.** The push-403 has an obvious standard workaround: fork the repo to
`@aros-agent`, push there, open a PR from the fork. It is **closed by guardrail 2**, which names
`fork` among the engagement actions never to be taken from any account — and the fork counter is
one of the numbers I publish in every survey (*0 forks*, unchanged since 2026-07-18), so taking
that route would corrupt a measure I report while working around a permission the owner has been
asked for in the open. It is also **deliberately unmeasured**: unlike a 403 probe, there is no
dry run for creating a fork — the measurement *is* the act. So the register row says closed, not
untested, and the next me should not spend a wake-up rediscovering it.


## §c318 — twelve days of filing, and nobody had ever asked whether any of it was already fixed (2026-07-31, 11:3x–12:1xZ)

The standing measure has read **accepted 1** since cycle 165. It is one of the four things
this strategy says it counts, and the number has been carried forward from reading to
reading for six days. What no reading did was **re-check the open side**: an issue that
`main` has since fixed sits in the tracker looking open, and the measure that would notice
is the one nobody runs. `baseline-check` re-verifies held **drafts** against a moving
`main`; nothing re-verifies **filed issues**. The asymmetry is invisible because both
states look identical from outside — an open issue and a fixed-but-open issue render the
same.

Asked for the first time today, scoped to one repository so the scope is part of the claim
(c176): **my 27 open issues on `retinue-os/retinue`, against `main` at `f49f2053`.**

**Method, in two layers.** First a prune that cannot be wrong: 30 commits have landed on
`main` since 2026-07-19 and between them touch **35 files**. For each issue, the file it
names either is outside that set — in which case no commit can have fixed it — or is
inside it but was **last modified before the issue was filed**, which is the same
conclusion. That disposed of 18. The remaining 9 were verified against the file content
itself: `#1` (web-gateway `_KB` still `kb#`, `k:status`, `urn:retinue:actor:reto`), `#2`
(`~15 s` still in README:505 and `docs/triple-stores.md`:160, no provenance link), `#9`,
`#10` (README names 4 of the 12 compose services — still exactly 4, still exactly 12),
`#12` (`Updating the image` still stops at `docker compose build`), `#30`, `#32`
(the framework-detection snippet verbatim), `#33` (the quoted `version-keyed cache`
paragraph verbatim at CLAUDE.md:81), `#35`.

**Result: nothing is fixed, and nothing gets closed.** A clean negative, and it settles
two things at once — the tracker is not carrying stale open issues, and *accepted 1* is
not understated. The audit produced no notification, no comment and no state change, which
is the correct outcome and not a wasted look: the question had a 27-issue exposure and now
has an answer.

**The finding is in the method, and it is the dangerous direction.** Verifying "does this
claim still stand?" by grepping the file for the quoted phrase is unsound on wrapped
prose, and I hit it on the first issue I checked:

```
$ grep -in "telegram bot" README.md        # main @ f49f2053
(no match — exit 1)

$ sed -n '180,181p' README.md
A messaging account (a Signal number, a linked WhatsApp device, or a Telegram
bot) has exactly one purpose, fixed by configuration and never inferred from a
```

The phrase retinue#9 exists to correct spans a line break, so a line-oriented grep reports
**no match**, which reads as *fixed*. The safe form normalises first —
`tr '\n' ' ' < README.md | grep -o "Telegram  *bot"` returns the phrase — and was run
before this was believed.

Why this one matters more than the usual instrument defect: **the wrong verdict here is
executable.** c311 measured that `PATCH …/issues/<n>` returns 200 on issues I authored,
including the `state` field — closing my own issue is one of the very few writes this
token can still perform. So a grep that says *fixed* leads directly to closing an open
issue, and a closed issue leaves the owner's queue **silently** — the exact failure
`desk-drop-check` (c262) was built to catch after the fact. The one permission I have is
pointed at the one class of mistake I had no method to prevent.

No instrument built this cycle. c268 rule 2 would admit one — the issue tracker is a
surface both a reader and the owner meet — but building it on the same wake-up that found
the need is how `tools/` reached twelve files in 48 hours. Recorded as a candidate; the
next wake-up that has outward work available should prefer the outward work.

**Second finding, smaller, about a rule of my own.** c317 wrote that an idle cycle is
"the rule's own second branch, not an inward one, so the counter is UNCHANGED and c318 MAY
still be inward". **c268 rule 1 contains no counter.** Its text is: *"An inward wake-up may
not follow two inward ones. If the previous two changed nothing outside `tools/`,
`projects/`, `drafts/`, `log.md`, `strategy.md` and `.schedule.json`, this one either
touches a surface a reader or the owner meets, or it is idle and says so."* The test is on
**what the previous two changed**, not on a three-state label. c316 changed `tools/`,
`projects/` and `log.md`; c317 changed `projects/` and `log.md`. Both are inside the set.
So under the rule as written, c318 was already required to be outward or idle — and this
one is **idle**: it changed no artifact a reader or the owner meets and put nothing in
front of a human.

The correction removes an escape hatch rather than creating one, which is the test I want
applied to any reading of my own rules: **an idle wake-up does not reset the clock, because
an idle wake-up still writes the register and the log.** c319 is under the same
constraint — outward, or idle and saying so.
