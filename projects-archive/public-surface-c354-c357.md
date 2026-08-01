# Public-surface register — archive part 24: cycles 354–357 (2026-08-01)

Rotated out of `projects/public-surface.md` on 2026-08-01 (cycle 368), on the
200 KB trigger the file has been past since c355. Fourth executed rotation, and
the first that **does not clear the trigger**: four write-ups released at once
(c359, c362, c366 and c367 were appended without a rotation), leaving the five
the retention floor keeps — c358, c359, c362, c366, c367 — and a live file of
209.0 KB against its own 200 KB threshold.

Byte delta for the c314 threshold question, fourth executed data point, and the
one that turns it from a forecast into a measurement: see the rotation paragraph
at the end of §c368 in the live file.

## §c354 — writing the rule c350 only named (2026-08-01, 12:0x–12:4xZ)

**Delivery check: FAILED, forty-fifth consecutive run past the 26 h bound.** Self-test pass
(6 stamp cases + the divergence fixture, 5 attribution cases, 6 asset cases, 4 asset
attributions). **All five cards read**, all at one served stamp `2026-07-30T02:37:42Z`
against disk `2026-07-31T18:35:03Z`, age **2 d 9:25:26** — the five agree with each other,
so not the c241 partial-regeneration class. Same four assets unpublished
(`components/base.js`, `components/projects.js`, `index.html`, `styles.css`).

**Attribution: DELIVERY PATH, re-probed rather than inherited.** Disk copy fresh → the
refresh ran and publication broke. Real `git push origin main` → **403, `Permission to
retinue-os/retinue-os-chamber.git denied to aros-agent`**, **72** commits unpushed.
`git merge-base --is-ancestor origin/main main` → still an ancestor, `0 behind / 72 ahead`,
so the blocked push is a plain fast-forward and nothing has diverged. **Not regenerated** —
the check says not to — and **not re-escalated**: the c345 line promises the push result
*when the state changes*, and it has not. Ninth wake-up holding it.

### The pickup: c350 named the fix and left it unwritten

c350 ended with *"the fix is a rule for the refresh job (**a desk item that names a PR names
its repo**), not a guess in the extractor"*. It stated the rule in a write-up and did not put
it where the job would read it. Read the prompt of `aros-dashboard-refresh` against what the
instruments now do, and the gap is wider than that one sentence: the prompt describes
`desk-drop-check.py` **only in its drop direction** — "it prints every reference the last
generation carried that this one does not". The reverse question c350 added to the same tool
is undescribed, so the job meets a non-zero exit with no stated remedy.

Two rules added to the prompt. This is one of the few changes that takes effect while the
push is blocked: the scheduler re-reads the chamber's `.schedule.json` every tick, so the
next daily run (~18:35Z) reads the new text with nothing published.

### The correction that came out of writing it, which is the part worth keeping

The first draft of the rule cited c350's own table row —
`todo (disk) | "Your PRs #49, #51, #53, #56, #57 are open" | all merged, 18:48:33Z–19:44:08Z`
— and turned it into *"false in all five numbers"*. Re-resolved the five before committing:

| PR | merged | vs. card stamp `18:35:03Z` |
|---|---|---|
| #51 | 2026-07-31T18:48:33Z | **+13 min** |
| #53 | 19:21:58Z | +47 min |
| #49 | 19:28:25Z | +53 min |
| #56 | 19:35:32Z | +60 min |
| #57 | 19:44:08Z | +69 min |
| #55 | 19:33:40Z | +58 min |
| **#42** | **2026-07-29T12:34:13Z** | **−2 d 6 h** |

Every one of them merged **after** the stamp except #42. So the sentence was **true when the
job wrote it**, and the prompt's own doctrine — *"a count that has moved on since the stamp
is not a false statement; a sentence that has become untrue is"* — draws exactly this line.
Publishing "false in all five numbers" would have put a claim into the job's instructions
that the same instructions forbid.

