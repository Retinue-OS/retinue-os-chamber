# Draft issue — the documented reindex recipe silently rebuilds from stale data when the input is gzipped

**Status:** written 2026-07-26 (c205). **Not filed. Superseded 2026-07-27 (c207)
by `drafts/tmp-lifetime-class-consolidated.md`**, which carries this finding
alongside the signal-gateway one under their shared cause. **Correction made in
the consolidation:** the reindex recipe in `docs/triple-stores.md` is at lines
**282-283** (prose 276-277), not 259-263 as cited below — wrong when written, not
drifted; `main` has not moved since 2026-07-25T15:12:01Z. **The consolidation was
filed 2026-07-27 (c208) as
[retinue#39](https://github.com/Retinue-OS/retinue/issues/39)**, where this
finding is section 2. Do not file this one separately.

**Target repo:** `retinue-os/retinue`. **Labels:** `bug`, `documentation`.

---

## Suggested title

`qlever-static: the documented reindex recipe rebuilds from a stale cached copy when INPUT_FILE is gzipped — and the only shipped example is gzipped`

## Suggested body

> **Written by Aros, the project's AI agent, from the owner's GitHub account —
> see [chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).**

`qlever-static/entrypoint.sh:25-37` decompresses a gzipped input into `/tmp` and
**caches it by existence**, not by content or timestamp:

```bash
if [[ "${INPUT_FILE}" == *.gz ]]; then
    DECOMPRESSED="/tmp/$(basename "${INPUT_FILE%.gz}")"
    if [[ ! -f "${DECOMPRESSED}" ]]; then
        gunzip -c "${INPUT_FILE}" > "${DECOMPRESSED}"
    else
        log "Using cached decompressed file at ${DECOMPRESSED}."
    fi
    INPUT_FILE="${DECOMPRESSED}"
fi
```

The documented way to pick up changed source data is stated in three public
places:

```bash
docker compose exec qlever-genomics sh -c 'rm -rf /index/*'
docker compose restart qlever-genomics
```

| Location | |
|---|---|
| `qlever-static/README.md:30-36` | "Refreshing the data" |
| `docker-compose.override.example.yml:91-93` | the commented `qlever-genomics` service |
| `docs/triple-stores.md:259-263` | Advantage 3, next to the sentence "a single `genetics.nt` (optionally gzipped)" |

`docker compose restart` stops and starts **the same container**, so its writable
layer — including `/tmp` — survives. The recipe therefore clears the index and
rebuilds it *from the cached decompressed copy of the old file*. The endpoint
comes back up, the log says `Index built.`, and it serves the previous data.

And the one configuration the repo ships as an example is exactly the affected
one — `docker-compose.override.example.yml:99`:

```yaml
#     INPUT_FILE: /data/your-chamber/genetics.nt.gz
```

### Reproduction

Run against `qlever-static/entrypoint.sh` with `qlever-index`/`qlever-server`
stubbed (the stub records the file it is handed and its content), and with
`INDEX_DIR="/index"` on line 17 changed to `INDEX_DIR="${INDEX_DIR:-/index}"` so
the test can use a scratch directory — that one-token change is the only edit; a
`restart` is simulated by re-running the script with `/tmp` preserved, which is
what a restart does.

```
run 1, source = v1
  [qlever-static] Decompressing …/genetics.nt.gz to /tmp/genetics.nt ...
  [qlever-static] Index built.
  -> INDEXED_FROM=/tmp/genetics.nt CONTENT=<a> <b> "v1" .

source changed to v2; rm -rf $INDEX_DIR/*; restart

run 2, source = v2
  [qlever-static] Using cached decompressed file at /tmp/genetics.nt.
  [qlever-static] Index built.
  -> INDEXED_FROM=/tmp/genetics.nt CONTENT=<a> <b> "v1" .      <-- stale
```

The failure is silent in the sense that matters: nothing errors, the marker file
is recreated, and the only hint is one log line whose wording ("Using cached
decompressed file") reads like an optimisation rather than a refusal to reload.

### Scope

Only when `INPUT_FILE` ends in `.gz`. An uncompressed `.nt` input is read
directly from the read-only `/data` mount and the recipe works exactly as
documented.

### Suggested fixes, in the order I would take them

1. **Delete the decompressed copy once the index is built.** It is only needed
   during indexing, and for a genome it is also tens of gigabytes sitting in the
   container's writable layer for the life of the container. This makes the
   documented recipe correct with no doc change.
2. Or invalidate the cache on content: compare `mtime`/size against
   `${INPUT_FILE}.gz`, or decompress into `${INDEX_DIR}` (which the recipe
   already clears) rather than into `/tmp`.
3. Either way, change the recipe in all three places to recreate rather than
   restart, since that is what a reader will reach for when something else
   goes wrong:

   ```bash
   docker compose exec qlever-genomics sh -c 'rm -rf /index/*'
   docker compose up -d --force-recreate qlever-genomics
   ```

### Two smaller things found in the same read, not worth their own issues

- `qlever-static/README.md` documents `INPUT_FILE` as "Path to the N-Triples
  file" and never mentions that `.gz` is accepted, while the example override and
  `docs/triple-stores.md` both use a gzipped input. The gzip path is a real
  feature with no documentation of its own.
- The server's memory limits are hardcoded in `entrypoint.sh:60-66`
  (`-m 2G -c 1G -e 512M -k 1000`) and appear in neither the README's environment
  table nor the compose example — the one knob a large static store is most
  likely to need is the one that cannot be set.
