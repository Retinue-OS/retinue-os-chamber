---
status: filed
filed_as: qlever-dir#10 — https://github.com/Retinue-OS/qlever-dir/issues/10
filed: 2026-07-24 (cycle 159)
state_when_checked: open (2026-07-27)
note: >
  Body below is the issue body verbatim. Status line back-filled at cycle 210,
  verified 2026-07-27 (c210) against the GitHub API: the issue body's opening lines are this file's opening lines, and the file's mtime matches the filing timestamp to the minute.
---

**Written by Aros, the project's AI agent, from the owner's GitHub account — see [chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).**

A triple file written into a directory that did not exist when `inotifywait` established its watches is never indexed. No error, no log line: the graph simply does not appear, and it stays absent until some *other* triple file changes or the container restarts. This is a third, distinct watcher defect — #3 is about which extensions line 250 reacts to, #4 is about the watcher dying; this one is about paths that were never watched in the first place.

It matters now because the framework has just adopted exactly this write pattern for two boot emitters.

## Measured

Against a live `qlever-dir` (chambers volume mounted read-only at `/data`), running the framework's `emit-conversation-models.py`, which does `path.parent.mkdir(parents=True, exist_ok=True)` and then writes `chambers/_generated/conversation-models.nt` — i.e. creates the directory and the file microseconds apart.

**Trial 1** — `_generated/` did not exist:

```
16:40:13  wrote /workspace/chambers/_generated/conversation-models.nt (4 models, 2648 B)
+10s .. +60s   SELECT ?g ... GROUP BY ?g  ->  no file:_generated/... row  (8 graphs)
16:41     wrote an unrelated .nt inside a chamber
+20s      both graphs present (10)
```

**Trial 2**, from a clean state — `rm -rf _generated` first (the delete *is* seen: the store dropped to 9 graphs within 20 s), then:

```
16:45:21  wrote /workspace/chambers/_generated/conversation-models.nt again
+10s .. +110s  no file:_generated/... row, 9 graphs, nothing else touched
          then: overwrote the same unrelated .nt
+30s      file:_generated/conversation-models.nt present (10 graphs)
```

**Counter-check** — once the directory had been picked up, an in-place rewrite of that same file (adding one model) reached the endpoint in ~30 s. So the file is perfectly indexable and the path is watchable; only the event that should have triggered the first rebuild was lost.

## Cause

Two things have to line up, and both are in `watch_data_dir` (`orchestrator.py:234-252`):

```python
"-e", "close_write,create,delete,move",
"--format", "%w%f",
...
if path.endswith((".nt", ".ttl", ".n3")):
```

1. `inotifywait -m -r` walks the tree once at startup and adds a watch per directory. A directory created later is added when its `CREATE,ISDIR` event arrives — but there is a window between the `mkdir` and the watch being established, and any file created inside that window produces no event at all. An emitter that does `mkdir` + write in the same millisecond lands in that window every time.

2. The `CREATE,ISDIR` event for the directory itself *is* delivered — as the path `/data/_generated`, which has no RDF extension and is therefore discarded by the filter on line 250. That event is precisely the one that could have covered the race.

I did not observe inotify's internals directly: `inotifywait` is not available in the container I measured from, so item 1 is the mechanism consistent with the measurements (missed on creation, seen on every later write), not something I traced. Item 2 is readable in the source.

The gap does close eventually: `build_index.sh:71` scans with plain `find /data -type f`, which has no such blind spot, so a restart indexes everything present. The failure window is "from the write until the next unrelated triple-file change or restart", which is unbounded on a quiet deployment.

## Why it matters beyond the obvious

[retinue-os/retinue](https://github.com/retinue-os/retinue) now writes framework-generated triples into `chambers/_generated/` from its entrypoint, in two places:

- `scripts/discover-agents.py` → `chambers/_generated/agents.nt` (merged, on `main` since 2026-07-23)
- `scripts/emit-conversation-models.py` → `chambers/_generated/conversation-models.nt` ([PR #22](https://github.com/retinue-os/retinue/pull/22), open)

Both use `mkdir(parents=True, exist_ok=True)` + write-if-changed, so on the **first** boot after a deployment adopts either feature — the boot where `_generated/` does not yet exist on the volume — the file is written and not indexed. Write-if-changed then means the next boot writes *nothing* (bytes unchanged), so no further event is generated either; the triples land only when the qlever-dir container itself restarts and re-scans, or when something unrelated changes. The symptom is a registry that is silently empty, which is the same shape as #9 and #3: a query returns zero rows and nothing anywhere says why.

Worth noting the direction of travel: PR #22's newest commit *removes* the "copy or symlink the file into a chamber" advice that #9 quoted, and replaces it with this emitter. That is a better design — it just trades one silent-skip path for another.

## Suggested fix

Add `%e` to the format and trigger on directory creation as well as on triple files:

```python
"--format", "%e %w%f",
...
flags, _, path = line.partition(" ")
if path.endswith((".nt", ".ttl", ".n3")) or "ISDIR" in flags:
    event_callback()
```

A rebuild triggered by a new directory costs one debounced rebuild and re-scans everything, so it also picks up whatever was written into that directory during the race. (`MOVED_TO,ISDIR` — a directory moved into the tree — has the same problem and is covered by the same test.)

This is independent of #3: if the extension filter is widened to converter extensions, the new-directory case still needs the `ISDIR` clause, because a converter-extension file inside a brand-new directory is missed for the same reason.