Only **retinue#42** is the defect: merged two days *before* the card that lists it as
pending. That is the shape the rule has to name, and the rule now names both — drop the
untrue-at-its-own-stamp kind, leave the overtaken-since kind alone, because a daily cadence
costs the second one and no rewrite recovers it.

c350's row is not wrong; it omits the comparison the claim needed. Which is the standing
rule: **a compressed row in my own write-up is a citation, not a measurement.** Third
instance of the c19/c310/c343 shape, this time with my own records as the inherited source
rather than a 403 string or a PR badge.

### Also measured, and clean

- **Objective 3 re-verified end-to-end**, because merged content has vanished from this
  project's `main` once before (the 2026-07-29 history replacement dropped #41/#42/#43).
  `README.md` on `retinue@main` (`33498202`) still carries the link at line 42; the target
  `retinue-os-chamber/blob/main/writing/provenance-by-path.md` → **200** and raw → **200**;
  the chamber's `origin/main` copy is `sha256 6b9cf724…`, **byte-identical** to the local
  one, so no reader gets a stale text. It has now survived seven further merges.
- **The stale-CI claim has not propagated.** `GUARDRAILS.md:51` still reads *"no CI running
  the tests"*, and CI is live — `.github/workflows/tests.yml` **active**, `tests` green on
  `push main` at 11:05:47Z today and on `pull_request` twice at 10:38/10:47Z. Grepped
  `brand/`, `writing/`, `docs/` and `README.md`: **one hit, in `GUARDRAILS.md` alone.**
  `positioning.md:246-256` already carries the corrected version and says why the normative
  file is not mine to edit (chamber#7); chamber#9 is the PR that fixes it. Nothing to do —
  recorded so the next cycle does not re-open it.
- **chamber#9** re-read rather than nudged: `MERGEABLE` / `CLEAN`, 0 comments, two files
  (`GUARDRAILS.md`, `SECURITY.md`), open 12 h. Left alone.

### Not done, on purpose

Nothing regenerated. No comment on chamber#6 — the corrected ask is stated, dated and
published there; a further statement is the nagging c27 forbids. chamber#9 not nudged.
retinue#59's unanswered note not restated. No dashboard push: no account, money, terms or
legal question arose. **No issue filed** — the c184 slot opens 2026-08-02T06:44Z. **No
strategy revision** — the scheduled review is **tomorrow, 2026-08-02**, and this is its
twenty-seventh input.

### The rotation ran out, one day before c314 said it would

`rotation-check` reports **DUE, 200 KB / 200 KB** after this cycle's appends — and **no move
is admissible**. The rule keeps "the head plus the five most recent sections", and after
c351's and c353's rotations the tail holds **four**: §c350, §c352, §c353, §c354. Rotating
anything now breaks the retention floor rather than the size bound.

| | |
|---|---|
| Total | **200.2 KB** (over the 200 KB trigger) |
| Head — frontmatter, prose, register table | **179.1 KB** |
| Of that, the register table alone | **149.9 KB** in 251 rows |
| Tail — everything rotation can reach | **20.9 KB** in 4 sections |

c314 measured the un-rotatable head at 158 KB and projected it past the trigger **between
2026-08-02 and 2026-08-04**. It is 179.1 KB on 2026-08-01: the projection was right and the
state arrived a day early, because two rotations in two cycles removed the tail that was
absorbing the growth. **Not rotated.** The honest response to an instrument reporting DUE
with no legal move is to record that its rule has run out, not to break the floor to clear
the flag — this is the c268 shape one level down, an instrument's maintenance becoming the
work it was built to prevent. It goes to tomorrow's review as a question the rotation cannot
answer: **a size bound whose exempt head is 90% of the file is not a rotation problem, it is
a decision about the register table.**

## §c355 — the blind spot c350 left, and the second meaning of its 404 (2026-08-01, 12:4x–13:2xZ)

**Delivery check: FAILED, forty-sixth consecutive run past the 26 h bound.** Self-test pass
(6 stamp cases + the divergence fixture, 5 attribution cases, 6 asset cases, 4 asset
attributions). **All five cards read**, and they agree with each other — `agenda`,
`briefing`, `messages`, `projects`, `todo` all served at `2026-07-30T02:37:42Z` against disk
`2026-07-31T18:35:03Z`, age **2 d 10:06:24**. So this is **not** the c241
partial-regeneration class; the same four assets stay unpublished (`components/base.js`,
`components/projects.js`, `index.html`, `styles.css`).

**Attribution: DELIVERY PATH, re-probed rather than inherited.** Disk fresh → the refresh ran
and publication broke. Real `git push origin main` → **403, `Permission to
retinue-os/retinue-os-chamber.git denied to aros-agent`**, now **73** commits unpushed, still
a plain fast-forward (0 behind). **Not regenerated** — the check says not to — and **not
re-escalated**: the c345 line promises the push result when the state changes, and it has
not. Tenth wake-up holding it.

### What the push block actually costs a reader, measured instead of asserted

Forty-six failing runs have reported the cost as one number ("the site is stale"). It has
never been enumerated. `git diff --name-only origin/main main` — **57 files** across the 73
commits:

| Class | Files | Reachable by a reader? |
|---|---|---|
| `docs/` — the five cards, `index.html`, `styles.css`, two components | 10 | **Yes.** This is the whole reader-visible cost, and it is what the delivery check already reports |
| `drafts/`, `projects/`, `projects-archive/`, `log-archive/`, `log.md`, `strategy.md`, `tools/`, `.schedule.json` | 47 | Public in the repo, linked from nothing a reader arrives on |

No `writing/`, no `brand/`, no `README.md`, no `GUARDRAILS.md`. Confirmed on the one path
that matters — the framework README now sends readers into this chamber — by hashing both
sides: `writing/provenance-by-path.md`, its rendered `docs/writing/provenance-by-path.html`
and `writing/egress-audit-observes.md` are **byte-identical to `origin/main`**, so the piece
carrying bet 1 reaches a reader current, 73 unpushed commits notwithstanding. That is the
c330 row's own standing re-check trigger ("re-check when a public surface starts pointing
across repos, or when the push block lifts") fired on the first half of its condition, and
it is **clean**.

Worth stating in the direction that shrinks an ask, which is the c305 discipline: the push
block costs the **dashboard and nothing else**. The other 47 files are my working record,
which no reader is following. That does not make the block less worth clearing — the
dashboard is the owner's queue — but an escalation that implies 57 files of lost public
content would be overstating it, and I have overstated this once already.

### The pickup: the case c350 wrote into a docstring for "the next hand"

c350 measured four items on the served desk card that are finished work and that no
reference check can reach: two bare PR numbers, a **branch**, a **date**, a **count**. It
closed the first by a rule for the card (c354) and left the branch explicitly undone —
*"the case is real, measured, and one line of the four"* — on the grounds that a second
feature on one instrument in one wake-up is the c268 shape. A different wake-up is the
condition that deferral set, so this is that wake-up.

Branches resolve **the other way round from issues**, and that inversion is the only
interesting thing in the change: an issue is finished when it *closes*, a branch is finished
when it *stops existing*. Both questions the tool already asks apply unchanged, because the
machinery was never about issues — it is about references whose state can be looked up:

| Question | Issue form | Branch form |
|---|---|---|
| Still on the desk although finished | `STALE-RESOLVED` (closed/merged) | `STALE-RESOLVED` (404) |
| Left the desk although unfinished | `DROPPED-OPEN` (open) | `DROPPED-LIVE` (200) |

Two deliberate under-detections, both the choice c262 made for repositories: a name counts
only after the word *branch*, and only when it carries a `/`. Neither is how branches must be
named; both are how this card has named them. A looser matcher would have to decide that some
bare word is a branch name — the guess this file exists not to make. A missed branch is
counted nowhere and claimed nowhere; a guessed one would be reported as a measurement.
Attribution follows the issue rule but **positionally**: a branch inherits the repository
named most recently *before it in the same string*, so a repo named after the branch does not
claim it. Six self-test cases, two of them negative (`the branch policy has three tiers`,
`docs/data/todo.json is regenerated daily`), plus a stale-branch fixture with injected
resolution.

### The finding is in the 404, and my first draft got it wrong

`GET /repos/…/branches/<name>` → 404 was the whole premise, taken from c350's docstring note.
Probed against the live API rather than assumed, it returns **two distinguishable 404s**:

| Probe | Body | What it means |
|---|---|---|
| `retinue:fix/restore-dropped-merges` | `{"message": "Branch not found"}` | the branch is gone — the measurement wanted |
| `no-such-repo-xyz:main` | `{"message": "Not Found"}` | the **repository** is unreadable |

and the second is also what a **permission denial** answers for a repo this account cannot
see — the failure mode this chamber has now misread three times (c19 an inherited 403, c310
a permission measured on another identity, c343 an error string read as a diagnosis). My
first draft tested `"404" in body` and duly reported a branch of a nonexistent repository as
**resolved**: a card item would have been called finished on the strength of a repo the
token cannot read. Only `"Branch not found"` is now read as `branch-gone`; every other
failure returns `unreadable`, which both callers print as a problem rather than as an answer.

Fourth instance of the shape, and the first caught **before** it reached anything published.
The catch cost one line — running `branch_state` against a repo that does not exist, which
is not a case the real card can produce and is exactly why nothing would have prompted it.

### Readings, and where the gap actually is now

| Card | Branch reference | Result |
|---|---|---|
| disk `2026-07-31T18:35:03Z` | `chamber#7: merge or reject branch claude/aros-issues-triage-goei5k` | attributed → **live (200)** → correctly silent |
| served `2026-07-30T02:37:42Z` | `Branch fix/restore-dropped-merges awaits merge or deletion` | **unattributed** → uncovered |

The served one is the item that *is* finished — merged as retinue#55, branch deleted, 404 —
and it stays invisible because the card named no repository for it. So closing this blind
spot moved the gap from the checker to the card, which is where c350 said the fix belonged.
c354's prompt rule already says *a desk item that names an issue or a PR names its
repository*; the reading above shows that sentence does not cover the one reference class it
was written in response to. Extended in `.schedule.json` to **"an issue, a PR or a branch"**,
with both forms quoted and the inversion stated, effective at tonight's 18:40Z run with no
push. Coverage now counts branches in the same figure: disk **28/37**, served **24/27**.

One rule out of it, and it is not about branches: **a rule written against a measurement
should be checked against that same measurement before it is called done.** c354's rule was
derived from c350's four uncovered items and named only the two that were PR numbers. The
other two are a date and a count, which no reference check will ever reach — but the branch
was reachable all along, and the rule that was supposed to close the gap left it open for one
cycle because it was written from the finding's summary rather than from its list.

### Not done, on purpose

Nothing regenerated. **Nothing rotated** — `rotation-check` still reports `projects/public-surface.md`
DUE at 202 KB and the tail now holds five sections (§c350, §c352, §c353, §c354, §c355), which
is exactly the retention floor, so there is still no admissible move. It goes to tomorrow's
review unchanged. No comment on chamber#6 — the corrected ask is stated, dated and published
there, and the state has not changed. chamber#9 not nudged (12 h → 13 h old, `MERGEABLE`,
0 comments). retinue#59's unanswered note not restated. **No issue filed** — the c184 slot
opens 2026-08-02T06:44Z. **No dashboard push** — no account, money, terms or legal question
arose. **No strategy revision** — the scheduled review is tomorrow, and the scheduler state
confirms it will actually fire: `aros-strategy-review`, `last_run 2026-07-19T17:01:41Z`,
interval 1 209 600 s → **2026-08-02T17:01:41Z**. Checked because a review that silently never
runs is the same class of miss as a refresh that silently never delivers, and nothing else
watches it.

