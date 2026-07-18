---
type: reference
title: "Retinue positioning — what we claim and what we don't"
---

# Positioning

The source of truth for every public claim Aros makes. If a sentence isn't
supported here or in the framework's own docs, it doesn't go out.

## One sentence

Retinue is a self-hosted personal agent system where the agent has real
capability over your messaging, files and data — but never holds your
credentials, can't speak as you without your approval, and keeps everything it
knows as files in a git repo you own.

## The thesis, in three clauses

**Capability without credential custody.** Signal keys, the WhatsApp session,
the Telegram MTProto session, SMTP/IMAP passwords — all live in dedicated
sidecar containers. The model talks to thin HTTP APIs. A prompt-injected agent
cannot steal what it never sees.

**Autonomy without send authority.** Outbound messages are gated by policy keyed
to the *sending identity*, not the recipient. Undeclared accounts fail safe to
"needs approval". An agent can never approve its own send.

**Memory without a database you don't own.** Observations, notes, contacts, even
agent definitions — markdown and RDF in git. Diffable, revertable, greppable,
backed up by `git push`.

## The underrated fourth: the triple-store layer

The July 2026 architecture review marked this "unproven ROI" — fairly, because
`docs/triple-stores.md` did not exist yet. With it documented, this is arguably
the most genuinely novel part of the system, and Aros should lead with it more
often than the security story, which is easier to explain but less unusual.

What's actually different:

- **Provenance is free.** Every file's triples land in a named graph derived
  from the file's path. Scope a query to one sensor, one chamber, or one ingest
  run without anyone modelling provenance by hand. Move a file and its
  provenance follows.
- **Files that were never meant to be data become queryable.** Declare a
  converter for an extension in `.qlever/converters.json` and ordinary Markdown
  frontmatter — projects, goals, contact lists — joins the same graph as sensor
  data. No plugin API, no registration, no second authoring step. The artifact
  you were going to write anyway *is* the graph.
- **One query surface over heterogeneous chambers.** A standard vocabulary
  (SOSA for observations) means a glucose reading, a sleep score and a step
  count are the same shape. Adding a device is a new URI, not a new schema.
- **No write path at all.** No SPARQL UPDATE, no admin UI, no import job. You
  edit a file, commit it, and a blue-green reindex catches up in ~15 seconds.

The honest caveat, which Aros states unprompted: today this powers a dashboard
card and archivist ingestion. It is the heaviest infrastructure per delivered
feature in the stack. It is a bet that cross-domain queries become load-bearing,
and the bet is not yet won.

## What we do not claim

Restated from `GUARDRAILS.md` §3 because this is where enthusiasm leaks:

- The egress audit **observes**; it does not enforce. It works through
  `HTTP_PROXY` environment variables, which are advisory.
- The web gateway is large, hand-rolled, and thinly tested. CI does not yet run
  the test suite.
- The project is coupled to non-contractual Claude Code behaviour. That is where
  most of its leverage comes from, and it is a real strategic risk.
- Setup is a wall: ~30 environment variables, a manual certificate ceremony,
  per-account volume discipline. Single maintainer, early days.

Saying these first is not modesty, it's strategy. The audience most likely to
contribute is the audience most likely to notice them unaided.

## Who this is for

- People who want an agent with real reach into their life and are unwilling to
  hand a hosted service their message history.
- People who have watched the personal-agent projects of 2025–26 leak, and want
  to read the threat model before installing.
- Semantic-web people, who will recognise what the chamber/named-graph design is
  doing and are an underserved audience for agent tooling.

## Who this is not for

Say so plainly when it comes up — it costs nothing and buys credibility:

- Anyone wanting a one-click install today.
- Anyone who needs it model-agnostic.
- Anyone who needs sub-second responses; every message is a fresh session.
- Anyone who can't self-host, or doesn't want to operate a Compose stack.
