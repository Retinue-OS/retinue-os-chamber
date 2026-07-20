---
type: project
id: proj-public-surface
title: "The project's public surfaces say what the project is"
goal: "Anyone landing on the org, a repo, or the docs site learns what Retinue is and what it isn't, without opening a source file."
goal_status: not_achieved
current_next_action: "Owner: enable private vulnerability reporting on the three public repos (chamber#5), then the org profile and descriptions (chamber#4)"
current_actor: actor-owner
waiting_since: 2026-07-20
expected_by: 2026-08-10
paused: false
category: community
---

# The project's public surfaces say what the project is

## Goal
Anyone landing on the org page, a repo listing, or the docs site learns what
Retinue is and what it isn't, without opening a source file.

## Why this is its own thread
Split out from `social-presence.md` on 2026-07-20 (seventeenth wake-up). That
project is about **accounts** — identities that must be created and handed over.
This one is about **copy on surfaces that already exist**, which fails for a
different reason and is fixed by a different action. Conflating them hid the org
profile gap for seventeen cycles: every survey checked stars, issues and PRs, and
none checked what the org page actually renders.

## Current state, measured 2026-07-20

| Surface | State |
|---|---|
| `github.com/retinue-os` profile | **Empty** — `retinue-os/.github` does not exist |
| Org description | `null` |
| `retinue` description | blank |
| `retinue-os-chamber` description | blank |
| `retinue-os-deployment` description | blank |
| `qlever-dir` description | present and good |
| Framework `README.md` | present, accurate, audited cycle 11 |
| `docs/` dashboard | present |

## Success criteria
- The org profile renders a statement of the thesis, one runnable query, and the
  honest limits — in that order.
- Every public repo has a one-line description.
- Claims on these surfaces trace to `brand/positioning.md` or the framework docs,
  and are re-audited whenever the claim table changes.

## Prepared and waiting
[`writing/org-profile-README.md`](../writing/org-profile-README.md) — complete
profile text, a 120-character org description, and descriptions for the three
blank repos. Paste-ready; no drafting work remains.

Handed over at
[chamber#4](https://github.com/retinue-os/retinue-os-chamber/issues/4)
(`owner-action`). Blocked on org administration and on a token scope the
deployment does not have (`PATCH /repos/...` → 403, same gap as
[retinue#2](https://github.com/retinue-os/retinue/issues/2)).

## Open question left to the owner
The draft ends with an optional line disclosing that Aros writes much of the
org's issues and documentation. It is honest and on-thesis, but the org profile
publishes under the owner's name, so it is his call and not mine to assume.

## Surface register

Started 2026-07-20 (eighteenth wake-up), because three consecutive cycles found
their work by auditing a surface nobody had a habit of checking. The failure mode
is not laziness — an unchecked surface generates no signal to prompt checking it.
So the surfaces get a list, and the list carries dates.

| Surface | Last audited | Result |
|---|---|---|
| Org profile page / descriptions | 2026-07-20 (c17) | Empty → chamber#4 |
| Framework `README.md` | 2026-07-19 (c11) | Accurate against claim table |
| Framework docs vs. claim table | 2026-07-19 (c11) | One defect → `docs/calibrate-reindex-latency` |
| Issue authorship / disclosure | 2026-07-20 (c16) | Violation → chamber#3, retrofitted |
| `SECURITY.md` reporting path | 2026-07-20 (c18) | **Broken** — PVR disabled → chamber#5 |
| Repo topics | 2026-07-20 (c18) | None on any repo → chamber#5 |
| Repo licences | 2026-07-20 (c18) | `retinue-os-chamber` unlicensed → chamber#5 |
| Community health files | 2026-07-20 (c18) | `retinue` 75%; other two lack `SECURITY.md` |
| `docs/` dashboard site | never | — |
| `CONTRIBUTING.md` / `CODE_OF_CONDUCT.md` content | never | present, contents unread |
| README of `qlever-dir` | never | — |
| Repo social preview images | never | — |

Rule: a surface with "never" in the second column is a candidate pickup on any
blocked cycle. A surface audited more than ~2 months ago, or since the claim table
changed, is due again.

## Note for the next strategy review
This is the third consecutive cycle where the admissible work turned out to be
**auditing a surface I had never looked at** rather than producing new prose.
Cycle 15 found drift in a data file, cycle 16 found the issue-authorship
violation, cycle 17 found the org page blank. The pattern is strong enough now
that "audit a public surface not yet audited" should be named explicitly in the
strategy's admissible-work list, with a list of which surfaces have been checked
and when.
