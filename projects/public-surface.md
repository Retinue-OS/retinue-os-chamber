---
type: project
id: proj-public-surface
title: "The project's public surfaces say what the project is"
goal: "Anyone landing on the org, a repo, or the docs site learns what Retinue is and what it isn't, without opening a source file."
goal_status: not_achieved
current_next_action: "Aros, c224 (2026-07-28 18:5xZ): the c223 briefing-freshness check ran for the first time and passed - docs/data/briefing.json stamped 17:54:59Z, 53 minutes old, all five files on one stamp. Then the drain, which three cycles had reported empty on the grounds that main is unmoved at 26297a2: that inference needs each held write-up's own baseline, and two of the four named no commit at all. Re-measured both against retinue-os/retinue @ 26297a2 from the GitHub API, because the local checkout could not answer it - its gitdir is unmounted, which is the condition retinue#32 describes, filed three days ago and never noticed while standing in it. Both reproduce in full: the base compose has zero labels keys while deploy/traefik/README.md:49 says the service's labels already reference the mTLS middlewares, and the updater still returns 202 started from a daemon thread with no caller polling - the route table settling the third fact, since /status is a sibling of /update and not a child. One clause tightened before filing: the example router line is commented out, so the filed wording says the router the docs tell an operator to uncomment. A sentence that invites a correct rebuttal costs the issue its credibility on first reading. Ranking checked against c219 and upheld - w3id keeps the 06:0xZ slot, because owner-action names two populations, needs-legal-personhood and needs-a-permission-I-lack, and is therefore not the predictor the naive reading treats it as. Verified free on the side: the store carries this file's c223 frontmatter, so aros-store-refresh still delivers - which needed checking because the scheduler reports it [ok] in 0s and what exits 0 is the cp, not the reindex, the updater draft's own shape one flight down. Held queue unchanged at 4. Earlier note - Aros, c223 (2026-07-28 18:1xZ): read scheduler.log for the durations of aros-dashboard-refresh, the job that maintains this project's only self-updating public page - c192 made that log a register surface and 31 cycles asked it about one job only. Today's run finished in 875 s against the 900 s SCHEDULER_JOB_TIMEOUT, 97.2%, and the job has already failed twice (2026-07-21 on a 429 spend limit, 2026-07-23 on an API error), each leaving the page 48 h stale with no record anywhere - the stamp stayed honest, which is why nobody noticed. Measured before cutting anything: the briefing prose is not the driver (5823 chars today against 7742 yesterday), so nothing was trimmed on a theory. Fixed what holds under either cause - the cold dispatch now carries c192's commit-before-the-last-third rule inline with a 600 s commit point, which is c212's finding a second time in the same prompt, and aros-tick now checks the generated stamp every 30 min so a missed daily run is caught in half an hour. Earlier note - Aros, c219 (2026-07-28 15:3xZ): the owner commented on retinue#25 at 13:59:34Z, the first human action in the org in 2 d 21 h, so aros-tick is restored to 1800 s on the c154 trigger. Classifying ten days of tracker activity by author showed my own AI-disclosure line is four strings rather than one: guardrail 1 holds everywhere, every form discloses, but the c179 published matcher fails in both directions the moment it is pointed at comments, which this cycle demonstrated twice in ten minutes. Issue reading unaffected at 39 under either pattern, which is why it survived seven cycles. One standard sentence adopted forward, historical alternation recorded in strategy.md. With the classification corrected: 11 human actions in the trackers over ten days, 10 product and 1 presence, against 6 owner-action issues aged 8-10 days - not an escalation and pushed nowhere, but recorded as an input to the 2026-08-02 review, whose question is now which parts of reachable presence need nothing from him. Also probed POST /orgs/retinue-os/repos with no payload, so a success could create nothing: 403, so chamber#4 holds and the org profile README stays his. Earlier note - Aros, c218 (2026-07-28 12:2xZ): re-read the two public surfaces that describe the store-refresh mechanism I shipped at c213/c214, and both were stale within 24 h of my own fix. The live Pages README at docs/examples/provenance/ said Markdown reaches the store only at container restart or a human poke, 'not otherwise'; aros-store-refresh has poked it hourly since 27 July. Corrected there and in writing/provenance-by-path.md, with delivery measured rather than config quoted: no container restart in 8 d 18 h, job [ok] at 09:17/10:17/11:17Z, an edit written at 09:16Z queryable at 12:2xZ - so the new stated bound is within one hour, worst case, not 'not otherwise'. The finding is not softened: qlever-dir#3 is still open, a Markdown-only chamber with no .nt file and no such job is still never indexed, and the automation adds a second silent-failure point, which both pages now say. Rule taken from it: a shipped fix is a scheduled re-read of every surface that describes what it fixed, due the same day - c214 verified the job worked and never asked which sentences it had falsified."
```

— in Turtle, a literal backslash followed by a quote. `strip_quotes()` removed
the wrapping quotes of a YAML double-quoted scalar and returned the body
verbatim, so every escape survived into the literal and `ttl_string()` then
escaped the backslash again. The store's copy of a value would disagree with the
file it is derived from, silently, with no parse error anywhere.

Scope, stated because a claim's scope is part of it (c176): **no project file in
this chamber currently contains an escape**, so nothing in the live store is
wrong today — I avoided the trap by rewriting my own sentence, which is exactly
how a defect like this stays invisible. It is not a qlever-dir bug either; the
converter is chamber content, shipped by me, and `qlever-dir#6` is about the
*upstream* `md2ttl.py`'s IRI and typed-literal handling, a different function in
a different repository.

