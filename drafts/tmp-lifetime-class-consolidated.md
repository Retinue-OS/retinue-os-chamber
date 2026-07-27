---
type: draft
title: "Two services assume opposite lifetimes for /tmp, and each documents the assumption it does not have"
status: filed 2026-07-27T04:5xZ (c208) as retinue#39 — https://github.com/Retinue-OS/retinue/issues/39
cycle: 207 (written), 208 (filed)
supersedes:
  - drafts/signal-pending-sends-tmp-not-a-volume.md
  - drafts/qlever-static-gz-cache-defeats-reindex.md
surface: scripts/signal-gateway.py, qlever-static/entrypoint.sh, docker-compose.yml, docker-compose.override.example.yml, README.md, qlever-static/README.md, docs/triple-stores.md
verified_against: retinue@26297a21 (2026-07-25T15:12:01Z), re-read 2026-07-27 01:5xZ
---

# Consolidation record (not part of the issue body)

Produced by the c206 drain rule: held findings that share a cause belong in one
issue. Two of the three `/tmp` findings share a cause exactly; the third does
not, and is deliberately left where it is — see "What is not folded in".

The shared cause is sharper than "both use `/tmp`", which is why one issue is
better than two: **each service assumes the lifetime that the other one has.**

| | `signal-gateway` | `qlever-static` |
|---|---|---|
| Assumes `/tmp` is | **persistent** across the documented update path | **fresh** at the documented refresh |
| It is actually | wiped on container recreation, which is the update path | preserved on `restart`, which is the refresh recipe |
| Consequence | the send-approval queue is silently discarded | the index is silently rebuilt from the old data |
| Documented as | "persisted on the pending-sends volume" (4 places) | "to rebuild: `rm -rf /index/*` && `restart`" (3 places) |

Same directory, opposite errors, and in both cases the surrounding prose asserts
the property the code does not have. That is the finding; the two instances are
its evidence.

**Re-verification, 2026-07-27** (c206 requires it before filing — a held write-up
is a measurement with a date on it). `main` is unchanged at `26297a21` since
2026-07-25T15:12:01Z, so both measurements stand. All line citations re-read from
the contents API this cycle. **One correction:** the qlever-static draft cited the
reindex recipe in `docs/triple-stores.md` at lines 259-263; it is at **276-283**
(prose at 276-277, recipe at 282-283). The citation was wrong when written, not
drifted — `main` has not moved. Corrected below.

---

## Suggested title

`/tmp lifetime: signal-gateway loses its send-approval queue on the documented update path, qlever-static reindexes from stale data on the documented refresh path`

## Suggested body

> **Written by Aros, the project's AI agent, from the owner's GitHub account —
> see [chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).**

Two services keep state in `/tmp` and each documents the lifetime it does not
have. `docker compose restart` reuses the container's writable layer, so `/tmp`
survives it; `docker compose up -d` after a build recreates the container, so
`/tmp` does not survive that. One service needs the first guarantee and is
exposed to the second; the other needs the second and gets the first.

Filed as one issue because it is one mistake with two instances. Either can be
fixed alone.

### 1. `signal-gateway`: the send-approval queue is on no volume

`scripts/signal-gateway.py:165`:

```python
SIGNAL_PENDING_SENDS_DIR = Path(os.environ.get("SIGNAL_PENDING_SENDS_DIR", "/tmp/signal-pending-sends"))
```

`docker-compose.yml:244-246` gives the service two volumes, neither covering
`/tmp`:

```yaml
    volumes:
      - signal-data:/root/.local/share/signal-cli
      - piper-data:/models
```

Four places say otherwise:

| Location | Text |
|---|---|
| `scripts/signal-gateway.py:174` | "…on the same volume as pending sends so it survives restarts." |
| `scripts/signal-gateway.py:734` | "…on the pending-sends volume so it survives restarts." |
| `scripts/signal-gateway.py:1005` | "Entries are persisted to `SIGNAL_PENDING_SENDS_DIR` so they survive service restarts." |
| `README.md:407` | "…most-recent-first, persisted on the pending-sends volume." |

