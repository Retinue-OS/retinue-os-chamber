# Public-surface register — archive part 19: cycles 336–343 (2026-08-01)

Rotated out of `projects/public-surface.md` on 2026-08-01 (cycle 351), on the
200 KB trigger that file's own rotation rule sets. The write-ups move and the
register table stays — the c216 split, because the index is the thing a reader
needs whole.

Worth recording where the next rotation will read it: this one moved 8.4 KB and
took the live file from 200 KB to 191 KB, because **164 KB of it is the register
table, which does not rotate**. The rule can buy about one wake-up at a time now,
and c314 already measured the head crossing 200 KB on its own between 08-02 and
08-04. That is a question for the 2026-08-02 review, not something a rotation
can answer.

Nothing here is edited, reordered or deleted. Reconstruction was asserted
byte-identical against the pre-move file before anything was written, and the
section split is **fence-aware** (c343's rule, from the c320 near-miss).

The two register rows whose evidence lives here now point at this part rather
than at `below`; the repointing was done against the **masked** text, per c348.

---

## §c336 — the surface that was never in the register: branches other than `main` (2026-08-01, 00:0x–00:4xZ)

**The audit, in full, because it is small enough to state completely.** Four public repos in the
org (the fifth is private, so its branches are not a public surface and are out of scope here):

| Repo | Branches besides `main` | Compare against `main` |
|---|---|---|
| `qlever-dir` | none | — |
| `retinue-os-deployment` | none | — |
| `retinue` | `feat/chamber-secretary-style-override` | **0 ahead / 20 behind** — fully merged, an undeleted leftover of the #53 merge. Cosmetic |
| `retinue-os-chamber` | `claude/aros-issues-triage-goei5k` | **2 ahead / 170 behind, diverged** — `GUARDRAILS.md` and `SECURITY.md` |

**What was on it.** Two commits, both made by the owner's own Claude session on 2026-07-25 and
pushed at 16:34:31Z: `492793b` corrects `GUARDRAILS.md` §3 row 2, which currently instructs me to
say the project has **no CI running the tests** — false since 2026-07-19; and `6fb2bdd` adds a
`SECURITY.md` to this repository, which has none (`/community/profile` → `files.security: null`,
health 25%). Both issues they answer, #7 and #5, are **still open and still labelled
`owner-action`** — six and twelve days respectively — while the work sat finished on a branch.
**No pull request had ever been opened on this repository at all**; the one I opened is its first.

**Why this surface generated no signal, which is the reusable part.** Every survey I run asks the
same five questions of a repo — stars, forks, watchers, issues, PRs — and a branch is none of them.
`gh pr list` returns nothing for a branch with no PR, which is exactly the state that hides work.
The register's own premise is that an unchecked surface emits nothing to prompt checking it; this
one had the additional property that **the instrument I do run reports it as empty rather than as
unmeasured** — zero open PRs reads as "nothing pending", when what it meant was "nothing pending
*that anyone opened*."

**Verified before putting it in front of him, rather than after.** `GUARDRAILS.md` has not moved on
`main` since 2026-07-19 (`24cf883`) and `SECURITY.md` does not exist there, so both apply cleanly —
confirmed by the PR reporting `MERGEABLE` / `mergeStateStatus: CLEAN`, +16/−1 over 2 files. The CI
fact the row turns on still holds: `tests.yml` runs on push to `main` and on every PR, five most
recent runs green, latest 2026-07-31T19:44:10Z. The `SECURITY.md` text is robust to a setting I
cannot read — it branches on whether the Security tab offers private vulnerability reporting rather
than asserting which — and its deferral of framework reports matches `retinue/SECURITY.md`, which
exists and describes the same process.

**The part that is against my own interest, stated because leaving it out would be the violation.**
The `GUARDRAILS.md` row this branch lands is *still* imprecise, and I am the one who found that:
six minutes after the branch was pushed I commented on #7 that "security-critical paths are
untested" is broader than the evidence and "on every push and PR" is broader than the trigger, and
proposed a better row. **That comment is why nothing merged for six days.** It gave him a reason to
wait and no reason to act, and the thing it left standing on `main` is a flatly false sentence
rather than a merely imprecise one. Recommending the merge *and* saying the row is imperfect is not
a hedge — it is the ranking: an imprecise claim in the safe direction beats a false one, and the
better row is a one-line follow-up either way.

**Rule this adds, and it is not about branches.** *A checker that reports zero should say whether it
measured zero or measured nothing.* `gh pr list → 0` and `gh api notifications → 403` are both
reported in my survey lines, and only the second is honestly labelled as a gap. The first meant
"unmeasured" for thirteen days and read as "clean". Same family as c335's note that a 403 on
notifications is a gap and not a zero — but that one I had already learned on the instrument that
errors, and missed on the instrument that succeeds.

**Reference discipline, caught in my own PR body before it shipped.** The body first wrote the
framework's `#57` bare, inside a pull request that lives in *this* repository — where a bare `#N`
resolves here. That is c332's defect with the repos swapped: c332 found bare `#54`/`#55` in a
`chamber#`-prefixed card line resolving to this repo and 404ing. Qualified as
`retinue-os/retinue#57`, with one sentence in the body stating the convention it uses. In the other
direction the same edit was a gain: writing #7 and #5 bare rather than as `chamber#7`/`chamber#5`
is what put PR #9 into both issues' timelines, which is how he finds it from his desk.

## §c343 — the ask, which nothing in this chamber ever re-derives (2026-08-01, 04:4x–05:2xZ)

The register tracks **surfaces** and `baseline-check` tracks **held findings**. Nothing tracks the
**ask** inside an `owner-action` issue — the one paragraph the owner would act on. chamber#6 has
carried the same ask since 2026-07-31, restated in three comments: `Contents: read and write` on the
`aros-agent` token. Re-derived from a measurement for the first time this cycle, it is wrong, and
acting on it as written would have changed nothing.

### The discriminator, and it costs four calls

Two pairs. Within each pair, both endpoints declare the **same** required token permission in
GitHub's own `x-accepted-github-permissions` header, against the same repository, seconds apart:

| Call | Declared | Result |
|---|---|---|
| `GET /repos/Retinue-OS/retinue` | `metadata=read` | **200** |
| `GET /repos/Retinue-OS/retinue/collaborators` | `metadata=read` | **403** |
| `PATCH /repos/Retinue-OS/retinue/issues/54` (mine, no-op title) | `issues=write; pull_requests=write` | **200** |
| `POST /repos/Retinue-OS/retinue/issues/54/labels` (same issue) | `issues=write; pull_requests=write` | **403** |

Pair 1 reproduces identically on `retinue-os-chamber`. A token permission cannot be present and
absent on one repository in one second, so **none of these 403s is about the token's permission
set.** What pair 1's failing endpoint requires and its succeeding one does not is documented:
*"The authenticated user must have write, maintain, or admin privileges on the repository"*. Pair 2
is corroboration rather than a second citation — the labels page states no role requirement — and
shows the same shape observed: the call with an author path succeeds, the call without one does not.

**The binding constraint is the `aros-agent` account's repository role, and it is below Write.** A
fine-grained PAT can never exceed what the account itself may do.

### The lesson, which is the expensive part

GitHub returns `Resource not accessible by personal access token` for **role** denials as well as
scope denials. Every 403 recorded in this chamber carries that string, and every cycle since
2026-07-19 read it as a diagnosis. It is a label. *An error message that names a cause is not a
measurement of that cause* — the c19/c310/c342 shape, one layer down: an **inherited** 403 is not a
measurement, and now, a **self-measured** 403 is not a measurement of *why* either.

### What was published, and what was deliberately not

Published: one comment on [chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6#issuecomment-5149872274),
carrying the corrected two-step ask (role first, then scope — the role denial *masks* the scope, so
the scope stays in the ask rather than being dropped from it) and a one-command verification I
promised to report either way. c342 judged a further chamber#6 comment to be nagging and was right
about the class it had: a ninth *consequence* adds nothing. A correction that changes what he would
do is not that class, and holding it would have been the more expensive silence.

Not published: no new issue (the c184 slot is shut until 06:26:15Z, and this belongs on the existing
tracker regardless), no dashboard push (ten threads unread; one venue per thing), nothing about the
private finding routed at c340.

### Proposal for the 2026-08-02 review

Give `owner-action` asks an expiry, the way `baseline-check` gives held drafts one. The candidate
rule is cheap and needs no new instrument: **before treating a tracked blocker as covered, re-derive
its ask from a live measurement rather than re-reading it.** The existing no-re-escalation rule
already requires verifying that the *tracker* exists (c19); it has never required verifying that
what the tracker *asks for* is still the right thing.
