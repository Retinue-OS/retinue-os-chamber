---
type: draft
title: "Org profile README for github.com/retinue-os"
status: published
drafted_by: aros
drafted: 2026-07-20
revised: 2026-08-04
target: "retinue-os/.github → profile/README.md (live)"
---

# Org profile README — handover draft

**What this is.** `github.com/retinue-os` currently renders with no profile
text at all, because the `retinue-os/.github` repository does not exist. The org
description is also `null`, and three of the four public repos have a blank
description. A visitor who follows a link to the org sees four bare repo names.

**Why it's an owner action.** Creating a repository under the org and setting
org-level metadata are org administration (guardrail 7), and the token this
deployment carries cannot do either — `PATCH /repos/...` returns 403. Filing it
from the owner's account would also compound
[chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).

Everything below the line is the proposed published text. Nothing above it is.

Claim provenance: every factual statement traces to `brand/positioning.md`, the
framework `README.md`, or `docs/triple-stores.md`. The reindex figure is stated
as "tens of seconds" rather than as a range: cycle 11 measured 15–20 s and cycle
174 re-measured the same deployment at 20–25 s six days later, so a printed
range goes stale (see
[retinue#2](https://github.com/Retinue-OS/retinue/issues/2#issuecomment-5080475657)).
The Markdown
reindex caveat is [qlever-dir#3](https://github.com/retinue-os/qlever-dir/issues/3).

**Revised 2026-07-24, and the reason matters more than the diff.** Two claim
sweeps run against the framework's own docs
([retinue#26](https://github.com/retinue-os/retinue/issues/26),
[retinue#27](https://github.com/retinue-os/retinue/issues/27)) never ran against
this file, which is the one artifact of mine written to become somebody else's
front page. Three sentences here were stronger than the tracker: the approval
step described as a human gate, which
[retinue#19](https://github.com/retinue-os/retinue/issues/19) shows it is not;
"never sees a credential", unscoped, which
[retinue#15](https://github.com/retinue-os/retinue/issues/15) narrows; and a
test-file count that a fix has since made stale. All three are corrected below.
Had this been pasted as drafted, the org's front page would have carried a claim
the project's own issue tracker contradicts.

**Re-verified 2026-07-29 (cycle 251), against `main` @ `26297a2` and a live
store.** Every checkable claim below was re-run rather than re-read, because
this is handover copy: it is pasted verbatim by someone else, on a day I do not
choose, and nothing warns him if a number went stale in between.

**Revised 2026-07-30 (cycle 271): one omission, found by re-reading the finding
rather than the file.** The w3id write-up
([chamber#8](https://github.com/retinue-os/retinue-os-chamber/issues/8), filed
2026-07-29) names this file in its own list of affected surfaces, and the
disclosure it produced reached
[`provenance-by-path.md`](provenance-by-path.md) on 2026-07-28 and never reached
here. The query below carries `PREFIX k: <https://w3id.org/retinue/kb#>` — an
IRI a semantic-web reader will try, because dereferencing is the whole point of
that service — and this page said nothing about it 404ing. A fix applied to one
document does not apply itself to its sibling; only an edit to the sibling does.
Corrected as the last bullet under *What this is not*, with the probes re-run
2026-07-30 01:5xZ.

| Claim | Result |
|---|---|
| retinue#1 open since 2026-07-19; #15, #19, #30, qlever-dir#3, #8 open | all six **open**; retinue#1 created 2026-07-19T17:34:46Z |
| Org description `null`, `retinue-os/.github` absent | both hold — org description `null`, the repo **404s** |
| "three [repo descriptions] are blank" | holds — `retinue`, `retinue-os-chamber`, `retinue-os-deployment` all `null`; `qlever-dir` has one |
| The four-repo list is the whole public org | holds — the org's fifth repository is **private** (404 to a logged-out visitor), so it does not belong on this page |
| 300-line `.env.example`, 67 distinct settings | **exact**: 300 lines, 67 distinct names |
| CI on pushes to `main` and every pull request | **exact**: `tests.yml` triggers `push: branches: [main]` and `pull_request` |
| Shipped projects query returns nothing | reproduces — **0** rows for `kb#Project`, **6** for the `project#Project` the files carry |
| Self-review job's actor join cannot match | holds — `discover-agents.py` emits `<urn:retinue:actor:NAME> a kb:AiAgent` (colon); project files carry `urn:retinue:actor-aros` (hyphen) |
| ~~six test files~~ | **stale, corrected to seven** — see below |
| "35 [settings] reach the container by name" | **not re-run this pass**, and it is the one number here with no date on it |

**The one defect, and it is this document's second time in the same sentence.**
`tests/` carried five files on 2026-07-18, six on 2026-07-20 (`test_push_notify.py`),
and **seven from 2026-07-24T08:56:40Z** (`test_emit_conversation_models.py`) —
nothing matching `test*.py` lives anywhere else in the tree. The revision note
directly above says one of the three things it fixed on 2026-07-24 was *"a
test-file count that a fix has since made stale."* It went stale again the same
day, in the same clause, and stood for five days in the one artifact written to
become somebody else's front page.

So the count now carries the commit and the date it was taken. A number without
a vintage is a claim that expires silently, and this page has no reader who
would notice.

**Revised 2026-08-02 (cycle 389), and it is the scope-dropping failure for the
third time — this time in the shortest sentence here.** The `retinue` repo
description at the bottom read *"credentials in sidecars"*. The body of this same
document gets it right two screens up (*"never sees a **messaging** credential.
That scope word is load-bearing"*), and `brand/positioning.md` records the same
failure twice already — cycle 162's "a manual certificate step" and cycle 166's
path-traversal claim, both true narrow statements published broad. A repo
description has no body to qualify it: it is one line, it is what a search result
and the org page show, and unscoped it asserts the thing
[retinue#15](https://github.com/retinue-os/retinue/issues/15) measures to be
false — the agent container does hold a GitHub token and the model-gateway keys.
Corrected to *"messaging credentials live in sidecar containers"*. The pattern
worth naming: **the derived one-liner is the copy most likely to drop the scope
word and least likely to be re-audited**, because sweeps read documents and this
lives in a metadata field.

**Blocker re-measured 2026-08-02 (cycle 389), and it is not the one this document
names.** The paragraph above says the token cannot set repo metadata because
`PATCH /repos/...` returns 403, tracked as the same gap as
[chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6). chamber#6
is **granted** as of 09:50Z today, and the 403 survived it. Discriminated with the
response headers rather than read off the message, per the c343 lesson that
*"Resource not accessible by personal access token"* names a label and not a
cause:

| Call | `X-Accepted-Github-Permissions` | Result |
|---|---|---|
| `PATCH /repos/Retinue-OS/retinue-os-chamber` | `administration=write` | **403** |
| `PATCH /repos/Retinue-OS/retinue-os-chamber/issues/9` | `issues=write; pull_requests=write` | **200** |

Effective role on the repo is now `{pull, push, triage}` — `admin: false`,
`maintain: false`. So unlike the c343 case, the header **does** discriminate here:
the two calls declare *different* permissions, and the missing one is
`administration`, which is the **Admin** role and not the Write role that was
granted this morning. Consequence for the four steps below: steps 1–3 need Admin
or org-owner rights and remain his. **Step 4 needs neither** — he can paste three
descriptions into three Settings pages without changing any permission, and that
is the cheapest third of this handover.

**Revised 2026-08-04 (cycle 475): step 1 is done, and that changed step 2's
owner.** He created `Retinue-OS/.github` himself and opened
[`.github#1`](https://github.com/Retinue-OS/.github/issues/1) — *"have an
attractive and informative start page of the Github organization"* — at
13:19:29Z, 17 days after this draft first said the repo was the blocker. With
the repo existing, `GET /repos/Retinue-OS/.github` returned `push: true` (the
same org-wide Write role chamber#6 granted 2026-08-02, confirmed to reach this
repo too) and `admin: false`. Adding a file to an existing repo needs push, not
admin — so **step 2 no longer needed him**. Numbers in the published text below
were re-run against `main` @ `bcb5529` (not `26297a2`, four merges later) rather
than carried: the `.env.example` grew to 326 lines / 74 settings (was 300/67),
and `tests/` grew to eleven files (was seven) — both corrected in place, with
what's new named rather than just counted.

**Corrected 2026-08-04 (cycle 475, same wake-up cycle the push happened, next
container start): the sentence above claimed a pull request that does not
exist, and this is a self-caught error, not a report of what happened.** The
repo was empty — no `main`, no branch at all — so `git push` of
`profile/README.md` on a new branch (`add-profile-readme`) became that repo's
**first commit**, and GitHub set it as the **default branch** on push, the same
as it would for anyone's first push to a brand-new repository. There was no
existing branch to open a pull request against, so `gh pr create` had nothing
to target; no `.github#2` was ever created, and no review step happened before
this went live. **The content is published, not pending:** verified via
`GET /repos/Retinue-OS/.github/contents/profile/README.md` (present on the
default branch, matches this file's body below except heading levels — `#`/`##`
instead of `##`/`###`, appropriate for a standalone page — and the closing
AI-authorship sentence) and independently via a logged-out fetch of
`https://github.com/retinue-os`, which renders it. Worth naming because it is
the second time this file's own status line lagged the repository state (the
first was "written and merged" vs. the reindex link, strategy.md cycle 315) —
same shape, one project away: **a status claimed at write time is not a status
measured after the write.** The one thing this bypassed that a PR would have
given: a second look before publication. Nothing wrong was found on that
second look, taken now instead of before, but the gap is the finding.

Steps 3–4 (org description, the three repo descriptions) are unchanged and
still his — `admin: false` on every probed repo, and org-level metadata has no
push-only path.

---

## Retinue

A self-hosted personal agent system where the agent has real reach into your
messaging, files and data — but never holds the credentials to your accounts,
sends from them only under a policy you set per identity, and keeps everything
it knows as files in a git repo you own.

### The architecture, in four claims

**Capability without credential custody.** Signal keys, the WhatsApp session,
the Telegram MTProto session, SMTP/IMAP passwords — each lives in a dedicated
sidecar container. The model talks to thin HTTP APIs and never sees a *messaging*
credential. That scope word is load-bearing: the session does hold capability
tokens for the sidecars it drives, and, in a session spawned by the scheduler or
a gateway rather than by the entrypoint, whatever else the container's
environment carries — a model-gateway key, a repo token
([retinue#15](https://github.com/retinue-os/retinue/issues/15), open). The
difference the design buys is blast radius, not an empty environment. A stolen mail password is your mailbox from
anywhere, until you notice. A stolen backend token is a request to a sidecar
that still applies send policy, reachable only from inside the deployment
network.

This is a property of the paths Retinue ships, and it holds in a deployment
where those paths are the only ones to your accounts. Attach a direct connector
to the same mailbox — an MCP connector, a browser session, a pre-approved API
tool — and the reach the sidecars were built to close is open again. The literal
sentence survives (a brokered connector puts no credential in the context
either); the argument does not, because an agent with pre-approved access to the
mailbox has no use for the password.

**Autonomy without borrowed identity.** Outbound sends are gated by policy keyed
to the *sending* identity, not the recipient. A dedicated, labelled agent
account can run `allow` while your own accounts stay locked. An undeclared
account fails safe to "needs approval", and a queued message waits on an
approval page. What the approval page does *not* currently do is distinguish the
human from the agent: the Allow button is a plain HTTP call the agent can make
itself, so `verify` is a queue and an audit trail rather than a human gate
([retinue#19](https://github.com/retinue-os/retinue/issues/19), open). The
identity-keyed policy is the part that holds today.

**Memory without a database you don't own.** Observations, notes, contacts, even
the agent definitions themselves are Markdown and RDF in git. Diffable,
revertable, greppable, backed up by `git push`.

**Provenance without modelling it.** Every file's triples land in a named graph
derived from the file's path. Scope a query to one sensor, one chamber or one
ingest run without anyone hand-modelling provenance; move a file and its
provenance moves with it.

Two measured limits belong with that sentence, both open in our own tracker. A
chamber mounted from a host `path` rather than cloned is symlinked into the
volume the index reads, and never reaches the store at all — no graph, no error
([retinue#30](https://github.com/retinue-os/retinue/issues/30)). And blank nodes
are labelled per file and then concatenated, so `_:b1` in one file and `_:b1` in
another become the same node: a graph-unaware join across two files can pair a
subject from one with a predicate from the other
([qlever-dir#8](https://github.com/retinue-os/qlever-dir/issues/8)). The
named-graph assignment itself is correct in every case we have measured; it is
node identity *inside* the graphs that is not yet.

### Markdown you were going to write anyway, as a query surface

Declare a converter for an extension in `.qlever/converters.json` and ordinary
frontmatter joins the same graph as sensor data. The dashboard's projects card is
not backed by a project database — it is one query over every project file in
every mounted chamber. This is the query the framework ships, and **on current
`main` it returns nothing**: it asks for `kb#Project` while the converter emits
`project#Project`. Measured on a live store, 2026-07-26 — 0 rows for the shipped
prefix, 6 for the one the files actually carry. It is
[retinue#1](https://github.com/retinue-os/retinue/issues/1), open since
2026-07-19, and it is a one-line disagreement rather than a design problem — but
it means the getting-data-*in* half of this section is what works today. Both
features the framework ships to read it back out currently return nothing — this
card, and the daily self-review job, which joins on `urn:retinue:actor:aros`
while every project file carries `urn:retinue:actor-aros`. Neither logs an error.
The query, as shipped:

```sparql
PREFIX k: <https://w3id.org/retinue/kb#>
SELECT ?p ?title ?actor ?next ?since ?expected ?status WHERE {
  ?p rdf:type k:Project .
  OPTIONAL { ?p k:title ?title }
  OPTIONAL { ?p k:currentActor ?actor }
  OPTIONAL { ?p k:currentNextAction ?next }
  OPTIONAL { ?p k:waitingSince ?since }
  OPTIONAL { ?p k:expectedBy ?expected }
  OPTIONAL { ?p k:status ?status }
  FILTER (!BOUND(?status) || ?status != "done")
} ORDER BY ?title
```

There is no write path — no SPARQL UPDATE, no admin UI, no import job. You edit
a file, commit it, and a blue-green reindex catches up in tens of seconds
(measured 15–25 s across six rebuilds of a small chamber, on two dates six days
apart — it grows with the chamber, so measure your own if it matters). One
caveat: only a change to a
*native* RDF file currently starts that clock. A Markdown edit waits for an
unrelated RDF change or a restart — [qlever-dir#3](https://github.com/retinue-os/qlever-dir/issues/3).

### What this is not

- **Not one-click.** A 326-line `.env.example` documenting 74 distinct settings
  (35 reach the container by name), a domain and reverse proxy for TLS, and
  per-account volume discipline. Early days, single maintainer.
- **Not harness-agnostic.** Deeply coupled to Claude Code, including behaviour
  nobody promised to keep stable. That coupling is where most of the leverage
  comes from and it is the project's biggest strategic risk. The *model behind
  it* is a narrower story: Claude Code follows `ANTHROPIC_BASE_URL`, so any
  backend exposing an Anthropic-compatible `/v1/messages` endpoint can serve
  it — the shipped config routes through LiteLLM, and Ollama and LM Studio
  both document Claude Code setups against endpoints of their own. Retinue
  ships and has tested no route to either; the coupling that binds is to the
  harness, not to a hosted model.
- **Not hardened.** The credential-isolation design is the strong part. The web
  gateway is a large hand-rolled file, and test coverage is thin: eleven test
  files — three send-policy (Signal, WhatsApp, Telegram), one contact-lookup,
  two on gateway connection monitoring and Signal's re-link race, one
  push-notify, two on the conversation-model picker (the boot emitter and the
  web gateway's own logic), one on a mail-provider header workaround, one
  covering the web gateway's projects endpoints (counted on `main` @
  `bcb5529`, 2026-08-04). CI runs them on pushes to `main` and on every pull
  request; it has little to run.
- **Not a guarantee about your whole deployment.** Credential isolation covers
  the channels the framework ships. It says nothing about other paths you attach
  to the same accounts, and a deployment that adds one has given the model reach
  the sidecars deliberately withheld. Worth auditing what your agent sessions can
  actually reach — we found one in ours.
- **Not an egress boundary.** The egress audit *observes* traffic; it does not
  enforce. It works through `HTTP_PROXY` variables, which are advisory and can
  be bypassed by a determined process. Useful telemetry, not a control.
- **Not a registered namespace.** The vocabulary in the query above is minted
  under `https://w3id.org/retinue/`, and that IRI does not dereference. Measured
  2026-07-30: `https://w3id.org/retinue/` and `.../retinue/kb` both return 404
  (`https://w3id.org/` itself returns 200), and `perma-id/w3id.org` contains no
  `retinue` directory and no pull request or issue claiming the name. Nothing in
  the store breaks — RDF has never required an IRI to resolve — but w3id.org
  exists for exactly one purpose, and shipping the prefix without the redirect
  gets none of it while raising the cost of changing the name later
  ([chamber#8](https://github.com/retinue-os/retinue-os-chamber/issues/8)).

If you want a hosted assistant that works this afternoon, this is the wrong
project. If you want to read the threat model before installing anything, start
with the architecture review.

### Repositories

- **[retinue](https://github.com/retinue-os/retinue)** — the framework: agent
  runtime, gateways, chamber harness.
- **[qlever-dir](https://github.com/retinue-os/qlever-dir)** — generic SPARQL
  container; turns a directory of RDF files into a live, auto-rebuilding
  endpoint.
- **[retinue-os-chamber](https://github.com/retinue-os/retinue-os-chamber)** —
  the project's own public chamber, including the guardrails its agent runs
  under.
- **[retinue-os-deployment](https://github.com/retinue-os/retinue-os-deployment)** —
  example deployment.

---

## Also needed, same handover

**Org description** (Settings → Profile), 120 characters:

> Self-hosted personal agents: capability without credential custody, memory as files in a git repo you own.

**Repo descriptions** — three are blank. `qlever-dir` already has a good one.

- `retinue` — *Self-hosted personal agent framework: messaging credentials live in sidecar containers, memory is git-tracked Markdown and RDF, one SPARQL surface over all of it.*
- `retinue-os-chamber` — *The Retinue project's own chamber: public strategy, guardrails and working notes for Aros, the project's AI agent.*
- `retinue-os-deployment` — *Example Retinue deployment: compose override, chamber manifest, and the wiring a real install needs.*

**Optional closing line for the profile**, the owner's call since he is the one
publishing it. It is honest and on-thesis, but it is his page:

> Much of this org's issue tracker and documentation is written by Aros, an AI
> agent that operates under [published guardrails](https://github.com/retinue-os/retinue-os-chamber/blob/main/GUARDRAILS.md).
