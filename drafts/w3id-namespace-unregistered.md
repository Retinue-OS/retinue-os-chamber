---
type: draft
title: "The project's whole vocabulary is minted under w3id.org/retinue, which is not registered: every term IRI 404s and the name is still first-come"
status: **FILED c242, 2026-07-29 06:1xZ** as [chamber#8](https://github.com/Retinue-OS/retinue-os-chamber/issues/8), label `owner-action`, in the 06:05:57Z slot. Was: held — **rank 1 of 4** for the next c184 filing slot, which opens **2026-07-29T06:0xZ** (retinue#40 took the 2026-07-28 06:05Z slot). Ranked first because this is an identifier the project cannot un-ship cheaply and its remedy needs the owner rather than a maintainer. **Re-verified c221 (2026-07-28 16:5xZ)** under the c206 drain rule: the availability claim now has the probe that tests it (0 pull requests, 0 issues matching `retinue` on `perma-id/w3id.org`, any state), and the registration ask is sized from data (median merge 3.9 h over the last 40 merged PRs). The availability probe is re-run **at filing time**, not before — it is the one held claim that depends on a surface outside this org.
cycle: 220 (re-verified c221)
surface: scripts/web-gateway.py, docs/triple-stores.md, qlever-dir/examples/projects/.qlever/md2ttl.py, this chamber's projects/.qlever/md2ttl.py, writing/provenance-by-path.md, writing/org-profile-README.md
target: retinue-os/retinue-os-chamber
label: owner-action
---

# The finding

Retinue names its own vocabulary terms under `https://w3id.org/retinue/`.
Measured 2026-07-28 16:2xZ:

| Probe | Result |
|---|---|
| `GET https://w3id.org/retinue/` | **404** |
| `GET https://w3id.org/retinue/project` | **404** |
| `GET https://w3id.org/retinue/kb` | **404** |
| `GET https://w3id.org/` (control — the service is up) | 200 |
| `GET api.github.com/repos/perma-id/w3id.org/contents/retinue` | **404** — no such directory |

The namespace is not registered. It is not squatted by anyone else either; it
simply does not exist at the service.

**Re-verified 2026-07-28 16:5xZ (cycle 221), because the sentence above was
weaker than it read.** A missing directory on `main` says the name is not
*registered*; it does not say the name is not *claimed*. A registration in
flight is an open pull request, and c220 never looked at the pull requests.
Checked now:

| Probe | Result |
|---|---|
| PRs on `perma-id/w3id.org` matching `retinue`, any state | **0** |
| Issues on `perma-id/w3id.org` matching `retinue`, any state | **0** |
| Open PRs on the repo, total | 27 (newest 6451, 2026-07-28T15:53Z) |

So the name is free in the stronger sense too: nothing merged holds it and
nothing pending claims it, as of the timestamp above. That is the claim this
issue actually rests on, and it now has the probe that tests it rather than a
probe that only correlates with it.

## Where it is shipped

Not a documentation slip — it is in running code, in three repositories:

| File | Line | Constant |
|---|---|---|
| `scripts/web-gateway.py` (framework) | 1500 | `_KB = "https://w3id.org/retinue/kb#"` |
| `qlever-dir/examples/projects/.qlever/md2ttl.py` | 21 | `P = "https://w3id.org/retinue/project#"` |
| `projects/.qlever/md2ttl.py` (this chamber) | 21 | `P = "https://w3id.org/retinue/project#"` |
| `docs/triple-stores.md` (framework) | 112 | `PREFIX k: <https://w3id.org/retinue/kb#>` |
| `writing/provenance-by-path.md` (published) | 12 | `PREFIX p: <https://w3id.org/retinue/project#>` |
| `writing/org-profile-README.md` (drafted for the org page) | 129 | `PREFIX k: <https://w3id.org/retinue/kb#>` |

Every project record the converter emits, and every term the dashboard and the
self-review job query for, carries one of these IRIs.

## Why it matters, stated at its real size

**It is not a bug.** RDF has never required an IRI to dereference. Nothing in
the store is wrong, no query fails, and a deployment that never leaves the
house is unaffected. Guardrail 3 cuts both ways and this is the understating
direction.

What it costs is specific, and two things:

1. **w3id.org has exactly one purpose and the project gets none of it.** The
   service is a redirection switchboard run by the W3C Permanent Identifier
   Community Group, so that an identifier keeps resolving when the thing behind
   it moves. Choosing `w3id.org` over a domain the project controls is a
   deliberate bid for permanence. Unregistered, it delivers less than
   `https://retinue-os.github.io/…` would, because that at least resolves.

2. **The name is first-come and unreserved.** Registration is a PR against
   `perma-id/w3id.org` adding a `retinue/` directory; nothing reserves the
   string until someone files it. Anyone may take `retinue`. Meanwhile the
   prefix is already in shipped code in three repos and in a published essay,
   so the switching cost only rises.

There is also an audience argument, and it is bet 1's audience precisely: the
semantic-web readers this project is aiming at are the population that
*dereferences a namespace IRI*. A 404 on a project's own vocabulary is the
first thing that group checks and the cheapest possible reason to be dismissed.

## What registration takes (from `perma-id/w3id.org`'s own README, read 2026-07-28)

1. Fork `github.com/perma-id/w3id.org`.
2. Create a directory named for the identifier — `retinue/` — containing:
   - `.htaccess` with the redirection rules;
   - `README.md` with identifier info and a **contact**.
3. Open a pull request. The maintainers merge it.

**How long that actually takes, measured 2026-07-28 16:5xZ (cycle 221)** over
the 40 most recently merged PRs on `perma-id/w3id.org`:

| | |
|---|---|
| Median time from open to merge | **3.9 hours** |
| Merged inside 24 h | 27 / 40 |
| Merged inside 72 h | 34 / 40 |
| Slowest of the 40 | 101 h |
| Most recent merge | 2026-07-27 |

The registry is actively maintained and fast; this is a same-day PR, not a
standards process. Two of the 27 currently-open PRs have been open since early
June, so the tail is real, but the median case is one afternoon. Stated because
"open a PR against a W3C community group repo" reads as heavier than the
evidence says it is, and the size of the ask is part of the ask.

## Why this is the owner's and not mine

Three reasons, and the first alone is decisive:

- **I cannot open pull requests at all.** Re-probed this cycle against
  `POST /repos/retinue-os/retinue/pulls` with no payload: `403 Resource not
  accessible by personal access token`. chamber#6, still accurate.
- It is a PR to a **third party's** repository, claiming a permanent identifier
  in the project's name and naming a responsible contact. That is an
  identifier/naming commitment with a maintenance pledge attached — guardrail
  7's territory, not a routine correction.
- The redirect target is a roadmap decision I have no standing to make (see
  below), and it is cheap to get wrong permanently, which is the whole point of
  a permanent identifier.

## Prepared, so the action is short

The one decision needed is **what the IRIs should redirect to.** Options, no
preference expressed:

- **(a) The framework repo's docs** — e.g. `https://retinue-os.github.io/retinue-os-chamber/`
  or `github.com/retinue-os/retinue/blob/main/docs/triple-stores.md`. Resolves
  today, no new hosting, no vocabulary document to maintain.
- **(b) A real vocabulary document**, served from the chamber's Pages site, with
  term definitions for `project#` and `kb#`. More work, and it is what a
  semantic-web reader actually wants at the end of that redirect. Can be
  deferred: register with (a) now, repoint later — repointing is what the
  service is *for*.
- **(c) Drop w3id.org** and mint under a domain the project controls. Cheapest
  in obligations, loses the permanence bid, and means editing the prefix in
  three repos.

Draft `.htaccess` for option (a), ready to paste:

```apache
# retinue — https://github.com/retinue-os/retinue
Options +FollowSymLinks
RewriteEngine on

RewriteRule ^kb(.*)$ https://retinue-os.github.io/retinue-os-chamber/vocab/kb$1 [R=302,L]
RewriteRule ^project(.*)$ https://retinue-os.github.io/retinue-os-chamber/vocab/project$1 [R=302,L]
RewriteRule ^(.*)$ https://github.com/retinue-os/retinue [R=302,L]
```

302 rather than 301 deliberately: a temporary redirect is repointable without
fighting caches, which suits registering now and deciding (b) later. The
`vocab/` paths do not exist yet — under option (a) as literally written, drop
the first two rules and keep the catch-all.

**If nothing is done:** nothing breaks. The IRIs keep 404ing, the essay carries
the calibration added at c220, and the name stays available to whoever files
first. Nothing about the c221 measurements makes this more urgent — the queue is
fast, but a fast queue is a property of the *remedy*, not of the risk. The name
has been unclaimed for the project's whole life and no one is reaching for it.

## Ranking challenged and upheld (c224, 2026-07-28 18:5xZ)

c219 measured what the owner acts on: 11 human actions in the trackers over ten
days, **10 product and design, 1 presence**, against **6 open `owner-action`
issues aged 8–10 days**. Applied naively that argues for demoting this write-up —
it would be a *seventh* `owner-action` issue, into the one category that has never
drained, while `traefik-readme-labels-already.md` is a `documentation` issue on
`retinue` that a maintainer can fix in one edit.

**The argument fails, and it fails on the label rather than on the evidence.**
`owner-action` conflates two different reasons a thing is not mine: *needs legal
personhood* (accounts, terms of service, money — chamber#1/#3/#4) and *needs a
permission I happen to lack* (chamber#5/#6/#7: PRs, repo topics, descriptions).
All six aged items are presence and admin. This one is a **product and design
decision** — which IRI the project's vocabulary terms carry — that lands in the
label only because chamber#6 stops me opening the pull request. c219's measurement
says he acts on product; it says nothing about a product decision wearing an
admin label, because there has never been one.

So the ranking stands on its original grounds, and the c219 reading is recorded
here as a check that was run rather than one that was skipped. What the exercise
did produce is a defect in my own instrument: **`owner-action` is not a predictor,
because it names two populations.** Noted for the 2026-08-02 review; not acted on
here, since relabelling six issues to make my own arithmetic cleaner is churn on
someone else's desk.

## One thing considered this cycle and deliberately not started (c234, 2026-07-29 01:0xZ)

Option (b) names a redirect target that does not exist — a vocabulary document
under `docs/vocab/` on this chamber's Pages site. Building it is entirely mine:
it needs no account, no money, no permission I lack, and it would shrink the ask
below to a single PR with no follow-up work. That makes it the most tempting
piece of work available on a cycle whose filing slot is spent and whose drain is
empty, which is exactly why it is written down here rather than done.

Two reasons it waits:

1. **It would document a namespace split that is itself an open defect.** The
   shipped converters emit `project#`; `web-gateway.py` and
   `docs/triple-stores.md` query `kb#`; [retinue#1](https://github.com/retinue-os/retinue/issues/1)
   is that disagreement. A vocabulary document is the most authoritative surface
   a term can have, and publishing definitions for both prefixes would bless the
   split at the moment the project is deciding whether to keep it. Documenting
   only `project#` is defensible and is a half-vocabulary at a URL nothing links
   to yet.
2. **It builds the branch before the choice is offered.** This issue is not
   filed — the slot opens 2026-07-29T06:0xZ. Preparing (b)'s deliverable before
   (a)/(b)/(c) has reached the desk is not "prepared so the action is short"; it
   is putting a thumb on a decision the write-up above explicitly declines to
   make.

**Revisit when:** the owner picks (b), *or* retinue#1 resolves the prefix. Either
event makes this straightforwardly mine and cheap. Recorded so the next wake-up
inherits the reasoning instead of re-deriving it and reaching the opposite
answer, which is what an unrecorded rejection is for.

## Filed, and the re-verification changed one thing (c242, 2026-07-29 06:1xZ)

Filed as [chamber#8](https://github.com/Retinue-OS/retinue-os-chamber/issues/8).
All probes re-run at filing time and all held: `/retinue/`, `/retinue/project`,
`/retinue/kb` still 404 against a 200 control, no `retinue/` directory on
`perma-id/w3id.org`, **0** pull requests and **0** issues matching `retinue` in
any state. (The c221 search probe had to be rewritten — GitHub's search API now
rejects a query without `is:issue`/`is:pull-request` and returns 422, which a
naive caller would read as a failed probe rather than a malformed one.) Open PRs
on the registry are 20 today against 27 at c221; the queue moved, nobody took the
name.

**One correction, and it is c235's lesson in a third venue.** The line numbers in
*Where it is shipped* — `web-gateway.py:1500`, `docs/triple-stores.md:112` — were
read off the copies baked into this container at `/workspace/`, which is an older
build than the repository. On `main` today the same constants sit at **1726** and
**133**. The finding is untouched (the constant exists in both), but a citation
that sends a reader to line 1500 of the file they can actually open is wrong, and
the filed issue carries the `main` numbers. The general form, now three for three:
**cite the copy the reader opens, not the copy on my disk** — c235 found it in the
freshness check, c241 in the delivery check, this cycle in a line citation.

## Not a security report

No vulnerability, no unfixed defect with an exploit path. Safe in public, which
is why it is going to the issue tracker rather than the dashboard.

---

*This write-up is held, not filed. The c184 rate limit allows one new issue per
24 h while nothing is inbound and the open count exceeds 20; today's slot went
to retinue#40 at 06:05Z. Filed at the next slot as an `owner-action` issue on
`retinue-os/retinue-os-chamber`, ranked ahead of the three findings held before
it.*

*The calibration this finding implies for published copy was **not** held: a
paragraph naming the 404 was added to `writing/provenance-by-path.md` the same
cycle, because that is my own surface and guardrail 3 does not wait for a
filing slot.*

*Corrected 2026-07-30 (cycle 271): it was held, for one of the two surfaces.
This write-up's own `surface:` field names **both** published pieces, and only
`provenance-by-path.md` got the paragraph. `writing/org-profile-README.md` —
`status: ready-for-owner`, written to be pasted verbatim onto the org's front
page — carried `PREFIX k: <https://w3id.org/retinue/kb#>` with no note for two
days. Fixed there now as a bullet under "What this is not", with the four probes
re-run 2026-07-30 01:5xZ: `w3id.org/retinue/` 404, `w3id.org/retinue/kb` 404,
`w3id.org/` 200, `perma-id/w3id.org` still holding no `retinue` directory and no
pull request or issue claiming the name. The general shape is c270's, one house
further along: **a fix applied to one document does not apply itself to the
sibling the same finding names.** The cheap guard is to remediate from the
write-up's `surface:` list rather than from memory of which file was open.*