Fixed the same cycle, since the file is mine and needs no permission:
`strip_quotes()` now undoes `\"`, `\\`, `\/`, `\n`, `\t`, `\r` for
double-quoted scalars and `''` for single-quoted ones, leaving `\uXXXX` and
other YAML exotica to pass through visibly rather than silently; `ttl_string()`
now also escapes CR and TAB, a raw CR being illegal inside a Turtle quoted
literal in the first place. Checked two ways: a fixture covering all six
sequences round-trips correctly, and the converter's output over the six real
project files is **byte-identical** to the previous version's, so the fix is
inert on current data and only changes the case that was wrong.

The through-line with the first finding is the same one: this chamber is the
project's worked example of the converter contract, so both its prose about the
mechanism and its implementation of it are public surfaces, and neither gets
re-read by anyone who is not me.

## c219 (2026-07-28) — the disclosure line is a matcher, and it is four strings

**The trigger was an easy question.** The owner commented on retinue#25 at
13:59:34Z — the first human action in the org in 2 d 21 h — so I went to classify
ten days of tracker activity by author. We post from the same GitHub account
(chamber#3), so GitHub's own metadata cannot separate us; guardrail 1's disclosure
sentence is the only authorship record either of us has, a fact c176 recorded and
c179 turned into a published, re-runnable command.

**Both directions, inside ten minutes.** A loose `test("Aros")` classified the
owner's qlever-dir#8 comment as mine, because he wrote *"Aros' solution is
easier"*. The strict c179 pattern then classified three of my own comments as his
— retinue#1 and qlever-dir#3 (2026-07-19) and chamber#6 (2026-07-20). All three do
disclose; they disclose in words I chose that day:

| Form | Where |
|---|---|
| `**Written by Aros, the project's AI agent, from the owner's GitHub account…**` | every issue body I have filed; most comments |
| `**Filed by Aros…**` | a few early issue bodies |
| `— Aros (AI agent; I maintain the project's public-facing chamber and filed this issue)` | comments on retinue#1, qlever-dir#3 |
| `— Aros, the project's AI agent…` / `**Correction from Aros, the project's AI agent.**` | comments on chamber#1, chamber#6 |

**Guardrail 1 is fine; the instrument is not.** Every comment discloses, so no
reader was ever misled — this is a measurement defect. It survived seven cycles
because the number it feeds is the *issue* count, and every issue body I filed
happens to use one of the first two forms: **39 under either pattern.** The defect
is only reachable by pointing the method at comments, which is what a question
about someone else's activity requires and what nobody had asked.

Fixed forward: one standard sentence for issues and comments alike, and the
historical alternation written into `strategy.md` so the archive stays countable.
The lesson is c179's, in a fourth venue — **a proxy is a claim**, and guardrail 3
binds my instruments before it binds the project's copy.

**Second finding, and it is the one that matters for the review.** With the
classification corrected, ten days of trackers read: **11 human actions, 10 of
them product or design, 1 presence** (chamber#1, *"Nostr Should also be
considered"*, day one). Six `owner-action` issues are open at ages 8–10 days.
Nothing here is overdue and none of it was pushed anywhere — the c27 clock rule
holds, and at 34 hours this was not a measurement, while at ten days of near-daily
activity it is. The consequence is for the 2026-08-02 review and is stated in
`strategy.md`: the phase-exit condition is composed entirely of the category he
demonstrably defers, so the review's question is *which parts of reachable
presence need nothing from him*, not how to get the accounts moved.

**Third, and the probe I wanted to fail.** chamber#4 justifies itself with
*"creating a repository under the org … is org administration (guardrail 7)"* and
cites a `PATCH /repos/…` 403 as evidence — a different endpoint, which is the
c176/c217 shape. Guardrail 7's list is exhaustive and *creating* a repo is not on
it, so if the token could do it, `retinue-os/.github` and the finished
`writing/org-profile-README.md` were mine to deliver today, and the org's
most-read surface would have stopped being blank. Probed with **no payload at
all**, so authorization answers before validation and a success creates nothing:
`POST /orgs/retinue-os/repos` → **403, Resource not accessible by personal access
token.** The claim holds. Fifth distinct endpoint behind the one missing
permission at chamber#6, and nothing posted — a confirmation is owed to the
record, a correction would have been owed to the issue the same minute (c217).

## c220 (2026-07-28) — 220 cycles of auditing what the links *say*, none of what they *reach*

The register has audited the prose of `writing/provenance-by-path.md` at least
four times — its claims, its dates, its re-run outputs, and at c218 the sentence
a fix of mine had falsified. Nobody had ever asked whether its links resolve.
Same for `writing/egress-audit-observes.md` and for `docs/index.html`, the live
landing page. Link integrity is a different property from prose accuracy, it
fails silently, and it fails *outward* — the reader finds it, not the writer.

Run this cycle over every absolute URL in the three surfaces, following
redirects: **25 URLs, 24 return 200.**

The one failure is not link rot in someone else's site. It is the project's own
vocabulary namespace:

| Probe | Result |
|---|---|
| `https://w3id.org/retinue/` | **404** |
| `https://w3id.org/retinue/project` | **404** |
| `https://w3id.org/retinue/kb` | **404** |
| `https://w3id.org/` (control) | 200 |
| `api.github.com/repos/perma-id/w3id.org/contents/retinue` | **404** — no directory |

`https://w3id.org/retinue/project#` and `…/kb#` are not documentation strings.
They are constants in running code in three repositories — `scripts/web-gateway.py:1500`,
`qlever-dir/examples/projects/.qlever/md2ttl.py:21`, this chamber's
`projects/.qlever/md2ttl.py:21` — plus `docs/triple-stores.md:112`,
`writing/provenance-by-path.md:12` and `writing/org-profile-README.md:129`.
Every project record this chamber emits carries one.

**Sized honestly, because guardrail 3 has an understating direction too.**
Nothing is broken. RDF has never required an IRI to dereference; no query fails
and no deployment is affected. What is lost is the only thing w3id.org sells:
it is a redirection switchboard run by the W3C Permanent Identifier Community
Group, and choosing it over a domain you control is a deliberate bid for
permanence. Unregistered, it delivers less than a plain GitHub Pages URL, which
at least resolves. And the string is unreserved — registration is a PR adding a
`retinue/` directory, nothing holds the name until someone files it, and every
document shipping the prefix raises the cost of moving off it.

**The audience argument is bet 1's, exactly.** The semantic-web readers this
project is aimed at are the population that dereferences a namespace IRI. It is
the cheapest available reason to be dismissed by the one group the strategy
says to lead with.

**Split by who can act, which is the part worth recording as a habit.** The
finding has two halves and only one of them waits:

- *The published claim* is mine and was fixed the same cycle — a paragraph in
  `writing/provenance-by-path.md` naming the 404, the date it was measured, and
  the first-come risk. Guardrail 3 does not wait for a filing slot.
- *The remedy* is a PR to a third party's repository claiming a permanent
  identifier in the project's name with a maintenance contact attached. I cannot
  open PRs anywhere (re-probed this cycle: `POST /repos/retinue-os/retinue/pulls`,
  no payload → **403**, chamber#6 still accurate), and an identifier commitment
  is guardrail 7's territory regardless of the token. Written up in
  `drafts/w3id-namespace-unregistered.md` with the three redirect options, a
  paste-ready `.htaccess`, and what happens if he does nothing. **Held** — the
  c184 slot went to retinue#40 at 06:05Z — and **ranked first** for the next
  one, ahead of the three findings held before it.

The generalizable check, now in the register: **an audit of a document's claims
is not an audit of its links.** One is about what the text asserts, the other
about what it delivers, and this chamber has repeatedly found that *written is
not delivered* (c163, c201, c206). This is the same distinction pointed at a
surface where it costs one `curl` per URL to test.

## c221 (2026-07-28) — "not registered" and "not claimed" are different probes, and only one had been run

Short wake-up. Nothing external moved in the 13 minutes since c220: last human
action in the org is still the owner's retinue#25 comment at 13:59:34Z, 0 stars,
0 forks, 0 non-me issues, no open PRs, `main` unmoved at `26297a2`. The c184
filing slot is spent until 2026-07-29T06:0xZ and the c206 drain rule binds at
three held items, so the admissible work was drain, and drain's second clause is
**re-verify before filing**.

Applied it to the item ranked first for tomorrow's slot,
`drafts/w3id-namespace-unregistered.md`, and the re-verification found a real gap
in my own evidence rather than confirming it.

**The gap.** c220 established the namespace is unregistered from
`api.github.com/repos/perma-id/w3id.org/contents/retinue` → 404, and then wrote
*"It is not squatted by anyone else either."* Those are two different claims. The
`contents` endpoint reads the default branch, so it answers **is it merged**; the
issue's load-bearing sentence — the name is first-come and still available, so
the switching cost only rises — is about whether anyone is **in the process of
taking it**, and a registration in flight is an open pull request. c220 never
looked at the pull requests. The conclusion happened to be right; the probe did
not test it.

**Measured this cycle (16:5xZ):**

| Probe | Result |
|---|---|
| PRs on `perma-id/w3id.org` matching `retinue`, any state | **0** |
| Issues on `perma-id/w3id.org` matching `retinue`, any state | **0** |
| Open PRs on that repo, total | 27 (newest 6451, 2026-07-28T15:53Z) |

So the name is free in the stronger sense, and the issue can now say so on
evidence.

**A second thing fell out, and it changes the shape of the ask.** The draft told
the owner to open a PR against a W3C community group's repository, which reads
heavier than it is. Over the 40 most recently merged PRs there: **median
open→merge 3.9 h**, 27/40 inside 24 h, 34/40 inside 72 h, slowest 101 h, most
recent merge 2026-07-27. It is a same-day PR against an actively maintained
registry, not a standards process. The size of an ask is part of the ask, and I
had left him to guess it.

**What did not change, stated because the temptation ran the other way.** Not
filed — the slot is spent and this is not the urgent-defect exemption. Not made
more urgent: a fast merge queue is a property of the *remedy*, not of the risk,
and the name has been unclaimed for the project's entire life. Ranking unchanged.
Nothing pushed to the dashboard (nine agent threads unread; c201 allows one open,
and nothing here needs a decision inside a day). Nothing re-escalated.

**The check this adds to the register**, and it is c179's shape pointed at
someone else's repository: *a probe is a claim about a state, and a state has a
branch.* An endpoint that reads `main` cannot answer a question about what is
pending. Where a finding's urgency rests on "nobody else has done this yet", the
open-PR list is the surface that answers it, not the file tree.

## c223 (2026-07-28) — the job that keeps the public dashboard honest is 25 seconds from being killed

Measured 2026-07-28 18:10–18:15Z from `/root/.retinue/scheduler/scheduler.log`
and this repo's git history. The dashboard-refresh job had just finished, 30 s
before this wake-up started.

**Every dispatch of `aros-dashboard-refresh` since it was created:**

| Date | Result |
|---|---|
| 2026-07-20 | `[ok] in 253s` |
| 2026-07-21 | `[fail] rc=1 in 3s` — HTTP 429, monthly spend limit |
| 2026-07-22 | `[ok] in 323s` |
| 2026-07-23 | `[fail] rc=1 in 33s` — API error, zero tokens used |
| 2026-07-24 | `[ok] in 467s` |
| 2026-07-25 | `[ok] in 727s` |
| 2026-07-26 | `[ok] in 519s` |
| 2026-07-27 | `[ok] in 566s` |
| 2026-07-28 | `[ok] in 875s` |

`SCHEDULER_JOB_TIMEOUT` is unset in this deployment, so it is the 900 s default
(`scripts/scheduler.py:52`, and the daemon's own start line prints
`timeout=900s`). **875 of 900 is 97.2%.** No dashboard-refresh dispatch has been
killed yet; four `aros-tick` dispatches have been, which is the mechanism c192
documented for the other job.

**The two failures were not theoretical and their cost is measurable.** The
regeneration commits once, at the end, so a failed run leaves the working tree
clean and the page exactly as it was. `git log -- docs/data/briefing.json` shows
the consequence: nothing between 2026-07-20 17:04 and 2026-07-22 17:11, and
nothing between 2026-07-22 17:11 and 2026-07-24 17:19. **Two 48-hour gaps on the
project's only self-updating public page, and no record of either exists in
`log.md`, in this file, or anywhere a reader could see.** The stamp on the page
stayed honest — it said the day it was generated — which is precisely why nobody
noticed: an honest stale page and a fresh page look the same to anyone not doing
the arithmetic.

**What I did not do, and why.** The obvious move was to trim the job's output on
the theory that the briefing prose grows with the owner's desk (11 items now,
each with a computed absolute age). I measured before cutting, and the theory is
wrong: briefing text across generations runs 1962 → 3430 → 4548 → 8084 → 7764 →
7011 → 7075 → 7742 → **5823**, and today's — the 875 s run — is the *second
smallest of the last six*. Whatever drives the duration, it is the measuring and
not the writing. c221's rule applied to my own remedy: a probe is a claim, and
so is a diagnosis.

**Two fixes, both certain under either cause, both inside this chamber.**

1. **The deadline is now in the prompt itself.** c192's standing rule — *commit
   and push before the wake-up's last third, because a kill destroys everything
   uncommitted* — is a subsection of an 84 KB `strategy.md`. Its prompt now names
   the timeout, sets a 600 s commit point, and says what to do if the
   measurements are not finished by then (commit five files from one consistent,
   narrower stamp rather than lose the run).

   **Correction, made in the same wake-up, before the second pickup and after
   the commit above went out.** The paragraph here first read that the rule "was
   written into `strategy.md`, which `aros-tick` reads and which this job is
   never told to open". That is false and I could have checked it in one command.
   `.retinue/agents/aros.md` — the definition every dispatch of this subagent
   receives, whatever the dispatching prompt says — instructs at step 2: *Read
   `strategy.md`*. So the rule is reachable from this job and always has been.
   What is measurable is weaker and is the part that stands: nine runs never
   applied it, and the durations grew to 97% of the wall. Whether it was read and
   not applied, or never reached in an 84 KB file, I cannot tell from the
   evidence, and the fix is the same either way. The false version is the more
   flattering one — it makes the defect structural rather than mine — which is
   the c163 shape pointed at a justification instead of at a measure. Guardrail 3
   before it is anyone else's copy.
2. **A missed run is detected in 30 minutes instead of 24 hours.** `aros-tick`
   runs 48x more often than the refresh; its prompt now includes reading the
   `generated` stamp in `docs/data/briefing.json` and, if it is more than 26 h
   old, spending that wake-up on the regeneration and recording the miss. 26 h
   rather than 24 h so that a run which merely started late does not trip it.

**The general lesson, which is c145's with the noun changed.** c145: *a public
artifact can fail silently by growing.* c190 generalized it from `log.md` to
every append-only file. This is the same failure one level out — **a public
artifact can fail silently because the job that maintains it did**, and the job's
own success is a surface with no reader. `scheduler.log` has been a register
surface since c192; in the 31 cycles since, it was asked about exactly one job,
the one it was added for.

Not filed as an issue anywhere: the manifest, the prompts and the dashboard are
all this chamber's, so this is a fix rather than a report, and the c184 filing
slot (spent until 2026-07-29T06:0xZ) does not apply to work I do myself.

## §c224 — the drain was reported empty from a commit hash that two of the four held write-ups never named

2026-07-28 18:4x–19:0xZ. Survey clean: 0 stars, 0 forks, 0 watchers on all four
public repos since 2026-07-18; 47 issues, no PRs, no discussions; the last human
action anywhere in the org is still the owner's comment on retinue#25 at
13:59:34Z, so the re-slow bound holds at 2026-07-29T13:59:34Z. `briefing.json`
stamped 2026-07-28T17:54:59Z, **53 minutes old** — the c223 freshness check ran
for the first time and passed, which is the first evidence that yesterday's fix
works from the consumer side.

**The finding is in my own reporting, not in the framework.** c219, c222 and c223
each closed with "drain empty this cycle, `main` unmoved at `26297a2`". That
inference is only sound if every held write-up was measured *at or after*
`26297a2`. Checked this cycle for the first time:

| Held write-up | Baseline recorded before today |
|---|---|
| `w3id-namespace-unregistered.md` | live probes, re-verified c221 |
| `webapp-manifest-german-description.md` | `26297a2`, stated |
| `traefik-readme-labels-already.md` | **none** |
| `updater-reports-dispatch-not-result.md` | **none** |

Half the queue was being carried by a hash it never cited. The dates happen to
acquit both — c198 and c206 are after 2026-07-25T15:12:01Z — but that is luck
reconstructed afterwards, not a measurement, and it is c179's lesson in a fourth
venue: **a proxy is a claim.**

**Re-measured both, from the GitHub API rather than the local checkout** (whose
gitdir is unmounted, the condition retinue#32 describes — so the local tree could
not have answered this question at all, and no cycle had noticed that either).
Both reproduce in full at `26297a2`: the base compose has **zero** `labels:` keys
and zero mentions of `retinue-mtls@file` while `deploy/traefik/README.md:49` says
the service's labels already reference them; and the updater still returns
`202 {"status": "started"}` from a daemon thread, `self-update.py` still issues no
second request, and the route table confirms `/status` is a **sibling** of
`/update` rather than a child, so `PathPrefix('/update')` cannot reach it.

One clause tightened before either is filed: the updater draft called
`docker-compose.override.example.yml:74` "the only public router the project
ships". It is commented out — the router an operator uncomments. The finding is
untouched, but the sentence as written invites a correction that would cost the
issue its credibility on first reading, and the filed wording now says *"the
example router the docs tell an operator to uncomment"*.

**Ranking checked against c219 and upheld.** c219's measurement (10 of 11 human
tracker actions are product/design; 1 is presence; 6 `owner-action` issues aged
8–10 days) reads at first as an argument to demote `w3id` — a seventh item into
the category that has never drained. It fails on the label: `owner-action`
conflates *needs legal personhood* (chamber#1/#3/#4) with *needs a permission I
lack* (chamber#5/#6/#7), and `w3id` is a product decision wearing the second.
Recorded as an instrument defect for the 2026-08-02 review — the label is not a
predictor, because it names two populations — and not acted on, since relabelling
six issues to tidy my own arithmetic is churn on someone else's desk.

Also verified, at no cost, because it is the other half of c218's rule: the life
store's copy of this file's frontmatter carries c223's `currentNextAction`,
written ~30 minutes earlier, so `aros-store-refresh` is still delivering. The
scheduler reports that job `[ok] in 0s` on every run, which reports the `cp && mv`
exiting 0 and not the reindex happening — the same *dispatch-not-result* shape as
the updater draft, one flight down. Worth knowing that the only check that
distinguishes them is a SPARQL query, and that it is cheap.

Not filed as an issue: the c184 slot is spent until 2026-07-29T06:0xZ, and the
reporting defect is mine rather than the framework's. Held queue unchanged at 4.
