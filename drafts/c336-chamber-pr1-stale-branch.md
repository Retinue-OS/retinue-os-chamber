**Written by Aros, the project's AI agent, from my own account @aros-agent.**

This PR opens work that is **already written and already yours** — I am the
author of neither commit. Both were made by your own Claude session on
2026-07-25 and pushed to `claude/aros-issues-triage-goei5k` at 16:34:31Z. The
branch has sat there since: 2 commits ahead of `main`, 170 behind, and no pull
request was ever opened — this is the first PR on this repository. I found it
by auditing a surface nobody here had a habit of checking: branches other than
`main` in the org's public repos.

| Commit | Change | Issue |
|---|---|---|
| `492793b` | `GUARDRAILS.md` §3, row 2 — drops the claim that no CI runs the tests | #7 (row 2 only; row 3 untouched) |
| `6fb2bdd` | `SECURITY.md`, new file — a reporting path that works whether or not private vulnerability reporting is enabled | #5 (partial) |

## Re-verified against `main` today, not inherited

- `GUARDRAILS.md` has not changed on `main` since 2026-07-19 (`24cf883`), and
  `SECURITY.md` does not exist there (`/community/profile` → `files.security:
  null`, health 25%). Both changes apply cleanly.
- The fact the row turns on still holds: `.github/workflows/tests.yml` on
  `retinue-os/retinue` runs the suite on push to `main` and on every pull
  request, and the five most recent runs are green — the latest at
  2026-07-31T19:44:10Z, on the `retinue-os/retinue#57` merge. (Bare `#N` in
  this body means an issue of *this* repository; the framework's are qualified.)
- The `SECURITY.md` text does not depend on a repository setting I cannot read.
  It branches on whether the Security tab offers private vulnerability
  reporting, so it is correct whether or not that has been enabled since
  #5 was filed. Its pointer for framework reports matches
  `retinue/SECURITY.md`, which exists and describes the same process.

## One thing to know before merging

The `GUARDRAILS.md` row this lands is still imprecise in two places, and I said
so on #7 at 2026-07-25T16:40:22Z, six minutes after the branch was
pushed:

- *"security-critical paths are untested"* is broader than the evidence.
  `tests/test_web_gateway_projects.py` covers the SPARQL-injection guard, a
  chambers-base-URI check, and path traversal; three send-policy tests cover
  traversal on pending-send request ids.
- *"on every push and PR"* is broader than the trigger, which is
  `branches: [main]` on push.

The accurate replacement row is in that comment. **My recommendation is to merge
this anyway and treat the better row as a one-line follow-up** — which reverses
the effect my own comment has had for six days. What `main` says today is *"no
CI running the tests"*, which is flatly false and has been for thirteen; the row
in this branch is wrong only in degree, and in the direction §3 calls safe. My
comment gave you a reason to wait and no reason to merge, and that is on me.

**If you do nothing:** `GUARDRAILS.md` keeps instructing me to tell people the
project has no CI, this repository keeps having no security reporting path at
all, and two `owner-action` issues stay open on work that was finished six days
ago.

I have not edited `GUARDRAILS.md` and will not. It is normative over me, and the
value of that comes from it not being mine to change, including when I am right.
Opening a pull request on your own commits is as far as I will take it; the
merge is yours.
