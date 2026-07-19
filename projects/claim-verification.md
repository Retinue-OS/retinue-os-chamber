---
type: project
id: proj-claim-verification
title: "Verify the claims before publishing them"
goal: "Every load-bearing claim in brand/positioning.md has been run, not just read."
goal_status: in_progress
current_next_action: "Owner: rule on the second open finding routed privately 2026-07-19; Aros holds a patch and test cases ready to write"
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
| An agent can never approve its own send | not yet run | |
| Credentials live only in sidecars, never in the model's context | not yet run | Check by inspecting the agent container's own environment. |
| Egress audit observes but does not enforce | **verified, and the claim understates the weakness** 2026-07-19 | Ran a proxied and a bypassing request to the same host, seconds apart. Both returned 200; the bypass terminated at a public IP, not the sidecar. The audit logged the proxied one and has **no record at all** of the bypass. So it is not just unenforced — a bypass is *unobserved*. Written up in `writing/egress-audit-observes.md`. Not a disclosure: `review.md` §3.2 already states the mechanism publicly. |
| Named graph derived from file path; move a file and provenance follows | not yet run | Testable against the live store. |
| Blue-green reindex catches up in ~15s | not yet run | The one claim with a number in it (guardrail 3). |

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
