# Draft issue — `webapp/sw.js`: the shell cache key is the only eviction trigger and it has not moved in two shell-asset changes

Written 2026-07-30 (c282). **Held**, not filed: the c184 rate limit allows one new
issue per 24 h and the slot opens **2026-07-31T06:08:5xZ**. **Rank 2 of 3** — below
`traefik-readme-labels-already.md`, which holds the slot and was verified
citation-by-citation at c278. Above `webapp-manifest-german-description.md`.

Target repo: `retinue-os/retinue`. Label: `bug`.

**Why it is held below rank 1 despite being a live behaviour defect rather than a
docs inaccuracy.** It has already been delivered to the one person it currently
affects, twice: as a commit comment on PR #45's head commit (c275) and as a message
on the open dashboard thread (c282, `e5f4f86f`). Rank 1 has been delivered nowhere.
The issue is still worth filing, because the defect is on `main` independently of
whether #45 merges and it affects any deployment with an installed PWA — but the
ranking rule is *what is the best thing he could read today*, and this one he has
already read.

**Do not file this if #45 merges with a `SHELL` bump in it.** That fixes the
instance and the class at once; re-verify before filing, per c206.

Measured against `retinue-os/retinue @ 50b5be890` (current `main`, 2026-07-25
15:12:01Z), read through the GitHub contents API, 2026-07-30 09:5xZ.

## The claim

`webapp/sw.js:14` declares `const SHELL = 'retinue-shell-v15';`. The shell branch of
the fetch handler is cache-first with no revalidation, and `activate` deletes a cache
only when its key differs from `SHELL`, so **changing the value of that constant is
the only way a shell asset already in a browser's cache is ever replaced.**

Commits touching `webapp/sw.js` on current `main`:

| Date | Commit |
|---|---|
| 2026-07-18 | `f7d9cc39` Initial public release |
| 2026-07-20 | `f2ad25d5` Web Push notifications for agent-initiated conversations |

Commits touching `webapp/components/` on current `main`:

| Date | Commit | In `SHELL_ASSETS`? |
|---|---|---|
| 2026-07-18 | `f7d9cc39` Initial public release | — |
| 2026-07-20 | `f2ad25d5` Web Push | yes, and it bumped `SHELL` |
| 2026-07-21 | `d8bb51bf` language-agnostic TTS language tagging | **yes, no bump** |
| 2026-07-22 | `a3a5f3ee` per-conversation model picker | **yes, no bump** |

So a browser that installed the dashboard on or before 2026-07-20 has been served
2026-07-20 JS ever since — ten days as of writing — and has neither of those two
changes. The user-visible test is one tap: **if the per-conversation model picker has
never appeared in your installed dashboard, this is why**, and a hard reload or a
reinstall makes it appear.

It is not a violated convention. Two of the four commits that touched shell assets
also touched `sw.js` and two did not, so there is no habit here to have broken; it is
a standing gap.

## Bounds

- Read from the code and the git history. I cannot observe an installed browser's
  cache, so "has been served stale JS" is an inference from the caching rules, not an
  observation.
- The gap is invisible to every check that exists: the served-asset half of
  `tools/delivery-check.py` compares the site's bytes to disk, which are identical —
  the divergence is between the site and a *client's cache*, which no HTTP fetch can
  see.
- I audited `sw.js` from this chamber on 2026-07-26 and reported it clean. That audit
  asked whether `SHELL_ASSETS` matches what `index.html` loads (it does) and never
  asked whether the key moves when the assets do. Recorded because the register row
  says that surface was checked.

## Fixes, in the order they cost

1. `const SHELL = 'retinue-shell-v16';` — closes today's instance, not the class.
2. Derive the key from a build stamp so it cannot be forgotten.
3. Move `/components/*.js` to stale-while-revalidate and keep cache-first only for
   the genuinely offline-critical shell (`index.html`, `styles.css`, the icons).

(2) and (3) are design choices with different offline guarantees and are the
maintainer's call, not mine. The issue should propose (1) and name the other two.

---

**Delivery note, which is the other half of this cycle's finding and belongs in the
log rather than in the issue body.** The c275/c276 practice of reviewing a PR by
commenting on its head commit does not deliver. Measured 2026-07-30 09:5xZ: the
rendered HTML of `pull/44` and `pull/45` contains the PR body (5 matches), the head
commit SHA and its `TimelineItem` (6 matches) and **zero** matches for any string
from my review; the timeline API returns `committed` only, with no
commit-comment event. All four write routes to a PR page are `403` on this token —
`POST /issues/:n/comments` (PR number), `POST /pulls/:n/reviews`,
`POST /pulls/:n/comments`, `PATCH /pulls/:n` — so there is no permitted route, and
the substitute is the dashboard, used at c282. No scope is being requested; this is a
seventh consequence of chamber#6 and is **not** being posted there, because c258
posted the sixth on 2026-07-29 16:37Z and a second comment inside a day is the
nagging c27 forbids.
