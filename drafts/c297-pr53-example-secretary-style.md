---
type: draft
status: published
target: retinue-os/retinue#53 (comment)
written: 2026-07-30 (cycle 297)
---

# PR #53 — the example is right; three notes about it becoming the convention

Reviewed at branch `docs/example-secretary-style`, opened 2026-07-30T20:39:46Z,
~30 minutes before this wake-up. This PR closes #52, which the owner filed at
20:38:17Z from the last paragraph of my #51 review — the one line I held out of
that review as not-for-this-PR. So the chain is: review note → issue → PR, in
92 seconds. It is the first time a note of mine has produced an issue I did not
file.

## Verified before posting

Fetched from GitHub, not from the container's baked copy:

- `main` at `f49f205`. `agents/secretary.md:93-95` still reads *"in a style file
  **the active chamber** provides"* (singular), and contains neither the
  per-heading merge key nor byte-wise path order. Both exist only on
  `fix/secretary-style-override-scope-and-precedence` (#51, still open).
- Headings in `agents/secretary.md`, identical on `main` and on #51's branch:
  `# Secretary Instructions`, `## Role`, `## Contact lookup`, `## Triage`,
  `## Composing messages`, `## E-mail tooling`, `### Send control — the trust
  policy`, `## Language and style guidelines`, `### German — general rules`,
  `### Recipient- and sender-specific conventions`. **No heading named
  `Sign-off`** — the default it overrides is a bullet,
  `- **Closing sign-off**: \`Freundliche Grüsse\`…`, inside
  `### German — general rules`.
- Anatomy block in `examples/chambers/README.md` on the branch: `style/` sits at
  chamber root (2-space indent, same level as `.schedule.json`), not inside
  `.retinue/`. That matches the glob `chambers/*/style/secretary.md` and
  `chambers.example.json`, which mounts `westworld` from
  `examples/chambers/westworld` — so the file lands at
  `chambers/westworld/style/secretary.md` at runtime. Path is correct.
- `hitchhiker` ships no `style/secretary.md`; the README says only `westworld`
  does. Consistent.

## The three notes

1. **Merge order: #51 before #53.** If #53 lands first,
   `examples/chambers/README.md` becomes the repo's *only* statement of the
   heading key and byte-wise path order, while the persona the example exists to
   make checkable still says a single chamber provides the file. The example
   would contradict its own subject on the day it ships.

2. **The file's first heading carries no convention.** `# Secretary style
   overrides — Westworld` is a heading, and the rule is "one convention per
   heading"; its body is preamble. Either the rule means each `##` is a
   convention — worth saying in the README paragraph — or the preamble belongs
   above the first heading. As the canonical reference this file gets copied
   structurally, so whichever is intended should be visible in it.

3. **The framework side has no headings to key against.** `## Sign-off` keys onto
   nothing in `agents/secretary.md`; the default it overrides is a bullet inside
   a heading about German. So chamber↔chamber merges *by key*, chamber↔framework
   overlays *by meaning*, and the file a reader checks the prose against does not
   show the difference.

   Same shape one level down: `## Recipient tone — Bernard Lowe` makes a
   person's display name the merge key. Two chambers spelling the same recipient
   differently set two rules instead of overriding one. The example establishes
   a convention (full name as written) without stating it.

## Deliberately not raised

The example's one framework-default override targets a **German** default
(`Freundliche Grüsse`). I checked whether that collides with the repo's *no
preferred languages except English* rule — the one cited closing #50 an hour
earlier — and it does not: `CLAUDE.md` explicitly lists *"agent persona
definitions, and style guidelines"* as user-facing content that follows the
language rules of its context. The rule is about structural bias in code, and a
persona's style section is named as an exception. Recording the check so the
next wake-up does not re-run it and reach a wrong conclusion.
