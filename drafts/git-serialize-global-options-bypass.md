---
type: draft
title: "git-serialize.sh: `git -C <repo> commit` bypasses the lock entirely"
status: filed (retinue#37, 2026-07-26)
cycle: 182
surface: scripts/git-serialize.sh, scripts/entrypoint.sh:219-228, scripts/web-gateway.py:1878-1932
---

# The finding

`scripts/git-serialize.sh` decides whether an invocation is a write with
`case "${1:-}"` — i.e. it reads `$1` as the subcommand. Git's global options
come **before** the subcommand, so `git -C /path commit` has `$1 == "-C"`,
falls through to the `*)` arm, and is `exec`'d unserialized.

Not theoretical: `scripts/web-gateway.py` commits dashboard project edits with
exactly that form at four call sites (`:1890`, `:1892`, `:1896`, `:1899`), and
its own docstring at `:1883` says "The in-container `git` is the serializing
wrapper (git-serialize.sh), so concurrent agent commits in the same chamber
don't race." The one component the wrapper's header names as the reason it
exists ("The web gateway can run several Claude sessions at once") is the one
component whose call form the wrapper does not match.

Failure is silent by construction: `_commit_project_file` runs in a background
thread (`:1932`), the HTTP response has already been sent, and the `except`
arm prints to the gateway's stdout and returns. A losing race leaves the edit
on disk, uncommitted and unpushed, with the user told it was saved.

# Measurement

Same repo, same wrapper path, 20 parallel `git -C <repo> commit --allow-empty`,
differing only by the patch below:

| wrapper | commits landed | stderr lines |
|---|---|---|
| `main` @ `26297a2` | 5/21, 6/21 (two runs) | 28, 21 |
| patched | 21/21, 21/21 | 0, 0 |

Losses are `Another git process seems to be running in this repository` —
`.git/index.lock`, the exact race the wrapper exists to prevent.

Lock-file probe (`GIT_SERIALIZE_LOCK_DIR` pointed at an empty dir, one
invocation, count the lock files created):

| invocation | lock files, `main` | lock files, patched |
|---|---|---|
| `(cd repo && git add f)` | 1 | 1 |
| `git -C repo add f` | **0** | 1 |
| `git -c user.name=z -C repo add f` | **0** | 1 |
| `git --git-dir=… --work-tree=… add f` | **0** | 1 |
| `git -C repo status --short` | 0 | 0 (correct — read-only) |
| `git --version` | 0 | 0 |

# The second-order trap

Adding `-C` to the subcommand list is not a fix. `repo_root` is resolved by
`"$REAL_GIT" rev-parse --show-toplevel` **without** the caller's global
options, so it answers for the wrapper's own cwd — the wrong repository, or
`_global` when cwd is not a repo. Two callers writing to the same chamber
would then take two different locks, or every caller in the container would
serialize on one global lock. The options have to be split off and forwarded
to the `rev-parse` as well as to the real invocation.

# Patch (tested, above)

Insert before the existing `case`, and forward `GLOBALS` at the three
invocation sites:

```bash
GLOBALS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    -C|-c|--git-dir|--work-tree|--namespace|--exec-path|--config-env)
      GLOBALS+=("$1" "${2:-}"); shift 2 || true ;;
    --git-dir=*|--work-tree=*|--namespace=*|--exec-path=*|--config-env=*|\
    --bare|--no-replace-objects|--literal-pathspecs|--glob-pathspecs|\
    --noglob-pathspecs|--icase-pathspecs|--no-optional-locks|\
    -p|--paginate|-P|--no-pager)
      GLOBALS+=("$1"); shift ;;
    *) break ;;
  esac
done
```

`${GLOBALS[@]+"${GLOBALS[@]}"}` rather than `"${GLOBALS[@]}"` because the file
runs under `set -u`.

# Negative results, recorded so they are not re-checked

- `scripts/refresh.py:_git` builds `["git", *args]` and passes `cwd=data_dir`,
  so its `$1` *is* the subcommand. Correctly serialized. It is the only other
  Python site invoking git.
- The shim is on `PATH` before the gateway and scheduler are forked
  (`entrypoint.sh:228` vs `:321`/`:323`), so the wrapper is genuinely reached —
  the bug is in the match, not in the installation.
- Read-only commands stay unlocked under the patch, which is the property the
  header comment asks for.

# Aside, not in the patch

The header comment says "index/ref/**remote**-mutating operations", but
`remote` is not in the subcommand list, so `git remote set-url` is unserialized
even in cwd form. Mentioned in the issue, deliberately not folded into the
patch — it is a one-word change with a different argument behind it.