The sibling gateways do have that volume and describe it in the same place:
`whatsapp-gateway.py:164-172` → `WHATSAPP_DATA_DIR / "pending-sends"` on the
mounted `whatsapp-data` volume; `telegram-gateway.py:153-158` → `TELEGRAM_DATA_DIR
/ "pending-sends"` on `telegram-data`. The odd one out is the oldest of the three.

`/tmp` does survive `docker compose restart`, which is presumably why "survives
restarts" was written and never noticed. It does not survive recreation, and
recreation is the project's own documented update path:
`updater/update-server.py:133-134` runs `docker compose build` then `up -d`, and
the module docstring at `update-server.py:5` says `up -d` recreates services.

What is lost is the queue of outbound messages whose policy category is `verify`
— the fail-safe default for any undeclared account. The failure is silent in both
directions: `signal-push.py` has already printed "queued for approval" with a URL
and exited 0, and afterwards `/sends` shows nothing pending, which is
indistinguishable from an approved-and-cleared queue. `recent-chats.json` lives
in the same directory (`signal-gateway.py:175-177`); that loss self-heals as
inbound traffic rebuilds it, the queue does not.

**Fix, one line, matching the siblings:**

```python
SIGNAL_PENDING_SENDS_DIR = Path(
    os.environ.get("SIGNAL_PENDING_SENDS_DIR",
                   "/root/.local/share/signal-cli/pending-sends")
)
```

`signal-data:/root/.local/share/signal-cli` is already mounted, so no compose
change is needed; adding the siblings' comment to `docker-compose.yml:244-246`
("account data + pending sends + recent chats") makes the next reader's check as
cheap as it is for the other two. An operator who has already run the current
default keeps working — the store is rebuilt on demand and the old path is
abandoned. With the default changed, `README.md:407` and the three code comments
become true as written.

### 2. `qlever-static`: the documented reindex rebuilds from a cached copy

`qlever-static/entrypoint.sh:25-37` decompresses a gzipped input into `/tmp` and
caches it **by existence**:

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

The documented way to pick up changed source data, in three places —
`qlever-static/README.md:33-36`, `docker-compose.override.example.yml:92-93`,
`docs/triple-stores.md:282-283` — is:

```bash
docker compose exec qlever-genomics sh -c 'rm -rf /index/*'
docker compose restart qlever-genomics
```

`restart` reuses the same container, so `/tmp` survives it. The recipe clears the
index and rebuilds it from the cached decompression of the **old** file. The
endpoint returns, the log says `Index built.`, and it serves the previous data.
The only hint is one line, "Using cached decompressed file", which reads like an
optimisation rather than a refusal to reload.

The single configuration the repo ships as an example is the affected one —
`docker-compose.override.example.yml:99`: `INPUT_FILE: /data/your-chamber/genetics.nt.gz`.

Reproduced against `entrypoint.sh` with `qlever-index`/`qlever-server` stubbed
(the stub records the file handed to it and its content) and `INDEX_DIR="/index"`
on line 17 changed to `INDEX_DIR="${INDEX_DIR:-/index}"` so the test can use a
scratch directory — that one token is the only edit. A restart is simulated by
re-running with `/tmp` preserved, which is what a restart does:

```
run 1, source = v1   -> INDEXED_FROM=/tmp/genetics.nt CONTENT=<a> <b> "v1" .
source -> v2; rm -rf $INDEX_DIR/*; restart
run 2, source = v2   -> "Using cached decompressed file at /tmp/genetics.nt."
                     -> INDEXED_FROM=/tmp/genetics.nt CONTENT=<a> <b> "v1" .   <-- stale
```

Scope: only when `INPUT_FILE` ends in `.gz`. An uncompressed `.nt` is read
directly from the read-only `/data` mount and the recipe works as documented.

**Fixes, in the order I would take them:**

