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
| Repo → live site delivery path (Pages) | 2026-07-20 (c24) | **Working.** Three data files byte-identical to repo; newest build `c467c9f` = cycle 23's commit. Rule 4's chain ends at the served bytes, not at the commit — see below |
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
