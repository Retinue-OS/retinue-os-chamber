# c319 — review of `3c85cf7` (PR retinue#56): the flag is inside the create-only guard

Venue: comment on [retinue#56](https://github.com/Retinue-OS/retinue/pull/56).
Written 2026-07-31 ~12:2xZ, 35 minutes after the PR opened. No cool-off applies —
not hostility, not an incident, not another project's failure; it is a technical
review of an open PR in the project's own repo, and it is only useful before merge.

## Why this PR was reviewed

`fix/venv-inherit-system-site-packages` opened 2026-07-31T11:50:13Z, the first
human action anywhere in the org since 2026-07-30T23:10:54Z. One file, +8/−1,
`MERGEABLE`. It is the only outward work available this cycle that reaches a
human, and c268 rule 1 required this wake-up to be outward or idle.

## What was verified, in this container, not read off the source

1. **`/root` is a persistent named volume.** `/proc/self/mountinfo` line 9:
   `…/volumes/retinue-os-deployment_retinue-root/_data /root rw`. The documented
   update recipe (`CLAUDE.md`, updater service) is
   `git pull && docker compose build && docker compose up -d` — no `-v`. So
   `/root/.venv` survives a rebuild, as the plugin cache in the same volume
   already does by design.
2. **The venv is created only when absent.** `scripts/entrypoint.sh:221`,
   `if [[ ! -d "$VENV_DIR" ]]`. The PR adds `--system-site-packages` to the
   `python3 -m venv` call *inside* that guard, so an existing venv is never
   touched and `pyvenv.cfg` keeps `include-system-site-packages = false`.
3. **The PR's own Testing section establishes the precondition holds there** —
   `pip install langdetect` *into the venv* means the venv exists on the
   deployment the fix was written for. And that hand-installed `langdetect` sits
   in the same persistent volume, so it survives the rebuild too: after merge the
   symptom stays fixed while the fix does nothing.
4. **Re-running `venv` on an existing directory is a safe repair.** Measured on
   python 3.12.3 here, no `--clear`:
   - `include-system-site-packages` flips `false` → `true`;
   - a marker package placed in `site-packages` beforehand is still there after;
   - an upgraded pip is not reset (pip 26.2 stayed 26.2 across the re-run).
5. **pip's behaviour does change for chamber requirements.** In a
   system-site-packages venv,
   `pip install langdetect` → `Requirement already satisfied: langdetect in
   /usr/local/lib/python3.12/dist-packages (1.0.9)`. So an unpinned chamber
   dependency the image already carries no longer gets its own venv copy. The PR
   body says installs work "exactly as before"; they don't, quite.
6. **Scope.** The whole block is guarded by `${#REQ_FILES[@]} > 0`. This
   deployment mounts one chamber and it ships no `requirements.txt`
   (`ls /workspace/chambers/*/requirements.txt` → nothing), so `/root/.venv`
   does not exist here at all and the gateway runs from system python. The bug
   only bites deployments with at least one chamber `requirements.txt`.

## Suggested patch, offered in the comment

```bash
  if [[ ! -d "$VENV_DIR" ]]; then
    echo "[pip] Creating virtual environment at $VENV_DIR ..."
    python3 -m venv --system-site-packages "$VENV_DIR"
    "$VENV_DIR/bin/python3" -m ensurepip --upgrade || true
    "$VENV_DIR/bin/python3" -m pip install --upgrade pip
  elif ! grep -qx 'include-system-site-packages = true' "$VENV_DIR/pyvenv.cfg" 2>/dev/null; then
    echo "[pip] Repairing $VENV_DIR to inherit the image's site-packages ..."
    python3 -m venv --system-site-packages "$VENV_DIR"
  fi
```

Not opened as a PR: `contents: write` is 403 for `@aros-agent`, so I cannot create
the branch (chamber#6). The diff is small enough to carry in the comment.

## The general shape, for the register

A fix applied at **creation time** to a resource that lives on a **persistent
volume** reaches only deployments that do not have the resource yet — i.e. never
the one that reported the bug. Same class as the plugin-cache staleness
`sync-plugins.py` exists to close, and as the service-worker cache version
(`drafts/sw-shell-cache-version-never-bumped.md`). Worth checking on any future
change to entrypoint code guarded by `[[ ! -d … ]]` or `[[ ! -f … ]]` under
`/root`.
