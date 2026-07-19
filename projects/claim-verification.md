---
type: project
id: proj-claim-verification
title: "Verify the claims before publishing them"
goal: "Every load-bearing claim in brand/positioning.md has been run, not just read."
goal_status: in_progress
current_next_action: "Owner: rule on the two open findings routed privately 2026-07-19; Aros holds a patch and test cases ready to write. Meanwhile the affected claim is withdrawn from positioning.md, so nothing false is published while it waits. Every other claim in the table has now been run."
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
| Egress audit observes but does not enforce | **verified, and the claim understates the weakness** 2026-07-19 | Ran a proxied and a bypassing request to the same host, seconds apart. Both returned 200; the bypass terminated at a public IP, not the sidecar. The audit logged the proxied one and has **no record at all** of the bypass. So it is not just unenforced — a bypass is *unobserved*. Written up in `writing/egress-audit-observes.md`. Not a disclosure: `review.md` §3.2 already states the mechanism publicly. |
| Named graph derived from file path; move a file and provenance follows | **verified** 2026-07-19 | Ran it, did not trust it. `git mv` of `sensor-a/readings.nt` into `sensor-c/`, no edit to the file's two triples. `urn:demo:obs:a:1` moved graph from `file:retinue/docs/examples/provenance/sensor-a/readings.nt` to `…/sensor-c/readings.nt` with no migration step. Moved back; store restored to the identical pre-test state. Demonstration added to `writing/provenance-by-path.md`, replacing an assertion that had rested on the docs. |
| Blue-green reindex catches up in ~15s | **verified, restate as 15–20s** 2026-07-19 | Polled at 5s intervals across three separate rebuilds: old value at t+15s, new value at t+20s, every time. So "~15s" is not wrong but rounds the wrong way; I state 15–20s for a small file. **The load-bearing caveat is what starts the clock:** only a native RDF file event does. A new Markdown file sat unindexed for 32 minutes (`projects/claim-verification.md`, committed 22:07, absent at 22:39) and a probe `.md` stayed at zero triples for a full 60s poll — then appeared within 20s the moment an unrelated `.nt` write triggered a rebuild. That is qlever-dir#3 observed from the other side, and it means the latency figure only holds for RDF. |

## Open findings — deliberately not detailed here
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
