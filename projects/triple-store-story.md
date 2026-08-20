---
type: project
id: proj-triple-store-story
title: "Make the triple-store layer the lead story"
goal: "The named-graph/converter architecture is explained well enough that a semantic-web engineer immediately sees why it is unusual."
goal_status: in_progress
current_next_action: "Aros, c884 (2026-08-20 17:3xZ): retinue-os/qlever-dir#13, his omnibus PR closing 8 of the 9 open qlever-dir issues in one pass (#2 .qleverignore, #3 converter-extension watch, #4 silent watcher death, #5 sed-built graph IRIs, #6 unvalidated frontmatter interpolation, #7 dead-endpoint-reported-healthy, #8 blank-node collisions, #10 new-directory race), reviewed against the diff (not just the description): watcher stderr-drain/restart, percent-encoded graph IRIs via a Python urlencode passed through awk on ENVIRON (no sed/shell interpolation of filenames), blank-node rewriting matched only at exact subject/object token positions (verified against the regex), and the supervision loop's poll()-before-reap_zombies() ordering (verified the call order in main(), matches the docstring's own constraint) all check out against the code, not just the PR prose. No defect found; no comment posted, per the established clean-review practice (2026-08-16 review's bet-5 clarification: a clean verification is a correct outcome, not a miss). Bearing on bet 1: if this merges, the qlever-dir defect count this project has been citing (8/9 open) drops to 1/9, and the reindex-latency and blank-node caveats in writing/provenance-by-path.md and docs/triple-stores.md should be re-checked against whatever lands, not assumed fixed from the PR title. NOT reviewed this pass: #6's frontmatter-validation claim (IRI-legal-character rejection) - narrower risk, deferred to the next PR touch or the merge itself. EARLIER, c342 (2026-08-01): criterion 1's blocker (retinue#1, dashboard projects card returns 0 rows) re-verified reproducing on main @ f1f8c72f; the canonical-namespace question was found half-answered by the framework's own files (kb# / colon-actor form already used by three framework-shipped producers/consumers, only this chamber's md2ttl.py disagrees) and posted as issuecomment-5149744968; not yet acted on by the owner. Criterion 3 (framework README link) confirmed merged and live (retinue#55); org-profile half stays chamber#4's open ask."
current_actor: actor-aros
waiting_since: 2026-07-19
expected_by: 2026-08-30
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

## c222 (2026-07-28) — the first time the store answered a design question for someone else

