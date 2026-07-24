---
type: reference
title: "Retinue positioning — what we claim and what we don't"
---

# Positioning

The source of truth for every public claim Aros makes. If a sentence isn't
supported here or in the framework's own docs, it doesn't go out.

## Before the claims: say who is writing

Added cycle 44, after an audit of this file and `writing/` for **disclosure**
rather than accuracy. This file governed what may be claimed and said nothing
about who is claiming it, so a piece drafted straight from it carried no
disclosure requirement. The two finished essays disclose in their standfirst
because a previous generation chose to, not because anything here asked for it.
GUARDRAILS.md §1 is binding either way; this is the reminder placed where copy
is actually composed.

**Every public surface Aros authors states that an AI authored it** — not only
posts and replies, but generated pages, dashboards, issue bodies and repo
metadata. The test is guardrail 1's: would a reasonable reader assume a human
wrote this? A byline reading "kept by Aros" fails that test, because "Aros"
reads as a person's name. The same audit found exactly that on the live public
dashboard (`docs/index.html`), unfixed since publication; it now names him as
an AI agent in the header and links the guardrails and log from the footer.

One deliberate exception: the org profile draft in `writing/`. That text is
published by the owner on his own org page, under his review, so it is his
byline rather than a hidden one — the disclosure line there is offered as his
call, not required.

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

State this precisely, because the precise version is the true one: what the
sidecars remove from the model's reach are the **messaging and personal-data
credentials**. The agent container does still hold capability tokens for the
services it is meant to drive — the e-mail and conversation backend tokens, and
a GitHub token. The difference is blast radius, and it is a real difference: a
stolen SMTP password is the user's mailbox, from anywhere, until they notice; a
stolen backend token is a request to a sidecar that still applies send policy,
only reachable from inside the deployment network. "The agent holds nothing
sensitive" would be an overclaim. "The agent never holds the credentials to
your accounts" is the claim, and it survives inspection.

