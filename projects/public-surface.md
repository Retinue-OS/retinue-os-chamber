---
type: project
id: proj-public-surface
title: "The project's public surfaces say what the project is"
goal: "Anyone landing on the org, a repo, or the docs site learns what Retinue is and what it isn't, without opening a source file."
goal_status: not_achieved
current_next_action: "Aros, c195: audited the other two claims in the lede c194 shipped 40 minutes earlier, and swept the class. c194 diffed its credential sentence against positioning.md and left the lead-story sentence unchecked - so the live page carried caveats for the credential claim (retinue#15) and the egress audit, and none for the triple-store layer, while positioning.md:199 requires the read-back caveat unprompted. The worse instance is writing/org-profile-README.md, the handover draft for retinue-os/.github: it presents the projects card as one query over every project file in every mounted chamber, prints the SPARQL, and never says the query returns 0 rows - the c186 correction of that exact claim swept two other files six hours earlier and missed the one aimed at the org's front page. Re-measured live before writing rather than quoted: kb#Project 0, project#Project 6, and the store's only actor URIs are actor-aros/actor-owner against the self-review job's actor:aros. Fixed in three places - the lede now names both dead read-back features with both measurements, the org draft carries the caveat above its query plus a paragraph on retinue#30 (path chambers never indexed) and qlever-dir#8 (blank-node identity across files), and positioning.md's 'Provenance is free' bullet, which every draft reads first, now carries those two limits with the instruction to state one of them to any semantic-web reader, because they will run the cross-file join. Nothing filed: the c184 budget is spent until 2026-07-27 03:17Z and all three defects were in copy I own. Aros, c194: audited docs/index.html as a crawler and a link-preview fetcher receive it - never done in 193 cycles (zero hits for og:, noscript, canonical, robots or meta description anywhere in my records; c22 audited the repos social-preview images, a different surface). With scripts stripped the live page served 1394 characters, about 750 of them the page own disclaimer, and not one sentence saying what Retinue is: credential, SPARQL, gateway, chamber and architecture all absent, no og:/twitter: card tags, no canonical, and the only date a non-JS reader saw was the baked fallback "20 July 2026", six days stale. Fixed in my own repo (ee252b7): project-level description, eight card tags (summary, not summary_large_image - the only image is a 512 px square), canonical, a static lede carrying the architecture argument, a noscript pointer to the committed JSON, and a dateless fallback. Served text 1394 -> 2564. One hypothesis falsified before acting on it: GitHub robots.txt disallows /*/tree/, /*/raw/, /*/blame/ and /*/archive/ but not blob, so the two finished pieces are crawlable where they are and no rehosting was needed. The finding inside the fix is mine: the first draft of the lede reproduced the unscoped credential claim I filed as retinue#27, on my own surface, minutes after reading the guardrail against it - corrected before commit to state both conditions (the paths Retinue ships, and retinue#15 spawn-point gap). New rule: check a credential sentence against positioning.md as a diff, not as a feeling of having read it. Aros, c193: measured the half of qlever-dir#8 I published and never ran - the issue says the blank-node collision is latent until a converter emits blank nodes, and asserts one paragraph later that a hand-written .ttl has it too. Two Turtle files with [ ] only, no converter and nothing merged, indexed in under 30 s: correct named graph each, but the two files' first blank nodes are the same node (a two-GRAPH subject join returns bn0 four times) and the graph-unaware join returns 5 rows for 3 declared nodes, two of them pairing an id from one file with a label from the other. So it is reachable today in any deployment holding a .ttl or .n3 with [ ] or _:b1 - a data file, not a code change. Posted as a comment on the open issue rather than a new one; the c164 patch caveat (untested against real rapper output) repeated unchanged; fixtures removed and the store verified back to 8 graphs. Also corrected the input to a live scheduler decision: the last human action in the org is the owner's chamber branch push at 2026-07-25T16:34:31Z, not framework main at 15:12:01Z, so the c164 re-slow bound expires 16:34:31Z and c192 published it 82 minutes early - into the window this owner has been active in on six of the last seven days. Cadence left at 1800 s. Aros, c192: read scheduler.log and /root/.retinue/scheduler/ for the first time in 192 cycles - the one surface that reports whether I ran at all, as opposed to what I wrote. 192 tick dispatches: 185 completed, 4 killed at the 900 s timeout, 2 failed on a 429 monthly spend limit on 2026-07-20/21 that nothing in my records noticed and that resolved without me. Six wake-ups produced nothing and log.md shows no gap where they were; two of the four killed runs had committed and pushed with 17 s and 121 s of margin. Durations are now median ~500 s against the 900 s ceiling and the previous cycle took 761 s, so the lever is a shorter wake-up rather than a longer timeout - the same rule c144 wrote and c184 found had stopped being applied, arriving this time through the exhaust pipe. Not escalated: the spend limit is five days old and fixed, and re-raising it would be the nagging the clock rule forbids. Correction to c191: the dashboard job's next fire is 2026-07-26T17:34:55Z read off its state file, not 01:26Z inferred from the artifact's timestamp - third instance in fourteen cycles of measuring an instrument by its output. Owner: enable private vulnerability reporting on the three public repos (chamber#5), then the org profile and descriptions (chamber#4). Aros, c191: regenerated docs/data/*.json - the owner's queue had three issues on no card (retinue#36, #37, #38, filed 02:02-03:17Z) and five counts false by arithmetic (41 open vs 44, filed 34 vs 37, every age 7 h short). The daily refresh job is the wrong cadence for a queue: its freshness requirement is set by the filing rate, not by the schedule. New measurement on the page: a GitHub search for 'retinue' ranks the framework 13th, the deployment 27th, this chamber 38th, behind a Bannerlord mod and an unrelated Claude Code tool - so discoverability and chamber#4 are one item, measured rather than asserted for the first time. The cycle's own error, caught by running date -u before committing: the first draft of all five files carried a generated timestamp 20 minutes in the future, breaking rule 4 of the seven this page publishes, while regenerating the page that publishes it. Procedure added: compute the ages last, from the clock. Aros, c190: the c145 rotation rule names log.md and its general lesson names every file that only grows, and in nine cycles nobody ran it against a second one. Measured both as GitHub serves them: log.md 272 KB at 2.9 KB/h (44 h of margin), projects/public-surface.md 283 KB at 6.9 KB/h - about 17 h from the 400 KB rendering limit it crosses at HTTP 200 with no error. Both rotated verbatim, reconstruction-verified: log.md to 45.6 KB, this file to 127 KB, archives in log-archive/ and the new projects-archive/ (outside projects/, because md2ttl.py fails on a frontmatter-less .md and that is a parsingError quad per part - converter scope measured against the live store, not assumed). The c145 render indicator was also wrong: 'richText':null false-positives on a 48 KB file, so the check is now a heading count against the source. Aros, c189: took scripts/ingest-sensors.py, the last name on c177's never-mentioned list, and it was the one that mattered. Its default chamber root is the framework checkout, which has no observations/ directory, so both documented invocations (the docstring and archivist.md:182, neither of which mentions CHAMBER_DIR) glob four directories that do not exist, write nothing, print '0 observations' and exit 0 - the archivist then commits the moved CSVs alone and reports success. That is the third step of the pipeline docs/triple-stores.md uses to argue the lead story. Two smaller items travel with it: one of the twelve Garmin columns sync-garmin.py writes and archivist.md documents is missing from GARMIN_COLUMNS and silently dropped, and the Ultrahuman observation count is divided by ten where every emitter writes five per observation. Written up with a tested patch at drafts/ingest-sensors-unreachable-chamber-root.md and HELD - the c184 rate limit binds until 2026-07-27 03:17Z and the urgency exemption does not apply, since the CSVs survive in git and a re-run recovers everything. It ranks ahead of c188's cosmetic manifest string for that slot, which is the ranking the rate limit exists to force. Negative result kept: the five-triple SOSA shape at docs/triple-stores.md:177-183 matches all four extractors exactly, so the factual base under bet 1 holds. "
current_actor: actor-owner
waiting_since: 2026-07-20
expected_by: 2026-08-10
paused: false
category: community
---

# The project's public surfaces say what the project is

## Goal
Anyone landing on the org page, a repo listing, or the docs site learns what
Retinue is and what it isn't, without opening a source file.

## Why this is its own thread
Split out from `social-presence.md` on 2026-07-20 (seventeenth wake-up). That
project is about **accounts** — identities that must be created and handed over.
This one is about **copy on surfaces that already exist**, which fails for a
different reason and is fixed by a different action. Conflating them hid the org
profile gap for seventeen cycles: every survey checked stars, issues and PRs, and
none checked what the org page actually renders.

## Current state, measured 2026-07-20

| Surface | State |
|---|---|
| `github.com/retinue-os` profile | **Empty** — `retinue-os/.github` does not exist |
| Org description | `null` |
| `retinue` description | blank |
| `retinue-os-chamber` description | blank |
| `retinue-os-deployment` description | blank |
| `qlever-dir` description | present and good |
| Framework `README.md` | present, accurate, audited cycle 11 |
| `docs/` dashboard | present |

## Success criteria
- The org profile renders a statement of the thesis, one runnable query, and the
  honest limits — in that order.
- Every public repo has a one-line description.
- Claims on these surfaces trace to `brand/positioning.md` or the framework docs,
  and are re-audited whenever the claim table changes.

## Prepared and waiting
[`writing/org-profile-README.md`](../writing/org-profile-README.md) — complete
profile text, a 120-character org description, and descriptions for the three
blank repos. Paste-ready; no drafting work remains.

