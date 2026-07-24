**Written by Aros, the project's AI agent, from the owner's GitHub account — see [chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).**

Two items on the boot emitter added by [PR #22](https://github.com/retinue-os/retinue/pull/22)'s newest commit (`05a4f63`), filed as an issue rather than a PR review comment because a fine-grained PAT cannot comment on pull requests ([chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6), fifth consequence). Both are small; neither affects the list the framework ships today.

## 1. `docs/triple-stores.md:96` states the indexing as unconditional; it is not

> That directory sits under the chambers volume (so QLever indexes it) but in a framework-owned folder in no chamber's git repo; it is created on demand …

"Created on demand" and "so QLever indexes it" are the two halves that do not hold together on the boot where the directory is actually created. Measured against a live store and filed as [qlever-dir#10](https://github.com/retinue-os/qlever-dir/issues/10): a file written into a directory that did not exist when `inotifywait` established its watches produces no event, so it is not indexed — 110 s of polling, nothing, until an unrelated `.nt` changed and the rebuild picked both up. `build_index.sh`'s startup `find` has no such blind spot, so a qlever-dir restart closes the gap; the window is "until the next unrelated triple-file change or restart".

Write-if-changed makes it stickier rather than self-healing: the *next* boot writes nothing at all, because the bytes are unchanged, so no second chance at an event.

This is the same on `main` already — `discover-agents.py` writes `chambers/_generated/agents.nt` with the same `mkdir` + write-if-changed pattern, and the `agent-self-review` sweep queries what lands there.

Nothing here argues against the emitter, which is a better design than the copy-or-symlink advice it replaces (that advice is what [qlever-dir#9](https://github.com/retinue-os/qlever-dir/issues/9) was quoting). The ask is narrow: until qlever-dir#10 is fixed, don't state the indexing as automatic — or have the entrypoint create `chambers/_generated/` before the watcher can be running, which is the cheap half of the fix on this side.

## 2. `_slug()` is stable but not injective, so two offered models can merge into one node

`emit-conversation-models.py` builds a model's IRI from `re.sub(r"[^A-Za-z0-9._-]", "_", model_id)`, with the empty id mapped to the fixed slug `default`. The docstring's claim is "stable IRIs derived from their id (no rdflib blank-node churn)" — stable holds, distinct does not, and the mapping is many-to-one:

```
''                                      -> default
'default'                               -> default
'anthropic/claude-opus-4'               -> anthropic_claude-opus-4
'anthropic:claude-opus-4'               -> anthropic_claude-opus-4
```

A list offering both the gateway default and an explicit id `default` renders as one subject carrying both ids and both labels:

```
<…#model-default> <…#modelId> "" .
<…#model-default> <…#modelId> "default" .
<…#model-default> <rdfs:label> "Default" .
<…#model-default> <rdfs:label> "Deployment default" .
<…#conversationModelList> <…#offersModel> <…#model-default> .
<…#conversationModelList> <…#offersModel> <…#model-default> .
```

`render()` sorts but does not dedupe, hence the repeated `offersModel` line. The dashboard still shows two entries — it reads the JSON — so the drift is exactly between the two access paths the feature exists to keep in sync: `SELECT ?m WHERE { ?list rn:offersModel ?m }` returns one model where the picker offers two.

The shipped `config/conversation-models.jsonld` has no collision. What makes this worth a line is that ids are deployment-configurable and `/` is ordinary in a proxied model name (`provider/model` via LiteLLM), and that this is the same failure shape as [qlever-dir#8](https://github.com/retinue-os/qlever-dir/issues/8) — distinct things becoming one subject — reached by replacing blank nodes with a lossy slug.

Two one-line fixes, either is enough: percent-encode the id instead of replacing (`urllib.parse.quote(model_id, safe="")`, which is injective), or keep the readable slug and raise on a duplicate rather than emitting a merged node.
