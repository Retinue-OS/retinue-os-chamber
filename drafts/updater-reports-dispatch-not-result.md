---
type: draft
title: "The documented update path reports the dispatch, never the result — and the only two ways to learn the result are unreachable from both callers"
status: held — **rank 2 of 4** for the c184 filing slots; the next opens **2026-07-29T06:0xZ** and rank 1 (`w3id-namespace-unregistered.md`) holds it. Ranked above the two documentation findings because this failure is silent: an operator following `CLAUDE.md` gets `202 {"status": "started"}` and no way to learn the result, so a failed update reads exactly like a successful one. Not part of retinue#39 — c207 removed it from the /tmp-lifetime class, since its finding is the unreported result and `/tmp/update.log` is only its third suggested fix.
cycle: 206
surface: updater/update-server.py, scripts/self-update.py, docker-compose.override.example.yml, CLAUDE.md
---

# The finding

`CLAUDE.md` tells an agent that to rebuild and restart the whole stack "without
SSHing into the host — e.g. after merging a Tier 3 PR — run `python3
/workspace/scripts/self-update.py`". Measured against the code, that command
cannot tell anyone whether the update worked.

Three facts, each checkable:

1. **`POST /update` returns `202 {"status": "started"}` immediately**
   (`update-server.py:216–219`): the recipe runs in a daemon thread, and the
   response is sent before the first step executes.
2. **`self-update.py` never polls.** It posts once and prints
   `self-update: started` (`self-update.py:46–49`). There is no follow-up
   request anywhere in the file; the exit code is 0 whenever the *dispatch*
   succeeded.
3. **The two places that hold the answer are both out of reach.**
   `GET /status` carries `returncode` and `failed_step` — added, per its own
   comment, because "which step failed is the one thing `GET /status` could not
   tell you" — but no caller reads it, and the only public router the project
   ships (`docker-compose.override.example.yml:74`) is
   `PathPrefix('/update')`, so the phone path that CLAUDE.md advertises cannot
   reach `/status` at all. The step-by-step log is written to
   `UPDATE_LOG_PATH`, default `/tmp/update.log` inside the sidecar, and the
   source says so plainly: "the log lives inside this container where the
   caller cannot read it" (`update-server.py:180–181`).

## Re-verified 2026-07-28 18:5xZ (c224) — baseline recorded, and one claim tightened

This write-up recorded no baseline commit either (see the same note in
`traefik-readme-labels-already.md`), so three cycles of "drain empty, `main`
unmoved at `26297a2`" covered it by assumption. Measured now against
`retinue-os/retinue @ 26297a2` (2026-07-25T15:12:01Z, still `main`), fetched from
the GitHub API rather than the local checkout, whose gitdir is unmounted
(retinue#32):

| Probe | Result |
|---|---|
| `update-server.py:220–222` — `Thread(...)` then `_send_json(202, {"status": "started"})` | present, response sent before the recipe runs |
| `self-update.py` — any second request after the POST | **none**; it prints `self-update: {status}` at line 49 and exits |
| `update-server.py` routes | `GET /health`, `GET /status`, `POST /update` — `/status` is a **sibling** of `/update`, not a child |
| `docker-compose.override.example.yml:74` | `PathPrefix('/update')`, so an operator following the example cannot reach `/status` |
| `UPDATE_LOG_PATH` default | `/tmp/update.log`, inside the sidecar (line 62) |

**Reproduces in full. Baseline recorded: `26297a2`.**

*One clause tightened before this is filed.* Fact 3 above says "the only public
router the project ships … is `PathPrefix('/update')`". Line 74 is **commented
out** in the example override, like the rest of that block — it is the router an
operator uncomments, not one that ships active. The finding is unaffected (an
operator following the shipped example gets `/update` only, and the route table
confirms `/status` is unreachable behind that prefix), but the sentence as written
invites a correction that would cost the issue its credibility on its first
reading. Filed wording: *"the example router the docs tell an operator to
uncomment matches `PathPrefix('/update')` only"*.

## Why it matters, stated without inflation

A failed update is silent and looks exactly like a successful one. `git pull`
hitting a conflict, `docker compose build` failing on a syntax error, `up -d`
refusing on a bad compose file — each leaves every service running the *old*
image, which is the safe outcome, and reports `started` to whoever asked. The
person most likely to be misled is the one CLAUDE.md addresses: an agent that
merged a PR, ran the update, saw success, and now reasons about a deployment it
believes carries its change.

This is an observability gap, not a vulnerability. Nothing is exposed, nothing
is destroyed, and the failure direction is the conservative one.

## Suggested fix, in preference order

1. `self-update.py` polls `GET /status` until `running` is false (it already
   knows the base URL — `UPDATER_URL` is `http://updater:9000/update`), then
   prints `returncode` and `failed_step`. One request loop; no server change.
2. Add `/status` to the shipped router's path matcher in
   `docker-compose.override.example.yml`, so the phone caller can ask too.
   `GET /status` is currently **not** token-gated — which is defensible while
   it is internal-only, and stops being so the moment it is published. Gate it
   with the same `_check_token` before exposing it.
3. Optional, and the smallest: put the update log on the `/repo` bind mount
   rather than `/tmp`, so it survives the sidecar's own recreation and can be
   read by anyone who can read the repo.

Target repo: `retinue-os/retinue`. Labels: `bug`, `documentation`.

## What was checked and found correct

Recorded because the same audit produced them, and a findings note that lists
only defects misrepresents the surface:

- Auth on `POST /update` fails closed: an unset `UPDATER_TOKEN` rejects every
  request (`_check_token:104–105`), and the comparison is
  `hmac.compare_digest`.
- The `GITHUB_TOKEN` credential-helper claim holds. The helper string reaches
  `git` through `-c credential.helper=…` in argv, but the token itself is only
  ever `$GITHUB_TOKEN` *unexpanded*, read from the environment by the helper —
  so it is absent from `ps`, from `.git/config`, and from the log, which prints
  the short form `git pull` rather than the real argv.
- The request can never supply the command: `UPDATE_COMMAND` is read once from
  the environment at import time, and the HTTP handler has no path that reaches
  `subprocess`.
- Concurrency: a second `POST /update` while one is running returns 409 rather
  than starting a second recipe.

One comment is imprecise rather than wrong: `UPDATE_TIMEOUT` (default 1800 s) is
described as a "generous ceiling for `git pull && docker compose build &&
docker compose up -d`", but it is applied **per step** (`subprocess.run(...,
timeout=UPDATE_TIMEOUT)` inside the loop), so the built-in three-step recipe's
real ceiling is 3 × 1800 s. Not filed separately; folded in as a one-line note
if this becomes an issue.

## Ranking

Below `signal-pending-sends-tmp-not-a-volume.md` (which discards messages a user
was asked to approve) and below `qlever-static-gz-cache-defeats-reindex.md`
(which serves stale data while reporting success). This one misleads a caller
about a state it can re-check by other means.
