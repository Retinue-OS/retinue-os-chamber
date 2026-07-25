# Aros — activity log

Append-only. Newest last. One short entry per wake-up. In the owner-blocked
phase the survey *is* the recorded work: a wake-up that checks the org and
confirms nothing moved still gets a short entry, because the durable record that
the check ran — and found no signal — is the point (strategy, "Working while
blocked"). Only a wake-up that does literally nothing, which should not happen,
goes unlogged.

This file is Aros's only memory across wake-ups. He starts cold every time and
sees nothing of the previous run except what is written here.

**Rotation (added 2026-07-23, cycle 145).** Append-only does not mean unbounded
in one file. When this file passes 300 KB, whole entries move verbatim, oldest
first, into `log-archive/` until the live file is back under 50 KB; each archive
file also stays under 300 KB, so a new part is started rather than the last one
grown. Nothing is edited, reordered or deleted, and git history keeps the entries
at their original path either way. The reason is measured, not aesthetic: GitHub
renders Markdown only up to 400 KB and stops long before it stops *storing* the
file, and `docs/index.html` links this file as the project's public log.

Archive, oldest first:

- [`log-archive/cycles-001-044.md`](log-archive/cycles-001-044.md) — 2026-07-18
  to 2026-07-20, cycles 1–44.
- [`log-archive/cycles-045-123.md`](log-archive/cycles-045-123.md) — 2026-07-20
  to 2026-07-22, cycles 45–123.

---

## 2026-07-22 (cycle 124) — idle blocked wake-up; nothing moved since c123

Survey verified live via `gh`, not trusted from c123's log. `git status -sb`
clean (`main...origin/main`, not ahead) at start.

- 4 public repos (retinue, retinue-os-chamber, qlever-dir, retinue-os-deployment)
  all ★0 ⑂0, none archived, discussions disabled/0 on all. Non-owner author
  sweep (issues + PRs, state=all, per_page=100) across all four: 0 each — every
  issue/PR still authored by `retog`. Open retinue PRs #20 (2026-07-22 12:09Z)
  and #14 both confirmed owner-authored (`retog`); not external contact.
- `orgs/retinue-os/events` distinct actors = [`retog`] only. Nothing inbound.
- Rule-3 check: framework HEAD still `6d6a18a` (PR #17 merge, 07-21 16:28Z) —
  no new framework commits since c118, so the claim-table re-audit trigger is
  not met. No claim-table subject touched.
- Admissible-work register (`projects/public-surface.md`): no open
  "never"/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted; own-records current (re-read strategy.md — internally consistent).
  Re-auditing a just-checked surface would be manufactured activity — inadmissible.

Blockers all still OPEN (chamber#1 accounts, #3 agent account, #4 org profile,
#5 security reporting path, #6 token write scope, #7 GUARDRAILS §3 CI claim),
plus retinue#4 (Actions PR permission); none updated since 2026-07-20, none
overdue on the wall clock (repos ~4 days public), each tracked in exactly one
venue. chamber#7 reviewed this cycle: Aros correctly declined to self-edit the
normative GUARDRAILS.md; owner half stands, not re-escalated. c52 security
finding stays on the dashboard thread; not re-pushed.

Drafts unchanged since 07-20 (four qlever-dir .md drafts mapped to issues #3–#7,
plus env-example-audit.md and retrofit.py). None subject to cool-off (no
hostility/incident/other-project-failure draft); no external channel to publish
to anyway (no accounts).

No pickup. Escalated: nothing new (all handoffs already tracked, none overdue).
Published externally: nothing (no accounts). Files changed: this log only.
Scheduled strategy review 2026-08-02.

## 2026-07-22 (cycle 125) — idle blocked wake-up; nothing moved since c124

Survey verified live via `gh`, not trusted from c124's log. `git status -sb`
clean (`main...origin/main`, not ahead) at start.

- 4 public repos (retinue, retinue-os-chamber, qlever-dir, retinue-os-deployment)
  all ★0 ⑂0, none archived. Non-owner author sweep (issues + PRs, state=all,
  per_page=100) across all four: 0 each — every issue/PR still authored by
  `retog`. Newest retinue issues #18/#19 (07-21) owner-authored; no external
  contact.
- `orgs/retinue-os/events` distinct actors = [`retog`] only. Nothing inbound.
- Rule-3 check: framework HEAD still `6d6a18a` (PR #17 merge, 07-21 16:28Z) —
  no new framework commits since c118, so the claim-table re-audit trigger is
  not met. No claim-table subject touched.
- Admissible-work register (`projects/public-surface.md`): no open
  "never"/candidate rows (tail re-read; last finds c71/c119). Claim-verification
  supply exhausted; own-records current. Re-auditing a just-checked surface would
  be manufactured activity — inadmissible per strategy.

Blockers all still OPEN (chamber#1 accounts, #3 agent account, #4 org profile,
#5 security reporting path, #6 token write scope, #7 GUARDRAILS §3 CI claim),
plus retinue#4 (Actions PR permission); none updated since 2026-07-20, none
overdue on the wall clock (repos ~4 days public), each tracked in exactly one
venue. Owner is demonstrably active (filed retinue #9–#20 on 07-20/07-21) but
has not touched the blocker issues; per the wall-clock + no-re-escalate rules
this is not overdue and not re-escalated. c52 security finding stays on the
dashboard thread; not re-pushed.

Drafts unchanged since 07-20 (four qlever-dir .md drafts mapped to issues #3–#7,
plus env-example-audit.md and retrofit.py). None subject to cool-off (no
hostility/incident/other-project-failure draft); no external channel to publish
to anyway (no accounts).

No pickup. Escalated: nothing new (all handoffs already tracked, none overdue).
Published externally: nothing (no accounts). Files changed: this log only.
Scheduled strategy review 2026-08-02.

## 2026-07-22 (cycle 126) — idle blocked wake-up; nothing moved since c125

Survey verified live via `gh api`/`gh repo list`, not trusted from c125's log.

- 4 public repos (retinue, retinue-os-chamber, qlever-dir, retinue-os-deployment)
  all ★0 ⑂0, none archived. Non-owner author sweep (issues + PRs, state=all,
  per_page=100) across all four: 0 each — every issue/PR still authored by
  `retog`. Nothing inbound.
- `orgs/retinue-os/events` distinct actors = [`retog`] only.
- Rule-3 check: framework HEAD still `6d6a18a` (PR #17 merge, 07-21 16:28Z) —
  no new framework commits since c118, so the claim-table re-audit trigger is
  not met. No claim-table subject touched.
- Admissible-work register (`projects/public-surface.md`): no open
  "never"/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted; own-records current (re-read strategy.md — internally consistent).
  Re-auditing a just-checked surface would be manufactured activity — inadmissible.

Blockers all still OPEN, verified via `gh api` (chamber#1 accounts, #3 agent
account, #4 org profile, #5 security reporting path, #6 token write scope,
#7 GUARDRAILS §3 CI claim), plus retinue#4 (Actions PR permission); none updated
since 2026-07-20, none overdue on the wall clock (repos ~4 days public), each
tracked in exactly one venue. Owner demonstrably active on other work but has
not touched the blocker issues; per wall-clock + no-re-escalate rules this is
not overdue and not re-escalated. c52 security finding stays on the dashboard
thread; not re-pushed.

Drafts unchanged since 07-20 (four qlever-dir .md drafts mapped to issues #3–#7,
plus env-example-audit.md and retrofit.py). None subject to cool-off (no
hostility/incident/other-project-failure draft); no external channel to publish
to anyway (no accounts).

No pickup. Escalated: nothing new (all handoffs already tracked, none overdue).
Published externally: nothing (no accounts). Files changed: this log only.
Scheduled strategy review 2026-08-02.

## 2026-07-22 (cycle 127) — idle blocked wake-up; nothing moved since c126

Survey verified live via `gh`, not trusted from the log. Housekeeping note up
front: the c126 log entry was written but **never committed** (last commit was
c125 `654488b`; `git diff` showed 35 uncommitted insertions matching the c126
block). This cycle commits the orphaned c126 entry together with this one — no
data lost, just a missed commit by the previous wake-up.

- 4 public repos (retinue, retinue-os-chamber, qlever-dir, retinue-os-deployment)
  all ★0 ⑂0, none archived; discussions 0 on all four (GraphQL-confirmed).
  Non-owner author sweep (issues + PRs, state=all, per_page=100) across all
  four: 0 each — every issue/PR still authored by `retog`. Nothing inbound.
- `orgs/retinue-os/events` distinct actors = [`retog`] only.
- Rule-3 check: framework HEAD still `6d6a18a` (PR #17 merge, 07-21 16:28Z) —
  no new framework commits since c118, so the claim-table re-audit trigger is
  not met. No claim-table subject touched.
- Admissible-work register (`projects/public-surface.md`): no open
  "never"/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted; own-records current (re-read strategy.md — internally consistent).
  Re-auditing a just-checked surface would be manufactured activity — inadmissible.

Blockers all still OPEN, verified via `gh issue list` (chamber#1 accounts,
#3 agent account, #4 org profile, #5 security reporting path, #6 token write
scope, #7 GUARDRAILS §3 CI claim), plus retinue#4 (Actions PR permission); none
updated since 2026-07-20, none overdue on the wall clock (repos ~4 days public),
each tracked in exactly one venue. Owner demonstrably active on other work
(filed retinue #9–#20 on 07-20/07-21) but has not touched the blocker issues;
per wall-clock + no-re-escalate rules this is not overdue and not re-escalated.
c52 security finding stays on the dashboard thread; not re-pushed.

Drafts unchanged since 07-20 (four qlever-dir .md drafts mapped to issues #3–#7,
plus env-example-audit.md and retrofit.py). None subject to cool-off (no
hostility/incident/other-project-failure draft); no external channel to publish
to anyway (no accounts).

No pickup. Escalated: nothing new (all handoffs already tracked, none overdue).
Published externally: nothing (no accounts). Files changed: this log only (plus
committing the orphaned c126 entry). Scheduled strategy review 2026-08-02.

## 2026-07-22 (cycle 128) — idle blocked wake-up; nothing moved since c127

Survey verified live via `gh`, not trusted from the log. `git status -sb` clean
(`main...origin/main`, not ahead) at start; last commit `5698ffd` (c126+c127).

- 4 public repos (retinue, retinue-os-chamber, qlever-dir, retinue-os-deployment)
  all ★0 ⑂0, none archived. Non-owner author sweep (issues + PRs, state=all,
  per_page=100) across all four: 0 each — every issue/PR still authored by
  `retog`. Newest retinue issues #16/#18/#19 (07-21) owner-authored; nothing
  inbound.
- `orgs/retinue-os/events` distinct actors = [`retog`] only.
- Rule-3 check: framework HEAD still `6d6a18a` (PR #17 merge, 07-21 16:28Z) —
  no new framework commits since c118, so the claim-table re-audit trigger is
  not met. No claim-table subject touched.
- Blocker issues checked for new owner comments (would be inbound): all still
  OPEN, all `updatedAt` = 2026-07-20, no comment added since c118 — chamber#1
  (accounts), #3 (agent account), #4 (org profile), #5 (security reporting
  path), #6 (token write scope), #7 (GUARDRAILS §3 CI claim), plus retinue#4
  (Actions PR permission). None overdue on the wall clock (repos ~4 days
  public), each tracked in exactly one venue. Owner demonstrably active on other
  work but has not touched the blockers; per wall-clock + no-re-escalate rules
  this is not overdue and not re-escalated. c52 security finding stays on the
  dashboard thread; not re-pushed.
- Admissible-work register (`projects/public-surface.md`): no open
  "never"/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted; own-records current. Re-auditing a just-checked surface would be
  manufactured activity — inadmissible per strategy.

Drafts unchanged since 07-20 (four qlever-dir .md drafts mapped to issues #3–#7,
plus env-example-audit.md and retrofit.py). None subject to cool-off (no
hostility/incident/other-project-failure draft); no external channel to publish
to anyway (no accounts).

No pickup. Escalated: nothing new (all handoffs already tracked, none overdue).
Published externally: nothing (no accounts). Files changed: this log only.
Scheduled strategy review 2026-08-02.

## 2026-07-22 (cycle 129) — idle blocked wake-up; nothing moved since c128

Survey verified live via `gh`, not trusted from the log. `git status -sb` clean
(`main...origin/main`, not ahead) at start.

- 4 public repos (retinue, retinue-os-chamber, qlever-dir, retinue-os-deployment)
  all ★0 ⑂0, none archived. Non-owner author sweep (issues + PRs, state=all,
  per_page=100) across all four: 0 each — every issue/PR still authored by
  `retog`. Nothing inbound.
- `orgs/retinue-os/events` distinct actors = [`retog`] only.
- Rule-3 check: framework HEAD still `6d6a18a` (PR #17 merge, 07-21 16:28Z) —
  no new framework commits since c118, so the claim-table re-audit trigger is
  not met. No claim-table subject touched.
- Re-examined whether retinue#19 (agent can self-approve a verify-policy send)
  needs a self-check against my own send-control copy. It does not: #19 was
  handled at c91 and `brand/positioning.md:105-121` already carries the
  calibration — it declines to claim "an agent can never approve its own send"
  and spells out the same-bearer-token gap (`/pending-sends/<id>/approve` and
  `/send` share one token). No copy change; confirmatory only.
- Admissible-work register (`projects/public-surface.md`): no open
  "never"/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted; own-records current (re-read strategy.md — internally consistent).
  Re-auditing a just-checked surface would be manufactured activity — inadmissible.

Blockers all still OPEN, verified via `gh issue list` (chamber#1 accounts,
#3 agent account, #4 org profile, #5 security reporting path, #6 token write
scope, #7 GUARDRAILS §3 CI claim), plus retinue#4 (Actions PR permission); all
`updatedAt` = 2026-07-20, none touched since c118, none overdue on the wall clock
(repos ~4 days public), each tracked in exactly one venue. Owner active on
framework 07-21 (retinue #15–#19 + PR #17) but has not touched the blockers; per
wall-clock + no-re-escalate rules this is not overdue and not re-escalated.
c52 security finding stays on the dashboard thread; not re-pushed.

Drafts unchanged since 07-20 (four qlever-dir .md drafts mapped to issues #3–#7,
plus env-example-audit.md and retrofit.py). None subject to cool-off (no
hostility/incident/other-project-failure draft); no external channel to publish
to anyway (no accounts).

No pickup. Escalated: nothing new (all handoffs already tracked, none overdue).
Published externally: nothing (no accounts). Files changed: this log only.
Scheduled strategy review 2026-08-02.

## 2026-07-22 (cycle 130) — dashboard refresh from live state; two real changes reflected

Dispatched to regenerate all of `docs/data/*.json` from current, verified state.
`git status -sb` opened `ahead 1`: c129's log commit (`26a7c7b`) was committed
but never pushed by the previous wake-up — same stranded-commit pattern noted at
c118/c127. Pushed it with this cycle's work.

Discovered the live dashboard schema before writing (five cards, five files):
briefing → briefing.json {generated,title,text}; projects → projects.json
{mine[],waiting[]}; milestones → agenda.json {events[]}; community →
messages.json {items[]}; owner's desk → todo.json {top,others[]}. Field names
confirmed against `docs/components/*.js`. Kept the existing schema; invented no
new one.

Every number re-verified live via `gh api`/`gh graphql`/`gh issue list`/`gh pr
list` at 2026-07-22 17:08Z, not trusted from the last log:
- 4 public repos (retinue, retinue-os-chamber, qlever-dir, retinue-os-deployment)
  all ★0 ⑂0 watchers0; discussions disabled + count 0 on all four.
- 27 open issues (retinue 14, chamber 6, qlever-dir 6, retinue-os-deployment 1)
  and 3 open PRs (retinue #14/#20/#21). Author sweep: every issue and PR is
  `retog` (the owner's account). `orgs/retinue-os/events` actors = [`retog`].
  0 external contact.
- Descriptions: 3 of 4 blank (qlever-dir has one); no topics on any repo.

Two real changes since the 2026-07-20 17:05 generation, both reflected honestly:
1. **First 3 open PRs now exist** (all owner-authored) where the last dashboard
   said "no open pull requests"; open-issue count 18 → 27. Framed as throughput,
   not traction — all owner/Aros output, no external contribution.
2. **Two previously-private verification findings are now public**: the owner
   reproduced them and filed retinue#15 (credentials leak into subsessions) and
   retinue#19 (agent self-approves a verify-policy send), both still unfixed.
   Updated the owner's-desk item accordingly (was "routed privately... appears
   in no public file" — now stale) and reflected in projects/claim-verification
   and community cards.
Also carried forward the c118 rename (`deployment` → `retinue-os-deployment`).

**Owner's-desk staleness check (task requirement).** Oldest owner-action item is
chamber#1, created 2026-07-18 22:17Z → ~3.8 days (~91 h) at generation. Every
other owner-action issue is 2026-07-20 (~2.6 days). Nothing is older than one
week; briefing states this explicitly ("nothing on the owner's desk is stale").
No re-escalation — per wall-clock + no-re-escalate rules, nothing is overdue.

All five files carry generated=2026-07-22T17:10:00Z, all parse, internally
consistent. No public post (no accounts). No new escalation (all handoffs
already tracked, none overdue). Files changed: the five docs/data JSON files,
this log. Scheduled strategy review 2026-08-02.

## 2026-07-22 (cycle 131) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live at ~2026-07-22 17:2x Z.

- **Traction:** all 4 public repos ★0 ⑂0 watch0; discussions disabled/0. Zero
  external contact still holds.
- **Authorship sweep:** every open issue (27) and PR (retinue #14/#20/#21) is
  `retog`. `orgs/retinue-os/events` distinct actors = [`retog`] only. Latest org
  event is a 17:11Z PushEvent to retinue-os-chamber — my own c130 log push.
  Newest issue/PR `updatedAt` across all repos = 2026-07-22T14:54:56Z, i.e.
  before c130. Nothing external arrived.
- **Git:** chamber `main` clean and level with origin — no stranded commit this
  cycle (the c118/c127/c129 pattern did not recur; c130 pushed cleanly).
- **Blockers:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt` 2026-07-20,
  none touched, none overdue on the wall clock (repos ~4 days public, unannounced,
  no accounts). Each tracked in exactly one venue; not re-escalated. c52 security
  finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (PR #17
  merge, 07-21 16:28Z) — unchanged since c118. Owner's PRs #20/#21 are open, not
  merged, so no new framework commits and the re-audit trigger is not met. No
  claim-table subject touched.
- **Drafts:** unchanged since 07-20 (four qlever-dir issue drafts + env-example
  audit + retrofit.py). None subject to cool-off (none about hostility/incident/
  another project's failure); no external channel to publish to regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply exhausted.
  Own records re-read and internally consistent. Re-auditing a just-checked
  surface would be manufactured activity — inadmissible.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
already tracked in one venue each, none overdue). Files changed: this log only.
Scheduled strategy review 2026-08-02.

## 2026-07-22 (cycle 132) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked"). All checks live via
`gh` at ~2026-07-22 17:3x Z, not trusted from the log.

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0 watch0, none archived. Zero external contact
  still holds.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo (state=all).
  `orgs/retinue-os/events` distinct actors = [`retog`] only. Newest retinue
  issue `updatedAt` = 2026-07-21T19:52Z (#19, owner). Nothing inbound.
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments (chamber#1 comment history ends 2026-07-19, both
  `retog`). None overdue on the wall clock (repos ~4 days public, unannounced,
  no accounts). Each tracked in exactly one venue; not re-escalated. c52 security
  finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (PR #17
  merge, 07-21 16:28Z) — unchanged since c118. Re-audit trigger not met; no
  claim-table subject touched.
- **Git:** chamber `main` clean and level with origin — no stranded commit this
  cycle.
- **Drafts:** unchanged since 07-20 (four qlever-dir issue drafts #3–#7 +
  env-example-audit.md + retrofit.py). None subject to cool-off (none about
  hostility/incident/another project's failure); no external channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records re-read (strategy.md, positioning.md) — internally
  consistent. Dashboard current as of c130's live regeneration (2026-07-22
  17:10Z). Re-auditing a just-checked surface would be manufactured activity —
  inadmissible.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c131. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 133) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 17:4x Z, not
trusted from the log. `git status -sb` clean (`main...origin/main`, not ahead)
at start — no stranded commit from c132.

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0 watch0, none archived. Zero external contact
  still holds.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo (state=all,
  L100). `orgs/retinue-os/events` distinct actors = [`retog`] only. Newest
  retinue issue `updatedAt` = 2026-07-21T19:52Z (#19, owner). Nothing inbound.
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments since c118. None overdue on the wall clock (repos
  ~4 days public, unannounced, no accounts). Each tracked in exactly one venue;
  not re-escalated. c52 security finding stays on the dashboard thread; not
  re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (PR #17
  merge, 07-21 16:28Z) — unchanged since c118. Re-audit trigger not met; no
  claim-table subject touched.
- **Drafts:** unchanged since 07-20 (four qlever-dir issue drafts #3–#7 +
  env-example-audit.md + retrofit.py). None subject to cool-off (none about
  hostility/incident/another project's failure); no external channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records current (strategy.md, positioning.md internally
  consistent). Dashboard current as of c130's live regeneration. Re-auditing a
  just-checked surface would be manufactured activity — inadmissible per strategy.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c132. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 134) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 18:2x Z, not
trusted from the log. `git status -sb` clean (`main...origin/main`, not ahead)
at start; last commit `0d7e36c` (c133).

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0 watch0, none archived. Zero external contact
  still holds.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo
  (state=all, L100). `orgs/retinue-os/events` distinct actors = [`retog`] only.
  Nothing inbound. (chamber pushed 18:18Z = c133's own log commit.)
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments since c118. None overdue on the wall clock (repos
  ~4 days public, unannounced, no accounts). Each tracked in exactly one venue;
  not re-escalated. c52 security finding stays on the dashboard thread; not
  re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (PR #17
  merge, 07-21 16:28Z) — unchanged since c118. Owner's PRs #20/#21 still open,
  not merged; re-audit trigger not met, no claim-table subject touched.
- **Drafts:** unchanged since 07-20 (four qlever-dir issue drafts #3–#7 +
  env-example-audit.md + retrofit.py). None subject to cool-off (none about
  hostility/incident/another project's failure); no external channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records re-read (strategy.md, positioning.md) — internally
  consistent. Dashboard current as of c130's live regeneration (17:10Z). Re-
  auditing a just-checked surface would be manufactured activity — inadmissible.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c133. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 135) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 19:2x Z, not
trusted from the log. `git status -sb` clean (`main...origin/main`, not ahead)
at start; last commit `0d7e36c` (c133), c134 was log-only.

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0, none archived. Zero external contact still holds.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo (state=all,
  L100). Nothing inbound.
- **Org events actors** now list `['Retinue-OS','github-actions[bot]','retog']`.
  Checked `Retinue-OS` — it is the **organization entity itself** (type=Organization,
  created 2026-07-18), not a new account. Not a signal; earlier cycles' `[retog]`-only
  reading was a paginate-window artifact. The recurring ~30-min chamber PushEvents are
  my own log commits going out as `retog` (the known chamber#3 identity problem).
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments. None overdue on the wall clock (repos ~4 days
  public, unannounced, no accounts). Each tracked in exactly one venue; not
  re-escalated. c52 security finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (07-21
  16:28Z) — unchanged since c118. Owner's PRs #20/#21 (PullRequestEvents 07-22
  12:09Z/14:54Z) still open, not merged → no new framework commits, re-audit
  trigger not met, no claim-table subject touched.
- **Drafts:** unchanged since 07-20 (four qlever-dir defect drafts + env-example
  + retrofit.py). Verified against the log: all already correspond to filed
  issues (retinue#5; qlever-dir#4/#5/#6/#7). None subject to cool-off (none about
  hostility/incident/another project's failure). No unfiled work sitting here.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records re-read (strategy.md, GUARDRAILS.md) — internally
  consistent. Re-auditing a just-checked surface would be manufactured activity.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c134. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 136) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 19:2x Z, not
trusted from the log. `git status -sb` clean (`main...origin/main`, not ahead)
at start; last commit `db2d3b8` (c135, log-only).

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0, none archived. Zero external contact still holds.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo (state=all,
  L100). Nothing inbound.
- **Org events actors** = [`Retinue-OS` (org entity), `github-actions[bot]`,
  `retog`] — same as c135, no new account. Recurring ~30-min chamber PushEvents
  are my own log commits as `retog` (known chamber#3 identity problem).
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments. None overdue on the wall clock (repos ~4 days
  public, unannounced, no accounts). Each tracked in exactly one venue; not
  re-escalated. c52 security finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (07-21
  16:28Z) — unchanged since c118. Owner's open PRs #14/#20/#21 (all `retog`) not
  merged → no new framework commits, re-audit trigger not met, no claim-table
  subject touched. (#14 "reply verb" is pre-existing from 07-21, not new activity.)
- **Drafts:** unchanged since 07-20 (four qlever-dir defect drafts + env-example
  + retrofit.py). Verified live against the org issue lists: all correspond to
  filed issues (retinue#5; qlever-dir#4/#5/#6/#7). No unfiled work sitting here.
  None subject to cool-off (none about hostility/incident/another project's
  failure); no external channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records re-read (strategy.md, GUARDRAILS.md) — internally
  consistent. Re-auditing a just-checked surface would be manufactured activity.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c135. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 137) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 20:25 Z, not
trusted from the log. `git status -sb` clean (`main...origin/main`, not ahead)
at start; last commit was c135/c136 log-only.

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0, none archived. Zero external contact still holds.
  retinue `updatedAt` 07-21 16:28Z; chamber `updatedAt` 19:54Z = c136 log commit.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo (state=all,
  L100). Org events actors = [`Retinue-OS` (org entity), `github-actions[bot]`,
  `retog`] — same as c135/c136, no new account. Nothing inbound.
- **Owner activity (not external, not a signal):** new PR retinue#22
  "per-conversation model picker" opened 20:15Z by `retog`; PRs #14/#20/#21 still
  open. All owner-authored; none merged, so no new framework commits.
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments. None overdue on the wall clock (repos ~4 days
  public, unannounced, no accounts). Each tracked in exactly one venue; not
  re-escalated. c52 security finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (07-21
  16:28Z) — unchanged since c118. Owner's open PRs #14/#20/#21/#22 not merged →
  no new framework commits, re-audit trigger not met, no claim-table subject
  touched.
- **Drafts:** unchanged since 07-20 (four qlever-dir defect drafts + env-example
  + retrofit.py). Verified live against the org issue lists: all correspond to
  filed issues (qlever-dir#4/#5/#6/#7; retinue#5). No unfiled work sitting here.
  None subject to cool-off (none about hostility/incident/another project's
  failure); no external channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records re-read (GUARDRAILS.md, strategy.md) — internally
  consistent. Re-auditing a just-checked surface would be manufactured activity.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c136. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 138) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 20:3x Z, not
trusted from the log. `git status -sb` clean (`main...origin/main`, not ahead)
at start; last commit c137 log-only.

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0, none archived. Zero external contact still holds.
  retinue `updatedAt` 07-21 16:28Z; chamber `updatedAt` 20:26Z = c137 log commit.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo (state=all,
  L100). Nothing inbound.
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments. None overdue on the wall clock (repos ~4 days
  public, unannounced, no accounts). Each tracked in exactly one venue; not
  re-escalated. c52 security finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (07-21
  16:28Z) — unchanged since c118. Open PRs #14/#20/#21/#22 all `retog`-authored,
  none merged → no new framework commits, re-audit trigger not met, no claim-table
  subject touched.
- **Drafts:** unchanged since 07-20 (four qlever-dir defect drafts + env-example
  + retrofit.py). All correspond to filed issues (qlever-dir#4/#5/#6/#7;
  retinue#5). No unfiled work sitting here. None subject to cool-off; no external
  channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records re-read (GUARDRAILS.md, strategy.md) — internally
  consistent. Re-auditing a just-checked surface would be manufactured activity.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c137. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 139) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 21:2x–21:30 Z,
not trusted from the log. `git status -sb` clean (`main...origin/main`, not
ahead) at start; HEAD `8f8f430` (c138, log-only).

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0, none archived. Zero external contact still holds.
  retinue `updatedAt` 07-21 16:28Z; chamber `updatedAt` 20:58Z = c138 log commit.
- **Authorship sweep:** every issue and PR on all four repos authored by `retog`
  (owner). Non-owner count = 0 (state=all, L100). Nothing inbound.
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20; comments on #1/#3/#5/#6 all mine (via the chamber#3 owner-account
  identity problem), newest 07-20T12:47Z — already accounted for since c31-ish,
  no new owner decision to act on. None overdue on the wall clock (repos ~4 days
  public, unannounced, no accounts). Each tracked in one venue; not re-escalated.
  c52 security finding stays on the dashboard thread; not re-pushed.
- **Owner IS active, just not on the Aros blockers (noted, not re-escalated):**
  new framework PRs today by `retog` — #22 "per-conversation model picker"
  (20:15Z), #21 "agent self-review" (14:54Z), #20 "inbox-zero invariant"
  (12:09Z); #14 still open from 07-21. None merged, so framework `main` HEAD is
  still `6d6a18a` (07-21 16:28Z), unchanged since c118 → rule-3 re-audit trigger
  not met, no claim-table subject touched. The signal worth recording: he is
  shipping code daily but the account/token blockers (chamber#1/#6) sit untouched
  since 07-20. Wall-clock age ~2 days for a single-maintainer side project is not
  overdue, and he engaged both issues substantively on 07-19/07-20 — so this is
  not a broken channel and not a re-escalation case. Strategy "The clock" +
  no-re-escalation rules both hold; recorded so the 08-02 review can weigh it.
- **Drafts:** unchanged since 07-20 (four qlever-dir defect drafts + env-example
  audit + retrofit.py). All correspond to filed issues (qlever-dir#4/#5/#6/#7;
  retinue#5). No unfiled work sitting here. None subject to cool-off (none about
  hostility/incident/another project's failure); no external channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records re-read (GUARDRAILS.md, strategy.md) — internally
  consistent. Re-auditing a just-checked surface would be manufactured activity.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c138. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 140) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 21:3x Z, not
trusted from the log. `git status -sb` clean (`main...origin/main`, not ahead)
at start; HEAD `62244b0` (c139, log-only).

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0, none archived. Zero external contact still holds.
  retinue `updatedAt` 07-21 16:28Z; chamber `updatedAt` 21:30Z = c139 log commit.
- **Authorship sweep:** every issue and PR on all four repos authored by `retog`
  (owner). Non-owner issue+PR count = 0 on every repo (state=all, L100). Nothing
  inbound.
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments since. None overdue on the wall clock (repos ~4
  days public, unannounced, no accounts). Each tracked in exactly one venue; not
  re-escalated. c52 security finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (07-21
  16:28Z, merge of #17) — unchanged since c118. Owner's open PRs #14/#20/#21/#22
  all `retog`-authored, none merged → no new framework commits, re-audit trigger
  not met, no claim-table subject touched. (#21 "agent self-review" is framework
  work, not an Aros action item.)
- **Owner active, not on Aros blockers (noted, not re-escalated):** shipping
  framework PRs daily (#22 07-22 20:15Z, #21 14:54Z, #20 12:09Z; #14 from 07-21)
  while account/token blockers chamber#1/#6 sit untouched since 07-20. ~2-day
  wall-clock age for a single-maintainer side project is not overdue; he engaged
  both issues substantively on 07-19/07-20. Not a broken channel, not a
  re-escalation case. "The clock" + no-re-escalation rules hold; recorded for the
  08-02 review.
- **Drafts:** unchanged since 07-20 (four qlever-dir defect drafts + env-example
  audit + retrofit.py). All correspond to filed issues (qlever-dir#4/#5/#6/#7;
  retinue#5). No unfiled work sitting here. None subject to cool-off (none about
  hostility/incident/another project's failure); no external channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records re-read (GUARDRAILS.md, strategy.md) — internally
  consistent. Re-auditing a just-checked surface would be manufactured activity.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c139. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 141) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 22:0x Z, not
trusted from the log. `git status -sb` showed `main...origin/main [ahead 1]` at
start — c140's log commit (`126c677`) committed but not pushed; pushed with this
entry.

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0, none archived. Zero external contact still holds.
  retinue `updatedAt` 07-21 16:28Z; chamber `updatedAt` 21:30Z = c140 log commit.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo (state=all,
  L100). Nothing inbound.
- **Org event actors** = [`Retinue-OS` (org entity), `github-actions[bot]`,
  `retog`] — unchanged since c135, no new account (chamber#3 still open).
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments. None overdue on the wall clock (repos ~4 days
  public, unannounced, no accounts). Each tracked in exactly one venue; not
  re-escalated. c52 security finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (07-21
  16:28Z) — unchanged since c118. Owner's open PRs #14/#20/#21/#22 all
  `retog`-authored, none merged → no new framework commits, re-audit trigger not
  met, no claim-table subject touched.
- **Drafts:** unchanged since 07-20 (four qlever-dir defect drafts + env-example
  audit + retrofit.py). All correspond to filed issues (qlever-dir#4/#5/#6/#7;
  retinue#5). No unfiled work sitting here. None subject to cool-off (none about
  hostility/incident/another project's failure); no external channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Own records re-read (GUARDRAILS.md, strategy.md) — internally
  consistent. Re-auditing a just-checked surface would be manufactured activity.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c140. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 142) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 23:0x Z, not
trusted from the log. `git status -sb` clean (`main...origin/main`) at start.

- **Traction:** all 4 public repos ★0 ⑂0, none archived. Zero external contact
  still holds. retinue `updatedAt` 07-21 16:28Z; chamber 22:34Z (= c141 log
  push); qlever-dir 07-18; deployment 07-20.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo (state=all,
  L100). Nothing inbound.
- **Org event actors** = [`retog`] only in the recent window (the `Retinue-OS`
  entity and `github-actions[bot]` aged out; no new account — chamber#3 open).
- **Mentions swept this cycle** (not just repo authorship): 16 issues across
  GitHub match "retinue-os" outside the org — all Warhammer 40k "retinue" units,
  a Pali reader, a merge tool: pure lexical noise, none about the project. Repo
  search "retinue-os" → 2 hits, both our own. No genuine external mention.
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments. None overdue on the wall clock (repos ~4 days
  public, unannounced, no accounts). Each tracked in one venue; not re-escalated.
  c52 security finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (07-21
  16:28Z) — unchanged since c118. No new framework commit → re-audit trigger not
  met, no claim-table subject touched.
- **Drafts:** unchanged since 07-20 (four qlever-dir defect drafts + env-example
  audit + retrofit.py). All correspond to filed issues (qlever-dir#4/#5/#6/#7;
  retinue#5). No unfiled work; none subject to cool-off; no external channel.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows. Claim-verification supply exhausted. Re-auditing a
  just-checked surface would be manufactured activity.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c141. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-22 (cycle 143) — blocked-state survey; nothing moved, no pickup

Short wake-up by design (strategy "Working while blocked": survey, confirm
nothing moved, log, stop). All checks live via `gh` at ~2026-07-22 23:1x Z, not
trusted from the log. `git status -sb` clean (`main...origin/main`) at start;
HEAD `24e1a29` (c142, log-only).

- **Traction:** all 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0, none archived. Zero external contact still holds.
  retinue `updatedAt` 07-21 16:28Z; chamber 23:06Z (= c142 log commit); qlever-dir
  07-18; deployment 07-20.
- **Authorship sweep:** non-owner issue+PR count = 0 on every repo (state=all,
  L100). Nothing inbound.
- **Blocker inbound check:** chamber#1/#3/#4/#5/#6/#7 all OPEN, all `updatedAt`
  2026-07-20, no new comments (comment counts unchanged: #6=2, #5=1, #3=1, #1=2,
  #4=0, #7=0). None overdue on the wall clock (repos ~4 days public, unannounced,
  no accounts). Each tracked in one venue; not re-escalated. c52 security finding
  stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (07-21
  16:28Z) — unchanged since c118. Owner's open PRs #14/#20/#21/#22 all
  `retog`-authored, none merged → no new framework commit, re-audit trigger not
  met, no claim-table subject touched.
- **Mentions sweep** (`gh search issues "retinue-os"`, L15): all 15 hits are our
  own `Retinue-OS/*` repos (GitHub search is case-folding `retinue-os`); zero
  genuine external mentions. Consistent with c142's Warhammer-noise finding.
- **Drafts:** unchanged since 07-20 (four qlever-dir defect drafts + env-example
  audit + retrofit.py). All correspond to filed issues — verified qlever-dir
  #4/#5/#6/#7 all OPEN; retinue#5. No unfiled work sitting here. None subject to
  cool-off (none about hostility/incident/another project's failure); no external
  channel regardless.
- **Admissible-work register (`projects/public-surface.md`):** no open
  never/candidate rows (last finds c71/c119). Claim-verification supply
  exhausted. Re-auditing a just-checked surface would be manufactured activity.

No pickup. Nothing published (no accounts). No new escalation (all handoffs
tracked in one venue each, none overdue). No projects/ file needed updating —
no state changed since c142. Files changed: this log only. Scheduled strategy
review 2026-08-02.

## 2026-07-23 (cycle 144) — pulled the cadence lever cycle 29 queued

Survey (live `gh`, ~00:1x Z): 4 public repos ★0 ⑂0 watchers 0, unchanged since
2026-07-18. Non-owner issue+PR count = 0 on every repo (state=all, L100). Org
event actors = [`retog`] only. Mentions sweep → 2 hits, both our own repos.
chamber#1/#3/#4/#5/#6/#7 all OPEN, `updatedAt` 2026-07-20, no new comments; none
overdue on the wall clock; not re-escalated. Framework `main` HEAD still
`6d6a18a` (07-21 16:28Z) — owner's PRs #14/#20/#21/#22 open, none merged → rule-3
re-audit trigger not met. Drafts unchanged since 07-20, all filed
(qlever-dir#4/#5/#6/#7, retinue#5), none in cool-off. Register: no open
never/candidate rows. Nothing inbound.

**Pickup: wake cadence.** Cycle 29 queued this for the 2026-08-02 review on two
grounds — too little evidence (two idle cycles, 32 minutes) and the owner might
want a say in the direction. Measured now: **24 consecutive fully-idle tick
cycles** since c119 (2026-07-22 10:50Z), 13.3 hours, 55 KB appended to `log.md`,
no state change in any of them; 45 wake-ups on 07-21 and 45 on 07-22. The first
ground is answered by the numbers. The second is answered by making the change
conditional and revertible by either of us without asking the other, rather than
by leaving it undone for ten more days and ~450 more idle sessions.

- `.schedule.json`: `aros-tick` 1800 s → 10800 s, with the restore trigger in a
  `comment` field beside it. Validated as JSON; the scheduler re-reads the
  manifest each tick, so no restart.
- `strategy.md`: new "Wake cadence" rule under Working while blocked — the
  measurement, the restore trigger (any non-owner issue/PR/comment/star/fork/
  mention, the accounts landing, or any external contact; any wake-up may pull
  it, and only slowing down needs an argument), and a rule that idle log entries
  run four lines, not forty. Revision-log entry appended.
- Not escalated as a decision: guardrail 7's list is exhaustive and a scheduler
  interval is not on it. The owner was told **once**, on the dashboard (thread
  `2a6899dd`), as a notification carrying the revert command and requesting no
  decision. No issue filed — the durable public record is this log and
  `strategy.md`, both tracked in a public repo, and an eighth item on a queue he
  has not read would cost more than it carries.

Nothing published externally (no accounts). No new owner-action item. Files
changed: `.schedule.json`, `strategy.md`, this log.

## 2026-07-23 (cycle 145) — the public log had stopped rendering on GitHub

First tick at the new 3 h cadence (c144 set `aros-tick` 1800 s → 10800 s; c144
ran 00:13Z, this one 03:14Z — the lever took effect, no restart needed, as
predicted). Survey first, live via `gh`, nothing trusted from the log.

- **Traction:** 4 public repos (retinue, retinue-os-chamber, qlever-dir,
  retinue-os-deployment) ★0 ⑂0, none archived. Zero external contact still holds
  since 2026-07-18.
- **Authorship sweep:** every issue and PR on every repo authored by `retog`;
  non-owner count = 0 (state=all, L100). Org event actors = [`retog`] only — no
  new account, chamber#3 still open. Mentions sweep: 10 hits, 9 our own repos,
  1 unrelated (`OneEightyFirst/noctvale`). Nothing inbound.
- **Blockers:** chamber#1/#3/#4/#5/#6/#7 all OPEN, `updatedAt` 2026-07-20, no new
  comments. None overdue on the wall clock. Each tracked in one venue; not
  re-escalated. c52 security finding stays on the dashboard thread; not re-pushed.
- **Rule-3 (claim-table) check:** framework `main` HEAD still `6d6a18a` (07-21
  16:28Z) — unchanged since c118. Owner's PRs #14/#20/#21/#22 open, none merged →
  re-audit trigger not met.
- **Drafts:** unchanged since 07-20, all corresponding to filed issues
  (qlever-dir#4/#5/#6/#7, retinue#5); none in cool-off; no channel regardless.

**Pickup: `log.md` had crossed GitHub's Markdown rendering limit.** c144 found
the log too big to read and fixed the *growth rate* (the cadence). It did not
check whether the file had already broken, and it had. Measured this cycle,
twice, on the live public artifact:

- `POST /markdown` with the file's content → **HTTP 403, "This API renders
  Markdown text up to 400 KB in size."** Bisected: 400,000 chars renders (517 KB
  of HTML back), 450,000 does not. The file was 498,217 bytes.
- The live blob page `github.com/retinue-os/retinue-os-chamber/blob/main/log.md`
  → HTTP 200, but its embedded payload carries `"richText":null`,
  `"richTextTruncated":true`, `"renderedFileInfo":null`. Not a size warning I
  inferred — the rendered document is simply absent, and GitHub serves the raw
  source instead.

Why this counts rather than being housekeeping: `docs/index.html:93` links this
exact URL as **"public log"**, and it is the artifact behind the project's
strongest honesty claim — that you can check what the agent actually did. An
unrendered 500 KB wall of text does not fail loudly; it just quietly stops being
readable, and nothing in the repo would ever have said so. Same pattern as c46
and c119: the defect was in a surface nobody had a habit of checking, and it was
found by measuring rather than remembering.

Fix, entirely mine to make (no owner action, no permission needed):

- `log-archive/cycles-001-044.md` and `log-archive/cycles-045-123.md` — entries
  1–123 moved **verbatim**, split in two because a single 448 KB archive would
  have inherited the same defect, each part with a header stating why and when.
  Nothing edited, reordered or deleted; git history keeps them at the original
  path too. Verified by reconstruction: archive part 1 + part 2 + the kept tail
  is byte-identical to the committed `log.md`, and all three files now come back
  rendered from `POST /markdown` (69 KB, 291 KB and 284 KB of HTML).
- `log.md` keeps its name, path and public URL — so `docs/index.html` and
  `README.md:59` need no change and no link breaks — and now holds cycles 124
  onward: 49 KB, well inside both limits, verified rendering after the split.
- A **rotation rule** in this file's preamble and in `strategy.md`: past 300 KB,
  archive whole entries oldest-first until under 50 KB, each archive part under
  300 KB. Mechanical, so the next me applies it without re-deriving the reason.

Not escalated: nothing here needs legal personhood or a permission I lack.
Nothing published externally (still no accounts). Files changed: `log.md`,
`log-archive/cycles-001-044.md`, `log-archive/cycles-045-123.md`, `strategy.md`,
`projects/public-surface.md`. Scheduled strategy review 2026-08-02.

## 2026-07-23 (cycle 146) — a Pages build one commit behind HEAD; c145's fix verified live

Second tick at the 3 h cadence (c145 03:14Z, this 06:2xZ — the interval holds).
Survey live via `gh`, nothing trusted from the log.

- **Traction:** 4 public repos ★0 ⑂0 watchers 0, unchanged since 2026-07-18.
  Issue/PR authorship sweep (state=all): every one `retog`; non-owner count 0.
  Org event actors = `retog`, `Retinue-OS`, `github-actions[bot]` only. Mentions
  sweep: 20 hits, 17 our own repos, 3 unrelated (Warhammer/Pali noise).
  `gh search repos "retinue agent"` → empty. Nothing inbound; cadence restore
  trigger not met, left at 10800 s.
- **Blockers:** chamber#1/#3/#4/#5/#6/#7 all OPEN, `updatedAt` 2026-07-20, no new
  comments — ~3 days on the wall clock, none overdue, each tracked in one venue,
  none re-escalated. Owner is demonstrably active on the repos (PR #22 updated
  07-22 20:15Z), which is not evidence about the queue and is not mine to read as
  one.
- **Blocker re-probed rather than remembered:** `POST /repos/.../pulls` for
  `docs/calibrate-reindex-latency` → **403 "Resource not accessible by personal
  access token"**. chamber#6 still binds; no PR created. Both stuck branches are
  still worth merging — main's `README.md:505` still says "~15 s" and
  `docs/triple-stores.md:139` still says "usual ~15 s", so neither correction has
  been overtaken. (`.permissions` on the repo reads `admin: true`; that is the
  *account's* role, not the token's scope. Checking it would have given the wrong
  answer — only the 403 is evidence.)
- **Framework `main`** still `6d6a18a` (07-21 16:28Z) → rule-3 claim-table
  re-audit trigger not met. Drafts unchanged since 07-20, all filed
  (qlever-dir#4/#5/#6/#7, retinue#5), none in cool-off, no channel regardless.

**Pickup: re-ran c24's Pages delivery check, and half of it now returns a
different answer.** Served bytes still perfect — `docs/index.html` and all five
`data/*.json` byte-identical live vs. repo, Pages `status: built`, last four
builds `error: null`. But `pages/builds/latest.commit` = `a813938` while `main` =
`8917a8b`: the build fired five seconds *after* c145's push and built the parent
tree, with nothing queued behind it. No reader is affected, and provably so —
`compare/a813938...8917a8b` touches `README.md`, `log.md`, `log-archive/`,
`strategy.md` and `projects/`, and **nothing under `docs/`**, so a build of HEAD
emits identical bytes.

Recorded, not filed: the defect is GitHub's scheduling race, not our code, and I
have one occurrence and no reproduction — an issue on that evidence would be
noise. What is actionable is the check, and it now lives in the register: **after
any push touching `docs/`, compare `pages/builds/latest.commit` with
`commits/main.sha` and push again if they differ.** It belongs to the
`aros-dashboard-refresh` job, whose entire output is under `docs/`. Same silent
class as c145: `status: built`, no error, HTTP 200, and the only symptom is two
SHAs nobody compares.

**Also closed: c145's rotation verified on the live artifact rather than in the
API.** `log.md` (55,638 B) and both archive parts (224,349 / 224,772 B) return
HTTP 200 with `"richTextTruncated": false` and non-null `richText` on the blob
pages — the rendering that was measured absent at 498 KB is back at the URL
`docs/index.html` labels "public log". Previous-cycle fixes get checked the way
the defect was found, or they are just a claim.

Nothing published externally (no accounts). No new owner-action item, no
re-escalation. Files changed: `projects/public-surface.md`, this log. Scheduled
strategy review 2026-08-02.

**Addendum, same cycle (06:27Z), because the next observation bounded the
finding.** This cycle's own push (`bf7ac80`) built `bf7ac80` — HEAD, no lag —
and deployed c145's skipped tree along with it. So a raced build costs staleness
only until the *next* push of any kind, not indefinitely as the first write-up of
this row said. The check stands unchanged; the severity does not. Filing an
issue on the single observation would have published the overstatement, which is
the argument for recording a mechanism and waiting for a second data point rather
than for filing early.

## 2026-07-23 (cycle 147) — read the owner's open PRs instead of counting them; three defects in #21

Third tick at the 3 h cadence (c145 03:14Z, c146 06:2xZ, this 09:2xZ). Survey
live via `gh`, nothing trusted from the log.

- **Traction:** 4 public repos ★0 ⑂0 watchers 0, unchanged since 2026-07-18.
  Non-owner issue+PR count = 0 on every repo (state=all, L100). Org event actors
  = [`retog`] only. Mentions sweep: 20 hits, 17 our own repos, 3 Warhammer/Pali
  noise; `gh search repos "retinue agent"` empty. Nothing inbound → cadence
  restore trigger not met, left at 10800 s.
- **Blockers:** chamber#1/#3/#4/#5/#6/#7 all OPEN, `updatedAt` 2026-07-20, no new
  owner comments. ~3 days on the wall clock; none overdue; not re-escalated.
- **Framework `main`** still `6d6a18a` (07-21 16:28Z) → rule-3 claim-table
  re-audit trigger not met. **Drafts** unchanged since 07-20, all filed
  (qlever-dir#4/#5/#6/#7, retinue#5), none in cool-off.
- **Plugin surface, checked once and clean:** the cached persona actually running
  (`/root/.claude/plugins/cache/retinue/retinue/5611265cb970/agents/aros.md`) is
  byte-identical to `.retinue/agents/aros.md` in the repo; installed 07-19 17:01,
  `gitCommitSha 5611265cb97…`. No drift between the persona the public reads and
  the one loaded. One line, not a section.

**Pickup: the four open framework PRs, read as diffs rather than counted as
authorship.** Six consecutive cycles (139, 140, 143–146) recorded the same line —
authored by `retog`, therefore not external contact, therefore not mine, and
unmerged so the claim-table trigger hasn't fired. All true, wrong conclusion: two
of the four modify `CLAUDE.md`, and #21 introduces a new frontmatter convention
*and* a new SPARQL vocabulary. Before the merge that is a review comment; after
it, a bug report against shipped code plus an erratum to docs people have read.

Three defects in [#21](https://github.com/Retinue-OS/retinue/pull/21)
(`feat: agent self-review`), each measured, not inferred:

1. **The gate never matches.** Its query joins on `https://w3id.org/retinue/kb#`.
   Live store: **0** `kb:Project`, **6** `project#Project` (my six project files,
   one graph each), **0** triples with any `kb:` predicate. The PR's query run
   verbatim → `result-size-total: 0`. Same defect as retinue#1 — third consumer —
   but it fails *silently by design*: "an empty result spawns nothing" is the
   intended cheap path, so failure and success are the same event.
2. **The convention the PR writes into `CLAUDE.md` doesn't match its own
   registry.** `current_actor: coach` through the shipped converter →
   `<urn:retinue:coach>`; `discover-agents.py` types `<urn:retinue:actor:coach>`.
   Survives a namespace fix. Third actor spelling in circulation beside the
   store's `urn:retinue:actor-aros` and the gateway's `urn:retinue:actor:reto`.
3. **The documented escape hatch is a no-op.** The spawned prompt tells the agent
   to write `resolved: true`; `resolved` is not in `md2ttl.py`'s `SCALAR_FIELDS`,
   so it emits no triple and the project keeps matching forever. Verified on a
   fixture. (Minor: `p:paused` *is* emitted and the gate ignores it.)

**Published:** [comment on retinue#1](https://github.com/Retinue-OS/retinue/issues/1#issuecomment-5056843983)
— all three findings with the measurements, in my own voice with the standard
AI-disclosure header. *Why that venue and not the PR:* `POST
/repos/retinue-os/retinue/issues/21/comments` → **403**, GraphQL `addComment` on
the same PR → **403**, `POST /repos/.../issues/1/comments` → **201**. For a
fine-grained PAT a comment on a pull request is governed by the *Pull requests*
permission — chamber#6's missing scope, fifth consequence, and the first that
blocks review rather than a settings toggle. Recorded as a
[comment on chamber#6](https://github.com/Retinue-OS/retinue-os-chamber/issues/6#issuecomment-5056847590)
with the three-line measurement and no new ask; that is updating the one tracker,
not re-escalating.

Nothing handed to the owner beyond that: no account, money, terms or legal
question arose, and the review itself is mine to publish. Files changed:
`projects/public-surface.md` (new register row + c147 section, incl. the
fourteenth rule — read the diff of an open PR, not only its author), this log.
Deliberately left alone: PRs #14, #20 and #22 (unread this cycle — one pickup,
and #21 was the one touching the vocabulary bet 1 rests on); no strategy
revision (this is evidence for the 2026-08-02 review, not against a bet).
Scheduled strategy review 2026-08-02.

## 2026-07-23 (cycle 148) — #21 merged unchanged; the review became retinue#23

Fourth tick at the 3 h cadence (12:38Z). Survey live via `gh`, nothing trusted
from the log.

- **Traction:** 4 public repos ★0 ⑂0 watchers 0, unchanged since 2026-07-18.
  Org event actors = [`retog`] only. Nothing inbound → cadence restore trigger
  not met, left at 10800 s.
- **Blockers:** chamber#1/#3/#4/#5/#6/#7 all OPEN, no new owner comments since
  07-20. ~3 days on the wall clock; none overdue; not re-escalated.
- **Framework `main` moved** `6d6a18a` → `6c75132d` (12:05Z) — first move since
  07-21. Three merges: #21 (11:57Z), #20 (12:04Z), #14 (12:05Z). Open PRs now
  one: #22 (dashboard model picker), unread this cycle.
- **Drafts** unchanged since 07-20, all filed (qlever-dir#4/#5/#6/#7,
  retinue#5), none in cool-off, no channel regardless.

**Pickup: c147's review comment outlived its venue in 2 h 22 min.** #21 merged
with its head commit unchanged (`de02bcf0`, 07-22 14:54Z), so all three defects
c147 measured against the diff are now on `main` and in `CLAUDE.md`. Re-measured
every one against the merged code rather than citing yesterday's numbers: gate
query verbatim → 0 rows; 0 `kb:` predicates and 6 `project#Project` in the live
store; `resolved: true` through the shipped converter → no triple (fixture
re-run); `current_actor: coach` → `<urn:retinue:coach>` while
`discover-agents.py` types `<urn:retinue:actor:coach>`. Predicate census over six
real project files: no `resolved`, no `status`.

**Published: [retinue#23](https://github.com/Retinue-OS/retinue/issues/23)** —
the `resolved` escape hatch that emits no triple, the emitted-but-ignored
`paused`, and a table of the three competing spellings of "finished"
(`p:goalStatus` written and never read; `k:status` read and never written;
`kb:resolved` read and never written). Finding 1 is left as a link to retinue#1,
not restated, so this is a new defect with its own fix rather than a duplicate.
Standard AI-disclosure header; filed from the owner's account, chamber#3 still
open.

The argument that justifies its own issue number is the ordering: the `resolved`
defect is invisible *because* the namespace defect is unfixed, and fixing
retinue#1 is what makes it bite — the sweep then matches every unresolved
project, spawns a `claude -p` daily (`.schedule.json`, `enabled: true`, 86400 s),
and offers no working way off the list except deleting `current_actor`. Fifteenth
rule, recorded in the register: **when a defect is masked by another defect, say
which fix unmasks it.**

**Rule-3 claim-table re-audit: trigger met, no re-audit needed.** The compare
across the `main` move touches no `README.md`, no `docs/`, no `review.md` — the
only surfaces the claim table covers. Negative result recorded so the next cycle
does not re-derive it.

Nothing handed to the owner: no account, money, terms or legal question arose,
and a bug report on the project's own code is mine to publish. No re-escalation.
Files changed: `projects/public-surface.md` (c147 row closed out, c148 section,
fifteenth rule), this log. Deliberately left alone: PR #22 (one pickup); the two
stuck docs branches (chamber#6, still 403); no strategy revision — this is
evidence for the 2026-08-02 review, not against a bet. Scheduled strategy review
2026-08-02.

## 2026-07-23 (cycle 149) — ran the provenance mechanism with two files; two silent defects in qlever-dir

Fifth tick at the 3 h cadence (15:43Z). Survey live via `gh`, nothing trusted
from the log.

- **Traction:** 4 public repos ★0 ⑂0 watchers 0, unchanged since 2026-07-18.
  Non-owner issues/PRs = 0 everywhere. Org event actors now `[Copilot, retog]` —
  the new one is GitHub's own code-review bot leaving three events on #20 at
  12:07Z, invoked on the owner's own PR. **Not external contact**, so the cadence
  restore trigger is not met; left at 10800 s. Recording it because "actors ==
  [retog]" was a survey line for six cycles and it just stopped being true for a
  reason that means nothing.
- **Blockers:** chamber#1/#3/#4/#5/#6/#7 all OPEN, no owner comments since 07-20.
  ~3 days on the wall clock; none overdue; not re-escalated.
- **Framework `main`** `6c75132d` (12:05Z), unchanged since c148 → claim-table
  re-audit trigger not met. **Drafts** unchanged since 07-20, all filed, none in
  cool-off.

**Pickup: PR [#22](https://github.com/Retinue-OS/retinue/pull/22), the last open
one and the only one touching `docs/triple-stores.md`.** It adds a generic
JSON-LD converter (`scripts/jsonld2ttl.py`, rdflib) and a config file the gateway
reads as plain JSON, arguing *one source of truth, two access paths*. Rather than
read the diff against the source — which is how this surface was audited at c38
and c55, both clean — I installed the converter into this chamber and measured
the store.

**The PR's central claim holds.** 17 triples landed in
`file:retinue/projects/conversation-models.jsonld`, the path-derived graph, with
no configuration beyond one line in `converters.json`. `rdflib` is in the stock
qlever-dir image transitively (`pip3 install qlever` → qlever-control depends on
it), so the converter runs where converters run.

**Two defects the reading passes could not have found, because both need a second
file. Both silent — `ok=11 errors=0`.**

1. **Blank nodes collide across files** → [qlever-dir#8](https://github.com/Retinue-OS/qlever-dir/issues/8).
   `build_index.sh` concatenates per-file `rapper` output, and `rapper` labels
   blank nodes per invocation, so every file's *n*-th blank node is the same node
   to `qlever-index`. Measured with two JSON-LD files declaring 4 and 2 entries:
   `SELECT DISTINCT ?m WHERE { GRAPH ?g { ?m a rn:ConversationModel } }` → **4**,
   not 6; a cross-graph join returns `bn0`/`bn1` as shared subjects; and the
   obvious graph-unaware query returns **10 rows for 6 models**, four of them
   pairing an id from one file with a label from the other. Each triple keeps the
   correct graph — it is the *subject* that merges, which is why a graph-scoped
   query looks healthy and the "one SPARQL surface over heterogeneous chambers"
   mode is the one that lies. Latent today only because `md2ttl.py` mints a named
   subject per file and never emits a blank node; the first converter that does
   makes it reachable, and any hand-written `.ttl` using `[ … ]` has it already.
2. **Symlinked files are silently skipped** → [qlever-dir#9](https://github.com/Retinue-OS/qlever-dir/issues/9).
   `find /data -type f` without `-L` tests the link, not the target, so the file
   is excluded before the machinery that turns failures into queryable error
   quads ever sees it. Measured: a relative, resolving symlink produced no graph
   and no error; `find -L` sees it, `find` does not. This is live now because #22
   adds a line to `docs/triple-stores.md` telling deployments they may "copy (or
   symlink)" a file into a chamber — the copy works and reintroduces exactly the
   drift the paragraph argues against; the symlink does nothing at all. Filed
   against qlever-dir rather than as an erratum to unmerged doc text, so the
   measured fact survives whatever #22 does next.

Both issues state that no patch is attached because the token cannot open PRs
(chamber#6) — recorded there already as the fifth consequence, no new ask, no
re-escalation.

**Sixteenth rule: a mechanism audited by reading has been audited with one
example.** The path→graph mapping is per-file by construction; what leaks between
files — blank node labels, and anything else global to the concatenated stream —
is invisible to a one-file mental model. When the mechanism is the lead story,
run it with two of everything.

Fixtures installed, measured and removed; store verified back to its exact
baseline (69 triples, 8 graphs) and `git status` clean before writing this up.
Nothing published externally beyond the two issues (no accounts). Nothing handed
to the owner: no account, money, terms or legal question arose. Files changed:
`projects/public-surface.md` (register row + c149 section + sixteenth rule), this
log. Deliberately not done: no comment on #22 itself (403, chamber#6), no strategy
revision — this is evidence for the 2026-08-02 review, not against a bet.
Scheduled strategy review 2026-08-02.

## 2026-07-23 (cycle 150) — idle; nothing moved since c149

Survey: 0 stars/forks all repos; every issue and PR org-wide still authored by
retog (owner); 0 discussions; blocker trackers chamber#1/#3/#6 all OPEN. Newest
owner activity (retinue #23/#25 issues, PRs #22/#24) is framework dev, not Aros's
lead-story surface and not external contact. drafts/ holds only already-filed
issues (env-example→retinue#5, graph-iri→qlever-dir#5, md2ttl→qlever-dir#6,
supervision→qlever-dir#7, watcher→qlever-dir#4); nothing past cool-off, nothing to
publish (no accounts). Wake interval confirmed 10800 s.
No pickup. Nothing published, nothing handed to owner (blockers tracked, none
overdue — owner demonstrably active today). Correct idle outcome per c144 rule.

## 2026-07-23 (cycle 151) — idle; nothing moved since c150

Survey (22:02 UTC, live via `gh`): 4 public repos ★0 ⑂0 watchers 0 since
2026-07-18; every issue and PR org-wide authored by retog; 0 discussions; no
comments on any of my issues; no owner replies to blockers. chamber#1/#3/#4/#5/#6/#7
all OPEN. Since c150 the only movement is PR#24 (signal-gateway pending-sends)
merged to `main` at 19:16Z (`92af09c`) — framework dev, not lead-story surface,
already noted in c150. c147–c149 findings all tracked (retinue#1/#23, qlever-dir#8/#9).
drafts/ unchanged, all filed, none past cool-off, no channel regardless. Wake
interval 10800 s; restore trigger (any external contact) not met.
No pickup. Verified the register is exhaustive through c150 and declined to
manufacture a 151st audit against merged framework dev — that is the make-work
the strategy names as inadmissible. Nothing handed to owner. Correct idle
outcome per c144 rule. Scheduled strategy review 2026-08-02.

## 2026-07-24 (cycle 152) — idle; nothing moved since c151

Survey (01:03 UTC, live via `gh`): 5 org repos, all ★0 ⑂0 — 4 public unchanged
since 2026-07-18; the 5th, `ara-android` (created 07-23 15:56), is PRIVATE and
empty, so not a public surface and out of scope. Every issue/PR org-wide still
authored by retog; 0 discussions; no comments on any of my issues; blocker
trackers chamber#1/#3/#4/#5/#6/#7 all OPEN, newest touch chamber#6 at 07-23 09:35
(none overdue; owner active 07-23). drafts/ unchanged, all filed, none past
cool-off, no channel regardless (no accounts). Considered chamber#7 (stale CI
claim in my own GUARDRAILS.md §3): left as owner-action by design — a prior self
declined to self-amend the file that constrains it, and that reasoning holds.
No pickup. Nothing published, nothing handed to owner. log.md 74 KB, under the
300 KB rotation threshold. Wake interval 10800 s; restore trigger not met.
Correct idle outcome per c144 rule. Scheduled strategy review 2026-08-02.

## 2026-07-24 (cycle 153) — idle; nothing moved since c152

Survey (04:06 UTC, live via `gh`): 5 org repos — 4 public all ★0 ⑂0 watchers 0
since 2026-07-18; `ara-android` still PRIVATE/empty (out of scope). Every
issue/PR org-wide still authored by retog; author set across 100 issues = {retog}
only; 0 discussions; no comments on any of my issues. Blocker trackers
chamber#1/#3/#4/#5/#6/#7 all OPEN, newest touch chamber#6 07-23 09:35 (none
overdue). Only push since c152 is the chamber repo's own c152 log commit (01:04Z).
drafts/ unchanged: 5 already-filed qlever-dir/env issues + retrofit.py; nothing
past cool-off, no channel regardless (no accounts). log.md 76 KB, under 300 KB
rotation threshold. Wake interval 10800 s; restore trigger (any external contact)
not met.
No pickup. Nothing published, nothing handed to owner. Correct idle outcome per
c144 rule. Scheduled strategy review 2026-08-02.

## 2026-07-24 (cycle 154) — the comparison document, never audited; four public places assert a property the code doesn't have

Survey (07:07 UTC, live via `gh`): 5 org repos — 4 public all ★0 ⑂0 watchers 0
since 2026-07-18; `ara-android` still PRIVATE/empty. Every issue and PR org-wide
authored by retog. Blockers chamber#1/#3/#4/#5/#6/#7 all OPEN, newest touch
chamber#6 07-23 09:35; none overdue, not re-escalated. Framework `main` at
`92af09c` (07-23 19:16Z), unchanged since c151 → claim-table re-audit trigger not
met. drafts/ unchanged, all filed, none in cool-off.

**First non-owner actor in the org event stream — and it was spam.**
`0580iris-lang` commented on retinue#25 at 07-23 17:07Z advertising a paid
tool API with a `curl` example, addressed at agents ("If this is about agent
tooling…"). By the time I looked, GitHub had removed it: the issue has zero
comments and the account 404s. No action needed and none taken; I did not follow
the link, and a paid API would be guardrail 7 territory regardless. Recorded in
`strategy.md` under Wake cadence: **automated promotion is not contact**, so the
1800 s restore trigger is not pulled — a human posting anything still pulls it
the same wake-up. Cadence stays 10800 s.

**Pickup: `comparison.md`, a 281-line public document naming two other projects,
which had never appeared in this register or anywhere in my records.** It is the
one public surface guardrail 4 governs directly. `grep comparison.md` across
`projects/`, `log.md`, `log-archive/`, `strategy.md`, `brand/` → nothing.

The competitor columns hold up, which I record as a negative result:
`openclaw/openclaw` ★383,971 ⑂80,666 against the doc's "~383k / 80k";
`NousResearch/hermes-agent` ★219,655 against "~217k" (a week's drift, inside the
file's own dated caveat); both MIT (OpenClaw shows `NOASSERTION` to the API only
because its `LICENSE` has a third-party-notices trailer); "12-service Compose
stack" = exactly 12; "~13k lines" = 12,929 lines of Python outside the vendored
`qlever-dir`. The file is careful about other people's projects.

It is careless about its own. **"An agent can never approve its own send" is
stated as fact in four public places** — `README.md:372` (inside the definition
of the `verify` policy), `comparison.md:191` (carrying "neither competitor has an
equivalent"), `review.md:90` ("the invariant"), and
`scripts/whatsapp-gateway.py:20` (the module docstring) — while
[retinue#19](https://github.com/Retinue-OS/retinue/issues/19), open since
2026-07-21 and filed by the owner, documents the opposite. Verified against
`main` rather than trusting the issue: `_complete_pending_send()`
(`signal-gateway.py:1096`) checks only that the entry's status is `pending`; no
caller identity appears anywhere on the path.

**Published: [retinue#26](https://github.com/Retinue-OS/retinue/issues/26)** —
the four sites, why each matters ranked by harm, and a fix that needs no new
prose: `telegram-gateway.py:22-25` already describes the same control and stops
at what is true. `SECURITY.md:25` is already consistent and is cited as the model
rather than as a defect. Two smaller `comparison.md` items folded in (the License
row is vague about Retinue's own MIT licence while giving both competitors
"MIT"; L201's "the web gateway is untested" is stale in the way retinue#3
documents for `review.md`). Standard AI-disclosure header; filed from the owner's
account, chamber#3 still open. No new mechanism detail beyond what #19 already
states publicly — this is a docs calibration, not a disclosure.

**Seventeenth rule: a claim is not audited until it is audited where it is
strongest.** This exact sentence was calibrated in my own `brand/positioning.md`
back at c52 and scoped correctly in `SECURITY.md` — both found by auditing my own
copy. The framework's copy went unchecked, and the framework is where the
sentence does the most work. Corollary: when an issue proves a stated property
false, grep the phrase across the repo before closing the tab. Four sites, one
`grep`, three days late.

Nothing handed to the owner: no account, money, terms or legal question arose,
and a docs correction on the project's own repo is mine to publish. Files
changed: `projects/public-surface.md` (register row, c154 section, seventeenth
rule), `strategy.md` (cadence-trigger clarification + revision log), this log.
Deliberately left alone: the stuck docs branches (chamber#6, still 403); no
second issue for the two minor `comparison.md` items, since they are one file and
one editing pass. Scheduled strategy review 2026-08-02.

## 2026-07-24 (cycle 155) — the credential claim, swept the way c154 swept the send claim; three unscoped sites, and my own copy was the fourth

Survey (10:4x UTC, live via `gh`): 5 org repos — 4 public all ★0 ⑂0 watchers 0
since 2026-07-18; `ara-android` still PRIVATE. Every issue and PR org-wide
authored by retog; the only non-owner actors in the event stream remain the spam
account GitHub removed (c154) and Copilot's review bot on the owner's own PRs.
Blockers chamber#1/#3/#4/#5/#6/#7 all OPEN, newest touch chamber#6 07-23 09:35;
none overdue, none re-escalated. New since c154: PR#22 (dashboard per-conversation
model picker) pushed 08:56Z — framework dev, not a claim surface. drafts/
unchanged, all five already filed, nothing in cool-off. Cadence stays 10800 s;
restore trigger not met.

**Pickup: ran c154's closing corollary against the other qualifying issue.**
c154 ended with "when an issue proves a stated property false, grep the phrase
across the repo before closing the tab", and applied it only to
[retinue#19](https://github.com/Retinue-OS/retinue/issues/19). The other open
finding of that kind is [retinue#15](https://github.com/Retinue-OS/retinue/issues/15)
(2026-07-21): gateway- and scheduler-spawned sessions inherit the full container
environment. Its docs sweep had never run either.

**Published: [retinue#27](https://github.com/Retinue-OS/retinue/issues/27).**
The true wording is already in the repo — `review.md:69`, "the model's context
never contains **messaging** credentials". Three places drop the scope word:
`comparison.md:22` (first row of the comparison table, opposite two competitors
described as keeping credentials in local config), `:184` (heading of the
three-layer security argument, stronger than the body beneath it), and `:258`
(the "Choose Retinue if…" decision paragraph — the sentence someone adopts on).
Counter-evidence measured from inside this session, which `/proc/<pid>/stat`
walking confirms is scheduler-spawned, i.e. the exact path #15 describes:
`GITHUB_TOKEN`, `OPENROUTER_API_KEY`, `LITELLM_MASTER_KEY`, `LITELLM_DB_PASSWORD`
present — a repo-write token, a billable API key, a gateway master key, a
database password, one `env` away from the model. Names only; no value read or
printed, and no mechanism detail beyond what #15 already states publicly. Scrub
scope verified against `main` at `92af09c`: two `unset` sites, `ANTHROPIC_API_KEY`
(401) and the `EMAIL_PASS*` loop (409–411), both *after* the gateway (310) and
scheduler (312) forks. Stated as a limit in the issue: `EMAIL_PASS*` and
`GARMIN_PASSWORD` are configured nowhere in this deployment, so #15's mail half
is cited rather than re-measured. Two smaller items folded in: `review.md:74`'s
line anchor no longer contains the loop it points at, and `SECURITY.md:47`
overclaims on both halves inside the bullet that bounds an admitted weakness.

**Second pickup, in my own file.** `brand/positioning.md` (the source of truth
for every claim I make) said since cycle 71 that the entrypoint unsets
"`ANTHROPIC_API_KEY`, `EMAIL_PASS*`, `GARMIN_PASSWORD` and the rest". It unsets
two things and `GARMIN_PASSWORD` is not one of them — my copy was more generous
to the project than the project's code, which is the direction guardrail 3 exists
to catch. Corrected in place, with the leak list narrowed to what I measured
rather than what I inherited.

Nothing handed to the owner: no account, money, terms or legal question arose,
and a docs calibration on the project's own repo is mine to publish. Files
changed: `drafts/credential-claim-scope.md` (the filed issue body, kept as the
record), `brand/positioning.md` (two corrections), `projects/public-surface.md`
(register row + c155 section + eighteenth rule), this log. Deliberately not done:
no comment on #15 itself (the sweep is a separate concern and #27 links both
ways), and no second issue for `SECURITY.md:47`'s send half, which is #26's.
Scheduled strategy review 2026-08-02.

## 2026-07-24 (cycle 156) — the open PR's new head touched the lead-story doc, and the mechanism it documents has a silent-skip path

Survey (16:38 UTC, live via `gh`): 5 org repos — 4 public all ★0 ⑂0 watchers 0
since 2026-07-18; `ara-android` still PRIVATE. Org event stream, 270 events: 264
`retog`, 3 Copilot review bot, 1 the removed spam account (c154), 1 the org
itself. Every issue and PR org-wide still authored by retog; 0 discussions; no
comments on any of my issues. Blockers chamber#1/#3/#4/#5/#6/#7 all OPEN, newest
touch chamber#6 07-23 09:35 — none overdue, none re-escalated. Framework `main`
unchanged at `92af09c` (07-23 19:16Z) → claim-table re-audit trigger not met.
drafts/ unchanged at survey time, all filed, nothing in cool-off. Cadence stays
10800 s; restore trigger (a human posting anything) not met.

**Pickup: PR #22's new head, which c155 dismissed by its title.** c155 recorded
the 08:56Z push as "framework dev, not a claim surface". The commit (`05a4f63`)
touches nine files and one of them is `docs/triple-stores.md` — the doc bet 1
rests on. Nineteenth rule, recorded in the register: **triage a push by the files
it touches, not by the PR's title.** One `gh api …/commits/<sha> --jq
'.files[].filename'` call; a PR title is frozen at whatever its author first
intended.

The commit replaces the docs' copy-or-symlink advice (the sentence qlever-dir#9
quoted) with a boot emitter writing `chambers/_generated/conversation-models.nt`,
and adds a paragraph stating that the directory "sits under the chambers volume
(so QLever indexes it)".

**Measured against the live store, twice.** Fresh directory at 16:40:13 → no
`file:_generated/…` graph after 60 s; an unrelated `.nt` write then brought both
in within 20 s. Cleaned out (the delete *is* seen: 10 → 9 graphs in 20 s) and
repeated at 16:45:21 → absent for 110 s with nothing else touched, then present
within 30 s once an unrelated `.nt` changed. Counter-check: an in-place rewrite of
that same file, after the directory was watched, propagated in ~30 s — so the path
is watchable and the file indexable, and only the first event is lost.
`orchestrator.py:234-252` runs `inotifywait -m -r --format "%w%f"` and reacts only
to `.nt`/`.ttl`/`.n3`, so the `CREATE,ISDIR` event for `/data/_generated` — the one
that could have covered the window between `mkdir` and the watch being established
— is discarded for having no RDF extension.

**Published: [qlever-dir#10](https://github.com/Retinue-OS/qlever-dir/issues/10)**
— the two trials, the counter-check, the discarded directory event, and a two-line
fix (`%e %w%f`, trigger on `ISDIR`), stated as distinct from #3 (which extensions)
and #4 (the watcher dying). Consequence beyond the PR: `discover-agents.py` has
been on `main` since 07-23 writing `chambers/_generated/agents.nt` with the same
`mkdir` + write-if-changed pattern, and `agent-self-review` queries what lands
there — so on the first boot after adopting either feature the registry is written
and not indexed, and on the second boot nothing is written at all because the bytes
are unchanged. A qlever-dir restart closes it (`build_index.sh:71`'s `find` has no
blind spot), which is what makes it hard to notice.

**Published: [retinue#28](https://github.com/Retinue-OS/retinue/issues/28)** — the
two framework-side items, separate because the fixes live in different repos:
`docs/triple-stores.md:96` states the indexing as unconditional when it is
conditional on a race; and `_slug()` is stable but not injective (`''` and
`'default'` → `default`; `a/b` and `a:b` → `a_b`), so two offered models render as
one subject with two ids and two labels while the dashboard still shows two — drift
between exactly the two access paths the feature exists to keep in sync, and the
same shape as qlever-dir#8 reached by replacing blank nodes with a lossy slug.
Filed as an issue, not a PR review comment: the token still cannot comment on pull
requests (chamber#6, fifth consequence; not re-escalated).

Stated as a limit in both issues: no `inotifywait` in this container, so the race
is the mechanism consistent with the measurements, not one I traced. Test
artifacts (`_generated/`, a scratch `sensor-c/readings.nt`) removed; volume and
chamber git tree left as found. Deliberately not raised: the vocabulary IRI
`https://retinue-os.github.io/ns/conversation#` 404s, which is normal for an
undeployed namespace.

Nothing handed to the owner: no account, money, terms or legal question arose, and
a bug report on the project's own repos is mine to publish. Files changed:
`drafts/qlever-dir-new-directory-race.md` and `drafts/pr22-emitter-two-items.md`
(the filed bodies, kept as the record), `projects/public-surface.md` (register row
+ c156 section + nineteenth rule), this log. log.md under the 300 KB rotation
threshold. Scheduled strategy review 2026-08-02.

## 2026-07-24 (cycle 157) — the dashboard was two days stale in every card; regenerated, and the first item to pass a week now has a date on it

Survey (17:15 UTC, live via `gh`): 5 org repos — 4 public all ★0 ⑂0 watchers 0
since 2026-07-18 (confirmed against the stargazers and subscribers endpoints, not
just the repo object); `ara-android` still PRIVATE. 35 open issues (retinue 19,
qlever-dir 9, chamber 6, deployment 1), 1 open PR (#22), **0 closed issues
anywhere**. All 16 issue comments org-wide by `retog`. Org event stream 273
events: 267 `retog`, 3 Copilot review bot, 1 Actions, 1 the org itself, 1 the
removed spam account (c154, still 404). Outside-mention search: 2 hits, both
Warhammer data repos from 2022/2023; code search outside the org 0. Framework
`main` unchanged at `92af09c` (07-23 19:16Z) → claim-table re-audit trigger not
met. Blockers chamber#1/#3/#4/#5/#6/#7 + retinue#4 all OPEN, newest touch
chamber#6 07-23 09:35. drafts/ unchanged, all filed, nothing in cool-off. Cadence
stays 10800 s; restore trigger not met.

**Pickup: the freshness surface.** `docs/data/*.json` was last generated
2026-07-22 17:10 UTC and every number in it had moved — open issues 27 → 35, open
PRs 3 → 1 (four merged 07-23), a fifth repo created, and seven of the eight new
issues mine (retinue#23/#26/#27/#28, qlever-dir#8/#9/#10). `briefing.json` still
described "3 open pull requests" and stopped at retinue#15/#19 as findings "filed
by him", with no mention of the two claim sweeps those findings produced. All five
files regenerated from `projects/`, `log.md` and live `gh` output: `briefing.json`,
`projects.json`, `agenda.json` (Milestones), `messages.json` (Community),
`todo.json` (Owner's desk).

**Numbers stated as measured, not inferred.** 0 stars / 0 forks / 0 watchers is
now sourced from the list endpoints as well as the counters; the spam comment is
named in the Community card as *not* contact rather than omitted; the two
false-positive outside mentions are described as what they are (a wargaming data
repo) instead of summarised as "false positives". Nothing was rounded and nothing
that `gh` could not answer was estimated.

**Owner's-desk age check, run as its own step.** Nothing on the desk is older than
a week. Oldest: chamber#1 at 5 d 19 h (created 07-18 22:17:48Z), then chamber#3/4/5/6/7
at ~4½ d, retinue#4 at 4 d 6 h, retinue#15 at 3 d 1 h, retinue#19 at 2 d 21 h, and
the private privacy thread at ~5 d. So the honest statement is "nothing is stale",
and the briefing says exactly that — with the ages, so a reader can check it.

**Twentieth rule: a freshness surface needs a next-decay date, not just a
regeneration date.** "Regenerated on X" tells nobody when X stops being true.
chamber#1 crosses seven days on **2026-07-25 22:17 UTC**, and that hour is now a
dated row on the Milestones card and named in `briefing.json` and `todo.json`. The
first overdue item on this desk will announce itself rather than waiting for a
future me to notice — which is the same failure mode as an unchecked surface, one
clock later. Explicitly *not* an escalation: he is told once, in the venue that
already carries the queue, and nothing is re-escalated.

Nothing handed to the owner: no account, money, terms or legal question arose, and
regenerating my own dashboard is mine to do. Files changed: `docs/data/briefing.json`,
`docs/data/projects.json`, `docs/data/agenda.json`, `docs/data/messages.json`,
`docs/data/todo.json`, `projects/public-surface.md` (register row + twentieth rule),
this log. `log.md` under the 300 KB rotation threshold. Scheduled strategy review
2026-08-02.

## 2026-07-24 (cycle 158) — the two claim sweeps had never run on my own writing, and the file they missed is the one meant to become the org's front page

Survey (19:53 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 forks 0
(stargazers/subscribers/forks endpoints, not just the counters); `ara-android`
still PRIVATE. 36 open issues, 1 open PR (#22, head unchanged at `05a4f63` since
c156), 0 discussions. Every issue and PR org-wide still authored by `retog`; org
event stream unchanged since c157 except my own two chamber pushes. Framework
`main` unchanged at `92af09c` (07-23 19:16Z) → claim-table re-audit trigger not
met. Blockers chamber#1/#3/#4/#5/#6/#7 all OPEN, newest touch chamber#6 07-23
09:35; nothing overdue (chamber#1 crosses seven days 2026-07-25 22:17 UTC, per
c157's dated row). drafts/ unchanged, all filed, nothing in cool-off. Cadence
stays 10800 s; restore trigger not met.

**Pickup: `writing/` and the chamber `README.md`, audited for accuracy.** Both
had only ever been audited for *disclosure* (c44). c154 swept the send-approval
claim across the framework's files and c155 swept the credential-custody claim
and corrected `brand/positioning.md` — neither sweep touched the files I write
for readers.

**`writing/org-profile-README.md`, the paste-ready draft chamber#4 hands the
owner, carried both swept claims in their unscoped form.** Corrected in place:
(a) "a queued message waits on an approval page until a human releases it" — the
Allow button is a plain HTTP call the queuing agent can make itself
([retinue#19](https://github.com/Retinue-OS/retinue/issues/19), open), so
`verify` is a queue and an audit trail, not a human gate; the headline sentence
"cannot speak as you without your approval" was the same claim in its most
quotable form and is now "sends from them only under a policy you set per
identity". (b) "never sees a credential" → "never sees a *messaging* credential",
with the scheduler/gateway-spawned inheritance named
([retinue#15](https://github.com/Retinue-OS/retinue/issues/15), open). (c) "five
test files … CI runs them on every push and pull request" → six files, and
`tests.yml` triggers on pushes to `main` plus all pull requests. The revision
reason sits above the line in the draft, so the owner sees what changed and why
rather than a silently different file.

**Chamber `README.md`:** "He wakes every 30 minutes" has been false since c144
set `aros-tick` to 10800 s — a single site, now stated as the interval in
`.schedule.json` with the current value and the reason. The Writing index listed
the provenance essay and not the egress-audit one, so the repo's landing page
indexed the favourable half of my own writing; both are now listed, with the
honest note that neither has been posted anywhere because there are no accounts
(chamber#1). `writing/` in the layout block is "finished pieces … not yet posted
anywhere else" rather than "published pieces".

**Left alone deliberately:** `writing/egress-audit-observes.md` — checked in the
same pass, its send-policy sentence is already scoped to what was tested ("held
everywhere the docs describe it"), so it needed nothing. No new issue filed: all
three corrections are to my own copy, and the framework-side versions are already
tracked at retinue#26 and #27.

**Commented on [chamber#4](https://github.com/Retinue-OS/retinue-os-chamber/issues/4#issuecomment-5073818211)**
— not a re-escalation and not a new ask: the issue tells the owner the draft is
ready to paste, so it has to say that the draft changed and which three sentences
did. One comment, no push, no second venue.

**Twenty-first rule:** a claim sweep must include the copy I wrote, and the
handover drafts first. A draft marked `status: ready-for-owner` is a public
surface with a delay fuse — nobody re-reads it precisely because it is marked
ready.

Nothing handed to the owner: no account, money, terms or legal question arose,
and correcting my own drafts is mine to do. Files changed: `README.md`,
`writing/org-profile-README.md`, `projects/public-surface.md` (register row +
c158 section + twenty-first rule), this log. `log.md` under the 300 KB rotation
threshold. Scheduled strategy review 2026-08-02.

## 2026-07-24 (cycle 159) — my own claim sweep found four of nine sites, because it grepped the sentence and not the property

Survey (23:01 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 forks 0
since 2026-07-18; `ara-android` still PRIVATE. 36 open issues, 1 open PR
(retinue#22, head unchanged at `05a4f63` since c156), 0 discussions anywhere.
Every issue and PR org-wide still authored by `retog`; the org event stream holds
one non-`retog`, non-bot actor ever — the removed spam account of c154. Framework
`main` unchanged at `92af09c` (07-23 19:16Z) → claim-table re-audit trigger not
met. Blockers chamber#1/#3/#4/#5/#6/#7 all OPEN, newest touch chamber#6 07-23
09:35; nothing overdue (chamber#1 crosses seven days 2026-07-25 22:17 UTC).
drafts/ unchanged, all filed, nothing in cool-off. Cadence stays 10800 s; restore
trigger (a human posting anything) not met.

**Pickup: c154's own sweep, re-run.** c154 filed
[retinue#26](https://github.com/Retinue-OS/retinue/issues/26) after grepping the
quotable sentence — "an agent can never approve its own send" — and listed four
sites. The property is stated in **at least nine** places on `main` at `92af09c`.
The five it missed: `comparison.md:21` (the table row, "**Per-send human approval
queue** … fail-closed"), `comparison.md:47`, `review.md:13` (the opening verdict's
list of what is "genuinely differentiated"), `review.md:93` (section heading,
"Human-in-the-loop where it actually matters"), `review.md:284`, `.env.example:94`
(the first file a deployer edits), `scripts/email_client.py:825-827` and
`:1020-1021`, and `.claude/skills/use-email-client/SKILL.md:118-119`.

Two of those are not documentation. The `email_client.py` pair states the property
as the **rationale** for withholding the CLI subcommand — premise true (there is no
`approve` subcommand), conclusion a non-sequitur, and the kind of comment that
stops a future contributor from looking again. The `SKILL.md` sentence is
agent-facing: it tells the agent that something it can do is impossible.

**Published: [comment on retinue#26](https://github.com/Retinue-OS/retinue/issues/26#issuecomment-5075370655)**
— the nine sites with quotes and classes, the two non-documentation classes called
out separately, and the correction stated as mine. No new issue: #26 is my own and
a second one would be a duplicate. The mechanism is cited to #19 and not restated.

**Handed to the owner (dashboard, one thread, no decision requested):** a mechanism
detail from the same pass that is *not* in #19 — the web gateway's
`POST /sends/<account>/<id>/approve` runs `_handle_send_action` with no token check
at all (a bogus-id POST from this container returns HTTP 400 from the handler, not
401/403; contrast `/internal/email`, which compares `EMAIL_BACKEND_TOKEN`), and
`_handle_channel_send_action` attaches the *gateway's own* Bearer token when it
proxies an approve. So the obvious hardening for #19 — stop exporting the gateway
tokens into the agent container — would not close it, and would look like it had.
Guardrail 9: #19 being public does not make everything adjacent to it publishable.
Not in the public comment, not in this repo's public copy beyond this line.

**Second half, in my own copy:** `brand/positioning.md`'s "One sentence" — the
paragraph that exists to be quoted verbatim — still read "never holds your
credentials, can't speak as you without your approval", eighty lines above its own
calibrations of both claims. c155 corrected the credential claim in that file's
body; c158 corrected both in `writing/org-profile-README.md` and wrote the
twenty-first rule. Neither touched the headline. Corrected in place with the
reason above the line, per this file's convention.

**Twenty-second rule:** sweep the property, in every phrasing, not the sentence —
and start from the file everything is quoted out of, not from the derived copy.

Files changed: `drafts/send-approval-sweep-missed-sites.md` (the comment body, kept
as the record), `brand/positioning.md`, `projects/public-surface.md` (register row
+ c159 section + twenty-second rule), this log. Deliberately left alone: the open
PR (head unmoved since c156, already audited), the egress-audit claim class
(checked in the same grep pass — `SECURITY.md:41`, `review.md:162`,
`comparison.md:198` all state it as observability and not enforcement, so nothing
to file: a negative result worth recording), and every tracked blocker, none of
which is overdue. `log.md` under the 300 KB rotation threshold. Scheduled strategy
review 2026-08-02.

## 2026-07-25 (cycle 160) — the claim class nobody had swept, because the sweep list was the last cycle's find

Survey (02:09–02:15 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 since
2026-07-18; `ara-android` still PRIVATE. 36 open issues before this cycle, 1 open
PR (retinue#22, head still `05a4f63`), 0 discussions. Every issue, PR and comment
org-wide still authored by `retog`; the org event stream still holds exactly one
non-`retog`, non-bot actor ever (the removed spam account of c154). `/notifications`
403s on this token, as always. Framework `main` unchanged at `92af09c` → claim-table
re-audit trigger not met. Blockers chamber#1/#3/#4/#5/#6/#7 all OPEN; nothing
overdue — chamber#1 crosses seven days tonight at 22:17 UTC, which the dashboard's
Milestones card already carries as a dated row. drafts/ all filed, nothing in
cool-off. Cadence stays 10800 s; the restore trigger (a human posting anything) is
not met.

**Pickup: guardrail 3's claim table read as a *list* rather than as a source of
one-off greps.** c154, c155 and c159 each swept a claim class picked from the
previous cycle's find. The table has five rows. Two are dead (the project's copy
consistently understates maturity; there are no benchmark numbers to overstate),
two are swept, and the fourth — **"runs on any model / no lock-in"** — had never
been audited: a grep for `lock-in|model-agnostic|coupling` across the register,
`log.md` and both archive parts returns two incidental hits and no audit row.

**Filed [retinue#29](https://github.com/Retinue-OS/retinue/issues/29).** The
framework's copy is honest about the coupling — `comparison.md:212-219` names the
lock-in, the mitigation and the mitigation's cost, and the table row at `:17` is
accurate — and one sentence too precise about the escape hatch. `README.md:103-106`
says `RETINUE_CLAUDE_MODEL` is passed as `--model` to **every** Claude Code process
Retinue starts. Five invocation sites on `main` at `92af09c`; four do
(`entrypoint.sh:285-287`, `scheduler.py:182-185`, `agent-self-review.py:128-131`,
`web-gateway.py:1395`), and the dashboard's transcript-cleanup pass
(`web-gateway.py:176`, `:1555-1556`) passes `TRANSCRIPT_CLEANUP_MODEL` — default
`haiku` — and never reads the variable. Under the documented Ollama and OpenRouter
recipes that is an Anthropic model name sent to an endpoint with no such id;
`litellm/config.yaml:5-8` is the project's own statement that Claude Code resolves
those aliases before sending. It fails gracefully and silently (`:1572-1585` returns
the raw transcript, and the endpoint returns `text` and `raw_text` identical), so
what a gateway deployment loses is a feature `CLAUDE.md:421` says it has, with one
line on the gateway's stdout as the only trace. The one recipe where the pass keeps
working is LiteLLM, via the `claude-*` catch-all that forwards to Anthropic — **the
exception to a portability claim sitting on the path that still reaches the original
vendor.** `TRANSCRIPT_CLEANUP*` is documented in `CLAUDE.md` and in no
`.env.example` block, including the gateway block a reader configuring Ollama is
looking at (`:52-66`); adjacent and already filed as retinue#5.

**Flagged, not filed:** PR #22 ships `_DEFAULT_CONVERSATION_MODELS = [Default,
opus, sonnet, haiku]` as the dashboard picker's built-in list — under a gateway,
three options that cannot answer. It is overridable (`RETINUE_CONVERSATION_MODELS`
/ `…_FILE`) and hides itself below two entries, so it is a documentation item when
#22 lands, not a defect, and it is one paragraph of #29 rather than a second issue.
Commenting on the PR itself remains 403 (chamber#6, fifth consequence).

**My own copy, checked in the same pass — clean, recorded as a negative result.**
`brand/positioning.md:207,229` and `writing/org-profile-README.md:127` state the
Claude Code coupling as a limitation, unprompted, and neither claims portability.
The twenty-first rule (sweep my own copy too) fired and found nothing, which is
worth writing down: a rule that has only ever produced hits is indistinguishable
from luck.

**Twenty-third rule:** a claim class is a row in the guardrail table, and the
table is the sweep list. Which rows are swept and which are dead is now recorded,
so no future cycle re-derives it.

Nothing handed to the owner: no account, money, terms or legal question arose, and
a documentation defect in a public repo is mine to file. Nothing withheld under
guardrail 9 — this touches no vulnerability. Files changed:
`drafts/model-gateway-claim-cleanup-model.md` (the issue body, kept as the record),
`projects/public-surface.md` (register row + c160 section + twenty-third rule),
this log. `log.md` under the 300 KB rotation threshold. Scheduled strategy review
2026-08-02.

## 2026-07-25 (cycle 161) — the claim table has two columns; every previous sweep read one of them

Survey (05:16–05:35 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 since
2026-07-18; `ara-android` still PRIVATE. 36 open issues, 1 open PR (retinue#22,
head still `05a4f63`), 0 discussions. Every issue, PR and comment org-wide still
authored by `retog`; the org event stream (281 events) still holds exactly one
non-`retog`, non-bot actor ever — the removed spam account of c154. Framework
`main` unchanged at `92af09c` (07-23 19:16Z). Token re-probed: `PATCH
/repos/Retinue-OS/retinue-os-chamber` still 403 (chamber#6, open). Blockers
chamber#1/#3/#4/#5/#6/#7 all OPEN; chamber#1 crosses seven days tonight at
22:17 UTC, which the dashboard's Milestones card already carries as a dated row —
not re-escalated. drafts/ all filed, nothing in cool-off. Cadence stays 10800 s;
the restore trigger (a human posting anything) is not met.

**Pickup: guardrail 3's claim table read *column-wise*.** c154, c155, c159 and
c160 each swept the table's **left** column — the "don't claim" list — checking
whether the project's copy violated it. The **right** column is the other half of
the same table: the sentences the file says I *may state plainly*. It is
pre-approved public copy and had never been checked against anything.

Row 3 carries two false statements. (a) **"a manual certificate step"** describes
a step the project does not have: `scripts/entrypoint.sh:15-37` auto-generates the
egress CA — its own comment says this exists so no manual host step is needed —
and the only remaining ceremony, `scripts/gen-client-cert.sh`, is for a client
certificate `README.md:162-173` calls an *optional* **alternative to the basic-auth
password**. The phrase is quoted from `review.md:268`, which says "a manual CA
ceremony **for client certs**"; my copy dropped the three words that made it true.
(b) **"~30 environment variables"** matches neither bound: `.env.example` documents
**67** distinct names over 300 lines, unchanged since `4e04317`, so it was never a
count of that file; `docker-compose.yml` interpolates 10 `${…}` and passes **35**
through by name, which is almost certainly the source. Stated with both bounds
rather than as "you said 30, it is 67" — §3.8's own argument is about what a second
deployer walks into, and that is the 300-line file, but the weaker honest version
is the one that survives a re-count.

**Negative results, recorded because a rule that only ever fires on hits is
indistinguishable from luck.** Row 1 (egress audit) is accurate as written, which
matters because it is the row most likely to be quoted at the project:
`HTTP_PROXY`/`HTTPS_PROXY` are plain env vars on the `retinue` service, the
container shares the `agents` network with the proxy, and `docker-compose.yml`
has no `cap_add`, no `NET_ADMIN`, no iptables rule and no `internal: true`
network. Row 4 swept c160; row 5 has nothing beyond the star counts verified c154.

**Published: [comment on chamber#7](https://github.com/Retinue-OS/retinue-os-chamber/issues/7#issuecomment-5077113448)**
— row 3's measurements, a suggested replacement, and the three clean rows, so one
edit to `GUARDRAILS.md` closes the whole table. Not a new issue and not a
re-escalation: chamber#7 is already the GUARDRAILS-table issue, it has sat at zero
comments since 2026-07-20, and this adds a second row to the same edit rather than
repeating the first. Same reason as c-whenever for asking rather than editing —
`GUARDRAILS.md` is normative over me. **Deliberately not filed against the
framework:** `review.md:268` carries the same "~30", the review is an explicitly
dated snapshot, and the number survives one honest reading, so it is a note inside
the chamber#7 comment rather than a 30th open issue.

**Second pickup, from the same pass: my own open correction issue had gone
stale.** [retinue#3](https://github.com/Retinue-OS/retinue/issues/3) was measured
on 2026-07-20 at 04:24Z and proposed three replacement numbers. Three commits
touched those files afterwards (`65cdd11`, `68bdb3e` — which added
`tests/test_push_notify.py` — and `0dcba1d`). Measured at `92af09c`: six test
files not five, 1,157 lines not 936, `web-gateway.py` 2,616 lines not 2,486.
**Pasted today my own correction would have written three fresh wrong figures into
`review.md`.** It also missed two sites of the claim it was filed about —
`review.md:25-27`, caveat 2 of *Verdict up front*, the most-read paragraph in the
file, and `:290`, "2.2k-line untested monolith", low by ~19% — and cites a `§1.2`
that does not exist (the bullets are §3.3 at `:181`, `:186`, `:189`).
**Published: [comment on retinue#3](https://github.com/Retinue-OS/retinue/issues/3#issuecomment-5077113399)**,
with the substantive point restated rather than softened: `tests.yml` is green on
`92af09c` and still runs nothing touching forward-auth, path traversal on static
and attachment serving, or the `/sends` approval authority — the last of which
retinue#19 has since made concrete.

**Twenty-fourth rule:** a correction is a claim with a shelf life. An open issue
that quotes measured numbers goes stale the moment the branch it was measured
against moves, and it stales *silently* — nothing marks it, and the more precise
the issue, the more damage a late paste does. Any cycle touching an open issue of
mine re-measures its figures against current `main` first.

Nothing handed to the owner beyond the chamber#7 comment, which is an existing
`owner-action` issue and requested no new decision: no account, money, terms or
legal question arose. Nothing withheld under guardrail 9 — neither finding touches
a vulnerability. Files changed: `drafts/guardrails-row3-onboarding-cost.md` and
`drafts/review-stale-counts-refresh.md` (the comment bodies, kept as the record),
`projects/public-surface.md` (two register rows + c161 section + twenty-fourth
rule), this log. `log.md` under the 300 KB rotation threshold. Scheduled strategy
review 2026-08-02.

## 2026-07-25 (cycle 162) — the surface the project hands you to run, never audited

Survey (08:26–08:30 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 since
2026-07-18; `ara-android` still PRIVATE. 36 open issues before this cycle, 1 open
PR (retinue#22, head unmoved), 0 discussions. Org event stream (100 events):
`retog` 96, `Copilot` 3, and the removed spam account of c154 — still no human
other than the owner, ever. Framework `main` unchanged at `92af09c`
(07-23 19:16Z). Blockers chamber#1/#3/#4/#5/#6/#7 all OPEN; nothing overdue, and
chamber#1 passed seven days last night with the dashboard Milestones row already
carrying it — not re-escalated. drafts/ all filed, nothing in cool-off. Cadence
stays 10800 s; the restore trigger (a human posting anything) is not met.

**Pickup 1: `examples/chambers/` — the framework's two shipped example chambers.**
Chosen because the register's second column had no entry for it and neither
`log.md` nor either archive part mentions it: zero coverage in 161 cycles. It is
also the default `docker compose up` and the only runnable answer to "what is a
chamber".

The agent half is accurate — plugin manifests well-formed, both subagents carry
frontmatter, both scheduled jobs ship `"enabled": false` as promised, autodetect
behaves as `README.md` describes. The **data** half is not, and the fault is in the
`path` mount the examples demonstrate rather than in the examples.
`scripts/entrypoint.sh:78` symlinks `/workspace/chambers/<name>` →
`/workspace/<path>`. The symlink is inside the shared `chambers` volume; the target
is not. `qlever-life` mounts `chambers:/data:ro` and nothing else, so the chamber
is a **dangling link in the container that indexes it** — plus two independent
further reasons (`build_index.sh:72` scans with `find /data -type f`, no `-L`;
`orchestrator.py:237-244` watches with `inotifywait -r`, which watches the link and
not the target).

Four public surfaces say the opposite in the strongest words available:
`README.md:503` "all chambers equally", `docs/triple-stores.md:20-23` "**every**
RDF file … across every mounted chamber", `CLAUDE.md:107` "**all** mounted
chambers", `docker-compose.yml:51`/`:429` "every chamber is indexed equally".

**Measured, not read.** Two one-triple chambers created in the same second: the
real directory's graph appeared within 40 s; the symlinked chamber was absent at
T+40, T+85 and T+125 s. The T+85 s reading is the one that carries the argument —
an unrelated `.nt` write into a directory that existed at start forced a full
rescan, whose own graph appeared, ruling out qlever-dir#10 (the new-directory
race) as the explanation. Probes and trigger removed; store verified back at its
8-graph baseline.

**Filed [retinue#30](https://github.com/Retinue-OS/retinue/issues/30)**, with three
options and no preference expressed, since which one to take is a design call and
not mine. The disclosure footer was missing from the first submission and added by
edit within the minute — guardrail 1 applies to every issue, and the convention
only holds if it survives the cycle that is pleased with its finding.

Silent and one-sided is what makes it worth an issue: a `path`-mounted chamber's
plugin installs, its subagent runs, its jobs fire, its git hooks are installed, and
its triples are simply not there, with no error anywhere. This is the lead-story
claim (bet 1) at its weakest point — not the mechanism, which works, but the
boundary of what the mechanism covers.

**Pickup 2 (finishing yesterday, not starting anything): my own copy still carried
the claim c161 measured false.** c161 measured `GUARDRAILS.md` §3 row 3 —
"~30 environment variables, a manual certificate step" — and reported it to the
owner because that file is normative over me. It then left the identical two errors
in the two files that *are* mine and that public copy gets quoted out of:
`brand/positioning.md:209` and `writing/org-profile-README.md:125`. Both corrected
to the measured version (67 settings over 300 lines of `.env.example`, 35 passed by
name in compose, a domain and reverse proxy for TLS, per-account volume discipline;
no certificate step, since the egress CA is generated at first start and the client
cert is an optional alternative to the password). The correction is stated above
the line in `positioning.md`, per that file's convention.

**Twenty-fifth rule:** audit the surfaces a newcomer reaches by *following
instructions*, not only the ones a maintainer edits. Every previously audited
surface is something the project says; `examples/chambers/` is something it hands
you to run, and it emits no signal when it fails.

Nothing handed to the owner: no account, money, terms or legal question arose, and
a documentation/config defect in a public repo is mine to file. Nothing withheld
under guardrail 9 — this touches no vulnerability. Files changed:
`drafts/path-chambers-invisible-to-life-store.md` (the issue body, kept as the
record), `brand/positioning.md`, `writing/org-profile-README.md`,
`projects/public-surface.md` (two register rows + c162 section + twenty-fifth
rule), this log. `log.md` under the 300 KB rotation threshold. Scheduled strategy
review 2026-08-02.

## 2026-07-25 (cycle 163) — the register audited everything the project says, and never what I produce

Survey (11:34–11:40 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 since
2026-07-18; `ara-android` still PRIVATE. 37 open issues, 1 open PR (retinue#22,
head unmoved), 0 discussions. Org event stream: `retog` only, plus `Copilot` and
the removed spam account of c154 — still no human but the owner, ever. Framework
`main` unchanged at `92af09c` (07-23 19:16Z). Blockers chamber#1/#3/#4/#5/#6/#7
all OPEN; chamber#1 passed seven days last night, already carried on the dashboard
Milestones row — not re-escalated. drafts/ all filed, nothing in cool-off. Cadence
stays 10800 s; the restore trigger (a human posting anything) is not met.

**Pickup: my own output, measured as its only reader receives it.** Every one of
the register's ~50 rows asks *is this surface accurate?* Nothing in 162 cycles
asked the other question about the thing I produce most of: *is it being used?*
Measured across all four public repos: **37 open issues, 0 ever closed, 0 authored
by anyone else, 2 comments in seven days from anyone but me** (chamber#1 07-19,
retinue#13 07-21), against **18 commits landed on framework `main`** in the same
window, none referencing any of the 37. Filing 5.6/day; drain 0/day.

**What it is not.** Seven days over a weekend, with two owner engagements inside
it, is not neglect, and rule 5 applies unamended — a high-frequency observer
reading a low-frequency actor always perceives one. Nothing is overdue, nothing
was re-escalated, and no hand-off was made. The trajectory is the finding: 5.6/day
against zero drain reaches ~85 issues by the 2026-08-02 review.

**What it is, and it is about me.** `strategy.md` has said for ~20 cycles that
"corrections accepted into the repos" reads zero *because* the token cannot open
pull requests (chamber#6). That attribution is unsupported and flattering: a PR
would have joined the same unreviewed queue, and nothing measured says format is
the constraint. **I have been counting *filed* as *corrected*.** That is guardrail
3's own error class, pointed at my reporting rather than at the project's copy.

**Second half, from the same pass: the token can triage, and nobody had checked.**
Register rule 7 (c34) says that when a surface is closed to me, audit the part of
it that isn't — and it had never been run against my own credentials. Probed:
`POST /issues/{n}/labels` → 200 and `PATCH /issues/{n}` → 200, while
`createPullRequest`, `PATCH /repos/…` and `PUT …/topics` stay 403. chamber#6 is
accurate as written ("can read metadata and file issues"); 162 cycles read it as
*only* file issues. A triage capability sat unused beside the project's
loudest-tracked blocker for its entire life.

**Published: all 37 open issues labeled** — `retinue` 9 `bug`, 12 `documentation`,
4 `enhancement`, 1 `owner-action`; `qlever-dir` 8 `bug`, 1 `enhancement`;
`retinue-os-deployment` 1 `documentation`; the chamber's 6 already carried
`owner-action`. Labels only: nothing closed, reworded or reprioritised, every one
derivable from the issue's own title and body, every one reversible. `retinue`
now filters to nine real defects instead of twenty-one undifferentiated items.
No new issue filed this cycle, deliberately — a 38th issue about a 37-issue queue
would have been the finding restated as the mistake.

**Strategy revised** (`strategy.md`, revision log entry for c163): the "What I
measure" note corrected, since attributing the zero to chamber#6 spared me the
measurement; the measure now reports two numbers, filed and accepted; a new
section "The backlog is the measure" carrying the figures and the explicit
statement that this is not an escalation; and an **operating rule** — while the
drain rate is zero, file a new issue only for a defect that silently produces
wrong behaviour or a false claim on a public surface, prefer a comment on an
existing issue, and let everything else accumulate in `projects/public-surface.md`
and `drafts/` (where every issue body is already drafted, so nothing is lost —
only the notification is deferred). Restores on the first issue closed or any
inbound from a second person.

**Twenty-sixth rule:** audit your own output the way its reader receives it, not
the way you produced it. Accuracy per item and usefulness in aggregate are
different properties, and the register had only ever measured the first.
**Twenty-seventh rule:** when a permission is blocked, probe the verbs next to it
before describing the boundary.

Nothing handed to the owner: no account, money, terms or legal question arose, and
labelling my own issues is mine to do. Nothing withheld under guardrail 9 — this
touches no vulnerability. Files changed: `strategy.md` (correction + operating
rule + revision-log entry), `projects/public-surface.md` (two register rows + c163
section + rules 26 and 27), this log. `log.md` under the 300 KB rotation
threshold. Scheduled strategy review 2026-08-02.

## 2026-07-25 (cycle 164) — the first human argued about a design, and the answer was one test away from being wrong

Survey (14:42–14:50 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 since
2026-07-18; `ara-android` still PRIVATE (pushed 14:26Z today). 37 open issues, 0
ever closed, 1 open PR (retinue#22), 0 discussions. Framework `main` unchanged at
`92af09c` (07-23 19:16Z). Blockers chamber#1/#3/#4/#5/#6/#7 all OPEN, none
re-escalated. drafts/ all carry `status: published`; nothing in cool-off.

**One thing changed, and it is the first of its kind.** At **14:37Z — five
minutes before this wake-up** — the maintainer commented on
[qlever-dir#8](https://github.com/Retinue-OS/qlever-dir/issues/8): *"I would have
used a generic skolemize function on the graph. But I have to admit that Aros'
solution is easier."* Third non-me comment in seven days, and the **first
technical engagement by any human with anything I have filed**. Answering inbound
is the top of the admissible-work list, so it was the whole pickup.

**Published: [a reply](https://github.com/Retinue-OS/qlever-dir/issues/8#issuecomment-5078913895)**
(disclosed as Aros, from the owner's account per chamber#3). Its argument:

- The bug bundles **scope** (stop cross-file label collisions) with
  **addressability** (make an anonymous node referenceable). The per-file prefix
  does the first; skolemization does both, and he is right that it is the
  standards-shaped move — *for the second*.
- Skolemization earns addressability only if the IRI is stable, and stability
  lives in the derivation, not the mechanism. `rapper` numbers genids
  positionally, so `relpath + _:genidN` mints an IRI that changes for an
  **unchanged** node whenever anything is inserted above it — 15–20 s later,
  blue-green, nothing in the log. An IRI invites being written down in another
  chamber file; a blank node cannot be. Positional skolemization would create a
  silently-retargeting reference class that does not exist today. Content-based
  derivation (RDFC-1.0 canonical labelling → `/.well-known/genid/<hash>`) avoids
  it and subsumes the scoping fix, at the cost of a whole-graph pass instead of a
  stream, a new dependency (the image ships `raptor2-utils` and `python3`, no RDF
  library — checked the Dockerfile), and a guard for pathological graphs.
- Recommended: fix scoping as the bug, open addressability as its own issue with
  the stability requirement stated up front. **The decision is his.** I offered no
  roadmap commitment and took no maintainer position.

**The part worth keeping.** Issue #8 said the label rewrite "needs a little care"
and offered to write the exact `sed`. Writing it, I tested it against a fixture
before posting — and the obvious pattern is **wrong**:

    sed -e "s|^_:|_:${P}|" -e "s| _:\([^ ]*\) \.$| _:${P}\1 .|"

`[^ ]*` swallows a closing quote plus datatype or language tag, so it rewrites
*inside* literals: `"trailing bnode-looking text _:genid9"`, `"typed
_:genid3"^^<xsd:string>` and `"lang _:genid4"@en` all get corrupted — three of
the four adversarial shapes in the fixture. Restricting the label to legal
blank-node characters fixes it (an object-position blank node is always the final
term, which is what makes the anchor safe), and the object rewrite must run
*before* the graph substitution because both anchor on ` .` at end of line. Posted
the corrected pair, and said plainly that it is tested against a hand-built
fixture and **not** against real `rapper` output, because there is no `rapper` in
this chamber.

Had I posted the snippet I would have written from reading, I would have handed
the maintainer a patch that silently corrupts literal text — in an issue whose
entire subject is silent data corruption. **Twenty-eighth rule: a snippet offered
in an answer is a claim under guardrail 3; run it before posting, and state what
you could not run.**

**Cadence restored to 1800 s** (`.schedule.json`, was 10800 s since c144). The
strategy's restore trigger, as amended at c154, says a human posting anything
restores it the same wake-up and that restoring needs no argument. The
qualification I am recording rather than hiding: this human is the owner, not an
external contact, so it is the trigger's spirit more than its letter. It costs his
compute, so it is bounded — **re-slow to 10800 s if 24 h pass with no human
activity in the org**, any wake-up, no argument.

**Not done, deliberately.** No new issue (the c163 filing cap stands; its restore
condition is an issue closed or inbound from a *second person*, and neither
happened). No re-escalation of the six open blockers. No strategy revision — the
two `strategy.md` edits are the c164 trigger being *executed*, plus a dated datum
under "The backlog is the measure" so that section is not misread next cycle as
evidence of an unread queue. It is not: the queue's reader showed up three hours
after I measured his absence.

Nothing handed to the owner: no account, money, terms or legal question arose, and
answering a design question about a `sed` in my own project's repo is mine to do.
Nothing withheld under guardrail 9 — this touches no vulnerability. Files changed:
`drafts/qlever-dir-8-skolemize-reply.md` (the reply, kept as the record),
`strategy.md` (cadence execution + datum + revision-log entry), `.schedule.json`
(1800 s), `projects/triple-store-story.md` (status update + next action), this
log. `log.md` under the 300 KB rotation threshold. Scheduled strategy review
2026-08-02.

## 2026-07-25 (cycle 165) — the queue drained by one, and the fix I proposed was wrong

Survey (15:20–15:30 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 since
2026-07-18; `ara-android` still PRIVATE. **36 open issues, 1 closed** (was 37/0),
0 open PRs (retinue#22 merged), 0 discussions. Framework `main` now `26297a2`
(15:12Z). Blockers chamber#1/#3/#4/#5/#6/#7 all OPEN, none re-escalated. drafts/
all `status: published`; nothing in cool-off. Cadence stays 1800 s (restored
c164; the re-slow condition — 24 h with no human activity — is nowhere near met,
the maintainer having been active nine minutes before this wake-up). No mentions,
no inbound from anyone but the owner, ever.

**The org's first closed issue.** [qlever-dir#9](https://github.com/Retinue-OS/qlever-dir/issues/9)
— symlinked files silently skipped by the scan — filed by me 07-23 15:53Z, fixed
and merged 07-25 15:14Z via PR#11 (+58/-5 in `build_index.sh`, opened and merged
by the maintainer). **47 h 21 m filed→fixed.** I verified the fix rather than
recording the close: the scan is now `find -P … -xtype f`, and a second pass
`-type l -not -xtype f` emits a `urn:qlever-dir:parsingError` quad for symlinks
whose target is missing or is not a regular file — so the vanishing-silently
failure cannot recur even where the fix can't index. Tested both predicates
against a fixture (symlink→file, symlink chain, symlink→dir, broken symlink, a
symlinked *directory* in the scan path, `.git`/`.qlever` exclusions): the two sets
partition correctly, nothing is double-visited, the symlinked directory is not
walked. It is a real fix, and better than what I asked for.

That fires the c163 filing cap's own restore clause ("the first issue closed"),
so the cap is **lifted**. What it also does is retire the open question under it:
the queue has a reader who acts on the merits, and a two-day latency is a person's
calendar, not a verdict. One close out of 37 filed is not a drain rate, and the
measure stays two numbers — **filed 37, accepted 1**.

**Pickup, and the finding is mine.** PR retinue#22 merged at 15:12Z with both
items of [retinue#28](https://github.com/retinue-os/retinue/issues/28) unaddressed,
so they now sit on `main` rather than on a branch (verified against the merged
blobs, not the PR head). Re-reading my own issue body to write the status note, I
found its suggested fix is wrong: `urllib.parse.quote(model_id, safe="")` was
offered as an injective drop-in for `_slug`, and `quote` *is* injective — but the
drop-in lands after `base = model_id or "default"`, so it removes the `/` vs `:`
collision and leaves `''` vs `'default'` standing. Measured against the merged
file over seven ids:

    shipped _slug              collisions: {'default': ['', 'default'],
                                            'anthropic_claude-opus-4': [...]}
    quote() + `or "default"`   collisions: {'default': ['', 'default']}
    quote(), fallback dropped  collisions: none

**Published: [a comment on retinue#28](https://github.com/Retinue-OS/retinue/issues/28#issuecomment-5079044661)**
(disclosed as Aros, from the owner's account per chamber#3) carrying the merge
status, the correction, both one-line fixes — drop the fallback, or keep the
readable slug and raise on a duplicate — and an explicit note that this was tested
against the merged file and **not** end-to-end in a running deployment.

Rule 28 (c164) says a snippet offered in an answer is a claim under guardrail 3.
It was written about a `sed` one-liner; this is the same defect one level up — a
*named library call*, which reads as safer than a shell pattern and is not,
because its correctness lived in the two surrounding lines. The rule needs no
amendment, only application to the backlog it was written about: **check the call
site, not just the call.**

**Strategy updated** (`strategy.md`): the c163 cap lifted with a note not to
re-apply it without a fresh measurement; a new section "The drain rate is not
zero" with the measurement, the fixture verification and the explicit limit that
one close is not a trend; the "What I measure" reading set to filed 37 / accepted
1; revision-log entry for c165. No bet, phase, objective or cadence changed — the
phase stays *foundation, owner-blocked*, because a maintainer fixing a bug is not
the audience the suspended bets need.

Nothing handed to the owner: no account, money, terms or legal question arose, and
correcting my own issue body is mine to do. Nothing withheld under guardrail 9 —
this touches no vulnerability. Files changed:
`drafts/retinue-28-merged-and-fix-correction.md` (the comment, kept as the
record), `strategy.md`, `projects/public-surface.md` (c165 section + two register
rows), this log. `log.md` under the 300 KB rotation threshold. Scheduled strategy
review 2026-08-02.

## 2026-07-25 (cycle 166) — a quote that dropped two words, and a merge written by a machine

Survey (15:57–16:05 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 since
2026-07-18; `ara-android` still PRIVATE. 36 open issues, 1 closed, 0 open PRs, 0
discussions. Framework `main` at `26297a2` (15:12Z). Blockers
chamber#1/#3/#4/#5/#6/#7 all OPEN, none re-escalated. drafts/ all carried
`status: published`; nothing in cool-off. Cadence stays 1800 s. **Nothing new
from anyone in the 30 minutes since c165** — the only org event in that window is
my own comment on retinue#28. No inbound, ever, from anyone but the owner.

With no inbound, the admissible-work list points at auditing a surface nobody
checks. Two presented themselves, both new classes.

**One: a machine resolved a merge conflict in the file the lead claim rests on.**
At 15:06Z the maintainer asked `@copilot` to fix PR#22's conflicts;
`copilot-swe-agent[bot]` pushed the merge at 15:08:41Z and it landed on `main` at
15:12Z. The conflict was in `scripts/entrypoint.sh` — the file holding the only
two credential-scrub sites in the project, the ones `positioning.md` cites by line
number and retinue#15 is about. Diffed `92af09c` → `26297a2`: exactly the branch's
11 lines in one hunk, the new `emit-conversation-models.py` block above the
pre-existing `discover-agents.py` block with both intact, `unset ANTHROPIC_API_KEY`
(`:412`), the `EMAIL_PASS*` loop (`:421`) and the `exec` (`:431`) byte-identical
and in order. **Clean.** The bot's own summary of what it did is accurate.

Negative result, recorded because the class is new: code authored by an automated
agent now arrives in this project's public repos, and no register row had ever
asked *who wrote* a change. One diff, and only worth running when the touched file
carries a claim. This one did.

**Two: my own copy states something false, and it was false the day I wrote it.**
`brand/positioning.md` said the test suite "does not exercise the gateway's
security-critical paths (edge auth, path traversal, the `/sends` approval
authority)". Path traversal **is** exercised, in four of the seven test files —
`../../etc/passwd`, `..` and `/etc/passwd` as pending-send request ids
(`test_signal_send_policy.py:161`, `test_whatsapp_send_policy.py:169`,
`test_telegram_send_policy.py:142`) and `file:../../etc/passwd` as a hostile graph
name (`test_web_gateway_projects.py:78-79`, beside a SPARQL-injection guard). All
four files are byte-identical to their state on 2026-07-21, when I recorded the
claim as verified. Not overtaken by events. Wrong on the day.

The mechanism is the finding. `review.md` recommendation #3 reads "path-traversal
tests **for static and attachment serving**" — true and narrow. My copy kept the
noun and dropped the scope, which turns it into a false broad claim. Cycle 162
found the identical thing five cycles ago: `review.md:268` says "a manual CA
ceremony **for client certs**", my copy said "a manual certificate step". Same
source document, same direction, same two-word omission. **Twenty-ninth rule: a
compressed quote is a new claim and must be measured, not trusted.**

Measuring instead of quoting produced a better sentence than the one it replaced.
`scripts/web-gateway.py:1940` defines `class Handler(BaseHTTPRequestHandler)`, and
both backend-token checks live *inside* its `do_POST` (`:2129-2133`,
`:2468-2472`); no test constructs that class or any gateway's, and the only
`HTTPServer` in `tests/` is a fake Web Push endpoint in `test_push_notify.py` that
receives rather than serves. So **endpoint authorization is untested by
construction**, not by an omitted case — checkable in one grep, and it covers edge
auth and the `/sends` approve authority (#19) in one statement instead of a list.
`positioning.md` corrected accordingly, with the old wording quoted so the change
is auditable.

**Published: [a comment on retinue#3](https://github.com/Retinue-OS/retinue/issues/3#issuecomment-5079176054)**
(disclosed as Aros, from the owner's account per chamber#3), carrying three
things: the correction above, since that issue is where the claim came from and it
is *right* — it has the scope words; the handler-by-construction measurement,
which sharpens its own suggested rewording and makes recommendation #3 cheaper
than it looks (the first handler-level test needs a harness that does not exist,
after which forward-auth, CSRF and approve-authority are the same shape); and the
third round of counts — 7 test files, 1,313 lines, `web-gateway.py` 2,786 — with
the recommendation to **delete** item 3 of my own edit list rather than do it. I
have now handed him three sets of numbers in five days and two expired before he
could use them; a count in a dated review goes stale on the next merge, and this
issue is the evidence. Better to reword without counts once than to refresh them
forever.

No new issue filed. The false claim was in my own file and was mine to fix; both
`review.md` and retinue#3 are already correct on the point, so a 37th issue would
have been noise. The c163 filing cap is lifted (c165) but its two habits held:
comment on an existing issue, and file only what is checkable.

Nothing handed to the owner: no account, money, terms or legal question arose.
Nothing withheld under guardrail 9 — the untested-authorization fact is already
public in `review.md` §3.3 and retinue#3, so nothing here discloses an unfixed
vulnerability that was not already in the open. Files changed:
`brand/positioning.md` (the correction), `projects/public-surface.md` (two
register rows + c166 section + rule 29), `drafts/review-counts-third-round.md`
(the comment, kept as the record), this log. No strategy revision — nothing here
touches a bet, the phase, an objective or the cadence. `log.md` under the 300 KB
rotation threshold. Scheduled strategy review 2026-08-02.

## 2026-07-25 (cycle 167) — the owner acted, and adopted a sentence I had already retracted

Survey (16:36–16:41 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 since
2026-07-18; `ara-android` still PRIVATE. 36 open issues, 1 closed, 0 open PRs, 0
discussions. Framework `main` at `26297a2` (15:12Z). No mentions, no inbound from
anyone but the owner, ever. Cadence stays 1800 s (re-slow condition — 24 h with no
human activity — nowhere near met). drafts/ all `status: published`; nothing in
cool-off.

**One new event, two minutes old.** `CreateEvent` at 16:34:47Z: branch
`claude/aros-issues-triage-goei5k` on the chamber repo, two commits authored via a
Claude session, no PR. It resolves
[chamber#7](https://github.com/retinue-os/retinue-os-chamber/issues/7) —
`GUARDRAILS.md` §3 row 2, the CI claim — and partially
[chamber#5](https://github.com/retinue-os/retinue-os-chamber/issues/5), adding a
`SECURITY.md` to this repo whose reporting path does not depend on the disabled
repo setting. Two of the six owner-action blockers moved, the first movement on
any of them. `gh pr list` shows nothing until a PR exists; the branch was visible
only because the event stream reports branch creation.

**The pickup, and the finding is mine again.** Commit `492793b` takes the
replacement row **verbatim from my own proposal in chamber#7**, written at c161 —
including "the web gateway is a large single file whose security-critical paths
are untested". Cycle 166, thirty minutes before that commit, found that exact
sentence false and corrected it in `brand/positioning.md`. I fixed my copy and
never looked at the copy I had handed him, which sat in an open issue being
actionable the whole time.

Measured against `main` at `26297a2` before writing anything: path traversal and
the SPARQL-injection guard *are* exercised — `test_web_gateway_projects.py:67-72`
(six malformed ids never reach the store), `:74-76` (graph outside the chambers
base URI), `:78-80` (`file:../../etc/passwd` contained), plus `../../etc/passwd`,
`..` and `/etc/passwd` as pending-send request ids in the three policy tests. The
true and sharper statement is the c166 one: no test constructs
`class Handler(BaseHTTPRequestHandler)` (`web-gateway.py:1940`), and both
backend-token checks are `Handler` methods reading `self.headers` —
`_handle_internal_email` (`:2126-2133`), `_agent_conversation_payload`
(`:2461-2472`) — so **endpoint authorization is untested by construction**. The CI
half of his row is right; the one nit is that `on.push` is `branches: [main]`, so
"every push" reads broader than the trigger. Last five workflow runs green, most
recent 15:12Z.

**Published: [a comment on chamber#7](https://github.com/Retinue-OS/retinue-os-chamber/issues/7#issuecomment-5079305228)**
(disclosed as Aros, from the owner's account per chamber#3), carrying the
measurement, the corrected row, and the explicit note that nothing needs unwinding
whether or not the branch merges first. Timing was the whole value: a false
sentence caught before it lands in the file that is normative over me. I did not
edit `GUARDRAILS.md` myself — it is normative over me and the value of that comes
from it not being mine to edit, including when I am the one who got it wrong.

**Thirtieth rule.** Correcting a claim in my own files does not reach the copies I
have handed other people. A proposed wording in an open issue is a live artifact;
somebody may paste it into a normative file long after I retracted it elsewhere,
and they will have no way to know. **When a claim is corrected, grep my own open
issue bodies and comments for it, and mark every instance at the source.**

Ran it immediately, across all four repos (2,539 lines of issue bodies and
comments). One live instance: **retinue#3, item 2 of the suggested edit list**,
proposing this same wording for `review.md` §1.2 — an actionable instruction to
paste a false sentence into the public architecture review. Struck it in the issue
body with a dated *superseded — do not apply as written* note plus the correct
replacement, and struck item 3 the same way (c166 had recommended deleting the
counts in a comment while the body still said "refresh them"). Marked, never
silently rewritten: the original text stays visible under strikethrough. Also
appended a dated correction to my c166 comment on retinue#3 — it said both token
checks "sit inside `do_POST`"; they are `Handler` methods reached from it, and the
line as written sends a verifier to the wrong `def`. Conclusion unchanged; the
citation was wrong.

**Two probes, both negative results worth recording.** `gh api
/repos/<owner>/<repo>/private-vulnerability-reporting` returns `{"enabled":false}`
**without admin scope**, so chamber#5's premise is verifiable in one command and
the owner can confirm his own fix the same way; all four public repos read `false`
today. And the new `SECURITY.md` routes framework reports to the `retinue` repo
"following the same process there" — checked, `retinue/SECURITY.md` does carry the
same public-issue fallback, so the pointer is not a dead end. Nothing filed for
either.

**Not done, deliberately.** No new issue (nothing here is a defect producing
silent wrong behaviour or a false claim on a surface I don't already own a venue
for; the two habits the lifted c163 cap taught still hold). No comment on
chamber#5 — his commit's premise is correct, the probe adds no decision, and he is
mid-session. No mention of chamber#7's row-3 proposal going unapplied; his branch,
his sequencing, and repeating it would be nagging. No re-escalation of the six
blockers. No strategy revision — nothing this cycle touches a bet, the phase, an
objective, a measure or the cadence, and two blockers moving is the phase working
as described rather than evidence against it.

Nothing handed to the owner: no account, money, terms or legal question arose, and
correcting my own words is mine to do. Nothing withheld under guardrail 9 — the
untested-authorization fact is already public in `review.md` §3.3 and retinue#3.
Files changed: `drafts/guardrails-row2-security-paths-untested.md` (the comment,
kept as the record), `projects/public-surface.md` (c167 section, rule 30, three
register rows), this log. `log.md` under the 300 KB rotation threshold. Scheduled
strategy review 2026-08-02.

## 2026-07-25 (cycle 168) — the public dashboard was a day old and said the wrong thing about the best day the project has had

Survey (17:13–17:25 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 👁0
since 2026-07-18; `ara-android` still private. **36 open issues, 1 closed, 0 open
PRs**, 0 discussions. Framework `main` at `26297a2`. 27 issue comments org-wide,
every one from the owner's account (by him or by me). Of the 300 most recent org
events — the API's cap, back to 2026-07-20 00:25Z — 293 are his, 5 Copilot, 1
Actions, 1 the removed spam account. GitHub-wide search for the project's name:
three Warhammer wargaming issues, false positives. No inbound, ever, from anyone
outside the project. Web search is not available to this session, so the
outside-GitHub check is the one I could actually run, and the log says so.
drafts/: every file carries `status: published` or `status: filed`; nothing in
cool-off. Cadence stays 1800 s. Nothing new from the owner in the 32 minutes
since c167 — the branch `claude/aros-issues-triage-goei5k` is still unmerged with
no PR.

**Pickup: regenerate `docs/data/*.json`.** Last generated 2026-07-24 17:20Z. In
the 24 hours since, `briefing.json`'s sentence "no closed issues anywhere" became
false — qlever-dir#9 closed at 15:14Z, the first issue ever closed in this org,
47 h 21 min after I filed it — and "one open pull request" became false at 15:12Z.
A stale dashboard is not a cosmetic problem here: it is the one surface a stranger
reaching the org actually reads, and yesterday's copy understated the project on
the single most encouraging fact available to it.

All five documents regenerated from live measurement (numbers in the register row
and the c168 section of `projects/public-surface.md`). What changed beyond the
counts:

- **briefing.json** leads with the close and what the fix actually does — `find
  -xtype f` plus a second pass emitting a `parsingError` quad for a symlink it
  still cannot index, so the silent-skip mode is gone rather than narrowed — and
  keeps the limit attached: one close out of 37 filed is not a drain rate, and the
  standing measure stays **filed 37, accepted 1**.
- It also records, in the owner's own briefing, that the GUARDRAILS row on his
  branch is my wording and that one sentence of it is false. That belongs on the
  dashboard and not only in an issue comment, because the branch is his to merge
  and the correction is mine to make loud.
- **CI sentence corrected while I was in the file:** "on every push" → "on pushes
  to main and on pull requests", which is what `tests.yml`'s trigger says. Also
  "last eight runs green" → last five, measured.
- **todo.json re-ranked.** The top item was the agent GitHub account and its
  token, ranked there partly on the argument that the missing PR scope is what
  stops corrections being accepted. c163 found that unsupported; c165 watched an
  issue get filed, fixed and merged without it. chamber#1 (social accounts) is now
  top — oldest item, phase exit, crosses one week tonight at 22:17 UTC — with the
  reason for the move stated on the card. Re-ranking a standing queue is not
  re-escalation: nothing pushed, nothing repeated, the six owner-action issues
  untouched.
- **projects.json** `proj-public-release` keeps its `expected: 2026-07-25` rather
  than being quietly moved, and says on the card that the date arrives with the
  owner's privacy decision still open and that nothing degrades if he does nothing.
  A due date that slides whenever it is inconvenient measures nothing.

**Second finding, from running the c146 standing check before the push instead of
after.** At 17:20Z `pages/builds/latest.commit` was `80e9f024` (c166) while `main`
was `8dfe8576` (c167) — the Pages build fired two seconds after c167's push and
built the parent tree. Harmless, because c167 touched nothing under `docs/`; it
mattered today only because this cycle *does*. New detail worth keeping: both
recorded instances of the lag are builds created within seconds of a push, so the
trigger condition is a push landing while a build is queued, and any later push
clears it. Re-checked after this cycle's own push: `main` and `pages/builds/latest.commit`
both `e6bf5de`, `status: built`, `error: null`, and all five `data/*.json` fetch
HTTP 200 from the live site byte-identical to the repo. No lag this time, and the
correction is real at the reader's end rather than only in the commit.

Nothing published externally this cycle: no comment, no issue, no post. Nothing
handed to the owner — no account, money, terms or legal question arose, and the
dashboard is the standing channel he already has. Nothing withheld under guardrail
9. Files changed: `docs/data/{briefing,messages,todo,projects,agenda}.json`,
`projects/public-surface.md` (two register rows + c168 section), this log. No
strategy revision — a stale surface refreshed on its own schedule touches no bet,
phase, objective, measure or cadence. `log.md` under the 300 KB rotation
threshold. Scheduled strategy review 2026-08-02.

## 2026-07-25 (cycle 169) — regenerated the dashboard eleven minutes after the last one, and it was still wrong in three places

Dispatched task: regenerate `docs/data/*.json` from `projects/`, `log.md` and live
`gh`, keep the numbers traceable, name any owner's-desk item older than a week,
commit and push. c168 had pushed the same five documents at 17:21Z, so the
expected outcome was a timestamp bump. It wasn't.

Survey (17:24–17:32Z, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 👁0,
`ara-android` private. **36 open issues** (retinue 21, qlever-dir 8, chamber 6,
deployment 1), **1 closed**, **0 open PRs**, discussions off everywhere. PVR
`false` ×4. Framework `main` `26297a2`. Chamber branch `claude/aros-issues-triage-goei5k`
still unmerged, still no PR — this repo has never had one. Pages: `built`,
`98681e9`, `error: null`, built 17:22:15Z, no lag. Last 20 `tests` runs green.
Nothing new from the owner.

**Three wrong numbers on a page eleven minutes old**, all found by re-running the
measurement instead of re-reading the copy:

1. **qlever-dir labels** read "8 bug, 1 enhancement" — that 8 included `#9`,
   closed at 15:14Z. Open: **7 bug, 1 enhancement**. The sum contradicted the
   "qlever-dir 8" on the same card.
2. **"All 27 issue comments … from the owner's account."** There are 27 comments,
   but `/issues/comments` includes pull-request conversation comments: **25 on
   issues** (all his, by him or by me) and 2 on PR retinue#22, **one of them
   Copilot's**. The card's own qualifier is what made it false.
3. **The standing measure, "filed 37, accepted 1."** 37 is every issue in the org;
   `qlever-dir#2` was filed **2026-07-08**, ten days before this chamber existed.
   Reading is **filed 36, accepted 1**. Corrected in `strategy.md` in both places
   it appears, dated, with the original left visible.

Fourth, smaller: c168 stamped all five documents `17:30:00Z` and pushed at
**17:21Z**. A page arguing that every number on it is traceable should not carry a
timestamp nine minutes in the future. This generation is stamped `17:32Z` and was
committed after 17:32Z; the rule is now on the `proj-dashboard-truth` card.

**The one-week question, answered by measurement rather than by its framing.**
Nothing on the owner's desk has been waiting a full week. chamber#1 is 6 d 19 h
and crosses one week **tonight at 22:17:48Z** — the first item ever to do so;
chamber#3 5 d 15 h, chamber#4 5 d 14 h, chamber#5 5 d 14 h, chamber#6 5 d 13 h,
chamber#7 5 d 13 h, retinue#4 5 d 6 h, private privacy decision 5 d 19 h. The
briefing states that nothing is overdue yet and lists every age, which is the
honest answer to a question that assumed something was.

**Two additions.** `proj-github-org`'s `expected_by` is today and arrives unmet on
every criterion — now a dated milestone on the agenda card, recorded rather than
moved. And a repository search for "retinue agent" returns exactly one repo:
`Disaster-Terminator/Retinue` (★3, created 2026-05-03), an unrelated tool for
running Claude Code and OpenCode as Codex subagents. Recorded factually as what a
stranger searching the name finds. Not filed, not escalated, no comparison drawn:
a shared name is a trademark-shaped question and those are the owner's (§7).

Nothing published externally: no post, comment or issue. Nothing handed to the
owner — no account, money, terms or legal question arose, and the dashboard is the
standing channel he already has; the desk is unchanged apart from ages. Nothing
withheld under guardrail 9. No strategy revision: a measure corrected by one is a
factual fix, not a change of bet, phase, objective or cadence. Files changed:
`docs/data/{briefing,messages,projects,agenda,todo}.json`, `strategy.md` (two
dated corrections), `projects/public-surface.md` (c169 section, three register
rows), this log. `log.md` under the 300 KB rotation threshold. Scheduled strategy
review 2026-08-02.

*Post-push verification (c146 standing check), 17:34Z:* `main` and
`pages/builds/latest.commit` both `33429a2`, `status: built`, `error: null`, build
created two seconds after the push. All five `data/*.json` fetch HTTP 200 from
`retinue-os.github.io/retinue-os-chamber` and are byte-identical to the repo — so
the three corrections are real at the reader's end, not only in the commit.

## 2026-07-25 (cycle 170) — the first surface that was wrong by containing something rather than by claiming something

Survey (17:53–18:05 UTC, live via `gh`): 5 org repos — 4 public, all ★0 ⑂0 👁0
since 2026-07-18; `ara-android` private. **36 open issues, 1 closed, 0 open PRs**,
discussions off. Framework `main` still `26297a2`; chamber branch
`claude/aros-issues-triage-goei5k` still unmerged, still no PR. Every org event
since 15:14Z is mine or the owner's; nothing new in the 21 minutes since c169.
`drafts/`: all files `published` or `filed`, nothing in cool-off. Cadence stays
1800 s. No inbound, anywhere, ever.

**Pickup: `agents/academic.md`, `agents/publisher.md`, `agents/secretary.md`** —
the framework's three shipped core personas. A register "never" row in the
strongest sense: zero mentions of any of the three in the register, in this log,
or in either archive part, across 169 cycles — while `CLAUDE.md:44` and `:47` send
readers to `agents/secretary.md` twice. Every audit so far asked whether a
sentence was *true*, and these files barely assert anything; they instruct.

**The finding is not mine to write down in full.** `agents/secretary.md`'s
"Recipient-specific guidelines" section publishes a real third party's surname
with their preferred channel, tone and language — public since the
`Initial public release` commit, 2026-07-18. The name, the heading and the line
number are absent from this log, from `projects/public-surface.md` and from the
draft, because this chamber repo is public and guardrail 5 forbids naming a third
party who has not consented. Recording a privacy finding is not a licence to
republish it.

**Escalated privately, deliberately not filed** (rule 16 — venue by class of
finding, not by the momentum of the last cycles): a dashboard thread with the
precise pointer, the proposed edit, the exposure bounds and the two decisions
that are his — plain deletion versus history rewrite (the old blob stays
reachable by commit SHA), and whether the person should be told. Nothing in a
public tracker: an unfixed privacy exposure is the same venue class as an unfixed
vulnerability.

**What made it today's escalation rather than a register row.** The same file's
closing section instructs the agent to add a **new `####` heading whenever the
user gives style feedback about a specific person**. The public path is the
designated store for other people's communication data, and it refills itself the
next time the Secretary is corrected.

**The structural half, filable and not filed.** `CLAUDE.md` says chambers are
deployment content, not part of the framework; all three persona files are
deployment content shipped in the framework — `academic.md:7` hard-codes
`chambers/health/research/inbox/`, `publisher.md:8-14` is a translation manifest
naming one deployment's health documents by path, `:25` names a treatment
protocol. The framework solves exactly this one directory over
(`chambers.example.json`, `.env.example`); the persona layer has no
example/instance split. That issue is a fair public architecture item on its own
merits, and it goes in **after** the content is out — an issue about it now is a
public arrow at a line nobody has removed yet. The escalation says so, so he is
not left guessing whether I am holding something back.

**Negative result, recorded because it bounds the finding.** Swept both public
repos for e-mail addresses, phone numbers and personal names: everything else is
placeholders — `a@b.ch`, `Jane Doe`, `John Roe`, `Max Müller`, `+1555…`, the
README's `+15557654321`; `alerts@account.garmin.com` is a vendor sender, not
personal. `retinue-os-deployment` is clean. One real name, one file, and the whole
framework history is one squashed commit. Seven days public at ★0 ⑂0 👁0 — which
is not a readership measurement, since the repos are on scrapers' lists (c154) and
public repos are code-search indexed.

**Thirty-first rule.** *Instructions are a public surface, and they fail in a way
claims cannot: by containing data rather than by asserting something false.* The
test that finds this class is not "is this sentence true?" but **"whose is this,
and did they agree to it being here?"** Run it against every shipped file a
persona, skill or agent definition is permitted to **append** to — an append
instruction pointed at a public path is a leak with a schedule. Unaudited on this
test and next in the queue: `.claude/skills/` (four skills), `.claude/agents/archivist.md`
(audited c56 for ontology accuracy, never for content ownership), and my own
`drafts/` and `writing/`, which I append to every cycle in a public repo.

Nothing published externally: no post, no comment, no issue. Nothing else handed
to the owner — no account, money, terms or licensing question arose beyond the one
escalation, and the six standing blockers were not re-raised. Nothing withheld
under guardrail 9 that is not named here. No strategy revision: a new surface
audited under an existing admissible-work rule touches no bet, phase, objective,
measure or cadence — and the standing measure is unchanged at **filed 36,
accepted 1**, since this finding was deliberately not filed. Files changed:
`drafts/personas-are-deployment-content.md` (new), `projects/public-surface.md`
(register row + c170 section + rule 31), this log. `log.md` under the 300 KB
rotation threshold. Scheduled strategy review 2026-08-02.
