# Public surface register — archive part 9 (cycles 288–294)

Rotated out of [`projects/public-surface.md`](../projects/public-surface.md) on
2026-07-30 (cycle 300), when the live file reached its 200 KB threshold. Whole
sections, verbatim, oldest first. The register table in the live file points
here for each of them.

## §c288 — 2026-07-30 13:5x–14:1xZ — the item a review admitted it could not test, tested after the merge

The surface is a sentence of my own: *"Not checked, and it is the single point of
failure"* — the closing section of the c276 review of `feat/chamber-instructions`
(commitcomment-194312465). Every audit since has looked at what my reviews **said**
(c274, c276) or at **where they landed** (c282, c287). None went back to the one thing
a review declared untestable, and that is the class of sentence nobody re-reads,
because it comes with its own excuse attached.

**The merge is what re-opened it.** PR #48 merged at **13:30:57Z** as `6257ae4f2` —
and it is a *merge* commit, parents `99667116d` + `a266eb6c2`, the second being the
exact commit c274/c276 reviewed. Blob-compared rather than assumed: `CLAUDE.md`
`c242c836…` and `scripts/entrypoint.sh` `2780e892…` are identical at both refs. So
the mechanism reached `main` with none of the review addressed and its single point of
failure still unverified, and the thing I called untestable-without-a-restart was now
untested *in production* rather than on a branch.

**Four fixtures, no restart, Claude Code 2.1.220, `claude -p --model haiku`:**

| | cwd | target | answer |
|---|---|---|---|
| A | 10-line `CLAUDE.md`, `@.retinue/chamber-instructions.md` | present, canary | canary returned |
| B control | same, `@retinue/…` not hidden | present, other canary | canary returned |
| C **negative control** | same as A | **absent** | `NONE`, exit 0, clean stderr |
| D | the merged `CLAUDE.md` **verbatim** (783 lines, import at `:782`) | generated-shape file, canary | canary returned |

C is the case that makes the others evidence rather than a coincidence: an unbacked
canary word could in principle be guessed once, but the identical prompt answers
`NONE` when the file is missing, so the answer tracks the file. D removes the "long
file, import at the very end" worry, which is the condition the deployment actually
runs.

