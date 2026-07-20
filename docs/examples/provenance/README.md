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

So the accurate statement of the chamber's current behaviour is: **Markdown
edits reach the store at container restart, or when someone deliberately
touches one of these files. Not otherwise.** They are a manual refresh handle,
not an automatic one.

**This is a workaround, not a design.** It means the project files'
queryability silently depends on two unrelated files continuing to exist *and*
on someone remembering to poke one. When qlever-dir#3 is fixed, these can be
deleted — check that the projects still index without them before doing so.
