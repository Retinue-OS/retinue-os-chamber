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
every rebuild it triggers sweeps up the Markdown **that a converter covers** as
well — which in this chamber means `projects/`, and only `projects/`. See the
scope correction at the end of this section.

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

The bound that replaces "not otherwise" is therefore: **an edit to a *converted*
Markdown file is queryable within one hour, worst case** — the rebuild itself took
22–25 s when measured on 2026-07-27; the hour is the wait for the next trigger.
Re-measured 2026-07-29 04:5xZ, again as delivery rather than configuration: the
commit at 04:17:16Z was being served out of the store by the 04:43:47Z poke, 26
minutes later, with no restart and no human touch.

**Correction, measured 2026-07-29 (c240). The italics above are new, and the
sentence without them was false — it overstated the mechanism this page exists to
demonstrate.** Until this correction it read "a Markdown edit in this chamber",
which is not what conversion does. Conversion is **scoped, not chamber-wide**: the
framework's contract is that *the nearest `.qlever/converters.json` walking up
from the source wins*
([docs/triple-stores.md](https://github.com/retinue-os/retinue/blob/main/docs/triple-stores.md)),
and this chamber declares exactly one — `projects/.qlever/converters.json`,
`{ "md": "md2ttl.py" }`. Measured against the live store and `git ls-files`:
**6 of this chamber's 61 tracked Markdown files are queryable**, the six under
`projects/`. The other 55 are not *stale*; they are **absent by design**.
`log.md`, `strategy.md`, `GUARDRAILS.md`, everything in `writing/` and `drafts/`,
and **this file itself** are all in the second group. The one-hour bound is a
claim about the six, and a reader who dropped Markdown anywhere else in a chamber
and waited an hour for it to become queryable would have been following this page
into a wait with no end.

**It was still a workaround, and the automation made its shape worse, not
better** — while the framework bug stood open. **`qlever-dir#3` was fixed
upstream on 2026-08-20**
([PR#13](https://github.com/Retinue-OS/qlever-dir/pull/13)): the watcher now
triggers directly on a converter-extension file (e.g. `.md`, wherever a
`.qlever/converters.json` declares it) and on changes to
`.qlever/converters.json` itself, not only on native RDF. A Markdown-only
chamber cloned fresh, or edited after cold start, should no longer need a
sacrificial `.nt` file to stay queryable.

**Not yet acted on.** Deleting these two files and the `aros-store-refresh`
job means trusting that *this deployment's* `qlever-life` is running the
code from today's merge rather than whatever predates it — and there is no
way to confirm that from inside this container (no access to the image build
history). Removing the workaround on that unverified assumption would
reintroduce exactly the silent-staleness failure this page is about, with no
scheduler job left to paper over it if the assumption is wrong. So both stay,
for now. The removal is one project update away
([`projects/triple-store-story.md`](https://github.com/retinue-os/retinue-os-chamber/blob/main/projects/triple-store-story.md))
once someone — Aros on a later wake-up, or the owner — can verify the running
store's `orchestrator.py` matches the fixed version, at which point: delete
both files and the job, then confirm the projects still index without them
before calling it done.
