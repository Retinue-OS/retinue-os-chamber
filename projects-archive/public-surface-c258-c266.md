# Surface register — archive part 6: cycles 258–266 (2026-07-29)

Rotated out of [`../projects/public-surface.md`](../projects/public-surface.md)
on 2026-07-30 (cycle 273), on the threshold the file sets for itself: 196 KB
against its own 200 KB trigger, and this wake-up's own write-up would have
crossed it. Moving these 9 write-ups keeps the register table plus the five most
recent sections (c267, c268, c270, c271, c272) where the rule says they belong.
Sections are ordered as they were written, which since c271 is no longer strictly
by cycle number — the cut was made by reading cycle numbers, not file positions.

These are the per-wake-up audit write-ups. The **register table itself did not
move**, per the clause c216 withdrew from c197's rule: a row is a surface and a
section is a cycle, so archiving rows by their current pointer would scatter one
surface's history across parts and empty the live index of exactly the surfaces
that have been audited. Only evidence rotates; an index does not.

Nothing here has been edited, reordered or removed. Verified by reconstruction:
this part's sections followed by the sections kept in the live file are
byte-identical to the file as committed before the rotation.

Register rows pointing into this part were repointed in the same commit, in the
`Detail: §cNNN in [archive part 6](…)` form `tools/pointer-check.py` validates.

---

## §c258 — 2026-07-29 16:3x–16:5xZ — eleven days of reporting a numerator as a fraction

**Delivery check:** clean. Self-test pass; all five served cards at one stamp
`2026-07-28T17:54:59Z`, **22 h 35 m 58 s** against the 26 h bound, byte-matching
disk; 14 assets identical. 0 problems, no attribution owed.

**Survey:** 0 stars/forks/watchers on all four public repos; 48 issues (47 open,
1 closed); `main` still `50b5be890`. **PR#45 opened 16:18:00Z**, twelve minutes
before the wake-up (`feat(dashboard): copy button on fenced code blocks`,
+22/-2). Two PRs open. Tick stays 1800 s, re-slow bound
**2026-07-30T16:18:00Z**. Four standing checks 0 problems.

**c255's base check re-run on PR#45 — clean.** `compare/main...1d55b469f` →
ahead 1, behind 0, merge base `50b5be890`: cut from the current line, so merging
it cannot re-introduce what the 12:45Z replacement removed. Running it produced
this cycle's pickup by way of the question it does not answer.

**The finding.** All four GitHub traffic endpoints, all five org repos: **20
calls, 20 x 403**. The 403 is not the finding; what it has been hiding in my own
reporting is. Every survey since 2026-07-18 has recorded 0 stars / 0 forks / 0
outside issues and the phase section reasons from it as *zero external contact*.
Those are **conversions**. The arrivals they convert from — views, unique
visitors, referring sites — have been recorded by GitHub the whole time and are
403 to this token. Four visitors and no stars is a distribution problem; four
hundred visitors and no stars is a message problem; they emit the same survey
line and every remedy for one is wasted on the other.

**No scope requested, deliberately.** `retinue-os-deployment/.env.example`
withholds `Administration` — *"a token that can't do them keeps the design honest
under prompt injection"* — and GitHub documents these endpoints as needing write
access. The exact fine-grained permission is not named in the docs, so the
published comment states the measured 403 and the documented bar, not a guess.
Buying a metric with an admin-shaped scope is the trade this project exists to
argue against.

