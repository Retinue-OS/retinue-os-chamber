---
type: draft
title: "Org profile README for github.com/retinue-os"
status: ready-for-owner
drafted_by: aros
drafted: 2026-07-20
target: "retinue-os/.github → profile/README.md"
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
framework `README.md`, or `docs/triple-stores.md`. The 15–20 s figure is the
measured range from cycle 11, not the docs' rounded "~15 seconds". The Markdown
reindex caveat is [qlever-dir#3](https://github.com/retinue-os/qlever-dir/issues/3).

---

## Retinue

A self-hosted personal agent system where the agent has real reach into your
messaging, files and data — but never holds your credentials, cannot speak as
you without your approval, and keeps everything it knows as files in a git repo
you own.

### The architecture, in four claims

**Capability without credential custody.** Signal keys, the WhatsApp session,
the Telegram MTProto session, SMTP/IMAP passwords — each lives in a dedicated
sidecar container. The model talks to thin HTTP APIs and never sees a
credential. It does still hold capability tokens for the services it drives; the
difference is blast radius. A stolen mail password is your mailbox from
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
approval page until a human releases it.

**Memory without a database you don't own.** Observations, notes, contacts, even
the agent definitions themselves are Markdown and RDF in git. Diffable,
revertable, greppable, backed up by `git push`.

**Provenance without modelling it.** Every file's triples land in a named graph
derived from the file's path. Scope a query to one sensor, one chamber or one
ingest run without anyone hand-modelling provenance; move a file and its
provenance moves with it.

### Markdown you were going to write anyway, as a query surface

Declare a converter for an extension in `.qlever/converters.json` and ordinary
frontmatter joins the same graph as sensor data. The dashboard's projects card
is not backed by a project database — it is one query over every project file in
every mounted chamber:

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
a file, commit it, and a blue-green reindex catches up in 15–20 seconds
(measured on a small file, three rebuilds). One caveat: only a change to a
*native* RDF file currently starts that clock. A Markdown edit waits for an
unrelated RDF change or a restart — [qlever-dir#3](https://github.com/retinue-os/qlever-dir/issues/3).

### What this is not

- **Not one-click.** Around thirty environment variables, a manual certificate
  step, and per-account volume discipline. Early days, single maintainer.
- **Not model-agnostic.** Deeply coupled to Claude Code, including behaviour
  nobody promised to keep stable. That coupling is where most of the leverage
  comes from and it is the project's biggest strategic risk.
- **Not hardened.** The credential-isolation design is the strong part. The web
  gateway is a large hand-rolled file, and test coverage is thin: five test
  files, concentrated on send-policy and contact-lookup logic. CI runs them on
  every push and pull request; it has little to run.
- **Not a guarantee about your whole deployment.** Credential isolation covers
  the channels the framework ships. It says nothing about other paths you attach
  to the same accounts, and a deployment that adds one has given the model reach
  the sidecars deliberately withheld. Worth auditing what your agent sessions can
  actually reach — we found one in ours.
- **Not an egress boundary.** The egress audit *observes* traffic; it does not
  enforce. It works through `HTTP_PROXY` variables, which are advisory and can
  be bypassed by a determined process. Useful telemetry, not a control.

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

- `retinue` — *Self-hosted personal agent framework: credentials in sidecars, memory as git-tracked Markdown and RDF, one SPARQL surface over all of it.*
- `retinue-os-chamber` — *The Retinue project's own chamber: public strategy, guardrails and working notes for Aros, the project's AI agent.*
- `retinue-os-deployment` — *Example Retinue deployment: compose override, chamber manifest, and the wiring a real install needs.*

**Optional closing line for the profile**, the owner's call since he is the one
publishing it. It is honest and on-thesis, but it is his page:

> Much of this org's issue tracker and documentation is written by Aros, an AI
> agent that operates under [published guardrails](https://github.com/retinue-os/retinue-os-chamber/blob/main/GUARDRAILS.md).
