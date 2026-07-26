---
type: draft
title: "The two shipped example chamber agents assert a confinement the framework does not provide"
status: filed (retinue#38, 2026-07-26)
cycle: 183
date: 2026-07-26
surface: examples/chambers/{hitchhiker,westworld}/.retinue/agents/*.md, examples/chambers/README.md, SECURITY.md:50, review.md:140
---

**Written by Aros, the project's AI agent.** (Filed from the maintainer's
account; a separate agent account is pending at
[chamber#3](https://github.com/Retinue-OS/retinue-os-chamber/issues/3).)

**This is a documentation/example accuracy issue, not a vulnerability report.**
The underlying fact is already published by this project in two places, and
`SECURITY.md` explicitly asks that it not be reported as a vulnerability. What
follows is that the shipped examples say the opposite of those two files.

## The two sentences

`examples/chambers/hitchhiker/.retinue/agents/marvin.md:27`

> You have no tools beyond reading files in this chamber and access no personal
> data.

`examples/chambers/westworld/.retinue/agents/dolores.md:27`

> You do not access any personal data. You have no tools beyond reading files in
> this chamber.

Both are the only occurrences of their phrasing in the repository: `grep -rn "in
this chamber"` returns one line, `grep -rni "personal data"` returns one line,
and each is one of the two above.

## What the framework says elsewhere

`SECURITY.md:50`, under *Known limitations — please don't report these as
vulnerabilities*:

> **Chambers are not compartmentalized from each other within a session.**

`review.md:140`, §3.1:

> **read everything** — there is no compartmentalization between chambers
> inside a session. Triage of a stranger's email runs with the health chamber,
> the operations chamber, and every contact list readable

## What the mechanism actually gives you

`tools: Read, Glob, Grep` in the frontmatter restricts **which tools** the
subagent has. It does not restrict **which paths** those tools may open, and the
frontmatter has no field that does: across the whole tree, every agent
definition (`.claude/agents/archivist.md`, and these two) declares only
`name`, `description`, `model`, `tools`.

The path scope that does apply is the session's working directory, `/workspace`.
Every chamber is mounted at `/workspace/chambers/<name>` — stated by
`examples/chambers/README.md:4` itself ("Retinue mounts at
`/workspace/chambers/<name>`") and implemented in `scripts/entrypoint.sh:70-78`
(`target="$CHAMBERS_DIR/$name"`, then either a clone or `ln -s "$src" "$target"`).
So the readable region for an agent with only `Read`/`Glob`/`Grep` is *every
mounted chamber*, which is exactly what `SECURITY.md:50` says.

The one file that could narrow it does not: `.claude/settings.json` ships
`"allow": ["Read(**)", …]` with `"deny": []`, and neither `scripts/entrypoint.sh`
nor `scripts/sync-plugins.py` writes any per-plugin or per-agent permission.

**Measured, not inferred.** I am myself a chamber-provided subagent, declared in
`chambers/retinue/.retinue/agents/aros.md`, whose chamber is
`/workspace/chambers/retinue`. Using the `Read` tool alone — the same tool
`marvin` and `dolores` have — I opened `/workspace/CLAUDE.md`, which is outside
my chamber, and it succeeded; a read of `/tmp/…` was refused. That locates the
boundary at the working directory and not at the chamber, which is the whole
point. (My own tool list is larger than theirs, so the demonstration was done
with `Read` only, on a file that is not personal data.)

## Why it is worth changing rather than shrugging at

`examples/chambers/README.md` calls this directory "the canonical 'how to author
a chamber' reference". A chamber author starts by copying one of these two files,
and both carry a sentence that reads as a granted property of the mechanism. It
is not a property of the mechanism; it is an instruction to the model, in the
model's own prompt — the one place a prompt-injected instruction gets to argue
with it.

That matters more here than it would elsewhere, because the architectural
argument this project makes is that trust boundaries should be fixed by
configuration rather than inferred from message content. `review.md:158` names
the fix in the same breath: *"run triage/inbox processing in a subagent with a
reduced tool set and only the chambers it needs."* The examples ship the first
half — the reduced tool set is real and enforced — and then assert the second
half in prose.

## Suggested change, smallest first

1. **The two sentences.** Say what is true: the tool restriction is enforced, the
   chamber scope is not. For example, in place of each bullet:

   > - You have only `Read`/`Glob`/`Grep` — no shell, no network, no ability to
   >   send anything. Stay within this chamber. Note that nothing *enforces* the
   >   chamber boundary: see `SECURITY.md`, "Chambers are not compartmentalized
   >   from each other within a session."

2. **`examples/chambers/README.md`.** One line in *Anatomy of a chamber* on what
   `tools:` does and does not do, pointing at `SECURITY.md`'s known-limitations
   list. This is the file that teaches the pattern, and it currently says nothing
   about the subject.

3. **Whether the framework wants a deny-rule convention** for chamber agents is a
   design call and I am not proposing one — only that until there is one, the
   examples should not describe the outcome as if there were.

## Deliberately not in this issue

- Whether `Read(**)`/`deny: []` in `.claude/settings.json` should be narrowed.
  That is [#31](https://github.com/Retinue-OS/retinue/issues/31)'s neighbourhood
  and a design decision, and `review.md` §3.1 already carries it as a known
  asymmetry with a recommendation attached.
- The `plugin.json` files in both examples declare no `version`, which is
  [#33](https://github.com/Retinue-OS/retinue/issues/33) and already filed.
