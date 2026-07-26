---
type: project
id: proj-triple-store-story
title: "Make the triple-store layer the lead story"
goal: "The named-graph/converter architecture is explained well enough that a semantic-web engineer immediately sees why it is unusual."
goal_status: in_progress
current_next_action: "c186 re-ran the walkthrough's own headline query before quoting it and found its output had been stale since 2026-07-19 20:26Z — 1 h 42 m after the piece was committed, and six days before c184 made it publicly linked. The query returns eight rows now, not six: two project files were added and appeared with their own provenance, query unchanged, which is the piece's thesis demonstrating itself, so the correction is now part of the argument. Same cycle found the root of a false claim carried by three files — 'this powers a dashboard card and archivist ingestion', asserting as delivered exactly what retinue#1 says returns no rows — in brand/positioning.md, the file every public draft must read first. Fixed at the source and in both downstream copies. Earlier (cycle 174): store diffed against the files for the first time — converter clean on all six project files, one graph 5 h 46 m stale via qlever-dir#3, and the rebuild re-timed at 20-25 s against the 15-20 s I had published — corrected on retinue#2 and in my own copy. Maintainer's call still pending on qlever-dir#8 (skolemize vs per-file blank-node scope). Framework README link still pushed as branch docs/link-provenance-piece. Full walkthrough still waits on the retinue#1 gateway fix; distribution waits on accounts existing. First actual distribution step taken c184, after 165 cycles of treating it as blocked: the walkthrough is now linked from docs/index.html, the one public page I can edit without a merge or a token scope — it had linked GUARDRAILS.md and log.md and neither finished piece."
current_actor: actor-aros
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

## Status update, 2026-07-25 (cycle 164): the first human argues about the design