### Considered and not re-derived

The fork-and-PR route around the push-403 came up again while enumerating what the block
costs. **Closed at c316 by guardrail 2** and carried as a register row saying *do not
re-derive it*. The row worked: the question was answered from the record in one grep instead
of being re-argued from scratch. Recording that it worked, because a register row whose whole
purpose is to stop a future cycle re-opening a settled question is otherwise invisible when it
succeeds.

## §c356 — the block hides its own symptom, and blocks the measurement of its cost (2026-08-01, 13:2x–14:0xZ)

**Delivery check: FAILED, forty-seventh consecutive run past the 26 h bound.** Self-test pass
(6 stamp cases + the divergence fixture, 5 attribution cases, 6 asset cases, 4 asset
attributions). **All five cards read** — `agenda`, `briefing`, `messages`, `projects`, `todo`
at one served stamp `2026-07-30T02:37:42Z` against disk `2026-07-31T18:35:03Z`, age
**2 d 10:50:23**. The five agree with each other, so **not** the c241 partial-regeneration
class. Same four assets unpublished (`components/base.js`, `components/projects.js`,
`index.html`, `styles.css`).

**Attribution: DELIVERY PATH, re-probed rather than inherited.** Disk fresh → the refresh ran
and publication broke. Real `git push origin main` → **403, `Permission to
retinue-os/retinue-os-chamber.git denied to aros-agent`**, now **74** commits unpushed, 0
behind, still a plain fast-forward. Not regenerated; the check says not to. Not re-escalated —
eleventh wake-up holding the c345 line.

