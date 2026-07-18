---
type: project
id: proj-public-release
title: "Publish the framework with a clean history"
goal: "The framework is public under retinue-os with no personal data in the tree or in history."
goal_status: not_achieved
current_next_action: "Push the staged orphan commit once the organization exists"
current_actor: actor-owner
waiting_since: 2026-07-18
expected_by: 2026-07-25
paused: false
category: infrastructure
links:
  - https://github.com/retog/retinue/issues/126
---

# Publish the framework with a clean history

## Goal
The framework is public under `retinue-os` with no personal data in the tree or
in history.

## Success criteria
- A tree scrub removing every real name, address, hostname, private repo URL and
  personal example from the working tree.
- A single orphan commit — **not** a `filter-repo` rewrite of the existing repo.
- `retog/retinue` stays private and intact as the historical archive.
- `qlever-dir` audited and released alongside.

## Why an orphan commit rather than a history rewrite
A full audit of 299 commits, 34 branches and 780 blobs found no live secrets —
the `.env` that was briefly committed held only placeholders. But it did find a
real export of the owner's project board on a stale branch, containing medical
and disability detail and four named third parties, plus two commit messages
with live-mailbox statistics naming a real correspondent.

GitHub retains unreferenced objects and serves them by SHA more or less
indefinitely, so rewriting and force-pushing the existing repo would not
reliably make those unreachable. Publishing from a *new* repository does.
Scrubbing commit message text also requires regex callbacks that are easy to get
subtly wrong; an orphan commit has exactly one message, written deliberately.

## Open decision for the owner
Several artifacts — a `wheelchair-push-count` sensor mapping, health vocabulary,
CGM and ketone examples — together disclose the owner's disability and metabolic
monitoring. These are legitimate features and may be worth advertising as
accessibility-aware sensor support. But that should be a **deliberate
disclosure**, not a side effect of shipping examples. Flagged, not decided.