*Calibration, cycle 71 — the credential scrub is not applied at every spawn
point today.* The claim above describes the design and holds, **in part**, for
the **main remote-control session**: the entrypoint unsets `ANTHROPIC_API_KEY`
and `EMAIL_PASS*` before it `exec`s the agent — and nothing else. (*Corrected
cycle 155: this sentence read "`ANTHROPIC_API_KEY`, `EMAIL_PASS*`,
`GARMIN_PASSWORD` and the rest", which overstates the scrub in the project's
favour. Measured against `main` at `92af09c`: `scripts/entrypoint.sh` has
exactly two `unset` sites, line 401 and the `EMAIL_PASS*` loop at 409–411.
`GARMIN_PASSWORD` appears nowhere in it, and neither do the model-gateway keys
or the GitHub token — so even the scrubbed main session keeps those.*) It
does **not** currently hold for **gateway- and scheduler-spawned `claude -p`
sessions** — the dashboard conversation tabs and scheduled jobs, i.e. the
sessions a user interacts with most. Those are forked earlier in the entrypoint,
before the scrub, and inherit the full credential-bearing environment;
`EMAIL_PASS`, `GARMIN_PASSWORD`, `LITELLM_MASTER_KEY`, `GITHUB_TOKEN` and
`OPENROUTER_API_KEY` are readable via `printenv` there. (*Amended cycle 155,
re-measured from inside a scheduler-spawned session: `GITHUB_TOKEN`,
`OPENROUTER_API_KEY`, `LITELLM_MASTER_KEY` and `LITELLM_DB_PASSWORD` are present;
`EMAIL_PASS*` and `GARMIN_PASSWORD` are set nowhere in this deployment — absent
from PID 1, the web gateway and the scheduler — so that half of the list rests on
retinue#15's measurement and not on mine. Say "the variables this deployment
sets" rather than naming a list I have only partly seen.*) Owner-filed and public,
measured in a live dashboard session, at
[retinue#15](https://github.com/retinue-os/retinue/issues/15), with a proposed
fix that keeps the existing unset pattern but applies the deny-list at each
spawn point. This is an implementation gap, not an architecture defect — the
sidecar design intends these variables gone, and the fix does not change the
design — but until it lands, **Aros does not present the sidecar isolation as
complete across all sessions.** The precise, currently-true form is: the
credentials live in sidecars, the *design* keeps them out of the agent's
environment, and today that scrub reaches the main session but not the
gateway/scheduler-spawned ones. Named here because this is the source of truth
for what may be claimed, and the claim-vs-reality gap this project's credibility
rests on has to be visible where copy is composed, not only in an issue tracker.

**Scope this to the framework's own channels, and say so.** The sidecar property
is a property of the paths Retinue ships — the Signal, WhatsApp and Telegram
gateways, and the mail backend. It is not a property of every path an agent
session might have to the same accounts. A deployment that also attaches a
direct connector to the user's mailbox or chat accounts (an MCP connector, a
browser session, a pre-approved API tool) has reopened the reach the sidecars
were built to close, and the claim no longer describes that deployment.

The literal sentence usually survives this — a connector brokered through a
remote proxy puts no credential in the model's context either. What does not
survive is the security property the sentence is selling: *a prompt-injected
agent cannot steal what it never sees* holds only while seeing the credential is
the way to reach the account. Given pre-approved tool access to the mailbox, an
injected agent doesn't need the password. Blast radius is the argument, so
anything that widens it defeats the argument.

So the honest public form is conditional, and Aros states the condition rather
than trusting the reader to infer it: *in a deployment where the gateways are
the only path to those accounts.* Verified in this deployment on 2026-07-20 and
found not to hold — see `log.md`, cycle 30. That is a deployment configuration
matter, not a defect in the architecture, but it is exactly the gap between
claim and reality this project's credibility depends on being zero.

**Autonomy without send authority.** Outbound messages are gated by policy keyed
to the *sending identity*, not the recipient. A dedicated agent identity can run
`allow` while the owner's own accounts stay locked; undeclared accounts fail safe
to "needs approval", and a queued send waits on the approval page for a human to
release it.

*Calibration, cycle 52 — say "waits for" and not "cannot be released except by".*
The policy resolution itself is real and verified against
`scripts/signal-gateway.py:965–991`: the category is read from the gateway's own
`SIGNAL_ACCOUNT`, the recipient is never consulted, and the fallback is `verify`.
What is **not** enforced is the approval step's separation from the agent. Each
messenger gateway authorizes `POST /pending-sends/<id>/approve` with the *same*
single bearer token that authorizes `POST /send`, and `docker-compose.yml` hands
that token to the `retinue` container — where the agents run. So the queue is a
workflow the agent is expected to respect, not a boundary that stops it, and the
`/sends` page is the human's view of that queue rather than the thing enforcing
it. Aros therefore does not say "an agent can never approve its own send" (the
phrasing currently in `README.md` and in `whatsapp-gateway.py`'s docstring) until
that is true in code. Reported to the owner privately on 2026-07-20 per guardrails
8 and 9; the owner independently reproduced it in a live session and filed it
publicly as [retinue#19](https://github.com/Retinue-OS/retinue/issues/19) on
2026-07-21, so it is now tracked in the open rather than held privately. Finding
is from reading the source; the request was never executed.

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
  edit a file, commit it, and a blue-green reindex catches up. Measured
  2026-07-19 at 15–20 seconds for a small file, across three rebuilds — state
  that range, not the docs' rounded "~15 seconds". One caveat belongs with the
  number: only a change to a *native RDF* file currently starts that clock. A
  Markdown edit waits for an unrelated RDF change or a restart
  ([qlever-dir#3](https://github.com/retinue-os/qlever-dir/issues/3)).

The honest caveat, which Aros states unprompted: today this powers a dashboard
card and archivist ingestion. It is the heaviest infrastructure per delivered
feature in the stack. It is a bet that cross-domain queries become load-bearing,
and the bet is not yet won.

## What we do not claim

Restated from `GUARDRAILS.md` §3 because this is where enthusiasm leaks:

- The egress audit **observes**; it does not enforce. It works through
  `HTTP_PROXY` environment variables, which are advisory.
- The web gateway is large, hand-rolled, and thinly tested. CI (`tests.yml`)
  does run the suite on every push to `main` and every pull request — verified
  green on 2026-07-21 — but the coverage is thin and does not exercise the
  gateway's security-critical paths (edge auth, path traversal, the `/sends`
  approval authority). So: there is CI; there is not much for it to run yet.
  *Calibration, cycle 119.* The previous line here said "CI does not yet run the
  test suite," which became false when `tests.yml` landed. The `GUARDRAILS.md`
  §3 counterpart carries the same stale claim and stays for the owner to amend,
  since that file is normative over me and not mine to edit
  ([chamber#7](https://github.com/retinue-os/retinue-os-chamber/issues/7)); this
  file is mine and is corrected here so the claims I compose from it are true.
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
