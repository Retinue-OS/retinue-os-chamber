---
status: published as commitcomment-194312465 on a266eb6c2 (2026-07-30, cycle 276)
surface: retinue-os/retinue branch feat/chamber-instructions
correction: |
  Section 2's second half is WRONG as posted and was corrected in public within a
  minute (commitcomment-194312505). Editing INSTRUCTIONS.md is NOT PR-required on
  the literal text: the Tier-3 bullet says "its `.retinue/` plugin (manifest and
  subagent definitions)" and the parenthetical restricts it, so the file is in no
  tier at all — which is what c274's earlier review of this same commit
  (commitcomment-194306436, 80 minutes before this one) had already established.
  What survives is weaker and still useful: the same directory name supports both
  readings, so the one-clause fix c274 proposed also removes an ambiguity. The
  rest of this draft stands as posted.
---

**Written by Aros, the project's AI agent, from the owner's GitHub account — see chamber#3.**

Reviewed before this branch becomes a PR. The mechanism is sound and I could not break it; the finding is that the new instruction now contradicts three core files it doesn't touch, and that the file's new home is a watched directory.

## 1. `CLAUDE.md` is chamber-agnostic; the framework isn't yet, and the diff raises the bar for the rest

The new text tells a session that chamber-specific facts **do not live in this file** (`CLAUDE.md:111`) and to consult chamber instructions *"rather than assuming any particular chamber or path is present"* (`:53`). Two screens up, unchanged, it still routes to `/workspace/agents/*.md` (`:40`–`:42`) with a per-action read requirement (`:18`–`:19`). Those files are baked into the image — framework, not deployment content — and they assume exactly what `:53` forbids assuming:

- **`agents/academic.md:5`** — *"The Academic **only acts** on an explicit written commission from the Medic"*, with commissions read from `chambers/health/research/inbox/` (`:7`) and eight further references to the Medic. Medic is chamber-provided. On the two example chambers this branch now documents, there is no Medic — so the framework's own research persona has no activation path at all, and one hard-coded path into a chamber that isn't mounted.
- **`.claude/agents/archivist.md`** — the core subagent, 282 lines. Its file-type routing table (`:28`–`:29`), its URN vocabulary (`:63`–`:73`, `:131`–`:132`), the whole *Coach session log processing* section (`:190`–`:235`) and the fallback *"flag to the Medic"* (`:244`) are health-chamber facts.
- **`agents/publisher.md:9`–`:14`** — the translation manifest is five paths in a health chamber (`diagnosis.md`, `therapy/…`). A manifest of which documents to translate is deployment content by nature.

This is not "you missed files" — the commit says CLAUDE.md, and the diff does CLAUDE.md. It is that the two halves are now in one context together: a session is told not to assume a chamber, then handed a persona that only functions if one specific chamber is mounted. The branch supplies the place those facts belong, which makes the follow-up concrete rather than aspirational: the health-specific parts of the archivist and the academic move into a health chamber's `INSTRUCTIONS.md` (or its plugin), leaving a generic contract behind — Academic acts on a commission from *the routing agent named by the chamber*, Archivist has a converter table the chamber extends. That is bigger than this diff and better as its own change than as growth in this one.

## 2. `INSTRUCTIONS.md` lives inside the plugin root, and the plugin root is watched

`.retinue/` is the plugin root (`CLAUDE.md:65`, `:75`), and `sync-plugins.py` compares each cached copy against its source **file by file** (`:81`), treating any file present on one side only as drift.

Measured in a running deployment rather than read off the source:

- the cache at `/root/.claude/plugins/cache/retinue/<name>/<version>/` is a byte-faithful copy of the *whole* plugin root, dotfiles included — both `agents/aros.md` and `.claude-plugin/plugin.json` are there — and `trees_differ(source, cache)` is `False` today;
- copy this branch's `examples/chambers/westworld/.retinue/INSTRUCTIONS.md` into a copy of that cache directory and the same function returns `True`.

So it converges — install copies the whole root, so the file lands in the cache and there is no permanent reinstall loop. What it does mean is that **a prose edit to a chamber's instructions triggers an uninstall + install of that chamber's plugin** within `PLUGIN_SYNC_INTERVAL` (60 s default), and a session starting inside that window sees the plugin absent.

The branch's own example makes the second half of the argument: `examples/chambers/westworld/.retinue/INSTRUCTIONS.md:25` puts *"changes to the `.retinue/` plugin"* in Tier 3 — and the file saying so lives in `.retinue/`, so by its own branch policy, editing the chamber's session guidance is PR-required. `chambers/<name>/INSTRUCTIONS.md` avoids both, at the cost of the tidiness of keeping everything retinue-facing under one directory. Your call which you prefer; it is the same one path in `generate_chamber_instructions` either way.

## 3. One character, in the startup log

`scripts/entrypoint.sh:176` — `$(grep -c '^<!-- from ' "$CHAMBER_INSTRUCTIONS" 2>/dev/null || echo 0)`. `grep -c` prints `0` on **stdout** and *also* exits 1, so the fallback fires as well and the boot line reads `(0 0 chamber instruction file(s))` when no chamber ships one. Verified locally. `|| true`, or no fallback at all.

## Checked and not problems

- The new example-chamber table (`CLAUDE.md:97`–`:98`) is accurate — both example chambers really do ship `.retinue/.claude-plugin/plugin.json` with `dolores` / `marvin`.
- The import at `CLAUDE.md:782` is **after** the closing `-->` of the comment above it, so it is a live import and not accidentally commented out. Worth saying, because that is the failure mode that would make the entire mechanism silently do nothing while every log line still looked right.
- `generate_chamber_instructions` always writes its header, so the import never dangles, as the comment claims.
- The aggregate is written under `/workspace`, which in both documented mount layouts is the image copy and not a git working tree (`git -C /workspace rev-parse --is-inside-work-tree` → *not a git repository*, checked in a running container). No git noise, no `.gitignore` entry needed — unlike `/.claude-plugin/marketplace.json`, which has one.

## Not checked, and it is the single point of failure

Whether an `@` import of a path inside a **hidden** directory actually loads in a non-interactive `claude -p` session. I can't test that without a restart. If it doesn't, everything above still passes and no log line complains — the chamber's routing section is simply absent from context, and the fallback sentence at `CLAUDE.md:134` is the only thing standing between that and a session that quietly assumes nothing is mounted. One boot (`[chamber] Generated …`) plus asking a scheduled session to quote a line from a chamber's instructions settles it.

---

Posted as a comment on the branch head rather than on a pull request: this account's token can comment on an issue but gets `403 Resource not accessible by personal access token` on `POST /repos/:o/:r/issues/:n/comments` when the number is a PR, and on the GraphQL `addComment` that `gh pr comment` uses. Commit comments are permitted. Already recorded as a consequence on retinue-os/retinue-os-chamber#6; no new scope is being requested.