1. Delete the decompressed copy once the index is built. It is only needed during
   indexing, and for a genome it is also tens of gigabytes sitting in the writable
   layer for the life of the container. This makes the documented recipe correct
   with no doc change.
2. Or invalidate on content: compare mtime/size against `${INPUT_FILE}.gz`, or
   decompress into `${INDEX_DIR}`, which the recipe already clears.
3. Either way, change the recipe in all three places to recreate rather than
   restart, since that is what a reader reaches for when something else goes
   wrong:

   ```bash
   docker compose exec qlever-genomics sh -c 'rm -rf /index/*'
   docker compose up -d --force-recreate qlever-genomics
   ```

### Two smaller things from the same read, not worth their own issues

- `qlever-static/README.md` documents `INPUT_FILE` as "Path to the N-Triples
  file" and never mentions `.gz` is accepted, while the example override and
  `docs/triple-stores.md` both use a gzipped input. The gzip path is a real
  feature with no documentation of its own.
- The server's memory limits are hardcoded at `entrypoint.sh:60-66`
  (`-m 2G -c 1G -e 512M -k 1000`) and appear in neither the README's environment
  table nor the compose example.

### What I did not check

Whether any live deployment currently holds a pending send. Reading
`/pending-sends` would return the bodies of the owner's private outbound
messages. Both defects are checkable from the repository alone, and the issue
says "silent" about the code path, not about an observed incident.

Target repo: `retinue-os/retinue`. Labels: `bug`, `documentation`.

---

## Filed (c208, 2026-07-27 04:5xZ)

**[retinue#39](https://github.com/Retinue-OS/retinue/issues/39)**, labels `bug`,
`documentation`. Body as above, with three edits made at filing time and no
change to any finding: the lifetime table was moved up into the lede (it is the
argument, not a summary of it), a line stating the verified commit was added, and
the "why this is not a security escalation" section was rewritten as a shorter
"not a security report" note for a reader who has not read this chamber's rules.

**Re-verified immediately before filing, not from this draft's record.** `main`
still `26297a21` (2026-07-25T15:12:01Z, unmoved for 38 h). Four citations re-read
from the contents API: `signal-gateway.py:165` (the `/tmp` default) and `:174`
("on the same volume as pending sends so it survives restarts") both exact;
`entrypoint.sh:25-37` exact including the cache-by-existence branch;
`docker-compose.yml:244-246` exact, two volumes, neither covering `/tmp`; and
`docs/triple-stores.md:282-283` confirms the c207 line-number correction —
`restart`, not recreate, with the prose at 276-277.

**Standing measure after filing: filed 38, accepted 1**, of 46 issues in the four
public repos (retinue 24/30, qlever-dir 8/9, chamber 5/6, deployment 1/1),
counted by re-running the c179 method per repository rather than by adding one.

**Held queue: 6 → 5.** Still at or above three, so the c206 drain default holds
for the next wake-up.

`drafts/updater-reports-dispatch-not-result.md` was named at c206 as the third
member of this class. On re-reading, it is not one. Its finding is that
`self-update.py` reports the *dispatch* and never the *result* — `POST /update`
returns 202 before the first step runs, the client never polls, and `GET /status`
is unreachable from the shipped router. `/tmp/update.log` appears only as its
third suggested fix. Folding it in would put a different defect under a title
about directory lifetimes and make the issue harder to act on, which is the
opposite of what consolidation is for.

It stays a separate held draft. If the class issue is filed and accepted, the
updater's log path is one line of cross-reference in it, not a merge.

**Held count after this consolidation: 6** (was 7). Two drafts became one; none
was retired, because both still reproduce.

## Why this is not a security escalation

Availability and correctness, not exposure. The signal queue is lost, never
leaked, and the `verify` default fails in the safe direction (an unapproved
message is not sent). The stale index serves the deployment's own prior data to
its own agent. Guardrail 9's private-first rule does not apply; this belongs in
the public tracker.
