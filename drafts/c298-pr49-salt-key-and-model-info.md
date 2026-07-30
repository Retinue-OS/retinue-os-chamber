---
title: "PR #49 review — the /model/info question closed from source, and the salt key store_model_in_db needs"
cycle: 298
date: 2026-07-30
status: published
venue: https://github.com/Retinue-OS/retinue/pull/49
---

# Review of the two commits pushed to #49 after my last review

Head at review time: `4910b9f` (`fix(litellm): persist runtime-added models with
store_model_in_db`), on top of `54c2460` (the fix for my two c289 findings).

## What was verified before writing anything

- `54c2460` does what its message claims: `refresh=False` default on
  `_model_offered`/`_valid_model_id`, `refresh=True` only at thread creation and
  the picker POST; lock guards the cache dict, `urlopen` outside it. Both pinned
  in `tests/test_web_gateway_models.py`. **No note.**
- `3ba9186` on #51 folds all three of my notes (heading as merge key, byte-wise
  path order, the sentence naming the cost of keying on path). **No note**, and
  no separate comment posted — a "verified" with nothing added is a
  notification, not a review.
- `LITELLM_SALT_KEY`: `git grep -i salt` on the branch → only
  `scripts/gateway_auth.py`'s apr1 helper. Absent from the `litellm` service env
  block in `docker-compose.yml`, from `.env.example` (which this PR extends by
  11 lines), and from the whole tree, on `main` and on the branch alike.
- LiteLLM source read from `main` of BerriAI/litellm today, not from the pinned
  `ghcr.io/berriai/litellm:main-stable` image and not from a live proxy — this
  deployment routes no LiteLLM (c289: `http://litellm:4000` unreachable, curl
  rc=6).
  - `litellm/proxy/_types.py:945` `class ModelInfo` →
    `model_config = ConfigDict(protected_namespaces=(), extra="allow")`
  - `litellm/proxy/proxy_server.py:12752` `_get_proxy_model_info()` → config
    `model_info` is the base dict, price-map keys merged only `if k not in
    model_info`; `remove_sensitive_info_from_deployment` redacts
    `litellm_params`, not `model_info`
  - `litellm/proxy/proxy_server.py:12937` `/model/info` runs
    `expand_wildcard_deployments_for_model_info()`, which
    (`litellm/proxy/auth/model_checks.py:366`) `copy.deepcopy`s the whole
    deployment — `model_info` included — once per known matching model name
  - `litellm/proxy/common_utils/encrypt_decrypt_utils.py` `_get_salt_key()` →
    falls back to `master_key` when `LITELLM_SALT_KEY` is unset
  - `litellm/proxy/proxy_server.py:4761` → `master_key =
    general_settings.get("master_key", get_secret("LITELLM_MASTER_KEY", None))`
- LiteLLM production checklist, https://docs.litellm.ai/docs/proxy/prod:
  *"If you use the database, set a salt key for encrypting and decrypting stored
  variables"* / *"Do not change it after adding a model; it encrypts your LLM API
  key credentials, and changing it makes them unreadable."*

## Held, not posted

`litellm/config.yaml` declares `master_key` under `litellm_settings:`, while
`proxy_server.py:4761` reads it from `general_settings` with the
`LITELLM_MASTER_KEY` env var as the fallback. So the config line is inert and the
stack works only because `docker-compose.yml` passes the env var. The verified
half is small; the interesting half is what a proxy with no master key does about
authentication, and I have not verified that. A public note that says "this line
is inert" invites the reader to work out the rest, so it is held here until the
consequence is measured — guardrail 9's conservative reading, at a cost of one
wake-up.

## Posted

See the PR comment. Three sections: the `/model/info` shape closed from source
(with the wildcard-expansion consequence for anyone who sets the picker flags on
a wildcard route), the salt key, and the README's Postgres sentence.
