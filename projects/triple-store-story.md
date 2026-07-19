---
type: project
id: proj-triple-store-story
title: "Make the triple-store layer the lead story"
goal: "The named-graph/converter architecture is explained well enough that a semantic-web engineer immediately sees why it is unusual."
goal_status: not_achieved
current_next_action: "Blocked: decide the canonical namespace on retinue#1 before the walkthrough can show a real query"
current_actor: actor-owner
waiting_since: 2026-07-19
expected_by: 2026-08-15
paused: false
category: content
links:
  - docs/triple-stores.md
  - https://github.com/Retinue-OS/retinue/issues/1
  - https://github.com/Retinue-OS/qlever-dir/issues/3
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

## Blocked, as of 2026-07-19

The walkthrough cannot be written yet, because the pipeline it would walk
through does not currently produce an answer. Found by querying the live store
while preparing it:

1. **retinue-os/retinue#1** — `web-gateway.py` queries the `kb#` namespace;
   `md2ttl.py` emits `project#`. The one non-OPTIONAL pattern in the projects
   query (`?p rdf:type k:Project`) matches nothing, so the card returns no rows
   in any deployment. Two further mismatches behind it: `k:status` vs
   `p:goalStatus`, and `urn:retinue:actor:reto` vs `urn:retinue:actor-aros`.
2. **retinue-os/qlever-dir#3** — the inotify watcher reacts only to
   `.nt`/`.ttl`/`.n3` while the builder also indexes converter extensions. A
   chamber holding only Markdown — like this one — is never indexed at all.
   This chamber's own store serves nothing but the `urn:qlever-dir:empty`
   placeholder.

Both are filed with reproductions. Neither is mine to fix unilaterally: #1
needs a call on which namespace is canonical, #3 needs a decision on watch
semantics.

This is the guardrail-3 case working as intended. The walkthrough was one
session away from claiming a worked example that returns an empty result set,
and the reader most likely to run it is exactly the reader this project is
trying to earn. Publishing it would have cost more credibility than the piece
could have bought.

## Honest framing required
Per `brand/positioning.md`: today this powers one dashboard card and archivist
ingestion, and it is the heaviest infrastructure per delivered feature in the
stack. The walkthrough must say so. The argument is that the bet is a good one,
not that it has already paid off.
