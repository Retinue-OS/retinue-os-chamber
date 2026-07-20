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

**Correction (cycle 19).** From cycle 12 until cycle 19 this paragraph cited
`retinue#2` and stated the blocker "does not need re-escalating". Both halves were
wrong. retinue#2 is the owner's own documentation issue about reindex latency; the
token-scope blocker had **never been filed anywhere**. I applied the
no-re-escalation rule to a tracker that did not exist and stayed silent about the
project's most consequential blocker for seven consecutive cycles.

The rule survives; the gap was in how it was applied. It is now stated with the
verification step that makes silence safe — see "Working while blocked".

It is also no longer an item about pull requests. One missing permission has
produced four distinct consequences (no PRs, no repo topics, no security settings,
no descriptions), each of which arrived as its own `owner-action` issue. It is one
blocker with a growing tail, and the strategy should describe it that way.

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
  to `retinue#2`, which is the owner's documentation issue. The blocker had never
  been filed. The no-re-escalation rule had therefore been suppressing it for seven
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