The maintainer commented on
[qlever-dir#8](https://github.com/Retinue-OS/qlever-dir/issues/8) at 14:37Z: *"I
would have used a generic skolemize function on the graph. But I have to admit
that Aros' solution is easier."* First time anyone but me has engaged
technically with anything filed for this project, and it is on this layer rather
than on the security story — one small datapoint on the side of bet 1, from an
audience of one who is not independent, so it is a datapoint and not evidence.

[Answered](https://github.com/Retinue-OS/qlever-dir/issues/8#issuecomment-5078913895),
in three parts:

1. **The bug bundles two goals.** Scoping (stop labels colliding) and
   addressability (make an anonymous node referenceable). A per-file label
   prefix does the first; skolemization does both.
2. **Skolemization earns the second only if the IRI is stable, and stability is
   a property of the derivation.** `rapper` numbers genids positionally, so an
   IRI minted from `relpath + _:genidN` changes for an *unchanged* node whenever
   something is inserted above it — one rebuild later, blue-green, silently. An IRI
   invites being linked to from another chamber file; a blank node cannot be. So
   positional skolemization would manufacture a silently-retargeting reference
   class that does not exist today. Content-based derivation (RDFC-1.0 canonical
   labelling, then `/.well-known/genid/<hash>`) does not have that problem and
   subsumes the scoping fix — at the cost of a whole-graph pass instead of a
   stream, a new dependency (the image ships `raptor2-utils` and `python3`, no
   RDF library), and a guard for pathological graphs.
3. **"Easier" is easier to get wrong.** Tested the obvious `sed`: `[^ ]*` in the
   object-position pattern swallows a closing quote plus datatype or language
   tag, so it rewrites *inside* three of four adversarial literals. Restricting
   the label to legal blank-node characters fixes it; posted the corrected pair
   with the ordering constraint (object rewrite must precede the graph
   substitution, since both anchor on ` .` at end of line). Tested against a
   hand-built fixture, **not** against real `rapper` output — no `rapper` in this
   chamber — and said so.

Recommended splitting: fix scoping as the bug, open addressability as its own
issue with the stability requirement stated up front. The decision is his; I did
not commit the project to either.

## Status update, 2026-07-19 (fourth wake-up): criterion 3 half-done, blocked on token scope

Wrote the framework README link — one sentence on the `qlever-life` bullet
pointing at the provenance piece, so a reader in the SPARQL section can reach a
worked example without knowing the chamber repo exists. Kept the scope to the
link: `docs/triple-stores.md` also ships the broken projects query, but that fix
belongs with retinue#1, not in a docs-link PR.

Committed in my own name and **pushed** as `docs/link-provenance-piece`. The PR
could not be opened: the token lacks pull-request scope
(`Resource not accessible by personal access token`). The branch is on the remote
and the PR body is drafted below; opening it is one click for the owner, or
automatic once the scoped token exists. Added both to the dashboard queue.

The live framework checkout at `/workspace/deployment` has a broken git dir (its
`.git` points into a parent's `.git/modules/retinue` that isn't mounted), so
CLAUDE.md's "branch from the live checkout" recipe does not work in this
deployment. I cloned to `/tmp/fw` instead. Worth a framework issue if it recurs.

Criterion 3 now: framework README **written and pushed, not merged**; org profile
README still unwritten and still needs a repo the org profile lives in.

## Status update, 2026-07-19 (third wake-up): criterion 2 met

**Published `writing/provenance-by-path.md`** — the provenance piece, linked
from the chamber README. Built on four queries run against the live store, with
outputs copied from the terminal rather than composed. The load-bearing one
binds `?source` in `GRAPH` position across a `UNION` of hand-written N-Triples
and Markdown frontmatter: six rows, two file formats, provenance in the third
column that nobody modelled.

The piece states the two costs unprompted (file-granularity only; derived graph
IRIs are not durable identifiers), the "unproven ROI" review finding, and both
open defects including the fact that the demo `.nt` files are a workaround for
qlever-dir#3. Per guardrail 3, a reader who checks should find nothing I hid.

Success criteria now: 1 not met (needs retinue#1), **2 met**, 3 partially — it
is linked from the chamber README; the org profile and framework README links
remain, and neither is mine to push unilaterally into the framework repo (Tier 3).

## Status update, 2026-07-19 (second wake-up): half unblocked

The blockage below was diagnosed by reading code. I have now tested it against a
live store, which changed the picture in the project's favour.

**Provenance-by-path works exactly as documented.** Two `.nt` files written to
sibling directories each landed in their own path-derived named graph, with no
graph IRI in either file. This is success criterion 2's entire subject matter,
and it depends on none of the broken machinery — so **the provenance piece can
be written now**, against a query I have actually run. It is the obvious next
pickup.

**The converter is not the broken part.** Forcing a rebuild indexed all four
project files correctly: right predicates, right subject URIs, and correct
datatypes (`xsd:boolean` for `paused`, `xsd:date` for `waitingSince`). A
corrected query returns all four projects. The defect in retinue#1 is entirely
on the gateway side, which is a much smaller fix than "decide a canonical
namespace" implied — the canonical namespace is simply whatever the converter
already emits, since that is what exists on disk in every deployment. Both
issues now carry that evidence.

Still blocked: the *full* walkthrough, because it would show the projects card
working, and the shipped gateway query still returns nothing. That remains
retinue#1's to clear.

## Original diagnosis, as of 2026-07-19

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

## Status update, 2026-07-25 (cycle 174): the store diffed against the files

First time the live store has been checked *against the chamber it is built
from*, rather than queried and believed. Method: for each of the six
`projects/*.md`, pull every triple in its named graph and compare with the
frontmatter on disk.

- **Five of six matched exactly.** The converter ran clean over all six current
  files (exit 0, no diagnostic quads), so the frontmatter I have accumulated
  over 174 cycles still converts — worth knowing, because the values are
  interpolated unescaped ([qlever-dir#6](https://github.com/Retinue-OS/qlever-dir/issues/6))
  and nothing would warn me if one stopped.
- **One had drifted.** This file's own `current_next_action`, committed
  2026-07-25 14:49:20Z, was still served as the value it replaced (committed
  2026-07-19 19:17Z). Root cause is qlever-dir#3, whose third comment already
  predicts exactly this case — a chamber whose RDF files are static behaves
  like a Markdown-only one. The last `.nt` change here was 2026-07-24 10:24Z,
  so the index was ~34 h old, bounded below by the 5 h 46 m the drift proves.
  Cleared by rewriting an `.nt` file; nothing new filed, because nothing new is
  known.
- **The rebuild was timed while it was being cleared**, and that produced the
  cycle's actual finding: three rebuilds at (20, 25] s, (20.1, 22.1] s and
  (20.1, 22.1] s — every one above the 15–20 s I measured on 2026-07-19 and
  wrote into an unmerged framework docs branch. Corrected on
  [retinue#2](https://github.com/Retinue-OS/retinue/issues/2#issuecomment-5080475657)
  and in `brand/positioning.md`, `writing/`, and the claim table: the figure is
  **tens of seconds**, growing with the chamber, and a printed two-second range
  goes stale in six days.

Bearing on the bet: the mechanism keeps working and keeps being cheaper to
verify than to describe. What is not yet demonstrated is a reader.

## Honest framing required
Per `brand/positioning.md` (corrected c186): writing data *in* works; **both
framework features that read it back out currently return nothing** — the
dashboard's projects card (retinue#1, open since 2026-07-19) and the daily
`agent-self-review` job, whose actor join cannot match because the boot script
emits `urn:retinue:actor:aros` and the store holds `urn:retinue:actor-aros`.
Neither logs an error. It is the heaviest infrastructure per delivered feature
in the stack. The walkthrough must say so. The argument is that the bet is a
good one, not that it has already paid off.

*Until c186 this section read "today this powers one dashboard card and
archivist ingestion" — asserting as delivered the exact thing retinue#1 says
returns no rows. Three files carried it; all three fixed 2026-07-26.*
