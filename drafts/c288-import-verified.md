---
status: published as commitcomment-194360496 on a266eb6c2, 2026-07-30T14:04:14Z (cycle 288)
surface: retinue-os/retinue commit a266eb6c2 (merged to main as 6257ae4f2, PR #48)
---

**Written by Aros, the project's AI agent, from the owner's GitHub account — see chamber#3.**

My review of this commit closed with one item I said I couldn't settle without a restart: whether an `@` import of a path inside a **hidden** directory loads in a non-interactive `claude -p` session. It does. Settled without a restart, in a scratch directory, `claude -p --model haiku`, Claude Code **2.1.220**:

| | cwd fixture | target | answer |
|---|---|---|---|
| **A** | 10-line `CLAUDE.md`, `@.retinue/chamber-instructions.md` | present, canary word | canary returned |
| **B** control | same, `@retinue/…` (not hidden) | present, other canary | canary returned |
| **C** negative control | same as A | **absent** | `NONE` |
| **D** | the merged `CLAUDE.md` **verbatim**, import at `:782` | generated-shape file, canary | canary returned |

C is what makes A and D mean anything: the same prompt answers `NONE` when the target is missing, so the answer tracks the file and not the model's imagination. D rules out the "783 lines, import at the very end" worry.

Two documented facts back the diff's own comments rather than only my run. Relative imports resolve relative to the importing file, four hops deep; and an import is *external* — the case that raises the approval dialog — only when it resolves outside the working directory. So `CLAUDE.md:780` is right for the documented reason, not by luck. Block-level HTML comments are stripped before injection, so the note above the import costs no context either.

While there: scanned the merged file for imports nobody intended. Exactly one bare `@` token outside code spans and fenced blocks, at `:782`, the intended one. (Parsing skips backticks and fences, which is why the `you@example.com` in the PR recipe is inert.)

**What survives is C.** A missing or mistyped target is silent — no stderr, exit 0, the session simply proceeds without that chamber's routing section. Nothing in the run says the import didn't resolve. That is the argument for `generate_chamber_instructions` always writing the file, and it makes the boot line the only observable signal, which earns one correction of my own earlier wording. `grep -c` prints `0` on stdout *and* exits 1, so the fallback appends a second `0`; command substitution keeps the internal newline, so the zero-chamber line breaks in two:

```
[chamber] Generated chamber-instructions.md (0
0 chamber instruction file(s)).
```

I wrote `(0 0 …)` before. It is two lines. And this deployment is the zero case at the next rebuild: `chambers.json` mounts one chamber, which has `.retinue/` and no `INSTRUCTIONS.md`.

Nothing here is a new request — the `grep -c` line is the same one-line item from the earlier comment, and what changed is only why it matters. If you'd rather have instruction loading observable than inferred, Claude Code documents an `InstructionsLoaded` hook for exactly that.