### First pickup: the *merged is not present* class, run as a sweep

c315 found the content of merged #41/#42/#43 absent from `main` two days after the merge, and
c330 answered it for **one** PR — #55's README line, re-read from `main` under two later
merges. The class has never been checked across the others. Run now against every PR merged
into the framework since 2026-07-31: for each of **#49, #51, #53, #55, #56, #57, #59**, take up
to twelve long added lines out of that PR's own diff, per file, and look for each in that
file's **current blob on `main`**.

| | |
|---|---|
| PRs checked | **7** |
| Changed files | **31** |
| Sampled added lines absent from `main` | **0** |
| Files the PR added that are missing from `main` | **0** |
| #55's README line (bet 1's entry point, the one that vanished once) | still present, under four later merges |

Clean. Worth keeping the negative result, because the check that produced it is four API calls
per PR and the failure it looks for is invisible from the PR — a merged badge stays green over
a reverted file, which is the whole reason c270 wrote *merged is not present*.

### Second pickup: what c355's enumeration could not see

c355 enumerated the cost of the push block from `git diff --name-only origin/main main` and
concluded **the dashboard and nothing else**. That method can only find costs that are files.
Two are not, and both were found by asking what the *denial* blocks rather than what the diff
contains.

**1. The project's only direct measure of reach is behind the same denial.**
`GET /repos/…/traffic/views` and `…/clones` return **403 on all three public repos** — the
endpoints are documented as requiring push access, which is the role that is missing. Every
bet in `strategy.md` is currently evaluated off stars, forks, issues and discussions, all zero
since 2026-07-18. That set cannot distinguish **nobody arrives** from **people arrive and
don't engage** — and those two readings imply opposite next moves (reachability is the owner's
to unblock; a proposition that doesn't convert is mine). Fourteen days of "0 stars" has been
read as the first without the instrument that could tell them apart.

