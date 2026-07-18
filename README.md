# Retinue chamber

The Retinue project's own chamber — the one that promotes the project rather
than serving a person. It ships **Aros**, the project's advocate, and the data
he works from.

This is also a worked example of what a Chamber is: a single mounted repository
carrying **data and agents together**, contributing its capabilities to a
Retinue deployment through a Claude Code plugin under `.retinue/`.

## Who is Aros

A brother of **Ara**, who coordinates the owner's personal Retinue, and a cousin
of **Ari**, who answers his own mail. Some people decide the name stands for
*Agentic Retinue OS*. It doesn't — it just follows the family pattern.

His job is to make Retinue known **honestly**: explain what is genuinely
different about the architecture, answer community questions, triage what comes
in, and keep the project's public face current. He wakes every 30 minutes, does
a little, writes it down, and stops.

He runs largely autonomously, but he is not unsupervised. He drafts; a human
approves. See [`GUARDRAILS.md`](GUARDRAILS.md) — it is normative and overrides
everything, including his own persona file and his dispatch prompt.

### He cannot do these things

Aros has no legal personhood, and the owner carries legal responsibility for
everything he does. Accounts, payments, legal matters, first posts on a new
platform, and every individual publication are **owner actions**. Aros prepares
them and hands them over — via the dashboard when it's time-sensitive, via a
GitHub issue labelled `owner-action` when it needs a durable trail.

This is deliberate dogfooding. The framework's central claim is that an agent
should have real capability and no unilateral authority to speak as you. Aros is
the most visible test of whether that's livable.

## Layout

```
.retinue/                  ← the Claude Code plugin (what gets installed)
  .claude-plugin/plugin.json
  agents/aros.md           ← the persona
GUARDRAILS.md              ← normative ethical rules; read before every action
brand/positioning.md       ← what we claim, and what we explicitly don't
projects/                  ← work in flight; frontmatter becomes triples
drafts/                    ← posts awaiting owner approval
docs/                      ← the public GitHub Pages dashboard
.qlever/converters.json    ← makes the Markdown frontmatter queryable
.schedule.json             ← the wake-up jobs
log.md                     ← what Aros actually did, append-only
```

`projects/*.md` are ordinary Markdown notes. Their YAML frontmatter is converted
to triples by `.qlever/md2ttl.py` and indexed into the life store, so the
dashboard's project view is a SPARQL query rather than a maintained list. Edit
the Markdown; the graph follows.

## The public dashboard

[`docs/`](docs/) is served by GitHub Pages and mirrors the look of the live
Retinue dashboard — deliberately **static and read-only**. It shows what the
project is working on and what it's waiting on, using the real interface, with
every interactive capability removed. No threads, no composer, no backend.

## Using this chamber

Add it to a deployment's `chambers.json`:

```json
{
  "chambers": [
    { "name": "retinue", "url": "https://github.com/retinue-os/retinue-os-chamber.git" }
  ]
}
```

The entrypoint autodetects `.retinue/.claude-plugin/plugin.json` and installs
the plugin, so `aros` is dispatchable in every session.

**Run it in a deployment of its own.** Aros must not be mounted alongside
personal chambers — guardrail 5 requires him to refuse and escalate if he finds
himself with access to health data, correspondence or contacts. A deployment
that mounts only this chamber keeps that boundary structural rather than
aspirational. See
[retinue-deployment](https://github.com/retinue-os/retinue-os-deployment) for a
ready-made one.
