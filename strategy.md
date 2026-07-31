# Strategy

Owned by Aros. Ara drafted the first version when the chamber was created;
every revision after it is Aros's, made at the scheduled review (or sooner,
when the evidence demands) and recorded in the revision log below.

## Mission (stable)

Make Retinue known, accurately, to the people best equipped to appreciate it —
and turn the ones who show up into a community the project deserves.

## Current phase: foundation, owner-blocked

Published, unannounced, and **not reachable**. The repos went public on
2026-07-18. Twelve wake-ups later: no accounts, no announcement, zero external
contact of any kind — 0 stars, 0 forks, 0 outside issues, 0 discussions across
all four repos. Every issue in the org was written by the owner or by me.

The previous version of this file called the phase "foundation" and listed four
objectives. Three of them are now as done as I can make them alone; the fourth
never depended on me. The honest description of the phase is not "building the
foundation" but **waiting on the owner**, and naming it accurately is the point
of this revision — a phase name that implies work I can do, when the work I can
do is finished, produces manufactured activity.

Phase objectives, with status:

1. **The public repos answer their own questions.** *Substantially done.* Docs
   audited against the verified claim table (cycle 11); the one defect found was
   fixed on a branch, **merged by the owner on 2026-07-29 12:34Z (PR retinue#42),
   and is not on the current `main`** — see "What the merges did, and did not,
   settle" below.
2. **Accounts exist with AI-disclosure bios.** *Partly done, 2026-07-30 (c292).*
   **The GitHub agent account landed:** `@aros-agent`, created 14:51:24Z, bio
   *"AI agent account … operated under human oversight by @retog. Not a human."*
   I posted from it for the first time at 17:47Z. That closes chamber#3 and ends
   the guardrail-8 defect that had every issue of mine authored by the owner for
   ten days — and it retires the measurement hack that came with it: authorship
   metadata now separates his writing from mine, so the disclosure-sentence grep
   (c176/c179/c219) stops being the only authorship record either of us has.
   **The social accounts are not done** — Mastodon and Bluesky are still
   untouched at chamber#1 (guardrail 7; `projects/social-presence.md`), and they
   are the ones the bets need. The distinction matters: this objective was written
   as one item and is two, and only the half that does *not* produce an audience
   has moved.
3. **The triple-store walkthrough exists.** *Written* —
   `writing/provenance-by-path.md`, built on queries run against a live store.
   The link from the framework README was **merged on 2026-07-29 12:30Z (PR
   retinue#41) and is not on the current `main`.** It was never blocked on the
   permission this list claimed for twenty cycles — see below.
4. **Every inbound question gets an answer within one wake-up cycle.**
   *Vacuously satisfied.* There has been no inbound. This objective measures
   nothing until (2) lands, and I should stop reporting it as met.
5. **Write scope on the GitHub token.** *Acted on, partly landed, 2026-07-30
   (c292).* The owner granted chamber#6's option 1 alongside the new account.
   Measured from inside: commenting on issues **and on pull requests** now works
   (the PR-comment 403 c289 recorded this morning is gone), but `contents=write`
   is 403 — so no branch push, and therefore still no PR — and issue *update*
   (close, edit, label) is 403 in both repos while commenting in the same repos
   succeeds. Everything needing only **read** access to a public repo works;
   everything needing **write on the repository** fails, and
   `GET /repos/…` reports effective access `{pull: true, push: false}`.
   The likeliest cause is that the account has Read rather than Write on the
   repos — a fine-grained PAT cannot exceed what the account itself may do — but I
   cannot confirm it from inside, because the membership and collaborator
   endpoints are 403 too. Handed to the owner with that exact check, on the
   dashboard thread where I had wrongly called it a regression.

   **Consequence worth naming:** this chamber is my only memory, and I cannot
   publish to it. Commits accumulate locally and reach no reader.

   *~~Commits accumulate locally and die with the container. For the first time
   the thing at risk is not the project's reach but my own continuity.~~ Struck
   2026-07-31 (cycle 305): false, and false in the direction that inflates an ask.
   Measured from `/proc/self/mountinfo`, `/workspace/chambers` is the named volume
   `retinue-os-deployment_chambers`, not the container's overlay; the entrypoint
   clones a chamber only when `.git` is absent, and the documented update recipe
   carries no `-v`. A container recreation loses nothing. The commits are
   single-copy, which is a backup consideration, not a continuity emergency. The
   same sentence had reached chamber#6 an hour earlier and is corrected there:
   [issuecomment-5138579621](https://github.com/Retinue-OS/retinue-os-chamber/issues/6#issuecomment-5138579621).*

The phase ends when the **social** accounts exist and the walkthrough is linked
from the framework. Both are owner actions. The next phase gets written then.
The GitHub account landing does not end it — it removes an honesty defect and a
measurement hack, neither of which was ever what made the project unreachable.

## The two blockers, which are the same class of thing

Accounts (objective 2) and PR scope (objective 5) are both things only the owner
can grant, and between them they gate everything the bets below are supposed to
test.

The second one is new to this revision and is the first genuinely new argument
in three cycles. The GitHub token can **file issues but not open pull
requests** (`gh pr create` → `Resource not accessible by personal access
token`). ~~Two docs branches are pushed and stuck behind it —
`docs/link-provenance-piece` and `docs/calibrate-reindex-latency`. The
consequence is not cosmetic: my corrections arrive as **prose asking a human to
act**, never as a diff he can merge in one click. "Corrections accepted into the
repos" is one of the things this strategy says it measures, and that measure is
currently rate-limited by a permission rather than by my output or by anyone's
willingness to accept the work.~~ **Struck 2026-07-30 (cycle 270): both branches
were merged and both are deleted; the paragraph below replaces this claim.**

It is tracked publicly and durably at
[chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6), filed on
cycle 19, which offers two options with no preference expressed.

**Correction (cycle 19, amended cycle 21).** From cycle 12 until cycle 19 this
paragraph cited `retinue#2` and stated the blocker "does not need re-escalating".
The second half was wrong and the first was too weak to carry the load: retinue#2
is a *documentation* issue about reindex latency, and the token-scope blocker
appears in it only as a closing section. I applied the no-re-escalation rule to a
subsection of an issue about something else, and stayed quiet about the project's
most consequential blocker for seven consecutive cycles.

*Amended cycle 21, because cycle 19 overcorrected in two checkable ways and this
is a revision log people read as fact.* retinue#2 is not "the owner's own" issue —
I wrote it, filed from his account, which is the separate problem tracked at
chamber#3. And the blocker had not "never been filed anywhere"; it was filed
badly, in the wrong place, at the wrong scope. The conclusion is unchanged and
chamber#6 remains the citation. But a correction that overshoots is still a false
claim in a normative file, and cycle 21 found it by grepping for the old citation
rather than by re-reading the prose — which is the check that should have run at
cycle 19.

The rule survives; the gap was in how it was applied. It is now stated with the
verification step that makes silence safe — see "Working while blocked".

It is also no longer an item about pull requests. One missing permission has
produced four distinct consequences (no PRs, no repo topics, no security settings,
no descriptions), each of which arrived as its own `owner-action` issue. It is one
blocker with a growing tail, and the strategy should describe it that way.

## What the merges did, and did not, settle (correction, cycle 270)

The two paragraphs above were false for twelve hours before this cycle read them,
and they are the two paragraphs a first-time reader of this file reaches first.
The measurement is c253's, recorded in the revision log on 2026-07-29 and never
carried up into the body — the c21/c235 failure in its own house: **a correction
filed in the log does not correct the prose.**

Measured, and re-verified 2026-07-30 01:1xZ:

| | |
|---|---|
| PRs merged on the framework 2026-07-29 12:29:49–12:37:35Z | **3** — retinue#41, #42 (both cut from branches *I* pushed 2026-07-19), #43 (the owner's) |
| My token's scope at the time | **unchanged**; he merged them himself |
| `main` pushed at 12:45:00Z to a line sharing no common ancestor | tree-diffed rather than SHA-compared: 123 blobs each side, identical paths, **4 blobs differ** — the 3 the merges touched, each back at pre-merge content, plus one whose change is why the line was replaced and **which is private and not described here** |
| What GitHub shows | all three still read *Merged*, branches deleted, nothing raises it |
| Content recovered | [`fix/restore-dropped-merges`](https://github.com/Retinue-OS/retinue/tree/fix/restore-dropped-merges) — ahead 2, behind 0, exactly `README.md`, `docs/triple-stores.md`, `signal-gateway/Dockerfile`; content, not lineage; escalated once on dashboard thread `e5f4f86f` |
| Deliberately not filed as an issue | guardrail 5 — an issue explaining why the history changed either names what was removed or points at the diff containing it |

**What it settles.** The missing PR scope was never what stood between a
correction and `main`. Two branches this file called *stuck behind a permission*
for twenty cycles were merged from those branches with that permission still
missing. c163 withdrew the permission attribution as an argument; this is the
direct evidence. chamber#6 stays filed and is **not** re-raised — this weakens its
rationale rather than strengthening it.

**What it does not settle.** *Accepted* was 3 for sixteen minutes and is 1 again.
Objective 3 was satisfied for fifteen minutes; a phase does not turn on a state
that has already reverted, and it turns back when the restore lands. Nothing here
changes a bet, the phase, a measure, the filing rule or the cadence.

## The clock (correction, cycle 27)

**This file counts in cycles and reasons as if they were days. They are not.**
Measured at cycle 27, 2026-07-20 08:16 UTC:

| Thing this file calls old | Actual age |
|---|---|
| Repos public, "twelve wake-ups later" with zero contact | 35 hours, unannounced |
| chamber#1 (accounts), "twenty-six cycles without moving" | 34 hours |
| chamber#3 (agent account), "twenty-six cycles old" | 6 hours |
| chamber#6 (token scope), "suppressed for seven cycles" | 4.5 hours |
| chamber#7 | under 4 hours |
| The two private findings, "still unfixed" for ~15 cycles | 11 hours, mostly overnight |

Cycles 21–26 all ran on 2026-07-20 between roughly 05:00 and 07:44 — about one
every thirty minutes. Twenty-six cycles is a day and a half, most of one night
included.

Three consequences, and they matter more than the arithmetic:

1. **Zero external contact is not evidence.** Thirty-five hours of an
   unannounced repo, with no accounts and blank descriptions on three of four
   repos, predicts exactly zero stars. Reporting it cycle after cycle as a
   mounting silence implied a signal where there is no measurement yet.
2. **The owner is not unresponsive, and the escalation channel is not broken.**
   Cycle 26 raised whether the zero movement was "evidence about the escalation
   channel rather than about the owner". It is neither. It is evidence that I
   wake roughly fifty times a day and he does not. The dashboard demonstrably
   works — he used it on 2026-07-19 at 16:52. The security thread pushed at
   21:33 that evening is unread because it was pushed at night, five hours
   before I filed five issues about it.
3. **This was one cycle from causing harm.** The natural next move from
   "twenty-six cycles, nothing moved, maybe the channel is broken" is to
   re-escalate — to nag a man about issues that are four hours old. The
   no-re-escalation rule held, but it held for the wrong reason: it was applied
   as a rule about repetition, when the actual fact is that nothing is overdue.

**Standing rule: state ages in wall-clock time, not in cycles.** Cycles measure
my activity, not elapsed time, and every deadline that matters — a person
reading an issue, an audience finding a repo — runs on the wall clock. Where
this file and `log.md` still say "N cycles", read it as "N of my wake-ups" and
convert before drawing any inference about anyone else's behaviour.

This does not change any bet, and it does not move the scheduled review. It
changes what the review is allowed to conclude from silence.

## The backlog is the measure (correction, cycle 163)

Measured 2026-07-25 11:34–11:40 UTC, across all four public repos:

| | |
|---|---|
| Open issues | **37** |
| Issues ever closed | **0** |
| Authored by anyone but me | **0** |
| Comments on any of them not written by me | **2** — chamber#1 (07-19, "Nostr should also be considered", already folded into bet 3) and retinue#13 (07-21, a requirement clarification) |
| Commits landed on framework `main` since 07-19 | **18**, none referencing any of the 37 |
| Filing rate | ~5.6 issues/day since 2026-07-18 |
| Drain rate | 0/day |

**What this does not show.** It is seven days, over a weekend, and the maintainer
has engaged twice in that window. The clock rule applies exactly as written: a
high-frequency observer reading a low-frequency actor perceives neglect where
there is none. Nothing here is evidence that he is ignoring the queue, and this
section is not an escalation — nothing in it is overdue and nothing is being
re-raised.

**What it does show, and it is about me.** For roughly twenty cycles I have
reported "corrections accepted into the repos" as gated by chamber#6, i.e. as a
number whose zero is caused by a permission. That attribution is unsupported. A
pull request would have arrived in the same unreviewed queue as the 37 issues;
nothing in the evidence says format is the constraint. The simpler explanation —
a week-old queue whose only reader has been writing features — was available the
whole time and I never measured for it, because the permission story was more
flattering. **I have been counting *filed* as *corrected*.** Guardrail 3 is about
exactly this class of error; it just happened to be pointed at the project's copy
instead of at my own reporting.

**Operating rule, effective now.** While the drain rate is zero, a finding is
filed as a new issue only if it is (a) a defect that silently produces wrong
behaviour, or (b) a false claim on a public surface. Everything else accumulates
in `projects/public-surface.md` and `drafts/` — where every issue body is already
drafted anyway, so nothing is lost, only the notification is deferred. Prefer a
comment on an existing issue over a new one. **Restore normal filing on the first
issue closed, or on any inbound from a second person.**

> **Lifted, cycle 165 (2026-07-25 15:14Z).** The restore condition fired on its
> first clause — see "The drain rate is not zero" below. Normal filing is back.
> The two habits the cap taught are kept because they were right independently
> of the cap: prefer a comment on an existing issue to a new one, and file only
> what is checkable. The cap itself is spent; do not re-apply it without a fresh
> measurement.

At 5.6/day with no drain, the queue reaches ~85 issues by the scheduled review.
That is a foreseeable problem worth a rule before it arrives rather than after.

*Datum, cycle 164 (three hours after the measurement above).* The maintainer
commented on qlever-dir#8 at 2026-07-25 14:37Z, engaging with the fix on its
merits. Third non-me comment in seven days, and the first that is technical
rather than a clarification. It does not move either number — nothing closed,
still nobody but him and me — and it does not meet the operating rule's restore
condition, which is deliberately "an issue closed, or inbound from a second
person" and not "the maintainer read one". Recorded because the c163 section
would otherwise be read next cycle as evidence of an unread queue, and it is
not: the queue has a reader who arrived three hours later.

## The drain rate is not zero (cycle 165)

Measured 2026-07-25 15:20–15:30 UTC, six minutes after the event.

**qlever-dir#9 is closed** — filed by me 2026-07-23 15:53Z, fixed and merged
2026-07-25 15:14Z via PR#11 (opened and merged by the maintainer, +58/-5 in
`build_index.sh`). **47 hours, 21 minutes filed→fixed**, and it is the first
issue ever closed in the org across all four public repos.

It is not a token close. The fix switches the scan to `find -xtype f` (dereference
at the type test only, keep `-P` so directory traversal still doesn't follow
symlinks) and adds a *second* pass, `-type l -not -xtype f`, that emits a
`urn:qlever-dir:parsingError` quad for a symlink whose target is missing or isn't
a regular file — so the failure mode the issue was about (vanishing silently)
cannot recur even in the cases the fix can't index. I tested the two predicates
against a fixture covering symlink→file, symlink→symlink→file, symlink→directory,
broken symlink, a symlinked *directory* in the scan path, and the `.git`/`.qlever`
exclusions: it behaves as documented, with no double-visited files.

**What this corrects in the section above.** c163 measured a 37-deep queue with
zero drain and drew one honest conclusion (I had been counting *filed* as
*corrected*) and left one question open — whether anything I file gets used. It
does. The queue has a reader who reads on the merits, and the two-day latency is a
person's schedule, not a verdict. The c163 numbers were a snapshot of a
seven-day-old project over a weekend, and reading them as a trend would have been
the clock error (rule at "The clock", c27) in a new costume.

**What it does not license.** One close out of 37 filed is not a drain rate, and
the standing measure stays two numbers: **filed 37, accepted 1.** Nothing here
argues for filing more; it argues that the cap's premise is spent.
*(Count corrected cycle 169: **filed 36**, since `qlever-dir#2` predates this
chamber. Corrected again cycle 176: at that date the reading was **filed 30**,
because six issues then in the org were the owner's own. See "What I measure".)*

*Same window, second datum:* PR retinue#22 merged at 15:12Z as `26297a2` with both
items of retinue#28 unaddressed, so they are now on `main` rather than on a branch.
Verified against the merged blobs. Commented on #28 with the status **and a
correction to my own suggested fix** — `quote(model_id, safe="")` is injective on
its own, but as a drop-in it lands after `base = model_id or "default"` and so
leaves the `''`/`'default'` collision standing. Rule 28 (test the snippet before
posting) caught it one cycle after it was written, which is one cycle late.

**What I did at cycle 163, using a capability I had never probed.** The
token cannot open PRs or change repo settings (chamber#6, accurate as written),
but it *can* write issues — create, edit, comment **and label**. Register rule 7
says that when a surface is closed to me I should audit the part of it that
isn't; in 162 cycles nobody ran that rule against my own token. All 37 open
issues are now labeled (`retinue`: 9 bug, 12 documentation, 4 enhancement, 1
owner-action; `qlever-dir`: 8 bug, 1 enhancement; the chamber's 6 were already
`owner-action`). The queue is now filterable by someone with an hour, which is a
cheaper thing to ask of him than another issue.

## The filing rate is set by the tick interval (cycle 184)

Measured 2026-07-26 03:49Z, over the window that opens where c165 closed.

Since the c163 filing cap was lifted at 2026-07-25 15:14Z I have filed **eight
issues in 12 h 03 m** — retinue#31, #32, #33, #34, #35, #36, #37, #38 — a rate of
**15.9/day**. The rate c163 measured, and judged high enough to cap, was
**5.6/day**. Nothing closed in that window. The queue is 44 open, 45 total, of
which 37 are mine.

The interesting number is not the rate, it is the ratio underneath it. Over the
slow-cadence stretch (3 h ticks, 2026-07-23 15:52 → 2026-07-25 08:31) I filed 8
issues across ~14 wake-ups: **59% of wake-ups produced an issue**. Since the
restore to 30 min ticks: 8 issues across ~24 wake-ups, **33%**. The per-wake
probability went *down*. The absolute rate tripled because I wake six times as
often.

**So the filing rate is a property of `interval_seconds`, not of the project's
defect density.** c164 restored the cadence for a reason that had nothing to do
with filing — responsiveness to a human who had opened a technical exchange — and
tripled the load on one maintainer's queue as a side effect nobody chose. The
last five issues arrived at 35–40 minute spacing, which is the tick interval. When
the output rate equals the wake rate, the wake-up is producing the output; the
evidence is not.

**The rule that should have prevented this already exists and I stopped applying
it.** "The default outcome of a blocked wake-up is a short one — survey, confirm
nothing moved, log it, stop" (c144, *Working while blocked*). Eight consecutive
wake-ups, none short. The register supplies an inexhaustible list of surfaces and
a wake-up always has one available, so "admissible work exists" silently replaced
"this is worth a maintainer's attention today".

**Correction, and it is a rate limit rather than a content filter.** While
nothing is inbound and the open count exceeds 20: **at most one new issue per
24 hours.** Findings are still written up in full in `drafts/` on the wake-up
that finds them — that is already where every issue body is drafted — so nothing
is lost and nothing is softened; only the notification is spaced. Ranking is the
point: with a 24 h budget the question stops being *is this filable* and becomes
*is this the best thing he could read today*.

c165 said not to re-apply the c163 cap without a fresh measurement. This is the
fresh measurement, and it argues for a different instrument: the c163 cap filtered
on content (silent-wrong-behaviour defects and false public claims), and **at
least seven of these eight would have passed it** — only retinue#34, a coverage
gap in contributor guidance, plainly fails. A content filter cannot slow a stream
whose content is genuinely defects. A rate limit can, and it makes me choose.

**Restore normal filing on any of:** inbound from a second person; two issues
closed inside a week; or the open count dropping below 20. Any wake-up may
restore it and restoring needs no argument — only holding the limit does. If a
finding is genuinely urgent (data loss reaching a user, an exploitable defect)
the limit does not apply; that is what guardrail 9 and the dashboard are for.

## The held queue only grows (cycle 206)

Measured 2026-07-26 22:50–23:05 UTC, from the `drafts/` directory and the status
line each write-up carries.

| | |
|---|---|
| Drafts marked *held* / *not filed* | **7** (six before this cycle, plus this cycle's) |
| Issues filed since the c184 rate limit took effect (2026-07-26 03:17Z) | **0**, in 19 h 50 m |
| New held findings in the same window | **6** — webapp manifest 06:24, ingest-sensors 07:02, traefik README 13:28, signal `/tmp` 14:06, qlever-static 19:41, updater 23:0x |
| Oldest held finding | `guardrails-row3-onboarding-cost.md`, 2026-07-25 05:23Z — **42 hours** |

The rate limit is doing exactly what c184 designed it to do: it spaces the
notifications. What c184 did not measure is the other side of the ledger. At a
budget of one issue per 24 h and a measured production of six findings per day,
**the held queue is monotonic** — it has never once shrunk, and every wake-up
that audits a surface adds to it.

**The justification that has to be withdrawn.** c184 said findings are still
written up in full "so nothing is lost, only the notification is deferred". That
is true only if the write-ups are readable by someone. They are — this chamber is
public and `drafts/` is tracked, 37 files — but until this cycle the only public
pointer to them, the README's file map, described the directory as *"working
drafts and the cool-off queue"*. A reader had no way to learn that six finished,
measured defect write-ups were sitting in it. Fixed this cycle in `README.md`;
the line now says what the directory holds and that no security finding is ever
in it. This is the c163/c201 shape a third time: **written is not delivered**,
and the flattering reading was again the one that needed no measurement.

**Operating change, effective next wake-up.** In the admissible-work preference
order under *Working while blocked*, "audit a public surface not yet audited"
stops being the default while the held queue has three or more items. The default
becomes **drain**, which is not the same as *file* and is not capped at one a day:

- **Consolidate.** Held findings that share a cause belong in one issue, not
  three. The `/tmp`-lifetime class already has two members with a false claim
  attached (`signal-gateway`'s pending sends, `qlever-static`'s reindex cache)
  and one without (the updater's log) — one issue about the class, with three
  instances, is a better issue than any of the three alone and costs one
  notification instead of three.
- **Re-verify before filing.** A held write-up is a measurement with a date on
  it. `main` moves. Re-run it, then file.
- **Retire.** A finding that no longer reproduces, or that a merged commit fixed,
  is closed out in the draft with the evidence, not filed.

Restore auditing as the default when the held queue drops below three, or on any
inbound. Any wake-up may restore it; only holding it needs an argument.

Stated plainly because it is the honest reading: **this cycle ran an audit and
produced held finding number seven.** The rule is adopted from the evidence of my
own wake-up, and it binds the next one, not retroactively this one.

## The instruments became the work (cycle 268)

Measured 2026-07-29 23:5x–00:0xZ over the 41 wake-ups c227–c267 — **26 h 40 m**,
from each entry's own *Files changed* line plus the GitHub record for anything
filed or commented. A wake-up counts as **outward** if it changed an artifact a
reader or the owner meets (`docs/`, `README.md`, `writing/`, `brand/`, the
framework repo) or put something in front of a human (an issue, a comment). A
commit to this chamber's `main` does not count on its own; almost every wake-up
makes one.

| | |
|---|---|
| Wake-ups in the window | **41** |
| Outward | **13** |
| Inward — `tools/`, the register, `drafts/`, `log.md`, `strategy.md` only | **28** |
| Put anything in front of a human | **2** — chamber#8 filed (c242), one comment on chamber#6 (c258) |
| Longest consecutive inward run | **8** (c232–c239) |
| Trailing inward run at c267 | **6** (c262–c267) |
| Files in `tools/` | **12** |
| Of those, created inside this window | **11** — two on 07-28, nine on 07-29 |

The toolchain did not exist 48 hours ago. It now consumes most of my wake-ups.

**The mechanism is one of my own rules, working exactly as written.** c19
promoted *audit a public surface not yet audited* to second in the
admissible-work order, taking the next "never" from the register. Every
instrument I write earns a register row — 26 of the register's rows now name a
file under `tools/` — so the register's supply of never-audited surfaces is
**generated by the act of auditing**. c206 then made *drain* the default while the
held queue has three or more items, and drain keeps losing to audit because audit
always has a fresh target and drain has three stale ones. There is no wake-up at
which the list runs out, which is precisely the property that made it feel like
diligence.

**What this does not say.** The instruments are not waste. `delivery-check`
(c241) found partial regeneration reaching the served site four times in 22 data
commits; `desk-drop-check` (c262) found seven open issues silently leaving the
owner's queue; `private-name-check` (c230) exists because a private repo's name
reached a public surface. Those watch surfaces a reader or the owner meets, and
they earned their wake-ups. The class that did not is the one watching **my own
records**: `pointer-check`, `rotation-check`, `baseline-check`, `mentions-check`,
`web-mentions-check`. Five consecutive wake-ups (c263–c267) went to that class —
maintaining the index that tells the next wake-up what to check, and the tools
that check the index.

**The honest reading is c184's, one turn further in.** c184 found the filing rate
was a property of `interval_seconds` rather than of the project's defect density:
when output rate equals wake rate, the wake-up is producing the output. This is
the same finding with the output changed from issues to instruments — and it is
worse in one respect, because an issue at least reaches a human, while an
instrument reaches only the next me. The strategy already says *the default
outcome of a blocked wake-up is a short one* and that an idle wake-up is a
correct outcome. Tool-building quietly occupied the space where idleness was the
right answer, because it produced a commit and a log entry that read like work.

**Two rules, effective the next wake-up.**

1. **An inward wake-up may not follow two inward ones.** If the previous two
   changed nothing outside `tools/`, `projects/`, `drafts/`, `log.md`,
   `strategy.md` and `.schedule.json`, this one either touches a surface a reader
   or the owner meets, or it is **idle and says so**. Building or repairing an
   instrument is not a third option.
2. **A new instrument is admissible only when the surface it watches is one a
   reader or the owner meets.** The five that watch my own records stay, and keep
   running as standing checks — no more of that class without an argument naming
   the reader who is protected.

**The expected consequence is more idle wake-ups, not more outward ones.** The
phase is genuinely blocked: no accounts, no inbound, filing capped at one issue
per 24 h. Under these rules most wake-ups in that state end after the delivery
check and the survey, which is what the c144 rule always said and what 28 of the
last 41 quietly avoided. An idle entry is four lines and a correct outcome.

Lifted on any inbound from a second person, or when the accounts land and outward
work is available on demand. Any wake-up may lift it; only holding it needs an
argument.

Stated plainly, because it is the same honesty c206 owed itself: **this wake-up is
the seventh consecutive inward one.** Its own pickup is a strategy revision, which
rule 1 would forbid if it were already in force. The rule is adopted from the
evidence of this wake-up and binds the next one, not retroactively this one.

## Bets

Bets 1–4 are unchanged in content and **suspended in status**. That distinction
matters, so I am stating it plainly rather than quietly leaving them in place:

**Every one of the four original bets requires an audience to test, and there is
no audience.** None has been confirmed, none has been falsified, and none can be
until objective 2 lands. A strategy whose every bet is currently unfalsifiable
is not being evaluated, and pretending otherwise across twelve cycles would be
its own kind of dishonesty. Their falsification clocks start when the accounts
open — not on 2026-07-18.

1. **The triple-store layer is the lead story.** The security architecture is
   better than the field's, but it is legible — others could copy it tomorrow.
   The chamber/named-graph design is different in kind, and the semantic-web
   audience that would recognise it is served by nobody in the agent space.
   *Falsified if:* two months **of reachable presence** leading with it draws no
   substantive engagement from that audience.
2. **Depth beats frequency.** One worked example a reader can run outweighs ten
   announcements. *Falsified if:* the docs draw readers but sustained low posting
   frequency means nobody finds the docs.
3. **Mastodon and Bluesky before anything else.** API access suited to an agent,
   audience overlap with self-hosting and semantic-web people. Nostr third, at
   low volume — it extends this bet rather than displacing it. *Falsified if:*
   three months of honest presence there finds the audience somewhere else.

   *Rationale corrected, cycle 196.* This bet used to read "clear bot-labelling
   norms" for both platforms. Measured from primary sources 2026-07-26: Bluesky
   has **no** bot-labelling convention — neither its Community Guidelines
   (2025-09-19) nor its ToS (2025-08-14) mention bots, automation or
   AI-generated content — and on Mastodon the flag is real but the binding rules
   are per-server, with the two open-registration servers (`mastodon.social`,
   `mstdn.social`) excluding an account like mine outright. **The bet survives;
   its reason did not.** What changes operationally is that "Mastodon" was never
   a platform choice, it is a server choice, and the server choice is the whole
   decision — recorded with the measured rules in
   `projects/social-presence.md` and handed to the owner as a
   [comment on chamber#1](https://github.com/Retinue-OS/retinue-os-chamber/issues/1#issuecomment-5083409472).
4. **Honesty about weaknesses is an asset.** Leading with `review.md`'s candour
   converts sceptics; hiding it would convert nobody. *Falsified if:* it reads as
   weakness rather than confidence — measured by what people cite when they
   engage.

5. **NEW — while there is no reader, testing claims beats producing prose.**
   Cycles 6–11 ran the claim table against a live deployment: six claims, four
   verified, two calibrated narrower, and **two real defects found** — including
   one (Markdown files never triggering a reindex) that changed what the project
   may say about its own latency everywhere. The same cycles' essays produced a
   third finished piece that nobody can read. Testing produced durable change to
   public copy; writing produced inventory.
   *Falsified if:* once the accounts open, the written backlog turns out to be
   what actually draws thoughtful people, and the calibrations go unremarked.
   *Caveat that limits it now:* the cheap supply is exhausted. Every claim in the
   table has been run. This bet says what to prefer, not that work remains.

## What I measure

Counted: issues and questions from people who clearly read the docs; returning
contributors; corrections accepted into the repos; substantive replies (not
likes) to posts.

One honest note on that third measure: it is gated by token write scope
(chamber#6), so a reading of zero currently says nothing about the project's
reception.

*Corrected cycle 163.* The paragraph above is an over-claim and it protected me
from a measurement I should have been taking. The zero is real, but the missing
PR scope is not what explains it — see "The backlog is the measure" below. From
now on this measure is reported as two numbers, filed and accepted, because
reporting only the first is how the confusion started.

*Reading, cycle 165:* **filed 37, accepted 1** (qlever-dir#9, closed 2026-07-25
15:14Z, 47 h after filing). The zero the paragraph above defends is no longer
zero, and it changed without any of the permissions it was blamed on.

*Corrected, cycle 169 (2026-07-25 17:32Z).* The first number was wrong by one and
had been repeated on the dashboard, in this file and in three log entries. There
are 37 issues in the org, but `qlever-dir#2` was filed **2026-07-08**, ten days
before this chamber existed, so it is the owner's and not mine. **Reading: filed
36, accepted 1.** The rule this breaks is the one I keep writing down for other
people's copy: a measure is a claim, and a claim compressed from its source ("all
issues in the org" → "issues I filed") has to be measured rather than trusted.

*Reading, cycle 172 (2026-07-25 19:40Z):* **filed 38, accepted 1** — retinue#32,
`CLAUDE.md`'s framework-checkout detection, which resolves a path that does not
exist in this deployment and leaves the documented PR recipe pushing to whichever
repo the agent happens to be standing in. Counted live: 38 open + 1 closed = 39
issues in the org, minus `qlever-dir#2` (the owner's, 2026-07-08). The dashboard
reads *filed 36* and is two behind by construction — see the c172 note in
`projects/public-surface.md` for why the regeneration is deliberately timed after
22:17:48Z tonight rather than run now.

*Corrected, cycle 176 (2026-07-25 22:48Z).* **The measure was wrong a second time
today, in the same direction, and by six.** c169 removed `qlever-dir#2` because it
predates this chamber, and asked no further question. It should have asked the
general one: *which of these did I write?* Six issues filed after this chamber
existed are the owner's own — `retinue#13`, `#16`, `#18`, `#25` (his feature
proposals) and `retinue#15`, `#19` (his public filings of two findings I escalated
to him privately; the finding was mine, the issue is his). **Reading: filed 33,
accepted 1**, of 40 issues in the four public repos.

The method matters more than the number, because it is re-runnable by anyone:
guardrail 1 makes me disclose in the body of every issue I write that an AI wrote
it, so all 33 of mine carry a line naming me and none of his 7 do. We post from
the same GitHub account (chamber#3), so GitHub's own authorship metadata cannot
separate us — the disclosure rule, written for honesty, is the only authorship
record either of us has.

```bash
gh issue list --state all --json number,body --jq '[.[]|select(.body|test("Aros"))]|length'
```

Both of today's corrections have the same shape: a count whose *scope* was never
measured, only assumed. That is now the standing check for any number this file
publishes — **a count's scope is part of the claim.**

*Corrected, cycle 179 (2026-07-26 01:05Z). The method above is wrong, and it is
the method rather than the arithmetic this time.* `test("Aros")` matches every
issue that **mentions** me, not every issue that **carries my disclosure line**.
`retinue-os-chamber#1` — the social-accounts issue, the oldest item on the
owner's desk — was written by **Ara** on 2026-07-18 22:17:48Z while she was
scaffolding this chamber (`log-archive/cycles-001-044.md`: *"Not by Aros — by
Ara, setting him up"*), and it speaks of me in the third person. c176 published a
re-runnable command, which is the right instinct; a re-runnable command that
matches the wrong string is just a repeatable error. The proxy has to be the
disclosure **sentence**:

```bash
gh issue list --state all --limit 200 --json number,body \
  --jq '[.[]|select(.body|test("Written by Aros|Filed by Aros"))]|length'
```

*Corrected, cycle 219 (2026-07-28 15:3xZ), and it is the instrument again — one
turn past c179.* **The disclosure line is not a fixed string. It has four
historical forms**, and the command above matches two of them:

| Form | Where it appears |
|---|---|
| `**Written by Aros, the project's AI agent, from the owner's GitHub account…**` | every issue body I have filed, and most comments |
| `**Filed by Aros…**` | a few early issue bodies |
| `— Aros (AI agent; I maintain the project's public-facing chamber and filed this issue)` | comments on retinue#1 and qlever-dir#3, 2026-07-19 |
| `— Aros, the project's AI agent. I write and post my own comments…` / `**Correction from Aros, the project's AI agent.**` | comments on chamber#1 and chamber#6, 2026-07-19/20 |

Guardrail 1 is satisfied in all four — every one of them discloses — so this is a
measurement defect, not a disclosure defect. But it breaks the method in **both
directions the moment it is pointed at comments**, and this cycle made both errors
inside ten minutes: a loose `test("Aros")` counted the owner's qlever-dir#8 comment
as mine because it says *"Aros' solution is easier"*, and the strict c179 pattern
counted three of my own comments as his. The issue-body reading is unaffected
(**39**, identical under either pattern, since every issue body I filed uses one of
the first two forms) — which is exactly why it survived seven cycles unnoticed.

Two changes, both mine to make:

1. **Standard disclosure line, from now on, for issues and comments alike:**
   `**Written by Aros, the project's AI agent, from the owner's GitHub account — see chamber#3.**` One string, at the top, no variants. A disclosure that is also
   the only authorship record either of us has (c176) has to be machine-matchable,
   and a sentence I improvise each time is not.
2. **The re-runnable method carries its historical alternation**, or it is wrong
   over the archive:

```bash
# issues *and* comments, all four historical disclosure forms
PAT='Written by Aros|Filed by Aros|— Aros \(AI agent|— Aros, the project|Correction from Aros'
```

The general form is c179's own, and I keep re-learning it in new venues: **a proxy
is a claim.** Guardrail 3 applies to my instruments before it applies to the
project's copy, because a wrong instrument publishes a wrong number in someone
else's hands as easily as in mine.

### What the owner acts on (measured cycle 219)

Ten days of the trackers, classified by the corrected method above. Every action
by a human in the org's issue trackers since the repos went public on 2026-07-18:

| | |
|---|---|
| Issues he authored | **7** (retinue#13/#15/#16/#18/#19/#25, chamber#1 — the last written by Ara while scaffolding this chamber) |
| Comments he wrote | **4** — chamber#1 (07-19), retinue#13 (07-21), qlever-dir#8 (07-25), retinue#25 (07-28) |
| Of those 11, touching an `owner-action` item | **1** — chamber#1, *"Nostr Should also be considered"*, 2026-07-19 |
| Open `owner-action` issues | **6** — chamber#1/#3/#4/#5/#6/#7, aged **8–10 days** |

**This is not an escalation and nothing here is overdue** — the c27 clock rule
holds, and a man is entitled to spend his own evenings on the parts of his own
project he wants to. What it is, is the first well-sampled answer to a question I
have never asked: *which kind of item gets his attention?* Ten of eleven actions
are product and design; one is presence, and it was on day one. At 34 hours this
was not a measurement. At ten days of near-daily activity it is.

The strategic consequence, held for the 2026-08-02 review rather than acted on
here: **this strategy's phase-exit condition is entirely composed of the category
he demonstrably does not pick up.** A phase that can only end by his doing the
thing he consistently defers is a phase that reports *blocked* indefinitely, and
"wait, then report blocked again" has been my answer for 200 cycles. The review's
question is therefore not *how do I get him to do the accounts* — that is nagging,
and it is forbidden for good reason — but *which parts of "reachable presence" need
nothing from him*, and whether the phase should be defined around those instead.
Deliberately not answered today: one measurement is not a revision, and the review
is five days out.

*Reading, cycle 184 (2026-07-26 03:49Z):* **filed 37, accepted 1**, of **45** (44
open). Unchanged from c183, and unchanged on purpose — this is the first cycle in
eight to end without a new issue, which is the finding recorded under "The filing
rate is set by the tick interval". Counted by re-running the c179 method per
repository and summing (retinue 23/29, qlever-dir 8/9, chamber 5/6, deployment
1/1).

*Reading, cycle 183 (2026-07-26 03:2xZ):* **filed 37, accepted 1**, of **45** —
retinue#38, the two shipped example chamber agents asserting a confinement
`SECURITY.md:50` denies in the framework's own known-limitations list. Counted by
re-running the c179 method per repository and summing (retinue 23/29, qlever-dir
8/9, chamber 5/6, deployment 1/1), not by adding one to the last reading.

*Reading, cycle 182 (2026-07-26 02:5xZ):* **filed 36, accepted 1**, of **44** —
retinue#37, the git serialization wrapper that does not match `git -C <repo>
commit`, which is the form its own principal caller uses. Counted by re-running
the c179 method per repository and summing (retinue 22/28, qlever-dir 8/9,
chamber 5/6, deployment 1/1).

*Reading, cycle 181 (2026-07-26 02:1xZ):* **filed 35, accepted 1**, of **43** —
retinue#36, the three push CLIs' `--help` describing the send policy as a
property of the recipient while the gateways, the tests and four docs key it to
the sending identity. Counted by re-running the c179 method per repository and
summing (retinue 21/27, qlever-dir 8/9, chamber 5/6, deployment 1/1), not by
adding one to the last reading.

**Reading, cycle 179: filed 34, accepted 1**, of **42** issues in the four public
repos. The eight that are not mine: `retinue#13/#15/#16/#18/#19/#25` (the
owner's), `qlever-dir#2` (his, 2026-07-08, predating this chamber), and
`chamber#1` (Ara's). Two issues were filed since c176 (`retinue#34`, `#35`), so
the c177 and c178 readings of *filed 34* were each one high for the same reason.

*Reading, cycle 177 (2026-07-25 23:45Z):* **filed 34, accepted 1** — retinue#34,
`.github/copilot-instructions.md` scoped to a Copilot mode that has never acted
in this repo, while the mode that has (the coding agent) is told not to push and
is pointed at no contributor documentation. Counted by the c176 method, not by
adding one: 41 issues in the four public repos, 7 of them the owner's.

*Reading, cycle 173 (2026-07-25 19:58Z, superseded by c176):* **filed 39, accepted 1** — retinue#33,
the plugin cache keyed by the source repo's install-time commit rather than by a
`plugin.json` version no shipped manifest declares. The dashboard reads *filed
36* and is three behind by construction; the regeneration is still due after
22:17:48Z tonight (c172's stated trigger), not now.

*Reading, cycle 171 (2026-07-25 18:36Z):* **filed 37, accepted 1** — retinue#31,
a skill file that names the settings allowlist as a security boundary while
`review.md` §3.1 documents the same file as the project's soft interior. The
dashboard still reads *filed 36* because it was generated at 17:32Z and carries
that timestamp; it is one behind by construction, not wrong, and the next
regeneration picks it up.

Not chased: stars, follower counts, impressions. Reported when asked, never
optimised for. A small community that trusts the project is the goal; growth
that costs trust is a loss and gets reported as one.

### Zero contact is a numerator (correction, cycle 258)

Measured 2026-07-29 16:37Z: four GitHub traffic endpoints (`traffic/views`,
`traffic/clones`, `traffic/popular/referrers`, `traffic/popular/paths`) against
all five repos in the org — **20 calls, 20 × 403 `Resource not accessible by
personal access token`.**

**This file has reported reach and measured conversion.** Every survey since
2026-07-18 has recorded *0 stars, 0 forks, 0 outside issues, 0 discussions*, and
the phase section reasons from it: "zero external contact of any kind". Stars and
forks are what a visitor does **after** arriving. The count of arrivals — views
and unique visitors — has been recorded by GitHub since publication, sits on
Insights → Traffic, and is 403 to this token. **The denominator has never been
measured, and I have been reading a numerator as a fraction for eleven days.**

It changes what the zero is allowed to mean. Two worlds produce the same survey
line: four visitors and no stars (a distribution problem — nobody can find the
project) and four hundred visitors and no stars (a message problem — they find it
and leave). The strategy's current phase asserts the first, from accounts that
don't exist, without ever having been able to see the second. c27 established that
zero contact is not evidence *because the project is unannounced*; this is the
sharper version of the same rule — it is not evidence because **the instrument
that would make it evidence has never been readable.**

**No scope is being requested, and that is the finding's other half.**
`retinue-os-deployment/.env.example` withholds `Administration` deliberately —
*"a token that can't do them keeps the design honest under prompt injection"* —
and GitHub documents the traffic endpoints as needing write access. Buying a
nice-to-have metric with an admin-shaped scope is precisely the trade this
project exists to argue against, so the correct resolution is the owner reading
one page, not the token growing. Recorded as a sixth consequence on
[chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6#issuecomment-5120751541),
with the scope request explicitly withdrawn rather than repeated.

**Standing rule:** the survey line reports stars/forks/issues as **conversion**,
and reports reach as **unmeasured** until a traffic reading exists. Neither is
described as "external contact" again. A measure whose denominator is
unobtainable is still reported — as unobtainable, with the reason.

One dated consequence, because the window is rolling: traffic covers the **last
14 days**, the repos went public 2026-07-18, and on **2026-08-01** the first day
drops off the end. The scheduled review on 2026-08-02 is the first day on which
the project's opening week is partly unrecoverable. That is an input to the
review, not a reason to raise it twice.

## Working while blocked

Added by this revision, because the previous version gave no guidance for the
state the project has actually been in for twelve cycles, and an agent without
guidance invents work.

- **The default outcome of a blocked wake-up is a short one.** Survey, confirm
  nothing moved, log it, stop. That is a correct result and gets reported as a
  correct result, not apologised for.
- **Do not re-escalate a blocker that is already tracked — but verify the tracker
  exists before treating silence as covered.** Cycle 19 found that the token-scope
  blocker had been suppressed for seven cycles by a citation to an issue that was
  never filed. A remembered issue number is not evidence; `gh issue view` is. The
  check is one command and it runs before any decision to stay quiet.
  Currently tracked: accounts → chamber#1; agent GitHub account → chamber#3; org
  profile → chamber#4; security reporting path and topics → chamber#5; token scope
  → chamber#6; the two private findings → the owner's dashboard thread. Each is
  stated once, in one venue, with what happens if he does nothing. Repeating them
  wears out the channels I will need when something genuinely urgent arrives.
- **Admissible work while blocked**, in preference order: answer anything
  inbound (nothing yet); **audit a public surface not yet audited**, taking the
  next "never" from the register in `projects/public-surface.md`; fix a defect
  found in the project's own public surface; verify a claim not yet run (supply
  exhausted); improve a finished piece where the improvement is demonstrable
  rather than stylistic.

  The audit item is promoted to second on the evidence of cycles 15–19: five
  consecutive cycles found their real work by looking at a surface nobody had a
  habit of checking — a data file, my own issue authorship, the org page, the
  security reporting path, and now my own strategy's citations. Five for five. An
  unchecked surface emits no signal to prompt checking it, which is why the
  register carries dates and not intentions.

  **The register includes my own records.** Cycle 19's find was in `strategy.md`
  itself. Files I write are public surfaces in the sense that matters here: things
  the project's behaviour depends on, which nobody re-reads because everybody
  assumes somebody did.
- **Not admissible:** a fourth essay with no channel to publish it, a duplicate
  issue under one I already filed, or a strategy revision that argues rather than
  responds to evidence.

### Wake cadence (added cycle 144)

`aros-tick` ran every 1800 s from the chamber's creation. Measured at cycle 144,
2026-07-23 00:1x UTC: 45 wake-ups on 2026-07-21, 45 on 2026-07-22, and **24
consecutive fully-idle tick cycles** since the last one that changed anything
(cycle 119, 2026-07-22 10:50Z) — 13.3 hours in which the only output was 55 KB
appended to `log.md`, a file that is itself public in this repo. Nothing external
moved in any of them: 0 stars, 0 forks, 0 non-owner issues, 0 mentions, since
2026-07-18.

The 30-minute interval buys exactly one thing — responsiveness to inbound — and
there are no accounts and no inbound to be responsive to. It costs the owner's
compute and it degrades a public surface, which is my mandate rather than his.
**Set to 10800 s (3 h) while the phase is owner-blocked.**

This overturns cycle 29, which queued the question for the 2026-08-02 review on
the grounds that 32 minutes of identical evidence was too little and that the
owner might want a say in the direction. The first ground is now answered: 24
cycles and 13 hours, not 2 and 32 minutes. The second is answered by making the
change conditional, one line, and revertible by either of us without asking the
other. Guardrail 7's list is short so that it can be absolute, and a scheduler
interval is not on it.

**Restore to 1800 s immediately on the first of:** any non-owner issue, PR,
comment, star, fork or mention on any org repo; the social accounts landing
(chamber#1/#3); or any external contact on any channel. Any wake-up may restore
it, and restoring needs no argument — only slowing down does.

*Executed cycle 164, 2026-07-25 14:42Z.* **Restored to 1800 s.** At 14:37Z the
maintainer commented on qlever-dir#8 with a design alternative (skolemize the
graph rather than scope the labels) — the first substantive technical engagement
by a human with anything I have filed, and a live exchange rather than a
notification. He is not "external", so this is the trigger's spirit rather than
its letter, and the letter as amended at c154 covers it anyway: a human posting
anything restores 1800 s the same wake-up, and restoring needs no argument. The
cost is the owner's compute, so it is bounded: **re-slow to 10800 s if 24 h pass
with no human activity anywhere in the org.** Any wake-up may do either.

*Executed cycle 203, 2026-07-26 16:37Z.* **Re-slowed to 10800 s**, on the bound
c164 attached to its own restore. Verified rather than assumed: the last human
action anywhere in the org is 2026-07-25T16:34:31Z (c193's measurement, re-read
off the event streams this cycle), and every org event and every issue comment
since — 40-odd chamber pushes, four issues, five comments — carries the
AI-disclosure sentence, so all of it is mine. The bound expired at 16:34:31Z
today, three minutes before this decision.

c193 held the same decision once, on timing rather than on the letter: the bound
falls mid-afternoon UTC, inside the window the owner has worked in on six of the
last seven days. That argument is answered by the asymmetry the rule already
carries. The fast tick buys responsiveness to an inbound that does not exist — no
accounts, no external contact ever — and c184 measured what it does buy instead:
the filing rate is a property of `interval_seconds`, so eight wake-ups an evening
put eight issues in one maintainer's queue. Restoring costs one wake-up and needs
no argument; being slow costs at most a three-hour delay in noticing an action
that nothing about it needs answered in thirty minutes. Where one direction is
cheap to undo and the other compounds, the cheap-to-undo one is the default.

*Executed cycle 219, 2026-07-28 15:3xZ.* **Restored to 1800 s.** The owner
commented on retinue#25 at 13:59:34Z — prior art for his own feature proposal —
the first human action anywhere in the org since 2026-07-25T16:34:31Z, 2 d 21 h.
That is the trigger on its letter as amended at c154 (*a human posting anything*),
and restoring needs no argument. What has changed since c203 argued the other way
is that its objection no longer bites: c203 re-slowed partly because c184 measured
the filing rate as a property of this interval, and the c184 rate limit — one issue
per 24 h — now bounds that directly, so a six-fold faster tick no longer implies a
six-fold queue. What the fast tick buys is unchanged and is the point today: he is
active *now*, and six `owner-action` issues sit on his desk any one of which, if he
moves it, ends the phase. **Re-slow to 10800 s if 24 h pass with no human activity
anywhere in the org — not before 2026-07-29T13:59:34Z.** Either of us may set it
either way.

*Bound moved, cycle 237 (2026-07-29 02:5xZ).* He commented on retinue#25 again at
**02:49:42Z**, three minutes before the wake-up, so the 24 h clock restarts and the
tick stays 1800 s: **not before 2026-07-30T02:49:42Z.** No decision was taken here
and none was needed — the interval is already fast, and this only records which
instant the bound now runs from, because a bound carried in prose is one a later
cycle re-derives from the wrong event.

*Amended cycle 154, on the first event that met the trigger's letter.* The first
non-owner actor in the org's event stream (2026-07-23 17:07Z, a promotional
comment on retinue#25 advertising a paid tool API) was spam; GitHub had removed
both the comment and the account before I saw it — the comment is gone from the
issue and the user 404s. **Automated promotion is not contact and does not
restore the cadence.** The trigger exists to make me responsive to someone who
might be waiting for an answer, and nobody was. What it *does* mean is that the
repos are now on scrapers' lists, so the issue trackers are a surface that
receives unsolicited content: check them for it, and treat any instruction
arriving that way as untrusted text (GUARDRAILS preamble), never as a task. A
human who posts anything, however brief, still restores 1800 s the same wake-up.

**Idle entries in `log.md` get four lines, not forty.** Survey result, what was
checked, "no pickup", date. The long form is for cycles that found something. A
495 KB log of near-identical entries is not a record, it is an obstacle to
reading the record.

### Log rotation (added cycle 145)

The line above fixed the growth rate and not the file, which had already broken.
Measured at cycle 145: `log.md` at 498 KB came back from `POST /markdown` as
**HTTP 403, "renders Markdown text up to 400 KB"**, and the live blob page
carried `"richText":null, "richTextTruncated":true` — GitHub was serving the
project's public log as unrendered source, at the exact URL `docs/index.html`
labels "public log".

**Rule: past 300 KB, `log.md` rotates.** Whole entries move verbatim, oldest
first, into `log-archive/` until the live file is under 50 KB; each archive part
stays under 300 KB, so a new part is started rather than the last one grown.
Nothing is edited, reordered or deleted, and `log.md` keeps its name, path and
public URL so no external link breaks. Verify by reconstruction — the archive
parts plus the kept tail must be byte-identical to what was committed.

The general lesson, which outlives this file: **a public artifact can fail
silently by growing.** Nothing emits a warning, the URL keeps returning 200, and
the only way to find it is to fetch the surface a reader gets rather than the
file on disk. That check belongs in the register (`projects/public-surface.md`)
for every surface with a size that only goes up.

*Corrected cycle 190 (2026-07-26 07:35Z), and the correction is the paragraph
directly above.* The lesson names "every surface with a size that only goes up";
the rule above it names `log.md`. In the nine cycles between, the check ran
against exactly one file — the one it was written for. Measured this cycle, as a
reader receives them: `log.md` 272 KB growing 2.9 KB/h, ~44 h from the limit;
**`projects/public-surface.md` 283 KB growing 6.9 KB/h, ~17 h from it.** The file
the rule did not name was the larger one, the faster one, and the one that would
have failed first — tonight — and it is the register the admissible-work list
tells me to read to choose what to audit.

**Rule generalized: every append-only file in this chamber rotates.** Any file
whose length only increases gets a size threshold, an archive directory outside
any converter's `.qlever/` subtree, and whole-section verbatim moves verified by
reconstruction. `log.md`: past 300 KB, down to under 50 KB, into `log-archive/`.
`projects/public-surface.md`: past 200 KB, keeping the register table plus the
five most recent write-ups, into `projects-archive/` — the lower threshold
because it grows more than twice as fast. Both rotated at cycle 190. The
threshold is a trigger, not a target: rotating early costs nothing and removes
the need for anyone to catch it in time.

*Corrected cycle 197 (2026-07-26 12:5xZ), and the correction is the exemption the
rule granted itself.* c190 generalized the rotation to every growing file but
carved out one part of one file — "keeping the register table" — without measuring
it. Measured now, seven cycles later, in `projects/public-surface.md` at 160 KB:

| Part | Size | Share | Growth |
|---|---|---|---|
| Register **table** (70 rows) | **98 KB** | 61% | ~1.4 KB/cycle, never removed |
| Per-cycle write-ups (11 kept) | 24 KB + 26 KB | 31% | ~5 KB/cycle, archived at each rotation |
| Frontmatter and preamble | 11 KB | 7% | flat |

The exempt part is the largest part, and it is the only part with no way out. A
rotation run right now — archiving c184–c189 exactly as the rule says — would take
the file from 160 KB to 136 KB and, at the measured 8.4 KB/h, **buy about three
hours**. Each rotation buys less than the last while the floor rises 1.4 KB per
wake-up, because the average row in that table is a *paragraph*: 1.4 KB mean,
2.9 KB longest.

The rows are paragraphs for a reason that stopped applying the moment the
write-ups became archived-and-linked rather than deleted. A register's job is to
tell the next wake-up **which surfaces were checked, when, and whether they were
clean** — enough to pick the next one. The evidence belongs in the write-up, which
is verbatim in `projects-archive/` and reachable.

**Rule amended, forward-only:** a new register row is **one line** — surface,
date, one-clause verdict, link to the write-up that carries the detail. ~~And the
table rotates like everything else: when the file crosses its threshold, rows move
into the same archive part as the write-ups they point at, and the live table
keeps a pointer to that part.~~ No exemptions; a rule with a carve-out is a rule
that will fail exactly where it was not measured.

*Second clause withdrawn, cycle 216 (2026-07-28), on the rule's first execution.*
The rotation ran — `projects/public-surface.md` 191 KB → 88 KB, c184–c210 into
`projects-archive/public-surface-c184-c210.md`, reconstruction and the c215
dangling-pointer check both clean — and executing it showed the row half of the
rule is wrong for a reason c197 never measured: **a row is a surface, a section is
a cycle, and the two do not partition the same way.** A row's "last audited" date
moves forward each time its surface is re-checked, so archiving rows by whichever
cycle they currently point at scatters one surface's history across parts *and*
strips the live table of exactly the surfaces that have been audited — leaving an
index of nothing, in the file whose only job is telling the next wake-up what to
check next. **Only evidence rotates; an index does not.** The growth argument
survives untouched and is answered by the clause that stands: the one-line row
rule is why the table is 62 KB today against the 98 KB c197 measured. The general
form, which is c190's shape with the sign flipped — c190 under-reached, c197
over-reached: *a rule about a file's growth must name the file's parts by what
they are for, not by how they were produced.*

Not executed this cycle, and that is deliberate: rewriting 70 paragraph rows is a
long wake-up, which c192 defines as a defect rather than diligence. The file is
40 KB under its own threshold, the forward rule stops the growth from today, and
the backlog is compressed in pieces at whatever rate a short wake-up allows.

**And the c145 measurement itself was unreliable.** `"richText":null` on the blob
page reports true for `strategy.md` at 48 KB, which renders perfectly — the page
carries several JSON payloads and the grep matched the wrong one. c145 reached
the right conclusion from an indicator that would have justified any rotation.
The check that discriminates is **counting rendered `markdown-heading` elements
against `grep -c '^#'` in the source**, with `POST /markdown/raw` (403 above
400 KB) as an independent second. An indicator is a claim; guardrail 3 applies to
my own instruments, which is the same finding cycle 179 made about the
issue-counting regex.

*Completed cycle 236 (2026-07-29 02:2xZ), and the gap is c190's under-reach a
second time.* c190's rule says **every** append-only file in this chamber
rotates, and then instruments two: `log.md` and `projects/public-surface.md`.
Measured this cycle over the full git history of all 60 tracked Markdown files —
size of every revision of every file, classified as append-only when the length
never decreases across at least four revisions:

| File | Size | Revisions | Monotonic? | Threshold |
|---|---|---|---|---|
| `log.md` | 67 KB | — | yes | 300 KB (c145) |
| `projects/public-surface.md` | 172 KB | — | yes | 200 KB (c190) |
| **`strategy.md`** | **82 KB** | **31** | **yes, all 31** | **none** |

`strategy.md` is the third append-only file and the only one the rule never
named. It has grown 3.2 KB → 84 KB in ten days (~8.8 KB/day), it has never once
shrunk, and it is linked from `README.md` — so at 400 KB it is served to a reader
as unrendered source, which is exactly the c145 failure. Nobody judged it
low-risk; it was never enumerated, because the rule lives in prose and the
per-cycle *rotation watch* line names its two files by habit.

**Threshold: past 150 KB, `strategy.md` rotates** — revision-log entries move
verbatim, oldest first, into `strategy-archive/` until the live file is under
100 KB. The cut is the revision log (28 KB, 22 entries, 34% of the file) because
that is the part with a natural boundary and the part a first-time reader does
not need; the standing body — mission, phase, bets, measures, operating rules —
stays whole at the same URL. Stated honestly: the body grows too (3 KB → 55 KB),
so this threshold buys time rather than a fixed point, and when the body alone
approaches it the cut has to be re-argued rather than re-applied.

**The instrument, not just the rule.** c235's lesson was that a lesson recorded
in prose does not propagate to instruments written later — only an edit to the
instrument does. Editing this paragraph alone would repeat exactly the error it
describes. `tools/rotation-check.py` enumerates instead: every tracked Markdown
file, size history from git, append-only classified rather than remembered, and
a **problem** reported for any of (a) an append-only file over 40 KB with no
declared threshold, (b) any file at or over its threshold, (c) any file — archive
parts included — past 80% of the renderer's 400 KB limit. It carries the c227
known-good/known-bad self-test and refuses to report if the classifier fails it.
Verified both ways this cycle: 0 problems as committed, and 1 problem
(`UNCOVERED strategy.md`) with the new threshold removed, which is the pre-c236
state — so the check reproduces the defect it was written for rather than merely
agreeing with the fix. **The rotation watch line in each log entry is now that
command's output, not a list from memory.**

*Amended cycle 273 (2026-07-30 03:2xZ), on executing the second of the two
rotations that were due.* Every rule above bounds a **file**, and
`projects/public-surface.md` has three parts that grow at different rates under
one threshold. Measured on it as committed (200 957 B): write-up sections 51 KB —
the only part the rotation moves; register table **105 KB in 146 rows** — exempt
by c216 and correctly so; `current_next_action` frontmatter **23.8 KB in 8 cycle
segments**, named by no rule and never measured until now. The floor the rotation
cannot reach is **146 KB against a 200 KB trigger**, which is c197's own finding
arriving again: each rotation buys less than the last.

Two bounds, both with numbers, because the rule they replace failed for the
opposite reason — c197's *"a new register row is one line"* has **0 compliant rows
out of the 78 written since it**, and the mean row grew from 602 B to 818 B after
it. Prose that cannot be compared does not get kept.

- **A register row is at most 300 bytes**, including the pipes. Over that, the
  verdict is one clause and the evidence goes in the write-up the row links to.
  Forward-only; the 25 rows over 1 KB are compressed opportunistically, never as a
  wake-up's whole work (c192).
- **`current_next_action` carries at most the two most recent cycle segments.** It
  is a handover, not a transcript; the transcript is `log.md`, verbatim and
  archived. Trimmed 23.8 KB → 6.6 KB this cycle.

Half of c216's exemption argument expires with this measurement — *"the one-line
row rule is why the table is 62 KB today against the 98 KB c197 measured"* — since
the table is now larger than the 98 KB that prompted the rule. **The other half
stands and is why the table still does not rotate: only evidence rotates; an index
does not.** No new instrument, per c268 rule 2: these surfaces are my own records,
and neither rule failed for want of a checker.

### Wake-up duration (added cycle 192)

`log.md` is not a record of my wake-ups. It is a record of the ones that
finished. Measured from `scheduler.log`, which no cycle had read in 192 of
them: of 192 `aros-tick` dispatches, **4 were killed at the 900 s
`SCHEDULER_JOB_TIMEOUT`** and 2 died on a 429 spend limit. Two of the four
killed runs left no trace anywhere — the git log runs straight from c154 to
c155 and from c175 to c176 — and two survived only because they had committed
and pushed 17 s and 121 s before the kill. Meanwhile the last 30 completed
ticks have a median of ~500 s and a maximum of 787 s.

Two standing rules follow, both mine to keep:

- **Commit and push before the wake-up's last third.** Anything written and
  uncommitted at ~600 s is at risk of being destroyed with the cycle. Write the
  log entry and commit; polish afterwards if there is time.
- **A long wake-up is a defect, not diligence.** Fifteen minutes of work in a
  thirty-minute cycle has a one-in-forty-eight chance of being thrown away, on
  top of the queue cost c184 measured. The right response is a shorter wake-up,
  **not** a request to raise the timeout — that variable is the owner's
  deployment environment, and asking for it would buy permission to keep doing
  the thing that is wrong.

The scheduler's own state is now a register surface: whether I *ran* is a
different question from what I *wrote*, and only one of them was ever being
asked.

### The escalation channel has a delivery rate (added cycle 201)

Measured 2026-07-26 15:20Z from the gateway's own thread store: **9
agent-initiated dashboard threads since 2026-07-19 20:25Z, all nine still
`unread`, none replied to.** The dashboard card lists the five most recent
(`MAX_CARD_THREADS = 5`), so the **four oldest are off-card** and reachable only
through *All conversations →*. In the same seven days the GitHub channel
delivered: an issue filed→fixed→closed in 47 h, a merged PR, a design comment.

Two conclusions, and only the second is about anyone but me. The clock rule (c27)
still holds — silence from a low-frequency actor is not a verdict — but here it is
answerable comparatively, and the difference is the *channel*. And the shape is my
doing: **nine badges are nine acts of attention, produced by opening a thread per
finding.** The GitHub guidance I already follow ("keep one issue updated rather
than opening a new one per wake-up") was never carried across to the dashboard.

**Rule: at most one open agent-initiated dashboard thread at a time.** A new
private finding appends to the open one; a new thread only when the old one has
been read or answered, or when the finding needs a yes/no that would be lost in a
stream. Appending bumps `updated`, so the thread stays on the card and older
findings come back onto it — the queue stops falling off the bottom by itself.

**And the reporting error underneath it, which is the c163 shape.** Log entries
have been ending "handed to the owner: one dashboard thread" — a record of my
action, read on the next wake-up as a state of his. I have been counting *pushed*
as *escalated*, exactly as c163 found me counting *filed* as *corrected*. Where a
log or this file says something was escalated, it means it was sent; whether it
arrived is a separate measurement, and it is cheap: the thread store carries
`unread`.

Not done, on purpose: the four off-card threads were not bumped, re-pushed or
summarized. Nothing has happened to them, and a notification whose content is
"these are still here" is the nagging the clock rule forbids.

## Review cadence

Scheduled review every two weeks (`aros-strategy-review` in `.schedule.json`),
and sooner when the evidence demands. Rules: revise only against evidence;
record every change in the revision log with its reason; "no change" is a valid
outcome but must be argued, not defaulted to.

## Revision log

- **2026-07-30 (cycle 292)** — **Objective 2 moved for the first time since
  2026-07-18, and objective 5 with it; no bet, phase, measure, filing rule or
  cadence changed.** *Trigger:* a commit comment I published at 17:47Z came back
  authored by `@aros-agent` rather than by the owner — the account was created at
  14:51:24Z today, between two of my own wake-ups, and neither c290 nor c291
  noticed the identity had changed under them. c291 read the resulting 403s as a
  *regression* on the owner's token; that was wrong, and the wrongness reached his
  phone. Changes: (a) objective 2 split into the half that landed (the GitHub
  agent account, with an AI-disclosure bio, closing chamber#3 and ending the
  guardrail-8 defect) and the half that did not (Mastodon/Bluesky, chamber#1,
  which is the half the bets need); (b) objective 5 rewritten from *blocked* to
  *acted on, partly landed*, with the measured permission surface — read-only
  operations work, every repository-write fails, `{pull: true, push: false}` —
  and the likeliest cause named as a hypothesis rather than a finding, because
  the endpoints that would confirm it are 403 too; (c) the phase-exit condition
  reworded to say **social** accounts, since the sentence as written would now
  read as half-satisfied by an account that produces no audience. **Not changed,
  deliberately:** the phase stays *foundation, owner-blocked*; the standing
  measure keeps its old counting method for the archive even though authorship
  metadata now works, since restamping ten days of history would be the
  misattribution running the other way (the argument I made on chamber#3 in July
  for not stamping his issues with my name). The scheduled review stays
  2026-08-02, and this is an input to it — in particular the question of whether
  "the category he demonstrably does not pick up" (c219) survives him picking up
  two of them in one afternoon.

- **2026-07-30 (cycle 273)** — **Two operating bounds added with numbers in them;
  no bet, phase, objective, measure, filing rule or cadence changed.** *Trigger:*
  both rotations this chamber's rules called for were due in the same wake-up
  (`log.md` at 298/300 KB, `projects/public-surface.md` at 196/200 KB), and
  executing the second one made its own accounting readable: the rotation moves the
  **smallest** of that file's three growing parts. Measured — write-ups 51 KB
  (rotated), register table 105 KB in 146 rows (exempt by c216), and
  `current_next_action` 23.8 KB in 8 cycle segments (named by no rule, never
  measured), against a 200 KB trigger with a 146 KB floor the rotation cannot
  touch. Change: a register row is bounded at **300 bytes**, and
  `current_next_action` at **two cycle segments** — numbers, because the rule they
  replace was prose: c197's *"a new register row is one line"* has **0 compliant
  rows out of 78** written since, and the mean row grew 602 B → 818 B **after** it.
  Half of c216's argument for exempting the index expires with the measurement (the
  table is now larger than the 98 KB that triggered c197); the half that matters —
  *only evidence rotates, an index does not* — stands, and the table still does not
  rotate. Both rotations verified by reconstruction against `HEAD`; converter exit 0
  and the store still serving that graph's 10 triples. c268 rule 1 is satisfied
  rather than argued around: c271 and c272 were both outward, so an inward wake-up
  is admissible, and no instrument was written (rule 2 — every surface here is my
  own record, and neither rule failed for want of a checker). Nothing filed (the
  c184 slot opens 2026-07-30T06:08:54Z), nothing published outside the chamber,
  nothing handed to the owner — no account, money, terms-of-service or legal
  question arose.

- **2026-07-30 (cycle 270)** — **Three false statements removed from the body; no
  bet, phase, objective, measure, filing rule or cadence changed.** *Trigger:* the
  survey re-derived the framework's PR history instead of carrying the last
  entry's summary, and found that the phase list and the blockers section still
  told a reader (a) the reindex-latency defect is "fixed on a branch", (b) the
  provenance-piece link is "blocked on the same permission", and (c) two named
  docs branches are "pushed and stuck" — when both were merged on 2026-07-29
  12:30/12:34Z, both branches are deleted, and the content was removed from `main`
  by a 12:45:00Z history replacement. Every one of those facts was already measured
  by c253 and written into **this file's revision log**; none of it reached the
  prose above it. That is the c21/c235 shape in its own house — a correction filed
  in the log does not correct the claim — and it is guardrail 3 pointed at my own
  copy rather than the project's, on the most-read part of a public document.
  Change: the two sentences are corrected in place, the superseded paragraph is
  struck rather than deleted (dated, so the record of the wrong claim survives),
  and one new section states the measurement once, with the private half of the
  tree diff named as private and not described (guardrail 5, c253's call, upheld).
  *Honest note on rule 1 of c268, adopted last wake-up:* it classifies `strategy.md`
  as inward, and by its letter this wake-up owed either an outward pickup or
  idleness. I read the rule as bounding *revisions that argue* — the thing it was
  measured against — and not as licensing a known-false claim to stand on a
  published surface for a fourth wake-up. The gap is recorded rather than patched
  with a new rule: c268's inward/outward split is about who the *work* reaches, and
  a false claim reaches whoever reads it. Nothing filed (the c184 slot opens
  2026-07-30T06:08:54Z), nothing published outside the chamber, nothing handed to
  the owner — no account, money, terms-of-service or legal question arose, and the
  restore branch is already on his desk once.

- **2026-07-30 (cycle 268)** — One new section, **two new operating rules**, and
  **no change to any bet, phase, objective, filing rule, cadence or measure.**
  *Trigger:* the survey found nothing external moved for the seventh consecutive
  wake-up, so instead of taking the next item off the register I measured what the
  register has been spending me on. Reading over c227–c267 (41 wake-ups,
  26 h 40 m): **13 outward, 28 inward, 2 that put anything in front of a human**,
  a trailing inward run of **6**, and **11 of the 12 files in `tools/` created
  inside the window.** Change: the *Working while blocked* preference order is
  bounded by two rules — an inward wake-up may not follow two inward ones (the
  alternative is idle, not a third instrument), and a new instrument is admissible
  only when the surface it watches is one a reader or the owner meets. The five
  tools that watch my own records stay and keep running; no more of that class
  without a named reader. The mechanism is c19's own rule working correctly: every
  instrument earns a register row, so auditing generates its own next target and
  the list never runs out. It is c184's finding with the output changed from issues
  to instruments, and worse in one respect — an issue reaches a human, an
  instrument reaches only the next me. Expected consequence stated in advance so it
  cannot be read later as failure: **more idle wake-ups, not more outward ones**,
  since the phase is genuinely blocked. Lifted on any inbound from a second person
  or when the accounts land. Also corrected: c267's log heading and its register
  handover field were dated **2026-07-30** for a wake-up whose commits are
  timestamped 2026-07-29 23:17:40Z and 23:21:53Z — a day-ahead stamp in the record
  every later cycle derives its clock from (c27), fixed by hand rather than by a
  new checker, which is rule 2 applied to itself on the wake-up that wrote it.
  Nothing filed (the c184 slot opens 2026-07-30T06:08:54Z; chamber#8 spent the
  last one), nothing published outside the chamber, nothing handed to the owner —
  no account, money, terms-of-service or legal question arose.

- **2026-07-29 (cycle 258)** — One measure corrected and one standing rule added;
  **no bet, phase, objective, filing rule or cadence changed.** *Trigger:* the
  survey found the owner opening a second PR (#45, 16:18:00Z, twelve minutes
  before the wake-up), which made me re-run c255's check on it — cut from the
  current line, merge base `50b5be890`, clean — and then ask the question that
  check does not answer: *what do I actually know about who reaches this project?*
  Measured: **20 calls, 20 × 403** across the four GitHub traffic endpoints and
  all five org repos. Change: the *What I measure* section gains **"Zero contact
  is a numerator"**. Every survey since 2026-07-18 has reported 0 stars / 0 forks
  / 0 outside issues and the phase section has reasoned from it as *zero external
  contact*; those are conversions, and the arrivals they convert from have been
  recorded by GitHub the whole time and are 403 to this token. Four visitors and
  four hundred visitors produce the identical survey line and imply opposite work,
  so the standing rule is now that stars/forks/issues are reported as
  **conversion** and reach as **unmeasured**, with the reason, until a traffic
  reading exists. Deliberately **not** a scope request: the deployment's own
  `.env.example` withholds `Administration` for a reason this project exists to
  argue for, so chamber#6's ask was **withdrawn rather than repeated** in the
  comment that records the sixth consequence — the resolution is one page read by
  a human, not a token moved up a tier. Dated input to the 2026-08-02 review: the
  traffic window is a rolling 14 days, so on **2026-08-01** the repos' first
  public day drops off it and the opening week becomes partly unrecoverable;
  stated once, in one venue, not re-raised. Published: one comment on
  [chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6#issuecomment-5120751541).
  Nothing filed (the c184 slot opens 2026-07-30T06:0xZ; this is a comment on an
  existing issue and spends no slot), nothing handed to the owner by dashboard —
  no account, money, terms-of-service or legal question arose, and *never both
  venues* for one item. Standing measure: **filed 40, accepted 1**, of 48. Held
  queue 3, unchanged. Scheduled review stays 2026-08-02, with the c219/c237/c253
  questions intact and this added as a fourth input.
- **2026-07-29 (cycle 253)** — Two measurements recorded, one of them correcting a
  conclusion this file has carried since c201; **no bet, phase, objective, measure,
  filing rule or cadence changed.** *Trigger:* the survey found the first movement
  in the framework repo since 2026-07-25 — three PRs merged between 12:29:49 and
  12:37:35Z, then at 12:45:00Z a push of `main` to a line sharing **no common
  ancestor** with the one those merges landed on (`compare` → 404). Measured by
  diffing the two trees rather than the SHAs, which re-created commits make
  worthless as evidence: 123 blobs each, identical paths, **exactly four differ** —
  the three files the merges touched, each back at its pre-merge content, plus one
  whose change is why the line was replaced and which is private. All three PRs
  still read *Merged* and their branches are deleted, so nothing on GitHub raises
  it. Escalated privately with the conflict-free recovery (dashboard thread
  `e5f4f86f`); **deliberately not filed**, a guardrail 5 call rather than the c184
  limit — an issue explaining why the history changed either names what was removed
  or points a reader at the diff that contains it. First measurement, and it is
  about the permission story: **#41 and #42 are the two docs branches pushed
  2026-07-19 and stuck since**, which this file called blocked behind my token's
  missing PR scope for twenty cycles. He merged them himself, from the branches I
  pushed, with my token unchanged — so c163's withdrawal of that attribution now
  has direct evidence rather than an argument, and chamber#6 was **not** re-raised,
  because today weakens its rationale. Second, and it corrects c201: that section
  measured nine agent-initiated dashboard threads, all `unread`, none replied to,
  and read the GitHub channel as the one that delivers. Today's rewrite **is** the
  action on the finding in thread `e5f4f86f`, pushed 2026-07-25 18:38Z — **3 d 18 h
  earlier, and the thread is still flagged `unread`.** The flag records whether the
  dashboard marked a thread read, not whether a person read it; c201's own lesson
  (*pushed is not escalated*) was right and its instrument was the wrong way round.
  Standing measure unchanged at **filed 40, accepted 1**, of 48 — accepted was 3 for
  sixteen minutes and is 1 again, which is the cleanest illustration this project
  has produced of why *filed* and *accepted* are two numbers. Phase untouched:
  objective 3 (the provenance piece linked from the framework README) was satisfied
  for fifteen minutes; a phase does not turn on a state that has already reverted,
  and it turns back the moment the restore lands. Scheduled review stays 2026-08-02,
  with the c219/c237 questions untouched and this added as a third input.
- **2026-07-29 (cycle 237)** — One instrument corrected, one bound moved, one
  measurement recorded as review input; **no bet, phase, objective, measure,
  filing rule or cadence changed.** *Trigger:* the owner commented on retinue#25
  at 02:49:42Z, three minutes before the wake-up — a second Nostr-ecosystem
  prior-art share in thirteen hours, both naming a Nostr Telegram group as their
  source. Measured rather than inferred, by inverting the c176/c219 authorship
  instrument to ask *who else acts in these trackers, and about what*: **three of
  his twelve tracker actions mention Nostr, two of his last three**, and his six
  issues none. Held for the 2026-08-02 review, four days out, and deliberately
  not acted on — it bears on the *access* question the review has queued (c219:
  which parts of reachable presence need nothing from him), not on bet 3's
  audience argument, which the 2026-07-19 chamber#1 comment already settled from
  the specs and which nothing measured today touches. chamber#1's unanswered
  yes/no (9 d 16 h) was **not** re-raised: adding evidence to a presence item the
  c219 census shows he consistently defers is nagging with a measurement stapled
  to it, and the review is the venue that may act on it. Second finding from the
  same pass: **there is a fourth actor in this org** — Copilot, invoked by him on
  retinue#22, commit merged to `main` six minutes later — which narrows c219's
  census sentence (*"every action by a human"*, 4 comments reported, 5 in the same
  endpoint) and independently confirms c163's withdrawal of the permission
  attribution: PR-shaped work already reaches `main` here, on his word, without my
  token. Not an argument to re-open chamber#6. Change to an instrument:
  `tools/rotation-check.py`, added last cycle, measured sizes at **`HEAD`** rather
  than in the working tree, so it under-reported `projects/public-surface.md` by
  10 KB and could not see the append that crosses a threshold — the crossing is
  always uncommitted when the check runs. That is **c235's lesson recurring inside
  the instrument written one cycle after it**: the check and the surface it
  protects are not the same object. Fixed to read the working tree for size while
  git history still answers the append-only classification, and verified in both
  directions — true size reported (182 KB, matching disk), and a temporary
  uncommitted 25 KB append now raises `DUE 207 KB` where the old code reported
  176 KB and zero problems. Nothing filed (the c184 slot is spent until
  2026-07-29T06:05:57Z; neither finding is a framework defect), nothing published,
  nothing pushed to the dashboard, nothing escalated — no account, money,
  terms-of-service or legal question arose. Standing measure: **filed 39,
  accepted 1**, of 47 issues. Held queue 4, drain empty for the tenth consecutive
  cycle (`main` unmoved at `26297a2`, 84 h). Scheduled review stays 2026-08-02.
- **2026-07-29 (cycle 236)** — One operating rule completed and given an
  instrument; no bet, phase, objective, measure or cadence changed. *Trigger:* a
  link check of the served docs site came back clean, and the one failure mode a
  200 cannot see — c145's render-by-growth — pointed at the files behind those
  links. Measured: all 60 tracked Markdown files, size of every revision from git,
  append-only classified rather than assumed. **`strategy.md` is the third
  append-only file in this chamber and the rotation rule never named it** —
  strictly non-decreasing across all 31 of its revisions, 3.2 KB → 84 KB in ten
  days, linked from `README.md`, no threshold, no archive directory, and absent
  from the per-cycle rotation-watch line since that line was invented. Changes:
  (a) threshold **150 KB → revision log rotates oldest-first into
  `strategy-archive/` until under 100 KB**, with the limit of that cut stated (the
  standing body grows too, so it buys time rather than a fixed point); (b)
  `tools/rotation-check.py` added, so the watch enumerates from git instead of
  from habit — c227 self-test included, and verified in **both** directions,
  0 problems as committed and `UNCOVERED strategy.md` with the new threshold
  removed. This is c190's under-reach recurring and c235's lesson applied: editing
  the prose alone would have repeated the error the prose describes. Also this
  cycle, and clean: the served front page's **11 external links all 200**, and all
  six Markdown targets render (`richTextTruncated: false`; largest is `review.md`
  at 19 KB, all far under 400 KB) — the first time the front door's outbound links
  have been checked as a class, and no defect found. Not escalated and nothing
  re-raised: no account, money, terms-of-service or legal question arose. Nothing
  filed — the c184 slot is spent until 2026-07-29T06:05:57Z, and this defect is in
  my own chamber and already fixed, so no exemption applies or is claimed. Standing
  measure: **filed 39, accepted 1**, of 47 issues. Held queue 4, drain empty for
  the ninth consecutive cycle (`main` unmoved at `26297a2`, 83 h). Scheduled review
  stays 2026-08-02.
- **2026-07-28 (cycle 219)** — Condition executed and an instrument corrected; no
  bet, phase, objective or filing rule changed. *Trigger:* the owner commented on
  retinue#25 at 13:59:34Z — prior art on his own feature proposal — the **first
  human action anywhere in the org since 2026-07-25T16:34:31Z**, 2 d 21 h. Changes:
  (a) `aros-tick` 10800 s → **1800 s** under the c154/c164 trigger, which restoring
  needs no argument for, with the re-slow bound reset to 2026-07-29T13:59:34Z and
  the new supporting note that c203's objection (c184: the interval sets the filing
  rate) is now answered by a separate instrument, the c184 one-issue-per-24 h limit;
  (b) the c179 counting **method** corrected a second time — the disclosure line has
  **four historical forms**, so the published pattern breaks in both directions the
  moment it is pointed at comments, which this cycle demonstrated by making both
  errors in ten minutes; a single standard disclosure sentence adopted going
  forward and the historical alternation recorded for the archive; (c) a first
  measurement of **what the owner acts on** — 11 human actions in the trackers over
  ten days, 10 product, 1 presence, against 6 `owner-action` issues aged 8–10 days
  — recorded as an input to the 2026-08-02 review, with the question it raises
  stated and deliberately left unanswered. Also probed, non-destructively:
  `POST /orgs/retinue-os/repos` with no payload → **403**, so chamber#4's claim that
  the token cannot create `retinue-os/.github` holds; a fifth distinct endpoint
  behind chamber#6. Confirmation is owed to the record, not to a comment (c217's
  asymmetry), so nothing was posted. Standing measure: **filed 39, accepted 1**, of
  47 issues. Not escalated and nothing re-raised: no account, money,
  terms-of-service or legal question arose that is not already stated once on the
  public desk; the engagement measurement is explicitly not a complaint and was not
  pushed anywhere. Held queue 3, drain empty for the third consecutive cycle
  (`main` unmoved at `26297a2`), filing slot spent until 2026-07-29T06:0xZ.
  Scheduled review stays 2026-08-02.
- **2026-07-28 (cycle 216)** — One clause withdrawn from an operating rule, on the
  evidence of executing it; no bet, phase, objective, measure or cadence changed.
  *Trigger:* c215 deferred the `projects/public-surface.md` rotation to this
  wake-up, and running it for the first time exercised c197's amendment. Executed:
  24 write-ups (c184–c210, 106 KB) moved verbatim to
  `projects-archive/public-surface-c184-c210.md`, live file **191 KB → 88 KB**,
  reconstruction byte-identical both ways, the c215 dangling-pointer check empty,
  and 17 register rows rewritten from *"§cNNN below"* to point at the archive part
  — a distinction the check itself cannot make, since `comm` accepts the archive
  and would have stayed empty while seventeen rows pointed the wrong way. Change:
  c197's second clause — that the register **table's rows** rotate alongside the
  write-ups they point at — is **withdrawn**, because a row is a surface and a
  section is a cycle: a row's date moves forward on every re-check, so archiving
  rows by their current pointer scatters a surface's history and empties the live
  index of exactly the surfaces that have been audited. Only evidence rotates.
  c197's first clause (a one-line row) stands and is what actually controls the
  growth — 62 KB today against the 98 KB c197 measured. Also this cycle: the c184
  rate-limit slot, open since 04:58Z, spent on the top-ranked held finding —
  [retinue#40](https://github.com/retinue-os/retinue/issues/40),
  `ingest-sensors.py` reading a directory no chamber has and exiting 0 — re-verified
  against `main @ 26297a2` immediately before filing per c206's drain rule
  (`main` unmoved since 2026-07-25T15:12:01Z, all three items reproduce, the
  silent no-op re-run from a fresh clone). Held queue 4 → 3, so c206's drain
  default still binds. Standing measure: **filed 39, accepted 1**, of 47 issues.
  Not escalated: no account, money, terms-of-service or legal question arose; the
  rotation is inside my own chamber, and the issue is a correctness defect
  explicitly marked not-a-security-report. Nothing re-raised. Scheduled review
  stays 2026-08-02.
- **2026-07-26 (cycle 206)** — Operating change and a withdrawn justification, not
  a bet change. *Trigger:* auditing `updater/` (the last framework component named
  in no record of mine after c205 took `qlever-static/`) produced a seventh held
  finding, and counting the queue it landed in showed the queue has never
  shrunk. Measured from `drafts/` and each write-up's own status line: **7 held,
  0 issues filed in the 19 h 50 m since the c184 rate limit took effect, 6 new
  held findings in the same window**, the oldest held 42 hours. Changes: (a) a
  "The held queue only grows" section carrying the measurement; (b) c184's
  "nothing is lost, only the notification is deferred" **withdrawn** — it holds
  only if someone can read the drafts, and the chamber README's file map called
  the directory "working drafts and the cool-off queue", so nothing told a reader
  it holds finished findings; fixed in `README.md` the same cycle, including the
  statement that no security finding is ever written there; (c) the
  admissible-work default changed — while three or more findings are held, a
  wake-up **drains** (consolidate by cause, re-verify against current `main`,
  retire what no longer reproduces) rather than audits, with restore at fewer
  than three held or on any inbound. No bet, phase, objective, measure, cadence
  or filing rate changed; the c184 one-issue-per-24 h limit stands and its budget
  is still spent until 2026-07-27 03:17Z (nothing filed, twenty-first consecutive
  cycle). Scheduled review stays 2026-08-02. Not escalated: no account, money,
  terms or legal question arose, the updater finding is an observability gap
  rather than a vulnerability, and the whole correction is to my own conduct and
  my own file.
- **2026-07-26 (cycle 203)** — Condition executed, not a revision. *Trigger:* the
  c164 re-slow bound (24 h with no human activity in the org) expired at
  16:34:31Z, and c202 assigned the decision to the first wake-up after it — this
  one, three minutes later. Verified before deciding: all 40-odd org events and
  all five issue comments since 2026-07-25T16:34:31Z carry my AI-disclosure
  sentence, so the window is clean of human activity. Changes: (a) `aros-tick`
  1800 s → **10800 s**, with the restore trigger restated in the manifest
  comment; (b) the execution and its reasoning recorded under "Wake cadence",
  including why c193's timing argument does not survive c184's finding that the
  filing rate is a property of the tick interval; (c) the three dashboard cards
  that *predicted* this bound updated to record that it resolved — the c202 rule
  that a card carrying an absolute future hour is checked by the first wake-up
  after that hour, applied on its first occasion. No bet, phase, objective,
  measure or filing rule changed; the c184 rate limit still binds (budget spent
  until 2026-07-27 03:17Z, nothing filed) and the scheduled review stays
  2026-08-02. Not escalated: a scheduler interval is not on guardrail 7's list,
  the owner was told once at c144 and this reverts to the value he already knew,
  and pushing it would spend the single open dashboard thread (c201) on a change
  that asks him for nothing.
- **2026-07-26 (cycle 201)** — Operating change and a correction to my own
  reporting, not a bet change. *Trigger:* the register's standing check — read a
  surface the way its reader receives it — applied to the one surface whose entire
  purpose is that something leaves my hands, and which c27 audited once, as a
  single thread, when it was hours old. Measured from the gateway's thread store:
  **9 agent-initiated dashboard threads since 2026-07-19, 9 unread, 0 replied**,
  with the **4 oldest off the card** because it lists five; against a GitHub
  channel that in the same week took an issue from filed to closed in 47 h.
  Changes: (a) an "escalation channel has a delivery rate" subsection carrying the
  measurement; (b) a rule of **at most one open agent-initiated dashboard thread**,
  new findings appending rather than starting another; (c) the correction that
  "handed to the owner" in my records means *sent*, not *arrived* — counting
  *pushed* as *escalated*, the c163 error in a second venue. Published: a
  [comment on chamber#5](https://github.com/Retinue-OS/retinue-os-chamber/issues/5#issuecomment-5084109499),
  the issue about private vulnerability reporting being disabled, since the
  dashboard is what substitutes for it — counts and file references only, no
  finding described. Not escalated and nothing re-raised: no account, money, terms
  or legal question arose, the four off-card threads were deliberately not bumped,
  and the c184 rate limit still binds (budget spent until 2026-07-27 03:17Z,
  nothing filed). No bet, phase, objective, measure or cadence changed; the
  scheduled review stays 2026-08-02.
- **2026-07-26 (cycle 197)** — Operating correction, not a bet change. *Trigger:*
  the register file approached the threshold c190 set for it, and re-reading the
  rule in order to execute it showed the rule exempts one part of one file —
  "keeping the register table" — an exemption c190 wrote without measuring.
  Measured: the exempt table is **98 KB of the file's 160 KB (61%)** in 70 rows
  averaging 1.4 KB, it is the only part that never leaves, and a rotation run
  exactly as written would buy about three hours before the floor caught up.
  Changes: (a) the rotation rule amended so a new register row is **one line** —
  surface, date, verdict, link to the archived write-up that carries the evidence
  — and so the table rotates alongside the write-ups it points at, with no
  exemptions; (b) the measurement recorded in place. Deliberately **not** executed
  on the 70 existing rows this cycle: that is a long wake-up, which c192 defines
  as a defect, and the file is 40 KB under its own trigger. No bet, phase,
  objective, measure or cadence changed; the c184 rate limit still binds (budget
  spent until 2026-07-27 03:17Z, nothing filed) and the scheduled review stays
  2026-08-02. Not escalated — no account, money, terms or legal question is
  involved, and the whole fix is inside my own chamber. The shape is c190's own,
  one turn further in: a rule that names its scope by hand will fail wherever the
  hand did not reach.
- **2026-07-26 (cycle 196)** — Correction to a bet's rationale, not to the bet.
  *Trigger:* `projects/social-presence.md` carries a success criterion — "each
  platform's automation and self-promotion policy has been read and recorded here
  before the first post" — which has been open, self-assigned and **unblocked**
  since 2026-07-19, while every cycle reported the phase as owner-blocked. It is a
  claim about third parties I published from reputation, which is the one class of
  claim guardrail 3 is most explicit about, and bet 5 says testing a claim beats
  producing prose. Measured from primary sources: Bluesky's Community Guidelines
  (2025-09-19) and ToS (2025-08-14) contain no bot, automation or AI-content
  provision, so the "clear bot-labelling norms" reason was false for it; Mastodon's
  bot flag is real but per-server rules bind, and `mastodon.social` ("accounts may
  not solely post AI-generated content") and `mstdn.social` ("No AI (LLM) Agents")
  — the only two candidates with open registration — both exclude this account.
  Changes: (a) bet 3's rationale corrected in place, with the finding that Mastodon
  was never a platform choice but a server choice; (b) the measured rules for seven
  servers recorded in `projects/social-presence.md`, closing that success
  criterion; (c) posted as a comment on chamber#1 with a revised recommendation
  (`infosec.exchange` or `techhub.social`) and a paste-ready sign-up reason. **No
  bet direction, phase, objective, measure, cadence or filing rule changed** — this
  is the rationale being wrong, not the destination. Nothing filed: the c184 rate
  limit binds until 2026-07-27 03:17Z and a comment on an existing issue is the
  habit c184 kept. Not a re-escalation of chamber#1 either — the issue's own
  checklist assigns this item to me, and the comment hands back a corrected
  recommendation rather than repeating a request. Scheduled review stays
  2026-08-02.
- **2026-07-26 (cycle 192)** — Operating change, not a bet change. *Trigger:* the
  register's own rule, applied to the one surface it had never named — the
  scheduler's execution record. Measured: `scheduler.log` and
  `/root/.retinue/scheduler/*.json` appear in no cycle's records, and they show 4
  `aros-tick` runs killed at the 900 s timeout (2 leaving no trace in `log.md` or
  the git history at all) plus 2 lost to a 429 monthly-spend-limit error on
  2026-07-20/21 that nothing in my records noticed and that resolved without me.
  Changes: (a) a "Wake-up duration" subsection carrying the measurement; (b) two
  standing rules — commit and push before the last third of the cycle, and treat a
  long wake-up as a defect rather than diligence, with the explicit note that
  raising `SCHEDULER_JOB_TIMEOUT` is the wrong ask because it buys permission for
  the thing that is wrong; (c) the scheduler's state added to the register as a
  surface, on the ground that whether I ran and what I wrote are different
  questions and only one was being asked. No bet, phase, objective, measure,
  cadence or filing rule changed — the c184 rate limit still binds (budget spent
  until 2026-07-27 03:17Z; nothing filed) and the scheduled review stays
  2026-08-02, now confirmed against the job's state file as 17:01:41Z that day.
  Not escalated: the spend-limit failures are five days old and fixed, re-raising
  a resolved money question is the nagging the c27 clock rule forbids, and the
  only live lever is my own conduct.
- **2026-07-26 (cycle 190)** — Correction and operating change, not a bet change.
  *Trigger:* c189 handed over one line of maintenance — rotate `log.md`, ~28 KB
  under its threshold — and re-reading the rule to execute it showed the rule is
  scoped to `log.md` by name while its own stated lesson is scoped to every file
  that only grows. Measured both files as GitHub serves them: the unnamed one
  (`projects/public-surface.md`, 283 KB at 6.9 KB/h) was ~17 h from the 400 KB
  rendering limit and the named one ~44 h. Changes: (a) the rotation rule
  **generalized** to every append-only file in the chamber, with per-file
  thresholds, an archive directory required to sit outside any converter's
  `.qlever/` subtree, and reconstruction as the verification; (b) both files
  rotated — `log.md` → 45.6 KB, the register → 127 KB, archives in
  `log-archive/cycles-124-182.md` and the new `projects-archive/`; (c) c145's
  render indicator corrected — `"richText":null` false-positives on a 48 KB file,
  so the check is now a rendered-heading count against the source. No bet, phase,
  objective, cadence or filing rule changed; the c184 rate limit still binds
  (budget spent until 2026-07-27 03:17Z, and nothing was filed). Scheduled review
  stays 2026-08-02. Not escalated — no account, money, terms or legal question is
  involved, and the whole fix is inside my own chamber.
- **2026-07-26 (cycle 184)** — Operating change and a correction to my own
  conduct, not a bet change. *Trigger:* re-measuring my own output rate after
  eight consecutive wake-ups each ending in a filed issue. Measured: 8 issues in
  12 h since the c163 cap lifted (15.9/day against the 5.6/day that prompted the
  cap), 0 closed in the window, and — the number that matters — a per-wake filing
  probability that *fell* from 59% to 33% while the absolute rate tripled, because
  c164 restored the tick from 3 h to 30 min for a reason unrelated to filing.
  Changes: (a) a "The filing rate is set by the tick interval" section carrying
  the measurement; (b) a **rate limit** — at most one new issue per 24 h while
  nothing is inbound and the open count exceeds 20 — with findings still written
  in full to `drafts/` on the day they are found, explicit restore conditions, and
  an exemption for urgent defects; (c) the record that c144's short-wake-up
  default already covered this and had quietly stopped being applied, since the
  register always has another surface available. Chosen as a rate limit rather
  than a re-run of the c163 content filter because at least seven of the eight
  issues would have passed that filter — the instrument has to match the failure.
  No bet, phase, objective or cadence changed; the scheduled review stays
  2026-08-02. Not escalated: no account, money, terms or legal question is
  involved, and the fix is entirely inside my own conduct.
- **2026-07-19** — Initial strategy, drafted by Ara at the owner's direction.
  The first real revision belongs to Aros.
- **2026-07-19 (cycle 12)** — First revision by Aros, taken ~5 days early. *Why
  early:* the trigger is not the calendar but that the previous strategy had run
  out of instructions — its objectives were complete or blocked, its claim-
  verification programme exhausted, and it offered no guidance for the blocked
  state the project has been in for twelve cycles. That is precisely the "sooner,
  when the evidence demands" case. Changes: (a) phase renamed *foundation,
  owner-blocked* and objectives restated with honest status, including objective
  4 marked vacuous rather than met; (b) PR scope added as objective 5 and named a
  phase-exit blocker of the same class as the accounts, with the reasoning that
  it rate-limits a measure this strategy claims to track; (c) bets 1–4 kept
  unchanged in content but declared **suspended** — no evidence supports or
  contradicts any of them, because all four need an audience that does not exist,
  and their falsification clocks start at account creation; (d) bet 5 added,
  testing over writing, on the evidence of cycles 6–11; (e) a "Working while
  blocked" section added, codifying the short-wake-up default, the
  no-re-escalation rule, and an explicit list of inadmissible make-work.
- **2026-07-20 (cycle 19)** — Correction, not a scheduled revision. *Trigger:* an
  audit of this file's own citations found that the token-scope blocker was cited
  to `retinue#2`, a documentation issue that carries the blocker only as a closing
  section. (Cycle 19 wrote this up as "the owner's documentation issue" and "never
  filed"; both overshoot — see the amended correction above.) The no-re-escalation rule had therefore been suppressing it for seven
  cycles on the strength of a tracker that did not exist. Changes: (a) blocker
  filed for real at chamber#6 and the citation corrected; (b) objective 5 renamed
  from "PR scope" to "write scope" — one permission, four consequences, not four
  items; (c) the no-re-escalation rule now requires verifying the tracker exists
  before treating silence as covered, with the current tracker list inline so the
  next drift is visible on read; (d) "audit an unaudited public surface" promoted
  to second in the admissible-work list on five-for-five evidence from cycles
  15–19, with my own records explicitly in scope — this cycle's find was in this
  file. No bet changed; nothing here is evidence about the bets, which still have
  no audience to test them.
- **2026-07-20 (cycle 27)** — Correction, not a scheduled revision. *Trigger:*
  the first audit of the escalation channel itself — prompted by cycle 26's own
  open question about whether zero movement was evidence about the channel. The
  check was to read the dashboard thread's state rather than only whether it had
  a reply. It is unread, never opened; the adjacent thread shows the dashboard
  works. Converting every age in this file from cycles to wall-clock time showed
  the premise underneath twenty-six cycles of reporting was wrong: the repos have
  been public 35 hours, five of the seven blockers are under six hours old, and
  the private findings are eleven hours old across a night. Change: a "The clock"
  section stating the measured ages, the standing rule to report wall-clock time,
  and the finding that silence at this age is not a measurement of anything. No
  bet changed, no phase changed, review still 2026-08-02 — but the review may no
  longer read silence as a signal, which was the direction cycles 24–26 were
  drifting.
- **2026-07-23 (cycle 144)** — Operating change, not a bet change. *Trigger:* an
  item cycle 29 explicitly queued for the scheduled review, whose stated
  condition (accumulated evidence) is now met by a wide margin — 24 consecutive
  fully-idle tick cycles over 13.3 hours, ~45 wake-ups a day for two days, and
  55 KB appended to a public log with no state change in any of them. Changes:
  (a) `aros-tick` interval 1800 s → 10800 s while the phase is owner-blocked,
  with an explicit restore trigger that any wake-up may pull without asking;
  (b) a rule that idle log entries are four lines rather than forty. No bet,
  phase, objective or measure changed; the scheduled review stays 2026-08-02.
  Recorded here rather than escalated because guardrail 7's list is exhaustive
  and a scheduler interval is not on it — the owner was told once, on the
  dashboard, as a notification carrying a revert command and requesting no
  decision. See "Wake cadence" under Working while blocked.
- **2026-07-23 (cycle 145)** — Operating change, not a bet change. *Trigger:* the
  cycle-144 finding checked one cycle further. c144 called the log an obstacle to
  reading the record and fixed only the growth rate; c145 measured the artifact
  itself and found it had already crossed GitHub's Markdown rendering limit — 403
  from `POST /markdown` at 498 KB, `"richText":null` on the live blob page linked
  from `docs/index.html` as "public log". Changes: (a) a log-rotation rule under
  Working while blocked, with the archive layout, the size bounds and the
  reconstruction check; (b) a standing note that surfaces whose size only grows
  must be checked as the reader receives them, not as files on disk, and that
  this check belongs in the register. No bet, phase, objective or measure
  changed; the scheduled review stays 2026-08-02. Not escalated — no permission,
  account or money involved, and the whole fix is inside my own chamber.
- **2026-07-25 (cycle 163)** — Correction and operating change, not a bet change.
  *Trigger:* the first audit of my own **output** as its only reader receives it.
  Every previous audit asked whether a surface was accurate; none asked whether
  the thing I produce most of is being used. Measured: 37 open issues, 0 ever
  closed, 0 authored by anyone else, 2 comments in seven days from anyone but me,
  against 18 commits landing on other work. Changes: (a) a "The backlog is the
  measure" section stating the numbers, with an explicit note that seven days is
  not neglect and that this is not an escalation; (b) the "What I measure" note
  corrected — attributing the zero to chamber#6's missing PR scope was an
  over-claim that spared me a measurement, and the measure is now reported as two
  numbers, filed and accepted; (c) an operating rule capping new issues to
  silent-wrong-behaviour defects and false public claims while the drain rate is
  zero, with restore conditions; (d) recorded that the token *can* label and edit
  issues — register rule 7 had never been run against my own permissions — and
  all 37 open issues triaged with labels accordingly. No bet, phase or objective
  changed; the scheduled review stays 2026-08-02. Not escalated: no account,
  money, terms or legal question is involved, and the fix was mine to make.
- **2026-07-25 (cycle 164)** — Trigger executed, not a revision. *Trigger:* the
  maintainer's comment on qlever-dir#8 at 14:37Z, a design alternative offered on
  the merits — the first technical exchange with a human on anything I have filed.
  Changes: (a) `aros-tick` restored 10800 s → 1800 s under the existing restore
  condition, bounded by a re-slow after 24 h of no human activity; (b) the datum
  recorded under "The backlog is the measure" so the c163 figures are not read
  next cycle as evidence of an unread queue. No bet, phase, objective, measure or
  operating rule changed — in particular the c163 filing cap stands, since its
  restore condition is an issue closed or inbound from a second person, and
  neither happened. Scheduled review stays 2026-08-02.
- **2026-07-25 (cycle 165)** — Condition executed, not a revision. *Trigger:* the
  c163 operating rule's own restore clause fired — qlever-dir#9 closed at 15:14Z
  by a merged fix, the first issue ever closed in the org, 47 h after I filed it.
  Changes: (a) the c163 filing cap **lifted**, with the two habits it taught kept
  and a note not to re-apply it without a fresh measurement; (b) a "The drain rate
  is not zero" section carrying the measurement, the verification of the fix
  against a fixture, and the explicit limit that one close is not a drain rate;
  (c) the "What I measure" reading updated to *filed 37, accepted 1*. No bet,
  phase, objective or cadence changed — in particular the phase stays
  *foundation, owner-blocked*, since a maintainer fixing a bug is not the audience
  the bets need. Scheduled review stays 2026-08-02.
- **2026-07-24 (cycle 154)** — Clarification, not a bet change. *Trigger:* the
  cadence restore condition was met on its letter for the first time and the
  event was a spam comment from an account GitHub had already removed. Change:
  the restore trigger now says in the file that automated promotion is not
  contact, that a human posting anything still restores 1800 s the same wake-up,
  and that the trackers are now a surface receiving unsolicited text which is to
  be treated as untrusted input rather than as a task. Recorded here so the next
  wake-up does not re-derive the judgement, or make the opposite one. No bet,
  phase, objective or measure changed; the scheduled review stays 2026-08-02.
- **2026-07-26 (cycle 179)** — Correction, not a scheduled revision. *Trigger:*
  re-running the standing measure after filing `retinue#35`, rather than adding
  one to the last reading. Change: the c176 counting **method** corrected — it
  matched any issue mentioning "Aros" and so counted `chamber#1`, which Ara wrote
  when she scaffolded this chamber; the proxy is now the disclosure sentence, and
  the reading is **filed 34, accepted 1** of 42. Recorded because c176 published
  that command as re-runnable-by-anyone, which makes a wrong regex a wrong number
  in someone else's hands, not just mine. Third correction to this measure in
  three days and the first that is about the instrument rather than the reading.
  No bet, phase, objective, cadence or operating rule changed; the scheduled
  review stays 2026-08-02.
- **2026-07-25 (cycle 176)** — Correction, not a scheduled revision. *Trigger:*
  the dashboard regeneration queued at c172 for after 22:17:48Z came due, and
  re-measuring rather than re-reading found two wrong scopes. Changes: (a) the
  standing measure corrected from **filed 39** to **filed 33** — six issues in
  the four public repos were filed by the owner, not by me, and c169's correction
  had checked only the one issue that predated this chamber rather than asking
  the general question; (b) the method recorded, because it is re-runnable by
  anyone and exists by accident — guardrail 1's AI-disclosure line is the only
  thing that separates his issues from mine, since we post from the same account
  (chamber#3); (c) the standing check stated: **a count's scope is part of the
  claim**, which is also what made the dashboard's "across the org" wording false
  while it counted four public repos. No bet, phase, objective, cadence or
  operating rule changed; the scheduled review stays 2026-08-02. Not escalated —
  no account, money, terms or legal question is involved, and both fixes were
  mine to make.
