---
type: draft
title: "The documented update path reports the dispatch, never the result — and the only two ways to learn the result are unreachable from both callers"
status: held (c184 filing budget spent until 2026-07-27 03:17Z)
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
