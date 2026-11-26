---
type: project
id: proj-claim-verification
title: "Verify the claims before publishing them"
goal: "Every load-bearing claim in brand/positioning.md has been run, not just read."
goal_status: in_progress
current_next_action: "Owner: rule on the THREE open findings routed privately — two from 2026-07-19, one added 2026-08-01 (c340) on dashboard thread a9eba696. Aros holds a patch and test cases ready to write for the first two, and a suggested fix plus a cheaper interim for the third. Meanwhile the affected claims keep their previous status here and nothing false is published while they wait. NEW, and it is a method change rather than a claim: a verified row has an EXPIRY. The 2026-07-31 merges moved 21 files / 2 123 insertions under rows verified in cycles 6-11, and re-running two of them against Retinue-OS/retinue @ f1f8c72f produced the third finding. This table has no baseline field; baseline-check tracks commit baselines for held DRAFTS and nothing tracks them for VERIFIED CLAIMS, which is the stronger artifact. Proposed to the 2026-08-02 review, not built in an idle slot."
current_actor: actor-owner
waiting_since: 2026-07-19
expected_by: 2026-08-16
paused: false
category: credibility
---

# Verify the claims before publishing them

## Goal
Every load-bearing claim in `brand/positioning.md` has been **executed** by Aros
at least once, not merely read out of the documentation.

## Why this project exists
Guardrail 3 makes claims-must-be-true binding on marketing copy, and the
project's credibility rests on the gap between what it claims and what it does
being zero. Reading the docs cannot establish that gap is zero — the docs are
one of the things being checked. The foundation phase is credibility work, and
this is the cheapest form of it available while there is no audience.

It also has a second payoff: verification finds real defects, and a defect found
by the project's own comms agent before an outsider finds it is worth more than
a post.

## Method
For each claim: construct the failing case as well as the passing one. A claim
that only holds for well-formed input is a weaker claim than the docs make, and
the difference is exactly what an outsider would publish.

## Claims and status

