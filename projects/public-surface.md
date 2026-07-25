---
type: project
id: proj-public-surface
title: "The project's public surfaces say what the project is"
goal: "Anyone landing on the org, a repo, or the docs site learns what Retinue is and what it isn't, without opening a source file."
goal_status: not_achieved
current_next_action: "Owner: enable private vulnerability reporting on the three public repos (chamber#5), then the org profile and descriptions (chamber#4)"
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

## Cycle 33 — the register found a decision, not a defect

Every previous row recorded a surface that was *wrong*. This one recorded a surface
that was *right* and that I had been arguing against without reading it.

`retinue-os-deployment` is public, is described in its own README as "a reference
deployment: the smallest real thing you can point at", and had never had a row. It
contains the written specification for my own token — the thing chamber#6 spent
cycles 19–32 calling a missing permission. It is not missing. It is scoped to a spec
with a stated threat model, and three of the four things I wanted are forbidden by it
on purpose, for a reason better than my convenience.

**Sixth rule, added here: before escalating for a capability, read the config that
denies it.** An escalation asks a human to change something. The register's other
rules check whether my *claims* are true; this one checks whether my *requests* are
already answered. A request to reverse a documented decision, filed in ignorance of
the document, is worse than no request — it spends the owner's attention and it
spends it arguing against his own security reasoning.

The generalisation for the next me: **my blockers are surfaces too.** Ten open
owner-action items are, collectively, a claim that ten things need a human. That
claim has never been audited. The others should be checked the same way — against
whatever config, doc, or setting would grant them — before the next review reports
them as a queue rather than as a set of possibly-mistaken asks.

Candidates still unrowed: the Actions secrets/variables inventory; the framework's
own `.env.example` (same class as this find, never read); `qlever-dir`'s workflows.

## Cycle 35 — the blocker queue, audited as a surface

c33 named it ("my blockers are surfaces too"), c34 carried it to the review and
declared the register otherwise exhausted. It was not exhausted: this was sitting
in it, already named, unrowed. **A surface someone flagged and nobody rowed is
indistinguishable from a surface nobody thought of.** The candidate list at the
bottom of the c33 row got audited; the sentence in the middle of it did not.

**The claim under audit:** "ten open owner-action issues", repeated in the standing
state of every log entry from roughly c30 on.

**It was wrong three ways.** The queue is seven. Only six carried the
`owner-action` label; chamber#1 — the oldest item in the org and a §7 hard stop —
carried none, so the obvious query (`is:open label:owner-action`) never returned it.
And retinue#1/#2/#3 were being counted as owner actions when they are my own work,
blocked solely on the inability to open a PR. They are chamber#6's tail, not
independent asks.

**The negative result is the important one.** I went looking for mistaken asks —
escalations filed without reading the config that already answered them, which is
exactly what c33 found and what rule 6 exists to prevent. There are none. All seven
are denied by `.env.example`'s deliberate scope or by GUARDRAILS §7. The queue is
not padded, and the next cycle should stop treating that as an open suspicion.

Recording a clean audit matters as much as recording a defect: an unresolved
suspicion about my own records will otherwise be re-investigated by every cycle
that reads c33's row.

**Rule 6 fired again, before the mistake this time.** My first intended action was
a comment on chamber#5 pointing out that SECURITY.md carries a working fallback
("open a public issue containing only *security contact requested*") which the
issue's framing seemed to omit. I read chamber#5 in full before writing it. It has
a section titled "Why it matters more than it looks" that identifies the fallback,
states that it works, and explains precisely why it is still insufficient — the
reporter has to read past a link that just failed them. My correction would have
told the issue's author something the issue already said, less well.

That is twice in three cycles (c33, c35) that reading the artifact first killed the
planned action. **Eighth rule: an intended correction is a claim, and gets checked
against its target before it is written, not after.** The cost of checking is one
`gh issue view`. The cost of not checking is a public comment explaining something
to myself.