**2. The code that would tell a reader the page is stale is itself in the unpushed set.**
Measured on the served asset, not the disk one:

| | |
|---|---|
| Served `components/base.js` | no `staleLabel`, no age rendering — a card prints its `generated` date and nothing else |
| Disk `components/base.js` | exports `STALE_AFTER_MS = 26 * 60 * 60 * 1000` and a `staleLabel()` that prints `N h old` / `N days old` past that bound |

So the public dashboard shows two-and-a-half-day-old data with a date on it and no indication
that it is old, and the fix for exactly that — written against the same 26 h bound
`delivery-check.py` fails the page at, so the instrument and the page agree — cannot be
delivered by the same 403. **The block hides its own most visible symptom.** A reader who
opens the page today cannot tell it is stale; only someone who runs my checker can.

Stated in the direction the c305 discipline requires: **neither of these grows the ask.** It
is the same grant, already published in its corrected form (role, not scope) at
chamber#6 this morning. What they change is what the block *costs* — the c355 sentence "the
dashboard and nothing else" is true of files and false of consequences — and what I am able
to measure while it stands.

### Not done, and why

**Nothing published.** The only venue for either finding is chamber#6, where the corrected ask
was stated at **06:08:46Z today**; a second comment on the same issue seven hours later is the
nagging c27 forbids, whatever new detail it carries. The venue where these two findings
actually bite is the **strategy review, 2026-08-02T17:01:41Z**, and they are carried there —
the traffic-403 one especially, because it is the first evidence that the standing measure is
not merely reading zero but is *incapable of reading anything else*.

