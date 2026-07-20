---
type: project
id: proj-public-release
title: "Publish the framework with a clean history"
goal: "The framework is public under retinue-os with no personal data in the tree or in history."
goal_status: achieved
current_next_action: "Owner: decide the deliberate-disclosure question, and whether to purge this chamber repo's history of the c42 redaction (dashboard)"
current_actor: actor-owner
waiting_since: 2026-07-20
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
the `.env` that was briefly committed held only placeholders. It did find
personal data belonging to the owner and to third parties, in both file contents
and commit messages. The categories and locations are recorded privately with the
owner and deliberately not restated here; see the redaction note below.

GitHub retains unreferenced objects and serves them by SHA more or less
indefinitely, so rewriting and force-pushing the existing repo would not
reliably make those unreachable. Publishing from a *new* repository does.
Scrubbing commit message text also requires regex callbacks that are easy to get
subtly wrong; an orphan commit has exactly one message, written deliberately.

## Open decision for the owner
Some shipped examples and vocabulary entries carry inferences about the owner
personally. They are legitimate features and may be worth advertising as such,
but that is a **deliberate disclosure** for the owner to make, not a side effect
of shipping examples. The specifics are with him on the dashboard. Flagged, not
decided — and, until he decides, not described here.

## Redaction note — 2026-07-20 (c42)

The two sections above were rewritten this cycle. As originally written and
published, they stated in public exactly the personal facts this project exists
to keep out of the public tree: they named the categories of personal data found
in the private archive and, in the "open decision" section, spelled out the
inference that the shipped examples support about the owner's health.

This chamber repo is public. The scrub succeeded on the framework repo; the file
recording the scrub was then published verbatim in a different repo, and no
surface audit had ever covered this repo's own contents as a disclosure surface.
It was public from the initial commit (2026-07-19) until this edit.

**This edit fixes the readable surface only.** The original text remains in this
repo's git history, reachable by commit SHA — which is precisely the argument
this file makes above for publishing from a new repository rather than rewriting
one. Whether to purge it is repo administration and a decision about the owner's
own data: escalated to him, not actioned here.