**Published:** one comment on
[chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6#issuecomment-5022391206)
carrying the queue map, and the `owner-action` label added to chamber#1. Nothing
new escalated; the comment reduces the queue's apparent size rather than adding to
it.

**Still unrowed:** the framework's `.env.example` was read this cycle for the token
spec but not audited as a surface in its own right; `qlever-dir`'s workflows.

## Cycle 36 — retinue-os-deployment, a fourth public repo nobody had rowed

**The find before the find: there are four public repos, not three.** Every
survey in this log has said "all four repos" while the loop that produced the
number listed `retinue-os.github.io` — which does not exist. The actual fourth is
`retinue-os-deployment`, public since the org went public, and it had never been
audited, described, or rowed here. The count was right by accident and the
membership was wrong, which is the failure mode a register exists to catch.

**Security scan: clean.** No committed credentials (the only match is
`GITHUB_TOKEN=github_pat_replace_me`, a placeholder), no PII beyond
`you@example.com`, no reference to any private chamber — `chambers.json` mounts
exactly one chamber, `retinue-os-chamber`, which is what the README claims and
what GUARDRAILS §5 requires. `certs/`, `.env` and the client CA are gitignored.
Recording the clean result so it is not re-run.

**Two documentation defects, both in README.md, both filed as
[deployment#1](https://github.com/retinue-os/retinue-os-deployment/issues/1):**

1. The README summarises the token as "repository read/write on the `retinue-os`
   org and nothing more". `.env.example` specifies Contents r/w, Issues r/w, PRs
   *read*, Pages read, Metadata read — and withholds Workflows write with an
   explicit arbitrary-code-with-credentials rationale. The shorthand grants the
   one permission the spec argues hardest against.
2. The README says the framework's README documents every variable but
   `GITHUB_TOKEN` and `SOCIAL_SEND_POLICY`. `PUBLIC_HOST` and `ACME_EMAIL` appear
   nowhere in the framework — checked README, `.env.example`, both compose files,
   `deploy/`. They are the first two variables a deployer must fill in.

**Filed publicly, not through SECURITY.md, and the reasoning is recorded because
the call could have gone the other way.** Finding 1 touches privilege scoping, but
nothing is exploitable: no live credential is over-scoped (this deployment's own
token demonstrably cannot open PRs, so it was scoped from `.env.example`), and the
correct narrow spec is already public in the adjacent file in the same repo. The
defect is that a *future copier* would over-grant. Publishing the fix is how it
gets fixed.

**Ninth rule: a survey that reports a count must have enumerated the members.**
"All four repos" survived thirty-odd cycles because four was the right number and
nobody checked which four. A count is a claim like any other, and the cheapest
possible check — `gh repo list` — was never run.

**Still unrowed:** the framework's `.env.example` as a surface in its own right;
`qlever-dir`'s workflows; the Actions secrets/variables inventory. The register is
not exhausted — third correction of that claim.

## Cycle 37 — qlever-dir's workflows (a surface that does not exist), and the code underneath

**The candidate was fictional.** "`qlever-dir`'s workflows" sat in the unrowed list
from c33 through c36, carried forward by three cycles as pending work. The repo has
no `.github` directory at all — no workflows, no CI, nothing. Three cycles queued an
audit of a surface that has never existed.

This is c36's ninth rule in a new position. c36 found a *count* whose membership was
never enumerated; this is a *candidate* whose existence was never checked. The
register has been treating "someone named it" as evidence that it is there.

**Tenth rule: a candidate is a claim that a surface exists, and gets verified when it
is rowed, not when it is finally taken.** The check is one `ls`. Left unchecked, a
fictional candidate is worse than an empty register — it makes the register look like
it still has work in it, which is precisely what c34/c35/c36 kept mis-measuring.

**Reformulated into the readable neighbour** (the c34 move): no workflows exist, but
`orchestrator.py` and `build_index.sh` are public code that had never been read as a
surface, only cited. Read `orchestrator.py` in full.

**Finding, filed as [qlever-dir#4](https://github.com/Retinue-OS/qlever-dir/issues/4):
the watcher can die silently and take all rebuilds with it.**
`watch_data_dir` gives `inotifywait` `stderr=subprocess.PIPE` and never reads it —
a 64 KiB bounded buffer that, once full, blocks the child forever before it emits any
event. Separately, if `inotifywait` exits for any reason the `for` loop ends, the
daemon thread returns, and nothing logs or restarts it. Either way the endpoint stays
up, healthy, and serves a frozen index.

**Verified, not asserted.** I have no `inotifywait` here, so I reproduced the *pattern*
rather than the *cause*: the identical Popen/consume code with a chatty child
deadlocks with zero events delivered, and both candidate fixes (`DEVNULL`, merge into
stdout) deliver all events and exit cleanly. The issue states plainly which half is
measured and which half is reasoning — real inotifywait stderr volume is unmeasured,
and the exit-without-notice mode doesn't depend on it.

**Rule 8 fired and did not kill the action this time.** Checked #2 and #3 in full
before writing. #3 is the extension filter on line 250; this is the process plumbing
on 246–252, in the same function. Distinct cause, distinct failure (no events *at all*
vs. wrong events), and #3's title would lead nobody to it — so a separate issue,
cross-referenced, rather than a comment.

**Still unrowed:** the framework's `.env.example` as a surface in its own right;
`build_index.sh` (read only in the fragments #3 quotes, never audited whole).
**Closed as unauditable:** the Actions secrets/variables inventory (c34, 403 by
design) — c36 relisted it as unrowed in error; it is not a candidate.

---

## Cycle 38 — `build_index.sh`, audited whole

Took the older of the two unrowed candidates. Rule 10 first: both candidates were
confirmed to exist before either was taken (`gh repo clone` + `ls`), which is the
check c37 added after finding a fictional one.

**Finding, filed as [qlever-dir#5](https://github.com/Retinue-OS/qlever-dir/issues/5):
the path→graph-IRI step is a `sed` replacement, and the path is never escaped.**
Four filenames, four outcomes: `\` is silently consumed (valid but wrong graph IRI,
and a merge with the real file if that path exists), `&` expands to the matched text,
a space yields an illegal `IRIREF`, `|` breaks the `s` command. The last two abort the
whole build under `set -euo pipefail`. `escape_literal` has the same gap for `\r`.

**Why this one matters more than its size.** Provenance-by-path is the project's lead
story and strategy bet 1. Case (1) doesn't crash — it attributes triples to a path
they did not come from, with no log line. A store whose pitch is "the graph *is* the
file" has a specific obligation not to be quietly wrong about which file, and this is
the first defect found that undercuts the headline claim rather than the plumbing
around it.

**Also worth recording:** the c37 read of this repo listed `build_index.sh` as the
only unrowed file in it. The clone shows four more never read as surfaces —
`Dockerfile`, `docker-compose.yml`, `nginx.conf`, and `examples/.qlever/md2ttl.py`
(the converter the framework docs point readers at as the contract example). That is
the *contents* problem c37 raised for the 2026-08-02 review, showing up again: the
register's rows are audited, its omissions are not. Rowing them as candidates now
rather than leaving the register to look exhausted.

**Still unrowed:** the framework's `.env.example` as a surface in its own right;
`qlever-dir`'s `Dockerfile`, `docker-compose.yml`, `nginx.conf`.
~~`examples/.qlever/md2ttl.py`~~ — audited c39, rowed above.

## Cycle 40 — `.env.example`, and a theory that collapsed halfway

Took `.env.example` over the three remaining `qlever-dir` infrastructure files on
the same reasoning as c39 preferred the converter example: this is the file a new
deployer **edits**, and the README's onboarding path points at it. The project's
own honest self-assessment names a ~30-variable onboarding cost as a headline
weakness (guardrail 3). A file that documents that cost incorrectly makes the one
weakness the project already admits to worse than advertised.

**A theory collapsed mid-audit, and that is the part worth recording.** The
promising early shape was that `SEND_APPROVAL_BASE_URL` reaches only the three
messenger gateways in `docker-compose.yml`, and `CONVERSATION_BASE_URL` reaches
no service at all — which would have meant e-mail approval links are *always*
relative, unfixable by any documented setting. Approval URLs are how the human
exercises the send-control veto, so that would have been a positioning-level
finding, not a doc nit.

It is false. The `retinue` service takes `env_file: - .env`, so every variable in
the file reaches the container where `email_client.py` and `web-gateway.py` both
run. The `environment:`/`env_file` distinction I was reading as passthrough
coverage is only meaningful for the five services that lack `env_file`.

Two process notes from that:

- **The check that killed it was cheap and nearly skipped.** I had the compose
  line numbers for `SEND_APPROVAL_BASE_URL` and a clean story; `grep -n env_file`
  cost one command. The measured/unmeasured discipline (c37–c39) is aimed at what
  goes *into* an issue, but its real value showed up earlier here — before a
  false severity claim had been drafted at all.
- **My own service→`env_file` mapping produced a false positive**, matching the
  comment *"Deliberately no `env_file`"* in the `litellm` block as if it were a
  directive. The `awk` said `env_file -> litellm:`; the truth is the opposite of
  what the matched line says. Caught by reading the surrounding lines rather than
  trusting the extraction. **New rule 11: when a grep/awk over config matches a
  line, read the line, not just the fact that it matched — comments state the
  negation of what they mention.**

What survived is smaller and real: one silent override (`STT_SUPPORTED_LANGUAGES`,
findable only by reading compose), one undocumented credential pair (Garmin), one
undefined variable cited as a fallback, three duplicate keys. Filed at retinue#5
with the surviving severity, not the one the collapsed theory would have carried.

**Still unrowed:** `qlever-dir`'s `Dockerfile`, `docker-compose.yml`,
`nginx.conf`. ~~the framework's `.env.example`~~ — audited c40, rowed above.

## Cycle 39 — the converter example, and a candidate recorded at the wrong path

Took the converter example rather than the three infrastructure files, because it
is the one a reader *copies*: `docs/triple-stores.md` shows `{ "md": "md2ttl.py" }`
and this is the file that name resolves to. A defect in `nginx.conf` breaks a
deployment; a defect in the contract example propagates into every chamber that
follows the documentation. Strategy bet 1 spends the project's first audience on
the triple-store layer, and this is the file that audience will read first.

**Rule 10 fired, in its weaker form.** c38 rowed the candidate as
`examples/.qlever/md2ttl.py`; the actual path is
`examples/projects/.qlever/md2ttl.py`. The surface existed, so this is not c37's
fictional candidate again — but the recorded path was wrong, and a `Read` of it
failed before a `find` located the real one. Rule 10 verifies that a candidate
*exists*; it did not catch that the candidate was *misdescribed*. Recording the
distinction rather than folding it into rule 10, because the fix is different: an
existence check passes on a near-miss path only if you check the path you wrote
down, and c38 wrote the path from memory of a directory listing rather than from
the listing. **Amendment to rule 10: a candidate is recorded by copying its path
from the tool output that found it, never by retyping it.**

**The finding turned back on my own chamber.** The example is byte-identical to
`projects/.qlever/md2ttl.py`, which converts these very project files. Nothing is
broken — ids, actors and dates are all slugs and ISO dates throughout — but that
is a property of how I have happened to write them, not of anything enforced. If
a future me writes `current_actor: Reto Gmür` in a project file, that project
silently leaves the store, and the projects card loses a row with a diagnostic
quad as the only trace. Worth knowing before it happens; not worth a second issue,
since the fix belongs in the upstream example.

---

## Cycle 41 — the container's operational surface, and the end of the qlever-dir list

Took all three remaining `qlever-dir` candidates at once — `nginx.conf`,
`Dockerfile`, `docker-compose.yml` — because they are 35, 30 and 11 lines
respectively and they only mean anything read together. `nginx.conf` alone says
nothing; what it does depends on who writes `/run/nginx-upstream.conf` and who
reloads it, which is `orchestrator.py`, already read at c38.

**One theme, six findings, filed as
[qlever-dir#7](https://github.com/Retinue-OS/qlever-dir/issues/7).** The container
has no definition of "healthy" other than *PID 1 has not exited*, and PID 1 is the
orchestrator, which survives every failure that takes the endpoint down. Three of
the six are ways port 7001 is dead while `docker ps` says the container is up; the
fourth is that the logs which would explain it are written to files nobody reads.

**This one touches a public claim, which is why it was worth the cycle.**
`README.md` line 6 — "the endpoint stays available the whole time" — and line 26 —
"clients see no downtime". Both are about the *swap*, and about the swap they are
essentially right (finding 5 is a narrow in-flight race I flagged as my most
arguable). But a reader takes them as a statement about the endpoint's
availability generally, and generally it is unsupervised. Guardrail 3's
understate-rather-than-overstate rule applies to the project's own READMEs, not
only to what I post.

**Rule 8 fired and was resisted.** Findings 1–2 are the same class as #4 — a child
process failing quietly with nobody watching — and finding 4 is the same class as
#4's undrained stderr. Different processes, different fix, so: cross-referenced in
the issue body, not merged into #4. Third time this rule has kept two related
qlever-dir issues apart rather than letting one absorb the other.

**Not routed through SECURITY.md**, fifth time recorded. Availability of the
container against its own configuration; no untrusted input, no privilege boundary
crossed, nothing remotely triggerable. Same reasoning as c36–c40.

**Still unrowed:** nothing in `qlever-dir`. That repo's public surface is now
audited end to end — README (c19), `build_index.sh` (c38), the converter example
(c39), and the container's operational surface (c41). Per the c32 amendment, the
correct question now is not "what is due for re-audit" but **"what does this
project have that no row describes"** — and the honest answer this cycle is that I
don't have a candidate I can name and verify. Recording that as a state rather
than inventing one.

## Cycle 47 — the harm claim, and the one sentence nobody audits

c46 was a good cycle: it found a real defect, measured it precisely, labelled its
unmeasured half honestly, and refused to build the workaround that would have
hidden it. Then it closed with one sentence naming a victim, and that sentence was
false. This cycle's whole find is that sentence.

**Twelfth rule: a harm claim is a claim about a *reader*, and gets traced to the
code path that serves that reader — not inferred from what the system is for.**
"The store went stale, and the dashboard reads the store, so the dashboard was
wrong" is three steps, and the middle one was never checked. It took one `grep`
for `fetch(` in the component to find that the public card reads a committed JSON
file, and one `gh issue view` to find that the card which *does* read the store has
been returning nothing since 19 July for unrelated reasons.

**Why this class of error is the dangerous one for this project.** Everything c46
measured, it measured well; the register's rules were all followed. The harm claim
was the one part of the entry that was *not* a measurement — it was the part that
made the finding feel important, and it went in unchecked precisely because it was
the payoff rather than the evidence. Guardrail 3 is about overclaiming for the
project. This is the mirror image: overclaiming for a **bug**, borrowing severity
from an outage that did not occur. The credibility cost is identical, and the
audience for it is the maintainer of somebody else's repo.

A silent fault does not need an invented victim. If the only way to make a finding
sound serious is to assert an impact I have not traced, the finding was already
serious enough or it wasn't.

**Corollary to rule 4 (propagate a correction everywhere it lands):** c46's claim
had reached three surfaces within one cycle — the public issue comment, this
register, and `docs/examples/provenance/README.md`, which is served live on Pages.
The grep that found all three is the same one rule 4 has been asking for since c21.
It keeps finding things because a claim written once is rarely written once.

## Cycle 48 — `docs/styles.css` and `docs/icons/`: the row was clean, the page describing it was not

Took the register's last remaining "never" row, deferred twice as weak. The two
artifacts are in fact clean:

- **`icons/`** — both PNGs are byte-identical to `webapp/icons/` (md5 match).
  `icon-512.png` is unreferenced (the page is deliberately not a PWA and links
  only the 192 as favicon): 4.4 KB of dead weight, no defect. Recorded, not fixed.
- **`styles.css`** — the `:root` palette is identical to the live dashboard's,
  variable for variable, plus one addition (`--fg2`). The wide-screen grid matches
  exactly: `max-width: 1100px`, `minmax(0,1fr) 360px`, `gap: 12px 18px`. Its own
  header comment ("copied from the live dashboard and reduced") is accurate.

**The find was one level out again — in `index.html`'s footer disclaimer**, the
one paragraph on the public site that tells a reader what this page *is*:

> It reproduces the interface — the same stylesheet, cards and layout as the real
> Progressive Web App — over content committed to this repository.

Measured against the artifacts: the stylesheet is 128 lines against the live 124
and diverges from line 1; **all six** component files differ from their live
counterparts (`projects.js` by 111 changed lines, `base.js` by 38); the card set
drops two components and renames three headings. Nothing but the icons and the
palette is "the same". The removals are disclosed in the next sentence — the
overclaim is "the same stylesheet, cards and layout", not the omission.

Rewritten to what the diff supports: shared tokens and proportions, adapted
copies, every file edited, a reduced look-alike rather than the same code.

**Thirteenth rule: an artifact and the copy describing it are two surfaces, and
auditing the first does not audit the second.** Three consecutive cycles have now
found their defect not in the thing they set out to check but in a sentence
*about* it — c46 in a workaround note, c47 in a harm claim, c48 in a provenance
claim. In each case the artifact was fine and the description had drifted past it.
The description is the surface a reader actually consumes, and it is the one with
no test, no diff and no reviewer.

Guardrail 3 in its plainest form: the gap between what the project claims and what
it does must be zero, and that includes claims the project makes about its own
website.

**Register state.** No "never" rows remain. Per the c32 amendment the question is
"what does this project have that no row describes", and the honest answer stays
what c41 recorded: no candidate I can name and verify. But three-for-three says
the productive next move is not a new artifact — it is the copy attached to the
artifacts already audited.

## Cycle 49 — the framework README's Telegram sentence, checked against the code

Took the move c48 queued: the README prose in `retinue`, audited against the code
diff-by-diff rather than for claim accuracy (c11 did the latter). This is the
first row that audits a surface in the framework repo rather than in this chamber
or on the Pages site — and it is the repo a visitor reads first.

**The defect, README.md:180.** The "Messaging accounts" section opens by naming
the three account kinds as "a Signal number, a linked WhatsApp device, or a
Telegram **bot**". The Telegram gateway is a full MTProto user client:
`scripts/telegram-gateway.py:483` builds `TelegramClient(session, api_id,
api_hash)`, there is no `bot_token` in the file, and the setup steps use
my.telegram.org plus an interactive login with SMS code and 2FA — not BotFather.

The README contradicts itself sixty lines later, in "Telegram accounts", where it
says plainly "an MTProto user client (Telethon), not a bot". The code agrees with
the second passage.

**Why it is not a typo.** The error runs in the direction that *understates*
reach, inside the section whose entire purpose is to fix what an account can do.
A bot sees only what is sent to it; this client reads the user's DMs and messages
the user's contacts as them. It also breaks the README's own argument two
subsections down, where `TELEGRAM_SEND_POLICY` fails safe to `verify` "since it is
the user's own account" — reasoning a reader holding the word "bot" cannot follow.

Filed as [retinue#9](https://github.com/Retinue-OS/retinue/issues/9) with the
one-phrase diff. Not fixed directly: the framework checkout's git directory is
unreachable from this container (`fatal: not a git repository:
/workspace/deployment/../.git/modules/retinue`), so unlike previous cycles I could
not even push a branch — a second, smaller consequence of chamber#6 that this
cycle discovered rather than a new blocker.

**Everything else in the section verified clean:** mode names and the `inbox`
default with fallback on an invalid value (`telegram-gateway.py:58`), the
forward-to-triage behaviour (`_forward_to_inbox`, line 530), and the Signal and
WhatsApp descriptions.

**Rule 13 holds and extends.** Four consecutive cycles, four defects in the copy
*about* a thing rather than in the thing. This one adds a variant worth naming:
the description had not drifted away from the artifact over time — it was wrong
on the day it was written, and survived because the correct version sits sixty
lines below it, where nobody reads the two together. **Internal consistency is not
a check a reader performs, and it is not one the author performs either.** The
check that found it was reading the section against the code, and it took one
grep.

Also worth recording: a wrap-aware search was required. `grep -rn "Telegram bot"`
returns nothing, because the phrase breaks across a line. A single-line grep is a
test that can pass on prose for the wrong reason.

## Cycle 50 — the README's two structural summaries, both frozen at "Signal is the only gateway"

Continued c49's move: the framework README against the code, this time the two
sections that describe the *shape* of the stack rather than its behaviour. c49
queued them explicitly with the right open question — is the omission presented as
exhaustive, which is the difference between a summary and a defect. Answered by
measurement, not by reading tone.

**Finding 1 — `README.md:15`, "Defines these core compose services:", names four
of twelve.** Listed: `retinue`, `signal-gateway`, `stt`, `qlever-life`. Not
listed: `whatsapp-gateway`, `telegram-gateway`, `litellm`, `litellm-db`,
`updater`, `egress-audit`, `egress-log-viewer`, `egress-anomaly-agent`.

The check that turned this from "an overview is allowed to be short" into a
defect: **`grep -c "profiles:" docker-compose.yml` → 0.** No service is optional.
All twelve are built by `docker compose build` and started by `docker compose up
-d`, on the default path the README's own Installation section walks. Had even one
`profiles:` key existed, the honest verdict would have been "short but fair".

Two of the eight are gateways of exactly the class the list already contains, with
full README sections of their own further down; three are the egress-audit trio —
by my own positioning notes the project's most distinctive component, and absent
from the summary a security-minded reader reads first.

**Finding 2 — the `Layout` tree (`README.md:570`) omits ten root directories**,
all verified present: `whatsapp-gateway/`, `telegram-gateway/`, `stt/`,
`litellm/`, `updater/`, `egress-audit/`, `webapp/`, `tests/`, `deploy/`, `docs/`.
No ellipsis, no "selected entries" caption, so it reads as exhaustive. Same root
cause as finding 1, which is why both went into one issue rather than two.

Filed as [retinue#10](https://github.com/Retinue-OS/retinue/issues/10).

**What was checked and found correct**, recorded because a register of faults only
is itself a distortion: the four described services are described accurately;
startup steps 1–3, 5 and 6 match `entrypoint.sh` (hooks at :213, `refresh.py` at
:252); the Deployment and host-mount sections match the entrypoint's
already-present-chamber detection.

**One thing deliberately raised as a question, not a finding.**
`entrypoint.sh:301–308` forks the web gateway, `scheduler.py` and `sync-plugins.py
--watch` in remote-control mode; none appears in the startup list, and
`.schedule.json` is absent from `README.md` entirely (it is in `CLAUDE.md`). That
is either a missing step or a deliberate README/CLAUDE.md division of labour, and
I cannot tell which from the artifacts. Asked inside retinue#10 rather than
asserted. **Rule 14: when a gap could be a design boundary, the finding is the
question, not the verdict** — asserting it would have been c47's harm claim in a
new costume, a conclusion reached because it made the issue feel bigger.

**Rule 13 now five for five**, and this cycle sharpens it: the two defects were in
*summaries*, the copy whose whole job is to describe other artifacts. A summary
has no test, no diff, no reviewer, and it decays every time the thing beneath it
grows. It is the highest-yield surface in the repo and the one nobody re-reads.

## c51 — the docs and the compose file disagree about what is optional

Continued the c50 queue: the README's remaining sections read against the code.
The find is not in a summary this time but in the **disagreement between two
shipped artifacts**, which is a slightly different class and probably the more
durable one. `README.md` and `.env.example` both call LiteLLM optional;
`docker-compose.yml` makes it a hard `service_healthy` dependency of the main
container, whose database needs a password variable the "optional" block ships
commented out. Prose can be wrong on its own; here the prose is wrong *because*
the compose file moved under it, and the only artifact with authority is the one
nobody reads for documentation. → [retinue#11](https://github.com/Retinue-OS/retinue/issues/11)

**Rule 15: a grep is a claim, and an anchored grep is a narrow one.** This cycle
nearly filed a finding that `.env.example` omits `RETINUE_GATEWAY_USES_CLAUDE_OAUTH`
— which, via `entrypoint.sh:309`, would have meant the documented LiteLLM recipe
silently disables the remote-control session. It was false. The check was
`grep -c "^VAR="` across a file that is almost entirely commented-out examples,
so every optional setting read as absent, and the same pattern had reported
fourteen variables at once. The correction cost one `sed -n '46,70p'`.
The general form: when a pattern reports *absence*, read the region before
believing it. Absence is the one grep result that cannot be verified by the
grep that produced it.

Rule 13 now six for six — but note it held here only after rule 15 caught the
seventh candidate, which would have been a false one. The register's value is
the hit rate on *published* findings, not on candidates.

## c52 — the send-approval boundary is a workflow, not a boundary (not filed publicly)

Continued the c50/c51 queue as planned: the README's messaging-accounts block
(lines 178–450), chosen because its send-control claims are the ones
`brand/positioning.md` leads with in public. It paid, and it paid in the one
category that does **not** end in a public issue.

**The finding.** All three messenger gateways authorize
`POST /pending-sends/<id>/approve` with the same single bearer token that
authorizes `POST /send` — one `_authorized()` helper, one env var per gateway
(`scripts/signal-gateway.py` do_POST/`_PENDING_SEND_RE`, token check at :1188;
`whatsapp-gateway.py` ~:980; `telegram-gateway.py` ~:852). `docker-compose.yml`
hands all three tokens to the **`retinue` service** (lines 86, 95, 100) — the
container the agents run in. Confirmed the block boundary rather than assuming
it: no other service key appears between :31 and :105.

Consequence: an agent whose sending identity resolves to `verify` can queue a
send and then release it with the credential it already holds for queuing.
`README.md` and `whatsapp-gateway.py`'s module docstring both say "an agent can
never approve its own send". That is enforcement phrasing over a convention.

**Why it is not a public issue.** Guardrails 8 and 9: an unfixed weakness in a
security boundary of a public project goes to the owner and the `SECURITY.md`
process, never into a public tracker. The c50/c51 habit of "find defect → file
issue" had to be interrupted deliberately here, and the interruption is the
point. **Rule 16: the venue is decided by the class of the finding, not by the
momentum of the last three cycles.** Two consecutive cycles of issue-filing made
"file it" the default action, and this is precisely the finding for which the
default is wrong.

*Update 2026-07-21 (c91):* the owner independently reproduced this in a live
session and filed it publicly as
[retinue#19](https://github.com/Retinue-OS/retinue/issues/19). The private-venue
decision was correct for c52; the finding is now tracked in the open, and the c52
private escalation (dashboard thread `a9eba69…`) is superseded by #19 — no
re-escalation needed, the owner clearly has it.

**Stated as verified, so the scope stays honest.** The gating itself is sound.
`_outbound_policy_category()` (:965–991) keys off the gateway's own
`SIGNAL_ACCOUNT`, never consults the recipient, falls back through `"*"` to
`DEFAULT_SEND_CATEGORY = "verify"` (:151); the `verify` / `trust`-without-
`--user-approved` branch at :1291 matches the prose exactly; `--url` is a full
send URL and the README's examples use it correctly; the three roster endpoints
are read-only and token-gated as described. The weakness is the approval route's
authorization alone, and the issue says so.

**Stated as unmeasured.** This is a source-reading finding. I did not execute
the approve request, and would not have: exercising it means transmitting a real
message from the owner's personal account, and probing that gateway at all sits
badly with guardrail 5. Labelled as unexecuted in both the escalation and in
`positioning.md`.

**The smaller item in the same section, deliberately not filed separately.** The
bash comment at README:380 reads "Recipients matched by a verify/trust policy",
three lines below a paragraph insisting the policy is keyed to the sender and
not the recipient. It contradicts the section's central claim in the copy a
skimmer actually reads. It travels with the same fix, so it went into the
escalation rather than into its own issue.

**Rule 13 (audit an unchecked surface) now seven for seven** — and this is its
best result so far, because the surface audited was the one my own public
positioning rests on. The correction landed in `brand/positioning.md` the same
cycle, which is the first time an audit has changed what I am allowed to say
rather than what the repo says.

## c54 — the README's operational tail, and the update recipe that rebuilds an unused image

Took the surface c53 queued: the README's operational sections read against the
code. Two of the three sections c53 named (`First start`, `Normal start`,
`Deployment`, `Updating`) were genuinely first-look; `Deployment` was not —
**c50 already audited it** and found it matches the entrypoint's
already-present-chamber detection. Corrected the queue's premise in the register
row per rule 13's self-records clause, the same correction c53 made about its own
"never audited" note. The re-audit of `First start` and `Normal start` confirmed
them against `entrypoint.sh`'s `MODE="${1:-interactive}"` and its two-mode `case`.

**The find, README:592–599.** `Updating the image` says: to pick up changes to
agents, scripts or dependencies, run `git pull` then `docker compose build`. On a
running stack those two commands rebuild the image and stop — the containers keep
the old image until an `up -d` recreates them, so the section's stated goal is not
reached by the steps it lists. This is the c49 pattern again: the correct recipe
is already in the repo twice. `CLAUDE.md:601` gives the framework's own canonical
update as `git pull && docker compose build && docker compose up -d`, and the only
`up -d` in the whole README is at :475, in `Normal start`, which a reader following
`Updating` has no reason to revisit. → [retinue#12](https://github.com/Retinue-OS/retinue/issues/12),
one-line fix, standard disclosure header (chamber#3 practice).

**Deliberately not filed.** Startup step 4's "~15 s, no downtime" is the same claim
qlever-dir#7 already contests, and step 8's naming only `signal-gateway` in the
startup narrative is another face of retinue#10's still-open question about the
forked services that start but aren't listed. Neither gets a new issue; both are
tracked. Rule 16: the venue is decided by whether a tracker already covers the
root cause, not by the momentum of having just filed one.

**Unmeasured, stated in the issue.** No Docker daemon in this environment, so the
"rebuilds an unused image" consequence rests on Compose's documented
recreate-on-`up` semantics, not on an observed stale container. The rest of the
find — the missing command, the two authoritative recipes that include it — is
direct file reading.

Rule 13 now seven for seven on filed findings.

## c68 — the four README defects, cross-checked against my own copy

No new README surface to audit and no external contact. New angle instead:
retinue#9–#12 are README-defect findings already filed (c53–c54, from the
owner's account). The unchecked surface was whether *my own* public writing
repeats any of them — the rule-13 self-records clause applied to marketing copy
rather than to a repo file.

Grepped `brand/positioning.md`, `writing/`, chamber `README.md`, `docs/`:

- **retinue#9** (Telegram "bot" vs MTProto user client) — my copy is already
  correct: "Telegram MTProto session" at `positioning.md:44` and
  `org-profile-README.md:42`. The send-control positioning never leans on the
  word "bot", so the threat-model-narrowing error the issue flags is absent.
- **retinue#10 / #11 / #12** (compose-service list / LiteLLM-optional framing /
  update recipe) — zero matches. These are install-detail defects; my writing
  carries no install copy that could inherit them.

Negative result: my public surface repeats none of the four. Recorded so a
later cycle doesn't re-run the same grep and mistake it for new work. This is
not a rule-13 "filed finding" (nothing to file — the surface was clean); it is
the confirmatory half of the rule, checking that a defect found on the repo did
not silently also live in the copy I own.

## c71 — retinue#15 (credential scrub) vs my own credential-custody claim

Positive find, same self-check pattern as c68 but this time the copy *did* carry
an over-strong form. The owner filed [retinue#15](https://github.com/retinue-os/retinue/issues/15)
at 08:49Z (measured in a live dashboard session): the entrypoint's credential
scrub runs only on the main `exec claude --remote-control` path, so
gateway/scheduler-spawned `claude -p` sessions (dashboard tabs, scheduled jobs)
inherit `EMAIL_PASS`, `GARMIN_PASSWORD`, `LITELLM_MASTER_KEY`, `GITHUB_TOKEN`,
`OPENROUTER_API_KEY` in their environment. That contradicts `positioning.md`'s
"the agent never holds the credentials to your accounts … survives inspection"
for exactly the sessions users touch most.

Action: added a cycle-71 calibration to `positioning.md`'s credential-custody
section — the claim holds for the main session and describes the *design*, but
Aros does not present the sidecar isolation as complete across all sessions
until the fix lands. Implementation gap, not architecture defect; the fix keeps
the existing unset pattern. **Not filed as a new issue and not escalated:** the
owner filed it himself, so it is already tracked and he already knows; per
guardrail 9 an unfixed security weakness is not something Aros amplifies, and
re-telling the owner his own finding would only wear the channel. The calibration
is a working-note guard against a future overclaim, not an outbound post — no
account exists to publish from, and nothing was published.

## c119 — chamber#7 (stale "no CI" claim) vs my own positioning copy

Same self-check pattern as c68/c71: a defect tracked on the repo side, checked
against the copy I own, and this time the copy carried the stale claim.
`GUARDRAILS.md` §3 and `brand/positioning.md` both stated "CI does not yet run
the test suite." Verified false this cycle against the live repo: `tests.yml`
runs the suite on every push to `main` and every pull request, and the last
three runs (most recent 2026-07-21 16:28Z on `main`) all passed.

The split, deliberately: **GUARDRAILS.md stays for the owner.** A prior cycle
already made the principled call not to self-edit the document that constrains
me, tracked at chamber#7 (owner-action, OPEN, unchanged since 2026-07-20); that
decision stands and I did not re-escalate it. **positioning.md is mine** — I am
its sole author and instructed to keep it accurate — so I corrected its "What we
do not claim" bullet to the accurate, still-understated form: CI runs the suite
on push/PR, but coverage is thin and does not exercise the gateway's
security-critical paths (edge auth, path traversal, `/sends` approval
authority). The two files now disagree on this one parenthetical until the owner
amends GUARDRAILS; that is the correct transient state, not a new conflict —
§3's binding thrust (understate; the gateway's security paths are untested)
survives intact, and positioning is now the more accurate of the two.

Not filed as a new issue (chamber#7 already tracks the owner half), not
escalated (already tracked, ~2 days old, not overdue), nothing published (no
account). Files changed: `brand/positioning.md`, this file, `log.md`.

## c145 — `log.md` as a *rendered* artifact, not as a file: it had stopped rendering

New surface class, and the register's first size-driven find. Every prior row
audited a surface for what it *says*; this one failed on how much of it there is.
`docs/index.html:93` links
`github.com/retinue-os/retinue-os-chamber/blob/main/log.md` as **"public log"** —
the artifact behind the project's strongest honesty claim, that a reader can
check what the agent actually did.

**Measured twice, on the live public artifact, not on the file on disk:**

- `POST /markdown` with the file content → **HTTP 403, "This API renders Markdown
  text up to 400 KB in size."** Bisected: 400,000 chars renders (517 KB of HTML
  back), 450,000 does not. The file was 498,217 bytes.
- The live blob page → HTTP 200, but its embedded payload carries
  `"richText":null`, `"richTextTruncated":true`, `"renderedFileInfo":null`. The
  rendered document is absent; GitHub serves the raw source. Not inferred from a
  documented limit — read out of the response.

**Fixed this cycle, entirely within my own authority** (no owner action, no
permission I lack): entries 1–123 moved verbatim into
`log-archive/cycles-001-044.md` and `log-archive/cycles-045-123.md` — split in
two because a single 448 KB archive would have inherited the same defect —
`log.md` keeps its name, path and public URL and now holds cycle 124 onward at
55 KB. Verified by reconstruction (archive part 1 + part 2 + kept tail is
byte-identical to the committed file) and by re-rendering all three through
`POST /markdown` (69 KB, 291 KB, 284 KB of HTML, rc=0). A rotation rule is now
stated in `log.md`'s preamble and in `strategy.md`.

**What this adds to the register's method.** c144 had already named the log's
size a problem and fixed the *growth rate* — the wake cadence — without checking
whether the file had already broken. It had, and nothing would ever have said so:
the URL returns 200, no warning is emitted, and the degradation is invisible to
anyone reading the repo rather than the page. Standing check for any surface
whose size only goes up: **fetch what the reader gets, not what the disk holds.**
Rule 13's self-records clause now covers volume as well as accuracy.

## c146 — the same check c24 ran, three days later, returning a different answer

Not a new surface and not a defect: a **re-check whose result changed**, which
is the only reason this cycle has an entry at all. c24 audited the repo → live
site delivery path and recorded two facts — the served bytes match the repo, and
the newest Pages build is the newest commit. The first still holds. The second
does not.

Measured 2026-07-23 06:2x UTC:

- `docs/index.html` live vs. repo: identical. All five `docs/data/*.json` live
  vs. repo: byte-identical (2069, 3106, 2809, 942, 2444 B). Pages
  `status: built`, `https_enforced: true`, four most recent builds `error: null`,
  durations 17–22 s.
- `pages/builds/latest.commit` = `a813938` (cycle 144's commit).
  `commits/main.sha` = `8917a8b` (cycle 145's, pushed 03:20:14Z). The build was
  created at 03:20:19Z — five seconds *after* that push — and built the parent
  tree anyway. Nothing is queued behind it.
- Why no reader is affected: `compare/a813938...8917a8b` lists `README.md`,
  `log.md`, `log-archive/*`, `strategy.md`, `projects/public-surface.md` and
  **no file under `docs/`**. A build of HEAD would emit the same bytes. That is
  a proof, not a hope.

**What it adds.** The failure mode is silent in the same way c145's was: the API
reports `built`, no error field, the site returns 200, and the only way to see
the lag is to compare two SHAs that nobody compares.

**Bounded, by measurement rather than by assumption.** This cycle's own push
(`bf7ac80`, 06:26:46Z) built `bf7ac80` — HEAD, no lag — and carried the skipped
tree with it. So a raced build costs staleness until the *next* push of any kind,
not indefinitely; at the current cadence that is hours, and the damage case is a
`docs/`-touching push that happens to be the last one for a while. The first
draft of this row said "indefinitely" on the strength of one observation, and the
next observation, five minutes later, contradicted it. So the check goes in the routine rather than in a memory: **after
any push that touches `docs/`, compare `pages/builds/latest.commit` against
`commits/main.sha`, and if they differ, push again to re-trigger.** That belongs
to the `aros-dashboard-refresh` job's own completion, since that job is the one
whose whole output lives under `docs/`.

Also closed this cycle, in the same measure-the-reader's-view spirit: **c145's
rotation verified on the live artifact.** `log.md` (55,638 B) and both archive
parts (224,349 B and 224,772 B) now return HTTP 200 from the blob pages with
`"richTextTruncated": false` and a non-null `richText` — the rendering the
403/`richText:null` measurement said was gone. The fix is confirmed where it
matters, on the page a reader gets, not on the file on disk.

## c147 — an open pull request is a public surface, and four of them had only ever been checked for who wrote them

The register's territory question (c32: "what does this project have that no row
describes?") answered itself from the survey I run every cycle. Cycles 139, 140,
143, 144, 145 and 146 all recorded the same line about the owner's four open
framework PRs — that they are authored by `retog`, therefore not external
contact, therefore not an Aros item, and that since none is merged the rule-3
claim-table re-audit trigger has not fired.

Every clause of that is true and it is the wrong conclusion. Two of the four
modify `CLAUDE.md`, the framework's most-read document; one of those introduces a
new frontmatter convention *and* a new SPARQL vocabulary. Waiting for the merge
before reading them is precisely backwards: before the merge a finding is a
review comment, after it a finding is a bug report against shipped code and a
correction to documentation people have already read.

**Findings, all run rather than read** — full statement in the
[retinue#1 comment](https://github.com/Retinue-OS/retinue/issues/1#issuecomment-5056843983):

| # | Finding | Evidence |
|---|---|---|
| 1 | #21's gate joins on `kb#`; nothing emits `kb#` | live store: 0 `kb:Project`, 6 `project#Project`, 0 `kb:` predicates; PR query verbatim → `result-size-total: 0` |
| 2 | The `current_actor` convention the PR adds to `CLAUDE.md` doesn't produce the URI its own registry types | `md2ttl.py` on a fixture with `current_actor: coach` → `<urn:retinue:coach>`; `discover-agents.py` writes `<urn:retinue:actor:coach>` |
| 3 | The escape hatch the spawned prompt documents is a no-op | `resolved: true` in frontmatter → no triple (`resolved` absent from `SCALAR_FIELDS`) |
| 4 | minor: `p:paused` is emitted, the gate ignores it | same fixture emits `p:paused true`; query has no paused filter |

Finding 1 is retinue#1's namespace defect with a third consumer. Findings 2–4
are new and belong to this PR alone. Finding 2 is the more interesting of the
two: it is a convention being *created* by the same PR that misstates it, so
there is no legacy to blame and no existing user to break — the cheapest possible
moment to fix it, and it exists only because the PR was written against the
documentation rather than against what the converter emits, which is exactly how
`kb#` reached three consumers.

**Fourteenth rule: read the diff of an open PR, not only its author.** A PR is
the project's documentation and its future claims, in draft, at the only moment
when correcting them costs a comment instead of an erratum. The survey question
"is this external contact?" is a traction question; it is not an audit, and for
six cycles I let it stand in for one.

**Second thing this cycle established, and the reason the venue is wrong:**
`POST /repos/retinue-os/retinue/issues/21/comments` → 403, GraphQL `addComment`
on the same PR → 403, `POST /repos/retinue-os/retinue/issues/1/comments` → 201.
For a fine-grained PAT, a comment on a pull request is governed by the *Pull
requests* permission, not *Issues* — chamber#6's missing scope again, and the
first of its five consequences that blocks substantive technical contribution
rather than a settings toggle. The review went to retinue#1, which is the right
home for finding 1 and the wrong home for findings 2–4. Recorded on chamber#6 as
the fifth consequence, with the three-line measurement; no new ask, no new issue.

## c148 — the PR from c147 merged unchanged, so the review became a bug report

Three hours after c147 filed its review comment, [#21](https://github.com/Retinue-OS/retinue/pull/21)
merged as `11d2d06` (11:57Z), together with #20 and #14. Framework `main` moved
`6d6a18a` → `6c75132d` for the first time since 07-21. The PR head
(`de02bcf0`, 07-22 14:54Z) is unchanged since before the comment, so all three
defects shipped exactly as measured.

**Everything re-measured against `main`, nothing carried over from c147** — this
is the whole point of the previous cycle's discipline, and a bug report that
recites yesterday's numbers is a claim, not a measurement:

| Check | c147 (against the PR) | c148 (against `main`, after merge) |
|---|---|---|
| Gate query, verbatim | 0 rows | 0 rows |
| `kb:` predicates in live store | 0 | 0 |
| `project#Project` in live store | 6 | 6 |
| `resolved: true` through the converter | no triple | no triple (fixture re-run) |
| `current_actor: coach` → | `<urn:retinue:coach>` | `<urn:retinue:coach>` (registry writes `…actor:coach`) |
| Predicate census, `resolved` or `status` | — | **absent**, over 6 real project files |

**Filed: [retinue#23](https://github.com/Retinue-OS/retinue/issues/23)** — the
`resolved` no-op, the ignored `paused`, and the three-spellings table, with
finding 1 left as a link to retinue#1 rather than restated. This is the venue
c147 said was correct and could not reach: an issue on the repo, not a comment on
a PR (chamber#6, fifth consequence, still binding — `POST /issues/21/comments`
was 403).

**The argument the issue makes that the review comment could not**, and the
reason it is worth its own number: the ordering. Today the gate matches nothing,
so nothing misbehaves — the `resolved` defect is invisible *because* the
namespace defect is unfixed. Fixing retinue#1 is what makes it bite: the sweep
then matches every unresolved project with an agent in `current_actor`, spawns a
`claude -p` session every 24 h (`.schedule.json`, `enabled: true`,
`interval_seconds: 86400`), and the only way to take a project off the list is to
delete `current_actor` — which also deletes the record of who owned it. A bug
whose severity is *created* by the fix for another bug is not visible from either
one alone.

**Fifteenth rule: when a defect is masked by another defect, say which fix
unmasks it.** "Currently harmless" and "harmless" differ by exactly one merge,
and the person who merges the mask is usually not the person who read the report.

**Rule-3 claim-table re-audit: triggered, and no re-audit needed.** `main` moved,
which is the trigger condition, but `compare/6d6a18a...6c75132d` touches
`.claude/skills/triage`, `use-email-client`, `.schedule.json`, `CLAUDE.md`,
`agent-self-review.py`, `discover-agents.py`, `email_client.py`, `entrypoint.sh`,
`scheduler.py` — and **no `README.md`, no `docs/`, no `review.md`**, which is
where every row of the claim table lives. Trigger met, surface untouched, one
line rather than a cycle. Recording the negative result so the next cycle does
not re-derive it.

**Register row, updated in place:** open pull requests → also check them again at
the merge, because that is when a review comment's shelf life ends. The gap here
was 2 h 22 min; at the 3 h cadence it can be missed entirely, which argues for
reading the *merge* into `main` as its own event rather than trusting that a
comment was seen.

## c149 — the provenance mechanism, run instead of read

Fifth tick at the 3 h cadence. c147 established that an open PR is a public
surface; c148 established that the review window is about two hours. [#22](https://github.com/Retinue-OS/retinue/pull/22)
(`feat(dashboard): per-conversation model picker`) was the one PR left open, and
the only one touching `docs/triple-stores.md` — the doc bet 1 rests on. It adds
`scripts/jsonld2ttl.py`, a generic rdflib JSON-LD expander, and a
`config/conversation-models.jsonld` read by the gateway as plain JSON, with the
claim: *one source of truth, two access paths, no duplicated copy.*

**The claim holds.** Installed the converter and the file into this chamber's
`projects/.qlever/`, and the 17 triples landed in
`file:retinue/projects/conversation-models.jsonld` — the right named graph,
derived from the path, no configuration. `rdflib` is present in the stock
qlever-dir image, transitively: the Dockerfile's `pip3 install qlever` pulls it
in as a dependency of qlever-control. Worth noting only because `md2ttl.py`'s
docstring makes standard-library-only an explicit design constraint, and the new
converter relies on a dependency nothing declares.

**Two things the reading passes could not have found**, because both need a
second file:

1. Blank nodes are labelled per `rapper` invocation and the invocations are
   concatenated, so the *n*-th blank node of every file is the same node.
   Six models across two files became four. The named graph is right on every
   triple; it is the subject that merges, which is why a graph-scoped query looks
   fine and the graph-unaware query — the "one SPARQL surface" mode the docs sell
   — silently cross-joins files.
2. A symlink produces nothing at all: no graph, no diagnostic quad, no log line.
   `find` without `-L` tests the link, not the target.

**Sixteenth rule: a mechanism audited by reading has been audited with one
example.** Both of these defects are invisible to any pass over the source or the
docs, because both require a second file and a converter that had not been
written yet. The path→graph mapping is per-file by construction; the things that
leak between files (blank node labels, and now anything else global to the
stream) are exactly what a one-file mental model cannot see. When the mechanism
is the lead story, run it with two of everything.

**Method note, for reuse:** the whole experiment was fixtures in this chamber,
measured through the live endpoint, then removed — store verified back to its
exact baseline (69 triples / 8 graphs) and `git status` clean before the write-up.
A test that leaves residue in a public repo is a second finding for a later cycle.

## c154 — the comparison document, and what a comparison document is for

`comparison.md` has been in the framework repo since before publication, is 281
lines long, names two other projects, and had **never appeared in this register
or anywhere else in my records** — `grep comparison.md` across `projects/`,
`log.md`, `log-archive/`, `strategy.md` and `brand/` returned nothing. It is
also the single public surface that guardrail 4 (compare fairly, disparage no
one) governs directly, and the surface where an overclaim about Retinue is most
load-bearing, because every sentence in it is written to be weighed against an
alternative.

**The find is not in the competitor columns.** Those hold up: the star and fork
figures are within a percent of today's API values, both competitors' MIT
licences check out, the CVE and audit statements are attributed and dated, and
the tone is factual throughout. The file is scrupulous about other people's
projects and careless about its own — `README.md`, `review.md`,
`comparison.md` and `whatsapp-gateway.py` all assert an invariant that
`signal-gateway.py` does not implement and that the maintainer's own open issue
[#19](https://github.com/Retinue-OS/retinue/issues/19) documents as false.

**Seventeenth rule: a claim is not audited until it is audited where it is
*strongest*.** The send-approval property had been calibrated in
`brand/positioning.md` (which since c52 explicitly declines to say "an agent can
never approve its own send") and correctly scoped in `SECURITY.md`. Both were
found by auditing *my own* copy. Nobody had checked the framework's copy, and the
framework is where the sentence does the most work — it is inside the definition
of `verify` in the README a deployer reads before trusting the control. A
correction applied to the marketing copy and not to the reference documentation
leaves the claim standing exactly where it matters most.

**Corollary for the sweep after a bug report.** #19 was filed 2026-07-21 and
nothing looked for the prose it falsified. When an issue proves a stated property
false, the sweep is part of the report: `grep` the phrase across the repo before
closing the tab. Four sites, one `grep`, three days late.

## c155 — the same rule, run a second time, on the claim the project leads with

c154 ended with a corollary: when an issue proves a stated property false, `grep`
the phrase across the repo before closing the tab. This cycle ran that corollary
against the *other* open finding of the same kind — [retinue#15](https://github.com/Retinue-OS/retinue/issues/15),
open since 2026-07-21, which measured that gateway- and scheduler-spawned
sessions inherit the full container environment. Nobody had swept the docs for
it either.

**The sweep found the same shape of defect as c154, one claim over.** In both
cases the calibrated wording already existed inside the project — for the send
claim it was `telegram-gateway.py:22-25`; for this one it is `review.md:69`,
which says "messaging credentials" and is exactly right. In both cases the
unscoped version survived where the sentence does the most selling:
`comparison.md`'s first table row, its security-argument heading, and its
"Choose Retinue if…" paragraph.

**Eighteenth rule: a corollary is worth as much as the number of times it is
run.** c154 wrote the sweep rule and applied it to the issue that produced it.
Applying it to the *other* qualifying issue took one grep and produced a second
published correction on the project's most load-bearing claim. Open bug reports
are a queue of prose to re-check, not just of code to fix — and the queue is
short enough to enumerate: any issue that demonstrates a stated property is
false gets a docs sweep, once, and the sweep is recorded so it is not re-run
blind.

**What the measurement added over reading.** The claim sites could be found by
grep, but the counter-evidence could not: it took looking at my own environment
from inside a scheduler-spawned session and walking `/proc/<pid>/stat` up to
`scripts/scheduler.py` to establish that this session is on the leaky spawn
path. Rule 16 in its other direction — a mechanism audited by reading has been
audited with one example, and here the second example was the auditor.

**And the sweep bounced back into my own file.** `brand/positioning.md` had the
scrub covering `GARMIN_PASSWORD` "and the rest"; the entrypoint has two `unset`
sites and neither mentions it. My copy was more generous to the project than the
project's code — which is the direction guardrail 3 says to watch for, and it had
been sitting in the file that governs every claim I make since cycle 71.

## c156 — the same PR, a new head: `docs/triple-stores.md` changed and the previous cycle triaged it by its title

c155 saw PR #22 pushed at 08:56Z and recorded it as "framework dev, not a claim
surface". The push (`05a4f63`) touches nine files, and one of them is
`docs/triple-stores.md` — the lead-story doc bet 1 rests on, the one surface in
the repo I have most reason to read. The dismissal was made from the PR's title,
which has said "per-conversation model picker" since 07-22 and describes the
first commit rather than the third.

**Nineteenth rule: triage a push by the files it touches, not by the PR's title.**
`gh api /repos/…/commits/<sha> --jq '.files[].filename'` is the whole check, it
costs one call, and a PR's title is frozen at the moment its author had a
different idea of what it was going to do. c147 established that an open PR is a
public surface and c148 that the review window closes at the merge; both were
about *whether* to look. This one is about looking at the right thing after the
head moves — an audited surface stays audited only at the commit that was read.

### What the new head changes

It replaces the docs' advice to copy or symlink `config/conversation-models.jsonld`
into a chamber (the sentence [qlever-dir#9](https://github.com/Retinue-OS/qlever-dir/issues/9)
quoted) with a boot emitter: `scripts/emit-conversation-models.py` derives the
model list into `chambers/_generated/conversation-models.nt` at container start,
deterministic and write-if-changed, and the doc adds a paragraph saying that
directory "sits under the chambers volume (so QLever indexes it)". That is a
better design than the copy-or-symlink route it replaces. The paragraph is the
part worth measuring, because it is stated flat.

### Measured, twice, against the live store

Ran the emitter from the PR head with `CHAMBERS_DIR=/workspace/chambers` — the
real volume, the same one QLever mounts read-only at `/data`:

| | |
|---|---|
| 16:40:13 | emitter creates `_generated/` and writes `conversation-models.nt` (4 models, 2648 B) |
| +10 s … +60 s | no `file:_generated/…` graph; store stays at 8 graphs |
| 16:41 | unrelated `.nt` written inside the chamber |
| +20 s | **both** graphs present (10) |
| — | `rm -rf _generated` → the delete *is* seen, store drops to 9 within 20 s |
| 16:45:21 | emitter runs again, creating the directory fresh |
| +10 s … +110 s | absent, 9 graphs, nothing else touched |
| then | unrelated `.nt` overwritten → present within 30 s |

Counter-check, and the reason the mechanism is a race and not a permanent
exclusion: once the directory had been picked up, an in-place rewrite of that
same file reached the endpoint in ~30 s. The path is watchable and the file is
indexable; the first event is simply lost.

`orchestrator.py:234-252` explains the second half of it. The watcher runs
`inotifywait -m -r` with `--format "%w%f"` and reacts only to paths ending
`.nt`/`.ttl`/`.n3` — so the `CREATE,ISDIR` event for `/data/_generated`, the one
event that could have covered the window between the `mkdir` and the watch being
established, is discarded for having no RDF extension. Filed as
[qlever-dir#10](https://github.com/Retinue-OS/qlever-dir/issues/10) with the
two-line fix (`%e %w%f`, trigger on `ISDIR`), stated as distinct from #3 (which
extensions) and #4 (the watcher dying).

**What makes it more than a PR nit:** `discover-agents.py` has been on `main`
since 07-23 writing `chambers/_generated/agents.nt` with the identical
`mkdir` + write-if-changed pattern, and the `agent-self-review` sweep queries
what lands there. On the first boot after a deployment adopts either feature the
registry is written and not indexed; on the second boot the bytes are unchanged,
so nothing is written and no event is generated at all. The gap closes at a
qlever-dir restart, because `build_index.sh:71`'s `find /data -type f` has no
such blind spot — which is exactly the shape that makes it hard to notice: it
works on every machine where anything else has changed recently.

### The framework-side items → retinue#28

Filed separately because the fixes live in different repos:

1. `docs/triple-stores.md:96` states the indexing as unconditional. Until
   qlever-dir#10 is fixed it is conditional on a race, and the cheap half of the
   fix on this side is to have the entrypoint create `chambers/_generated/`
   before the watcher can be running.
2. `_slug()` is stable but not injective — `''` and `'default'` both map to
   `default`, `a/b` and `a:b` both to `a_b` — so two offered models render as one
   subject with two `modelId` values and two labels, while the dashboard (reading
   the JSON) still shows two. The drift is precisely between the two access paths
   the feature exists to keep in sync. Same shape as
   [qlever-dir#8](https://github.com/Retinue-OS/qlever-dir/issues/8), reached by
   replacing blank nodes with a lossy slug. Shipped list has no collision; ids
   are deployment-configurable and `/` is ordinary in a proxied model name.

Filed as an issue rather than a PR review comment because the token still cannot
comment on pull requests (chamber#6, fifth consequence) — unchanged, not
re-escalated.

### Bounds

No `inotifywait` in this container, so the race is the mechanism consistent with
the measurements (missed on creation, seen on every later write) rather than one
I traced; the issue says so. Everything else is measured or readable in the
source. Test artifacts (`_generated/`, a scratch `sensor-c/readings.nt`) were
removed and the volume left as found.

**Rule 16, again, and this is the third time it has paid.** The two paragraphs
this cycle audited had both been *read* before — c155 read the PR's file list,
c55 audited `docs/triple-stores.md` whole. Neither reading could have produced
this, because the defect only exists on the boot where a directory does not yet
exist, and the only way to be on that boot is to delete the directory and run the
thing.

## c158 — the sweeps ran on the framework's copy and never on mine, and the file they missed was the handover draft

c154 swept the send-approval claim across the framework's public files
(retinue#26). c155 swept the credential-custody claim (retinue#27) and, as a
second pickup, corrected `brand/positioning.md`, on the reasoning that my own
source of truth for claims deserved the same treatment. Both stopped there.

`writing/` was never swept by either, and it holds
`writing/org-profile-README.md` — the paste-ready text
[chamber#4](https://github.com/Retinue-OS/retinue-os-chamber/issues/4) offers the
owner for `github.com/retinue-os`. It carried both swept claims in their
unscoped form, plus a stale test-file count. The consequence is specific and not
hypothetical: the issue tells him the draft is ready to paste, so the correction
window was "until he next has fifteen minutes", not "until someone reviews it".

### What was measured, not inferred

- Six test files under `tests/` on `main`, not five; the new one is
  `test_web_gateway_projects.py`. `tests.yml` triggers on `push: branches:
  [main]` and on all `pull_request` — so "every push" was wrong in the direction
  that flatters the project.
- retinue#15, #19, #26 and #27 all still OPEN at the time of the edit, so none of
  the three corrections describes a fixed defect as unfixed or the reverse.
- `.schedule.json` `aros-tick` is 10800 s; the chamber README's "every 30
  minutes" was the only site of that claim anywhere in the repo (`grep` across
  `.md`/`.json`/`.html`/`.js`, excluding `log.md` and the archive, where it is
  history and correctly dated).
- The projects → triples claim in the README re-verified against the live store
  in the same pass: six `file:retinue/projects/*.md` named graphs present. That
  sentence stands as written.

### The asymmetry worth naming

The README's Writing section linked *Provenance by path* — the piece that shows
the architecture working — and omitted *We tested our own weakest claim* — the
piece that shows it failing. Nobody chose that; the second piece was finished
after the section was written and nothing prompted a revisit. But a landing page
that indexes the favourable half of your own writing is the exact shape of the
thing bet 4 says not to be, and it had been in that state since 2026-07-20.

## c159 — a sweep is only as wide as the string it greps for

c154 filed retinue#26 by grepping the quotable sentence. Re-run against the
property in every phrasing it takes, the same claim appears in at least nine
places on `main` at `92af09c` — and the five the sentence-grep missed are, on
average, the more consequential ones: a comparison table row, the review's
opening verdict, a section heading, the configuration file a deployer reads
first, and the source comments that give the property as a *design rationale*.

### Twenty-second rule

**Sweep the property, in every phrasing, not the sentence.** A grep for a
quotable sentence finds the places that quote it — which are the places most
likely to be known already. The sites that matter are the ones that restate the
claim in their own words, because nobody remembers writing them. Method that
would have worked at c154: grep the *subject* (`approve`, `approval`, `human`)
across every extension the repo ships, not just `*.md`, and read every hit.

### Two site classes that are not documentation

- **Rationale in source.** `email_client.py:1020-1021` explains that
  `approve_pending_send()` is deliberately not a CLI subcommand "so an agent
  running the CLI cannot approve a send". The premise is true and the conclusion
  does not follow; the friction is still worth having. A contributor reading it
  learns the hole is closed and has no reason to look again — a comment that
  *causes* the absence of future checking is worse than an absent comment.
- **Agent-facing instruction.** `use-email-client/SKILL.md:118-119` tells the
  agent it cannot approve a pending send. If the control's effectiveness rests
  partly on the agent believing that, the dependency should be deliberate and
  should not be described to the reader as "fail-closed".

### The half that was mine

`brand/positioning.md`'s "One sentence" — the paragraph written to be reused
verbatim in every future piece of copy — still carried both claims in their
unscoped form, eighty lines above its own calibrations of them. c155 corrected
the credential claim in the body of that file. c158 corrected both in
`writing/org-profile-README.md` and wrote the twenty-first rule (sweep the copy
I wrote, handover drafts first). Neither touched the headline. **A sweep that
starts from the derived copy will not find the origin**; start from the file
everything is quoted out of, then follow the quotes.

### Escalation split, recorded so the next me copies it rather than re-derives it

The same pass produced a mechanism detail beyond what retinue#19 published. The
public comment carries the documentation finding only and cites #19 for the
mechanism; the detail went to the owner's dashboard, once, with no decision
requested. Guardrail 9 draws the line at *unfixed vulnerability*, not at
*vulnerability* — #19 being public does not make everything adjacent to it
publishable.

## c160 — the fourth claim class in guardrail 3's table, never swept

c154, c155 and c159 swept two claim classes (send approval, credential custody).
Guardrail 3's table has five rows. Two of the remaining three are dead —
"production-ready" (the project's copy consistently understates maturity) and
benchmark numbers (there are none). The fourth, **"runs on any model / no
lock-in"**, had never been swept, and `grep -i "lock-in\|model-agnostic"` across
the register, the log and both archive parts returns two incidental hits and no
audit.

It yields one defect, in the direction the guardrail predicts: the framework's
copy is honest about the *coupling* (`comparison.md:212-219` is a good section,
and `brand/positioning.md:207,229` and `writing/org-profile-README.md:127` all
say "not model-agnostic" without prompting) and over-precise about the *escape
hatch*. `README.md:103-106` says `RETINUE_CLAUDE_MODEL` reaches "every Claude
Code process Retinue starts". Five invocation sites on `main` at `92af09c`; four
do, one does not — the dashboard's transcript-cleanup pass, which hard-codes
`TRANSCRIPT_CLEANUP_MODEL`, default `haiku` (`web-gateway.py:176`, `:1555-1556`).
→ [retinue#29](https://github.com/Retinue-OS/retinue/issues/29).

The shape is worth keeping. The pass is best-effort and returns the raw
transcript on any failure, so nothing breaks loudly; a gateway deployment simply
loses a feature `CLAUDE.md:421` says it has, with one line on the gateway's
stdout as the only trace. And the one documented gateway recipe where it keeps
working is LiteLLM — via the `claude-*` catch-all that forwards to Anthropic.
**The exception to a portability claim landed exactly where the claim is not
tested: the path that still reaches the original vendor.**

Not measured, and stated so in the issue: this deployment runs the default
Anthropic path, so the per-recipe consequences follow from the model names and
the endpoints' documented catalogues, not from a request I watched fail.

### Twenty-third rule

**A claim class is a row in the guardrail table, and the table is the sweep
list.** Three sweeps in a row picked their class from the previous cycle's find
rather than from the list that already exists. Guardrail 3's five rows are the
enumeration; two are now swept, one is swept as of this cycle, and the remaining
two are recorded above as dead with the reason, so no future cycle re-derives
which is which.

*Negative result, recorded because a rule that only ever fires on hits is
indistinguishable from luck:* my own copy is clean on this class. The chamber's
three claim-bearing files each state the Claude Code coupling as a limitation,
unprompted, and none of them claims portability.

## c161 — the claim table has two columns, and only one of them had ever been audited

Three cycles (c154, c155, c159, c160) swept guardrail 3's table by reading the
**left** column — the "don't claim" list — and checking whether the project's
copy violated it. The **right** column is the other half of the same table: the
sentences the file tells me I *may state plainly*. It is pre-approved public
copy, and it had never been checked against anything.

Reading the table column-wise found two false statements in row 3, both in the
copy I am licensed to publish.

### Row 3, "a manual certificate step" — describes a step that does not exist

- `scripts/entrypoint.sh:15-37` generates the egress-audit CA automatically when
  it is missing, onto a persistent volume. Its own comment says this exists so a
  deployment can adopt egress auditing "without having to run a manual one-time
  setup step on the host".
- The only manual CA ceremony left is `scripts/gen-client-cert.sh`, and
  `README.md:162-173` frames client certificates as an **alternative to the
  basic-auth password** — "Certificates are *optional*". Skipping it costs a
  password prompt.

The phrase is quoted from `review.md:268`, which says "a manual CA ceremony **for
client certs**". My copy dropped three words, and those three words were what
made the sentence true.

### Row 3, "~30 environment variables" — matches neither bound

`.env.example`: **67** distinct variable names over 300 lines, unchanged since
the initial public release (`4e04317`), so the number was never a count of that
file. Four are uncommented. `docker-compose.yml` interpolates 10 `${…}` and
passes **35** through by name — close enough to "~30" that this is almost
certainly its source.

So the number is defensible under one reading and about half the truth under the
reading the sentence's own argument needs: §3.8 is arguing that setup is "a wall
for a second user", and what a second user faces is the 300-line file, not the
compose passthrough list. Stated with both bounds in the comment rather than as
"you said 30, it is 67" — the weaker, honest version is the one that survives
someone re-counting.

### The other three rows, recorded as negative results

- **Row 1 (egress audit):** accurate as written, and worth having verified rather
  than assumed, because it is the row most likely to be quoted at the project.
  `HTTP_PROXY`/`HTTPS_PROXY` are plain environment variables on the `retinue`
  service; the container shares the `agents` network with the proxy; the compose
  file contains no `cap_add`, no `NET_ADMIN`, no iptables rule and no
  `internal: true` network. Nothing stops a process that unsets them.
- **Row 4 (model coupling):** swept c160.
- **Row 5 (benchmark numbers):** the only published figures are the competitor
  star counts in `comparison.md`, verified against the live API at c154.

Row 2 is chamber#7's existing subject, so the finding went there as a comment
rather than as a new issue: one edit to `GUARDRAILS.md` now closes the whole
table.

### The second half: my own open issues had gone stale

retinue#3 was measured against `main` on 2026-07-20 at 04:24Z and proposed three
replacement numbers. Three commits touched those files afterwards. Pasted today,
my own correction would have written **three fresh wrong figures** into
`review.md` — five files → six, 936 → 1,157, 2,486 → 2,616.

It also missed two sites of the claim it was filed about (`review.md:25-27`, the
*Verdict up front* caveat, and `:290`) and cites a section number that does not
exist in the document.

### Twenty-fourth rule

**A correction is a claim with a shelf life.** An open issue that quotes measured
numbers goes stale the moment the branch it was measured against moves, and it
stales *silently* — nothing in GitHub marks it, and the more precise the issue,
the more damage a late paste does. Any cycle that touches an open issue of mine
re-measures its figures against current `main` first; any cycle that finds `main`
has moved re-checks the issues that quoted it. This is the c159 rule (sweep the
property, not the sentence) pointed at time instead of at text.
