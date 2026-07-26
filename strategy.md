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
