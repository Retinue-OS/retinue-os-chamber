---
type: draft
title: "ingest-sensors.py: the only documented invocation reads a directory no chamber has, and exits 0"
status: held (c184 rate limit; budget refreshes 2026-07-27 03:17Z — file this ahead of drafts/webapp-manifest-german-description.md)
cycle: 189
surface: scripts/ingest-sensors.py, .claude/agents/archivist.md:182, docs/triple-stores.md:170-173, scripts/sync-garmin.py:27-31
read_against: retinue-os/retinue main @ 26297a2 (shallow clone /tmp/fwmain; deployed /workspace/scripts/ingest-sensors.py is byte-identical)
---

# The finding

`scripts/ingest-sensors.py` is the only path a sensor CSV has into the life
store. Neither of its two documented invocations reaches a chamber, and the one
an agent actually runs fails silently with exit 0.

```python
# scripts/ingest-sensors.py:24
REPO_ROOT = Path(os.environ.get("CHAMBER_DIR", Path(__file__).resolve().parent.parent))
```

The default is the **framework** root. The script then globs
`REPO_ROOT/observations/clinical/sensors/{ckm,cgm,wearable,garmin}`, which is a
**chamber** layout. `main @ 26297a2` has no `observations/` directory at the
framework root, and neither does the baked image (`/workspace/observations`
does not exist).

`Path.glob()` on a missing directory yields nothing and raises nothing. Three of
the four scan loops have no `.exists()` guard (`:212`, `:221`, `:230`; only
`garmin_dir` at `:240` is guarded), and none of the four would report an absence
anyway. So:

```
$ CHAMBER_DIR= python3 /workspace/scripts/ingest-sensors.py
Ingesting sensor data...

0 observations written to source-adjacent .nt files
$ echo $?
0
```

Both documented call sites hit this:

| Where | Command as written | Result |
|---|---|---|
| `ingest-sensors.py:10-11` (docstring) | "Run from repo root: `python3 scripts/ingest-sensors.py`" | framework root → 0 observations, exit 0 |
| `.claude/agents/archivist.md:182` | "After moving sensor files, run `python3 scripts/ingest-sensors.py`" | same, from the subagent's `/workspace` cwd |

Neither mentions `CHAMBER_DIR`. A repo-wide grep finds exactly one writer of it —
`scripts/refresh.py:215`, which sets it for the *refresh* sources it dispatches —
and `ingest-sensors.py` is not a refresh source in any shipped manifest
(`.schedule.json`, `examples/chambers/*/.schedule.json`; no `.refresh.json` ships
at all). `sync-garmin.py:24` and `garmin-reauth.py:35` read the same variable and
*are* dispatched by `refresh.py`, so the fetch half of the pipeline gets a chamber
root and the ingest half does not.

Running the relative command from a chamber root instead does not rescue it: the
script does not consult cwd, and a chamber that has no `scripts/` directory gets
`No such file or directory` — loud, at least, unlike the `/workspace` case.

## Why the silence is the defect rather than the path

The archivist's instruction at `:182-188` is: move the CSVs out of the inbox, run
the ingest, then commit the moved CSVs **and the generated `.nt` files** in one
`git add`. With zero `.nt` files generated and exit 0, that commit lands the CSVs
alone and reports success. The framework ships no `.qlever/converters.json` for
`.csv` anywhere, so a CSV that never becomes `.nt` never reaches the store by any
other route.

Nothing is destroyed — the CSVs are committed and a later run with a correct root
recovers everything. What is lost is the signal: the failure is indistinguishable
from "there was nothing to ingest".

This is also the last step of the pipeline `docs/triple-stores.md:170-173`
describes as the answer to "a decade of readings, one query away":

> `scripts/sync-garmin.py` … drops a CSV in `observations/inbox/` → the
> **archivist** subagent files it into the right folder → `scripts/ingest-sensors.py`
> writes a sibling `.nt` → qlever-life picks it up.

The first, second and fourth steps are fine. The third, run as documented, writes
nothing.

# Second item: one of the twelve documented Garmin columns is not implemented

`scripts/sync-garmin.py:27-31` writes twelve data columns.
`.claude/agents/archivist.md:146-159` documents a property URI for all twelve.
`ingest-sensors.py:136-148` (`GARMIN_COLUMNS`) maps eleven.

| CSV column (`sync-garmin.py:27-31`) | Documented (`archivist.md`) | In `GARMIN_COLUMNS` |
|---|---|---|
| Steps, RestingHR, AvgHRV, TotalSleepMin, DeepSleepMin, REMSleepMin, LightSleepMin, AvgStress, SpO2, BodyBattery, SkinTemp | yes | yes |
| `Pushes` → `urn:health:property:wheelchair-push-count` | yes | **no** |