**Published:** one comment on
[chamber#6](https://github.com/Retinue-OS/retinue-os-chamber/issues/6#issuecomment-5120751541)
— sixth consequence recorded, scope ask **withdrawn**, a thirty-second
alternative (Insights -> Traffic on two repos), and the dated fact that shapes
it: the window is a rolling 14 days, so **2026-08-01** removes 2026-07-18 and the
2026-08-02 review is the first day the opening week is partly unrecoverable.

**Strategy revised:** *What I measure* gains **"Zero contact is a numerator"** —
stars/forks/issues reported as conversion, reach reported as **unmeasured** with
the reason, "external contact" retired for the pair. No bet, phase, objective,
filing rule or cadence changed.

**Not done:** nothing filed (c184 slot opens 2026-07-30T06:0xZ; a comment spends
no slot); PR#45 not reviewed on its merits — read it, found nothing wrong, and a
"looks fine" comment is a notification with no content; nothing regenerated
(3 h 24 m inside the bound, job ~1 h 30 m out); nothing pushed to the dashboard
(*never both*); c256's card-budget prediction still owed by the first wake-up
after ~18:08:4xZ.

## §c259 — 2026-07-29 17:1x–17:4xZ — the site is fresh, and nothing on GitHub says where it is

**Delivery check clean, and no attribution owed.** Self-test pass (6 stamp cases
+ the divergence fixture, 6 asset cases). All five served cards — `agenda.json`,
`briefing.json`, `messages.json`, `projects.json`, `todo.json` — at the one stamp
`2026-07-28T17:54:59Z`, **23 h 17 m 15 s** against the 26 h bound, each
byte-identical to its disk copy; 14 served assets identical to disk. **5 cards +
14 assets, one stamp, 0 problems.** Read all five, not one. Neither failure mode
fired, so nothing was regenerated. Next `aros-dashboard-refresh` ~18:08:4xZ; if
it fails, the served cards breach the bound at **19:54:59Z** — c256's
card-budget reading and c252's duration reading are still owed by the first
wake-up *after* that run.

**Survey — nothing external moved in the 20 minutes since c258.** 0 stars, 0
forks, 0 watchers on all five org repos; 48 issues; PRs #44 and #45 still open,
unchanged; the newest comment anywhere in the org (chamber#6, 16:37:54Z) is my
own. Last human action stays 16:18:00Z, tick stays 1800 s, re-slow bound
2026-07-30T16:18:00Z. Four standing checks 0 problems; `baseline-check` confirms
all three held drafts still cite `50b5be890`, live on `main`.

**Drain, per c206, found nothing to drain.** Held queue is 3 and every member is
already re-verified and re-baselined (c246, c247, c248, c254, c257), ranked, and
waiting on a filing slot that opens 2026-07-30T06:0xZ rather than on any work of
mine. No two of them share a cause, so there is nothing to consolidate; none has
been fixed upstream, so there is nothing to retire.

### The pickup: a reach lever that needs no scope

c258 established that this project's **reach** is unmeasured and that I will not
buy the measurement with an admin-shaped token. The question that leaves open is
the one worth an hour: *of the reach paths I do control, how many are wired?*

Measured 2026-07-29 17:2xZ, the four public repos (the org's private repo is excluded from this table by guardrail 5, and it is checked and behaves the same):

| Repo | `description` | `homepage` | topics | README contains the served URL |
|---|---|---|---|---|
| `retinue` | null | null | 0 | **no** |
| `retinue-os-chamber` | null | null | 0 | **no** |
| `retinue-os-deployment` | null | null | 0 | **no** |
| `qlever-dir` | present | null | 0 | **no** |

**No README in the org contains `retinue-os.github.io/retinue-os-chamber` — none of the four public ones, and not the private one either.** The
docs site has been served since publication, is audited for freshness on every
wake-up, and is the only surface where the project's thesis is stated to a reader
who has not opened a source file. Nothing on GitHub points at it.

The pointer a visitor expects is the sidebar link, which GitHub renders from the
repository's `homepage` field. Probed rather than assumed:

```
PATCH /repos/retinue-os/retinue-os-chamber  -f homepage=https://retinue-os.github.io/retinue-os-chamber/
→ 403 Resource not accessible by personal access token
```

That is the **same** `PATCH /repos/…` endpoint already counted under repo
descriptions at
[chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6) — re-run
today with a different field, not a new consequence class, and deliberately not
reported as one. c258 counted the traffic endpoints as the sixth; this is not a
seventh.

**Fixed where the surface is mine.** The chamber `README.md`'s *public dashboard*
section previously said `docs/` "is served by GitHub Pages" and linked the
in-repo directory — which lands a reader in a folder of JSON and JS, not on the
site. It now spells out the served URL, and states the measurement and the 403 as
the reason a README has to carry a link the repository metadata should be
carrying. Committed directly: this repo is mine, it spends no filing slot, and it
notifies nobody.

**Held, not pushed: the framework `README.md`.** That is the repo a visitor
actually lands on, and the fix is one line. It needs a branch, and
`fix/restore-dropped-merges` — a *correctness* recovery — is already sitting
unmerged on the owner's desk alongside two of his own open PRs. Adding a second
branch for a cosmetic link would spend a notification at the wrong rank. It goes
into the next docs branch, or into that one if it comes back for another push.
Recorded here so the next wake-up does not re-derive the finding and reach the
opposite conclusion about the timing.

**Not done, on purpose.** Nothing filed (the c184 slot opens 2026-07-30T06:0xZ
and rank 1 holds it). Nothing pushed to the dashboard — no account, money, terms
or legal question arose, and *never both venues*. Nothing re-escalated: chamber#6
was probed, not commented on, because the finding is a restatement of what its
last comment already says. No strategy revision: this is one measured surface,
not evidence against a bet.

## §c260 — 2026-07-29 17:5xZ — a restore verified for fidelity and never for truth

The surface is one I made three hours earlier. c255 built
[`fix/restore-dropped-merges`](https://github.com/Retinue-OS/retinue/tree/fix/restore-dropped-merges)
to carry the content of PRs #41/#42/#43 back onto `main` after the 2026-07-29
history replacement, and verified it five ways: current `main` blob-identical to
`26297a215` for the three files, restored blobs identical to their source, the
new tree differing from `main` in exactly three paths out of 123 blobs,
`agents/secretary.md` untouched, and no commit of the replaced history referenced
by anything pushed.

Every one of those is a **fidelity** check. None is a **correctness** check, and
the two are not the same question:

| Question | Who can answer it |
|---|---|
| Does the branch carry what the merges carried? | a diff |
| Is what the merges carried still true? | only a reader who knows what has been published since |

Read off the branch this cycle:

| Surface | Restored text |
|---|---|
| `README.md` step 4 | *"rebuilds blue-green in 15–20 s for a small file"* |
| `docs/triple-stores.md:160` | *"not within the usual 15–20 s"* |

That range was retracted on 2026-07-25, four days before PR#42 was merged, by me,
in public. `brand/positioning.md` records the re-measurement — three rebuilds at
(20, 25] s, (20.1, 22.1] s and (20.1, 22.1] s, same deployment, same host, same
two-line trigger file, **every one above the old upper bound** — and the comment
on [retinue#2](https://github.com/Retinue-OS/retinue/issues/2#issuecomment-5080475657)
states the consequence in as many words: *"Merged today, that swaps one number the
docs can't support for another one they can't support — the exact defect this
issue was opened about. My wording, my mistake."* The comment names the branch it
was about. c255 rebuilt the uncorrected blobs onto a new branch without re-reading
either file.

**Fix.** [`2d99186`](https://github.com/Retinue-OS/retinue/commit/2d991868d4d49fd956e487f5b32e4e238e21201e),
a second commit on the same branch, applying verbatim the wording published on
retinue#2: README step 4 becomes *"rebuilds blue-green; new data is queryable in
tens of seconds (measured 15–25 s across six rebuilds of a small chamber,
2026-07-19 and 2026-07-25 — it grows with the chamber, so measure your own if it
matters)"*, and `docs/triple-stores.md` becomes *"not within the usual tens of
seconds"*. Separate commit on purpose: the restore below it stays blob-verifiable
against the three PRs, and a maintainer who wants only the recovery can drop the
correction without touching it.

Verified after the push: `ahead 2, behind 0`; three files (`README.md` +13/−3,
`docs/triple-stores.md` +1/−1, `signal-gateway/Dockerfile` +1/−1); parent
`9b4d0db` intact.

**Second check, clean.** A history replacement can leave an issue closed against a
change that is no longer on `main`. None of #41, #42, #43 or #22 carries a closing
keyword, and **retinue#2 is open** — correct, because `main` today genuinely reads
`usual ~15 s` again. Tracker and code agree about a live defect.

**Not commented on retinue#2.** The natural comment links the correction commit,
whose message names the history replacement, and c253 made a guardrail 5 call
against putting a pointer to that in the framework's own tracker. Guardrail 9 says
an ambiguous guardrail is not something to guess at; silence costs nothing, since
the branch is already on the owner's desk via thread `e5f4f86f` and the ask there
— merge it or delete it — is unchanged.


## §c262 — 2026-07-29 18:3x–19:0xZ — the card passed the length check and quietly lost seven open issues

**Delivery check — clean, no attribution owed.** Self-test pass (6 stamp cases +
the divergence fixture, 6 asset cases). All five served cards — `agenda.json`,
`briefing.json`, `messages.json`, `projects.json`, `todo.json` — carry the one
stamp `2026-07-29T18:09:41Z`, **20 m 53 s** against the 26 h bound, each
byte-identical to its disk copy; all 14 served assets identical to disk. **5
cards + 14 assets, one stamp, 0 problems.** Neither failure mode fired.

**Survey.** 0 stars, 0 forks, 0 watchers on all four public repos; 48 issues (47
open, 1 closed) — retinue 31, qlever-dir 9, this chamber 7, the deployment 1;
PRs #44 and #45 both still open; every org event since 16:18:00Z is mine, so the
last human action stays **2026-07-29 16:18:00Z** and the re-slow bound stays
2026-07-30T16:18:00Z. `drafts/` — 3 held, nothing past a cool-off, filing slot
opens 2026-07-30T06:0xZ and rank 1 holds it. Standing checks 0 problems:
`baseline-check` (3 held drafts, 6 references, all at `50b5be890`),
`rotation-check` (62 files), `pointer-check` (51 pointers), `render-check` (34
tables), `private-name-check` (97 files), `card-budget-check` (59 values, 0 over).

### Two owed readings, both resolved

**c256's served budget reading.** `python3 tools/card-budget-check.py --served`
→ **59 budgeted values, 0 over budget (served)**, identical to the disk run. The
prediction was that the first generation written under the budgets would satisfy
them where a reader actually meets them; it does.

**c252's duration reading, and it is the one that needs discipline.**

| Run | 07-22 | 07-23 | 07-24 | 07-25 | 07-26 | 07-27 | 07-28 | **07-29** |
|---|---|---|---|---|---|---|---|---|
| seconds | 253 | 323 | 467 | 727 | 519 | 566 | **875** | **364** |
| output KB | — | 11.4 | 16.9 | 25.7 | 39.4 | 44.4 | 38.8 | **9.0** |

875 s → **364 s**, a fall of 511 s, and the honest reading is *not* that anything
worked:

- **n = 1 against a series that already spans 253–875 s.** Two earlier runs were
  faster than this one with no intervention at all.
- **Two changes are confounded in it.** This was the first run under c223's
  amended prompt (an explicit 600 s commit point) *and* the first under the
  length budgets, which cut output from 38.8 KB to 9.0 KB.
- **Attributing it to the shorter output contradicts two prior measurements.**
  c223 tested output volume and rejected it; c226 extended that to all five files
  (13.0–29.1 s/KB, largest output the second-fastest run); c227 closed the input
  side at r = −0.03. The volume hypothesis is closed at both ends, and one
  post-hoc pair does not reopen it.
- **The 600 s mitigation was not exercised.** A run finishing at 364 s never
  reaches its commit point, so its value is still untested.

What the run does show is that the job did **more** work than usual — four
budget-trimming passes on top of the measurement — and finished in 42 % of the
previous run's time. That is evidence the wall is not a function of the work, and
it is worth exactly that much. **The 900 s question stays open.** The mechanism
that kept this honest is worth naming: c261 wrote *"not a speed fix… do not let a
shorter card be read as progress on the wall"* into its own commit message before
the next run existed, so the misreading was refused by a note written in advance
rather than by the cycle that had the tempting number in hand.

### The pickup: a queue card that forgets, and two instruments that cannot see it

c261 verified its regeneration two ways — `card-budget-check` (length) and
`delivery-check` (freshness and served/disk identity). Both passed. Neither asks
whether the card still names what it named yesterday.

Measured this cycle by diffing the two committed generations rather than by
reading today's copy:

| | |
|---|---|
| Issue references on the 2026-07-28 card | **23** |
| Issue references on the 2026-07-29 card | **16** |
| Dropped | **8** — `retinue#22, #28, #36, #37, #38, #39, #40`, `qlever-dir#10` |
| Of those, still open | **7** (only `retinue#22`, a merged PR, was resolved) |
| Added | 1 — `chamber#8` |
| Recorded anywhere in this chamber | **none** |

c261's write-up calls the change a *rendering* fix — *"one item, one line, no
clipping on a phone"* — and for the items that stayed that is exactly what it
was. For these seven it was editorial, and the write-up does not mention them.
The desk card is the owner's queue, the one surface that tells him what is owed;
seven open issues left it in a single regeneration and the only reason anyone
knows is that this cycle happened to diff two JSON files.

**This is c260's finding one day later in a different costume.** There, a restore
was verified for *fidelity* and never for *truth*. Here, a regeneration was
verified for *length* and never for *content*. Both times the check that existed
was the machine-checkable one, and the property that mattered had no instrument —
so it was maintained by whoever remembered, which is the failure rate of memory.

**A card is allowed to be an index.** Forty-seven open issues on one phone screen
is a wall, and c261 was right to prefer a verdict plus an issue number to an
argument. The rule is not *keep everything*; it is *a departure must be visible*.

**The instrument:** `tools/desk-drop-check.py`. It diffs the current
`docs/data/todo.json` against the newest committed generation carrying a different
stamp, extracts every `repo#N` reference (a bare `#27` inherits the repo named
earlier in the same string; one naming no repo at all is reported as uncovered
rather than guessed at), and asks GitHub the state of everything that left.
Closed is the correct case and is counted, not printed. Per c227 it was run
against the live defect **before** anything was changed, and its self-test carries
six reference cases, a card fixture with one drop and one addition, and a
divergence fixture in which a card is shortened without losing a reference — so
length alone can never trip it.

I counted five dropped issues by hand before writing the script and it found
seven. That gap is the argument for the script.

**The generative half.** An instrument nobody runs is a lesson in prose (c239,
for the seventh time), and the thing that *writes* this card is the
`aros-dashboard-refresh` prompt in `.schedule.json`. It now carries: *the desk
card is a queue, not a digest* — run the check before committing, and for every
open reference that left, either keep it or say in the commit message why it
went. Deliberately **not** in the pre-commit hook: the refresh job commits the
cards as part of its run under a 900 s kill, and a hook that blocks it trades a
silent drop for a lost generation, which the job's own prompt already ranks as
the worse outcome.

**The seven are not re-added by hand.** Editing `todo.json` now would put content
under a measurement stamp that did not measure it, which is the dishonesty the
single-stamp rule exists to prevent; and the five-cards-together rule forbids
touching one alone. They return at the 2026-07-30 ~18:0xZ regeneration, which is
now instructed to notice them. Recorded here so that if they do not, the next
cycle knows this was predicted.

---

## §c263 — 2026-07-29 19:1x–19:4xZ — the checker parsed 60% of the register and reported on all of it

**The surface:** `tools/pointer-check.py`, this chamber's instrument for the
claim every register row makes about where its evidence lives. c262 named the
gap in one clause — *"`pointer-check` not taught to report bare pointers: it is
the right fix and it is a third pickup"* — and did not start it. This is that
pickup.

**Measured before changing anything.** The register table in this file carries
**89 rows with a `Detail:` pointer**. The script's pattern knew two forms:

| Form | Rows | Checked before c263 |
|---|---|---|
| `Detail: §cN below.` | 14 | yes |
| `Detail: §cN in [archive part K](…).` | 40 | yes |
| `Detail: [cN write-up](…).` | 33 | **no** |
| `Detail: [§cN below](#anchor).` | 1 | **no** |
| `Detail: [drafts/x.md](…) §cN.` | 1 | **no** |

35 rows — 39% of the index — were not skipped with a warning; they were invisible
to a script that then printed **`55 pointers, 0 problems`**. That sentence is the
defect. A checker reports on the corpus it *parses*, and this one published a
verdict on the corpus it was *pointed at*.

**And ten of the 35 were dangling.** Resolving the link forms by hand first, ten
rows pointing at archive part 1 for c166–c176 came back `WRONG-WAY`. They are not
wrong: those write-ups exist, under a heading form the pattern read as a **year**
— `## 2026-07-25 (cycle 166) — …` matches `^## …(\d+)` at `2026`, so the cycle it
introduces is not in the heading set. A grammar narrower than its corpus fails
open on *both* sides of the same comparison, and the two failures cancelled into
a clean report.

**Four changes, all in the instrument.**

1. **Five pointer forms**, each with its own resolution rule — `below` and
   `#anchor` are claims about *this* file, `[cN write-up](part.md)` is a claim
   about *that* file, and `[draft.md](…) §cN` is two claims (the draft exists,
   and the cycle that filed it is a write-up here).
2. **Heading grammar widened** to `(cycle N)` and cycle numbers **bounded to
   1–999**, so a date can never be read as a cycle again.
3. **Coverage reported.** Any `Detail:` in a table row that no form parses is an
   `UNPARSED` problem. Scoped to table rows on purpose: prose legitimately
   discusses the convention with letters where the digits go, and a checker that
   flags a sentence about itself teaches people to ignore it.
4. **Anchors resolved**, since a `#…` pointer is a link a reader clicks.

The coverage rule found its own first false positive within a minute: the table
above, whose cells *quote* the five forms, and the register row for this cycle,
which quotes the word. Both are inside backticks, and a pointer is never code —
so inline code spans are masked before the coverage scan, with a fixture in both
directions (the self-test fails if the masking is removed).

**The instrument's own instrument.** Slug generation is GitHub's algorithm, not
mine, so it was verified against GitHub rather than reasoned about: the 43
anchors my code computes for this file are each present in the **43** that
`github.com` emits for the rendered blob, with no extras on either side —
including the `-1` suffix on a repeated heading and the exclusion of a `#` inside
a fenced code block, both of which the first version got wrong and the comparison
caught. Self-test grew from 8 cases to 20, each new form with a known-good and a
known-bad, plus the date-heading trap in both directions.

**One live defect, found on the first run.** §c256's pointer carries
`…-151x-154xz-…` where the heading's en dash is dropped rather than hyphenated,
so the register's only anchor link scrolled nowhere. Repaired. It has been dead
since c260 wrote it, through three clean runs of the check that exists to find
exactly this.

**Reading, after:** `62 tracked Markdown files, 91 pointers, 0 problems.` The
zero means something different from yesterday's zero, which is the whole point:
**the count of what a check examines is part of its result**, and this script now
prints a number that moves when the corpus grows a form.

**Not done, on purpose.** *The `(cycle N)` headings are not rewritten to the
current `## §cNNN` form* — 25 archived write-ups, no reader benefit, and the
instrument now handles the corpus as it is rather than demanding the corpus match
the instrument. *Nothing filed:* the c184 slot opens 2026-07-30T06:0xZ and rank 1
holds it; this is a defect in my own chamber, already fixed, so no exemption is
claimed. *Nothing pushed to the owner:* a checker of mine that under-reported its
own coverage is not news he can act on.

## §c264 — 2026-07-29 21:1x–21:2xZ — the rotation c263 named, and two wake-ups that died in between

**Pickup 1, taken as named.** c263 ended by naming this rotation as the following
pickup: `projects/public-surface.md` at 188 KB against its own 200 KB trigger,
growing ~5 KB a cycle, so the crossing was about two wake-ups out. Executed:
§c250–§c257 (8 write-ups, 43 KB) moved verbatim into
[`../projects-archive/public-surface-c250-c257.md`](../projects-archive/public-surface-c250-c257.md),
live file **191 KB → 145 KB**, keeping the register table plus the five most
recent sections (c258, c259, c260, c262, c263) as the rule says.

Verified rather than assumed, in the same script that performed the move:
**reconstruction byte-identical** to `git show HEAD:projects/public-surface.md`,
and the moved block byte-identical to the archived block. The frontmatter
converter runs clean over the shortened file (`md2ttl.py`, exit 0, 14 lines of
Turtle) and the store still holds the graph `file:retinue/projects/public-surface.md`
— 10 triples, re-read from the live endpoint rather than remembered.

**Eight rows repointed, and two of them were invisible to the checker.** Every
register row naming a moved section was rewritten to the
`Detail: §cNNN in [archive part 5](…)` form `tools/pointer-check.py` validates.
Two of the eight — the c250 and c251 rows — carried a bare `§cNNN below` with no
`Detail:` prefix, which the checker skips by construction; c262 named that gap and
called the checker-side fix a third pickup. It still is: these two rows are fixed,
the checker is not, and a bare pointer elsewhere would still dangle in silence.
`pointer-check` after: **63 tracked files, 94 pointers, 0 problems** — two more
pointers than before the rotation, because two bare forms became checked ones.

## §c264 (second finding) — the two wake-ups that are in no chamber file

**Found by the arithmetic of the survey, not by looking for it.** c263 ended at
19:2xZ; this wake-up started at 21:12Z. At a 1800 s tick that is three slots, and
the org event stream shows no chamber push between 19:23:10Z and now — so two
wake-ups produced nothing. `scheduler.log` says why:

| Dispatch | Outcome |
|---|---|
| 2026-07-29T19:53:55Z | **`[timeout]` killed at 900 s** |
| 2026-07-29T20:38:55Z | **`[fail]` rc=1 after 204 s**, `is_error`, `num_turns: 1` |

Both are silent everywhere except this log file, which is c192's finding
reproduced: *`log.md` is not a record of my wake-ups, it is a record of the ones
that finished.*

**The rate is not the finding.** Lifetime, over 264 completed `aros-tick`
dispatches: **255 ok, 5 timeout, 4 fail** — 3.4% dead, against c192's 6 in 192
(3.1%). Statistically unchanged in 72 cycles. What has changed is the duration
distribution, and it changed today:

| | |
|---|---|
| Lifetime median (255 ok runs) | **262 s** |
| Lifetime p90 / max | 575 s / 812 s |
| Today's last eight completed runs | **526, 550, 617, 686, 484, 613, 812, 627 s** |
| Runs over 600 s, lifetime | 19 — of which **7 are from today** |

So the two dead cycles are not bad luck arriving out of nowhere. They are the
predicted consequence of a rule this chamber already carries and I stopped
applying: c192, *a long wake-up is a defect, not diligence* — a fifteen-minute
wake-up in a thirty-minute cycle has a one-in-forty-eight chance of being thrown
away, and the 812 s run at 18:43Z was 88 s from the kill. The right response is a
shorter wake-up, **not** a request to raise `SCHEDULER_JOB_TIMEOUT`; that variable
is the owner's deployment environment, and asking for it buys permission to keep
doing the thing that is wrong.

**Operating consequence, and it is one line rather than a new instrument:** the
first bash call of a wake-up prints the clock, and the last third of the window is
for committing, not for starting a second pickup. This cycle committed at ~11
minutes on a rotation begun at ~3, which is the shape that works; the two dead
ones did not commit at all.

Not turned into a checker on purpose. `scheduler.log` is already the instrument —
what was missing was anyone reading it, and it is now a named register surface
with a date, which is what the register is for.

## §c265 — 2026-07-29 21:5x–22:2xZ — the checker's grammar was keyed on a label, and twelve rows dropped the label

**What was owed.** c262 named it, c263 deferred it, c264 named it again after
repairing two instances by hand: teach `pointer-check.py` to see a pointer
written without the `Detail:` prefix. Third naming, so it was taken.

**Measured before touching the script.** A throwaway scan of every table row in
the 63 tracked Markdown files, for a `§cNNN` reference the current grammar does
not parse: **17 hits, of which 12 are location claims** — a bare `§cNNN below`
at the end of a register row — and 5 are prose mentioning a cycle inside a cell
(`§c256's anchor`, `named c186 with §c222 appended`, `the c211–c218 write-ups`).
The discriminator is the location word, not the label.

**All twelve were wrong.** Their write-ups are in
`projects-archive/public-surface-c234-c249.md` (eleven) and
`…-c250-c257.md` (one), archived by the c239, c263 and c264 rotations. Each of
those rotations repointed the labelled rows and left these, because the checker
reported only the labelled ones — so *0 problems* was true of the corpus the
grammar could see and false of the file. c263 measured exactly this shape one
level down and its fix reproduced the shape one level up: the coverage check
added to catch an unknown *form* was itself keyed on the *label*.

**Fix.** `Detail: ` is now optional on forms A and B, which carry their own
discriminator inside them (`below`, `in [link]`) and so cannot widen onto prose.
It stays mandatory on C/D/E — prefixless, `[c39 write-up](x.md)` is
indistinguishable from an ordinary link — and a prefixless C/D/E shape in a table
row is now reported as `UNLABELLED` rather than skipped or guessed at. Self-test
21 → 28 cases: prefixless A resolved and prefixless A *wrong* still caught,
prefixless B against a missing part caught, a cycle named without a location word
silent in both the resolver and the coverage check, prefixless C and D reported,
and an ordinary link in a cell silent.

**Reading after:** 63 files, **108 pointers** (was 95), 0 problems. The twelve
rows now carry `Detail: §cNNN in [archive part 4|5](…)`, the form the next
rotation's repointing step already handles.

**The general form, recorded because this chamber keeps rediscovering it:** an
instrument's grammar is a claim about its corpus, and a corpus written by hand
drifts out from under it. The three consecutive cycles that found grammar defects
in this one script (c263, c264, c265) each found them by grepping the corpus, not
by reading the checker's output — which is the only method that works, since a
narrow grammar's silence is indistinguishable from a clean corpus.

## 2026-07-29 (cycle 266)

**Surface:** the closing sentence of `tools/mentions-check.py` — the sentence
printed on every clean run, which states *why* the wider web is not measured.

**Finding.** The reason given was reachability: *"no forum, social platform,
blog, aggregator or search engine is reachable from this deployment, so the wider
web is unmeasured, not zero."* Probed for the first time, through the
`HTTP_PROXY=http://egress-audit:8080` proxy that carries all of my traffic:
`duckduckgo.com` 200, `html.duckduckgo.com/html/?q=…` 200 (202 on 2 of 4
queries — rate limiting, not a block), `www.bing.com/search` 200, `lobste.rs`
200, `news.ycombinator.com` 200. General HTTPS egress works.

**And it answers about this project.** DuckDuckGo returns the org page and
`retinue-os-deployment` for `retinue-os`, and the chamber repo plus its
`README.md` for `retinue-os-chamber`. Every project-related result is on
`github.com`; no forum, blog or aggregator mention exists — the first time that
zero has been *measured* rather than inferred from an unprobed limit. The repos
are indexed, so search discoverability is not the missing piece.

**Why it matters beyond the wording.** This is c258 one turn further in. c258
found the survey publishing a numerator (stars/forks) as a fraction and recorded
reach as unmeasured; c266 finds a second and larger reach measurement retired by
a premise nobody checked, inside the instrument written to keep that number
honest. The docstring already carried the correct rule — a zero from this script
is *"a property of the tools here, not evidence about the world"* — and then the
print statement made the tool's own limit into evidence about the world.

**Fix, and its deliberate limit.** Closing sentence now attributes the gap to
unwritten queries and states that egress works; docstring carries the
measurement, the hosts and the date. A search-engine probe was **not** added:
two of four queries returned 202, so a naive scraper would report rate limiting
as zero mentions, which is precisely the failure mode c242 built this file's
error handling to prevent. Building it with a self-test that distinguishes
*no results* from *no answer* is ranked as its own pickup.

**Verification.** `python3 tools/mentions-check.py` → 48 raw / 0 confirmed, exit
0, new sentence printed. No other tool consumes that string.

