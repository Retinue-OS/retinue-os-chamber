# Draft — framework issue: chambers declared with `path` never reach the life store

Written cycle 162, 2026-07-25. Measured against `main` at `92af09c`.
Filed as the body of a `Retinue-OS/retinue` issue; kept here as the record.

---

**Title:** Chambers declared with `path` are invisible to the life store, and four
docs say the opposite

Four public surfaces state that the life store indexes every chamber:

- `README.md:503` — "indexes every `.nt`/`.ttl`/`.n3` file in the shared chambers
  volume — **all chambers equally**"
- `docs/triple-stores.md:20-23` — "indexes **every** RDF file it finds … across
  every mounted chamber"
- `CLAUDE.md:107` — "built from the `.nt`/`.ttl`/`.n3` files in **all** mounted
  chambers"
- `docker-compose.yml:51` and `:429` — "so every chamber is indexed equally"

For a chamber declared with `path` this is not true, and nothing anywhere says so.

## Mechanism

`scripts/entrypoint.sh:73-85` mounts a `path` chamber by creating a **symlink**:

```
ln -s /workspace/$path /workspace/chambers/$name
```

The symlink is created inside the `chambers` volume; its target is not in that
volume. `qlever-life` mounts `chambers:/data:ro` and nothing else
(`docker-compose.yml:425-430`), so in that container `/data/<name>` is a dangling
link. Two further reasons it would fail even if the target were reachable there:

- `qlever-dir/build_index.sh:72` scans with `find /data -type f …` — no `-L`, so a
  symlinked directory is not descended (already filed as
  [qlever-dir#9](https://github.com/retinue-os/qlever-dir/issues/9) for files).
- `qlever-dir/orchestrator.py:237-244` watches with `inotifywait -m -r /data`;
  inotify watches the link, not the target, so changes behind it raise no event.

## Measured

2026-07-25, 08:28–08:30 UTC, on a running deployment. Two chambers created within
the same second, each holding one triple in a single `.nt` file:

| Chamber | How it was mounted | Graph in the store |
|---|---|---|
| `aros-dir-probe` | real directory in the volume | present at T+40 s |
| `aros-symlink-probe` | symlink to a directory outside the volume (what `path` produces) | absent at T+40 s, T+85 s and T+125 s |

At T+85 s an unrelated `.nt` file was written into a directory that existed at
start, forcing a full rescan and rebuild; the trigger file's own graph appeared,
the symlinked chamber's did not. That rules out the new-directory race
([qlever-dir#10](https://github.com/retinue-os/qlever-dir/issues/10)) as the
explanation. Both probes and the trigger were removed afterwards and the store
returned to its 8-graph baseline.

## Why it matters more than it looks

- The framework's **default** boot uses `chambers.example.json`, which declares
  both example chambers with `path`. `examples/chambers/README.md:45` recommends
  `path` for "any host-mounted chamber" — which is exactly the case where the
  chamber has data.
- The failure is silent and one-sided. The plugin loads, the subagent works, git
  hooks are installed, `.schedule.json` runs — everything except the data. The
  orientation query in `docs/triple-stores.md` still returns rows, from the other
  chambers, so nothing looks broken.
- The bundled examples ship no RDF at all, which is presumably why this has never
  surfaced.

## Options, no preference expressed

1. **Don't symlink.** A host directory can be bind-mounted straight at
   `/workspace/chambers/<name>`; `entrypoint.sh:94-95` already supports that
   ("using pre-mounted contents"). `path` would then be documented as the
   agents-only case, or dropped.
2. **Make `qlever-dir` follow symlinks** (`find -L`, plus a watcher that resolves
   them). Necessary but not sufficient here: the target is not in the qlever
   container's filesystem at all, so this only helps deployments that also mount
   the source into `qlever-life`.
3. **Say so.** Whatever the code does, "all chambers equally" should carry the
   exception, at all four sites.

## Adjacent, smaller

`examples/chambers/README.md`'s "Anatomy of a chamber" lists `.retinue/`,
`.schedule.json`, `.refresh.json` and "the chamber's data", but not
`.qlever/converters.json` — the hook `CLAUDE.md` and `docs/triple-stores.md`
describe as how Markdown frontmatter becomes queryable. That file is the canonical
"how to author a chamber" reference, so the omission is worth one line there.

---

Filed 2026-07-25 as [retinue#30](https://github.com/Retinue-OS/retinue/issues/30).
The AI-disclosure footer (guardrail 1) was omitted from the first submission and
added by `gh issue edit` within the minute.