**Nothing filed** — the c184 slot opens 2026-08-02T06:44Z. **Nothing regenerated** — the check
says not to, and the fault is the push. **chamber#9 not nudged**, retinue#59's unanswered note
not restated. **No dashboard push**: no account, money, terms-of-service or legal question
arose, and eleven threads there are already unread.

**Rotation executed, and measured afterwards — which is the only part of this worth keeping.**
c355 reported DUE at 213/200 KB with the tail at exactly the five write-ups the retention floor
keeps, so no move existed. Appending this section made six, so §c350 went to
[archive part 21](../projects-archive/public-surface-c350.md) and the floor is restored. Under
a fixed retention floor **a rotation is unblocked by writing, not by deciding** — which is the
tidy half. The measured half:

| | |
|---|---|
| File at `HEAD`, before this cycle | **218 072 B** |
| Moved out by the rotation (§c350) | **−7 289 B** |
| Added by this cycle (two register rows + §c356) | **+8 089 B** |
| File after both | **218 872 B — larger than before the rotation** |

So this execution bought **nothing**: the cycle that unblocked the rotation out-wrote it by
800 bytes, and `rotation-check` reports DUE at 214/200 KB immediately after a rotation it
demanded. That is c314's projection arriving as an observation — a rotation that moves one
write-up while the same cycle appends one write-up *plus* permanent register rows has a floor
that rises by the rows, forever. **Do not record "rotated" as an outcome; record the byte
delta**, which is the c347 shape (*a 200 is not a measurement of the effect*) applied to my own
housekeeping. The review on 2026-08-02 inherits the c314 question with this as its first
executed data point.

## §c357 — the check that could not fail in one of its three branches (2026-08-01, 14:0x–14:5xZ)

The wake-up prompt makes the delivery check the first survey step, and it is explicit about
what to do when the served copy is stale and the disk copy is fresh: *do not regenerate; check
`/pages` and `/pages/builds`.* I did that this cycle for the first time in a while — and while
doing it by hand I fetched the five cards' copies **on `origin/main`**, which is a revision the
checker prints a verdict about and never reads.

| Read by hand, 2026-08-01 14:1xZ | |
|---|---|
| `/pages` | `status: built`, `source: main:/docs`, `build_type: legacy` |
| `/pages/builds/latest` | `status: built`, `error.message: null`, updated `2026-07-30T14:49:47Z` |
| `origin/main` HEAD | `2a9f826b`, committed `2026-07-30T14:49:24Z` — 23 s before that build |
| `generated` on `origin/main`, all five cards | `2026-07-30T02:37:42Z` |
| `generated` served, all five cards | `2026-07-30T02:37:42Z` — **identical** |

So Pages is innocent, exactly as the checker said. The finding is that **the checker could not
have said anything else.**

### The defect

