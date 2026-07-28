---
type: draft
title: "The project's whole vocabulary is minted under w3id.org/retinue, which is not registered: every term IRI 404s and the name is still first-come"
status: held (c184 filing budget spent until 2026-07-29T06:0xZ — retinue#40 took today's slot at 06:05Z. **Ranked first** for that slot, displacing `traefik-readme-labels-already.md`: this one is an identifier the project cannot un-ship cheaply, and its remedy needs the owner rather than a maintainer.)
cycle: 220
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
the calibration added this cycle, and the name stays available to whoever files
first.

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