| Claim (`brand/positioning.md`) | Status | Notes |
|---|---|---|
| Outbound sends gated by policy keyed to the sending identity | **verified** 2026-07-19 | Holds. Category resolves from the sending account, not the recipient, in all four gateways. |
| Undeclared accounts fail safe to "needs approval" | **verified with one caveat** 2026-07-19 | Holds for every case the docs describe: unset policy, empty policy, absent account, unparseable JSON. One class of input where it does not hold — routed privately to the owner (see below), not recorded here. |
| ~~An agent can never approve its own send~~ — **withdrawn from `positioning.md` 2026-07-19** | **claim retired** | The absolute no longer appears in the positioning doc. The clause now states only what the policy mechanism does. No result is recorded here; see "Open findings". |
| Credentials live only in sidecars, never in the model's context | **verified, with a calibration** 2026-07-19 | Inspected this container's own environment. **Every** messaging/personal credential is absent: `SIGNAL_ACCOUNT`, `SIGNAL_KEY`, `WHATSAPP_ACCOUNT`, `WHATSAPP_SESSION`, `TELEGRAM_API_ID/_HASH/_SESSION`, `SMTP_USER/_PASSWORD`, `IMAP_USER/_PASSWORD`, `EMAIL_PASSWORD` — not empty, *absent*. `ANTHROPIC_API_KEY` absent; `OPENROUTER_API_KEY`, `LITELLM_MASTER_KEY`, `LITELLM_DB_PASSWORD` present but empty. What **is** in context: `EMAIL_BACKEND_TOKEN`, `CONVERSATION_BACKEND_TOKEN` (capability tokens for sidecars, still policy-gated, internal network only) and `GITHUB_TOKEN` (a real external credential, len 93). So the claim is true as written about account credentials, and would be an overclaim if read as "holds nothing sensitive". `positioning.md` clause 1 rewritten to say the precise version. |
| Egress audit observes but does not enforce | **verified, and the claim understates the weakness** 2026-07-19 | Ran a proxied and a bypassing request to the same host, seconds apart. Both returned 200; the bypass terminated at a public IP, not the sidecar. The audit logged the proxied one and has **no record at all** of the bypass. So it is not just unenforced — a bypass is *unobserved*. Written up in `writing/egress-audit-observes.md`. Not a disclosure: `review.md` §3.2 already states the mechanism publicly. **Re-run 2026-07-29 (cycle 250): identical, down to both remote addresses — `172.25.0.3` proxied, `172.66.147.243` bypassing — and the bypass again absent from a log then holding 79,114 flows.** Two defects found in the *instrument*, not the result: the published log query (`?limit=2000`, no filter) now returns 2,000 records ending at 03:40:29Z and never reaches the probe, and the log contains a `probe=bypass` flow from 2026-07-28T16:09:04Z that my own link checker made *through the proxy* by fetching a URL scraped out of this essay's code block. Both fixed in the piece. |
| Named graph derived from file path; move a file and provenance follows | **verified** 2026-07-19 | Ran it, did not trust it. `git mv` of `sensor-a/readings.nt` into `sensor-c/`, no edit to the file's two triples. `urn:demo:obs:a:1` moved graph from `file:retinue/docs/examples/provenance/sensor-a/readings.nt` to `…/sensor-c/readings.nt` with no migration step. Moved back; store restored to the identical pre-test state. Demonstration added to `writing/provenance-by-path.md`, replacing an assertion that had rested on the docs. |
| Blue-green reindex catches up in ~15s | **verified 2026-07-19 as 15–20s; re-measured 2026-07-25 at 20–25s — restate as "tens of seconds"** | Polled at 5s intervals across three separate rebuilds: old value at t+15s, new value at t+20s, every time. So "~15s" is not wrong but rounds the wrong way; I state 15–20s for a small file. **The load-bearing caveat is what starts the clock:** only a native RDF file event does. A new Markdown file sat unindexed for 32 minutes (`projects/claim-verification.md`, committed 22:07, absent at 22:39) and a probe `.md` stayed at zero triples for a full 60s poll — then appeared within 20s the moment an unrelated `.nt` write triggered a rebuild. That is qlever-dir#3 observed from the other side, and it means the latency figure only holds for RDF. **Re-run 2026-07-25 (cycle 174), same deployment, same host, same two-line trigger file: (20, 25] s, (20.1, 22.1] s, (20.1, 22.1] s — every rebuild above the 2026-07-19 upper bound.** The chamber grew 340 KB / 38 files → 1.4 MB / 64 files in between while the indexed triple count barely moved (49 → 59), so it is not index size and the cause is not isolated. Six rebuilds over two dates span 15–25 s, which is a spread, not a scaling law: the claim is now stated as *tens of seconds, growing with the chamber*. Posted on [retinue#2](https://github.com/Retinue-OS/retinue/issues/2#issuecomment-5080475657) as a correction to my own unmerged branch, which would have replaced one unsupportable number with another. |
| Not model-agnostic; coupled to Claude Code | **re-affirmed 2026-08-09 (c687), against an owner challenge; recalibrated 2026-08-15 (c768) on his second reply** | The owner commented on `.github#1` that calling Retinue "not model-agnostic" is misleading since it "can run on ollama and even [shims] with litellm." Checked before answering: `litellm/config.yaml` on `retinue-os/retinue@main` defines exactly one non-Claude route, `retinue-openrouter`, used as subscription-failover — not a general model-swap path. Code search for `ollama` across the repo: **0 hits**. `review.md:202-218` (§3.4) — binding per guardrail 3 — calls Claude Code coupling *"the project's deepest dependency"* and states the LiteLLM failover path itself "adds terms-of-service gray area," i.e. treats it as a risk, not evidence of portability. Replied on the issue with the citations and asked the owner for a concrete counter-example (a working Ollama route or deployment) rather than change the claim on an unverified premise — that would trade one uncalibrated claim for another. No edit made to `writing/org-profile-README.md` or the live org README pending his answer. **Resolution, 2026-08-15 (c768).** His reply ([issuecomment-5303507398](https://github.com/Retinue-OS/.github/issues/1#issuecomment-5303507398)) split the layers correctly: *"any backends that provides anthropic compatible endpoints can be used … We do however depend on the Claude code as harness."* Both specifics verified against primary docs the same wake-up: Ollama documents an Anthropic-compatible `/v1/messages` endpoint naming Claude Code explicitly; LM Studio documents the same shape with a "Using Claude Code with LM Studio" walkthrough. My c687 hold-out was about repo evidence, and it stays true — no shipped route, 0 `ollama` hits — but it answered a question about the *repo* when his claim was about the *harness*, so "not model-agnostic" over-claimed by one layer. Profile README bullet renamed **"Not harness-agnostic"** (commit [`b06f7bf`](https://github.com/Retinue-OS/.github/commit/b06f7bf71374783cb748013ed3fa0809122219e7)), chamber source and `brand/positioning.md` updated in step; the caveat kept: backend flexibility is stated as those backends' documented capability, never as a Retinue feature, because Retinue ships and has tested no such route. Reply with citations: [issuecomment-5303821465](https://github.com/Retinue-OS/.github/issues/1#issuecomment-5303821465). |

## Open findings — deliberately not detailed here

**2026-08-01 (cycle 340).** Two rows of the table above were **re-run** — not
re-read — against `Retinue-OS/retinue @ f1f8c72f`, because the code they were
originally executed against had moved by 21 files and 2 123 insertions in the
five merges of 2026-07-31. One of them produced a result that is **unfixed**, so
neither the finding nor *which row produced it* is recorded here, on the same
reasoning as the 2026-07-19 entry below: naming the row would narrow it enough to
be a disclosure on its own, and this repo is public. **Both rows keep their
previous status** rather than recording a pass or a fail the public record cannot
support; the affected one is corrected once the owner has ruled and fixed.

Routed privately, appended to the existing send-control dashboard thread
(`a9eba696…`) rather than opening an eleventh unread tab. The
`SECURITY.md` route was tried first and refused:
`POST /repos/Retinue-OS/retinue/security-advisories` → 403, *"Resource not
accessible by personal access token"* — the same 403 the owner's token returned
on 2026-07-19, and the first permission that has turned out **identical** across
the two identities rather than different (cf. c310, c311, c315). Reading
advisories works.

**The transferable part, which is not a disclosure.** A verified row is a
measurement with a date, and this file records the date but not the **commit**
the measurement was taken against. `tools/baseline-check.py` does exactly that
for held drafts, and nothing does it for claims — the stronger artifact of the
two, since `brand/positioning.md`, `writing/org-profile-README.md` and every
public surface derive from this table rather than from `drafts/`. Rows whose
subject is **code** expire fastest: prose ages when someone edits that prose, a
mechanism ages when anyone touches any file that implements it. Handed to the
2026-08-02 review as a proposal rather than built in an idle slot (c268 rule 2
admits it — the surface it watches is one a reader meets — but a build is not an
idle-slot decision).

**2026-07-19 (second).** A further claim was run this cycle and the result is
**unfixed**, so neither the finding nor *which claim produced it* is recorded
here — naming the claim would narrow it enough to be a disclosure on its own.
Routed privately to the owner, appended to the existing dashboard thread rather
than opening a second one. The affected row below stays at its previous status
rather than recording a pass the evidence does not support; it is corrected once
the owner has ruled and fixed.

**2026-07-19.** Verifying the fail-safe claim turned up one defect in the
send-control model. It is **unfixed**, so per guardrail 9 it is not described in
this repo, which is public — no mechanism, no reproduction, no file references.

Routed privately to the owner via the dashboard, with reproduction, an honest
severity assessment (not remotely exploitable; needs operator misconfiguration),
and a suggested fix. Attempted the SECURITY.md channel first — a private GitHub
security advisory — and the token returned 403, the same missing scope that
blocks PR creation.

Nothing about this goes public until the owner has fixed it and says so.

## Standing constraint discovered here
**This chamber is a public repo.** `log.md`, `drafts/` and `projects/` are
published the moment they are committed. They are working notes in form but
disclosure in effect. Anything unfixed and security-relevant must therefore go
to the dashboard and stay out of every tracked file — including drafts, where a
cooling-off piece would otherwise sit in public for a full cycle.

## Documentation audit — 2026-07-19 (eleventh cycle)

The claim table above is complete, so this cycle audited the other direction:
**do the project's own public docs match the six verified claims?** A wrong
number in the README outranks a right one in this chamber, because the README is
what a first reader actually reads.

Audited `README.md`, `docs/triple-stores.md` and `CLAUDE.md` against the verified
results and against guardrail 3's forbidden-claim table.

**The clean result, worth recording as such:** `README.md` contains no instance
of *secure*, *hardened*, *audited*, *production-ready*, *guarantee*, *enforce*
or *just works*. The forbidden vocabulary is simply not there. Guardrail 3's
main risk in this project is not adjectives — it is unrun numbers.

**One defect, in three parts, all in `README.md` step 4:**

1. `~15 s` — rounds the measured 15–20 s toward the flattering end.
2. Describes the store as indexing only `.nt`/`.ttl`/`.n3`, omitting
   converter-declared extensions — i.e. omitting the frontmatter mechanism that
   `docs/triple-stores.md` is largely about and that the README itself links at
   line 39. The most novel part of the system is missing from its own summary.
3. "watches for filesystem changes" implies any change triggers a rebuild. Only
   native RDF changes do.

`docs/triple-stores.md` already carried the Markdown-staleness caveat, honestly
stated — it just repeated the rounded `~15 s`. Corrected to 15–20 s.

**Superseded 2026-07-25 (cycle 174), and the branch has not been rewritten.**
The re-measurement above puts every rebuild today above 20 s, so the branch's
replacement text ("15–20 s for a small file") is now itself unsupportable. The
suggested wording is *tens of seconds*, posted as a comment on retinue#2 rather
than force-pushed over a branch a reviewer may already be looking at — and the
token cannot update a pull request in any case (chamber#6).

**Delivered as:** branch `docs/calibrate-reindex-latency` (commit `5ab0ecb`,
docs-only, 2 files), pushed. PR creation returned
`Resource not accessible by personal access token` — the same missing scope that
blocked the private security advisory. Carried instead as
[retinue#2](https://github.com/retinue-os/retinue/issues/2), which states the
owner action: merge the branch, or grant PR scope. Labelled `documentation`;
the repo has no `owner-action` label.

Note the asymmetry this exposes: I can file issues but not open PRs, so my
corrections arrive as prose asking someone to act rather than as a diff someone
can merge. That is a real drag on the "corrections accepted into the repos"
measure in `strategy.md`, and the review should weigh it.

## Owner-PR review, 2026-11-25 (bet 5 operating clause)

retinue#437 (continuous-mode take cues, cap raised from 120 s to 4 min default,
30 min max), read at `bea2da01`. One note posted, distinct from Copilot's three:
the transcription path's limits (`TRANSCRIBE_TIMEOUT` 120 s, 25 MiB upload caps,
worker `DICT_TIMEOUT_MS` 4 min) are unchanged and a failed transcription keeps
no audio. Read from code, no long take run, stated as such.
https://github.com/Retinue-OS/retinue/pull/437#issuecomment-7149379951
Counter for bet 5's falsification clause: 0 (checkable content found). Next
check: whether a later commit or reply addresses it.

retinue#428 (archive the answered mail on /sends approval), read at `ed6739cc`
the same day. One note: `move_by_message_id` moves the last hit of a substring
header search without comparing the Message-ID. Distinct from the expunge
finding already on the PR. Read from code, not run against IMAP, stated as such.
https://github.com/Retinue-OS/retinue/pull/428#issuecomment-7154894522
Counter: 0. Next check: whether the fix commit compares the header exactly.

retinue#443 (mail Original links in the Android app), read at `7521a1a7`
(2026-11-25 07:02Z run). Checked against code: `ara-android` main sets
`setSupportMultipleWindows(false)`; `UrlRouter.route` sends an off-origin
main-frame http(s) address to the browser and `shouldOverrideUrlLoading` carries
that out; `_safe_href` admits only absolute http(s) and mailto targets. The
PR's description of the fix matched on those points. Tests not run, nothing
tried on a phone. No comment posted (clean review, per the 08-16
clarification). Counter: 0.

retinue#436 (paged Archived threads), read at `60b2c820` (2026-11-25 07:35Z
run). One note, distinct from Copilot's two: the client widens `limit` by 50
with no offset while the gateway clamps it to 500, so threads past the 500th are
unreachable on the tab and "Load more" stays without effect. Read from code, not
run, stated as such.
https://github.com/Retinue-OS/retinue/pull/436#issuecomment-7156047433
Counter: 0. Next check: whether a later commit pages by offset or lifts the clamp.

retinue#444 (chat actions on every tab, mail spam, multi-select), read at
`6ae0cb5` (2026-11-25 08:06Z run). One note, distinct from Copilot's three: a
deferred bulk Spam goes through `eachBounded` with limit 4, so on `pagehide`
only the first 4 requests are issued and the rest are dropped with the page.
`eachBounded` run alone under node with a never-resolving callback: 4 of 7 calls.
Not tried in a browser.
https://github.com/Retinue-OS/retinue/pull/444#issuecomment-7156657914
Counter: 0. Next check: whether a later commit issues all requests on
`keepalive`. Not a full review of the 21 files (mainly the gateway diffs and the
deferred-commit path).

retinue#444 follow-up (2026-11-25 08:39Z run). retog confirmed the 08:06Z note
and fixed it in `48aae26` (reply 08:10:23Z). The fix covers a page left while the
Undo toast is up. One narrower case posted: once the toast has lapsed,
`pendingCommit` is null, so `pagehide` does nothing while the bounded queue is
still draining. Node harness (stubbed DOM, real `swipe-rows.js` and
`eachBounded`, never-resolving requests): 4 of 7 issued. Not tried in a browser;
drain time not measured.
https://github.com/Retinue-OS/retinue/pull/444#issuecomment-7157341246
Counter: 0. Next check: whether he addresses or declines it.

retinue#444 follow-up outcome (2026-11-25 09:11Z run). retog confirmed the
narrower case and fixed it in `ccfc5b2` (reply 08:42:20Z). Diff read; its `test`
check succeeded; not re-run by me. No further comment.

retinue#438 (chamber apps), read in part at `81e3ffc` the same run:
`calendar_trigger.py` and the `scheduler.py` diff only, not the gateway, client
or service worker. One note, not among the review comments searched: the serial
tick loop lets a long job push a reminder past its `lead`, recorded `missed`
with the container up. Simulation with fake clock and stubbed `run_job` (10 min:
fires; 17 min: `missed`); no real deployment.
https://github.com/Retinue-OS/retinue/pull/438#issuecomment-7158047965
Counter: 0. Next check: whether a later commit moves reminders off the serial
loop, or the docs state the limit.

retinue#423 (2026-11-25 09:44Z run): not reviewed and dropped from the unreviewed list. Draft; retog's 11-23 comment says it is kept as the record of an exploration, not the plan. Revisit only if it is reopened as a proposal.

ara-android#30 (chamber apps, Android side; 2026-11-25 10:16Z run), read in part
at `288cd7c`, with the server skip path of retinue#438 at `81e3ffc`. One note,
distinct from Copilot's inline comments on #30: `skip` cancels no local alarm
when the post fails, and the queued `{}` body is dated by the server at
processing time, so a late flush skips the wrong day. Only `skip_today` and
`_prune` were run (fixed clock, stubbed zone helpers); no device.
https://github.com/Retinue-OS/ara-android/pull/30#issuecomment-7159506500
Counter: 0. Next check: whether a later commit sends the date or occurrence.
ara-android#29 not reviewed.

ara-android#29 (settings and Back stay in the app; 2026-11-25 10:48Z run), diff
read at `cf9e74c1` plus `UrlRouter` and parts of `MainActivity` and
`ShellWebClients`. No finding of my own beyond Copilot's StartPage history
comment, which was not repeated. Tests not run, no device. No comment posted
(clean review). Counter: 0.

2026-11-25 11:21Z run: no review. Open PR heads I had reviewed or read were
unchanged; bet 5 counter stays 0.

2026-11-25 11:52Z, 12:24Z and 12:56Z runs: no review. Open PR heads I had reviewed or
read were unchanged; bet 5 counter stays 0.

2026-11-25 13:58Z run: no review. Open PR heads listed in the 13:58Z log entry
were unchanged; bet 5 counter stays 0.

2026-11-25 15:34Z run: no review. Open PR heads in retinue and ara-android showed no
change from those listed in earlier log entries; bet 5 counter stays 0.

2026-11-25 16:06Z run: no review. #411 (owner's own review of 11-23 stands) and
#423 (marked exploration by him) not reviewed by me; no head change seen on the
others. Bet 5 counter stays 0.

retog's review pass (read in the 2026-11-25 16:38Z run). retinue#428 re-review
(head `ed6739cc`) agrees with my 06:32Z note on the substring Message-Id match
and lists it as blocking: accepted as a finding, not yet fixed.
https://github.com/Retinue-OS/retinue/pull/428#issuecomment-7168317754
His "fix before merge" comments on #436, #437 and #438 do not mention my notes
(500-thread clamp, transcription limits, serial tick loop); not re-raised. #444
merged after both points had been fixed. #445 merged before this run read it; no
note from me.

retinue#443 (merged): his review asked to confirm that the Android app hands
every off-origin URL to the browser. Read `ara-android@7839f11` (`ShellPage.kt`,
`ShellWebClients.kt`, `UrlRouter.kt`, `ShellIntents.openInBrowser`) and the #29
change at `cf9e74c`: an off-origin main-frame http(s) navigation is not loaded in
the dashboard WebView; it goes out as a VIEW/BROWSABLE intent. No tests run, no
device.
https://github.com/Retinue-OS/retinue/pull/443#issuecomment-7168362911
Counter: 0.

2026-11-25 17:11Z run: retog's 17:12Z status comment on retinue#438 says my
missed-reminder point was "confirmed and fixed in 62e94c4".
https://github.com/Retinue-OS/retinue/pull/438#issuecomment-7169157831
Read the commit diff and the relevant functions of `scripts/scheduler.py` at
`62e94c4`: app reminders run on their own daemon thread, so an inline prompt or
command job no longer delays them. Tests not run. Two small edges seen, by reading
only, not posted: both loops call `load_jobs()`, so its unthrottled manifest
warnings are now logged by both; an app job re-declared from prompt to reminder
while the old run is still going could have its state written by both loops.

Still present by reading at the new heads: retinue#436 `e32edb8` (the client
widens `limit` with no `offset`, the gateway clamps it at 500) and
ara-android#30 `84a4549` (skip posts `{}`; `skip_today(j, now)` at retinue#438
`62e94c4` dates it at processing time; local alarms of the day are not cancelled
in `skip`). No status comment on either PR yet, so not re-raised. Next run: look
again once they have one or are merged. Counter: 0.

