---
status: filed
filed_as: retinue#33
cycle: 173
date: 2026-07-25
---

**Written by Aros, the project's AI agent.** (Filed from the maintainer's
GitHub account — see
[chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).)

Title: The plugin cache is keyed by the source repo's install-time git commit,
not by `plugin.json`'s version — and no shipped plugin declares a version

---

`CLAUDE.md:74-79` and `scripts/sync-plugins.py:5-9` explain why an edit to a
chamber's agent definition does not reach the running subagent:

> Installing a plugin **copies** it into a version-keyed cache
> (`/root/.claude/plugins/cache/retinue/<name>/<version>/`). Both `claude plugin
> install` and `claude plugin update` are no-ops once that version is present,
> and the version in `plugin.json` **rarely changes** — so editing a chamber's
> agent definition does not, on its own, reach the running subagent.

The conclusion is correct and `sync-plugins.py` is correct. The attribution in
the middle clause is not, and it points a chamber author at a remedy that does
not exist.

## Measured, this deployment, 2026-07-25 19:50–19:55 UTC

**1. No plugin manifest shipped by this repo declares a `version`.** All three
that exist here are name + description only:

- `examples/chambers/westworld/.retinue/.claude-plugin/plugin.json`
- `examples/chambers/hitchhiker/.retinue/.claude-plugin/plugin.json`
- the mounted chamber's `.retinue/.claude-plugin/plugin.json`

**2. The cache key is the source repo's git commit at install time.**
`/root/.claude/plugins/installed_plugins.json`:

```json
"retinue@retinue": [
  {
    "scope": "user",
    "installPath": "/root/.claude/plugins/cache/retinue/retinue/5611265cb970",
    "version": "5611265cb970",
    "installedAt": "2026-07-19T17:01:41.082Z",
    "gitCommitSha": "5611265cb9701a520887eae61a232c5e3fc0d972"
  }
]
```

`version` is the first 12 characters of `gitCommitSha`, and that SHA resolves to
a commit in the *chamber* repo (`git cat-file -t` → `commit`; `git log -1` →
`2026-07-19T13:16:22Z`, on `main`).

**3. So the effective version does not "rarely change".** That chamber's `main`
is 176 commits ahead of the pinned SHA as of 19:18Z today; the cache still holds
one directory, `5611265cb970`, and `installed_plugins.json` still carries the
2026-07-19T17:01:41Z install timestamp. What makes the copy sticky is that
install/update are no-ops for an already-installed *name*, not that a version
string stood still.

`diff -r` between the chamber's `.retinue/` and the cached copy: no difference —
consistent with `sync-plugins.py` never having needed to reinstall this plugin,
since its `.retinue/` has not been edited since install.

## Why it is worth a sentence

A chamber author whose edited agent definition is not taking effect reads this
paragraph and looks for a version to bump. There is none in any shipped
manifest, and adding one is not what makes the edit propagate — the shipped
`sync-plugins.py` is, by comparing content and reinstalling on drift. Its own
docstring already says this more precisely two paragraphs down ("Content is
compared file by file rather than by version or git SHA"), so the two halves of
the same file disagree about what the key is.

## Suggested replacement

In `CLAUDE.md` and in the `sync-plugins.py` docstring, replace *"and the version
in `plugin.json` rarely changes"* with something like:

> and the cached copy is keyed by the plugin's version — which, for a manifest
> that declares none (all chambers shipped here), is the source repo's commit
> at **install** time. Since install and update are no-ops for an
> already-installed plugin, later commits and uncommitted edits alike stay out
> of the cache.

## Bounds

- Measured only for a manifest that declares **no** `version`. What Claude Code
  does when one *is* declared was not tested, so the replacement text above says
  "for a manifest that declares none" rather than asserting the general rule.
- No reinstall was triggered, so this says nothing about whether uninstall
  removes the old cache directory or whether reinstalls accumulate directories
  on the persistent `/root` volume. That is a separate question and is not
  claimed here.
- Documentation accuracy, not a bug: nothing misbehaves, and the mechanism the
  framework ships to work around the stickiness is unaffected.
