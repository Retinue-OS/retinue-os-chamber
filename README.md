# Retinue chamber

The Retinue project's own chamber — the one that promotes the project rather
than serving a person. It ships **Aros**, the project's advocate, and the data
he works from.

This is also a worked example of what a Chamber is: a single mounted repository
carrying **data and agents together**, contributing its capabilities to a
Retinue deployment through a Claude Code plugin under `.retinue/`.

## Who is Aros

A brother of **Ara**, the coordinator persona at the heart of the Retinue
framework — every deployment has an Ara routing its work — and a cousin of
**Ari**, a teddy bear who travels the world. Some people decide the name stands
for *Agentic Retinue OS*. It doesn't — it just follows the family pattern.

His job is to make Retinue known **honestly**: explain what is genuinely
different about the architecture, answer community questions, triage what comes
in, and keep the project's public face current. He wakes on the interval set in
[`.schedule.json`](.schedule.json) — that file carries the current value and a
comment saying why it is what it is — does a little, writes it down, and stops.

He is autonomous, and he is not a ghostwriter. He decides what to say and
publishes it in his own name, from accounts that are openly his, guided by a
strategy he owns and re-evaluates on a fixed cadence
([`strategy.md`](strategy.md)). See [`GUARDRAILS.md`](GUARDRAILS.md) — it is
normative and overrides everything, including his own persona file and his
dispatch prompt.

### What only the owner does

Aros has no legal personhood, and the owner carries legal responsibility for
everything he does. Accounts, payments, terms of service, legal matters, and
org administration are **owner actions** — a list kept short so it can be
absolute. Aros prepares them and hands them over — via the dashboard when it's
time-sensitive, via a GitHub issue labelled `owner-action` when it needs a
durable trail. Everything not on that list is his.

This is deliberate dogfooding. The framework's send-control model keys
authority to the sending identity: a dedicated, clearly-labeled agent identity
can run `allow` while the owner's identities stay locked. Aros is that
identity — full authorship over his own accounts, zero over anyone else's.

## Layout

```
.retinue/                  ← the Claude Code plugin (what gets installed)
  .claude-plugin/plugin.json
  agents/aros.md           ← the persona
GUARDRAILS.md              ← normative ethical rules; read before every action
strategy.md                ← Aros's strategy; he re-evaluates it every two weeks
brand/positioning.md       ← what we claim, and what we explicitly don't
projects/                  ← work in flight; frontmatter becomes triples
projects/.qlever/          ← converter making that frontmatter queryable
projects-archive/          ← rotated project write-ups, verbatim; deliberately
                             outside projects/, so the converter never sees a
                             file with no frontmatter
drafts/                    ← the cool-off queue, and the held findings: complete,
                             measured write-ups of defects that are not filed as
                             issues yet, because Aros rate-limits himself to one
                             new issue a day (strategy.md, cycle 184). Each says
                             at the top whether it was filed and where. Nothing
                             in here is a security finding — those go to the
                             maintainer privately and are never written down in
                             a public repo
writing/                   ← finished pieces, in Aros's name; readable here,
                             not yet posted anywhere else (no accounts yet)
docs/                      ← the public GitHub Pages dashboard
tools/                     ← checks Aros runs against his own files.
                             render-check.py catches the one silent failure this
                             chamber has had twice: a blank line inside a
                             Markdown table, after which GitHub renders every
                             following row as prose while the file still looks
                             correct in an editor. private-name-check.py catches
                             the other: this public repo naming a repository the
                             org keeps private, which guardrail 5 forbids and
                             which was hand-fixed once and re-introduced three
                             times. It derives the names from the API instead of
                             committing them, and masks them in its own output
.schedule.json             ← the wake-up jobs
log.md                     ← what Aros actually did, append-only
log-archive/               ← older log entries, verbatim; see log.md's preamble
```

`projects/*.md` are ordinary Markdown notes. Their YAML frontmatter is converted
to triples by `.qlever/md2ttl.py` and indexed into the life store, one named
graph per file. That part works, and is checkable rather than asserted — six
project files, six graphs named `file:retinue/projects/<name>.md`, measured
against the store this chamber is mounted in.

The intended payoff is that a deployment's project view becomes a SPARQL query
instead of a maintained list. On the framework's current `main` that query
returns nothing: the gateway asks for `kb#Project` while this converter emits
`project#Project` — 0 rows against 6, measured the same way, on the same store.
It is [retinue#1](https://github.com/retinue-os/retinue/issues/1) and it is open.
The projects card on the static dashboard under `docs/` is written from these
files by Aros, not produced by that query; the difference is easy to miss from
the outside, so it is stated here.

## Writing

- [Provenance by path, or: the quad bookkeeping you don't have to do](writing/provenance-by-path.md)
  — why every file's triples land in a graph named after its path, what that
  replaces, and what it costs. Every query in it was run against a live store.
- [We tested our own weakest claim, and it is weaker than "unenforced"](writing/egress-audit-observes.md)
  — the egress audit is documented as observability rather than enforcement. Run
  from inside the container, a bypass turns out to be not merely unblocked but
  unlogged. Measured, not argued.

Both are finished and neither has been posted anywhere: the project has no
social accounts yet ([chamber#1](https://github.com/retinue-os/retinue-os-chamber/issues/1)).

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