2026-11-25 17:44Z run. retog reports both outstanding notes confirmed and fixed:
ara-android#30 skip in `17323cd` plus retinue#438 `fcd5796`
(https://github.com/Retinue-OS/ara-android/pull/30#issuecomment-7169870872), and
the Archived 500 clamp in retinue#436 `57d57e1`
(https://github.com/Retinue-OS/retinue/pull/436#issuecomment-7169780411). With
the #438 scheduler fix (`62e94c4`), three notes of mine are reported fixed by him
this day. All three PRs open at this read. Diffs of `57d57e1`, `fcd5796` and
`17323cd` read; no tests run; retinue `test` checks still in progress, Android
build and unit tests succeeded.

One narrower case remains on ara-android#30 `17323cd`, by reading only (plus the
kotlinx `withContext` documentation): receiver budget 9 s, HTTP call timeout
20 s, so a POST that stalls past 9 s throws `CancellationException` before
`enqueue`; `refresh` holds the lock `skip` needs across network calls.
https://github.com/Retinue-OS/ara-android/pull/30#issuecomment-7169985044
Counter: 0. Next check: whether he addresses or declines it. #436 and #438 fixes:
nothing further seen by reading, no comment.

2026-11-25 18:17Z run. The "next check" above is answered: retog reports my
stalled-request note fixed in `acab173` (outbox first, no request under the
alarms' lock), CI build and unit tests succeeded. Diff `17323cd..acab173` read,
nothing run, no device. Found in it: an outbox entry without an `id` draws a new
UUID on each parse, so `removeFromOutbox` never matches it and it is resent until
a new action is enqueued. Only phones that queued under an earlier branch build
(`ReminderRuntime.kt` is not on `main`); a pre-`17323cd` skip posts `{}`.
https://github.com/Retinue-OS/ara-android/pull/30#issuecomment-7170737397
Counter: 0. Next check: whether he addresses or declines it.


2026-11-25 18:49Z run. The "next check" above is answered: retog reports the
legacy-id note fixed in `44481af` (name-based id for entries without one; undated
legacy skips dropped on read). Diff `acab173..44481af` and the outbox code at
that head read, plus the reminder-body lines of the PR's earlier commits; CI
build and unit tests passed; nothing run by me, no device. The fix holds by
reading: the legacy id is the same on every parse, current entries keep their
stored id, `skipBody` never yields `{}`, so the drop rule reaches only the old
shape. No comment posted (clean check).
Counter: 0. Next check: none pending on this note.

2026-11-25 19:21Z run: no review. retinue#436 and #438 merged (19:20Z, 19:21Z) at
`57d57e1` and `fcd5796`, the heads carrying the fixes for my notes. His closing
comment on #438 keeps one nit (arming via GET) as a follow-up; not my finding.
https://github.com/Retinue-OS/retinue/pull/438#issuecomment-7172194560
ara-android#30 still open at `44481af`. Counter: 0.

2026-11-25 19:53Z run: no review. retinue#411 and #437 merged, #428 closed
unmerged as obsolete (his comment, 19:52Z); no note of mine pending on the three
per the entries above. ara-android#30 listed as last updated 18:20Z. Counter: 0.

2026-11-25 20:24Z run: reviewed retinue#447 (chat triage, head `d60aed3`), view
code, gateway diff, module and design doc, by reading; nothing run. Two notes:
mixed-section "Delete all" label says only that mails move to the Trash (same
expression on `main`'s select bar; `_triArmed` also survives polls), and action
rows link to `pane=ara` with `CHAT_TRIAGE_FOLLOWUPS=0`, the default, with the
doc table and PR description still describing follow-ups.
https://github.com/Retinue-OS/retinue/pull/447#issuecomment-7173691737
Counter: 0. Next check: whether he addresses or declines them.

2026-11-25 20:58Z run: read retinue#448 (head `069cd71`), the follow-up PR for my
#447 notes: `chats.js` and design-doc diff, plus the follow-up states in
`chat_triage.py`, by reading; CI `test` succeeded; nothing run. Both notes are
fixed (three-way delete wording; "see Ara" and `pane=ara` only for queued,
working or done), as are the stale arm across polls and Copilot's two points. No
new finding, no comment posted. Not read: the test file and `webapp/README.md`
diffs. Counter: 0. Next check: none pending on these notes.

2026-11-25 21:29Z run: reviewed retinue#449 (triage feedback notes, head
`7e528e1`), by reading `chat_triage.py`, the gateway handlers, `chats.js` and
the doc diff; test diffs not read; nothing run. Three notes: save-then-502
shows "not saved" and a retry duplicates the note; `_batch` reads notes per
batch, against "the next press uses it"; the typing guard misses the 15 s list
refresh. https://github.com/Retinue-OS/retinue/pull/449#issuecomment-7175198064
Counter: 0. Next check: whether he addresses or declines them, and thread
`b4a3f76c`.

2026-11-25 22:01Z run: read the fixes for my three retinue#449 notes in the diff
`7e528e1...9a97c8a` (merged 21:53Z as `ba5d2f6`): chats read before the note is
saved; notes taken once per run; one typing guard shared by list refresh and
triage poll. All three hold by reading; nothing run; `test` on `ba5d2f6` in
progress. No comment posted. One follow-up appended to thread `b4a3f76c`.
Counter: 0. Next check: the owner's answer on that thread.

2026-11-25 22:34Z run: reviewed retinue#451 (a pressed reply reads the chat,
head `77edf59`), gateway and page diffs and the two prose docs, by reading;
Python test diffs not read; nothing run. Two notes beyond Copilot's three
threads: `docs/mail-chats.md` ("Unread / Read / Archived") and the module
docstring of `tests/test_chat_mail_send.py` still state the old rule; and
`_recheck` reaches `_readByReply()` on a repeat the gateway does not read, so
the page shows a newer mail as read until a poll.
https://github.com/Retinue-OS/retinue/pull/451#issuecomment-7176581010
retinue#450 and #452 opened in the same window, not reviewed. Counter: 0.
Next check: whether he addresses or declines the two notes.

2026-11-25 23:07Z run: reviewed retinue#454 (news-curate, head `286a16f`):
`news-curate.py`, the test and doc diff. Blocking: `--add-dir <directories...>`
is variadic and precedes the prompt, so with no model override the CLI reads the
prompt as a directory and exits ("Input must be provided"). Run offline on
2.1.332, the pinned version: argument handling only; both `--add-dir=<dir>` and
an option following the pair got past it. The PR's script and tests were not
run. Second note, by reading: feedback cursor acks without any check that
preferences were folded.
https://github.com/Retinue-OS/retinue/pull/454#issuecomment-7177215624
retinue#450, #452, #453 not reviewed. Counter: 0. Next check: whether the
argument order is fixed in what merges.

2026-11-25 23:40Z run: reviewed retinue#453 (arrival turn's triage word, head
`ba378be`): `scripts/` diff and surrounding gateway and store code; test diffs
not read; nothing run; CI `test` passed. One note beyond the three Copilot
threads: `_triage_from_arrival` uses the unconditional `put`, so an older word
can replace a newer entry (deferred mails of a large batch, or a sorting during
a running turn), and the word of a turn with deferred mails never saw them.
Smaller: feedback section and docstring still say every unread chat is sorted
again.
https://github.com/Retinue-OS/retinue/pull/453#issuecomment-7177947821
retinue#450 and #452 not reviewed. Counter: 0. Next check: whether the
overwrite is fixed in what merges; retinue#454 argument order still open.

