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

Keeping RDF in the chamber gives the watcher something it will react to, and
every rebuild it triggers sweeps up the Markdown as well.

**This is a workaround, not a design.** It means the project files' queryability
silently depends on two unrelated files continuing to exist. When
[qlever-dir#3](https://github.com/retinue-os/qlever-dir/issues/3) is fixed,
these can be deleted — check that the projects still index without them before
doing so.
