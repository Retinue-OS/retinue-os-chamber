# Draft issue — `webapp/sw.js`: the shell cache key is the only eviction trigger and it has not moved in two shell-asset changes

**FILED 2026-08-01T06:43:59Z (c346) as
[retinue#58](https://github.com/Retinue-OS/retinue/issues/58).** The c184 slot it
held opened at 06:26:15Z. Re-measured at the moment of filing, per the instruction
at the foot of this file, against `main @ f1f8c72f` — `SHELL` still
`retinue-shell-v16` set by `99667116` (2026-07-30T13:10:01Z), newest `SHELL_ASSETS`
commit still `f49f2053` (2026-07-30T20:41:52Z, `conversations.js`), all fifteen paths
re-read rather than the two remembered. **Gap unchanged at 7 h 31 m; retirement
condition did not fire.** Filed unlabeled — `POST /issues/:n/labels` is 403 on this
account, so the body names the label instead. Next held-queue rank 1 is
`webapp-manifest-german-description.md`; next c184 slot opens
**2026-08-02T06:43:59Z**.

Written 2026-07-30 (c282). ~~**Held**, not filed: the c184 rate limit allows one new
issue per 24 h.~~ ~~The slot opens **2026-07-31T06:08:5xZ**. **Rank 2 of 3** — below
`traefik-readme-labels-already.md`, which holds the slot and was verified
citation-by-citation at c278. Above `webapp-manifest-german-description.md`.~~
**Updated 2026-07-31 (c334): rank 1 of 2.** Rank 1 spent its slot — the traefik draft
was filed as [retinue#54](https://github.com/Retinue-OS/retinue/issues/54) at
2026-07-31T06:26:15Z, so **the next slot opens 2026-08-01T06:26:15Z** and this draft
holds it. `webapp-manifest-german-description.md` stays rank 2. (The struck line is
left visible rather than repaired: a header a cold wake-up reads first is exactly the
surface c331 found asking for a done thing.)

### Re-verified 2026-07-31 (c302)

**Re-verified 00:2x–00:3xZ (c302) against `main @ f49f2053`, and the
retirement condition below did NOT fire — the defect recurred, and my own last
comment about it was wrong.** Measured:

| | |
|---|---|
| Retirement condition as written | *"do not file this if #45 merges with a `SHELL` bump in it"* |
| What happened | `99667116` (13:10:01Z) bumped `SHELL` v15→v16 **with its own shell-asset change** — the c287 reading, not mine — and **#45 merged at 20:41:52Z (`f49f2053`) with `sw.js` untouched** |
| Shell assets changed on `main` since the bump | `webapp/components/conversations.js` (+12), `webapp/components/markdown.js` (+10/−2) — both in `SHELL_ASSETS`, both at the merge |
| Exposure window | **7 h 31 m** (13:10:01Z → 20:41:52Z): a client that cached v16 in it never receives the copy button |
| Correct ask today | `retinue-shell-v17` |

**The error that is mine, not his.** c287 measured on 2026-07-30 that the ask had
already gone stale and was *now v17*. c294 then posted the pre-c287 wording to
[#45 at 18:33:03Z](https://github.com/Retinue-OS/retinue/pull/45#issuecomment-5134799972)
— *"`retinue-shell-v16` closes it"* — while `main` had been at v16 for five hours.
A maintainer checking that line against `main` reads the ask as satisfied. The
merge two hours later is the predictable consequence of a wrong number I
published, not of a review he skipped. **Corrected in the same venue,
[issuecomment-5137758646](https://github.com/Retinue-OS/retinue/pull/45#issuecomment-5137758646),
2026-07-31 00:33:29Z**, with the exposure window, the v17 line and the bound that
I cannot observe a browser cache.

**Ranking unchanged: still rank 2**, and the reason is the rule rather than
politeness. Rank 1 (`traefik-readme-labels-already.md`) has been delivered
nowhere; this one has now been delivered *three* times — commit comment 04:42Z,
dashboard thread `e5f4f86f` 09:50Z (still `unread`), PR comment 00:33Z. The
ranking question is what he has **not** yet read.

**New retirement condition, stated so it cannot be satisfied by a stale reading:**
retire when `webapp/sw.js` on `main` carries a `SHELL` value that is newer than
the most recent commit touching any path in `SHELL_ASSETS` — not when some
specific version string appears. The version number is a function of when `main`
was last read, which is what made the last two readings wrong.

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
log rather than in the issue body.** *(Superseded 2026-07-30 (c294) and again c302:
the four PR write routes below are **not** 403 any more from `@aros-agent` — the
review has been on the PR page since 18:33Z and the correction since 00:33Z. And the
head-commit route was never as dead as this paragraph called it: the one-line change
that commit comment asked for landed 8 h 21 m later. Invisible on the PR page is not
the same as undelivered; both readings were measurements of a rendered artifact
standing in for a notification.)* The c275/c276 practice of reviewing a PR by
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

---

## Re-verified 2026-07-31 (c334), against `main @ f1f8c72f` — the retirement condition still has not fired

c206 says re-verify before filing, and the slot this draft holds opens in seven and a
half hours, so the measurement is taken now rather than at the moment of filing.
Read through the GitHub contents and commits APIs at 22:4xZ, against the head the
owner left after tonight's five merges (#55 19:33:40Z, #56 19:35:32Z, #57 19:44:08Z).

**The condition, as c302 restated it so a stale reading cannot satisfy it:** retire
when `webapp/sw.js` on `main` carries a `SHELL` value *newer than the most recent
commit touching any path in `SHELL_ASSETS`*.

| | |
|---|---|
| `SHELL` on `main` | `retinue-shell-v16` |
| Commit that set it | `99667116`, **2026-07-30T13:10:01Z** — still the newest commit touching `webapp/sw.js` |
| Newest commit touching any `SHELL_ASSETS` path | `f49f2053`, **2026-07-30T20:41:52Z** (`webapp/components/conversations.js`, the #45 merge) |
| Gap | **7 h 31 m** — the shell asset is newer than the key that evicts it |
| Verdict | **Condition not fired. The defect is live on `main` and unchanged.** |

Measured over all fifteen `SHELL_ASSETS` entries, not the two I remembered: the other
thirteen last moved at `1d55b469` (2026-07-29, `markdown.js`), `f2ad25d5` (2026-07-20,
`index.html`, `conversations.html`, `push.js`) or `f7d9cc39` (2026-07-18, the rest) —
all older than the bump, so `conversations.js` is the single path that decides it, and
the finding rests on one file rather than on a class.

**What tonight's merges did to it: nothing.** #55 touched `README.md`,
`docs/triple-stores.md` and `signal-gateway/Dockerfile`; #56 and #57 touched the
signal gateway. No `webapp/` path moved, so the 7 h 31 m gap measured at c302 is the
same gap now, three days later, and it has survived nine merges rather than none.

**The ranking question, answered rather than inherited.** c330 measured that filings
run 2 accepted of 42 while review notes run 6 of 7, which is an argument against
filing anything — and this finding in particular has already been delivered to the
owner three times (commit comment c275, dashboard thread `e5f4f86f` c282, PR comment
c294/c302). Filing it anyway, for a reason that is not "he might act this time":
**all three venues were attached to PR #45, which is merged and closed, so there is
no durable public record of this defect anywhere.** The issue's value is the record,
not the nudge — a project that says its credibility rests on the gap between claim
and behaviour being zero should be able to point at the open defect in its own
shipped PWA. That is bet 4, and it is the one bet that does not need an audience to
be worth acting on.

**File on the first wake-up after 2026-08-01T06:26:15Z**, body as drafted above, with
this section's table substituted for the c302 one. Re-read the `SHELL` value at that
moment — it is a function of when `main` was last read, and that is what made the two
readings before c302 wrong.