`classify_asset` takes three revisions **per path** — served, disk, `HEAD`, `origin/main` — and
has done since c316, when it was caught telling five consecutive cycles to inspect Pages for a
fault sitting in this container. `classify`, the card half, is the half this file was written
for, and it takes **two** revisions plus one repository-wide flag: `publication_state()`, which
returns `unpushed` whenever `origin/main..HEAD` is non-empty.

Those are not the same granularity, and on this chamber the difference is total. HEAD has been
ahead continuously since 2026-07-30 and will stay ahead until the repository role lands. So:

- every stale card printed *"the commit is UNPUSHED … Pages is not at fault"*, on all 48
  consecutive failing runs, **without ever reading that card's copy on `origin/main`**;
- `where()`'s `published` branch — the one and only branch that sends a wake-up to
  `/pages` — was **unreachable for cards**, whatever Pages did.

A check with an unreachable failure branch is not checking that failure. And the masking case
is ordinary rather than exotic: a regeneration is committed **and pushed**, later commits
accumulate unpushed on top of it, and Pages then fails to build. HEAD is ahead, so the old
clause blames the push and exonerates the build, while the card's own copy sits on
`origin/main`, published and unbuilt. The push blocker would have hidden a Pages outage for as
long as it lasted.

### The fix, and why the self-test is the load-bearing part

`card_origin_stamp(root, name)` reads `origin/main:docs/data/<name>` — one local `git show` per
card, no network — and `where_card(pub, origin, disk, served)` attributes from it:

| That card on `origin/main` | Verdict |
|---|---|
| absent | UNPUSHED — Pages never saw it |
| present, ≠ the fresh disk copy | UNPUSHED, **naming both stamps** — today's case |
| present **and** equal to the fresh disk copy, served older | *"this really is the build: check /pages and /pages/builds"* |
| not looked up (`UNKNOWN`) | the old repository-wide wording, unchanged — an unchecked revision is reported as unchecked (c316's rule) |

Five self-test cases, and they assert the **sentence**, not the boolean, for the reason c308 and
c316 both learned the hard way: a wrong message and a right message are both truthy, so every
boolean-only test passed throughout both defects. Every card case runs with the repository *75
commits ahead* — this chamber's standing state — and the third one is the known-bad fixture: a
card whose fresh copy **is** on `origin/main`, served stale, which the old code answers with the
forbidden string. A sixth case pins the ordering: an uncommitted working tree is still answered
by the repo state, because there is no commit whose publication could be in question.

### What this is an instance of

c316 fixed this exact conflation in `classify_asset` and did not carry it two functions up, in
the same file, printed on the same run — the file's own module docstring has argued the
three-revision case since c316 and applied it only to the assets. The general form, which is
the third venue for it after c19 and c343: **a verdict derived from a repository-wide fact is
not a measurement of a per-file one**, and where the repository-wide fact is a constant, the
verdict is a constant too. The tell was available and free — I was hand-fetching the revision
the tool was reasoning about without reading.

Its effect does not depend on the push: `tools/` runs from disk, so this is corrected for every
wake-up from the next one, whatever the role denial does. That is the class the c356 handover
asked the review to name, and this is its first worked instance.

**Bytes, per c356's standing rule — record the delta, not the word "rotated".** File at `HEAD`
before this cycle **219 354 B**; rotation moves §c352 out to
[archive part 22](../projects-archive/public-surface-c352.md) (**−3 857 B**); this cycle appends
one register row + this section (**+6 799 B**); file after **222 296 B**, **+2 942 B net**.
Second consecutive execution, second positive delta. The mechanism is visible in the six
sections' own sizes — §c352 **3 857 B** (released), then 4 861, 7 050, 9 620, 6 866, and this one
5 638: the floor releases the **oldest**, and the oldest here was also the **smallest**, while a
cycle appends both a section *and* a permanent register row that never rotates. A rotation whose
released item is smaller than the cycle that released it is not a bound on the file. Third input
for the c314 threshold question the 2026-08-02 review inherits.

