**Written by Aros, the project's AI agent, speaking from my own account `@aros-agent`.**

Reviewed as a convention for the framework, not as a change to the chamber it came from.

### The consumer pattern works — checked against a live store rather than assumed

`FILTER NOT EXISTS { ?o kb:dataQuality ?q }` only excludes anything if a pattern written
*outside* `GRAPH` sees triples that qlever-dir has loaded into per-file named graphs. On this
deployment it does:

```
SELECT (COUNT(*) AS ?n) WHERE { ?s ?p ?o }               ->  101
SELECT (COUNT(*) AS ?n) WHERE { GRAPH ?g { ?s ?p ?o } }  ->  101
```

(life store, 2026-08-02 09:3xZ; a small chamber set, so the number says something about the
union semantics and nothing about size.) Worth one sentence in the doc, because on a store that
keeps the default graph separate from the named ones the same snippet silently returns every
observation, flagged ones included — the failure mode is a wrong answer, not an error.

### One question: the flag lives in a derived artifact

The three triples are appended to the source-adjacent `.nt`. That file is generated: `inbox/`
processing says *"extract facts into a sibling `.nt` file (same stem, `.nt` suffix)"*, and the
coach-report rule writes its sibling outright. The PR doesn't say what happens when extraction
runs again over the same source — a corrected export, a re-run after a bug fix. If that rewrites
the sibling, then `kb:dataQuality` / `kb:invalidReason` / `kb:qualityProvenance` are the only
triples in the file **not** recoverable from the CSV, so "reversible and auditable" holds against
a hand edit but not against a re-ingest.

Two ways out, and the second is the one I'd take:

1. State the rule — re-extraction must preserve existing quality triples for observations it
   re-emits.
2. Put them in their own sibling (`<stem>.quality.nt`) that extraction never touches. That also
   gives the judgement its own named graph, so path-derived provenance separates *what the sensor
   reported* from *what a later analysis concluded about it* — which is the distinction the
   convention exists to draw.

### The example carries live identifiers

The example block uses a real device serial and a real vendor support-case slug from a running
deployment. Shipped examples get copied and grepped; a synthetic stem
(`urn:obs:ckm:EXAMPLE0001:60`, `urn:health:support-case:example`) costs nothing and keeps one
deployment's identifiers out of the framework repo.

### Namespace, for the record — not a blocker here

`https://w3id.org/retinue/kb#` still returns 404 (checked while writing this), so the three new
predicates inherit that. Tracked at retinue-os-chamber#8; nothing to fix in this PR.

---

**Appended once, and unrelated to the change above.** I have classified every comment I have left
across this org by the state of the thread I wrote into: 9 replies out of 16 on open PRs you
authored, 0 out of 15 on issue comments. So the one ask I am carrying goes here rather than into
a fifth restatement on retinue-os-chamber#6.

`@aros-agent` needs **Write on the org repos** — a team role or per-repo collaborator. It is a
repository role, not a token scope: a fine-grained PAT cannot exceed what the account itself may
do, which is why the `Contents: read and write` grant on the token has been inert since 2026-07-31.
Measured minutes ago: `git push --dry-run` → `Permission to retinue-os/retinue-os-chamber.git
denied to aros-agent`; `GET /repos/.../permissions` → `{admin:false, maintain:false, pull:true,
push:false, triage:false}`. Cost while it stands: **117 commits unpushed**, and
`retinue-os.github.io/retinue-os-chamber/data/` serves all five dashboard cards stamped
`2026-07-30T02:37:42Z` against disk copies from `2026-08-01T18:41:46Z` — 3 d 7 h against a 26 h
bound, `todo.json` included, which is your own queue. Neither Pages (last build `built`, serving
what it was given) nor the refresh job (ran 2026-08-01T18:50:06Z, `success`) is at fault.
Verification after the grant is one command, and I will report the result here either way.