2026-11-26 00:13Z run: reviewed retinue#450 (chat avatar opens the contact,
head `6c7d376`): webapp and doc diffs and the server code behind them.
`holdsHandle`, extracted into Node 22, ran on made-up persons; PR tests and
gateway not run. One note: a WhatsApp JID key never matches a filed number
(`+` kept), and for a phones-only person neither autolink nor `create` stops a
second person (by reading); letter-stripping lets unrelated ids match.
Overlaps Copilot's first thread on the `+`.
https://github.com/Retinue-OS/retinue/pull/450#issuecomment-7178578348
Also read the retinue#453 fix `ba378be..6851490` (non-test diff): both points
of my note are addressed by reading; CI succeeded; no comment. retinue#452 not
reviewed. Counter: 0. Next check: whether the JID match is fixed in what
merges; retinue#454 argument order still open at `286a16f`.

## retinue#452 review, 2026-11-26 (bet 5)

Read at `1fa3051` (open; CI `test` succeeded). One note posted:
https://github.com/Retinue-OS/retinue/pull/452#issuecomment-7179133488

- Restore path (`_restoreTriage`) only reads, so the view can render with
  `run: null` or an `interrupted` run; unsorted chats then read "Came in after
  the sorting.", false in both cases. Measured: `_triageSections` and
  `_triageStatus` run in Node 22 with `listGroup` stubbed. By reading: the
  restart path to `interrupted`. Not run: PR tests, browser.
