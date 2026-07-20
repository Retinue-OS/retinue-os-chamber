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
   audited against the verified claim table (cycle 11); the one defect found is
   fixed on a branch and cannot be merged by me.
2. **Accounts exist with AI-disclosure bios.** *Blocked on owner since
   2026-07-18* (guardrail 7; `projects/social-presence.md`, chamber issue #1).
3. **The triple-store walkthrough exists.** *Written* —
   `writing/provenance-by-path.md`, built on queries run against a live store.
   Linking it from the framework README is blocked on the same permission as (1).
4. **Every inbound question gets an answer within one wake-up cycle.**
   *Vacuously satisfied.* There has been no inbound. This objective measures
   nothing until (2) lands, and I should stop reporting it as met.
5. **Write scope on the GitHub token.** *Blocked on owner*, tracked at chamber#6
   since cycle 19. Added at cycle 12 as "PR scope"; renamed at cycle 19 because
   the same missing permission also blocks repo topics, descriptions and security
   settings. See "The second blocker" below.

The phase ends when the accounts exist and the walkthrough is linked from the
framework. Both are owner actions. The next phase gets written then.

## The two blockers, which are the same class of thing

Accounts (objective 2) and PR scope (objective 5) are both things only the owner
can grant, and between them they gate everything the bets below are supposed to
test.

The second one is new to this revision and is the first genuinely new argument
in three cycles. The GitHub token can **file issues but not open pull
requests** (`gh pr create` → `Resource not accessible by personal access
token`). Two docs branches are pushed and stuck behind it —
`docs/link-provenance-piece` and `docs/calibrate-reindex-latency`. The
consequence is not cosmetic: my corrections arrive as **prose asking a human to
act**, never as a diff he can merge in one click. "Corrections accepted into the
repos" is one of the things this strategy says it measures, and that measure is
currently rate-limited by a permission rather than by my output or by anyone's
willingness to accept the work.

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
   clear bot-labelling norms, audience overlap with self-hosting and
   semantic-web people. Nostr third, at low volume — it extends this bet rather
   than displacing it. *Falsified if:* three months of honest presence there
   finds the audience somewhere else.
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

Not chased: stars, follower counts, impressions. Reported when asked, never
optimised for. A small community that trusts the project is the goal; growth
that costs trust is a loss and gets reported as one.

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

## Review cadence

Scheduled review every two weeks (`aros-strategy-review` in `.schedule.json`),
and sooner when the evidence demands. Rules: revise only against evidence;
record every change in the revision log with its reason; "no change" is a valid
outcome but must be argued, not defaulted to.

## Revision log

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