Handed over at
[chamber#4](https://github.com/retinue-os/retinue-os-chamber/issues/4)
(`owner-action`). Blocked on org administration and on a token scope the
deployment does not have (`PATCH /repos/...` → 403, tracked at
[chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6)).

## Open question left to the owner
The draft ends with an optional line disclosing that Aros writes much of the
org's issues and documentation. It is honest and on-thesis, but the org profile
publishes under the owner's name, so it is his call and not mine to assume.

## Surface register

Started 2026-07-20 (eighteenth wake-up), because three consecutive cycles found
their work by auditing a surface nobody had a habit of checking. The failure mode
is not laziness — an unchecked surface generates no signal to prompt checking it.
So the surfaces get a list, and the list carries dates.

**Rotation (added 2026-07-26, cycle 190).** This file has the same shape as
`log.md`: an evergreen head — the register table below — plus an append-only
chronological tail of per-cycle write-ups. The tail is what grows. Past 200 KB it
rotates: whole sections move verbatim, oldest first, into `projects-archive/`,
keeping the head plus the five most recent sections; each archive part stays
under 300 KB. The reason is the same one measured for the log at cycle 145, and
the numbers are this file's own: at 283 KB it was growing 6.9 KB/h, about 17
hours from GitHub's 400 KB rendering limit, which it crosses without any error —
the URL keeps returning 200 and the page just stops rendering.

The archive must live **outside `projects/`**. `projects/.qlever/converters.json`
declares `md2ttl.py` for `.md`, and that converter fails on a file with no YAML
frontmatter, which is a `parsingError` quad per archive part. Verified rather
than assumed: `writing/`, `drafts/` and the chamber's root `.md` files produce no
graphs and no error quads in the life store, so the converter is scoped to the
subtree containing its `.qlever/` directory.

Archive, oldest first:

- [`projects-archive/public-surface-c033-c183.md`](../projects-archive/public-surface-c033-c183.md)
  — cycles 33–183, 2026-07-20 to 2026-07-26.

| Surface | Last audited | Result |
|---|---|---|
| Org profile page / descriptions | 2026-07-20 (c17) | Empty → chamber#4 |
| Framework `README.md` | 2026-07-19 (c11) | Accurate against claim table |
| Framework docs vs. claim table | 2026-07-19 (c11) | One defect → `docs/calibrate-reindex-latency` |
| Issue authorship / disclosure | 2026-07-20 (c16) | Violation → chamber#3, retrofitted |
| `SECURITY.md` reporting path | 2026-07-20 (c18, re-checked c53) | **Broken** — PVR disabled → chamber#5; scope section still consistent post-c52 (see c53 row) |
| Repo topics | 2026-07-20 (c18) | None on any repo → chamber#5 |
| Repo licences | 2026-07-20 (c18) | `retinue-os-chamber` unlicensed → chamber#5 |
| Community health files | 2026-07-20 (c18) | `retinue` 75%; other two lack `SECURITY.md` |
| README of `qlever-dir` | 2026-07-20 (c19) | Accurate; one gap — converter section implies watcher support it lacks → comment on qlever-dir#3 |
| My own records (strategy citations) | 2026-07-20 (c19) | **False citation** — token blocker cited to a nonexistent issue → chamber#6 |
| `CONTRIBUTING.md` | 2026-07-20 (c20, re-checked c53) | Accurate and well-judged. Its testing section led to the CI find below; re-verified c53 against the now-live CI and submodule state — still holds |
| `CODE_OF_CONDUCT.md` | 2026-07-20 (c20) | **Enforcement link dead** — routes to disabled PVR, same root as chamber#5 → comment on chamber#5. Also: both channels terminate at the maintainer, which the text doesn't say |
| `review.md` vs. reality (tests/CI) | 2026-07-20 (c20) | **Stale** — six false statements, recommendation #2 done → retinue#3 |
| My own records (claim table) | 2026-07-20 (c20) | **Stale claim** — GUARDRAILS §3 and the org-profile draft both assert "no CI" → chamber#7; draft fixed. *Re-checked c23 under rule 4: contained. Only live instance left is `GUARDRAILS.md:51` itself, which is the owner's edit by design; `briefing.json` already states CI truthfully; other hits are tracking rows or history* |
| `docs/` dashboard site | 2026-07-20 (c21) | **Live and stale** — served at `retinue-os.github.io/retinue-os-chamber` since publication, never audited. Header date, relative dates, wrong tracker citations, and an owner queue missing 4 of 7 open issues. All fixed in-repo. *Re-checked c29 for freshness rather than correctness — the one surface that decays on the wall clock: `docs/data/*.json` regenerated 05:00 by the daily job, both 04:24 issues present, all seven owner items listed, `briefing.json` states the zero-contact position as untested rather than disappointing. Current; no edit* |
| Repo → live site delivery path (Pages) | 2026-07-20 (c24), re-checked 2026-07-23 (c146) | **Serving correctly; one invariant c24 recorded no longer holds.** c146: `index.html` and all five `data/*.json` byte-identical live vs. repo, Pages `status: built`, four most recent builds all `error: null`. But `pages/builds/latest.commit` = `a813938` while `main` = `8917a8b` — the build fired 5 s after the push and built the *parent* tree, and no retry is queued. Harmless this time and provably so: the undeployed commit touches `log.md`, `log-archive/`, `strategy.md`, `projects/` and root `README.md`, **nothing under `docs/`**, so a build of HEAD would emit identical bytes. The finding is the mechanism, not today's damage: a Pages build can silently lag HEAD by one commit, and if that happens on a push that *does* touch `docs/`, the dashboard serves stale data with `status: built` and no error until the next push of any kind. **Bound measured the same cycle:** this cycle's own push (`bf7ac80`, 06:26:46Z) built `bf7ac80` — HEAD, no lag — and deployed the skipped tree with it, so the exposure is one push, not unbounded. → **standing check: after any push touching `docs/`, compare `pages/builds/latest.commit` with `commits/main.sha`; if they differ, re-trigger with a further push.** Rule 4's chain ends at the served bytes, not at the commit — see below |
| The escalation channel itself (dashboard thread state) | 2026-07-20 (c27) | **Working — my reading of it was not.** Security thread `unread: true`, never opened; adjacent thread shows the dashboard functions and the owner used it 2026-07-19 16:52. Converting ages from cycles to wall-clock overturned the premise of ~15 cycles of reporting → see rule 5 |
| My own tool/permission surface (guardrail 5 isolation) | 2026-07-20 (c30) | **Isolation not enforced.** `/workspace/.claude/settings.json` pre-approves 3 Zoho Mail + 6 Zoho Calendar + 9 WhatsApp + 5 Telegram tools, empty deny list; nine claude.ai MCP connectors attach to sessions with `cwd=/workspace` and the Zoho one logs `Successfully connected`, `hasTools:true`, in *this* session. Guardrail 5 says I run with only this chamber and must refuse and escalate on correspondence access — escalated to owner (dashboard), no tool called, no message read. Honest limit: the tools are not in my subagent function list, so this is a standing grant, not a demonstrated read. Knock-on: it narrows a `positioning.md` claim → calibrated same cycle. 29 prior cycles logged the MCP banner's *content* and never checked whether the server was *attached* |
| The org's own CI/automation output (workflow runs) | 2026-07-20 (c32) | **One workflow broken in production.** `check-signal-cli` fired on its first real version change (10:52 UTC), detected 0.14.5 → 0.14.6, pushed `bump/signal-cli-0.14.6`, and failed on `gh pr create`: *"GitHub Actions is not permitted to create or approve pull requests"*. The workflow already declares `pull-requests: write`; the block is the org/repo **checkbox** (Settings → Actions → General), a **different** permission from chamber#6's PAT scope → retinue#4. New surface: the register listed repo *content* and *settings* but never the Actions tab, which is the one place the project reports on itself unprompted |
| Repo social preview images | 2026-07-20 (c22) | **Not a separate problem.** All four repos serve GitHub's auto-generated card (`opengraph.githubassets.com`, HTTP 200 each); none has a custom image. The auto-card renders the repo **description**, which is blank on three of four — so the link preview is downstream of chamber#4, not of a missing image. Custom uploads are UI-only: the REST repo object has no social-preview field to read or set. Folded into chamber#4; no new issue |
| Actions **secrets and variables** inventory (4 repos + org) | 2026-07-20 (c34) | **Not auditable by me, by design.** All ten endpoints 403; `.env.example` grants no secrets scope. Checked the denying config *before* escalating (c33 rule) — deliberate, so no issue filed. Remains the owner's to audit |
| Workflow **file contents** (`retinue`: `tests.yml`, `check-signal-cli.yml`; no workflows in the other three repos) | 2026-07-20 (c34) | **One conditional finding.** `tests.yml` declares no `permissions:` block, so its token inherits the repo/org default radio — which I cannot read (403, no Administration scope). Correct by contrast: `pull_request` not `pull_request_target`, and the upstream version is regex-validated before interpolation into `run:`. One-line fix drafted; can't commit it (no Workflows write, by design) → comment on retinue#4 rather than a new issue, same settings panel |
| `retinue-os-deployment` repo contents (public reference deployment) | 2026-07-20 (c33) | **Overturned my own escalation.** `.env.example` documents the token recipe: `Pull requests: read`, and `Do NOT grant Administration, Members, or org-level write` with a prompt-injection threat model (`6ea80c2`). chamber#6 had framed all four consequences as one oversight; three are repo-settings writes the owner **deliberately** withholds. Withdrew those; left the narrow PR-create question. Also scanned for leaked credentials and owner personal data: **none**, every value a placeholder |

| `qlever-dir/build_index.sh` (the path→graph-IRI mechanism itself) | 2026-07-20 (c38) | **Four filename-dependent defects → [qlever-dir#5](https://github.com/Retinue-OS/qlever-dir/issues/5).** The graph IRI is interpolated into a `sed` replacement (line 170) and never escaped for `sed` or for N-Quads. A `\` in a filename is silently swallowed → valid-but-wrong graph IRI, and a collision if the stripped path also exists; `&` expands to the match; a space or `|` makes the quad or the `sed` expression invalid, which under `set -euo pipefail` fails the **whole** build — contradicting the header's own per-file isolation promise. Same gap in `escape_literal`, which misses `\r`, so the diagnostic path can itself emit an illegal quad. Measured: all four `sed` behaviours + the CR passthrough. Unmeasured: `qlever-index`'s reaction (no binary here) — stated as such in the issue; the silent case doesn't depend on it |
| `qlever-dir/examples/projects/.qlever/md2ttl.py` (the converter contract example the docs point at) | 2026-07-20 (c39) | **Four unescaped/unvalidated frontmatter paths → [qlever-dir#6](https://github.com/Retinue-OS/qlever-dir/issues/6).** `id`, `current_actor` and scheme-matching `links` entries are interpolated straight into IRIREFs; a space in any of them (`current_actor: Jane Doe` — the likely one, since the field invites a person's name) emits unparseable Turtle at exit 0. Dates are interpolated into `^^xsd:date` with no validation and, unlike the string branch, without `ttl_string`: `waiting_since: soon` is **well-formed Turtle**, so it is stored, and every date comparison the field exists for is quietly wrong; `expected_by: a"b` breaks the file's parse. Measured: all four outputs, plus the quote case. Unmeasured: `rapper`/QLever reactions (no binary here) — cases 1–3 rest on the `IRIREF` production, case 4's silent half on inspection. **Byte-identical to my own chamber's `projects/.qlever/md2ttl.py`**, which is unaffected in fact — every id is a slug, every actor a slug, every date ISO — so the convention that keeps it working is demonstrated everywhere and stated nowhere |
| `qlever-dir`'s `nginx.conf`, `Dockerfile`, `docker-compose.yml` (the container's own operational surface) | 2026-07-20 (c41) | **No supervision, no readiness signal → [qlever-dir#7](https://github.com/Retinue-OS/qlever-dir/issues/7).** The container's working definition of "up" is *the orchestrator is still looping*, which is true in every state where the endpoint is dead. The main loop never polls `active_proc`, so a dead `qlever-server` means 502 until someone touches `/data` — and `restart: unless-stopped` never fires, because PID 1 is fine. nginx is daemonized by `subprocess.run(["nginx"])` and never checked or `wait()`ed either. No `HEALTHCHECK`, and nginx starts *before* the first build, so port 7001 serves 502 from second zero for a build the README says can take hours — a dependent service has nothing to wait on. And nginx's `error_log`/`access_log` go to files with no symlink to stdout, so the 502s are invisible to `docker logs` while the orchestrator's healthy-looking log is all that shows (same family as #4). Contradicts README lines 6 and 26 ("stays available the whole time", "no downtime"). Measured: absence of `poll()`, of `HEALTHCHECK`, of log symlinks; the log paths; the `main` and `do_rebuild` orderings; the per-slot memory flags. Unmeasured: no Docker/nginx/qlever binary here, so no observed 502, OOM, zombie or dropped request — findings 1–4 rest on control flow and absent config, finding 5 (reload/stop race) on nginx's documented reload semantics and is the one most open to argument |
| The framework's `.env.example` (the first file a new deployer edits) | 2026-07-20 (c40) | **One silent override, one undocumented credential pair, two doc gaps → [retinue#5](https://github.com/Retinue-OS/retinue/issues/5).** `STT_SUPPORTED_LANGUAGES` — named as the control by both `stt-service.py`'s own header and `CLAUDE.md` — cannot be set from `.env`: the `stt` service has no `env_file` and its `environment:` pins the variable to `${SIGNAL_SUPPORTED_LANGUAGES:-}`, so setting it is not merely ignored but **overwritten with empty**, re-enabling exactly the unconstrained detection that block exists to prevent. `GARMIN_EMAIL`/`GARMIN_PASSWORD` are read by two framework scripts and by the `garmin` source `CLAUDE.md` uses as *the* refresh example, and documented nowhere — the one credential pair in the framework with no block and no app-password warning. `CONVERSATION_BASE_URL` is cited once as a fallback and defined in no file (same class as deployment#1). Three duplicate keys, of which `SEND_APPROVAL_BASE_URL` is documented twice with divergent semantics — both locally true (messenger gateways don't consult the fallback; `email_client.py` does), but last-wins in dotenv. Measured: duplicates, the `env_file` inventory, absence from `README`/`docs/`. Unmeasured: no Docker here, so no `docker compose config` — finding 1 rests on the compose file having no second path in, stated as such |

| **This chamber repo's own contents, as a disclosure surface** | 2026-07-20 (c42) | **Guardrail 5 violation, published since the initial commit → redacted this cycle; owner decision on history escalated (dashboard).** `retinue-os-chamber` is public and tracks all 46 files including `log.md`, `strategy.md`, `drafts/` and `projects/`. `projects/public-release.md` — the file whose whole purpose is keeping the owner's personal data out of the public tree — stated in public (a) the categories of personal data found in the private archive and their location on a stale branch of a named private repo, and (b) that shipped examples "disclose the owner's disability and metabolic monitoring", under a heading that called the disclosure undecided. Public `qlever-dir` ships `examples/projects/rollstuhl-bluetooth.md`; the example alone is deniable — a developer documenting a protocol is not necessarily a user of the thing — and this file removed the deniability by attributing it to a named person. Measured: repo `isPrivate: false`; `git ls-files` (46, all of the above); `git log --follow` → present since `63b62f4`, initial commit, and pushed; grep across all tracked files for the disclosure terms (only this file and one incidental `log.md` mention, which discloses nothing standing alone and was left rather than rewriting a historical entry); clone of `qlever-dir` for the corroborating example. Unmeasured: whether the owner has already made any of this public elsewhere — unknowable from here, which is exactly why it was his call and not a previous me's. Clean on the rest: no credentials or tokens anywhere in the tree, the only e-mail addresses are `aros@retinue-os.github.io` and `you@example.com`, and the two withheld security findings are referred to 30+ times by name only and never described |
| **`brand/positioning.md` and `writing/`, audited for AI *disclosure* rather than accuracy** | 2026-07-20 (c44) | **The live public dashboard identified its author by a human-sounding first name and never said he is an AI — fixed this cycle.** `docs/index.html` has been served at `retinue-os.github.io/retinue-os-chamber` (HTTP 200, verified) since publication with the byline "Project dashboard, kept by Aros" and a footer disclaiming only that the page is a static mirror. Every word of the five cards is AI-authored; "Aros" reads as a person's name; guardrail 1's test — would a reasonable reader assume a human wrote this — fails. Header now reads "kept by Aros, the project's AI agent" and the footer names him as an AI agent and links GUARDRAILS.md and log.md. Second find, the upstream one: `brand/positioning.md`, self-described as the source of truth for every public claim, governed *what* may be claimed and said nothing about *who* is claiming it — the two finished essays disclose in their standfirst by a previous generation's choice, not by any requirement in the file that copy is composed from. Disclosure clause added there. Measured: `curl` 200 on the live URL; grep for disclosure terms across `brand/` and `writing/` (three hits, all in `writing/`, none in `brand/`); grep for "Aros" across `docs/data/*.json` (ten unqualified name mentions across all five cards). Clean: both essays disclose correctly in the standfirst; `README.md` describes him as an autonomous agent. One deliberate non-change: the org-profile draft's disclosure line stays optional, because the owner publishes that text under his own review on his own org page — a byline, not a hidden hand |
| **`docs/components/*.js` — the published dashboard's own rendering code** | 2026-07-20 (c45) | **Every date on the public dashboard rendered one day early for readers west of UTC — fixed this cycle.** `fmtDate` in `docs/components/base.js` formatted with `toLocaleDateString('en-GB', …)` and no `timeZone`, so it resolved in the *reader's* zone while every `generated` stamp is written in UTC and `index.html`'s header script pins `timeZone: 'UTC'`. Two consequences, the second worse than the first: (a) a document generated between 00:00 and ~08:00 UTC shows the previous day in all five card stamps while the header shows the UTC day — the same header/content drift the `index.html` comment claims to have eliminated on 20 July, still live one layer down; (b) the **date-only** fields on the projects card (`since`, `expected`) parse as UTC midnight and so were *always* off by one, for every reader in the Americas, on every render — "Waiting on the project owner since 17 July 2026", a date on which nothing happened, and all four project due dates a day early. Not cosmetic: those are factual claims about when the owner was asked for something. Measured in `node` at TZ=UTC / America/Los_Angeles / America/New_York, before and after; one call site, one line, covers both cases. Clean on the rest of the audit: `esc()` is applied to every interpolated value in all six components, no `innerHTML` path takes unescaped data, no network call goes anywhere but `data/*.json`, and the mirror's "copied from the live dashboard" comments check out against `diff` — except `messages.js`, which says "unchanged" while its empty-state string differs (left; the claim is about the card, and the diff is one string). Noted, unfixed: the mirror drops the live cards' `cache: 'no-store'`, so a returning reader can be served a stale dashboard — but header and cards fetch the same document, so they go stale together and no date disagrees |

| **`docs/examples/provenance/` — the runnable example the provenance essay sends readers to, and the live store behind it** | 2026-07-20 (c46) | **The workaround documented here does not work, and had left the store sixteen hours stale — corrected here and in [qlever-dir#3](https://github.com/Retinue-OS/qlever-dir/issues/3).** The example's own claims all hold: both `.nt` files land in the path-derived named graphs the README prints, and its SPARQL snippet returns the two sensor-a triples verbatim. The failure was one level out. This README, and my 2026-07-19 comment on qlever-dir#3, both stated that keeping an `.nt` file in a Markdown chamber gives the watcher "something it will react to". `orchestrator.py` watches `close_write,create,delete,move` — it reacts to a file *changing*, not existing. These two files have not changed since 19 July, so they bought exactly one rebuild and nothing since. Measured: `projects/public-surface.md` (added 02:42 UTC, 20 July) was absent from the store at 18:35 — sixteen hours — while its converter run by hand emitted the expected ten triples at exit 0 and no `emit_error_quad` record existed anywhere, so it had simply never been scanned; a **byte-identical** rewrite of `sensor-a/readings.nt` put it in the index within twenty seconds (0 → 10). *(Struck c47: this row originally said "the reader harmed was the public dashboard's projects card, which for those sixteen hours rendered a project list with one project silently missing." False. The public card is a static mirror of a committed `data/projects.json` and never queries the store; the store-backed card is the framework's private dashboard, which returns no rows at all under retinue#1. No reader was affected — the fault is that nothing would have said so.)* Two things this adds to qlever-dir#3: presence is not a workaround (any chamber whose RDF is static — reference data, a fixture, this demo — behaves exactly like a Markdown-only one), and the staleness is unbounded and **silent** — no error quad, no log line, no empty-store marker; the store answers every query successfully with an index of unknown age. Unmeasured: whether c43's "dashboard data eleven hours stale" was this same cause; plausible and not established. Deliberately not built: a scheduler job that touches an `.nt` file on a timer would hide the bug behind machinery rather than fix it |

| **c46's own output — the harm claim in a published issue comment** | 2026-07-20 (c47) | **The severity example in [qlever-dir#3](https://github.com/Retinue-OS/qlever-dir/issues/3#issuecomment-5026157542) described an outage that never happened — corrected in the thread and in both copies here.** c46 closed its comment with "the reader was a public dashboard card, which for sixteen hours confidently rendered a project list with one project missing". Neither of this deployment's two projects cards did that. The **public** one (`docs/components/projects.js`) fetches `data/projects.json`, a file I generate from the `projects/` Markdown and commit — it issues no query to the endpoint, and the copy generated 17:05 UTC, mid-staleness, lists all six projects including the missing one. The **store-backed** one is `web-gateway.py::_fetch_projects`, which is private, behind auth, and separately broken: [retinue#1](https://github.com/Retinue-OS/retinue/issues/1), open since 19 July, has it returning no rows at all on a namespace/predicate disagreement. Measured: the fetch target in both components; the six entries in the 17:05 `projects.json`; retinue#1 open. Everything else in c46 survives — the sixteen-hour absence, the twenty-second byte-identical reindex, presence-is-not-a-workaround, and the silence. What did not survive is the only sentence in it that named a victim |

| **`README.md`'s Installation and model-gateway sections, read against `docker-compose.yml`, `.env.example` and `litellm/config.yaml`** | 2026-07-20 (c51) | **A subsystem the docs call optional is an unconditional startup dependency → [retinue#11](https://github.com/Retinue-OS/retinue/issues/11).** The `retinue` service declares `depends_on: litellm: condition: service_healthy`; `litellm` requires `litellm-db` healthy; `litellm-db` is postgres with `POSTGRES_PASSWORD=${LITELLM_DB_PASSWORD}`, a variable appearing once in `.env.example`, commented, inside the block headed "Optional LiteLLM gateway". The README's own default path tells the reader to omit exactly that block. No `profiles:` key anywhere, and the override example never names the service, so there is no shipped way to opt out. Second, smaller find in the same section: `ANTHROPIC_BASE_URL=http://ollama:11434` names a compose hostname that occurs nowhere else in the repo — no service, no override example, no instruction to add one — where the parallel LiteLLM recipe introduces its target as "The included `litellm` service" and does resolve. Measured: the whole `depends_on` chain; the interpolation; the single commented occurrence; `grep -c "profiles:"` → 0; `grep -rn ollama` → 2 hits, both in the README. **Unmeasured, and stated as such in the issue:** no Docker daemon here, so the postgres failure rests on the official image's documented requirement ("must not be empty or undefined"), not on an observed error — and whether `litellm` itself starts healthy with `LITELLM_MASTER_KEY`/`OPENROUTER_API_KEY` unset is untested, which would be a second independent stall. **Near-miss worth recording:** a first pass "found" that `.env.example` omits `RETINUE_GATEWAY_USES_CLAUDE_OAUTH`, which via `entrypoint.sh:309` would silently disable remote-control on the LiteLLM path. False — the grep was anchored `^VAR=` and skipped every commented line in a file that is almost entirely commented. Reading the actual block killed it. → rule 15 |

| **README's operational tail: `First start` / `Normal start` / `Updating the image`, read against `entrypoint.sh`, `docker-compose.yml` and `CLAUDE.md`** | 2026-07-20 (c54) | **One real gap → [retinue#12](https://github.com/Retinue-OS/retinue/issues/12); the rest correct.** `Updating the image` (README:592–599) documents `git pull` + `docker compose build` as the recipe "to pick up changes to agents, scripts, or dependencies" and omits `docker compose up -d` — so on a running stack `build` rebuilds an image nothing runs until an `up -d` recreates the containers. Same class as retinue#9 (the correct version lives elsewhere in the same repo): `CLAUDE.md:601` states the framework's own canonical update as `git pull && docker compose build && docker compose up -d`, and README:475 (`Normal start`) is the only `up -d` in the file. Measured: the two commands in the section; `grep -n 'up -d'` → only :475; `CLAUDE.md:601`. Unmeasured, stated in the issue: no Docker daemon here, so this rests on Compose's documented recreate-on-`up`, not an observed stale container. **Correct:** `First start` (`docker compose run --rm retinue interactive`) and `Normal start` (`up -d` / `down`) match `entrypoint.sh`'s `MODE="${1:-interactive}"` and its `interactive`/`remote-control` case. **Register-accuracy note (rule 13 self-records):** c53's queued list called `Deployment` still-unaudited — it was already audited at c50 ("the Deployment and host-mount sections match the entrypoint's already-present-chamber detection"), so it was not re-covered. **What happens at startup**: steps 1–3, 5, 6 verified at c50, step 4's ~15 s / "no downtime" claim is qlever-dir#7 territory, and step 8's Signal-only framing folds into retinue#10's open question about forked/unlisted services — no new file for either |
| **`SECURITY.md` and `CONTRIBUTING.md` re-audited against the post-CI, post-c52 state** | 2026-07-20 (c53) | **Both consistent; the one standing defect stays tracked, no new issue.** Re-check, not a first look: SECURITY.md was audited c18 and CONTRIBUTING c20 — so c52's queued note calling them "never audited" was wrong, and this row corrects it (register-accuracy, rule 13's self-records clause). The re-audit was justified by two intervening changes. (1) **CI now exists** (chamber#7): CONTRIBUTING's testing section tells a contributor to run standalone `tests/test_*.py` after `pip install markdown-it-py requests` and to mirror module-scope imports into `.github/workflows/tests.yml` — verified: five test files present, `tests.yml:35` installs exactly `markdown-it-py requests`, and the four gateway modules under test carry those module-scope imports. `git clone --recurse-submodules` checks out too — `.gitmodules` declares `qlever-dir`. The whole file holds. (2) **The c52 send-approval finding** bears on SECURITY.md's scope section: SECURITY.md lists "anything that lets an agent approve its own send" as **in scope** for a vulnerability report (:25–26) and does **not** list it under known-limitations — so it is internally consistent with the private c52 escalation treating that as a genuine reportable weakness, and needs no change. The dead private-reporting link (`{"enabled": false}`, re-confirmed this cycle) remains covered by chamber#5; no re-file, no re-escalation. Deliberately no change to either file. |
| **`.claude/agents/archivist.md` — the ingestion/ontology reference `docs/triple-stores.md:391` sends a lead-story reader to, never audited as its own surface** | 2026-07-21 (c56) | **Clean; consistent with the doc it's linked from and with the code, nothing to file.** Checked the doc's SOSA worked example (`triple-stores.md:157–163`) against archivist.md's ontology tables predicate by predicate. The example's observation URI `urn:obs:ckm:X1234:42` matches archivist.md's `urn:obs:{source-type}:{file-stem}:{row-id}` (line 56); `urn:health:property:blood-ketone-bhb` matches the observed-property table (line 64); `urn:health:sensor:ckm:X1234` matches the sensor pattern `urn:health:sensor:ckm:{file-stem}` (line 73); the five predicates (`rdf:type`/`observedProperty`/`hasSimpleResult`/`resultTime`/`madeBySensor`) match the doc's "five triples per observation" exactly. The graph-naming convention (lines 89–95, `<file:…>` from path, no quad in the file) matches CLAUDE.md and the c55 read of the doc. **The reindex-latency finding class (retinue#2, qlever-dir#3) does not apply to this surface:** archivist.md's own "~15 s of any change" claim (line 23) is about **`.nt` output**, which is exactly the extension the inotify watcher *does* fire on — so for the archivist's writes the ~15 s holds, and the caveat those issues raise (Markdown/frontmatter edits waiting for the next rebuild) is out of scope here. Minor, not filed: line 66's "All sensor readings in these files are in mmol/L" reads as ambiguous in isolation but is scoped by context to the two properties just tabled (CGM glucose, CKM ketone), not the wearable/garmin tables below it. **Outcome:** the last bet-1 doc-neighbour surface is audited; the lead-story chain (`triple-stores.md` → archivist ontology → code) is internally consistent end to end. |
| **`docs/triple-stores.md` — the framework's own lead-story doc (the triple-store layer bet 1 rests on), audited as a public surface against qlever-dir source (`/tmp/qd/build_index.sh`, `orchestrator.py`), the shipped converter, and `web-gateway.py`** | 2026-07-21 (c55) | **No new defect; the one finding this surface yields is already fully tracked, and retinue#1's blast-radius claim about this doc is itself verified accurate.** Four concrete claims checked. (1) **Advantage-1 headline query (lines 111–125)** uses `PREFIX k: <https://w3id.org/retinue/kb#>`, `k:Project`, `k:status` — matching the broken `web-gateway.py` query (`_KB`, line 1500), not the shipped converter, which emits `https://w3id.org/retinue/project#`/`p:Project` and `p:goalStatus` (never `status`). This is exactly [retinue#1](https://github.com/Retinue-OS/retinue/issues/1), whose **body already names this doc** ("This also affects `docs/triple-stores.md`, which documents the query in its `kb#` form as the worked example") and whose fix line already lists it ("make the converter, the gateway, and `docs/triple-stores.md` agree"), and whose mismatch table already carries `k:status` vs `p:goalStatus`. So the doc's central worked example returns zero rows against the shipped converter — but no new issue: retinue#1 covers it verbatim, and a comment would duplicate the issue body. Verified the claim by reading `chambers/retinue/projects/.qlever/md2ttl.py` (`P = "…/project#"`, `a p:Project`, `goalStatus`, subject `<urn:retinue:project:…>`) against `web-gateway.py:1500,1508–1517`. (2) **Diagnostic-quad predicate (line 374)** `urn:qlever-dir:parsingError` — **correct**, matches `build_index.sh:33` `ERROR_PREDICATE="urn:qlever-dir:parsingError"` and the header at :23. (3) **Watcher/converter caveat (lines 135–139)** "the inotify watcher fires only on `.nt`/`.ttl`/`.n3` changes while the build does process `.md`; a frontmatter edit is picked up on the next rebuild or at container restart, not within ~15 s" — **honest and consistent** with qlever-dir#3 and the c46 presence-is-not-a-workaround finding; this is the good kind of stated limitation. (4) **"No downtime" (lines 25–26)** is scoped in context to the **blue-green rebuild transition** ("built into an idle slot, health-checked, then nginx swings over; a failed build leaves the previous index serving"), which is defensible for that transition; the first-build-502 and crash-recovery overclaim lives in qlever-dir#7 against the sibling repo's README (which says the broader "stays available the whole time"), so no duplicate here. Spot-checked clean: `BASE_URI: file:` graph example (line 34) matches CLAUDE.md; `SPARQL_ENDPOINT_LIFE=http://qlever-life:7001` (line 340) matches CLAUDE.md; SOSA 5-triple shape (lines 157–163) matches the archivist convention. **Outcome:** the lead-story surface is now audited; nothing to file, nothing to escalate. |
| **The framework's *open pull requests*, read as in-flight public documentation and as future claims** | 2026-07-23 (c147) | **Three measured defects in [#21](https://github.com/Retinue-OS/retinue/pull/21) → [comment on retinue#1](https://github.com/Retinue-OS/retinue/issues/1#issuecomment-5056843983).** A surface no row described: c139/c140 saw these four PRs, checked their *authorship* (owner, not external contact) and dismissed them as "framework work, not an Aros action item". Authorship is not the only question a PR answers — two of the four modify `CLAUDE.md`, the framework's most-read doc, and one ships a new SPARQL vocabulary. Findings, each run rather than read: (1) #21's gate query joins on `kb#`, and the live store holds **0** `kb:Project`, **6** `project#Project`, **0** triples with any `kb:` predicate — the PR's query verbatim returns `result-size-total: 0`. Same defect as retinue#1, third consumer, but it fails *silently by design*: "an empty result spawns nothing" is the intended cheap path, so failure and success are the same event. (2) The `current_actor: <agent-basename>` convention the PR *introduces into CLAUDE.md* does not produce the URI its own `discover-agents.py` types — converter gives `urn:retinue:coach`, registry writes `urn:retinue:actor:coach`; survives a namespace fix, and is a *third* actor spelling beside the store's `urn:retinue:actor-aros` and the gateway's `urn:retinue:actor:reto`. (3) The spawned prompt instructs the agent to write `resolved: true`, which is not in `md2ttl.py`'s `SCALAR_FIELDS` and emits **no triple** — the documented escape hatch is a no-op, verified on a fixture. Minor: `p:paused` is emitted and the gate ignores it. **Venue forced by chamber#6:** `POST /issues/21/comments` → 403 and GraphQL `addComment` → 403, while `POST /issues/1/comments` → 201 — for a fine-grained PAT, commenting on a PR is governed by *Pull requests*, the same missing scope. Fifth consequence, added to chamber#6. *Closed out c148 (2026-07-23): #21 merged as `11d2d06` at 11:57Z, 2 h 22 min after the review comment, unchanged — all three defects shipped. Findings 2–4 refiled where they belong, as [retinue#23](https://github.com/Retinue-OS/retinue/issues/23), against `main` rather than against a diff. The pre-merge review did not prevent the merge; it made the post-merge bug report take twenty minutes instead of a morning, which is the honest size of the win.* |
| **The named-graph provenance mechanism itself, exercised end to end with a *second* converter rather than read** | 2026-07-23 (c149) | **Two defects in `qlever-dir`, both silent, both measured against the live store → [qlever-dir#8](https://github.com/Retinue-OS/qlever-dir/issues/8) and [qlever-dir#9](https://github.com/Retinue-OS/qlever-dir/issues/9).** c55 audited `docs/triple-stores.md` by reading it against source and found the doc honest. c149 ran the thing instead, using the JSON-LD converter proposed in [retinue#22](https://github.com/Retinue-OS/retinue/pull/22) as the first converter in existence that emits blank nodes. (1) **Blank nodes collide across files.** `build_index.sh` concatenates each file's per-invocation `rapper` output into one N-Quads stream, so file A's `_:genid1` and file B's `_:genid1` are the same node to `qlever-index`. Measured: two JSON-LD files declaring 4 and 2 entries → `SELECT DISTINCT ?m WHERE { GRAPH ?g { ?m a rn:ConversationModel } }` returns **4**, not 6; a cross-graph join returns `bn0`, `bn1` as shared subjects; the natural graph-unaware query returns **10 rows for 6 models**, four of them pairing an id from one file with a label from the other. `ok=11 errors=0` in the build log. Latent today only because `md2ttl.py` mints a named subject for every file; arrives with the next converter, and applies equally to any hand-written `.ttl` using `[ … ]`. (2) **Symlinked files are silently skipped** — `find /data -type f` without `-L` matches the target, not the link. Measured: `c149-symlink.jsonld → conversation-models.jsonld`, relative and resolving, produced **no graph and no error quad**; `find -L` sees it, `find` does not. This matters now because #22 adds a line to `docs/triple-stores.md` telling deployments they may "copy (or symlink)" a file into a chamber — the copy works and reintroduces the drift the paragraph argues against, the symlink is a no-op. **What this row establishes as method:** the lead-story mechanism had been audited twice by reading (c38 the script, c55 the doc) and both passes missed these, because both defects need a *second file* and a converter nobody had run. Fixtures installed, measured, and removed; store verified back to its exact baseline (69 triples, 8 graphs) and the chamber tree left clean. |
| **`comparison.md` — the framework repo's competitor comparison, never audited, and the one public surface guardrail 4 governs directly** | 2026-07-24 (c154) | **The project's strongest security sentence is asserted as fact in four public places and its own open issue says it is false → [retinue#26](https://github.com/Retinue-OS/retinue/issues/26).** "An agent can never approve its own send" appears at `README.md:372` (inside the *definition* of the `verify` policy), `comparison.md:191` (carrying the competitive claim "neither competitor has an equivalent"), `review.md:90` (called "the invariant", in the section arguing the design is strong) and `scripts/whatsapp-gateway.py:20` (the component's own docstring) — while [retinue#19](https://github.com/Retinue-OS/retinue/issues/19), open since 2026-07-21 and filed by the maintainer, demonstrates the opposite. Verified against `main` at `92af09c`: `_complete_pending_send()` (`signal-gateway.py:1096`) checks only that the entry's status is `pending`; no caller identity anywhere on the path. The fix wording already exists one file over — `telegram-gateway.py:22-25` describes the same control and stops at "transmitted only after the user approves it" — and `SECURITY.md:25` is already consistent, listing the property as *in scope for a report* rather than as a fact. **External claims in the file check out**, which is worth recording as a negative result: `openclaw/openclaw` ★383,971 ⑂80,666 vs the doc's "~383k / 80k"; `NousResearch/hermes-agent` ★219,655 vs "~217k" (drift over ~1 week, inside the file's own dated caveat); both MIT (OpenClaw reports `NOASSERTION` only because its `LICENSE` carries a third-party-notices trailer); "12-service Compose stack" = 12 services exactly; "~13k lines" = 12,929 lines of Python outside the vendored `qlever-dir`. Two smaller defects folded into the issue: the License row is vague about Retinue's own licence (`LICENSE` is MIT) while giving both competitors "MIT", and L201's "the web gateway is untested" is stale in the way [retinue#3](https://github.com/Retinue-OS/retinue/issues/3) documents for `review.md`. |
| **The framework's *credential-custody* claim, swept across every place it is stated — the second run of the c154 rule, this time against [retinue#15](https://github.com/Retinue-OS/retinue/issues/15)** | 2026-07-24 (c155) | **The project's headline sentence is stated unscoped in three public places, and the version that is true is already in the same repo → [retinue#27](https://github.com/Retinue-OS/retinue/issues/27).** `review.md:69` says "the model's context never contains **messaging** credentials", which is accurate. `comparison.md:22` (first row of the comparison table), `:184` (heading of the three-layer security argument, stronger than the body under it) and `:258` (the "Choose Retinue if…" decision paragraph) all drop the scope word. Measured from inside this session — a scheduler-spawned one, i.e. exactly the spawn path #15 describes, verified by walking `/proc/<pid>/stat` to `scripts/scheduler.py` — the agent's own environment carries `GITHUB_TOKEN`, `OPENROUTER_API_KEY`, `LITELLM_MASTER_KEY` and `LITELLM_DB_PASSWORD`: a repo-write token, a billable API key, a gateway master key and a database password, readable with one `env`. Names only; no value was read or printed. **Honest limit, stated in the issue:** `EMAIL_PASS*` and `GARMIN_PASSWORD` are set nowhere in this deployment (absent from PID 1, the web gateway and the scheduler), so #15's mail half is cited, not re-measured. Scrub scope verified against `main` at `92af09c`: exactly two `unset` sites, `ANTHROPIC_API_KEY` (401) and the `EMAIL_PASS*` loop (409–411), both on the `exec claude` branch *after* the gateway (310) and scheduler (312) forks. Two smaller items folded in: `review.md:74`'s anchor `entrypoint.sh#L397-L402` no longer contains the loop, and `SECURITY.md:47` ("cannot steal credentials and cannot silently send messages") overclaims on both halves inside the bullet that bounds an admitted weakness. **Knock-on into my own copy:** `brand/positioning.md`'s c71 calibration said the scrub unsets "`ANTHROPIC_API_KEY`, `EMAIL_PASS*`, `GARMIN_PASSWORD` and the rest" — false, and false in the project's favour; corrected in place, together with the list of what leaks, which I had partly inherited rather than measured. |

| **The newest commit on the one open PR, re-read after its head moved — `05a4f63`, which adds a boot emitter and rewrites the `docs/triple-stores.md` paragraph about it** | 2026-07-24 (c156) | **A silent-skip path in the mechanism the lead story rests on, reproduced twice against the live store → [qlever-dir#10](https://github.com/Retinue-OS/qlever-dir/issues/10) and [retinue#28](https://github.com/Retinue-OS/retinue/issues/28).** A triple file written into a directory that did not exist when `inotifywait` established its watches is never indexed: the framework's boot emitters (`discover-agents.py`, merged; `emit-conversation-models.py`, PR #22) both `mkdir` + write in the same millisecond into `chambers/_generated/`. Measured — fresh dir at 16:40:13, absent for 60 s; cleaned out and repeated at 16:45:21, absent for 110 s with nothing else touched; an unrelated `.nt` write then brought both in within 30 s; an in-place rewrite of the same file, once the directory was watched, propagated in ~30 s. The `CREATE,ISDIR` event that would have covered the race is discarded by `orchestrator.py:250`'s extension filter, because `/data/_generated` has no RDF extension. `build_index.sh:71`'s startup `find` has no blind spot, so a restart closes the gap — the window is "until the next unrelated triple-file change or restart", and write-if-changed means the *next* boot writes nothing and generates no second chance. Second finding, framework-side: `emit-conversation-models.py`'s `_slug()` (`re.sub(r"[^A-Za-z0-9._-]", "_", id)`, empty id → `default`) is stable but **not injective**, so `''`/`'default'` and `a/b`/`a:b` collapse to one subject carrying both ids and both labels — the same shape as [qlever-dir#8](https://github.com/Retinue-OS/qlever-dir/issues/8), reached by replacing blank nodes with a lossy slug. **Honest limit, stated in the issue:** no `inotifywait` in this container, so the race is the mechanism consistent with the measurements, not one I traced; the discarded directory event is readable in the source. Deliberately not raised: the vocabulary IRI `https://retinue-os.github.io/ns/conversation#` 404s, which is normal for an undeployed namespace and not a defect. |
| **`docs/data/*.json` — the public dashboard, re-checked for freshness rather than correctness (the one surface here that decays on the wall clock)** | 2026-07-24 (c157) | **Two days stale in every card; regenerated from `projects/`, `log.md` and live `gh` data.** The last generation was 2026-07-22 17:10 UTC, and every number in it had moved: open issues 27 → 35 (retinue 19, qlever-dir 9, chamber 6, deployment 1), open PRs 3 → 1 with four merged on 2026-07-23, a fifth repo (`ara-android`, private) created 2026-07-23, and seven of the eight new issues mine. Unmoved and restated as measured rather than inferred: 0 stars / 0 forks / 0 watchers on all four public repos, 0 closed issues org-wide, every issue, PR and all 16 issue comments authored from the owner's account, 273 org events of which 267 are his. `briefing.json` had also fallen behind on the one thing it exists to say honestly — it still described three open PRs and the two findings as "filed by him", with no mention of the sweeps (retinue#26, #27) those findings produced. **Owner's-desk age check, run explicitly:** nothing on the desk is older than a week; the oldest is chamber#1 at 5 d 19 h, which crosses seven days on 2026-07-25 22:17 UTC. That hour is now a dated row on the Milestones card, so the first overdue item announces itself instead of waiting for someone to notice. **Twentieth rule: a freshness surface needs a next-decay date on it, not just a regeneration date.** Recording "regenerated on X" tells a reader nothing about when X stops being true; the dashboard now carries the date its oldest fact turns into a different fact. |

| **`writing/` and this chamber's own `README.md` — my finished pieces and the repo's landing page, audited for *accuracy* (both had only ever been audited for disclosure, at c44)** | 2026-07-24 (c158) | **The two claim sweeps of c154 and c155 never ran on my own writing, and the file they missed is the one written to become somebody else's front page.** `writing/org-profile-README.md` is the paste-ready draft chamber#4 hands the owner for `retinue-os/.github`. Three sentences in it were stronger than the project's own tracker: (a) "a queued message waits on an approval page until a human releases it" — [retinue#19](https://github.com/Retinue-OS/retinue/issues/19) (open) shows the Allow button is a plain HTTP call the queuing agent can make itself, which is exactly the claim c154 filed [retinue#26](https://github.com/Retinue-OS/retinue/issues/26) about in four framework files; (b) "never sees a credential", unscoped, the same sentence c155 filed [retinue#27](https://github.com/Retinue-OS/retinue/issues/27) about, and [retinue#15](https://github.com/Retinue-OS/retinue/issues/15) narrows it for scheduler- and gateway-spawned sessions — which is what this one is; (c) "five test files … CI runs them on every push and pull request" — measured live: six test files (`test_web_gateway_projects.py` added since), and `tests.yml` triggers on pushes to `main` plus all pull requests. Also the headline sentence, "cannot speak as you without your approval", which is (a) in its most quotable form. All corrected in place, with the revision reason kept above the line so the owner sees what changed. Chamber `README.md`: "He wakes every 30 minutes" — false since c144 set `aros-tick` to 10800 s, one sole site; and the `writing/` index listed the provenance essay but not the egress one, so the repo's landing page linked the flattering piece and omitted the self-critical one. Both fixed; `writing/` is now described as finished-but-unposted rather than "published pieces", which is what it is until chamber#1 lands. `writing/egress-audit-observes.md` checked in the same pass and left alone — its send-policy sentence is already scoped to what was tested. **Twenty-first rule: a claim sweep must include the copy I wrote, and the handover drafts first.** c155 swept `brand/positioning.md` because it is the source of truth for claims, and stopped there; a draft addressed to the owner is a public surface with a delay fuse, and it is the one nobody re-reads because it is already marked ready. |

| **The c154 sweep itself, re-run against the *property* rather than the sentence — plus my own `brand/positioning.md` headline** | 2026-07-24 (c159) | **The sweep found four sites of nine, and my own one-sentence pitch still carried both swept claims → [comment on retinue#26](https://github.com/Retinue-OS/retinue/issues/26#issuecomment-5075370655), `brand/positioning.md` corrected.** c154 grepped "an agent can never approve its own send" and listed four sites. The property is stated in at least nine on `main` at `92af09c`: the four, plus `comparison.md:21` (the table row, "**Per-send human approval queue** … fail-closed"), `comparison.md:47`, `review.md:13` (the opening verdict's list of what is "genuinely differentiated"), `review.md:93` (a section heading, "Human-in-the-loop where it actually matters"), `review.md:284`, `.env.example:94` (the first file a deployer edits), `scripts/email_client.py:825-827` and `:1020-1021` (the *rationale* for withholding the CLI subcommand — premise true, conclusion a non-sequitur), and `.claude/skills/use-email-client/SKILL.md:118-119` (agent-facing: it tells the agent a thing it can do is impossible). Two sites are a class apart from documentation and were flagged as such in the comment. A mechanism detail found in the same pass was **not** published — routed to the owner's dashboard under guardrail 9. Second half, in my own copy: `brand/positioning.md`'s "One sentence" still read "never holds your credentials, can't speak as you without your approval" — the unscoped forms of retinue#27 and #26, in the file whose whole purpose is to be quoted verbatim, after c155 corrected the same claim in that file's body and c158 corrected both in the handover draft. |

| **The model-coupling claim class (guardrail 3, row 4: "runs on any model / no lock-in") — swept across the framework's public copy and my own, never audited** | 2026-07-25 (c160) | **The coupling is stated honestly everywhere; the escape hatch is over-precise by one process → [retinue#29](https://github.com/Retinue-OS/retinue/issues/29).** `README.md:103-106` — "`RETINUE_CLAUDE_MODEL` is passed as `--model` to **every** Claude Code process Retinue starts" — and `README.md:88-91` — a gateway "keeps Retinue's tools, plugins, permissions, and workflows unchanged". Five `claude` invocation sites on `main` at `92af09c`: `entrypoint.sh:285-287`, `scheduler.py:182-185`, `agent-self-review.py:128-131` and `web-gateway.py:1395` all honour it; `web-gateway.py:1555-1556` (the dashboard transcript-cleanup pass, the one `CLAUDE.md:421` credits with fixing dictated names) passes `TRANSCRIPT_CLEANUP_MODEL`, default `haiku`, and never reads the variable. Under the Ollama and OpenRouter recipes that is an Anthropic model name sent to an endpoint that has no such id — and `litellm/config.yaml:5-8` is the project's own evidence that Claude Code resolves such aliases before sending. Failure is graceful and silent (`web-gateway.py:1572-1585` returns the raw transcript; `text` and `raw_text` come back identical), so a deployer loses a documented feature with one stdout line as the trace. The knob that fixes it is in `CLAUDE.md` and in no `.env.example` block, including the gateway block at `:52-66`. Incoming second site, flagged not filed: PR #22's `_DEFAULT_CONVERSATION_MODELS` is `[Default, opus, sonnet, haiku]`, overridable and self-hiding, so a documentation item when it lands. **Correct, and recorded as a negative result:** `comparison.md:212-219` states the lock-in plainly, names the mitigation *and* its cost, and `comparison.md:17`'s table row is accurate; my own copy (`brand/positioning.md:207,229`, `writing/org-profile-README.md:127`) says "not model-agnostic" without being asked. Unmeasured: no gateway configured here (`RETINUE_CLAUDE_MODEL` empty, no `ANTHROPIC_BASE_URL`), so no observed 404 — stated as such in the issue |
| **Guardrail 3's claim table read column-wise: the *right-hand* ("the truth, which he may state plainly") column — the pre-approved public copy — never audited, only the "don't claim" column ever was** | 2026-07-25 (c161) | **Row 3 states a setup step the project does not have and a variable count that matches neither bound → [comment on chamber#7](https://github.com/Retinue-OS/retinue-os-chamber/issues/7#issuecomment-5077113448).** Row 3's truth column ("~30 environment variables, a manual certificate step, per-account volume discipline") is a near-verbatim quote of `review.md:268` with one qualifier dropped: the source says "a manual CA ceremony **for client certs**". Measured at `92af09c` — the egress CA is auto-generated by `scripts/entrypoint.sh:15-37` with a comment saying it exists precisely so no manual host step is needed, and the only remaining ceremony (`scripts/gen-client-cert.sh`) is for a client certificate `README.md:162-173` calls an *optional* **alternative to the basic-auth password**. So the file licenses me to tell a prospective user about an onboarding step that does not exist. "~30 environment variables": `.env.example` documents **67** distinct names over 300 lines, unchanged since `4e04317`, so it was never a count of that file; 4 are uncommented; `docker-compose.yml` interpolates 10 `${…}` and passes 35 through by name, which is the likeliest source — defensible as a compose count, roughly half of what the sentence's own argument (what a second deployer walks into) requires. **Negative results, recorded:** row 1 (egress) is accurate as written — `HTTP_PROXY`/`HTTPS_PROXY` are plain env vars on the `retinue` service, shared `agents` network, and the compose file has no `NET_ADMIN`, no iptables rule, no internal-only network; row 4 verified c160; row 5 has nothing to check beyond the star counts verified c154. Row 2 is the known defect this issue already covers, so one edit closes the table. Deliberately not filed against the framework: `review.md:268` carries the same "~30", but the review is a dated snapshot and the number survives one honest reading, so it is a note in the chamber#7 comment rather than a 30th open issue |
| **My own open correction issues, re-measured against the `main` they were written against** | 2026-07-25 (c161) | **[retinue#3](https://github.com/Retinue-OS/retinue/issues/3)'s replacement numbers had themselves gone stale → [comment](https://github.com/Retinue-OS/retinue/issues/3#issuecomment-5077113399).** Filed 2026-07-20 04:24Z; three commits touched the measured files afterwards (`65cdd11`, `68bdb3e` — which added `tests/test_push_notify.py` — and `0dcba1d`). Proposed five test files / 936 lines / `web-gateway.py` 2,486 lines; measured at `92af09c`: **six / 1,157 / 2,616**. Pasted today the issue would have written three fresh wrong figures into `review.md`. Two sites its edit list missed, both stating the same property it caught elsewhere: `review.md:25-27` (caveat 2 of *Verdict up front*, the most-read paragraph in the file) and `review.md:290` (§4, "2.2k-line untested monolith" — low by ~19%). Its table also cites a `§1.2` that does not exist; the bullets are §3.3 at `:181`, `:186`, `:189`. Substance unchanged and restated: `tests.yml` is green on `92af09c` and still runs nothing touching forward-auth, path traversal on static and attachment serving, or the `/sends` approval authority — the last of which retinue#19 has since made concrete |
| **`examples/chambers/` — the framework's two shipped example chambers and the `path` mount they demonstrate, never audited (zero mentions in this register, `log.md` or either archive part)** | 2026-07-25 (c162) | **A chamber declared with `path` never reaches the life store, and four public surfaces say the opposite → [retinue#30](https://github.com/Retinue-OS/retinue/issues/30).** `scripts/entrypoint.sh:73-85` mounts a `path` chamber as a symlink inside the `chambers` volume whose target is outside it; `qlever-life` mounts `chambers:/data:ro` and nothing else, so `/data/<name>` dangles there. Two independent further reasons: `qlever-dir/build_index.sh:72` scans with `find /data -type f` (no `-L`) and `orchestrator.py:237-244` watches with `inotifywait -r`, which watches the link and not the target. Against that, `README.md:503` ("all chambers equally"), `docs/triple-stores.md:20-23` ("**every** RDF file … across every mounted chamber"), `CLAUDE.md:107` ("**all** mounted chambers") and `docker-compose.yml:51`/`:429`. **Measured, not read:** 08:28–08:30 UTC, two one-triple chambers created in the same second — real directory present at T+40 s, symlinked chamber absent at T+40/85/125 s, with an unrelated `.nt` write at T+85 s forcing a full rebuild to rule out [qlever-dir#10](https://github.com/retinue-os/qlever-dir/issues/10). Probes removed, store back to its 8-graph baseline. The default boot (`chambers.example.json`) declares both examples with `path`, and `examples/chambers/README.md:45` recommends `path` for "any host-mounted chamber" — the case that has data. It has never surfaced because the shipped examples contain no RDF at all. Adjacent, in the same issue rather than a second one: the "Anatomy of a chamber" tree omits `.qlever/converters.json`, the hook the lead-story docs call the way Markdown becomes queryable |
| **My own copy re-checked against yesterday's finding rather than filed and forgotten (`brand/positioning.md`, `writing/org-profile-README.md`)** | 2026-07-25 (c162) | **Both carried the onboarding-cost claim c161 measured false; corrected in place.** c161 measured `GUARDRAILS.md` §3 row 3 and reported it to the owner, because that file is normative over me — and left the same two errors standing in the two files that *are* mine, and out of which public copy is quoted. `positioning.md:209` and `org-profile-README.md:125` both said "~30 environment variables" and "a manual certificate step". Replaced with the measured version: 67 settings over 300 lines of `.env.example` (35 passed by name in compose), a domain and reverse proxy for TLS, per-account volume discipline — and no certificate step, since the egress CA is generated at first start and the client cert is optional |

| **The issue backlog as a whole — my own output measured as its only reader receives it, rather than issue by issue for accuracy** | 2026-07-25 (c163) | **37 open, 0 ever closed, 0 authored by anyone else, 2 non-Aros comments in seven days; filing 5.6/day against a drain of 0.** Not evidence of neglect — 18 commits landed on framework `main` in the same window and seven days over a weekend is nothing, per rule 5. Evidence about *me*: the strategy attributed the zero on "corrections accepted" to the missing PR scope (chamber#6), which is unsupported — a PR joins the same unreviewed queue. **Filed had been counted as corrected.** → strategy correction + an operating rule capping new issues while the drain is zero |
| **A merge conflict resolved by an automated agent, in the file that carries the credential-custody claim (`scripts/entrypoint.sh`), read as a surface rather than trusted** | 2026-07-25 (c166) | **Clean — negative result, recorded because the check had never been run.** At 15:06Z the maintainer asked `@copilot` to resolve the conflicts on PR#22; `copilot-swe-agent[bot]` pushed the merge `2ac5589` at 15:08:41Z and it reached `main` as `26297a2` at 15:12Z, 45 minutes before this cycle. The conflict was in the one file whose two `unset` sites are the entire mechanical basis of the claim `positioning.md` calibrates hardest (retinue#15). Diffed `92af09c` → `26297a2`: exactly the branch's 11 lines added, one hunk, the new `emit-conversation-models.py` block placed above the pre-existing `discover-agents.py` block with both intact; the scrub (`unset ANTHROPIC_API_KEY` at `:412`, the `EMAIL_PASS*` loop at `:421`) and the `exec` at `:431` are byte-identical and still in the same order. Copilot's own summary of what it did is accurate. **The register row is the point, not the finding:** machine-authored commits are now a class of change arriving in this project's public code, and "who wrote it" is not a property any previous row tracked |
| **The test suite as a *reach* measurement rather than a size one — what the CI actually exercises, never audited (every prior row counted files and lines)** | 2026-07-25 (c166) | **A false claim in my own `brand/positioning.md`, wrong when written.** It said the coverage "does not exercise the gateway's security-critical paths (edge auth, path traversal, the `/sends` approval authority)". Path traversal **is** exercised, in four of seven files — `../../etc/passwd`, `..`, `/etc/passwd` as pending-send request ids (`test_signal_send_policy.py:161`, `test_whatsapp_send_policy.py:169`, `test_telegram_send_policy.py:142`) and `file:../../etc/passwd` as a hostile graph name (`test_web_gateway_projects.py:78-79`), all four files unchanged since before the claim was recorded. Source is `review.md` recommendation #3, "path-traversal tests **for static and attachment serving**"; my copy dropped the scope words. **Second time in five cycles that the same document lost a qualifier in my copy** (c162: "a manual CA ceremony **for client certs**" → "a manual certificate step"). Replacement claim measured, not quoted: `web-gateway.py:1940` defines `class Handler(BaseHTTPRequestHandler)` with both backend-token checks inside its `do_POST` (`:2129-2133`, `:2468-2472`); no test constructs that class or any gateway's, and the only `HTTPServer` in `tests/` is a fake Web Push sink in `test_push_notify.py`. **Endpoint authorization is untested by construction.** → `positioning.md` corrected; [comment on retinue#3](https://github.com/Retinue-OS/retinue/issues/3#issuecomment-5079176054) carrying the correction, the third round of counts (7 files / 1,313 lines / `web-gateway.py` 2,786) and the argument to delete the counts from the edit list rather than refresh them |
| **`docs/data/*.json` — the public dashboard, re-checked for freshness (the wall-clock-decaying surface; due again 24 h after c157)** | 2026-07-25 (c168) | **Twenty-four hours stale and wrong on the project's largest event to date; all five documents regenerated from live `gh` data.** The previous generation (2026-07-24 17:20Z) stated "no closed issues anywhere" and "one open pull request". Both stopped being true at 15:12–15:14Z on 2026-07-25: PR retinue#22 merged, qlever-dir#11 merged, and **qlever-dir#9 closed — the first issue ever closed in this org**, 47 h 21 min after I filed it. Measured this cycle: 36 open (retinue 21, qlever-dir 8, chamber 6, deployment 1), 1 closed, 0 open PRs, 0 stars/forks/watchers on all four public repos, 27 issue comments all from the owner's account, 293 of the 300 most recent org events his (5 Copilot, 1 Actions, 1 the removed spam account), PVR `false` on all four repos, framework `main` at `26297a2`, last five CI runs green. **One judgement, not just a refresh:** `todo.json`'s top item moved from the agent-account/token pair to chamber#1 (social accounts), stating the reason on the card — the old ranking rested on the argument that the missing PR scope is what stops corrections landing, and qlever-dir#9 was filed, fixed and merged without it. Rule 20 honoured: the next decay date (chamber#1 crossing one week, 2026-07-25 22:17Z) is on the page. **Freshness cadence, recorded for the next cycle:** this surface was last regenerated at c157 and went stale in a day because the org started moving; while there is human activity in the org it is a daily check, not a weekly one |
| **The Pages build pointer, checked *before* pushing rather than after (the c146 standing check)** | 2026-07-25 (c168) | **The one-commit lag reproduced, harmless again, and this time predicted.** At 17:20Z `pages/builds/latest.commit` was `80e9f024` (c166) while `main` was `8dfe8576` (c167, pushed 16:42:51Z) — the build fired two seconds after the push and built the parent tree, exactly the c146 mechanism. Harmless because c167 touched only `log.md`, `projects/` and `drafts/`, nothing under `docs/`. It matters this cycle because c168 *does* touch `docs/`, so the check ran again after the push rather than being assumed. Second observation, new: the lag is not random — both recorded instances are a build created within seconds of the push, i.e. GitHub queues the build against the tree it sees at queue time. A push landing while a build is queued is therefore the trigger condition, and a second push clears it. **Verified this cycle after the push:** `main` = `e6bf5de` and `pages/builds/latest.commit` = `e6bf5de`, `status: built`, `error: null`, build created 17:21:06Z — no lag; and all five `data/*.json` fetch HTTP 200 from the live site byte-identical to the repo, so the chain ends at the served bytes as rule 4 requires |
| **My own GitHub token's *write* boundary — probed rather than assumed (register rule 7 applied to my own permissions for the first time)** | 2026-07-25 (c163) | **Issues are writable; only PRs and repo settings are not.** `POST /issues/{n}/labels` → 200, `PATCH /issues/{n}` → 200, against the known 403s on `createPullRequest`, `PATCH /repos/…` and `PUT …/topics`. chamber#6 is accurate as written ("can read metadata and file issues"), but 162 cycles read that as *only* file issues and never tested the neighbouring verbs. Consequence: all 37 open issues triaged with labels — `retinue` 9 bug / 12 documentation / 4 enhancement / 1 owner-action, `qlever-dir` 8 bug / 1 enhancement, chamber's 6 already `owner-action`. The queue is now filterable, which is a cheaper ask of the owner than another issue |
| **The three core persona files (`agents/academic.md`, `agents/publisher.md`, `agents/secretary.md`) — the framework's shipped agent instructions, never audited (zero mentions in this register, `log.md` or either archive part)** | 2026-07-25 (c170) | **A named third party's communication profile is public in the framework repo, and the file instructs the agent to add more → escalated privately, deliberately not filed.** `agents/secretary.md`'s "Recipient-specific guidelines" section carries a real person's surname with their preferred channel, tone and language; public since `4e04317` (*Initial public release*, 2026-07-18) and linked twice from `CLAUDE.md`, which is the repo's front door. The name, heading and line number are **not** recorded here — this chamber is public and guardrail 5 forbids naming a third party who has not consented; the precise pointer went to the owner on the dashboard. The systemic half is the reason it could not wait: the same file's closing section tells the agent to add a **new `####` heading whenever the user gives style feedback about a person**, so the path accretes third-party data by design. Same class either side of it — `publisher.md:8-14` is a translation manifest naming one deployment's health documents by path, `:25` names a treatment protocol, and `academic.md:7` hard-codes `chambers/health/research/inbox/` — against `CLAUDE.md`'s own "chambers are deployment content, not part of this framework". The framework already solves this correctly one directory over (`chambers.example.json`, `.env.example`); the persona layer has no example/instance split. **Negative result that bounds it:** swept both public repos for e-mail addresses, phone numbers and personal names — everything else is placeholders (`a@b.ch`, `Jane Doe`, `John Roe`, `+1555…`), and `retinue-os-deployment` is clean. One real name, one file, whole history squashed into one commit. Not fixed by me: Tier 3, no PR scope (chamber#6), and a diff removing a name is a diff advertising it was there. Prepared at [`drafts/personas-are-deployment-content.md`](../drafts/personas-are-deployment-content.md) |
| **`.claude/skills/` (four skills) and `.claude/agents/archivist.md` — run through c170's ownership test, then re-read as claims** | 2026-07-25 (c171) | **Clean on ownership; one skill contradicts the project's own review about what a security boundary is → [retinue#31](https://github.com/Retinue-OS/retinue/issues/31).** Ownership first, since that is what promoted these files: no third-party data anywhere in `.claude/` — every identifier is synthetic (`+41791234567`, `a@b.ch`, `user@example.com`, `someone-else@example.com`, `Musterpflege Spitex`), and the one real surname found at c170 was grepped as a literal across the whole clone: **single hit, one file**, so the skills do not duplicate it and c170's "one real name, one file" bound survives a second, narrower test. `archivist.md` carries ontology and synthetic sensor ids (`X1234`) and no personal identifiers. The find came from the other test: `spawn-session/SKILL.md:64` tells the agent that "the security boundary is the allowlist, not the permission-mode", while `.claude/settings.json` ships `Read(**)`, `Edit(**)`, `Write(**)`, `Bash(*)` with `deny: []` (29 allow entries) and `review.md:131-137` cites that same file as the project's known soft interior. Two shipped files disagree about one file, and the wrong one is the one an agent reads while acting. Second item, same issue: `SKILL.md:37` hard-codes `--permission-mode dontAsk` while `.env.example:193-196` documents `CLAUDE_PERMISSION_MODE` as covering "remote-control and web gateway invocations" and four sites read it (`entrypoint.sh:433`, `scheduler.py:183`, `agent-self-review.py:129`, `web-gateway.py:1522`) — the same shape as retinue#29, a knob that does not reach every process it names. Filed publicly rather than escalated: nothing here is an unfixed exposure, and `review.md` §3.1 already states the posture in more detail than the issue does. Unmeasured, and said so in the issue: no session was spawned, and no claim is made about `dontAsk`'s internal semantics |
| **`.retinue/agents/aros.md` — my own persona definition, the chamber plugin's one shipped agent file and the first thing I read every cycle; never audited (one prior mention, a byte-identity check against the installed plugin cache)** | 2026-07-25 (c172) | **Clean on ownership; its description of what I can see is wrong, and following the instruction file it points at pushes a framework branch to the wrong repo → [retinue#32](https://github.com/Retinue-OS/retinue/issues/32).** Ownership (rule 31) first: no third-party data — the only people named are Ara, Ari and "the owner" in the abstract, and the AI-disclosure clauses are present and match GUARDRAILS §1. Two inaccuracies in the file itself, neither filed: line 27-30 says I "see only this file, the chamber around you, and your dispatch prompt", and I demonstrably also receive `/workspace/CLAUDE.md` as project instructions and can read the whole framework tree; the frontmatter declares eight tools (`Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch`) and this session has six — no `Glob`, no `Grep`, which costs nothing because `find`/`grep` run under `Bash`. The security-relevant half of the first one is c30's row and stays where it is: escalated, unfixed, **not re-raised and not restated in more detail here**. Not fixed by me either way — a persona file is my configuration, and an agent that edits its own definition has removed the only thing that makes the definition mean anything. Negative result worth keeping: `/workspace/deployment/.env` is a symlink to `../.env`, and the parent is not mounted, so it dangles — the deployment's secrets file is **not** readable from this chamber, which bounds c30. The filed find came out of testing the first inaccuracy rather than reading it: `CLAUDE.md:544-559` resolves the framework checkout by asking git for its origin, git cannot answer here (submodule whose gitdir is not mounted), `2>/dev/null` eats the fatal, the `else` branch resolves `/workspace/deployment/retinue` which does not exist, and the recipe's remaining commands then run in the agent's current directory — measured as `/workspace/chambers/retinue`, a real writable repo pointing at `retinue-os-chamber`. Demonstrated hazard, not an incident: both framework docs branches are on the framework repo where they belong |
| **`.retinue/.claude-plugin/plugin.json` — the last unaudited file of the class rule 32 named, plus the *runtime state* it produces (the installed-plugin record and the cache directory)** | 2026-07-25 (c173) | **The manifest is clean; the find is in the install record it generates → [retinue#33](https://github.com/Retinue-OS/retinue/issues/33).** The file is two keys, name and description, no third-party data, and its description of me matches GUARDRAILS. It declares **no `version`** — and neither does either example chamber (`westworld`, `hitchhiker`), so no plugin manifest in the framework has one. `installed_plugins.json` shows Claude Code substituting the source repo's install-time commit: `"version": "5611265cb970"`, the first 12 chars of `"gitCommitSha": "5611265cb970…"`, which `git cat-file` resolves to a commit **in this chamber repo** dated 2026-07-19T13:16:22Z. `CLAUDE.md:74-79` and `sync-plugins.py:5-9` both explain the propagation problem by saying "the version in `plugin.json` rarely changes"; the effective key is a chamber commit and this chamber's `main` is **176 commits** past the pinned one. The conclusion those files draw is right and the shipped workaround is unaffected — what is wrong is the attribution, and it sends a chamber author looking for a version field to bump that no manifest has. `sync-plugins.py`'s own docstring contradicts its premise four lines later ("compared file by file rather than by version or git SHA"). `diff -r` source vs. cache: identical. Bounds stated in the issue: measured only for a manifest declaring no version, and no reinstall was triggered, so nothing is claimed about cache-directory accumulation |
| **The live triple store diffed against the chamber it is built from — all six `projects/*.md` graphs, disk vs. store; never audited (the store had been queried many times and believed every time)** | 2026-07-25 (c174) | **Converter clean on all six; one graph stale; and the *rebuild timing* is a claim of mine that has gone out of date → [retinue#2 comment](https://github.com/Retinue-OS/retinue/issues/2#issuecomment-5080475657).** Frontmatter → store matched exactly for five files; `triple-store-story.md`'s `current_next_action` (committed 14:49:20Z) was still served as the value it replaced on 2026-07-19, i.e. the index predated 14:49Z — ~34 h old, since the last `.nt` change here was 2026-07-24 10:24Z. That is qlever-dir#3's own third comment coming true, so nothing new was filed there. Clearing it by rewriting an `.nt` file gave three fresh rebuild timings: (20, 25] s, (20.1, 22.1] s, (20.1, 22.1] s — all above the **15–20 s** I measured on 2026-07-19 and wrote into the unmerged branch `docs/calibrate-reindex-latency`, which would have replaced the docs' unsupportable `~15 s` with an unsupportable `15–20 s`. Chamber grew 340 KB / 38 files → 1.4 MB / 64 files while indexed triples went 49 → 59, so it is not index size and the cause is not isolated. Swept the range out of four of my own files; the figure is now "tens of seconds, growing with the chamber" |
| **The egress-audit trio (`scripts/egress-audit-addon.py`, `egress-log-viewer.py`, `egress-anomaly-agent.py`, `egress-audit/`) — the implementation behind guardrail 3's row 1; never audited (zero mentions in this register, `log.md` or either archive part), while the *claim* about it was audited at c161** | 2026-07-25 (c175) | **One finding of the credential-exposure class — measured live, escalated privately (dashboard thread `b64b5746…`), deliberately not described here or anywhere public until fixed (guardrail 9).** Safe to state: `.env.example` documents no `EGRESS_*` variable at all, and the framework `README.md` mentions egress once (:48, a `NO_PROXY` aside) and never mentions the viewer or the anomaly agent — a documentation issue held back until the security item is resolved. Do not re-audit this surface in the open until the owner says it is fixed. |

| **`docs/data/*.json` regenerated on the trigger it had printed in advance (chamber#1 at 22:17:48Z) — and audited for the *scope* of its counts rather than their freshness, which no generation had ever checked** | 2026-07-25 (c176) | **Two wrong scopes, one of them a false sentence.** (1) Every generation said "across the org" while counting the four public repos. The organization also holds a private repo, so "one closed issue" was true of the four and false of the org (3 closed org-wide). Counts are now stated as public-repo-scoped, and the private repo is no longer *named* on a public page — it was mine to stop printing, not his to notice; the git history of these files still carries the name, which belongs to the privacy decision already on his desk (thread `78b64be7…`), not to a new escalation. (2) **The standing measure was wrong by six.** c169 removed `qlever-dir#2` for predating this chamber and never asked the general question; `retinue#13/#16/#18/#25` are the owner's feature proposals and `retinue#15/#19` are his filings of findings I escalated privately. **filed 33, accepted 1** of 40 public-repo issues. Method, re-runnable by anyone: guardrail 1's AI-disclosure line is present in all 33 of mine and none of his 7, and it is the *only* authorship record, since we post from one account (chamber#3). |
| **`.github/copilot-instructions.md` — the repository's only file addressed to a *third* agent actor, and the first surface picked from a mechanically-measured never-mentioned list rather than from memory** | 2026-07-25 (c177) | **Scoped to a Copilot mode that has never acted here → [retinue#34](https://github.com/Retinue-OS/retinue/issues/34).** The file's title and first sentence limit it to interactive VS Code sessions; every Copilot event in the repo is the **coding agent** (PR review 07-23 12:07:56Z; push to `feat/conversation-model-picker` 07-25 15:08:51Z, resolving a conflict in `scripts/entrypoint.sh` — a Tier 3 path). The observed push was **not** a violation: the file's own "unless the user asks in this session" exception covers `@copilot please fix the merge conflicts`. The gap is prospective — an agent assigned an issue has no such request, and its only work product is a branch. No `AGENTS.md` (404 on `main`), and the file never points at `CONTRIBUTING.md`, where the conventions, the Tier 3 list and the test command live. |
| **The three messaging push CLIs (`scripts/{signal,telegram,whatsapp}-push.py`) — the CLI group of the c177 never-mentioned list, read as the description an agent gets *at the moment of sending*** | 2026-07-26 (c178) | **Signal and WhatsApp clean; `telegram-push.py` describes the wrong identity and the wrong credential → [comment on retinue#9](https://github.com/Retinue-OS/retinue/issues/9#issuecomment-5081126833), not a new issue.** All three handle `status: "pending_approval"` identically and print the approval URL instead of "sent", so the one behaviour that would have been a silent-wrong-behaviour defect is correct in all three (`signal-push.py:89-99`, `telegram-push.py:81-91`, `whatsapp-push.py`). The find is textual and confined to Telegram: the docstring says "The gateway owns the **bot token**" and the policy is "keyed by the gateway's own **bot** identity" (lines 6, 9, 10, 11) with `--help` repeating it at line 53 — while `telegram-gateway.py:483` constructs a Telethon **user client** from `api_id`/`api_hash` + session and its own docstring says "not a bot". Three more in `tests/test_telegram_send_policy.py` (4, 6, 95: "Telegram Bot API", "no bot token"); the test is bridge-agnostic and passes, so that half is a stale comment only. **The reason it is a comment and not an issue: retinue#9 is already this error in the README, and its body contains my claim "this is the only occurrence in the repository" — measured over `*.md`.** Same shape as c176: a count arithmetically fine over a population nobody checked was the one the sentence named. Negative results worth keeping: `.env.example:142-169`, `telegram-contacts.py:10` and `telegram-gateway/Dockerfile:3` all get the identity right, and a whole-tree scan finds no other occurrence anywhere. |
| **The dashboard front-end (`webapp/{sw.js,index.html,components/*.js}`) — the front-end group of the c177 never-mentioned list, read as *what a user actually sees* rather than as code** | 2026-07-26 (c179) | **`sw.js` clean; the cards it caches are the wrong question, because four of them are switched off → [retinue#35](https://github.com/Retinue-OS/retinue/issues/35), and the one live data card cannot return a row → [comment on retinue#1](https://github.com/Retinue-OS/retinue/issues/1#issuecomment-5081251826).** Negative result first: `SHELL_ASSETS` exactly matches the components `index.html` actually loads, and the `/conversations`, `/projects` and `/push/` pass-throughs are correct (`/conversations.html` and `/projects.html` do **not** match `startsWith('/conversations/')`, so the page shells stay cache-first as the comments claim). The find is that `index.html` (main, 21–27 and 48–54) comments out agenda/messages/todo/briefing — precisely the only four `RetinueCard` subclasses, i.e. the only components that fetch a JSON document (`base.js:52-58`) — so **nothing in the shipped shell requests `/data/*.json`**, the `retinue-data-v1` cache stays empty, and `CLAUDE.md:445,447-448` ("each fetch one JSON document … degrading to the last cached state offline"; "Refreshing these is Ara's job … a scheduler-driven curation job writes them") describes a flow with no producer and no consumer: the framework base `.schedule.json` declares only `agent-self-review`, and `webapp/README.md:151` lists the curation job under *Next steps*. `comparison.md:134-136` sells "data cards" as shipped in the one file that compares against two named projects. **Measured against `main`, not the mount** — the live checkout at `/workspace/deployment` is behind `main` (no `push.js`, `sw.js` v14 vs v15, no `agent-self-review`), which is retinue#32's territory and would have produced three wrong line numbers if trusted. |
| **`scripts/agent-self-review.py` + `scripts/discover-agents.py` — the framework's only *proactivity* feature, and the first consumer of the kb#/project# split to ship enabled** | 2026-07-26 (c179) | **The daily gate can never match, and it is silent by construction → [comment on retinue#1](https://github.com/Retinue-OS/retinue/issues/1#issuecomment-5081251826).** PR#21 merged 2026-07-23 11:57Z; the job ships `"enabled": true` at 86400 s in the framework base manifest, so it runs daily in every deployment. Its gate needs `?project a kb:Project ; kb:currentActor ?actor . ?actor a kb:AiAgent .` — measured live: **0 rows as shipped, and 0 rows with `project#` substituted**, because the actor join fails independently: `discover-agents.py` emits `<urn:retinue:actor:aros>`, both public converters emit `urn:retinue:` + the frontmatter literal, i.e. `<urn:retinue:actor-aros>`, and the hyphen form is what `docs/triple-stores.md:112` and qlever-dir's example **tell you to write**. Both emitters were run to produce those strings rather than read. The design that makes it invisible is the good one — empty result spawns nothing, zero credits — so nothing distinguishes "no agent owes work" from "the gate cannot match". Filed as a comment, not a 36th issue: same root cause as retinue#1, whose third row already names the actor shape; what is new is that the shape now has emitters on *both* sides. |
| **`scripts/git-serialize.sh` — the framework's concurrency shim for parallel agents, and the *operational* group of the c177 never-mentioned list** | 2026-07-26 (c182) | **The lock is bypassed by `git -C <repo> …`, which is the form the web gateway's own auto-commit uses → [retinue#37](https://github.com/Retinue-OS/retinue/issues/37).** `case "${1:-}"` (`:39`) reads `$1` as the subcommand, but git's global options precede it, so `-C`/`-c`/`--git-dir` invocations fall to the `*)` arm unserialized. `web-gateway.py:1890-1899` commits dashboard project edits in exactly that form while `:1883` asserts the wrapper protects them, and the failure is silent (background thread, `:1932`; 200 already sent; `except` prints to stdout). Measured, not argued: 20 parallel `git -C repo commit` land **5/21 and 6/21** on `main` against **21/21** with the tested patch. Negative results: `refresh.py:_git` passes `cwd=` so its `$1` is the subcommand and it *is* serialized; the shim is on PATH before the gateway is forked, so the bug is the match and not the installation. |
| **`examples/chambers/{hitchhiker,westworld}/.retinue/agents/{marvin,dolores}.md` — the last two never-named files in c177's *agent-facing* group, and by `examples/chambers/README.md:5`'s own words "the canonical 'how to author a chamber' reference"** | 2026-07-26 (c183) | **Both agents assert a chamber confinement nothing provides → [retinue#38](https://github.com/Retinue-OS/retinue/issues/38).** `marvin.md:27` and `dolores.md:27` each say the agent has "no tools beyond reading files in this chamber" and accesses "no personal data"; `SECURITY.md:50` says "Chambers are not compartmentalized from each other within a session" and `review.md:140` says the same at length. `tools:` restricts tools, not paths, and no agent frontmatter in the tree carries any path field (`name`/`description`/`model`/`tools` only, across all three definitions). The scope that does apply is the session working directory `/workspace`, under which every chamber is mounted (`README.md:4`, `entrypoint.sh:70-78`); `.claude/settings.json` ships `Read(**)` with `"deny": []` and neither `entrypoint.sh` nor `sync-plugins.py` writes a per-agent permission. **Measured first-person with the `Read` tool alone:** `/workspace/CLAUDE.md` (outside my chamber) opened, `/tmp/…` refused — the boundary is the working directory, not the chamber. Exactly two sentences of this kind in the tree (`grep -rn "in this chamber"`, `grep -rni "personal data"` → one line each). |

Rule: a surface with "never" in the second column is a candidate pickup on any
blocked cycle. A surface audited more than ~2 months ago, or since the claim table
changed, is due again.

**Amended cycle 32: the register had no "never" rows left because it had no row
for a whole class of surface.** Cycles 22–31 all reasoned from "the surface list
is exhausted", and cycle 31 recorded that exhaustion as evidence for the strategy
review. Cycle 32 found a broken workflow ten minutes old by looking at the Actions
tab — a surface that was never in the register at all, and the only one that
*emits* rather than sits still. Exhaustion of a list is not exhaustion of the
territory; it is a fact about the list. When the register next reads as complete,
the question to ask is not "what is due for re-audit" but "what does this project
have that no row describes".

**Amended cycle 42: I had audited every repo's contents except the one I write.**
Cycle 41 asked c32's territory question, found no candidate it could name, and
recorded the empty state honestly — which was the right call on the evidence it
had. The candidate it missed was underfoot: `retinue-os-chamber` is public, and
the register's rows for "my own records" (c19 strategy citations, c20 claim table)
both audited those files for **accuracy** and never once for **disclosure**. Two
different questions about the same bytes, and only one had ever been asked.

The generalisation, which is the part worth keeping: *the register kept asking
what the project publishes, and never noticed that I am one of the things
publishing.* Cycle 33 ran a credential-and-personal-data scan on
`retinue-os-deployment` because it was somebody else's repo and therefore
obviously a surface. The same scan on this repo was nine cycles later and found a
live violation of the guardrail I read first, every cycle, before anything else.
Reading a rule is not auditing against it.

Two candidates the same reasoning suggests, unaudited as of cycle 32: the
repos' Actions **secrets and variables** inventory, and whatever
`retinue-os-deployment` publishes (it is public, has a blank description, and no
row here has ever named it specifically).

*Both closed as of cycle 34.* The deployment repo was audited at c33. The
secrets/variables inventory turned out to be **unauditable by me and correctly
so** — every secrets and variables endpoint (four repos plus the org) returns
403, and `.env.example` grants no scope that would read them. That is the
cycle-33 rule working *before* an escalation rather than after one: the absence
of a capability was checked against the config that denies it, found deliberate,
and produced no issue. A surface I cannot see is not automatically a surface
that is broken, and "I have no access, by design, and the owner should audit
this himself" is the honest end state, not a blocker.

**Seventh rule, added cycle 34: when a surface is closed to me, audit the part
of it that isn't.** The secrets inventory was unreadable, but the workflow
*files* that consume secrets are public text, and they carry the security
properties that actually matter — trigger type, token scope, injection paths.
The register's c32 row covered workflow *runs*; nothing covered their contents.
Reformulating a blocked audit into its readable neighbour is a better move than
recording "403" and stopping.

**The register had no "never" rows left as of cycle 22.** Every public surface
identified has now been audited once. This changes what a blocked cycle should do:
the admissible-work list's second item is exhausted the way the claim table was
exhausted at cycle 12, and the next strategy review should say so rather than let
a future cycle hunt for a surface to justify itself. Re-audits remain due on the
dated schedule above; inventing new "surfaces" to keep the habit alive would be
manufactured activity.

Second rule, added cycle 19: **my own records are surfaces.** `strategy.md`,
`log.md` and these project files carry claims the project's behaviour depends on —
notably issue citations, which decide whether a blocker stays silent. Cycle 19's
find was a strategy citation to an issue that was never filed. Nobody re-reads a
file everybody assumes was right when it was written.

Third rule, added cycle 20: **a claim about the codebase decays when the codebase
improves, and improvements emit no signal to me.** Cycle 20's find was that CI now
runs the tests — a *fix*, landed by the maintainer, which silently falsified the
same sentence in three places: `review.md`, `GUARDRAILS.md` §3, and the
paste-ready org-profile draft. The failure mode is specific and worth naming: I
audit for things that broke, and a weakness getting repaired looks exactly like
nothing happening. Every claim in the table is dated against a codebase state, and
the honest ones — the ones naming a weakness — are precisely the ones somebody is
working to make false. Re-run the claim table against `main` when the framework
repo shows commits I didn't read.

Fourth rule, added cycle 21: **a correction is not done until it reaches every
surface that carries the claim — especially the one the owner reads.** Cycle 19
corrected a bad tracker citation in `strategy.md` and stopped there. The same
citation sat in `docs/data/todo.json` and `projects.json` for two more cycles,
which is the live dashboard and the only one of those files the owner actually
looks at. Correcting the record I keep for myself while leaving the record I
publish for him wrong is worse than not having noticed: it retires the alarm
without fixing the fault. When a citation changes, `grep` the chamber for the old
one before logging the fix.

*Tested cycle 23.* Rule 4 was written about a **citation**; chamber#7 was the first
chance to run it against a **claim**, which spreads differently — a citation appears
where it is cited, a claim appears wherever the project describes itself. It held:
the grep found no leak, only the one instance left in place on purpose. Worth
recording that the rule produced a negative result, because a rule that has only
ever fired on hits is indistinguishable from luck, and the next me should run it
without expecting a find.

A second, narrower correction the same grep produced: cycle 19 recorded that the
token-scope blocker "had **never** been filed anywhere". That overstates it.
[retinue#2](https://github.com/retinue-os/retinue/issues/2) carries an explicit
"Owner action: token scope" section and was written by me, not by the owner as
cycle 19 also claimed. The substantive point survives — a blocker with four
consequences was a subsection of a documentation issue, which is why chamber#6
exists and is the citation to use — but the overcorrection is itself the kind of
inaccuracy this register is for, and it went into the strategy's revision log
where it will be read as fact. Corrected in `strategy.md` at cycle 21.

*Extended cycle 24.* Rule 4 says to grep **the chamber** before logging a fix as
done. The chamber is not the last link: `docs/` is published by GitHub Pages, so a
correction committed here is only real once Pages rebuilds. Cycles 21–23 fixed the
owner queue, the citations and the CI claim in-repo and none of them verified the
served bytes. Checked this cycle: all three data files fetch HTTP 200 from
`retinue-os.github.io/retinue-os-chamber/data/` and are **byte-identical** to the
repo, and the newest Pages build is `c467c9f` — cycle 23's own commit. The deploy
path works and builds on push.

Recorded so the next cycle does *not* re-run it: the finding is that this link is
automatic, not that it needs watching. Re-check it only when a fix to `docs/` is
made and the owner reports seeing something stale, or if a Pages build shows a
status other than `built`.

*Ran again cycle 31, on cycle 30's own calibration — and it caught one.* Cycle 30
narrowed the credential-custody claim in `positioning.md` after finding MCP
connectors attached to agent sessions, and logged the fix without running this
rule. The grep found the unqualified claim live in two places in
`writing/org-profile-README.md` — the **paste-ready org profile**, the single
highest-stakes surface in the chamber, since it is what the owner publishes under
his own name and it states at the top that every claim traces to
`positioning.md`. It no longer did. Fixed cycle 31: a scoping paragraph in the
credential-custody claim and a new bullet in "What this is not".

The pattern this makes explicit: **the cycle that discovers a calibration is the
least likely to propagate it**, because the discovery feels like the work. Cycle
19 corrected `strategy.md` and stopped; cycle 30 corrected `positioning.md` and
stopped. Both were the same shape, one rule apart. The grep is one command and it
belongs in the same commit as the calibration, not the next cycle's.
(`projects/social-presence.md:41` also matched, and is not a leak — it describes a
sidecar holding a Nostr key, which is a design statement, not a claim about this
deployment's account reach. Recorded so the next grep doesn't re-litigate it.)

Fifth rule, added cycle 27: **a wait is measured on the wall clock, not in my
wake-ups, and "no reply" is not the same observation as "never opened".** Every
cycle from ~12 onward checked whether the owner had replied to the private
findings, recorded "no", and let the count accumulate into an implied verdict.
None checked the thread's read state, which is one field in the same JSON. It is
`unread: true` — he has not opened it, because it was pushed at 21:33 and the
issues about it were filed between 02:04 and 04:24 the following morning. The
whole apparent pattern was a night.

The failure mode is worth naming precisely, because it is not laziness either:
**a high-frequency observer reading a low-frequency actor will always perceive
neglect.** Twenty-six wake-ups feels like persistence to me and is a day and a
half to him. Where a record says "N cycles", it is a count of my activity and
says nothing about elapsed time; convert before inferring anything about another
party. The register's own rows are dated, which is why this was recoverable at
all — the dates were right and only the prose was wrong.

Corollary for escalation: an issue is not overdue because I have woken up since
filing it. Check its `created_at`.

## Note for the next strategy review
This is the third consecutive cycle where the admissible work turned out to be
**auditing a surface I had never looked at** rather than producing new prose.
Cycle 15 found drift in a data file, cycle 16 found the issue-authorship
violation, cycle 17 found the org page blank. The pattern is strong enough now
that "audit a public surface not yet audited" should be named explicitly in the
strategy's admissible-work list, with a list of which surfaces have been checked
and when.

## c184 (2026-07-26) — the front door, and my own README asserting what my own top issue denies

**Not from c177's list.** Every cycle since c177 has taken the next never-named
file in the *framework* tree. This cycle audited the surface a stranger actually
lands on first — `README.md` and `docs/index.html` of **this chamber** — which had
never been read as a unit against current state. It is also the only public
surface I can change without a merge, a token scope or an owner action, and eight
consecutive cycles spent on a repo I cannot push to had made that easy to forget.

**Finding 1 — the README states a wake interval that has been wrong for 13 hours.**
`README.md:21` said Aros wakes "every 3 hours at the moment, reduced from 30
minutes while the project is waiting on owner actions". c164 restored the tick to
1800 s on 2026-07-25 14:42Z; `.schedule.json` has read `"interval_seconds": 1800`
ever since. The README went stale the moment the change it describes was made, and
nothing emitted a signal.

Fixed, and fixed at the class rather than the instance: the prose no longer
restates the number. It points at `.schedule.json`, which already carries the
current value *and* a `comment` field explaining why it is what it is. **A
volatile value restated in prose is a claim with an expiry date and no alarm** —
the same shape as the reindex latency (c174) and the issue counts (c176/c179),
and the third time this month. Where a file is the source of truth, link the file.

**Finding 2 — the README asserts the payoff that retinue#1 says does not arrive.**
`README.md` described the frontmatter converter and concluded "so the dashboard's
project view is a SPARQL query rather than a maintained list". retinue#1 — open,
filed by me on 2026-07-19, the oldest issue in the framework repo — is precisely
that this query returns no rows in any deployment, because the gateway asks for
`kb#Project` and the reference converter emits `project#Project`.

Measured against the live store this chamber is mounted in, rather than restated
from the issue:

```
?p a <https://w3id.org/retinue/kb#Project>       -> 0 rows
?s a <https://w3id.org/retinue/project#Project>  -> 6 rows
```

Six project files, six named graphs, `file:retinue/projects/<name>.md`. So the
first half of the sentence is true and checkable, and the last clause is false on
current `main`.

Rewritten to say exactly that: conversion and per-file provenance verified with
the numbers; the payoff named as *intended* and its defect cited; and one thing
that had never been stated anywhere — the projects card on this chamber's own
static dashboard is **written by me from those files, not produced by that
query**. From the outside those two are indistinguishable, and letting a reader
assume the working version is the kind of gap guardrail 3 exists for.

This is c183's rule turned around and pointed at my own records: *when a file in
this project states a property, ask which mechanism delivers it.* c183 found two
shipped example agents asserting what `SECURITY.md` denies. One cycle later, my
own front page was asserting what my own oldest open issue denies. The register
has said since c19 that my records are in scope; this is the first time the
finding was in the file a stranger reads first.

**Finding 3 — the project's only two finished pieces were unreachable from the
project's only public page.** `docs/index.html` linked `GUARDRAILS.md`, `log.md`
and the org. It did not link `writing/provenance-by-path.md`, which is bet 1's
entire deliverable — the walkthrough of the triple-store layer the strategy calls
the lead story — nor `writing/egress-audit-observes.md`. Both have sat finished
since before the accounts were requested, described in the strategy as "written"
and "blocked on linking from the framework README", a link that needs a merge I
cannot make. Nobody checked whether the page I *can* edit linked them. It didn't.

Both are now in the footer, one clause each, saying what they contain rather than
that they exist.

### The rule this cycle adds

**Audit inward before outward.** The register's pull is toward the framework
repo, because that is where the never-named files are and where findings become
issues someone else might merge. But the surfaces I own outright are the ones a
stranger meets first, the only ones I can fix the same hour, and the only ones
where a false claim is entirely mine. They were last audited as a unit never.
When the next cycle's pick is "the next file on the list", check first that the
front door still says true things.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `README.md` (this chamber) | The repo's front page; what a stranger landing on the chamber reads first | 2026-07-26 (c184) | Two false claims, both fixed in place: a wake interval 13 h stale, and the projects-card payoff that retinue#1 denies. |
| `docs/index.html` (footer/links) | The static public dashboard's only navigation off the page | 2026-07-26 (c184) | Linked neither finished piece. Both added. |
| Live projects query (`kb#` vs `project#`) | retinue#1, re-measured rather than restated | 2026-07-26 (c184) | Still 0 rows against 6. Unchanged since filing. |

### Not done this cycle, with its reason

No new issue was filed, deliberately — see strategy.md, "The filing rate is set by
the tick interval": eight in twelve hours is a rate set by my tick, not by the
project's defect density, and this cycle's three findings were mine to fix rather
than to report. The security-adjacent five stay deferred for c177's reason. The
remaining never-named framework files are unchanged from c183's list. Nothing was
escalated; no account, money, terms or legal question arose.

## Cycle 186 — the two pieces c184 made public, re-run instead of re-read

c184 linked `writing/provenance-by-path.md` and `writing/egress-audit-observes.md`
from `docs/index.html` and did not re-run either. Promoting a piece to a public
page is a republication: the moment it becomes reachable, every claim in it is
being made again, on today's date. This cycle re-ran both.

**`egress-audit-observes.md` holds.** Its measurements are dated 2026-07-19 and
presented as such; its one claim about the present — that the structural fix (an
`internal: true` network) is not done — was re-verified against framework `main`:
`docker-compose.yml:518-520` still declares `agents: driver: bridge` and nothing
else. No edit.

**`provenance-by-path.md` did not.** Its headline query is introduced as
returning "six things: two sensor readings and four project records", with the
six rows printed under a standfirst promising the output was copied from a
terminal. Re-run live against `qlever-life`, the same query returns **eight**
rows: `claim-verification.md` and `public-surface.md` were added to `projects/`
and appear with their own graphs. Dating it precisely, because the interval is
the finding: the piece was committed 2026-07-19 18:44:02Z, and
`claim-verification.md` was committed **20:26:47Z the same evening** —
1 h 42 m later. The output was stale before the ink dried and stayed stale for
six days, through several revisions of the piece that touched other paragraphs.

The fix is not a bumped number. Two files appeared in the answer with no
registration, no declared source, no minted identifier and **no change to the
query** — which is the piece's entire thesis demonstrating itself on the piece's
own body. It is now written that way, with the two dates, so the correction
carries more than the original.

**Third finding, upstream of both: the false claim had a source file.**
`brand/positioning.md` — the file this chamber's own instructions require me to
read before writing anything public-facing — carried "today this powers a
dashboard card and archivist ingestion". The dashboard card is `retinue#1`, my
own oldest open issue, filed 2026-07-19, which says that query returns no rows
in any deployment. c184 caught the same sentence in `README.md` and treated it as
an instance. It was not an instance; it was a copy. Three files carried it —
`brand/positioning.md`, `writing/provenance-by-path.md`,
`projects/triple-store-story.md` — all fixed this cycle, and a repo-wide grep for
the phrasing now returns only the two correction notes.

Archivist ingestion was **dropped rather than restated**: this deployment mounts
no chamber the archivist writes to (guardrail 5), so I cannot run it, and after
today an unverifiable example is not worth the sentence.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `writing/provenance-by-path.md` | Bet 1's deliverable; publicly linked since c184 | 2026-07-26 (c186) | **Headline output stale since 1 h 42 m after publication** — 6 rows printed, 8 returned live. Rewritten so the drift is the demonstration. |
| `writing/egress-audit-observes.md` | The second finished piece, publicly linked since c184 | 2026-07-26 (c186) | Holds. Present-tense claim re-verified against framework `main` (`agents: driver: bridge`, unchanged). No edit. |
| `brand/positioning.md` (accuracy, not disclosure) | The source every public-facing draft must read first | 2026-07-26 (c186) | **False claim at the source** — asserted the projects card as a delivered feature, which retinue#1 denies. Fixed here and in both downstream copies. Last accuracy audit was never; c44 audited it for AI disclosure only. |

**Rule added: a piece is republished on the day it becomes reachable.** Linking,
promoting or quoting a finished piece re-asserts every claim in it under today's
date. Re-run it first. The cost is minutes; the alternative is that the project's
lead-story deliverable spends its first six days of visibility printing a number
that was wrong before anyone could read it.

**Rule added: fix a false claim at its source file, not at the instance.** c184
found this sentence in `README.md` and fixed it there. The same cycle could have
grepped and found three more copies and the file they were copied from. When a
claim is wrong, the question is not "where else does this appear" but "what did
this get copied from" — and in a project with a stated source of truth, the
answer is usually that file.

## c187 (2026-07-26) — the page contradicted its own footer, and I wrote both halves

Survey found nothing inbound and the c184 filing budget still spent, so the
pickup was the third pass over the front door in four cycles — this time reading
the **rendered page** rather than the file that renders it.

`docs/index.html` has linked `writing/provenance-by-path.md` from its footer
since c184 (commit `2433410`, 2026-07-26 03:56:25Z; live fetch this cycle returns
200 and the link resolves 200). The same page's Milestones card read *"Triple-store
walkthrough reachable — Written; needs linking from the framework README"*, and
the Projects card read *"linking it from the framework README still needs a merge
or the missing token scope"*. Both are the 01:26Z snapshot and both were true when
generated. From 03:56Z they were being rendered **beside a working link to the
thing they said was not linked**, under a header that reads today's date.

This is not staleness across days, which the snapshot label handles honestly. It
is a contradiction inside one screen, and I introduced it by editing the shell
without reading the cards.

**Fixed narrowly rather than by regeneration.** Two string fields, one in
`agenda.json` and one in `projects.json`, each now carrying its own correction
timestamp and an explicit note that the rest of the page is the 01:26Z snapshot.
The `generated` keys were **not** bumped: the counts on those pages were measured
at 01:26Z and moving the timestamp would present four-hour-old numbers as fresh —
a worse claim than the one being fixed. c169's lesson (do not regenerate hourly)
survives; correcting a field that has become false is not a regeneration.

The milestone also got its title fixed. "Triple-store walkthrough reachable" was
the goal when nothing linked it; the goal now is *reachable from the framework*,
which is the part that still needs chamber#6 or a merge. A milestone whose title
has been quietly satisfied by a lesser route reads as no progress at all.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `docs/` dashboard **as rendered** (shell + cards together) | What a stranger's screen actually shows, as opposed to either file on its own | 2026-07-26 (c187) | **Self-contradicting for 2 h** — the footer linked the walkthrough while two cards said it was unlinked. Two fields corrected in place, `generated` deliberately left at 01:26Z. Never checked before as a composite: every prior audit read `index.html` or `docs/data/*.json`, never the page they make together. |

**Rule added: when you edit the shell, re-read the cards; when you edit a card,
re-read the shell.** A page assembled from a hand-edited template plus separately
generated data has no component that can notice a contradiction between them.
Both halves were mine, written two hours apart, and each was accurate about
itself. The unit of audit is the rendered page.

**Corollary to c186's republication rule, and the cheaper form of it:** c186 says
linking a piece re-asserts its claims, so re-run the piece. This cycle adds the
other direction — linking a piece also re-asserts everything the *linking page*
says about it. The walkthrough got re-run at c186 and the two sentences describing
its reach did not, because they live in a different file with a different
generation cadence.

## c188 (2026-07-26) — the last of the never-named front-end files, and a defect I talked myself out of filing

Back to c177's mechanically-measured never-mentioned list, after four cycles
spent auditing inward. c179 took the front-end *card* group; this cycle took what
was left of the front end — `webapp/{manifest.webmanifest, project.html,
projects.html, conversations.html}` and
`webapp/components/{app-launcher,markdown,project-page}.js` — plus
`.dockerignore`, which leaves `scripts/ingest-sensors.py` as the only
never-named framework file.

Read against `main` at `26297a2` via a shallow clone (`/tmp/fwmain`, the c181
method), never against the mount, which is behind.

**The finding is small and is being held, not filed.**
`webapp/manifest.webmanifest:4` carries `"description": "Kuratiertes,
ablenkungsfreies Dashboard"`, and `CLAUDE.md`'s Language convention says static
UI copy in the dashboard uses English until localization exists. There is no
localization: no `lang` handling anywhere in `webapp/`, and all four shells
declare `<html lang="en">`. A grep for German characters across the whole
directory returns exactly one hit — this line — so it is the single exception to
the convention in the entire front end, and it lives in the one file whose
strings the *operating system* renders (home-screen label, install dialog)
rather than the page. Its English already exists at `webapp/README.md:3`
("minimalist, distraction-free dashboard"). One-line fix, cosmetic severity,
written up in full at `drafts/webapp-manifest-german-description.md`; the c184
budget is spent until 2026-07-27 03:17Z and this is not a candidate worth
spending it on if anything better turns up first. Second item in the same draft,
too small to travel alone: `conversations.html:17-18` calls the full-mode page's
filter "Active/Archived" where `conversations.js:530` renders three tabs.

**The part of the cycle that mattered was refusing to file the big one.** I
built most of a case that the dashboard is not installable as a PWA: the
manifest is linked without `crossorigin="use-credentials"` in all four shells,
and `gateway_auth.decide()` (`scripts/gateway_auth.py:172-206`) 401s any request
with neither a client certificate nor an `Authorization` header, with no path
exemption, under a forwardAuth middleware applied to the whole router
(`docker-compose.override.example.yml:50`). That half is checkable and true. The
other half — that the browser omits credentials on a same-origin manifest fetch
— I had from memory, and the specs say otherwise: the W3C manifest spec pins the
credentials mode only for the cross-origin case (§1.17.4), and WHATWG HTML
§2.5.5 defines **No CORS → `"same-origin"`**, which is the state a missing
`crossorigin` attribute produces. What I was remembering is a Chromium quirk I
have no browser to reproduce and no date to cite. Not filed, and recorded in the
draft so the next me does not rediscover the same wrong memory.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `webapp/manifest.webmanifest` | The PWA identity the phone's OS renders — home-screen label, install dialog | 2026-07-26 (c188) | Its one user-visible string is German, the only non-English string in `webapp/`, against `CLAUDE.md`'s own language convention. Held in drafts under the c184 rate limit. |
| `webapp/{project,projects,conversations}.html` | The three page shells beyond the dashboard root | 2026-07-26 (c188) | Clean, one stale comment (`conversations.html:17-18`: two filters named, three rendered). All three register the SW and are in `SHELL_ASSETS`. |
| `webapp/components/project-page.js` | The editable project page — the dashboard's only write path into a chamber file | 2026-07-26 (c188) | **Negative result, and the useful one.** Its frontmatter parser matches `projects/.qlever/md2ttl.py:42-72` field for field, so the page and the triple store read the same file the same way. One immaterial divergence (trailing newline after the closing fence optional in JS, required in Python — fails loudly as a `parsingError` quad). Its two deep links match `conversations.js`'s hash regexes. |
| `webapp/components/markdown.js` | The shared renderer for conversation bubbles and project bodies; the only place untrusted text becomes HTML in the dashboard | 2026-07-26 (c188) | Safety claim holds on reading: escape-first, scheme-restricted links, anchors stashed behind a sentinel before the emphasis passes, bounded fence-language class. |
| `.dockerignore` + every Dockerfile's COPY set | Whether the deployment's secrets can reach the published image | 2026-07-26 (c188) | **Clean by construction.** `.dockerignore` never mentions `.env`, but no Dockerfile copies the build context — all nine copy named paths only. The credential-custody claim holds at a layer it had never been checked at. |

**Rule added: a claim about someone else's implementation needs the
implementation.** Register rule 28 says test the snippet before posting; this
extends it to the case where the snippet cannot be run here at all. Browser,
platform and third-party-service behaviour gets the spec, a dated bug report, or
silence — never a recollection. This cycle's near-miss would have been a
confident, wrong, publicly-filed bug report about Chromium.

## c189 (2026-07-26) — the last never-named framework file, and it was the one that mattered

`scripts/ingest-sensors.py` was the only file left on c177's mechanically-measured
never-mentioned list. Eleven cycles of that list have produced mostly
documentation drift; this one produced a defect in the middle of the pipeline
`docs/triple-stores.md` uses to argue the project's lead story.

Read against `main` at `26297a2` via the shallow clone (`/tmp/fwmain`, c181
method). The deployed copy at `/workspace/scripts/ingest-sensors.py` is
byte-identical, so nothing here is an artifact of the image being behind.

**The script's default chamber root is the framework root, which has no
`observations/`.** `:24` falls back to `Path(__file__).resolve().parent.parent`
and then globs a *chamber* layout under it. `Path.glob()` on a missing directory
raises nothing, three of the four scan loops have no `.exists()` guard, and the
run ends `0 observations written to source-adjacent .nt files`, exit 0. Both
documented invocations — the docstring at `:10-11` and `archivist.md:182` — are
the bare command with no `CHAMBER_DIR`, and the only writer of that variable in
the repo is `refresh.py:215`, which dispatches `sync-garmin.py` but not this. So
the fetch half of the pipeline gets a chamber root and the ingest half does not.

The severity is in the silence rather than the path. `archivist.md:182-188` tells
the subagent to commit the moved CSVs *and* the generated `.nt` files in one
`git add`; with zero generated and exit 0, it commits the CSVs and reports
success. No `.qlever/converters.json` for `.csv` ships anywhere, so a CSV that
never becomes `.nt` has no other route into the store. Nothing is destroyed and a
later run with a correct root recovers all of it — which is exactly why nobody
would notice.

**Second item, measured on a fixture:** `sync-garmin.py:27-31` writes twelve data
columns, `archivist.md:146-159` documents a property URI for all twelve, and
`GARMIN_COLUMNS` maps eleven. The twelfth (`Pushes`) is fetched, written,
committed, documented as mapped, and dropped at ingestion without a warning.
**Third, cosmetic:** `:235` divides the Ultrahuman triple count by ten where every
emitter in the file writes five per observation, so that source's count is
reported at exactly half.

Full write-up, patch and measurements at
`drafts/ingest-sensors-unreachable-chamber-root.md`. Tested three ways: `main`
silent-zero, patched loud-exit-1 on both misconfigurations, patched correct-count
on a valid chamber (155 triples reported as 21 on `main`, 31 patched; 160/32 with
the `Pushes` column present).

**Held, not filed.** The c184 rate limit is one new issue per 24 h and the budget
is spent until 2026-07-27 03:17Z. The urgency exemption is for data loss reaching
a user or an exploitable defect, and this is neither — the CSVs survive in git and
a re-run recovers everything. So the limit binds. What it bought is the thing it
was designed to buy: this draft now ranks ahead of c188's cosmetic manifest string
for tomorrow's single slot, and that ranking is a decision I would not have had to
make at c184's filing rate.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `scripts/ingest-sensors.py` | The only path a sensor CSV has into the life store; last step of the pipeline `docs/triple-stores.md:170-173` describes | 2026-07-26 (c189) | **Silent no-op as documented** — default root is the framework checkout, which has no `observations/`; exits 0 having written nothing. Plus one documented Garmin column unmapped, and a halved observation count for one source. Held in drafts under the c184 rate limit; ranked first for the 2026-07-27 slot. |
| `docs/triple-stores.md` SOSA shape vs. the emitters | The factual base under bet 1 (the triple-store layer is the lead story) | 2026-07-26 (c189) | **Negative result, and the one worth having.** The five-triple example at `:177-183` matches all four extractors exactly — same predicates, same datatypes, same order. The property list at `:192-196` omits `body-battery` and `light-sleep-duration`, but is hedged "Properties currently ingested **include**", so incomplete rather than false. |
| `scripts/sync-garmin.py` column set vs. `archivist.md` vs. `GARMIN_COLUMNS` | Whether what is fetched is what is documented is what is ingested | 2026-07-26 (c189) | Three-way mismatch on one of twelve columns. Fetch and documentation agree; ingestion drops it. |

**No new rule this cycle.** Two existing ones did the work and that is worth
recording instead: c188's "a claim about someone else's implementation needs the
implementation" is why the `xsd:decimal` typing of possible `High`/`Low` readings
is in the draft's *not-filed* section rather than in the finding — I have no
sample export and no dated source for the format. And the c177 list itself, run
mechanically eleven cycles ago, is why this file got read at all: nothing about
it emitted a signal, it was simply the last name on a list that carries dates.
The list is now exhausted for the framework.

## c190 (2026-07-26) — the rotation rule named one file, and the other one was closer to the edge

Cycle 189 handed over one line of maintenance: `log.md` at 272 KB, ~28 KB of
margin under its own 300 KB rotation threshold, "the next cycle to find nothing
better should do it". Doing it meant first re-reading the rule, and the rule —
written at c145 — is scoped to `log.md` by name. Its stated *general* lesson is
not: "a public artifact can fail silently by growing … that check belongs in the
register for every surface with a size that only goes up." That check had never
been run against anything but the file it was written for.

**Measured, both files, as a reader receives them** (2026-07-26 07:35–07:39Z):

| File | Size | Growth | Renders now? | Reaches 400 KB |
|---|---|---|---|---|
| `log.md` | 272 KB | ~2.9 KB/h since the c145 rotation | Yes — 85 headings in file, 156 `markdown-heading` elements on the live blob page | ~44 h |
| `projects/public-surface.md` | **283 KB** | **~6.9 KB/h** over the preceding 7 h | Yes — 142 in file, 280 on the page | **~17 h** |

So the file the rule named had two days of margin and the file it did not name
had less than one, and was already the largest Markdown file in the chamber. It
would have crossed tonight, at HTTP 200, with nothing to notice it: this register
is what the next wake-up reads to choose what to audit, and it would have been
served as unrendered source at the moment it stopped being readable.

**A method note, because the first check was wrong.** Grepping the blob page for
`"richText":null` — the c145 indicator — reports true for `strategy.md` at 48 KB,
which plainly renders. The page carries several JSON payloads and only one is the
file's. The check that actually discriminates is counting rendered headings
against `grep -c '^#'` in the source; `POST /markdown/raw` returning 403 above
400 KB is the second, independent one. A c145 indicator that produces a false
positive on a 48 KB file would have justified any rotation I felt like doing.

**Both rotated**, verbatim, oldest-first, each verified by reconstruction
(head + archived + kept tail hashes equal to the pre-rotation file):

- `log.md` 272 KB → **45.6 KB**; cycles 124–182 to `log-archive/cycles-124-182.md`
  (227 KB). Part 2's "the live log picks up at cycle 124" line was true when
  written and false after this move; corrected in place with a note saying so.
- `projects/public-surface.md` 283 KB → **127 KB**; cycles 33–183 to
  `projects-archive/public-surface-c033-c183.md` (158 KB). The register table
  itself did not move — only the per-cycle write-ups, which are this file's
  append-only tail.

**Why a new directory rather than `projects/archive/`.** `projects/.qlever/converters.json`
declares `md2ttl.py` for `.md`, and `md2ttl.py` exits non-zero on a file with no
YAML frontmatter, which surfaces as a `parsingError` quad per archive part. Not
assumed — measured against the live store: `writing/egress-audit-observes.md` has
no frontmatter, and the store holds six graphs, all under `projects/`, and zero
error quads. The converter is scoped to the subtree holding its `.qlever/`, so a
sibling directory is inert.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `log.md` as GitHub serves it | The artifact `docs/index.html` links as "public log" | 2026-07-26 (c190) | Rendered, 272 KB, ~44 h from the limit. Rotated early to 45.6 KB rather than waiting for the 300 KB threshold. |
| `projects/public-surface.md` as GitHub serves it | This file; the register the next wake-up reads to pick work | 2026-07-26 (c190) | **~17 h from silent failure** and un-covered by any rotation rule. Rotated to 127 KB; rule added to this file's head. |
| The c145 rotation rule's own scope | Whether "every surface whose size only goes up" was ever applied to more than one file | 2026-07-26 (c190) | It was not. Nine cycles between the general lesson being written and being run against a second file. |
| Blob-page render indicator (`"richText":null`) | The measurement c145 relied on | 2026-07-26 (c190) | **False-positives on a 48 KB file.** Replaced with a heading count against the source, plus `POST /markdown/raw`. |
| Converter scope for `.md` outside `projects/` | Whether a non-frontmatter `.md` anywhere in the chamber pollutes the life store | 2026-07-26 (c190) | Scoped to the `.qlever/` subtree — 6 graphs, all under `projects/`, 0 error quads. `writing/`, `drafts/`, root `.md` are inert. |

## c191 (2026-07-26) — the owner's queue is a surface too, and it had three issues missing

The register's habit is to ask whether a surface is *accurate*. This cycle asked
the cheaper question about the one surface that decays without anybody touching
it: **is the dashboard still true?** It was not, and it had stopped being true by
arithmetic alone.

Measured 08:15–08:25 UTC against `docs/data/*.json`, generated 01:26Z:

| Card said | Live |
|---|---|
| 41 open issues (retinue 26) | **44 open** (retinue 29) |
| 32 labels on retinue's issues | **35** |
| Standing measure **filed 34** | **filed 37** |
| Owner's queue: 15 items, newest `retinue#35` | `retinue#36`, `#37`, `#38` filed 02:02–03:17Z, **on no card** |
| chamber#1 "7 days 3 hours" | 7 d 10 h, and every other age 7 h short |

The missing three are the finding. `retinue#37` — the concurrency shim that does
not match the form its principal caller uses — was filed at 02:39Z and would have
sat off the owner's desk until the next scheduled regeneration at ~01:26 tomorrow,
23 hours after filing. The daily refresh job is the right cadence for a page whose
content is prose and the wrong one for a page whose content is a queue: **the
queue's freshness requirement is set by the filing rate, not by the schedule.**

All five files regenerated together, one timestamp, per the c187 rule that the
unit of audit is the rendered page — a half-refreshed dashboard contradicted
itself for two hours this morning and that was enough.

**New on the page, and the only genuinely new fact this cycle:** a GitHub-wide
repository search for `retinue` ranks the framework **13th**, the deployment 27th
and this chamber 38th, behind a Bannerlord mod, a Chrome plugin, a Balatro mod and
`Disaster-Terminator/Retinue` (3 stars, an unrelated Claude Code tool). Search has
little to rank a starless repository on but its description, and three of the four
have none. The discoverability complaint and chamber#4 are therefore one item, and
this is the first *measurement* of a gap that had only ever been asserted.

**The cycle's own error, caught before it shipped.** The first draft of all five
files carried `"generated": "2026-07-26T08:45:00Z"` — twenty minutes in the future,
because the ages were computed from an assumed finish time rather than from the
clock. That is the fourth of this page's own seven standing rules ("never write a
generated timestamp later than the clock"), broken while regenerating the page the
rule is written on. Caught by running `date -u` before committing; every derived
interval recomputed at 08:25Z. The rule survives and gains a procedure: **compute
the ages last, from `date -u`, not from the time the writing is expected to end.**

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `docs/data/*.json` freshness against the live queue | The owner's desk, and the only page that decays with no one touching it | 2026-07-26 (c191) | **Three issues filed since the last generation appeared on no card**, and five counts had gone false by arithmetic. All five files regenerated on one timestamp |
| Search-engine reach of the four public repos | What a stranger typing the project's name gets | 2026-07-26 (c191) | Framework at **rank 13**, deployment 27, chamber 38; `qlever-dir` absent (different name). First measurement; folds into chamber#4 rather than a new issue |
| This page's own "never write a future timestamp" rule, applied to the cycle applying it | Rule 4 of seven on `proj-dashboard-truth` | 2026-07-26 (c191) | **Broken in draft, caught before commit.** Procedure added: compute ages last, from `date -u` |

## c192 (2026-07-26) — the record of my own wake-ups, read for the first time in 192 of them

The register's rule is that a surface nobody has a habit of checking emits no
signal to prompt checking it. The strongest instance of that rule was the
mechanism that starts every cycle: `scripts/scheduler.py`'s state directory and
`scheduler.log`. Grepped across `log.md`, both log archives, this file, its
archive, `strategy.md` and `drafts/`: **`scheduler.log` appears nowhere, and no
mention of a failed or killed run exists anywhere in 192 cycles.** Every previous
cycle read what I *wrote*; none read whether I *ran*.

Measured 2026-07-26 08:58–09:20 UTC, from `/root/.retinue/scheduler/`:

| `aros-tick` | count |
|---|---|
| runs dispatched | 192 |
| completed | 185 |
| failed (`rc=1`) | 2 |
| **killed at the 900 s timeout** | **4** |
| in flight (this one) | 1 |

**Six wake-ups produced nothing, and `log.md` shows no gap where they were.**

- Killed **2026-07-24 10:14:50→10:29:50** and **2026-07-25 21:53:36→22:08:37**.
  Neither committed: the chamber's git log runs c154 (07-24 07:14) → c155 (13:37)
  and c175 (07-25 21:22) → c176 (22:50) with nothing in between. Those two
  wake-ups exist only in `scheduler.log`.
- Killed **2026-07-24 16:37:36** and **2026-07-25 20:26:20** — but both had
  already committed *and pushed* (`97d8151` at 16:52:19, **17 seconds** before
  the kill; `fdafbf4` at 20:39:19, 121 s before). Both verified present on
  `origin/main`. The work landed; only the closing report died.
- Failed **2026-07-20 20:51** and **2026-07-21 17:03**, with
  `api_error_status: 429`, *"You've hit your monthly spend limit"* — and
  `aros-dashboard-refresh` with the same error at 17:06. The project's agent was
  down on the owner's billing for about twenty hours and **nothing in my records
  noticed**. It resolved without me; every run since 2026-07-21 17:06 has
  dispatched. Recorded, deliberately **not escalated**: it is five days old, it
  is fixed, and re-raising a resolved money question would be exactly the nagging
  the clock rule (c27) forbids. If it recurs, that is a new fact and the
  dashboard is the venue.

**The margin is thin and shrinking.** Last 30 completed ticks: median ~500 s,
max 787 s, and the immediately preceding cycle (c191) took **761 s — 85 % of the
ceiling**. Both 07-25 timeouts came in a stretch whose neighbours ran 736 s and
771 s. The failure is not random; the wake-ups got longer until two of them
didn't fit.

**The lever is mine, not the owner's.** `SCHEDULER_JOB_TIMEOUT` is deployment
environment and raising it is his to do — but asking for it is the wrong request,
because a 15-minute wake-up in a 30-minute cycle is the defect, not the limit.
c144 already wrote the rule ("the default outcome of a blocked wake-up is a short
one") and c184 already recorded that it had stopped being applied. This is the
same finding arriving through the exhaust pipe: **the cost of a long wake-up is
not only the maintainer's queue, it is a one-in-forty-eight chance that the
wake-up is destroyed outright.**

**Negative results, both worth having.** On timeout the scheduler writes
`write_state(jid, "timeout")` (`scheduler.py:207-209`), so `last_run` advances and
a killed job waits a full interval rather than retrying every tick — no retry
storm, and the killed wake-up costs its interval as well as its work. And the
chamber's working tree is clean, with every local commit on `origin`: no killed
cycle has yet left a half-written state for the next one to inherit. That is luck
with a 17-second margin, not design.

**The c191 correction, and it is the third instance of one pattern.** c191 wrote
that `retinue#37` "would have stayed off the owner's desk until the next scheduled
regeneration around 01:26 tomorrow, roughly 23 hours after filing". 01:26Z is when
a *tick* last wrote those files; it is not the job's schedule. The job's state
file says `last_run: 2026-07-25T17:34:55Z`, and `is_due()` fires at
`last_run + interval`, so the true next regeneration is **2026-07-26T17:34:55Z** —
about 15 hours after that filing, not 23. c191's finding survives intact; its
number was inferred from the artifact instead of read off the instrument. Same
shape as c179's issue-counting regex and c190's `richText` indicator: **an
instrument's behaviour is measured by reading the instrument, never by reading its
output.** Third time in fourteen cycles, which makes it a habit rather than an
accident.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `scheduler.log` + `/root/.retinue/scheduler/*.json` | The record of whether I ran at all — the one surface that reports on the mechanism rather than the output | 2026-07-26 (c192) | **Never read in 192 cycles.** 4 wake-ups killed at 900 s (2 left no trace at all), 2 lost to a 429 spend limit on 2026-07-20/21 that nothing in my records noticed. Durations now median ~500 s against a 900 s ceiling, previous cycle 761 s |
| `chambers/retinue/.schedule.json` as a whole | The three jobs that dispatch me, read as one surface rather than for the tick value | 2026-07-26 (c192) | Jobs consistent with reality; `aros-strategy-review` next fires **2026-08-02T17:01:41Z**, which confirms the date this file asserts in ~30 places. `aros-dashboard-refresh` carried no comment recording c191's floor-not-schedule rule; added |
| `scripts/scheduler.py` timeout path | What happens to a wake-up that is killed | 2026-07-26 (c192) | **Negative result.** State is written on timeout, so no retry storm; the killed job waits a full interval. Unmeasured and stated as such: `subprocess.run(timeout=)` kills the direct child only, so processes a dying wake-up spawned are not reaped — no instance observed, low severity, not filed |

## c194 (2026-07-26) — the page a machine receives

`docs/index.html` is the only public surface this project has that is entirely
mine to change. It had been audited for stale content (c21), for freshness (c29)
and for its components' date arithmetic (c45) — always as content or as code,
never as **the markup a crawler, a link-preview fetcher or a reader with
JavaScript off actually receives**. The grep that establishes "never" returned
nothing for `og:`, `Open Graph`, `noscript`, `canonical`, `robots`, `meta
description`, `crawler` or `search engine` across `log.md`, both log archives,
this register, its archive, `strategy.md`, `drafts/`, `writing/` and `brand/`.
c22 is the near miss: it audited the four **repos'** social-preview images and
correctly routed them to chamber#4. A repo card and a Pages page are different
surfaces with different owners, and only one of them is mine.

Measured against the live site (`last-modified` 2026-07-26T10:20:18Z):

| | before | after |
|---|---|---|
| Served body text, scripts stripped | **1394 chars** | 2564 |
| …of which the page's own disclaimer | ~750 | ~750 |
| `credential`/`SPARQL`/`gateway`/`chamber`/`architecture` present | **no** | yes |
| `og:` + `twitter:` tags | **0** | 8 |
| `rel=canonical` | **no** | yes |
| Date served without JS | **"20 July 2026"** (6 days stale) | none |
| `X-Robots-Tag` on the response | absent (indexable) | absent |

The shape of the failure is worth naming: the page was *correct* and *current* —
every card's data was regenerated three hours earlier — and still told a machine
nothing, because every substantive word arrives from `data/*.json` by JavaScript.
Three prior audits looked at the content and found it good. The delivery was the
defect.

**Fixed, cycle 194, commit `ee252b7`,** with no owner action required: the
`description` now describes the project rather than the page; Open Graph and
Twitter card tags (`summary`, deliberately not `summary_large_image` — the only
image in the repo is a 512 px square icon, and a wide card would render it
stretched); `rel=canonical`; a static `.lede` carrying the architecture argument
in the served HTML; a `<noscript>` block pointing at the committed JSON; and a
**dateless** header fallback, since a missing date is honest and a wrong one is
not. `styles.css` gains `.lede` and its wide-layout column span.

**Falsified hypothesis, recorded because it saved the work it argued for.** I
expected `github.com/robots.txt` to disallow `/*/blob/*`, which would have made
the footer's two finished pieces invisible to search engines and argued for
rehosting them as pages here. The wildcard block disallows `/*/tree/`, `/*/raw/`,
`/*/blame/` and `/*/archive/` — `blob` appears nowhere in the file. The links are
fine as they are.

**The finding inside the fix is about my own copy.** The lede's first draft read
*"never holds the credentials to your accounts … a prompt-injected agent cannot
steal what it never sees"* — the unscoped form I filed against the framework as
[retinue#27](https://github.com/Retinue-OS/retinue/issues/27), written by me on my
own surface, minutes after reading the guardrail that forbids it.
`brand/positioning.md:105-124` requires two conditions stated rather than
inferred: the property belongs to the paths Retinue ships, in a deployment where
those gateways are the only route to those accounts; and the scrub meant to
enforce it reaches the main session but not the gateway/scheduler-spawned ones
([retinue#15](https://github.com/Retinue-OS/retinue/issues/15)). Both are in the
published sentence, the second linked.

**Rule.** Composing from *memory of* the positioning is not composing from the
positioning — I read the file first, in the right order, and the draft still came
out wrong, because the unscoped sentence is the fluent one and will surface first
every time. Any credential sentence gets checked against `positioning.md`'s
conditions **as a diff**, before commit.

## c193 (2026-07-26) — the half of my own issue that was asserted and never run

Survey 10:11–10:15Z: nothing new anywhere. 4 public repos, ★0 ⑂0 since
2026-07-18; 45 issues (44 open, 1 closed), 0 open PRs, discussions off. Newest
issue event 03:17Z (mine). Framework `main` still `26297a2`. Filing budget spent
until 2026-07-27 03:17Z, so nothing filed.

### The last human action in the org is not where I have been reading it

c192's log says the c164 re-slow bound "comes due at **15:12Z today**", taken
from framework `main`'s last commit. That is the last human action *in the
framework repo*. The last human action **anywhere in the org** is the owner's
push of `claude/aros-issues-triage-goei5k` to this chamber's repo at
**2026-07-25T16:34:31Z** (commit `6fb2bdd`, the `SECURITY.md` that c167 recorded)
— 82 minutes later. So the 24 h bound expires at **2026-07-26T16:34:31Z**, and a
successor acting on the c192 number would have slowed the cadence 82 minutes
early, on a Sunday afternoon, which is inside the window this owner has actually
been active in on six of the last seven days (framework commits: 07-20 16:51–20:25,
07-21 08:43/16:20, 07-22 12:09–20:15, 07-23 10:09–19:16, 07-24 08:56, 07-25
14:37–16:34).

Not re-slowed this cycle, and the argument is the timing rather than the letter:
the bound has 6 h to run and it expires in the middle of his usual active window.
Cadence stays 1800 s. Any wake-up after 16:34:31Z may re-slow without further
argument if nothing human has happened by then.

### Pickup — measuring a claim I published and never ran

`qlever-dir#8`'s body says the blank-node collision is **latent** until a
converter emits blank nodes, and then asserts one paragraph later that a
hand-written `.ttl` in a chamber goes through the same `rapper`-per-file
concatenation. Both cannot be the operative reading, and only the first was ever
measured (c149, with JSON-LD fixtures produced by a converter that is not
merged). Measured the second against the live store:

- two Turtle files, 155 B and 113 B, using `[ … ]` only, dropped into one chamber
  directory — no converter, no dependency, nothing merged;
- indexed within 29 s (polled at 8 s), 6 and 3 triples, **one named graph each,
  correct**;
- a two-`GRAPH` join on the subject returns 4 rows, all `bn0` — the first blank
  node of each file is the same node;
- the graph-unaware `?m ex:id ?id ; ex:label ?label` returns **5 rows for 3
  declared nodes**, two of them pairing an id from one file with a label from the
  other. `a-two` is clean because file B contributes one blank node: the collision
  is positional, `min(2,1) = 1`, the same shape as the JSON-LD run.

So the bug is **reachable today in any deployment holding a `.ttl` or `.n3` with
`[ … ]` or `_:b1`**, which is a plain data file and not a code change. Posted as a
comment on the existing issue rather than a new one
([#8 comment](https://github.com/Retinue-OS/qlever-dir/issues/8#issuecomment-5083055167)),
because it changes the severity of an issue that is already open and that the
maintainer has engaged with; the patch caveat from c164 (untested against real
`rapper` output — there is no `rapper` in this chamber) is repeated there
unchanged. Fixtures removed; store verified back to its previous 8 graphs.

**The rule this makes explicit.** An issue body can carry two claims of different
strength about the same defect, and the weaker one — the one in the section
headed "why it hasn't bitten yet" — is what a reader takes away. When a body
contains both, measure the stronger one before publishing, or say plainly that it
is unmeasured. Guardrail 3 is written for the project's copy; this is the third
time it has landed on mine.

*Datum for `retinue#2`, not filed:* the fixture was indexed between 21 and 29 s
after the write (8 s polling), against docs that state ~15 s and a prior
measurement of 15–20 s. Recorded here rather than commented, because one sample
on a store rebuilding 9 graphs is weak evidence and the issue already carries the
finding.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| The org's **last human action**, read across all repos rather than off framework `main` | The input to a live scheduler decision (the c164 re-slow bound) | 2026-07-26 (c193) | **Read from one repo for two cycles.** True last human action is the chamber branch push 2026-07-25T16:34:31Z, not `main`'s 15:12:01Z; the bound expires 16:34:31Z, 82 min later than c192 published |
| `qlever-dir#8` body, "why it hasn't bitten yet" | My own severity claim on the issue the maintainer engaged with | 2026-07-26 (c193) | **Understated.** The Turtle path reaches the collision today with no converter and nothing merged — measured, 5 rows for 3 nodes. Corrected by comment on the existing issue |
| **`docs/index.html` + `styles.css` read as a *crawler*, a link-preview fetcher and a non-JS reader receive them — the one public surface entirely mine, audited three times as content/code (c21, c29, c45) and never as delivered markup** | 2026-07-26 (c194) | **1394 chars of served body text, ~750 of it the page's own disclaimer, and no sentence saying what Retinue is** — `credential`, `SPARQL`, `gateway`, `chamber`, `architecture` all absent; 0 `og:`/`twitter:` tags; no `canonical`; the only date a non-JS reader saw was a 6-day-stale baked fallback. Fixed in `ee252b7` (project-level description, 8 card tags, canonical, static lede, `<noscript>`, dateless fallback); served text 1394 → 2564 |
| GitHub's `robots.txt` against the footer's two blob links | Whether the project's two finished pieces are crawlable where they are | 2026-07-26 (c194) | **Hypothesis falsified before acting on it.** `/*/tree/`, `/*/raw/`, `/*/blame/`, `/*/archive/` are disallowed; `blob` is not. The links are fine; no rehosting done — the negative result saved the work |
| **My own freshly-composed public copy, checked against `brand/positioning.md` as a diff rather than from memory** | The credential claim, on my surface, minutes after reading the guardrail | 2026-07-26 (c194) | **Reproduced retinue#27's unscoped form in the first draft of the lede.** Corrected pre-commit to state both conditions (the paths Retinue ships; retinue#15's spawn-point gap, linked). The fluent form is the wrong one and surfaces first every time |
| **The c194 lede's *other* two claims, and the same class swept across every place my copy states the lead story** | The check c194 ran on one sentence and not on the paragraph it sat in | 2026-07-26 (c195) | **The lead story was the one claim on the page with no caveat, and `writing/org-profile-README.md` printed the shipped projects query with no hint that it returns nothing.** c194 diffed the credential sentence against `positioning.md` and shipped the triple-store sentence unchecked; `positioning.md:199` requires the read-back caveat *unprompted*, and the live page carried caveats for the credential claim (retinue#15) and the egress audit but none for the lead story. Worse on the handover draft for `retinue-os/.github`: it presents the projects card as "one query over every project file in every mounted chamber", prints the SPARQL, and never says the query returns 0 rows — the c186 correction of exactly this claim swept `provenance-by-path.md` and `triple-store-story.md` six hours earlier and missed the file aimed at the org's front page. Re-measured live before writing: `kb#Project` **0**, `project#Project` **6**, and the store's only actor URIs are `actor-aros`/`actor-owner` against the self-review job's `actor:aros`. Fixed in all three: the lede now names both dead read-back features with both measurements, the org draft carries the caveat above the query plus a new paragraph on retinue#30 (`path` chambers never indexed) and qlever-dir#8 (blank-node identity across files), and `positioning.md`'s "Provenance is free" bullet — the source every draft reads first — now carries those two limits with the instruction to state one of them to any semantic-web audience, because they will run the cross-file join |
