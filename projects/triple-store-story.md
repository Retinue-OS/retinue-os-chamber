---
type: project
id: proj-triple-store-story
title: "Make the triple-store layer the lead story"
goal: "The named-graph/converter architecture is explained well enough that a semantic-web engineer immediately sees why it is unusual."
goal_status: not_achieved
current_next_action: "Draft a worked walkthrough: one Markdown file to one SPARQL answer"
current_actor: actor-aros
waiting_since: 2026-07-18
expected_by: 2026-08-15
paused: false
category: content
links:
  - docs/triple-stores.md
---

# Make the triple-store layer the lead story

## Goal
The named-graph/converter architecture is explained well enough that a
semantic-web engineer immediately sees why it is unusual.

## Success criteria
- A walkthrough that goes from one hand-edited Markdown file to one SPARQL
  answer, with every intermediate artifact shown.
- A short piece on why provenance-by-path removes the usual quad bookkeeping.
- Both linked from the org profile and the framework README.

## Why this matters more than the security story
The July 2026 architecture review marked this layer "unproven ROI" and
recommended setting a deadline for the queries that justify it. That was fair on
the evidence available — `docs/triple-stores.md` did not exist yet. With it
written, this looks like the most genuinely novel part of the system.

The security architecture is *better* than the field's, but it is legible: other
projects could adopt sidecar credential isolation tomorrow. The chamber/named-graph
design is *different in kind* — the artifact you were going to write anyway
becomes the graph, provenance falls out of the filesystem layout, and there is
no write path to the store at all. Nobody else in the personal-agent space is
doing this, and the people best equipped to appreciate it are not currently
being addressed by anyone.

## Honest framing required
Per `brand/positioning.md`: today this powers one dashboard card and archivist
ingestion, and it is the heaviest infrastructure per delivered feature in the
stack. The walkthrough must say so. The argument is that the bet is a good one,
not that it has already paid off.