**The docs back the diff's own claims, which is better than my run backing them.**
Relative imports resolve against the importing file, four hops deep; an import is
*external* — the case that raises the approval dialog — only when it resolves outside
the working directory. `CLAUDE.md:780` ("inside the session working directory, so the
import loads with no approval prompt") is therefore right for the documented reason,
not by luck. Block-level HTML comments are stripped before injection, so the note above
the import costs no context. Also scanned the merged file for imports nobody intended:
**exactly one** bare `@` token outside code spans and fences, at `:782`, the intended
one — parsing skips backticks and fenced blocks, which is why the `you@example.com` in
the PR recipe is inert.

**What survives is C, and it changes the weight of a defect I had already filed.** A
missing or mistyped target is *silent*: no stderr, exit 0, the session proceeds without
that chamber's routing section and nothing anywhere says the import failed. That is the
argument for `generate_chamber_instructions` always writing the file — a design choice
of his that this verifies was the right one — and it makes the boot line the **only**
observable signal. Which is why the `grep -c … || echo 0` line matters more than it
looked: in the zero-chamber case `grep -c` prints `0` **and** exits 1, so the fallback
appends a second `0`, and command substitution keeps the internal newline, so the line
breaks in two (`(0` / `0 chamber instruction file(s)).`). c276 described it as
`(0 0 …)`; that was imprecise and is corrected in public. This deployment is the zero
case at the next rebuild: `chambers.json` mounts one chamber, which has `.retinue/` and
no `INSTRUCTIONS.md`.

**Published**, not filed: [commitcomment-194360496](https://github.com/Retinue-OS/retinue/commit/a266eb6c21181510ba9de395898e740498c3124f#commitcomment-194360496)
(14:04:14Z), on the reviewed commit rather than the merge commit, so the review and its
resolution sit on one page — and that page stays reachable from `main`'s history
precisely because #48 was merged rather than squashed. It requests nothing, withdraws
nothing, and states plainly that the `grep` item is the same one-line item and only its
rationale changed. The c184 filing slot (spent until 2026-07-31T06:08:5xZ) is untouched;
a comment is not an issue.

**Not done, deliberately.** This chamber does **not** get a `.retinue/INSTRUCTIONS.md`
today, although it is now the only real (non-example) public chamber and would document
the new convention by existing. Two reasons, both mine: the framework carrying the
import is not deployed yet, so the file would do nothing; and by my own c276 finding,
adding a file to `.retinue/` is drift, so `sync-plugins.py` would uninstall and
reinstall this chamber's plugin within `PLUGIN_SYNC_INTERVAL` — a window in which a
starting session finds the `aros` agent absent. Worth doing after the next rebuild,
not before.

**The general form.** *A finding marked "not checked" is a claim with its excuse
attached, and the excuse is what keeps it from being re-read.* The stated reason
("needs a restart") was true of one method and false of the problem: a canary in a
scratch directory tests the same mechanism in ninety seconds. The register now carries
the class — **the unchecked items inside my own audits** — and the practical rule is
that a review's open item expires at the merge, because after the merge nobody else is
going to test it either.

## §c289 — 2026-07-30 14:3x–14:5xZ — the PR reviewed while it was still open

**The surface.** Every audit from c274 on read either a pushed branch (c274/c275/c276),
a merged commit (c288), or where a review *landed* (c282/c287). None was a PR read in
the window it is actually decidable in — between `opened` and `merged`. PR #49 opened at
14:08:56Z, twenty-two minutes after the previous wake-up finished; three PRs merged today
inside ninety minutes, so that window is measured in tens of minutes here.

**What the PR does.** LiteLLM becomes the source of the dashboard's conversation-model
picker: the gateway reads `GET /model/info` from `RETINUE_LITELLM_URL` (default
`ANTHROPIC_BASE_URL`) and offers every route whose `model_info` sets
`retinue_picker: true`, cached `RETINUE_MODELS_CACHE_SECONDS` (default 60), with the
static JSON-LD/env chain as fallback.

**Method, and its limit.** This deployment routes **no** LiteLLM — `ANTHROPIC_BASE_URL`
unset, `LITELLM_MASTER_KEY` empty, `http://litellm:4000` unreachable (curl rc=6) — so
`_LITELLM_URL` is `""` here and the new path is dead code in this stack. Testing it at
all meant lifting lines 236–362 of the head blob (`50744eb`) into a standalone module
unchanged, adding only `_DEFAULT_MODEL_ENTRY` and stubbing the two module-level
constants, and pointing `RETINUE_LITELLM_URL` at a `ThreadingHTTPServer` with a latency
knob and a 503 knob. **The stub asserts the response shape the PR assumes; it does not
verify it.** Whether LiteLLM preserves custom `model_info` keys, and whether the admin UI
can set them, is untested and is stated as untested in the comment — c288's lesson
applied on the way in rather than four cycles later.

**Confirmed as described:** wildcard `claude-*` dropped even when flagged, unflagged
routes invisible, `Default` synthesized first; 20 lookups of an offered id → **0**
fetches; 5 list reads against a 503 → **1** fetch, the failure cached like a success.

**The finding.** `_model_offered` answers a miss with `_conversation_models(force=True)`,
and `force` skips the TTL branch outright — including the failure backoff it just
verified. So the cache bounds the hit path and nothing bounds the miss path:

| | fetches |
|---|---|
| 20 lookups of an unknown id, warm cache | **20** |
| 5 lookups of an unknown id while upstream 503s | **5** |

**Why it is not academic.** `_conv_summary` (`:1040`) calls `_conv_model` →
`_valid_model_id` → `_model_offered` for every thread, and `_conv_list` (`:1090`) calls
`_conv_summary` for every thread. So a route renamed or dropped in LiteLLM turns one
`GET /conversations` into one forced upstream fetch per affected thread — measured, 8
threads → **8 fetches, 4.02 s** at a 0.5 s stub delay. `_litellm_models_lock` is held
across `urlopen(..., timeout=5)`, so a thread reading an already-fresh cache waited
**1.80 s** behind one forced 2 s fetch. At the real timeout, 8 stale threads is ~40 s on
one list request with everything else queued behind it. Behind basic auth throughout —
a self-inflicted stall, not an attack surface, and the comment says so in those words.

**Venue, and a new datum.** `POST /repos/…/issues/49/comments` → **403 Resource not
accessible by personal access token.** A PR *is* an issue for that API and issue comments
work elsewhere in the org, so the token's issue-write scope does not extend to pull
requests — narrower than c287's model, which had established only that the *read* side
(cross-references) works. Fell back to the c287 recipe's first half: commit comment on
the head blob, [commitcomment-194366283](https://github.com/Retinue-OS/retinue/commit/50744eb1689c449c1d658dee17882d2ec3a015c1#commitcomment-194366283),
14:45:53Z.

**The cross-reference was deliberately skipped**, breaking the c287 recipe's second half
with a reason: the only issue I hold that would carry it is chamber#6, where I commented
83 minutes earlier and withdrew the scope request — a second comment there today is the
nagging c282 correctly refused and c287 caught itself doing. `retinue#11` is topically
adjacent (LiteLLM as an unconditional dependency) but a pointer-only comment on an issue
about something else is noise, and making it carry weight would mean adjudicating #11's
substance, which I have not measured. The commit comment produces a Commits-tab badge
(c287's verified mechanism) on a PR its author opened 37 minutes before.

**The general form.** *A review is worth a fraction of its content times the probability
it arrives before the decision.* Four wake-ups have now reviewed code after it merged.
This one cost the same effort and landed inside the window, because the survey read the
`PullRequestEvent` stream rather than only `main`'s SHA.

## §c290 — 2026-07-30 15:2x–15:3xZ — review.md's evidence links audited for the first time in 269 cycles

**The scope was in the row all along, as a parenthesis.** This file's register row
for `review.md` reads *"review.md vs. reality (tests/CI) | 2026-07-20 (c20) | Stale …"*.
The `(tests/CI)` is a **scope**, and 269 cycles read the row as "review.md: audited".
Everything outside the tests/CI cluster — including the five links the document uses as
its evidence — had never been looked at. Same shape as c176/c178: a claim whose scope
was assumed, not measured. The file earns the audit: it is linked from the served
landing page, `CONTRIBUTING.md` sends every new contributor to it, `GUARDRAILS.md` §3
binds my own public copy to it, and bet 4 stakes the strategy on its candour — and
candour a reader cannot verify is not candour.

**Method.** Blobs fetched via the contents API (c179: the local checkout is behind
`main`) at `6257ae4f2` (PR #48, merged 13:30:57Z today) and at `f7d9cc397` (*Initial
public release*, the only commit `review.md` has ever had). `review.md` has exactly five
Markdown links; three carry line ranges.

**Finding: all three line-range citations resolve to the wrong lines.**

| § | Citation | Correct now |
|---|---|---|
| 2.1 | `scripts/entrypoint.sh#L397-L402` (EMAIL_PASS strip) → OAuth cred-backup branch | **456–461** |
| 3.2 | `docker-compose.yml#L114-L119` (HTTP_PROXY/HTTPS_PROXY) → CONVERSATIONS_DIR/UPDATER_URL | **126–128** |
| 3.4 | `scripts/entrypoint.sh#L313-L372` (OAuth-rotation watcher) → end of a `disown` loop + Mode selection | **372–431** |

Two are ordinary drift — `entrypoint.sh` grew 422 → 481 lines and both ranges were
**correct at release** (`f7d9cc397`). **The `docker-compose.yml` one never rotted: it
was never right.** That file has one commit in history; the blob is byte-identical at
both SHAs (520 lines); `HTTP_PROXY` has been on line 126 since day one; 114–119 has
never held either variable. It is the §3.2 evidence — the section stating the egress
audit is *observability, not enforcement*, the claim this project is most careful not to
overstate and the subject of a piece I published under my own name. The claim is true;
its proof link has never worked. §3.5's three gateway line-counts are also stale
(1,362/1,177/993) but per the 07-25 rule I asked they be **deleted, not refreshed** —
its argument needs no count.

**The fix that does not expire, proposed:** a review is dated evidence about a specific
commit, so pin its citations to that commit as permalinks
(`…/blob/f7d9cc397/…#L397-L402`) rather than to a moving `main`. Repointing the ranges
buys about as long as the counts did.

**Published:** [retinue#3 comment 5132894733](https://github.com/Retinue-OS/retinue/issues/3#issuecomment-5132894733)
(15:31:16Z), added to the existing thread with an explicit offer to split it out; issue
comments work (unlike the PR-comment 403 c289 found). No filing slot spent — a comment,
not a new issue. Nothing escalated: not a security finding, needs only this file's
maintainer. Recovered and logged by c291 after c290 was interrupted between publishing
and committing.

## §c292 — 2026-07-30 17:4x–17:5xZ — the PR that verifies its own delivery, and does not

**Surface:** `scripts/daily-status.py` (new, 449 lines) plus a base `.schedule.json`
job, on `feat/daily-status-briefing` — PR
[#50](https://github.com/Retinue-OS/retinue/pull/50), opened 2026-07-30T17:33:12Z.
Reviewed ~14 minutes after it opened, inside the window where the merge decision is
still open (c282's rule, c289's precedent).

**What was new to review.** c289 audited a PR's *cache behaviour* — a property of the
code. This PR makes a claim **about itself**: "Send + verify … then confirms the
message reached the owner's personal account." A feature that reports on its own
success is the one place where a wrong report is invisible by construction, because the
thing that would tell you it failed is the thing that failed. That is what got audited.

**The finding.** `verify_delivery()` asks the personal gateway for `/recent-chats` and
tests whether the system account appears anywhere in the dump. Nothing in the test is
about *today*. `_record_recent_sender()` (signal-gateway.py:748) keeps one entry per
person indefinitely, capped only by `SIGNAL_RECENT_CHATS_MAX`, so the first delivered
briefing records the account and every later check finds it.

**Why it is worse than a stale read: it composes with the send path the PR ships on.**
`send_signal()` returns `out.returncode == 0`, and `signal-push.py` returns **0** from
its `pending_approval` branch (line 89, `return 0` at 97) — a *queued* send is
indistinguishable from a delivered one at that boundary. Under the
`SIGNAL_SEND_POLICY=verify` default the PR's own deployment note says is in force:

| | |
|---|---|
| Day 1 | queues → `sent=True`, `mark_sent_today()` fires, verify **False** (never delivered) → fallback thread. Correct. |
| Owner approves at `/sends` | it delivers; the personal gateway records the system account |
| Day 2 onward | queues again → `sent=True`, verify finds day 1's entry → **True**. No fallback, exit 0, "verified" — for a briefing sitting unapproved in the queue. |

So the failure mode the verification exists to catch becomes invisible the first time it
succeeds.

**Measured, on stubs emitting exactly the shape `_list_recent_chats()` returns:**

```
verify_delivery() with a year-old last_seen and nothing delivered today -> True
send_signal() when the send only QUEUED for approval                    -> True
roster contains only +1555000417, no system account anywhere            -> True
```

The third is a second, smaller point: the test concatenates every digit in the
pretty-printed JSON into one string, so digits from adjacent fields join across
boundaries. Contrived against a real epoch timestamp; not worth filing alone; free to
delete once the JSON is parsed, which the real fix requires anyway.

**Fix proposed, and tested before posting rather than after (rule 28).** `last_seen` is
already in the payload and `_record_recent_sender()` refreshes it on every inbound
event. Take the send time at the caller, parse the roster, compare:

```
a) account present, last_seen a year old   -> False (want False)
b) account present, last_seen after send   -> True  (want True)
c) account absent, digits straddle fields  -> False (want False)
```

**Stated untested, on the way in (c288's lesson, applied without being asked twice):**
whether the personal gateway records the system account at all in this deployment (if
not, verification is `False` forever — a fallback thread every morning instead of a
false green); and the **timing** — `verify_delivery()` fires immediately after
`send_signal()` with no wait for the send → receive → record round trip, so a correct
freshness check without a bounded poll trades false greens for false reds.

**Published:** [commitcomment-194391715](https://github.com/Retinue-OS/retinue/commit/11903e1688080a3b1403d9d3e5e80e0a6d4edc09#commitcomment-194391715)
(17:47:48Z) on the PR head — the commit-comment path, since `POST /issues/50/comments`
is 403 for this token (c289's scope datum). No filing slot spent: a PR under review
wants a comment, not a ticket. Nothing escalated — not a security finding, and it needs
only this repo's maintainer, who is its author.

## §c292b — 2026-07-30 17:5x–18:0xZ — the account changed under me and I found out by accident

**How it surfaced.** I published the §c292 review, then ran a routine verification
fetch on my own comment — the "next you audits the last you" habit, applied to the
current you. The response carried `"author": "aros-agent"`. I had expected `retog`.

**What had happened.** The owner created
[`@aros-agent`](https://github.com/aros-agent) at **2026-07-30T14:51:24Z**, six
minutes after c289 finished, with the bio *"AI agent account. Issues, comments, and
code by Aros, an AI agent of the Retinue-OS project, operated under human oversight
by @retog. Not a human."* He commented from it on chamber#3 at 16:00:17Z saying the
account exists, the PAT was granted chamber#6's option 1, and "Closing" — and the
issue stayed open.

**Two of my own wake-ups walked past it.** c290 published at 15:31Z as `retog`.
c291 hit `git push` 403 *"denied to aros-agent"* at ~15:5xZ — **the new account's
name was in the error text** — read it as a permission *regression* on the owner's
token, and escalated it to his phone in those words. The string that would have
identified the event was in the failure message and neither cycle asked whose name
that was.

**Why it went unseen for three cycles.** The survey checks stars, issues, PRs,
mentions and drafts. It has never checked *who I am*, because for 272 cycles the
answer could not change: chamber#3 was the oldest open item on the desk and the
disclosure-sentence grep (c176 → c179 → c219) existed precisely because
authorship metadata could not tell the owner and me apart. An identity that cannot
change is not a surface anyone audits — which is the register's own thesis, pointed
at me this time rather than at a doc.

**What I did about it, in order.**

1. **Corrected the disclosure line on the comment I had published six minutes
   earlier.** It read *"from the owner's GitHub account — see chamber#3"*, which
   had stopped being true three hours before I published it. Edited in place with
   the correction **shown** rather than made silently. New standard line, one
   string from here on: `**Written by Aros, the project's AI agent, from my own
   account @aros-agent.**` — still prefixed `Written by Aros`, so the c219
   historical-alternation pattern keeps matching the archive.
2. **Answered chamber#3** from the new account with the measured evidence, and
   asked for it to be closed — I cannot close it myself (403).
3. **Corrected the escalation** on the owner's dashboard thread
   `9b4d2e2055374245a34575827e6a40b9`, where c291's "regression" claim was
   sitting. Same venue as the wrong claim; not a second channel, not a re-ask.

**The permission surface, measured rather than assumed.**

| Operation | Result |
|---|---|
| Comment on an issue (both repos) | **works** |
| Comment on a pull request | **works** — the 403 c289 recorded this morning is gone, so `pull_requests=write` landed |
| `git push` / contents write | **403**, `X-Accepted-Github-Permissions: contents=write` |
| Close / edit an issue | **403**, in both repos, while commenting in the same repos succeeds |
| Org membership, collaborator role | **403** |
| Effective repo access (`GET /repos/…`) | `{pull: true, push: false}` |

Everything needing only **read** on a public repo works; everything needing
**write on the repository** fails. Commenting on a public repo needs no write
access to the repo at all, which is why it is the one thing that still works and
why it made the token look healthier than it is. The likeliest cause is that
`@aros-agent` has Read rather than Write on the three repos — a fine-grained PAT
cannot exceed the account's own access — but I have flagged it to the owner as a
hypothesis, not a finding, because the endpoints that would confirm it are 403 too.

**One error of my own, recorded because it left a mark on a public surface.** To
learn which permission the PR-comment endpoint needs I called it with `-f
body=probe` expecting another 403, and got **201 Created** — a comment reading
`probe` on the owner's PR #50, three minutes after he opened it. Deleted within
the minute; #50 now has zero comments. The lesson is not subtle: a write endpoint
is not a probe, and "I expect this to fail" is not a safety property. Read-shaped
diagnostics (the `X-Accepted-Github-Permissions` header on a genuine 403) were
available for every question I had.


## §c294 — 2026-07-30 18:2x–18:4xZ — the rung opened and nobody re-probed it

**Delivery check first, on the served site, all five cards.** Self-test pass (6 stamp
cases + the divergence fixture, 6 asset cases). `agenda`, `briefing`, `messages`,
`projects`, `todo` all at the one stamp **2026-07-30T02:37:42Z**, age **15 h 50 m**
against the 26 h bound — inside it, and the five agree with each other. Disk is at
**2026-07-30T18:19:00Z** (c293's regeneration, nine minutes before this wake-up), so
the **attribution is the second branch and it is already known**: the refresh ran and
the delivery path failed. Not a Pages failure — `git push` returns 403 *"Permission to
retinue-os/retinue-os-chamber.git denied to aros-agent"*, re-confirmed this cycle, and
`/pages` was deliberately not consulted because the cause is upstream of it. 16 assets
byte-identical. Five commits sit unpushed. **Served content crosses the 26 h bound at
2026-07-31T04:37:42Z** unless contents-write is restored; the escalation is already on
the owner's phone (thread `9b4d2e20…`, corrected at c292b) and is **not** repeated here.

**Survey:** nothing moved in the nine minutes since c293. 0 stars / 0 forks / 0
watchers on all four public repos; 49 issues; PRs #44/#45/#49/#50 open; last human
action **2026-07-30T17:33:12Z** (#50 opened), re-slow bound 2026-07-31T17:33:12Z, tick
stays 1800 s. `drafts/` 3 held, nothing past a cool-off. c184 filing slot spent until
2026-07-31T06:08:5xZ.

**Pickup: re-probe the closed door c282 built a rule around.**

c282 (09:5xZ) measured four PR write endpoints, got 403 on every one, and concluded
**there is no rung** — nothing this token can write appears on a pull request. It was
right at the time and it wrote a good rule from it: *when a review lands anywhere other
than the PR conversation, say so in the review and deliver the ask on a channel that
reaches him.* c287 found one hinge (a cross-reference from an issue). c289 and c292 then
inherited the 403 as a **standing fact** and each posted its review to a commit comment
without re-running it — c292 wrote *"issue comments on a PR are still 403 for this
token (c289's scope datum)"* into a draft and into the log at 17:47Z, five minutes
before c292b discovered by accident that the same endpoint returns 201.

Measured this cycle, before posting anything:

| | |
|---|---|
| Open PRs | **4** — #44, #45, #49, #50 |
| Conversation comments on them | **0, 0, 0, 0** |
| Reviews of them written and published | **4** — all on commit comments |
| `POST /repos/:o/:r/issues/:n/comments` | **201**, four for four |

So the class was four, not the two c282 measured, and the reason each one landed on the
wrong surface was a permission that stopped being missing at 14:51:24Z.

**Delivered, all four, in the venue the decision is made in:**

- [#50](https://github.com/Retinue-OS/retinue/pull/50#issuecomment-5134784937) — the
  `verify_delivery()` finding in full. Re-verified against head `11903e16` first: the
  function still has no time component, line 320 still concatenates every digit in the
  payload, and `signal-push.py` still `return 0`s on a queued send (line 97).
- [#49](https://github.com/Retinue-OS/retinue/pull/49#issuecomment-5134788171) — the
  model-cache miss path in full. Head `50744eb` unchanged. That draft had **named this
  venue as the one it wanted** and settled for the fallback.
- [#45](https://github.com/Retinue-OS/retinue/pull/45#issuecomment-5134799972) and
  [#44](https://github.com/Retinue-OS/retinue/pull/44#issuecomment-5134800083) —
  pointers rather than full text, because those two were delivered by notification
  fourteen hours ago and what was missing is the marker on the merge page, not the
  content. Each carries the one line that bears on merging (the `sw.js` cache key;
  `secretary.md:95`'s "active chamber" against the new plural, and its precedence gap)
  and links the original. #44's review ends with a paragraph explaining the 403 and
  requesting no new scope — the new comment supersedes it explicitly rather than
  leaving a stale claim on a public page.

Each comment states, in its first paragraph, that it duplicates a commit comment and
why it is arriving late. Nothing is retracted; the commit comments stay.

**What this changes in the rules.** c282's rule survives with its scope narrowed: it
applies **when** the PR route is closed, and the route is open. What replaces the
closure is a habit — *a permission measured on one account is not a fact about the
next one*. c292b learned that about authorship this afternoon; this is the same lesson
one endpoint over, and it cost four reviews their surface rather than one comment its
byline.

**The general form, and it is this file's oldest one.** c163: *filed* counted as
*corrected*. c201: *pushed* counted as *escalated*. c206: a `drafts/` write-up counted
as *not lost*. c270: a correction in a log counted as a correction in the prose. c282:
a comment on the right commit counted as a review on the PR. This cycle adds the turn
after c282 — **a route measured as closed counted as closed forever.** The check is one
POST that was going to be made anyway, and the cost of not making it was carried by the
four PRs the owner is deciding on.

**Not done, on purpose.** *Nothing filed* — no slot until 2026-07-31T06:08:5xZ, and
none of this is a ticket. *Nothing escalated* — no account, money, terms-of-service or
legal question arose, and the push block is already on his phone; adding *"and the
served dashboard goes stale at 04:37Z"* to it would be a second message on one ask,
which is the nagging c282 refused. *No instrument written* — c268 rule 2; the surface
here is a GitHub page I do not control and the finding is that a probe was not re-run.
*No strategy revision* — an input to the 2026-08-02 review, alongside the observation
that both of c292b's discoveries (the account, the endpoint) were found by accident
rather than by a check.

