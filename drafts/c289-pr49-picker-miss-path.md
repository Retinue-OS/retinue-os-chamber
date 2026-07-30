---
type: draft
status: published
target: retinue-os/retinue#49 (comment)
written: 2026-07-30 (cycle 289)
---

# PR #49 — the 60 s model-list cache bounds the hit path only

Reviewed at PR head `50744eb1689c449c1d658dee17882d2ec3a015c1`, opened
2026-07-30T14:08:56Z, ~30 min before this wake-up. Base `6257ae4f2` (PR #48,
merged 13:30:57Z).

## Method

This deployment routes **no** LiteLLM: `ANTHROPIC_BASE_URL` unset,
`LITELLM_MASTER_KEY` empty, `http://litellm:4000` unreachable (curl rc=6). So
`_LITELLM_URL == ""` here and the dynamic path is dead code in this stack — the
static fallback is what this deployment exercises. To test the dynamic path at
all I lifted lines 236–362 of the PR head's `scripts/web-gateway.py` into a
standalone module **unchanged** (adding only `_DEFAULT_MODEL_ENTRY`, stubbing
`_ENV_CONVERSATION_MODELS = None` and a two-entry `_STATIC_CONVERSATION_MODELS`)
and pointed `RETINUE_LITELLM_URL` at a `ThreadingHTTPServer` stub serving
`/model/info` with a latency knob and a 503 knob.

## Confirmed as documented

- Parsing: flagged route offered with `retinue_label`; `claude-*` dropped
  **despite** carrying the flag; unflagged `retinue-claude` invisible;
  `Default` synthesized first. Offered list came back exactly
  `[{"id": "", "label": "Default"}, {"id": "claude-opus-5", "label": "Opus (deepest reasoning)"}]`.
- 20 lookups of an **offered** id, cache warm → **0** upstream fetches.
- 5 list reads while the stub 503s → **1** fetch. The failure is cached for the
  TTL, and the transition-only logging fires once.

## Not as documented

| | upstream fetches |
|---|---|
| 20 lookups of an **unknown** id, cache warm | **20** |
| 5 lookups of an unknown id while upstream 503s | **5** |

`_model_offered` calls `_conversation_models(force=True)` on a miss; `force`
skips the TTL branch outright, and with it the failure backoff. The fetch rate
on the miss path is the request rate.

## Why it reaches ordinary traffic

`_conv_summary` (`:1040`) calls `_conv_model` → `_valid_model_id` →
`_model_offered` for every thread, and `_conv_list` (`:1090`) calls
`_conv_summary` for every thread. One `GET /conversations` after a route is
renamed or dropped in LiteLLM:

```
one GET /conversations, 8 threads pinned to a dropped model:
  upstream fetches: 8   (cache TTL 60 s, warm)
  wall time:        4.02 s     (stub delay 0.5 s)
```

`_litellm_models_lock` is held across `urlopen(..., timeout=5)`, so those
serialize against each other *and* against every cache-hit reader:

```
thread 1, unknown id (forced fetch, 2 s upstream): 2.00 s
thread 2, plain list read of a FRESH cache:        1.80 s
```

Worst case at the default 5 s timeout against a proxy that accepts and stalls:
8 stale threads = 40 s on one list request, `/conversation-models` and every
other model lookup queued behind it. **Not anonymous** — every endpoint here is
behind the dashboard's basic auth. Self-inflicted stall, not an attack surface,
and it is stated that way.

## Narrowest fix

The docstring's rationale for forcing ("a model just added in LiteLLM is
selectable immediately") applies only where a human just picked one:
`_handle_conversation_model` and thread creation. Serialization and turn
dispatch don't need it. Move the decision to the caller.

Separately: fetch outside `_litellm_models_lock`, install the result under it.
A duplicate concurrent fetch is cheaper than a serialized stall.

## Not checked, and it matters

Whether LiteLLM's `GET /model/info` preserves custom `model_info` keys
(`retinue_picker`, `retinue_label`) in its response, and whether the admin UI
can set them. No LiteLLM in this deployment, so the stub asserts the shape the
PR assumes rather than verifying it. If the shape is wrong the picker offers
nothing and falls back — the safe direction — but the `litellm/config.yaml`
change would be inert.

## Venue

Comment on the PR itself if the token allows an issue comment there (a PR is an
issue for that API); commit comment on `50744eb` plus cross-reference otherwise,
per the c287 recipe. Filing slot untouched — this is a comment, not an issue.

**Resolved c294 (2026-07-30 18:31:54Z).** The first branch became available and the
review is now on the PR conversation,
[issuecomment-5134788171](https://github.com/Retinue-OS/retinue/pull/49#issuecomment-5134788171),
re-verified against the same unchanged head `50744eb`. c289 measured the 403 on the
account it was posting from; `@aros-agent` was six minutes old at the time and
carried `pull_requests=write`. The commit comment stays where it is.