`writing/queries/newsfeed-keyframe-sample.rq`, posted as a
[comment on retinue#25](https://github.com/Retinue-OS/retinue/issues/25#issuecomment-5107457585).

The owner's news-agent proposal has three open questions; two of them are about
this layer. Sampling a time-relevance curve @now — bracketing keyframes with
`MAX`/`MIN` subqueries, linear `BIND` between them — runs in **64 ms** on the live
`qlever-life` endpoint and ranks three curve shapes exactly as the proposal
describes. So read-time sampling is the answer to "compute @now vs. materialize",
on evidence.

The part worth keeping for the walkthrough is the negative result, because it is
the kind of thing this layer's advocacy usually omits: **QLever can subtract two
`xsd:dateTime`s but cannot turn the result into a number.** `xsd:double(?t - ?now)`
and `xsd:double(?t)` both return unbound, so the interpolation `BIND` never
assigns and the row disappears with no error. A keyframe therefore needs epoch
seconds as `xsd:decimal` beside its `xsd:dateTime`, and the sample instant has to
be substituted by the caller rather than taken from `NOW()`. SPARQL 1.1 defines no
dateTime→number cast either, so this is the language, not the engine.

Two things this is evidence for, and one it is not. It is bet 1 working at the
scale of one reader: the triple-store layer answered a question the rest of the
architecture could not, and the answer was a query rather than a claim. It is also
the first use of this chamber's own store by anything other than this chamber. It
is **not** evidence about the section above — retinue#1 and the actor-join mismatch
are unchanged, and the framework's two store-reading features still return nothing.
A query I ran by hand is not a delivered feature, and the walkthrough keeps saying
so.

## c341 (2026-08-01) — the first half of criterion 3, met by a merge, in a project record that said otherwise

Success criterion 3 reads *"Both linked from the org profile and the framework
README."* Since 2026-07-19 this file has carried the framework half as **written
and pushed as branch `docs/link-provenance-piece`, unmergeable without PR scope
(chamber#6)**. That stopped being true at **2026-07-31T19:33:40Z**, when the
owner merged [retinue#55](https://github.com/Retinue-OS/retinue/pull/55).

Measured this cycle, from content rather than from the PR's badge (c270):

| | |
|---|---|
| `README.md` on `main @ f1f8c72f` | line 42 links `writing/provenance-by-path.md` |
| The branch this file named | **gone** — the remote holds `main` and `feat/chamber-secretary-style-override`, nothing else |
| Link target | **200** |
| The piece the framework now points at | blob `1fded9a9` on **both** `main` and `origin/main` |

The last row is the one worth having taken. The framework README now sends
readers *into a repository I cannot push to* — 55 commits deep at the time of
writing — so a correction made here after the merge would sit invisible behind
the same 403 that has held the dashboard stale for 33 consecutive delivery
checks, while the front door claimed to link the current text. It does not: the
blob is identical on both sides, `git diff origin/main..main -- writing/` is
empty, and the reader gets what I have. This is a negative result, and it is
worth exactly what it excludes.

**Still unmet, and not mine:** the org-profile half. `GET /repos/Retinue-OS/.github`
→ **404** and the org description is still empty, both unchanged since c251.
`writing/org-profile-README.md` stays `status: ready-for-owner`; it is chamber#4's
ask. Criterion 1 — the *full* walkthrough — still waits on retinue#1.

**The instrument gap, which is the transferable part.** c252 found this file's
handover field 36 cycles stale and gave `tools/pointer-check.py` an assertion for
it. That assertion checks the field **names** the newest write-up section. This
field named c222, and c222 *was* still the newest section — so the check ran
green for eight hours while `strategy.md` (objective 3, *satisfied 19:33:40Z*)
and this file (*unmergeable without PR scope*) asserted opposite things about the
same merge. **A handover field can be structurally current and factually wrong,
and nothing in `tools/` can tell the difference.** No instrument written for it
here (c268 rule 2): the general form — *when a merge lands, grep the chamber for
the blocker it cleared, not only for the wording it changed* — is c339's rule
pointed inward, and whether it deserves a checker is a question for the
2026-08-02 review, alongside c340's baseline-commit proposal.

## c342 (2026-08-01) — criterion 1's blocker re-verified, and the framework had already answered its open question

Criterion 1 (the full walkthrough) has waited on
[retinue#1](https://github.com/Retinue-OS/retinue/issues/1) since 2026-07-19,
because the projects card that `docs/triple-stores.md` presents as the payoff of
the whole converter mechanism returns no rows. Re-verified on `main @ f1f8c72f`
this cycle: **still reproduces**, unchanged by the 2026-07-29→31 merge wave that
edited both `scripts/web-gateway.py` and `webapp/components/projects.js`.

What changed is the shape of the question. I filed #1 saying I had no standing to
decide which namespace is canonical, and that framing was half wrong:

| Component | Ships with | Namespace | Actor URI |
|---|---|---|---|
| `web-gateway.py:1929-1930` — consumer | framework | `kb#` | `urn:retinue:actor:reto` |
| `agent-self-review.py:31,43-50` — consumer | framework | `kb#` | joins `?actor a kb:AiAgent` |
| `discover-agents.py:46,139-140` — **producer**, every boot | framework | `kb#` | `urn:retinue:actor:<name>` |
| `<chamber>/projects/.qlever/md2ttl.py:21,114` — producer | a chamber | `project#` | `urn:retinue:` + raw value |

Three framework files already agree; the dissenter is deployment content, and
nothing the framework ships emits `project#` at all. Measured on the live store
rather than argued: the self-review gate returns **0**, the same count over
`project#Project` returns **6**.

Two consequences for this project. First, the decision is now cheap enough to be
made — posted as
[issuecomment-5149744968](https://github.com/Retinue-OS/retinue/issues/1#issuecomment-5149744968),
with the cost of each option in files. Second, if the answer is *align the
converter*, criterion 1 stops being owner-blocked: `projects/.qlever/md2ttl.py`
is this chamber's own file and the diff is mine to land. That is the first time
any part of criterion 1 has been on my side of the line.

Note against this file's own frontmatter: `current_actor: actor-aros` is the
`urn:retinue:` + raw-value form, i.e. the losing shape. Whatever #1 resolves to,
this chamber's project files are one of the things that has to change with it.

## c884 (2026-08-20) — qlever-dir#13 reviewed: omnibus fix for 8 of 9 open defects

Found on this wake-up (opened 15:51:42Z, three hours before) — reviewed per
bet 5's operating clause. This is the PR version of the issue list this
project has cited since c174/c342 as evidence the layer works but is young:
watcher reliability (#3, #4, #10), quad-emission correctness (#5, #8),
supervision (#7), the converter-example validation gap (#6), and a new
`.qleverignore` feature (#2). One commit per issue, 676 insertions across 6
files.

Cloned the branch (`gh pr checkout` equivalent — fetched `pull/13/head`
directly, no local qlever/rapper/inotifywait binaries available, same
constraint the PR's own "Verification" section names) and read the diff
against the description's claims rather than trusting the prose:

- **#5 (sed-built graph IRIs) and #8 (blank-node collisions).** The fix
  routes the graph IRI and a per-file blank-node prefix through `awk` via
  `ENVIRON`, not `-v` and not string-interpolated into the program text —
  so a filename containing `&`, backslash, or awk-special characters can't
  corrupt the substitution. Blank-node rewriting matches only a line
  starting `_:` (subject position) or the last whitespace-delimited token
  before the stripped trailing ` .` when that token matches
  `^_:[A-Za-z0-9_][A-Za-z0-9_.-]*$` (object position) — a literal object
  always ends in a closing quote (or `^^<...>`/`@lang` after it), so it
  cannot collide with that pattern. Checked directly against the regex, not
  assumed from the comment above it.
- **#7 (dead endpoint reported healthy).** `nginx_is_alive()` reads
  `/proc/<pid>/stat` and treats state `Z` as dead (`os.kill(pid, 0)` can't
  tell a zombie from a live process, which the code's own docstring names as
  the reason). The main loop's ordering — `active_proc.poll()` before
  `reap_zombies()`, both before the next `time.sleep(1)` — matches the
  constraint `reap_zombies()`'s own docstring states (must never run before
  Popen has had a chance to observe/reap its own child). Verified the call
  order in `main()` directly, not inferred from the docstring alone.
- **#3/#4/#10 (watcher).** stderr is now drained on a daemon thread before
  it can block `inotifywait`'s `write()`; the process is restarted with a
  5 s backoff on any exit; `ISDIR` events and `.qlever/converters.json`/
  `.qleverignore` changes are classified separately from ordinary RDF-file
  events and each triggers the correct cache refresh. `classify_watch_event`
  was read directly; the KEEP-IN-SYNC comment between `build_index.sh`'s
  inline heredoc and `orchestrator.py`'s `converter_extensions()` names the
  actual risk (the two must agree or the watcher and the builder disagree
  about what's indexed) rather than asserting they can't drift.

**Not reviewed to the same depth:** #6's frontmatter-validation claim
(IRI-legal-character rejection in `md2ttl.py`) and #2's `.qleverignore`
matcher beyond a read-through — narrower surface, lower risk, deferred
rather than skipped. No defect found in what was checked; no comment posted,
per the 2026-08-16 review's clarification that a clean verification is a
correct outcome for bet 5, not a miss.

**Bearing on bet 1.** This project has been citing "qlever-dir defects: 8/9
open" as the honest state of the layer backing the triple-store story. If
#13 merges as written, that becomes 1/9 — a materially different claim to
make in public copy. The two published pieces that cite qlever-dir issue
numbers (`writing/provenance-by-path.md`'s caveat on `qlever-dir#3`,
`docs/triple-stores.md`'s latency caveat) should be re-checked against
whatever actually lands, not updated from the PR title — the same
merged-is-not-present lesson objective 3 already paid for once (c270).
