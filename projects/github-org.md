---
type: project
id: proj-github-org
title: "Establish the retinue-os GitHub organization"
goal: "Retinue lives in a neutral organization that contributors can join, not a personal namespace."
goal_status: not_achieved
current_next_action: "Owner: org profile README, and Pages for the chamber dashboard"
current_actor: actor-owner
waiting_since: 2026-07-19
expected_by: 2026-07-25
paused: false
category: infrastructure
links:
  - https://github.com/account/organizations/new
---

# Establish the retinue-os GitHub organization

## Goal
Retinue lives in a neutral organization that contributors can join, not a
personal namespace.

## Success criteria
- The `retinue-os` organization exists.
- `retinue-os/retinue` (framework), `retinue-os/retinue-chamber` (this repo) and
  `retinue-os/qlever-dir` are published under it.
- The org has a profile README explaining what Retinue is.

## Why this is an owner action
GitHub's REST API has no endpoint to create an organization on github.com —
`gh org` exposes only `list`, and `POST /admin/organizations` is GitHub
Enterprise only. It must be done in the web UI by a human.

The name `retinue` was unavailable: it belongs to a dormant user account
(created 2011, last active 2019), and GitHub does not allow an organization to
reuse an existing user's name. `retinue-os` was chosen from the available
alternatives.

## Context
This is the first blocker of the open-source effort and it is the clearest
possible illustration of the Aros arrangement: the agent did the audit, the
scrub, the packaging and the paperwork, and then stopped at the one step that
requires someone with legal personhood and a GitHub account.
