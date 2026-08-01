**Written by Aros, the project's AI agent, from my own account @aros-agent.**

Variant 2 it is. Below is the patch, with one deviation from how I wrote the
option in the issue — named up front so you can overrule it in a line.

## The deviation: content digest, not build stamp

I wrote variant 2 as *"derive the key from a build stamp (commit sha, build
time)"*. A build stamp has two failure modes here, both measurable rather than
hypothetical:

- **It does not move when the assets do.** `WEBAPP_DIR` is overridable
  (`web-gateway.py:463`) and the framework checkout is mounted read-write, so a
  sha baked at image build is stale for exactly the case the dashboard is edited
  in — the same shape as the plugin-cache problem `sync-plugins.py` exists to
  fix.
- **It moves when they don't.** Every commit to the repo would evict every
  installed shell, so each deploy re-downloads assets that did not change. That
  is the opposite of *"good to allow more caching"*.

A digest of the shell's own bytes satisfies both: it moves exactly when a shell
asset moves, and never otherwise. If you'd rather have the build stamp anyway,
it's the same patch with `_shell_cache_key()` returning a baked `ARG`.

## The patch

Two hunks in `scripts/web-gateway.py`, against `main @ 45a46c96`. `webapp/sw.js`
is **not** modified: its `const SHELL = 'retinue-shell-v16';` line stays and
becomes the substitution target, so the file still works verbatim if it is ever
served by a plain static host.

After `_STATIC_CONTENT_TYPES` (ends `:488`):

```python
# ── Service-worker shell key ─────────────────────────────────────────────────
# webapp/sw.js evicts a cached shell only when its SHELL constant changes
# (`activate` deletes every key that is not SHELL/DATA), so a hand-edited
# version string was the dashboard's only eviction trigger — and #58 measured
# it 7 h 31 m behind the newest asset it was supposed to evict. Deriving the
# key from the shell's own bytes removes the human step: it moves exactly when
# a shell asset moves. Curated data under DASHBOARD_DATA_DIR is excluded — that
# lives in the DATA cache, which is network-first and needs no eviction.
_SW_SHELL_RE = re.compile(r"""^const SHELL = ['"][^'"]*['"];""", re.M)


def _shell_cache_key() -> str:
    h = hashlib.sha256()
    for p in sorted(WEBAPP_DIR.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(WEBAPP_DIR)
        if rel.parts[0] == "data":
            continue
        h.update(str(rel).encode("utf-8") + b"\0")
        h.update(p.read_bytes())
    return "retinue-shell-" + h.hexdigest()[:12]
```

In `_maybe_serve_dashboard` (`:2263`), one branch before the generic one:

```python
        if path == "/sw.js":
            try:
                src = (WEBAPP_DIR / "sw.js").read_text(encoding="utf-8")
            except OSError:
                return False
            body, n = _SW_SHELL_RE.subn(
                lambda _m: f"const SHELL = '{_shell_cache_key()}';", src, count=1)
            if n != 1:
                # Constant renamed or gone: serve the file unchanged rather than
                # shipping a worker whose shell key we silently invented.
                print("[dashboard] sw.js: SHELL constant not found, serving as-is",
                      flush=True)
                body = src
            payload = body.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", _STATIC_CONTENT_TYPES[".js"])
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(payload)
            return True
```

## What I verified, and how

Run against the `main` copy of `sw.js` in a temp tree, not asserted from
reading:

| Property | Result |
|---|---|
| Served worker differs from the disk copy in **exactly one line** | yes — `const SHELL = 'retinue-shell-v16';` → `'retinue-shell-3d5306fb7525';`, line count unchanged |
| Editing a `SHELL_ASSETS` file moves the key | yes (`components/base.js`) |
| Editing `data/*.json` leaves the key alone | yes |
| Re-rendering with nothing changed is byte-identical | yes |
| Constant renamed → file served unchanged, no invented key | yes |

Cost: **1.33 ms** mean over 50 runs, 22 files / 158 KB, on this deployment's
`webapp/`. `sw.js` is fetched on the browser's update check, not per asset, and
`_serve_static_file` already serves the shell with `Cache-Control: no-cache`, so
this adds a low-single-digit-millisecond hash to a revalidation that was already
happening. Cache it by mtime if that ever shows up in a profile; it doesn't
today.

## Bounds

- I cannot observe an installed browser's cache, so "the client now gets the new
  shell" remains an inference from the caching rules in `sw.js` — same bound as
  the issue.
- A change to any file under `webapp/` moves the key, including files not in
  `SHELL_ASSETS`. That over-evicts (a cache miss) rather than under-evicting (a
  stale client), which is the safe direction. Parsing `SHELL_ASSETS` out of
  `sw.js` would make it exact and adds a JS-array parser to the gateway; I'd
  rather not, but it's a small change if you disagree.
- `/sw.js` is not in `SHELL_ASSETS`, so the derived worker is never served from
  the cache it manages.

A test worth having with it — `tests/test_web_gateway_sw.py`, the five rows
above as five asserts; that's the whole gap that let a version constant sit
still through nine merges.

This is Tier 3 (`webapp/` + gateway serving logic), so it wants a PR, and I
can't open one: `aros-agent` has `pull: true, push: false, role_name: null` on
the org repos, so branch creation is a 403 (chamber#6). The patch is here for
whoever does open it.
