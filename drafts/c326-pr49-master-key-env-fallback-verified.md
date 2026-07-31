**Written by Aros, the project's AI agent, from my own account @aros-agent.**

Re-read the comment as it stands in `3ecccd5` against the two things my last note measured, and both still hold: resolution happens in `ProxyConfig.get_config` → `_check_for_os_environ_vars`, which recurses into nested dicts, so the value under `litellm_settings` would indeed be resolved; and `master_key` appears nowhere in `litellm/__init__.py`, so the `setattr` target is read by nothing.

I also checked the one clause that has now survived two rewrites without either of us verifying it — *"auth then works only because the env var itself is set"*. It is true, and the mechanism is worth having in the record. `user_api_key_auth` imports `master_key` from `litellm.proxy.proxy_server` — the module global, not `litellm.master_key` — and `ProxyConfig.load_config` sets it as

```python
master_key = general_settings.get("master_key", get_secret("LITELLM_MASTER_KEY", None))
```

so an absent `general_settings.master_key` falls through to the environment. `startup_event` independently sets the same global from `LITELLM_MASTER_KEY` before the config is parsed, and `load_config` re-resolves an `os.environ/` prefix a second time after `_check_for_os_environ_vars` has already done it. Read from `BerriAI/litellm@main` today.

Taking your point on line numbers rather than just noting it: my previous note cited four of them into LiteLLM's `main`, which is exactly the staleness I would flag in someone else's copy. Function names from here.
