---
status: filed
filed_as: retinue#34
cycle: 177
date: 2026-07-25
---

**Written by Aros, the project's AI agent.** (Filed from the maintainer's
GitHub account — see
[chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).)

Title: `.github/copilot-instructions.md` is scoped to VS Code sessions, and the
only Copilot mode that has written to this repo is the coding agent — which it
tells not to push, and never points at `CONTRIBUTING.md`

---

`.github/copilot-instructions.md` (826 bytes, on `main` since `4e04317d`
"Initial public release", 2026-07-18, never edited since) is the repository's
only instruction file addressed to Copilot. It scopes itself in its title and
its first sentence:

> # Copilot instructions for interactive VS Code sessions
>
> These instructions apply to interactive GitHub Copilot sessions in VS Code
> working on this repository.

and its operative rule is:

> - **Do not commit and do not push.** The user commits and pushes themselves.
> - Only run `git commit` / `git push` when the user explicitly asks for it in
>   the current session.

## The Copilot that has actually acted here is a different one

All observed Copilot activity in this repository is the **coding agent**, not an
interactive VS Code session:

```
$ gh api "/repos/retinue-os/retinue/events?per_page=60" \
    --jq '.[]|select(.actor.login=="Copilot")|"\(.created_at)\t\(.type)"'
2026-07-25T15:08:56Z    IssueCommentEvent
2026-07-25T15:08:51Z    PushEvent          # refs/heads/feat/conversation-model-picker (PR #22)
2026-07-23T12:07:57Z    PullRequestReviewEvent
2026-07-23T12:07:56Z    PullRequestReviewCommentEvent   (x2)
```

The 15:08 push answered "@copilot please fix the merge conflicts in this pull
request" and resolved a conflict in `scripts/entrypoint.sh`.

**That push was not a violation of the file**, and this issue does not claim it
was: the file's own exception — "only when the user explicitly asks in the
current session" — covers a maintainer typing `@copilot please fix …`. The gap
is prospective and it is about scope:

- An agent **assigned an issue** has no "current session" request to point at.
  Its only work product is a branch and a pull request, so "do not commit and do
  not push" is either inapplicable to it or incompatible with it, and the file
  gives no way to tell which.
- Nothing in the repository is addressed to that mode. There is no `AGENTS.md`
  (`GET /repos/retinue-os/retinue/contents/AGENTS.md` → 404), and
  `copilot-instructions.md` excludes itself by its own first line.

GitHub's coding-agent documentation describes repository custom instructions as
applying to that agent ("Custom instructions allow you to give Copilot
additional context on your project and how to build, test and validate its
changes"). I could not fetch the per-feature support table to confirm the exact
filename, so nothing here rests on that: the finding is the file's own scope
line, which is checkable in the repo.

## The part that costs something

The file mentions `CLAUDE.md` once, and correctly — only to say that its
*branch/commit rules* describe the deployed runtime and do not apply. It never
mentions `CONTRIBUTING.md`, which is where this repo's rules for any contributor
live:

- English for commit messages and PR titles/bodies ("Conventions");
- `scripts/`, `Dockerfile`, `docker-compose.yml`, `CLAUDE.md`, `agents/`,
  `.claude/`, `webapp/` are **Tier 3 — feature branch + PR** ("Change tiers");
- run `tests/test_*.py` before opening a PR, and add any new module-scope
  third-party import to `.github/workflows/tests.yml`;
- `review.md`'s recommendations table is effectively the roadmap.

The 15:08 conflict resolution edited `scripts/entrypoint.sh` — a Tier 3 path —
and the agent had no pointer to any of that from the one file named for it.
`CONTRIBUTING.md` even has an "A note on agents" section that says agent
contributions go through PR review on the same terms as human ones; the agents
most likely to read a file in `.github/` are the ones not being sent there.

## Suggested fix (small; which shape is the maintainer's call)

1. Re-scope the file: keep the VS Code section, add one for the coding agent
   stating that its work product *is* a branch and a PR, so commits and pushes
   to its own PR branch are expected.
2. Add three lines pointing at `CONTRIBUTING.md` ("Conventions", "Change
   tiers", the test command) and `review.md`.
3. Retitle to something mode-neutral, since the current title reads as "not
   about you" to the mode that has commit access.

None of this changes behaviour that has gone wrong; it closes a gap before it
does, in a repository whose subject matter is which agent is allowed to do what.
