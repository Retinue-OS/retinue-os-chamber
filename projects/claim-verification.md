---
type: project
id: proj-claim-verification
title: "Verify the claims before publishing them"
goal: "Every load-bearing claim in brand/positioning.md has been run, not just read."
goal_status: in_progress
current_next_action: "Aros: continue working through the unverified claims list"
current_actor: actor-aros
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
| Egress audit observes but does not enforce | not yet run | Verifying this one *confirms a weakness*, which is the point. |
| Named graph derived from file path; move a file and provenance follows | not yet run | Testable against the live store. |
| Blue-green reindex catches up in ~15s | not yet run | The one claim with a number in it (guardrail 3). |

## Open finding — deliberately not detailed here
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
