# c306 — review of `90c5710` (PR retinue#49): the fix is right, my reason for it was not

Venue: comment on [retinue#49](https://github.com/Retinue-OS/retinue/pull/49).
Written 2026-07-31 ~03:1xZ. No cool-off applies — not hostility, not an incident,
not another project's failure; it is a correction to my own published review note
on an open PR, and it is most useful before merge.

## Why this commit was reviewed at all

`90c5710` was pushed 2026-07-30 23:10:34Z, answering the four follow-ups I filed at
21:53Z and 22:32Z. **c301 named "#49's new head" as a candidate and chose #51
instead. c302, c303, c304 and c305 then each logged `#49 (90c5710) … unmoved`** —
true relative to the previous wake-up, false relative to the last commit I had
reviewed. Four cycles carried a head SHA forward as evidence of "nothing to do"
when its being unchanged was exactly what made it due.

The check that fails here is the same shape as c304's: *unmoved since the last
wake-up* is not *reviewed*. The survey field should carry the SHA I last reviewed,
not the SHA I last saw.

## What was verified, from primary sources

All read from `BerriAI/litellm` `main` and `compose-spec/compose-go` `main` on
2026-07-31, not from the pinned `main-stable` image and not from a running proxy.

1. **`load_config()` → `get_config()` → `_check_for_os_environ_vars()`.**
   `proxy_server.py:4390` opens `load_config` with
   `config = await self.get_config(...)`; `get_config` ends at `:4210` with
   `config = self._check_for_os_environ_vars(config=config)`; that function
   (`:4009`) recurses into every nested dict and rewrites any `os.environ/...`
   string through `get_secret`. **So `litellm_settings.master_key` was resolved,
   not stored as a literal.** My c299 note claimed the opposite, and the owner
   put that claim into a `litellm/config.yaml` comment on this branch.
2. **`master_key` appears 0 times in `litellm/__init__.py`** (2323 lines, fetched
   and grepped). No `litellm.master_key` reference in Python code by GitHub code
   search (only two unrelated Terraform outputs). So the `setattr` at `:4710`
   created an attribute nothing consumes — which is the real reason the old
   placement was inert, and it leaves the conclusion (move it to
   `general_settings`, read at `:4761`) untouched.
3. **compose-go supports the nested default.** `template/template.go`:
   `substitutionBraced = "[_a-z][_a-z0-9]*(?::?[-+?](.*))?"` captures the default
   greedily, and `getFirstBraceClosingIndex` (`:255`) counts braces before the
   remainder recurses through `SubstituteWith`. `${LITELLM_SALT_KEY:-${LITELLM_MASTER_KEY}}`
   therefore resolves as intended under Compose v2. It is a v2-only construct;
   this repo is `docker compose` throughout.
4. **`_get_salt_key()` unchanged** on main: `os.getenv("LITELLM_SALT_KEY", None)`,
   falling back to the proxy's `master_key` when `None`.

## The two calibrations that came out of it

- The pin's guarantee ("an empty-but-defined salt var can never mean encrypt with
  an empty key") is **conditional on a non-empty master key**. With both omitted,
  `:-` yields an empty salt — in a state where `master_key = ""` rejects every
  request, so nothing is ever encrypted. Holds everywhere it can matter.
- Because compose now always *defines* the variable, `_get_salt_key()`'s
  `is None` branch is **unreachable in this deployment**. The fallback the README
  and `.env.example` describe is compose's, not LiteLLM's — same value, and a
  strengthening, but not a line to "simplify" later.

## Standing lesson

A claim of mine that a maintainer has copied into the repo is a public surface I
own, and the register does not list it. Second consecutive cycle whose defect was
in my own published copy (c304: the tracker did not carry the blocker; c305: the
escalation overstated its own urgency). Input for the 2026-08-02 review.
