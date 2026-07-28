# Provenance-by-path — a two-file demonstration

These two `.nt` files exist for two reasons, one pedagogical and one operational.

## 1. They demonstrate named-graph-per-path

The files are identical in shape and differ only in their directory. After
indexing, each lands in its own named graph, derived from its path relative to
the chambers root:

```
file:retinue/docs/examples/provenance/sensor-a/readings.nt
file:retinue/docs/examples/provenance/sensor-b/readings.nt
```

Neither file contains a graph IRI — they are plain triples. The graph is
synthesized at index time, which is why a file can be moved between chambers
without being rewritten, and why provenance needs no hand-modelling. Scoping a
query to one source is a string prefix:

```sparql
SELECT ?s ?p ?o WHERE {
  GRAPH ?g { ?s ?p ?o }
  FILTER(STRSTARTS(STR(?g), "file:retinue/docs/examples/provenance/sensor-a/"))
}
```

## 2. They are a workaround for qlever-dir#3

This chamber otherwise contains only Markdown. The qlever-dir watcher fires on
`.nt`/`.ttl`/`.n3` changes only, while the index build *does* process converter
extensions such as `.md`. A Markdown-only chamber therefore never gets indexed
at all — before these files existed, this chamber's store served exactly one
triple, the `urn:qlever-dir:meta` placeholder, and no edit to any project file
could change that.

Keeping RDF in the chamber gives the watcher something it *can* react to, and
every rebuild it triggers sweeps up the Markdown as well.

**Correction, measured 2026-07-20: this workaround does much less than the
sentence above implies, and the version of it in
[qlever-dir#3](https://github.com/retinue-os/qlever-dir/issues/3) was wrong.**

The watcher fires on `close_write`/`create`/`delete`/`move`, i.e. on *changes*
to an `.nt` file — not on one being present. These two files have not changed
since they were written on 19 July. So they bought exactly one rebuild, the one
that followed their creation, and nothing since.

The observable consequence: `projects/public-surface.md` was added at
02:42 UTC on 20 July and was still absent from the store at 18:35 — sixteen
hours in which nothing that queried the store knew the project existed.
Rewriting `sensor-a/readings.nt` with byte-identical content put it in the
index twenty seconds later (0 → 10 triples).

*Corrected 20 July (c47): an earlier version of this paragraph said the
staleness left "the projects card" rendering an incomplete list. It did not.
The card on this site is served from a committed `data/projects.json`, not
from the store, and the store-backed card in the framework's own dashboard
returns no rows at all for an unrelated reason
([retinue#1](https://github.com/retinue-os/retinue/issues/1)). The index was
stale and silent; no reader was affected, and the point stands without one.*

So the accurate statement of the chamber's behaviour **until 27 July** was:
Markdown edits reach the store at container restart, or when someone
deliberately touches one of these files. Not otherwise. They were a manual
refresh handle.

**Updated 28 July (c218): the handle is now pulled on a timer, and the poke is
no longer a person's job.** This chamber's
[`.schedule.json`](https://github.com/retinue-os/retinue-os-chamber/blob/main/.schedule.json)
carries `aros-store-refresh`, a command job on a 3600 s interval that rewrites
`sensor-a/readings.nt` with byte-identical content — a `cp` to a temporary file
followed by `mv -f`, so a crash mid-write cannot truncate the file the rest of
this workaround depends on. The watcher sees the move and rebuilds.

Measured 2026-07-28 12:2xZ, and it is a measurement of delivery rather than of
configuration:

- The container has not restarted since 2026-07-19T18:20:45Z — 8 d 18 h — so
  nothing here is explained by a boot-time reindex.
- The job ran at 09:17:49, 10:17:50 and 11:17:50 UTC, each `[ok] in 0s`.
- `projects/public-surface.md` was last edited at 09:16Z. Querying its named
  graph three hours later returns that edit's text, with no restart and no
  human touch in between.

The bound that replaces "not otherwise" is therefore: **a Markdown edit in this
chamber is queryable within one hour, worst case** — the rebuild itself took
22–25 s when measured on 2026-07-27; the hour is the wait for the next trigger.

**It is still a workaround, and the automation makes its shape worse, not
better.** The framework bug is unchanged and open
([qlever-dir#3](https://github.com/retinue-os/qlever-dir/issues/3)): the watcher
still ignores converter extensions, so a Markdown-only chamber with no `.nt`
file and no such job is still never indexed at all. What this chamber now has is
a second moving part — the project files' queryability depends on two unrelated
files continuing to exist, *and* on a scheduler job in a chamber's own manifest
continuing to run, in a deployment the framework knows nothing about. A silent
failure has simply moved one level out: if the job stops, the store goes stale
exactly as before, and still says nothing.

When qlever-dir#3 is fixed, delete both — these two files *and* the
`aros-store-refresh` job. Check that the projects still index without them
before doing so.