- Copilot's failed-restore thread was already fixed in `1fa3051`; not repeated.

Counter: 0. Next check: whether the wording changes in what merges.

2026-11-26 01:19Z run: read the retinue#452 fix `1fa3051..5b542f3`. The reply
on the PR (retog's account, signed as generated by Claude Code) calls the note
real and credits it; the commit message names the review. By reading,
"Came in after the sorting." now needs `run.state === 'done'`, and a chat a
finished run failed on still gets its own entry (`_unsorted`), so it does not
fall through to that line. A new view test covers `run: null`, `interrupted`
and `done`; CI `test` passed; I ran nothing. No comment posted. PR open,
unmerged. Counter: 0. Next check: retinue#450 JID match and retinue#454
argument order in what merges.

2026-11-26 01:52Z run: no review. Open PR heads (retinue#450 to #454, ara-android#29,
#30) unchanged since last read; #423 still skipped. Bet 5 counter stays 0. Next
check as above.

2026-11-26 02:23Z run: no review. Open PR heads (retinue#450 to #454,
ara-android#29, #30) unchanged since the 01:52Z run. Bet 5 counter stays 0.
Next check as above.

2026-11-26 02:54Z run: no review. Open PR heads (retinue#450 to #454,
ara-android#29, #30) unchanged since the 02:23Z run. Bet 5 counter stays 0.
Next check as above.

2026-11-26 03:27Z run: no review. Open PR heads (retinue#450 to #454,
ara-android#29, #30) unchanged since the 02:54Z run. Bet 5 counter stays 0.
Next check as above.

2026-11-26 03:58Z run: no review. Open PR heads (retinue#450 to #454,
ara-android#29, #30) unchanged since the 03:27Z run. Bet 5 counter stays 0.
Next check as above.

2026-11-26 04:30Z run: no review. Open PR heads (retinue#450 to #454,
ara-android#29, #30) unchanged since the 03:58Z run. Bet 5 counter stays 0.
Next check as above.
Repeated at 05:02Z, 05:34Z, 06:05Z, 06:37Z, 07:08Z and 07:39Z: same heads, no
review, counter still 0.
08:11Z run: no open PR listed as updated after 07:35Z (heads not re-read), no
review, counter still 0.
08:42Z run: open PR heads re-read, unchanged; no review, counter still 0.
09:14Z run: open PR heads re-read, unchanged; no review, counter still 0.
09:46Z run: open PR heads re-read, unchanged; no review, counter still 0.
10:17Z run: open PR heads re-read, unchanged; no review, counter still 0.
10:49Z run: open PR heads re-read, unchanged; no review, counter still 0.

2026-11-26 11:21Z run: retinue#452 and #453 merged at the heads last read
(`5b542f3`, `6851490`). Read on `main` at `a4682f9`: the "Came in after the
sorting." wording is gated on `run.state === 'done'`
(`webapp/components/chats.js`); `TriageStore.put_arrival` keeps a newer entry
under one lock (`scripts/chat_triage.py`) and the gateway calls it with the
`partial` flag for split batches. Both notes' fixes are present on `main`. Check
run `test` on that commit succeeded; I ran no tests. No comment posted. Counter:
0. Next check: retinue#450 JID match and retinue#454 argument order in what
merges.

2026-11-26 12:25Z run: reviewed retinue#455 (mail press releases a `verify`
queue, head `c59a627`; reading only). Posted: `compose-sheet.js` hint still says
the mail may wait for approval; two header comments carry the old rule.
Checked: both `_mail_send_pressed` callers sit behind the same-origin and edge
checks; reply recipients are re-asked at the press and on Check again. Copilot's
two points (lost approve response, repeat flag) not re-verified here. Counter:
0. Next check: whether the hint and Copilot's two points are in what merges.
https://github.com/Retinue-OS/retinue/pull/455#issuecomment-7192040365

2026-11-26 12:59Z run: open PR heads (retinue#450, #451, #454, #455, #423,
ara-android#29, #30) re-read, unchanged; no review, counter still 0.

2026-11-26 13:31Z run: open PR heads (retinue#450, #451, #454, #455, #423,
ara-android#29, #30) re-read, unchanged; no review, counter still 0.
14:03Z run: open PR heads re-read, unchanged; no review, counter still 0.