Fetched from Garmin (`sync-garmin.py:122`, `totalPushes`), written to the CSV,
committed to git, documented as mapped, and dropped at ingestion without a
warning. Measured on a one-row fixture carrying all twelve columns: `main` emits
55 triples / 11 observations, patched emits 60 / 12.

Two properties are in the code but missing from the list at
`docs/triple-stores.md:192-196` — `body-battery` and `light-sleep-duration`. That
list is hedged with "Properties currently ingested **include**", so it is
incomplete rather than false. Not part of the issue; noted so it is not
re-derived.

# Third item, cosmetic: the Ultrahuman observation count is halved

Every emitter in the file writes exactly five triples per observation. Three of
the four loops divide by five; `:235` divides by ten.

```
$ CHAMBER_DIR=/tmp/ingtest python3 scripts/ingest-sensors.py   # main @ 26297a2
  UH   ultrahuman-2026.csv ... 10 observations      # file contains 100 triples = 20
  GAR  garmin-daily-2026.csv ... 11 observations    # file contains 55 triples = 11

21 observations written to source-adjacent .nt files             # actually 31
```

Report-only — the `.nt` output is correct either way. It travels with the patch
because it is one character.

# Patch (tested, all three items)

```python
def resolve_root() -> Path:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chamber", help="chamber root holding observations/ (default: $CHAMBER_DIR)")
    args = ap.parse_args()
    root = args.chamber or os.environ.get("CHAMBER_DIR")
    if not root:
        sys.exit("ingest-sensors: no chamber given. Pass --chamber DIR or set CHAMBER_DIR.\n"
                 "This script reads <chamber>/observations/clinical/sensors/*; the framework "
                 "checkout has no observations/ directory.")
    p = Path(root)
    if not (p / "observations").is_dir():
        sys.exit(f"ingest-sensors: {p}/observations does not exist -- wrong chamber root?")
    return p
```

`REPO_ROOT` becomes module-level `None`, assigned from `resolve_root()` at the
top of `main()`. Plus `"Pushes": "urn:health:property:wheelchair-push-count"` in
`GARMIN_COLUMNS`, and `//10` → `//5` at `:235`.

Behaviour, measured:

| invocation | `main @ 26297a2` | patched |
|---|---|---|
| no arg, no `CHAMBER_DIR` | `0 observations`, exit 0 | error naming the variable, exit 1 |
| `--chamber` at a root with no `observations/` | n/a | error naming the path, exit 1 |
| `--chamber` at a valid chamber (2 UH days ×10 cols, 1 Garmin day ×12 cols) | `21 observations` (155 triples) | `32 observations` (160 triples) |

Removing the silent default is the substance; dropping `Path(__file__).parent.parent`
is what makes a misconfiguration impossible to mistake for an empty inbox. The
docstring and `archivist.md:182` need the flag added in the same change, or the
patch converts a silent no-op into a loud one an agent will hit on its next run.

# Negative results, recorded so they are not re-checked

- **The SOSA shape in `docs/triple-stores.md:177-183` matches the code exactly.**
  Five triples per observation, `rdf:type sosa:Observation`,
  `sosa:observedProperty`, `sosa:hasSimpleResult`^^`xsd:decimal`,
  `sosa:resultTime`^^`xsd:dateTime`, `sosa:madeBySensor` — the same five, in the
  same order, from all four extractors (`:76-82`, `:113-119`, `:165-171`,
  `:189-195`). This is the factual base under bet 1 and it holds.
- **The deployed script is byte-identical to `main`** (`diff` clean), so the
  finding is not an artifact of the 2026-07-19 image being behind.
- **The CGM deduplication is sound**: `(timestamp, record_type)` keyed, so a
  historic and a scan reading at the same minute both survive, which is what the
  Libre export means by types 0 and 1.
- **`extract_cgm` guards its own parse**: a row shorter than five fields or with
  an unparseable `%d-%m-%Y %H:%M` timestamp is skipped rather than crashing the
  run.

# Not in the issue, and why

- **N-Triples escaping.** `nt()`/`decimal()`/`dt_lit()` interpolate CSV values
  and filename stems into IRIs and literals with no escaping, so a stem
  containing a space or a value containing `"` emits invalid N-Triples. Same
  class as `drafts/qlever-dir-graph-iri-escaping.md` and
  `drafts/qlever-dir-md2ttl-escaping.md`, both already written. Belongs with
  those, not bolted onto this one.
- **Non-numeric readings typed as `xsd:decimal`.** Plausible for exports that
  write `High`/`Low` out of range, but I have no sample export and no dated
  source for the format. c188's rule: a claim about someone else's format needs
  the format, not a recollection.
- **Any framing of the `Pushes` column beyond the column mapping.** The property
  URI is quoted exactly as the framework's own public `archivist.md` states it,
  inside the twelve-row table, because that is both the accurate engineering
  report and the only version of it that says nothing about a person
  (GUARDRAILS §5). Do not headline it, and do not draw the inference.
