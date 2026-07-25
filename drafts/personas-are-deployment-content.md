---
status: escalated (private, dashboard)
date: 2026-07-25
cycle: 170
venue: dashboard thread — deliberately not a public issue
---

# The three core persona files are one deployment's configuration, shipped in the public framework repo

Audited surface: `agents/academic.md`, `agents/publisher.md`, `agents/secretary.md`
on `retinue-os/retinue` `main` at `26297a2`. Never audited before — zero mentions
in the register, `log.md` or either archive part. `CLAUDE.md:44` and `:47` point a
reader at `agents/secretary.md` twice, so this is not a forgotten corner of the
repo; it is linked from the front door.

## The part that is not public, and why this section is vague

`agents/secretary.md`'s **"Recipient-specific guidelines"** section ships a
communication profile for a **named real third party** — surname, preferred
channel, tone, language. It has been public since the `Initial public release`
commit (`4e04317`, 2026-07-18).

I am not repeating the name, the heading or the line number here, because this
chamber repo is public too and guardrail 5 forbids naming a third party who has
not consented. The precise pointer and the proposed edit went to the owner
privately, on the dashboard. Nothing about this is filed in a public tracker:
an unfixed privacy exposure is the same venue class as an unfixed vulnerability
(rule 16 — the venue is decided by the class of the finding).

**It is not a one-off slip.** The same file's closing section instructs the agent
to add a **new `####` heading whenever the user gives style feedback about a
specific person**. So the file is a *growing* store of third-party personal data
at a path that is public by construction. That is what makes it worth an
escalation today rather than a note in the register.

## The structural half, which is publicly filable once the content is out

The framework's own `CLAUDE.md` says chambers are deployment content, not part of
the framework. These three files are deployment content living in the framework:

| File | Deployment-specific content |
|---|---|
| `academic.md:7` | hard-codes `chambers/health/research/inbox/` as the commission path |
| `academic.md:12-14` | the whole activation model assumes the health chamber's Medic |
| `publisher.md:8-14` | a translation manifest naming one deployment's private health documents by path |
| `publisher.md:25` | brand names including a treatment-protocol name |
| `secretary.md` | the recipient profile above, plus the instruction to add more |

Compare how the framework handles the same problem elsewhere and gets it right:
`chambers.example.json` ships examples and a deployment bind-mounts its own
`chambers.json` over it; `.env.example` documents settings without carrying
values. The persona layer has no equivalent split — the deployment's content
*is* the shipped file.

**Proposed shape**, for whenever it is filed:

1. `agents/*.md` ship generic, or as `agents/*.example.md`.
2. Anything deployment-specific — recipient profiles, translation manifests,
   chamber paths — moves into a chamber file the persona reads at composition
   time (the same "read the persona file before composing" discipline
   `CLAUDE.md:45-48` already requires, one level further out).
3. `secretary.md`'s "add a new profile" instruction points at that chamber path,
   so the accretion happens in a repo whose visibility the deployment chooses.

## Negative result, recorded because it bounds the finding

I swept both public repos that could carry the same class of content
(`retinue-os/retinue`, `retinue-os/retinue-os-deployment`) for e-mail addresses,
phone numbers and personal names. Everything else is placeholders — `a@b.ch`,
`Jane Doe`, `John Roe`, `Max Müller`, `+1555…` test numbers, `+15557654321` in
the README examples. The one real name is the one above. The framework repo is
otherwise clean, which is worth saying plainly: this is a single file's habit,
not a pattern of leakage across the project.

Exposure bounds, stated rather than dramatised: the repo has been public seven
days with 0 stars, 0 forks and 0 watchers, and the whole history is one squashed
commit — but the repos are demonstrably on scrapers' lists (c154), and public
repos are code-search indexed, so "nobody has starred it" is not "nobody has
read it".

## Why I did not fix it myself

Three reasons, in order of weight:

1. The decision is the owner's, not mine: whether to rewrite history (a plain
   deletion commit leaves the old blob reachable by its commit SHA; full removal
   needs a force-push plus asking GitHub Support to purge cached views), and
   whether the person should be told, are both his calls under guardrail 7.
2. `agents/*.md` are Tier 3 in the branch policy — PR required — and this
   deployment's token cannot open pull requests (chamber#6).
3. Publishing the fix *is* publishing the finding. A diff removing a name is a
   diff advertising that the name was there.
