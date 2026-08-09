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
| Not model-agnostic; coupled to Claude Code | **re-affirmed 2026-08-09 (c687), against an owner challenge** | The owner commented on `.github#1` that calling Retinue "not model-agnostic" is misleading since it "can run on ollama and even [shims] with litellm." Checked before answering: `litellm/config.yaml` on `retinue-os/retinue@main` defines exactly one non-Claude route, `retinue-openrouter`, used as subscription-failover — not a general model-swap path. Code search for `ollama` across the repo: **0 hits**. `review.md:202-218` (§3.4) — binding per guardrail 3 — calls Claude Code coupling *"the project's deepest dependency"* and states the LiteLLM failover path itself "adds terms-of-service gray area," i.e. treats it as a risk, not evidence of portability. Replied on the issue with the citations and asked the owner for a concrete counter-example (a working Ollama route or deployment) rather than change the claim on an unverified premise — that would trade one uncalibrated claim for another. No edit made to `writing/org-profile-README.md` or the live org README pending his answer. |

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
