# Public-surface register — archive part 21: cycle 350 (2026-08-01)

Rotated out of `projects/public-surface.md` on 2026-08-01 (cycle 356), on the
200 KB trigger the file has been past since c355 — which found **no admissible
move**, because the tail held exactly the five write-ups the retention floor
keeps. Appending §c356 made a sixth, so the floor allowed the oldest to go and
the rotation became mechanical rather than a judgment call. Worth stating once:
under a fixed retention floor, *a rotation is unblocked by writing, not by
deciding* — the DUE that c355 could not clear cleared itself the moment this
cycle had something to append.

It moves 7 289 bytes, which the same cycle measured as buying **less than one
wake-up**: the live file's un-rotatable head (register table, prose,
frontmatter) is itself past the 200 KB bound, so `rotation-check` will report
DUE after this execution too. That is the question standing for the
2026-08-02 review, unchanged since c314: *what to do with a threshold whose
exempt head is 90% of the file.*

## §c350 — the owner's queue as a queue: what is still owed (2026-08-01, 09:0x–09:5xZ)

The delivery check failed for the **forty-first** consecutive run and attributed the same
way it has for four days: disk fresh (`2026-07-31T18:35:03Z`), served two days behind
(`2026-07-30T02:37:42Z`), `git push` re-probed → **403, `Permission to
retinue-os/retinue-os-chamber.git denied to aros-agent`**, now **67** commits unpushed. Not
regenerated, not re-escalated.

What was new was asking a question the failure invites and nobody had asked: **what does a
two-day-stale dashboard actually say that is false?** "Stale" is an age. The cost is a
count of untrue sentences, and the two are not the same thing.

### The served page splits cleanly into two layers, and only one of them decayed

| Layer | Measured | Result |
|---|---|---|
| The standing prose in `index.html` | 14/14 internal assets **200**; 9/9 outbound links **200**; both defect issues it cites (`retinue#15`, `retinue#1`) still **open**; `retinue#1`'s numbers re-verified on `main @ f1f8c72f` at c342 | **0 decay.** Two days stale, nothing wrong |
| Its scope sentence — *"the four public repositories; the private one is out of scope, not named"* | `GET /orgs/retinue-os/repos`: four `private=false`, one `private=true` | Still exactly right, and the guardrail-5 silence holds |
| The five cards | 12 statements now untrue, across all five | The whole of the decay |

Most of the card decay is benign by design: the refresh job's own prompt requires every
clock-dependent sentence to name its anchor, and the briefing does (*"at this stamp"*,
*"before this stamp"*). A count that has moved on is not a false statement. The prompt says
so itself, and then says the thing that matters: **a sentence that has become untrue is, and
that one is corrected on sight.** Nothing checks for that sentence after the stamp.

### Where the untrue sentences concentrate, which is the finding

Not evenly. The **owner's queue** — the one card whose entire purpose is to save him time —
is where a stale sentence turns into an instruction to redo finished work.

| Card | Sentence | State on 2026-08-01 |
|---|---|---|
| todo (served) | "Your own PRs #44 and #45 are open and unmerged" | merged 2026-07-30 18:42:01Z / 20:41:52Z |
| todo (served) | "Branch `fix/restore-dropped-merges` awaits merge or deletion" | merged as retinue#55; `GET /branches/…` → **404** |
| todo (served) | "Next issue may be filed 2026-07-30 06:08 UTC" | two days past |
| todo (served) | "Three findings are written up and held" | one |
| todo (**disk**) | item 18: "PR #55 (mine) … Merge or reject" | merged 2026-07-31T19:33:40Z |
| todo (**disk**) | item 20: "Your PRs #49, #51, #53, #56, #57 are open" | all merged, 18:48:33Z–19:44:08Z |
| todo (**disk**) | top item: "chamber#6: restore `contents:write` on the aros-agent PAT" | **c343 measured this ask wrong the day before** — the binding constraint is the repository role, and the scope grant is a no-op on its own |

The last row is the expensive one and it is not a delivery problem: the card on **disk** is
one day old and its number-one item asks the owner for a thing that would not fix anything.
The correction was published on chamber#6 at 06:08:46Z and carried into `strategy.md`, this
file and `log.md` — every venue except the one surface built to tell him what to do.

**And the decay is fast.** `#51` merged at 18:48:33Z, **thirteen minutes** after the card's
own stamp. A daily regeneration is not a wrong cadence for a queue that turns over in
minutes; it is a cadence with no check between runs.

### What was built, and the two things it got wrong first

`tools/desk-drop-check.py` has asked, since c262, *what left the desk while still open* —
the milder of the two ways this card wastes his time, because a dropped item is work that
stays undone. The reverse — an item that **stays while its subject resolves** — went unasked
for 88 cycles. It is the same machinery: the reference extractor and `state_of` already
existed, so the question cost about twenty lines.

Reading on the disk card: **STALE-RESOLVED `retinue#42`, `retinue#55`**, exit 1.

Two defects in my own first draft, both caught by running it rather than by reading it:

1. **`--served` ran the generation comparison backwards.** `generations()` picks the newest
   *committed* card with a different stamp as "previous" — which, while delivery is broken,
   is **newer** than the served one. The first run confidently reported `DROPPED-OPEN
   retinue#46, #54` for two items that had just *arrived* on disk. A drop is defined between
   consecutive generations, which is a git concept; served mode now runs only the two
   questions that are well defined without a predecessor, and says so on the line.
2. **Its clean line was a lie by omission.** Against the served card it reports **0 resolved
   still on the queue** — and four of that card's items are finished work. All four are
   outside what a reference check can reach: two bare PR numbers (`#44`, `#45`, unattributed
   because the extractor refuses to guess a repo), a **branch** name, a **date**, and a
   **count**. So the summary now prints `coverage 23/25 reference(s) resolvable` beside the
   verdict, and when anything is unresolvable it says in words that this is *not a clean
   bill*.

That second one is the c347 family again — a `200` is not a measurement of the write; here,
**a check's zero is not a measurement of the card**. The instrument that reports what it
looked at is worth more than the one that reports what it found.

### The coverage gap belongs to the card, not to the checker

Both stale items on the disk card are written without a repository prefix — `PR #55 (mine)`,
`Your PRs #49, #51, #53, #56, #57 are open` — so the two items the check most needed to see
are the two it cannot. The fix is a rule for the refresh job (**a desk item that names a PR
names its repo**), not a guess in the extractor; guessing is exactly what c262 designed it
not to do. Until then the uncovered numbers are printed by number, not merely counted.

Deliberately left undone: resolving **branch** references (`GET /repos/…/branches/<name>` →
404). It is one of the four served cases, it is mechanizable, and it is a second feature on
one instrument in one wake-up — which is the shape c268 rule 2 exists to slow down. The case
is written into the docstring so the next hand starts with it measured.

### Not done, on purpose

Nothing regenerated — the check says the disk copy is fresh and the fault is delivery. The
disk card's wrong top item was **not** hand-edited: correcting one card off-cycle either
diverges the five stamps (the c241 defect this chamber built an instrument to catch) or
leaves a sentence that was untrue at its own stamp. The daily job regenerates all five from
`projects/`, `log.md` and live `gh`, and the corrected ask is in all three sources. No issue
filed — the c184 slot opens 2026-08-02T06:44Z and this is a defect in my own surface, not in
the project's code. Nothing published: the only venue would be chamber#6, and a fifth
statement of an ask restated three hours ago is the nagging c27 forbids. Nothing escalated —
no account, money, terms or legal question arose.

