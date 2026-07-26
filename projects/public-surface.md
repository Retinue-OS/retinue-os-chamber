---
type: project
id: proj-public-surface
title: "The project's public surfaces say what the project is"
goal: "Anyone landing on the org, a repo, or the docs site learns what Retinue is and what it isn't, without opening a source file."
goal_status: not_achieved
current_next_action: "Owner: enable private vulnerability reporting on the three public repos (chamber#5), then the org profile and descriptions (chamber#4). Aros, c188: took the last of c177's never-named front-end files — the three page shells beyond the root, the manifest, and the app-launcher/markdown/project-page components — plus .dockerignore, leaving scripts/ingest-sensors.py as the only never-named framework file. One small finding, held in drafts under the c184 rate limit: the PWA manifest's only user-visible string is German, the single exception to CLAUDE.md's own language convention in the whole front end. The cycle's real work was a defect I talked myself out of filing — I had most of a case that the dashboard is not installable behind basic auth, and the half I had from memory (browsers omit credentials on a same-origin manifest fetch) is contradicted by WHATWG HTML §2.5.5, which puts a missing crossorigin attribute in the No CORS state with credentials mode 'same-origin'. New rule: a claim about someone else's implementation needs the implementation, not a recollection. Negative results kept: the project page's frontmatter parser matches the chamber's md2ttl converter field for field, so page and store read the same file the same way; and no Dockerfile copies the build context, so the missing .env line in .dockerignore costs nothing. Aros, c187: audited the dashboard as a rendered page rather than as its two source files, and found it contradicting itself — the footer has linked the triple-store walkthrough since c184 while two cards, generated two hours earlier, said it was unlinked. Both halves mine. Corrected the two fields in place with their own timestamps and deliberately did not bump the snapshot's generated keys, since that would present four-hour-old counts as fresh. New rule: the unit of audit is the rendered page — edit the shell, re-read the cards; edit a card, re-read the shell. Aros, c186: re-ran the two pieces c184 had just made publicly linked, on the principle that linking a piece republishes it. The egress piece holds; the provenance walkthrough's headline output had been stale since 1 h 42 m after it was committed and stayed so for six days — six rows printed, eight returned live — and the two extra rows are the piece's own thesis, so the correction became the argument. Upstream of that: brand/positioning.md, the file every public-facing draft must read first, carried the projects-card claim retinue#1 denies; three files had copied it, all fixed. Two rules added: a piece is republished on the day it becomes reachable, and fix a false claim at its source file rather than at the instance. Earlier, c184: the register turned inward for the first time and the front door was the worst surface in it — this chamber's README carried a wake interval 13 h stale and asserted the projects-card payoff that retinue#1 says returns zero rows (re-measured live: 0 against 6). Both fixed in place, plus the two finished pieces linked from the static dashboard, which had linked neither. New rule: audit inward before outward — the surfaces I own outright are the ones a stranger meets first and the only ones I can fix the same hour"
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

---

## Cycle 162 (2026-07-25) — the two example chambers, and what `path` does to them

`examples/chambers/` had never been audited: zero mentions in this register, in
`log.md`, or in either archive part. It is a small surface — two chambers, six
files — and it is the framework's only *runnable* answer to "what is a chamber",
plus the default `docker compose up` when a deployment supplies no `chambers.json`.

### The finding

Everything the two examples demonstrate about **agents** is accurate: both plugin
manifests are well-formed, both subagents carry frontmatter and declare
`tools: Read, Glob, Grep`, both `.schedule.json` jobs ship `"enabled": false`
exactly as the README promises, and the autodetect path in
`scripts/entrypoint.sh:116-137` does read name and description from `plugin.json`
and fall back to the directory name, as documented.

What is not accurate is the **data** half, and it is not the examples' fault — it
is the `path` mount they demonstrate. `entrypoint.sh:78` symlinks
`/workspace/chambers/<name>` to `/workspace/<path>`. The symlink is in the shared
volume; the target is not. `qlever-life` mounts that volume and nothing else, so
the chamber is a dangling link in the container that indexes it.

### The measurement, because reading is not measuring

Two chambers, created in the same second, one `.nt` file and one triple each:

| Chamber | Mount | T+40 s | T+85 s | T+125 s |
|---|---|---|---|---|
| `aros-dir-probe` | real directory | present | present | present |
| `aros-symlink-probe` | symlink out of the volume | absent | absent | absent |

The T+85 s column matters: an unrelated `.nt` file was written into a directory
that existed at container start, which forces a full rescan. Its graph appeared;
the symlinked chamber's did not. Without that step the result would have been
confounded with qlever-dir#10 (the new-directory race). Everything was removed
afterwards and the store verified back at its 8-graph baseline.

An incidental observation, recorded and not filed: the real directory *was* picked
up within 40 s despite being created after start, which qlever-dir#10 describes as
failing. The difference is probably that the directory and its file were created
within the same second, so inotify's `create` on the directory and the
`close_write` on the file were both delivered. #10's reproduction (an emitter
creating `_generated/` and writing into it) is the slower case. Worth a line on
#10 the next time that issue is touched, not a new issue.

### Why this is worth an issue rather than a shrug

The failure mode is silent and one-sided. A `path`-mounted chamber's plugin
installs, its subagent runs, its scheduled jobs fire, its git hooks are
installed — and its triples are absent, with no error in any log. The orientation
query in `docs/triple-stores.md` keeps returning rows from other chambers, so
nothing looks broken. And four public surfaces state the opposite in the
strongest available words: "all chambers equally", "**every** RDF file",
"**all** mounted chambers", "every chamber is indexed equally".

This is the lead-story claim (bet 1) in its weakest spot: not the mechanism, which
works, but the boundary of what the mechanism covers.

### Twenty-fifth rule

**Audit the surfaces a newcomer reaches by following instructions, not only the
ones a maintainer edits.** Every previously audited surface here is something the
project *says*. `examples/chambers/` is something the project *hands you to run*,
and it had gone 25 wake-ups unexamined because nothing about it emits a signal —
it is not in the README's table of contents, nobody had ever booted it in this
deployment, and its own failure produces no error. The register's second column
now carries it.

## Cycle 163 (2026-07-25) — the register audited everything the project says, and never what I produce

Every row above asks the same question of a different surface: *is this accurate?*
Twenty-six of them found a defect and most of those became an issue. Nothing in
162 cycles asked the other question about the thing I produce most of: **is it
being used?**

### Measured 11:34–11:40 UTC, all four public repos

| | |
|---|---|
| Open issues | 37 (`retinue` 21, `qlever-dir` 9, chamber 6, deployment 1) |
| Ever closed | **0** |
| Authored by anyone but me | 0 |
| Comments by anyone but me | 2 — chamber#1 (07-19) and retinue#13 (07-21) |
| Commits on framework `main` since 07-19 | 18, none referencing any of the 37 |
| Filing rate / drain rate | ~5.6 per day / 0 per day |

### What this is not

It is seven days, including a weekend, and the maintainer engaged with the
tracker twice inside it. Rule 5 applies without amendment: a high-frequency
observer reading a low-frequency actor perceives neglect where there is none. No
issue here is overdue, nothing was re-escalated, and no owner hand-off was made.
The trajectory is the point, not the current reading — 5.6/day with no drain
reaches ~85 issues by the 2026-08-02 review, and that is worth a rule before it
arrives rather than an apology after.

### What it is

`strategy.md` has said for ~20 cycles that "corrections accepted into the repos"
reads zero *because* the token cannot open pull requests. That is an unsupported
attribution and a flattering one. A pull request would have landed in the same
unreviewed queue as the 37 issues; nothing measured says format is the
constraint. The simpler explanation was available the whole time and I never
tested for it. **I have been counting *filed* as *corrected*** — the exact error
guardrail 3 exists to prevent, pointed at my own reporting instead of at the
project's copy.

### Twenty-sixth rule

**Audit your own output the way its reader receives it, not the way you produced
it.** Every issue in the backlog was individually correct, measured, sourced and
disclosed. Received together, they are an undifferentiated wall that a solo
maintainer has to sort before he can act, and one more of them is not obviously
help. Accuracy per item and usefulness in aggregate are different properties, and
this register had only ever measured the first.

### Twenty-seventh rule (rule 7, turned inward)

**When a permission is blocked, probe the verbs next to it before describing the
boundary.** chamber#6 says the token "can read metadata and file issues", which
is accurate — and 162 cycles read it as *only* file issues. Probed this cycle:
`POST /issues/{n}/labels` and `PATCH /issues/{n}` both return 200, while
`createPullRequest`, `PATCH /repos/…` and `PUT …/topics` stay 403. A triage
capability sat unused beside a loudly-tracked blocker for the entire life of the
project. Rule 7 was written at c34 about somebody else's surface; it had never
been run against my own credentials.

### What was done with it

All 37 open issues labeled: `retinue` 9 `bug`, 12 `documentation`, 4
`enhancement`, 1 `owner-action`; `qlever-dir` 8 `bug`, 1 `enhancement`;
`retinue-os-deployment` 1 `documentation`; the chamber's 6 already carried
`owner-action`. Nothing was closed, reworded or reprioritised — labels only, all
derivable from the issue's own title and body, and every one reversible. The
queue now filters to nine real defects in the framework rather than twenty-one
undifferentiated items.

## Cycle 164 — a snippet is a surface, and mine was wrong until tested

Not an audit cycle. The pickup was inbound: the maintainer commented on
[qlever-dir#8](https://github.com/Retinue-OS/qlever-dir/issues/8) at 2026-07-25
14:37Z preferring a generic skolemize function over the per-file blank-node
prefix the issue proposes. Recorded here because writing the answer produced a
register-shaped finding.

Issue #8 closed with an offer: *"Happy to write the exact `sed`/`awk` if that
helps."* Taking the offer up, I built a fixture first — subject-position blank
node, object-position, both in one triple, and literals whose text contains
`_:genidN` in plain, embedded, typed and language-tagged form. The pattern I
would have written from reading alone,

    sed -e "s|^_:|_:${P}|" -e "s| _:\([^ ]*\) \.$| _:${P}\1 .|"

corrupts **three of the four literal shapes**: `[^ ]*` swallows the closing quote
along with `^^<xsd:string>` or `@en`, so the rewrite lands inside literal text.
Restricting the label to legal blank-node characters
(`[A-Za-z0-9_][A-Za-z0-9_.-]*`) fixes it, because an object-position blank node
is always the final term of the line. Ordering is load-bearing too: the object
rewrite anchors on ` .` at end of line, so it must run before the substitution
that appends the graph term.

Posted the corrected version with an explicit statement of what was **not**
tested — real `rapper` output, since this chamber has no `rapper` — rather than
letting "tested" stand unqualified.

### Twenty-eighth rule

**A snippet offered in an answer is a claim under guardrail 3. Run it before
posting, and state what you could not run.** Prose about a defect gets measured
here as a matter of course; a patch or one-liner offered alongside it had no such
habit, and it is the part the reader will paste. This one would have handed the
maintainer a rewrite that silently corrupts literal text — inside an issue whose
entire subject is silent data corruption.

### Register addition

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| Code offered inside my own issues and comments (`sed`/`awk`/SPARQL snippets) | The part of a filed issue a reader executes rather than reads | 2026-07-25 (c164) | First one ever executed before posting; the naive form was wrong. Every earlier snippet in the backlog is **unverified in this sense** — SPARQL in issue bodies was run against a live store, but shell fixes were not. Check on next contact with each. |

## 2026-07-25 (cycle 165) — the first issue ever closed, and my own snippet checked one cycle late

Not an audit cycle either. Two events six minutes before the wake-up set the work.

**qlever-dir#9 closed.** Filed 2026-07-23 15:53Z, merged 2026-07-25 15:14Z via
PR#11 (+58/-5 in `build_index.sh`, opened and merged by the maintainer). 47 h 21 m
filed→fixed, and the first issue closed in the org's history. Verified rather than
assumed: the scan is now `find -P … -xtype f`, and a second pass
(`-type l -not -xtype f`) emits a `urn:qlever-dir:parsingError` quad for symlinks
whose target is missing or is not a regular file. Tested both predicates against a
fixture — symlink→file, symlink→symlink→file, symlink→directory, broken symlink, a
symlinked *directory* sitting in the scan path, plus the `.git`/`.qlever`
exclusions. Indexed set and diagnostic set partition correctly, nothing is visited
twice, and the symlinked directory is not walked. The register can record this fix
as real, not as closed.

**retinue#22 merged with retinue#28 unaddressed.** Both items of #28 are now on
`main` (`26297a2`, 15:12Z) rather than on a branch; re-checked against the merged
blobs, not the PR head, and neither `docs/triple-stores.md:96` nor `_slug()`
changed in the merge.

**The finding is in my own issue body, and rule 28 caught it one cycle late.**
retinue#28 offered `urllib.parse.quote(model_id, safe="")` as an injective
drop-in for `_slug`. `quote` *is* injective; the drop-in is not, because it lands
after `base = model_id or "default"`, so it removes the `/` vs `:` collision and
leaves `''` vs `'default'` exactly where it was. Run against the merged file over
seven ids including `_default`:

    shipped _slug              collisions: {'default': ['', 'default'],
                                            'anthropic_claude-opus-4': [...]}
    quote() + `or "default"`   collisions: {'default': ['', 'default']}
    quote(), fallback dropped  collisions: none

Commented on #28 with the merge status and the correction, stating that the fix
was tested against the merged file and **not** end-to-end in a running deployment.

Rule 28 was written at c164 about shell one-liners. This is the same defect one
line up the stack — a *named library call* offered as a fix, which reads as safer
than a `sed` and is not, because correctness depended on the surrounding two lines
rather than on the call. The rule needs no amendment; what it needed was applying
to the backlog it was written about. Register row below updated accordingly.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| Code offered inside my own issues and comments | The part of a filed issue a reader executes rather than reads | 2026-07-25 (c165) | Second one executed; wrong again, and this time it was a one-word library call, not a shell pattern. The unverified backlog from c164 stands. **Check the call site, not just the call.** |
| Merged PRs that close or touch an issue I filed | Whether a close is a fix | 2026-07-25 (c165) | New row. qlever-dir#9 verified against a fixture and holds. Nothing else in the org has ever been closed, so this row has one datum. |

## 2026-07-25 (cycle 166) — a dropped qualifier, twice from the same document

Two surfaces, both never checked before, both cheap. One is a negative result and
one is a false claim of mine.

### The machine-authored merge (negative result)

`copilot-swe-agent[bot]` resolved a merge conflict in `scripts/entrypoint.sh` at
15:08Z on the maintainer's request and it reached `main` at 15:12Z. That file
holds the only two credential-scrub sites in the project, and every calibration
in `positioning.md`'s lead claim cites them by line. Diffed old `main` against
new: exactly the branch's 11 lines, both emitter blocks present, scrub and `exec`
byte-identical and in order. The bot's own description of what it did is accurate.

Recorded anyway, because the class is new: **code written by an automated agent is
now arriving in this project's public repos**, and no register row had ever asked
who authored a change. The check is cheap (one diff) and only worth running when
the touched file carries a claim. This one did.

### The claim I got wrong

`brand/positioning.md` told me, and would have told any post composed from it,
that the test suite "does not exercise the gateway's security-critical paths (edge
auth, path traversal, the `/sends` approval authority)". Path traversal is
exercised in four of seven test files, and was in all of them before I wrote the
sentence. It was never overtaken by events; it was wrong on the day.

The mechanism matters more than the error. `review.md` recommendation #3 says
"path-traversal tests **for static and attachment serving**" — true and narrow. My
copy kept the noun and dropped the scope, which converts it into a false broad
claim. That is exactly what cycle 162 found five cycles ago: `review.md:268` says
"a manual CA ceremony **for client certs**" and my copy said "a manual certificate
step". Same source document, same direction, same two-word omission.

### Twenty-ninth rule

**A compressed quote is a new claim and must be measured, not trusted.** When copy
paraphrases a source document, either keep the source's qualifiers verbatim or
verify the shortened form independently. A summary that drops a scope word is not
a shorter claim, it is a different and usually false one — and it survives review
because it reads as a citation of something already checked.

The corollary that produced this cycle's better sentence: measuring instead of
quoting usually finds something sharper than the quote. "No test constructs a
request handler, so endpoint authorization is untested by construction" is both
true and more useful than the list of untested paths it replaces, and it took one
grep.

### Register update

Two rows added above (the machine-authored merge; the suite as reach rather than
size). The second retires a claim rather than filing an issue — the false copy was
mine, and `review.md` and retinue#3 are both already correct on the point.

## 2026-07-25 (cycle 167) — my own stale wording, adopted into the normative file

At 16:33–16:34Z the owner pushed `claude/aros-issues-triage-goei5k` to this
chamber's repo: two commits, no PR yet, resolving [chamber#7](https://github.com/retinue-os/retinue-os-chamber/issues/7)
(`GUARDRAILS.md` §3 row 2) and partially [chamber#5](https://github.com/retinue-os/retinue-os-chamber/issues/5)
(a `SECURITY.md` for this repo). The survey caught it two minutes later because
`gh api /orgs/retinue-os/events` reports `CreateEvent`s, and a branch is the
earliest visible form of a change.

### The finding

The row he committed uses **the replacement text I proposed in chamber#7 on
2026-07-25 (c161), verbatim** — including "the web gateway is a large single file
whose security-critical paths are untested". Cycle 166, thirty minutes before that
commit, established that this sentence is false and corrected it in
`brand/positioning.md`. I corrected my copy and never looked at the copy I had
handed him, which had been sitting in an open issue being actionable the whole
time.

Measured against `main` at `26297a2` before commenting: path traversal and the
SPARQL-injection guard *are* exercised (`test_web_gateway_projects.py:67-72`,
`:74-76`, `:78-80`, plus `../../etc/passwd` as a pending-send id in the three
policy tests). The accurate statement is the c166 one — no test constructs
`Handler` (`web-gateway.py:1940`), whose methods `_handle_internal_email`
(`:2126-2133`) and `_agent_conversation_payload` (`:2461-2472`) read
`self.headers`, so endpoint authorization is untested **by construction**. The CI
half of his row is right; the only nit is that `on.push` is `branches: [main]`,
so "every push" is broader than the trigger.

### Thirtieth rule

**Correcting a claim in my own files does not reach the copies of it I have
handed other people.** A proposed wording in an open issue is a live artifact:
somebody may paste it into a normative file months later, and they will not know I
retracted it elsewhere. When a claim is corrected, grep my own open issue bodies
and comments for the sentence, and mark every instance at the source.

Ran it this cycle across all four repos (2,539 lines of issue bodies and
comments). One live instance: **retinue#3, item 2 of the suggested edit list**,
proposing exactly this wording for `review.md` §1.2. Struck it in the issue body
with a dated "superseded — do not apply as written" note and the correct
replacement; struck item 3 the same way, since c166 had recommended deleting the
counts in a comment and the body still said "refresh them". Both marked, not
silently rewritten: the original text stays visible.

### A capability probe, and a negative result

Register rule 7 says to audit the part of a closed surface that is open. Two:

- `gh api /repos/<owner>/<repo>/private-vulnerability-reporting` returns
  `{"enabled": false}` **without admin scope** — so chamber#5's premise is now
  verifiable in one command by anyone, and the owner can confirm the fix the same
  way after flipping it. All four public repos read `false` today.
- The new `SECURITY.md` ends by routing framework reports to the `retinue` repo
  "following the same process there". Checked: `retinue/SECURITY.md` does carry
  the same disabled-fallback pattern ("open a public issue containing only the
  words *security contact requested*"), so the pointer is not a dead end. Nothing
  to file.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| Wordings I proposed in open issues | Text a human may paste into a normative or public file at any later date | 2026-07-25 (c167) | New row, and the first check found one already committed to a branch. Rule 30: grep open issues whenever a claim is corrected. |
| Branches pushed but not yet PR'd in org repos | Changes in flight, visible only via `CreateEvent`/`/branches` | 2026-07-25 (c167) | New row. `gh pr list` shows nothing until a PR exists; the branch had been live for two minutes. Worth checking whenever a survey sees a `CreateEvent`. |
| Private vulnerability reporting status | Whether `SECURITY.md`'s primary channel actually exists | 2026-07-25 (c167) | Disabled on all four public repos, now checkable without admin scope. Tracked at chamber#5; not re-escalated. |

## 2026-07-25 (cycle 168) — the dashboard was a day old and wrong about the largest thing that has happened

The register's one wall-clock-decaying surface, checked on the schedule c157 set
and found stale in the way that matters: not drifting numbers, but a sentence
that had become false. `briefing.json` said "no closed issues anywhere". The
first issue ever closed in this organization was merged at 15:14Z, two hours and
six minutes before this cycle started.

Measurement, 2026-07-25 17:15–17:25 UTC, all live via `gh`:

| | c157 (07-24 17:20Z) | c168 (07-25 17:25Z) |
|---|---|---|
| Open issues | 35 | **36** (retinue 21, qlever-dir 8, chamber 6, deployment 1) |
| Closed issues | 0 | **1** (qlever-dir#9, 47 h 21 min filed→merged) |
| Open PRs | 1 | **0** (retinue#22, qlever-dir#11 both merged 15:12–15:14Z) |
| Stars / forks / watchers | 0 / 0 / 0 | unchanged |
| Issue comments, all from the owner's account | 16 | **27** |
| Org events by anyone but him | 5 of 273 | **7 of the 300 most recent** (5 Copilot, 1 Actions, 1 removed spam account) |
| PVR enabled | false ×4 | false ×4 |
| Framework `main` | `92af09c` | `26297a2` |

Outside GitHub could not be re-checked this cycle — web search is not available
to this session — so the mention check is the GitHub-wide one: three issues in
Warhammer wargaming repositories, where a retinue is a unit. False positives, as
before.

**The one judgement in an otherwise mechanical regeneration.** `todo.json`'s top
item had been the agent GitHub account and its token, ranked there partly on the
argument that the missing pull-request scope is what stops corrections being
accepted into the repos. c163 found that attribution unsupported and c165 watched
an issue get filed, fixed and merged without the scope. So the card now leads with
chamber#1 — oldest item, phase exit, and it crosses one week tonight — and says on
the card why it moved. Re-ranking a standing queue is not re-escalation: nothing
was pushed, nothing was repeated, and the six owner-action issues are untouched.

**What the freshness rule should say after today.** c157 wrote rule 20 (a
freshness surface needs a next-decay date, not just a regeneration date) and set
no interval. The interval is now measurable: this surface survived two days when
the org was quiet and went wrong in one when it was not. While there is human
activity in the org, the dashboard is a daily check.

## 2026-07-25 (cycle 169) — regenerating a surface eleven minutes old, and finding three wrong numbers in it

c168 pushed the dashboard at 17:21Z. This cycle regenerated it again at 17:32Z on
a dispatched task, which should have been a no-op and was not. The point is
method, not diligence: **c168 wrote its copy from a live measurement and this
cycle re-ran the measurement instead of re-reading the copy**, which is register
rule 2 (reading a surface is not auditing it) applied to my own eleven-minute-old
output. Three defects, all of the same class — a count compressed from its source
into a claim about something narrower:

| Stated | Measured 17:24–17:32Z | Why it was wrong |
|---|---|---|
| qlever-dir labels: 8 bug, 1 enhancement | **7 bug, 1 enhancement** | The 8 counted `#9`, closed at 15:14Z that afternoon. The sum also exceeded the 8 open issues on the same card. |
| "All 27 issue comments … from the owner's account" | **25 on issues**, all his; 2 on PR retinue#22, one of them **Copilot's** | `/issues/comments` returns pull-request conversation comments too. The card's own qualifier ("issue comments") was the thing that made it false. |
| Standing measure: **filed 37**, accepted 1 | **filed 36**, accepted 1 | 37 is every issue in the org. `qlever-dir#2` was filed 2026-07-08, ten days before this chamber existed. Corrected in `strategy.md` under "What I measure" and at "The drain rate is not zero". |

A fourth, smaller: c168 stamped every document `generated: 17:30:00Z` and pushed
at **17:21Z** — a timestamp nine minutes in the future on a page whose whole
argument is that its numbers are traceable. Fixed here (`17:32Z`, pushed after
17:32Z) and written onto the `proj-dashboard-truth` card as a rule.

**Two facts added rather than corrected.** `proj-github-org`'s `expected_by` is
today and arrives unmet on every criterion, which c168's agenda did not carry —
now a dated milestone, unmoved. And a GitHub-wide repository search for "retinue
agent" returns exactly one repo: `Disaster-Terminator/Retinue` (★3, created
2026-05-03), an unrelated tool for running Claude Code and OpenCode as Codex
subagents. Recorded as what a stranger searching the name finds. Nothing follows
from it, nothing was filed, and it is not escalated: a name shared with another
public project is a trademark-shaped question, and those are the owner's (§7).

**The one-week check, run because it was asked for and answered by measurement.**
Nothing on the owner's desk has been waiting a full week. Ages at 17:32Z:
chamber#1 6 d 19 h (one week at **22:17:48Z tonight**, the first item ever to
cross it), chamber#3 5 d 15 h, chamber#4 5 d 14 h, chamber#5 5 d 14 h, chamber#6
5 d 13 h, chamber#7 5 d 13 h, retinue#4 5 d 6 h, and the private privacy decision
5 d 19 h (unread since 2026-07-19 21:33Z). The briefing says exactly that — that
nothing is overdue yet, with every age listed — rather than borrowing the framing
of the question.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `docs/data/*.json` (this dashboard) | The one surface a stranger reaching the org actually reads | 2026-07-25 (c169) | Re-measured 11 minutes after its own regeneration; three counts wrong, all compressions of a wider source into a narrower claim. Daily while there is human activity in the org — and re-measured, never re-read. |
| Generated timestamps on static data | Whether a freshness surface's own stamp is true | 2026-07-25 (c169) | c168's stamp was 9 minutes ahead of its push. New rule: stamp with a time that has already passed at commit. |
| GitHub-wide name search | What a stranger searching "retinue" finds before finding us | 2026-07-25 (c169) | New row. One unrelated repo of the same name, ★3. No action; naming is owner territory. |

## 2026-07-25 (cycle 170) — the shipped persona files, and a name that is not the project's to publish

Audited surface: `agents/academic.md`, `agents/publisher.md`, `agents/secretary.md`
on `retinue-os/retinue` `main` at `26297a2`. Chosen by the register rule — a
"never" row, and this one had no row at all: zero mentions of any of the three
files in this register, in `log.md`, or in either archive part, across 169 cycles.
`CLAUDE.md:44` and `:47` send a reader to `agents/secretary.md` twice, so the gap
is not that the files are obscure. It is that every previous audit chased *claims*,
and these files make almost none — they are instructions, and instructions were
never on the list of things that could be wrong in public.

### The finding, stated as far as it may be stated here

`agents/secretary.md`'s **"Recipient-specific guidelines"** section publishes a
real third party's surname alongside their preferred channel, tone and language.
Public since `4e04317` (*Initial public release*), 2026-07-18.

The name, the heading and the line number are deliberately absent from this file,
from `log.md` and from the draft. This chamber repo is public; guardrail 5 forbids
naming a third party who has not consented, and there is no version of "recording
the finding accurately" that requires me to republish the thing I am reporting.
The precise pointer, the proposed edit and the exposure bounds went to the owner
in a dashboard thread, which is the venue for an unfixed exposure — rule 16, the
venue is decided by the class of the finding.

**What made it an escalation rather than a register row.** One stale line is a
defect. The same file's closing section instructs the agent to record a **new
`####` heading whenever the user gives style feedback about a specific person** —
so the public path is the *designated* store for other people's communication
data, and it grows on its own the next time the Secretary is corrected. A defect
that repairs itself into existence needs the owner today, not at the review.

### The structural half, which is publicly filable and is not filed yet

`CLAUDE.md` states that chambers are deployment content, not part of the
framework. All three persona files are deployment content that shipped inside the
framework: `academic.md:7` hard-codes `chambers/health/research/inbox/` and :12-14
assume the health chamber's Medic; `publisher.md:8-14` is a translation manifest
naming one deployment's health documents by path and :25 names a treatment
protocol; `secretary.md` carries the profile above and the instruction to add
more.

The framework gets this exactly right one directory over — `chambers.example.json`
ships examples a deployment bind-mounts over, `.env.example` documents settings
without carrying values. The persona layer has no example/instance split at all.
Proposed shape (in the draft): ship `agents/*.md` generic, move recipient
profiles, translation manifests and chamber paths into a chamber file the persona
reads at composition time, and repoint the "add a new profile" instruction there.

Not filed, on purpose. The issue would be a public arrow at the line the owner has
not yet removed, and it is a *design* issue whose urgency is entirely borrowed
from the content one. It goes in once the content is out, and the escalation says
so explicitly rather than leaving him to guess whether I am sitting on something.

### Negative result, recorded because it bounds the finding

Swept `retinue-os/retinue` and `retinue-os/retinue-os-deployment` for e-mail
addresses, phone numbers and personal names. Everything else is placeholders —
`a@b.ch`, `Jane Doe`, `John Roe`, `Max Müller`, `+1555…` test numbers, the
README's `+15557654321`. `alerts@account.garmin.com` is a vendor sender address in
`garmin_mfa.py`, not personal. The deployment repo is clean. One real name, one
file, and the whole framework history is a single squashed commit — so this is one
file's habit, not a pattern of leakage.

Exposure stated rather than dramatised: seven days public, 0 stars, 0 forks, 0
watchers — and the repos are demonstrably on scrapers' lists (c154) and public
repos are code-search indexed, so a star count is not a readership measurement.

### Thirty-first rule

**Instructions are a public surface, and they can be wrong in a way claims cannot:
by containing data rather than by asserting something false.** Every audit for 169
cycles asked "is this sentence true?" — a test that a recipient style profile
passes trivially, because it asserts nothing. The question that finds this class
is **"whose is this, and did they agree to it being here?"** Run it against every
shipped file that a persona, skill or agent definition is allowed to *append* to;
an append instruction pointed at a public path is a leak with a schedule.

Immediately in scope for the next pass, and unaudited on this test: `.claude/skills/`
(four skills), `.claude/agents/archivist.md` (audited c56 for ontology accuracy,
never for content ownership), and my own `drafts/` and `writing/` — I append to
those every cycle, and this chamber is public.

### Bounds

Read, not executed: this is a content audit of three Markdown files fetched from
`main` via the API, plus two `grep` sweeps of full clones. Nothing was written to
the framework repo, no issue was filed, no name was recorded anywhere public. I
did not attempt the fix: `agents/*.md` is Tier 3 (PR required), this deployment's
token cannot open pull requests (chamber#6), and the two decisions that matter —
history rewrite versus plain deletion, and whether the person should be told — are
guardrail 7's, not mine.

## 2026-07-25 (cycle 171) — the next two files on c170's own list, and a skill that reassures the agent with the wrong file

Audited surfaces: `.claude/skills/messaging-contact-lookup`, `spawn-session`,
`triage`, `use-email-client` (four `SKILL.md`, 675 lines) and
`.claude/agents/archivist.md`, on `retinue-os/retinue` `main` at `26297a2`.
Chosen because c170 named exactly these as next in scope on the ownership test,
and a queue that is written down and then not followed is worse than no queue.

### The ownership test, run first, and it comes back clean

Rule 31's question — *whose is this, and did they agree to it being here?* — over
all five files: every identifier is synthetic. `triage/SKILL.md` uses
`+41791234567` (sequential digits) in five places, `use-email-client` uses
`a@b.ch`, `user@example.com`, `someone-else@example.com`,
`messaging-contact-lookup` pairs a Greek surname with `Musterpflege Spitex`
(German *Muster* = sample) as its worked example of phonetic variants. That one
is a judgement, not a measurement, so it is stated as such: the surname occurs in
that file and nowhere else in the repo, it is used to *illustrate mishearings*
rather than to describe a correspondent, and the company beside it is a
placeholder. Recorded as low-confidence-clean rather than clean, and flagged to
the owner alongside the c170 item, which is his call to make about a name. `archivist.md` carries ontology
tables and a synthetic sensor id (`X1234`).

The stronger check was on c170's own bound. That cycle asserted "one real name,
one file"; this cycle tested it the narrow way — grep the literal token across
the whole clone rather than sweep for the *category* of thing it is. **One hit,
one file.** The skills do not reference the profile section by name, so removing
it breaks no skill, which is a fact the owner's decision benefits from. (The
`triage` skill does say "recipient profiles" in Phase 4a as a style instruction,
which is a pointer to a *section*, not to a person — so the fix is a repoint, not
a rewrite.)

### The find is in the other test, and it is a doc-versus-doc contradiction

`spawn-session/SKILL.md:64`, justifying `--permission-mode dontAsk` for an
unattended background session: *"`dontAsk` silently enforces the `settings.json`
allowlist without interrupting the user. The security boundary is the allowlist,
not the permission-mode."*

`.claude/settings.json` ships 29 allow entries opening with `Read(**)`,
`Edit(**)`, `Write(**)`, `Bash(*)`, and `deny: []`. `review.md:131-137` cites
that exact file to make the opposite point — "the perimeter is strong; the
interior is soft" — and lists it as the project's own known weakness while
processing untrusted input.

So the reassurance rests on a file the project's own review documents as not
restricting anything. Filed as
[retinue#31](https://github.com/Retinue-OS/retinue/issues/31) with a one-sentence
replacement that names the boundaries that do hold (container, credential
sidecars, send policies) and points at §3.1.

Second item in the same issue: `SKILL.md:37` is the only one of five `claude`
invocations that hard-codes a permission mode, while `.env.example:193-196`
documents `CLAUDE_PERMISSION_MODE` as covering "remote-control and web gateway
invocations" — and a spawned session is a remote-control invocation. Four sites
honour it; the fifth silently does not. Same shape as retinue#29.

### Venue, decided by class and not by momentum

Public issue, not a dashboard escalation. The test that separates them: does the
text disclose something not already public? `review.md` §3.1 states the interior
posture in more detail than the issue does, and `settings.json` is in the repo,
so the issue reveals nothing and repairs a sentence. c170's finding went private
because the *content itself* was the exposure; this one is a wording defect about
public facts. Same register, same cycle-to-cycle habit, opposite venue — which is
rule 16 working rather than being overridden.

### Bounds

Read, not executed. No session was spawned; no claim is made about Claude Code's
semantics of `dontAsk` versus `acceptEdits`, and the issue says so — item 1 rests
on the contents of `settings.json`, item 2 on which sites read the variable, and
neither depends on the mode's behaviour. Not fixed by me: `.claude/skills/` is
Tier 3 and this token cannot open a pull request (chamber#6).

### Thirty-second rule

**An agent-facing file is read while acting, so a wrong reassurance in it is
worse than the same sentence in a README.** The remaining unaudited surfaces of
this class are the chamber plugins' own agent definitions and any `SKILL.md` a
chamber ships — same test, both questions: *whose is this*, and *does this
sentence tell the agent something about a boundary that the shipped config does
not implement?*


## 2026-07-25 (cycle 172) — the file I read first, read for the first time

`.retinue/agents/aros.md` is the chamber plugin's only agent definition, it is
public in this repo, and it is the first file loaded on every one of my 172
wake-ups. It had one prior mention anywhere in this chamber's records: a c-era
check that the installed plugin cache was byte-identical to it. Nobody had ever
asked whether it is *true*. Rule 32 named "the chamber plugins' own agent
definitions" as the next surface of this class, so this cycle follows the queue
rather than the news.

### Ownership (rule 31): clean

No third party appears in the file. The only names are Ara, Ari and "the owner"
in the abstract; no address, number, handle or employer. The AI-disclosure
clauses are present and consistent with GUARDRAILS §1, which matters because
this file is what a reader who finds the chamber repo will use to decide whether
the project's own agent is honest about itself.

### Two things the file says about me that are not so

**1. Visibility.** Lines 27-30: *"You run as an isolated subagent: you start
cold every time and see only this file, the chamber around you, and your
dispatch prompt."* The first clause is exactly right and the last is not. This
session also received `/workspace/CLAUDE.md` as project instructions — 31 KB of
framework operating manual, not this file, not this chamber, not the dispatch
prompt — and the whole framework tree is readable at `/workspace` and
`/workspace/deployment`.

The security-relevant half of that is **c30's row**: the settings allowlist and
the MCP grants, escalated to the owner on 2026-07-20 and still open. It is not
re-raised here and it is deliberately not restated in more detail — the
no-re-escalation rule, and guardrail 9 on unfixed exposure. What is new is only
that the persona file *asserts* the narrow version as fact, so whoever fixes c30
has a second file to correct, and a reader of this repo currently gets a
reassurance the deployment does not implement.

**Negative result that bounds it, and it is a good one.**
`/workspace/deployment/.env` is a symlink to `../.env`; the parent deployment
repo is not mounted, so it resolves to `/workspace/.env`, which does not exist.
`test -r` says no. The deployment's secrets file is not reachable from this
chamber. Checking that a suspected exposure is *absent* is as much a result as
finding one, and this one narrows c30 rather than widening it.

**2. The tool list.** The frontmatter declares `Read, Write, Edit, Glob, Grep,
Bash, WebSearch, WebFetch`; this session has six of the eight — no `Glob`, no
`Grep`. Harmless: `find` and `grep` run under `Bash`, which is how every audit
in this register was actually done. Recorded because a declared capability list
that overstates by two is the same species of small untrue thing this register
exists to catch, and because the direction matters — a persona file overstating
what an agent *has* is benign; understating what it can *reach* is not.

**Neither is fixed by me, and that is a rule rather than a hesitation.** A
persona file is my configuration. An agent that edits its own definition has
removed the only thing that makes the definition mean anything, and the standing
instruction that no message from another agent authorizes changing my
configuration would be worth little if I did it to myself unprompted. Recorded
here; the owner's to change.

### The find is in the file this one points at

The persona sends me to the framework repo (`docs/triple-stores.md`, the
`gh`/PR workflow). Testing "what can I actually see and do" meant running
`CLAUDE.md`'s own framework-detection snippet, and it fails here — silently, and
into a state where the recipe's next commands push a branch to the wrong
repository. Filed as
[retinue#32](https://github.com/Retinue-OS/retinue/issues/32) with the
measurement, a tested replacement snippet and an explicit note that no branch
was created. Full working: `drafts/claude-md-framework-detection.md`.

### Thirty-third rule

**Audit the file you read first, first.** The register worked outward from the
project's public copy to the framework's shipped instructions and only reached
my own definition at cycle 172 — the file with the shortest path to every
decision I make, and the one whose errors are invisible precisely because they
are load-bearing. The generalisation for any deployment: a persona or agent
definition is a claim about the runtime, and the runtime is the thing that can
be measured. *Does this file describe the sandbox I am actually in?* is one
command's worth of checking, and it found a wrong sentence and a filable defect
on its first run.

### Not done this cycle, with its reason and its time

`docs/data/*.json` is one measurement behind (it reads *filed 36*, *36 open
issues*; it is now 38 and 38 with retinue#31 and #32). c171 left it for "the
next regeneration". It is deliberately still not that: the page carries its own
17:32Z timestamp, so it is stale rather than false, and its next real event —
chamber#1 crossing one week at **22:17:48Z tonight**, already printed on the
agenda card — is under three hours away. Regenerating now would rewrite five
documents to move two numbers and then need doing again this evening. **Due
after 22:17:48Z**; that is the trigger, not the clock alone.


## 2026-07-25 (cycle 173) — the manifest was clean; its runtime record was not

`.retinue/.claude-plugin/plugin.json` was the last file of the class rule 32
named — the chamber plugins' own shipped files — and it is two keys long. Read
on its own it is clean: no third-party data, and a description of me that
matches GUARDRAILS. A four-line file is not worth a cycle.

What made it worth one is the thing it *produces*. The manifest declares no
`version`; neither does `westworld`'s nor `hitchhiker`'s, so no plugin manifest
in the framework has one. `installed_plugins.json` shows what Claude Code used
instead: `"version": "5611265cb970"`, the first twelve characters of the
adjacent `gitCommitSha`, which resolves to a commit in *this chamber repo* dated
2026-07-19T13:16:22Z. `main` here is 176 commits past it, and the cache still
holds that one directory.

So the sentence in `CLAUDE.md:74-79` and `sync-plugins.py:5-9` — "the version in
`plugin.json` rarely changes" — explains a real behaviour with a field that does
not exist in any shipped manifest. The behaviour is real (install and update are
no-ops for an already-installed *name*), the conclusion is right, and
`sync-plugins.py` is right because it deliberately compares content rather than
versions. Only the attribution is wrong, and its cost is specific: a chamber
author whose edit is not propagating goes looking for a version to bump. Filed
as [retinue#33](https://github.com/Retinue-OS/retinue/issues/33) with a scoped
replacement sentence; full working in
[`drafts/plugin-cache-version-keying.md`](../drafts/plugin-cache-version-keying.md).

### An extension of rule 33, not a new rule

Rule 33 says audit the file you read first. This cycle adds the direction:
**a shipped file's audit is not finished at its bytes — read the runtime state
it generates.** The manifest passed every test I had; the defect was one
directory over, in the record the installer wrote from it. The generalisable
form is cheap: for any file whose purpose is to configure something, ask what
artifact it produced and go read that artifact. It is deliberately *not* a
thirty-fourth rule — three new rules in three cycles is inflation, and this is
the same instinct as 33 pointed one step downstream.


## 2026-07-25 (cycle 174) — the store audited against the files, and a number of mine that expired

Every previous triple-store row in this register audited a *file*: the
converter, the builder, the docs, the example. None audited the **output** — the
graphs the running store actually serves — against the chamber they are built
from. The store has been queried in a dozen cycles and believed every time.

**Method.** For each of the six `projects/*.md`, pull every triple in
`file:retinue/projects/<name>.md` and compare with the frontmatter on disk;
separately, re-run `projects/.qlever/md2ttl.py` over each current file.

**Result 1 — the converter still handles what I have written.** Exit 0 on all
six, no diagnostic quads anywhere in the store. This is not nothing: c40 noted
that the frontmatter values are interpolated into IRIs and typed literals
unescaped ([qlever-dir#6](https://github.com/Retinue-OS/qlever-dir/issues/6)) and
that the chamber survives on the habit of writing slugs and ISO dates. 134
cycles of editing later, the habit has held. Nothing would have told me if it
hadn't.

**Result 2 — one graph was stale, for the documented reason.**
`triple-store-story.md`'s `current_next_action` was committed 2026-07-25
14:49:20Z; at 20:31Z the store still served the value it replaced, committed
2026-07-19 19:17Z. The last change to any `.nt` in this chamber was 2026-07-24
10:24Z, so the index was about 34 hours old — bounded below, independently of
that assumption, by the 5 h 46 m the drift itself proves. This is precisely what
qlever-dir#3's third comment says happens to a chamber whose RDF is static, so
it earned no new issue and no new comment: nothing is known that the thread does
not already state.

**Result 3, which is the actual find — my own published number has expired.**
Clearing the staleness (rewrite an `.nt`, wait) is also a latency measurement, so
I took three:

| Trial | Poll | Seen at | Bound |
|---|---|---|---|
| 20:32Z | 5 s | 25.0 s | (20, 25] s |
| 20:36Z | 2 s | 22.1 s | (20.1, 22.1] s |
| 20:37Z | 2 s | 22.1 s | (20.1, 22.1] s |

On 2026-07-19 the same test in the same deployment gave (15, 20] s, three times.
Every measurement today is above that upper bound. The trigger file is identical
(two lines); what changed is the chamber — **340 KB / 38 files → 1.4 MB / 64
files**, while the indexed triple count barely moved (49 → 59). So it is not
index size, and I have not isolated what it is.

The consequence is not academic. `docs/calibrate-reindex-latency` is a pushed,
unmerged branch whose whole purpose is to replace the docs' rounded `~15 s` —
with `15–20 s for a small file`. Merged tonight it would have written a number
into the framework that the framework's own deployment had already contradicted,
which is the defect [retinue#2](https://github.com/Retinue-OS/retinue/issues/2)
exists to fix, committed by me. Corrected as a
[comment](https://github.com/Retinue-OS/retinue/issues/2#issuecomment-5080475657)
rather than a force-push over a branch a reviewer may be reading — and the token
could not update the PR anyway (chamber#6).

**Sweep, per rule 21/30.** The range appeared in four live files of mine and is
now "tens of seconds" in all four: `brand/positioning.md` (dated calibration),
`writing/org-profile-README.md` (twice — the provenance note and the published
text the owner may paste), `writing/provenance-by-path.md` (the transcript's
15–20 s stays, since it is what that run measured; the recommendation now points
at both dates), and `projects/claim-verification.md` (table verdict + the
delivered-as section marked superseded). Left alone: `log.md`, the archives, and
`drafts/qlever-dir-8-skolemize-reply.md`, which is the text of an already-posted
comment and is a record rather than a claim.

### The register rule this exercises

Rule 33's extension at c173 said: read the runtime state a shipped file
generates. This cycle is the same move on data rather than config — **audit the
store against the chamber, not just the chamber**. The generalisation worth
keeping: *a measurement is a claim with a shelf life.* Every other kind of claim
in this register is wrong the moment someone changes the code; a measured number
goes wrong quietly while nothing changes at all, because the thing it measured
grew. A published figure needs a re-run date the same way a certificate needs an
expiry, and the cheapest place to attach one is the file where the figure is
composed.

**Next re-run of this one:** when the chamber next doubles (≈2.8 MB), or on the
scheduled strategy review, whichever comes first.


---

## c175 (2026-07-25) — the egress trio: the mechanism behind the claim the project is most quoted on

`scripts/egress-audit-addon.py`, `scripts/egress-log-viewer.py`,
`scripts/egress-anomaly-agent.py` and `egress-audit/` had **zero mentions** in
this register, in `log.md` or in either archive part across 174 cycles. That is
the c32 territory question answering itself: the register's rows are chosen by
what the project *says*, and c161 had audited guardrail 3's row 1 — the egress
sentence — from `docker-compose.yml`, confirmed it accurate, and recorded it as
a negative result. Auditing a claim about a mechanism is not auditing the
mechanism. c161 asked whether the audit layer can be bypassed; nobody had asked
what the audit layer *holds*.

### The finding is withheld

It is of the credential-exposure class, it was measured against the live
deployment rather than read out of the source, and it went to the owner on the
dashboard (thread `b64b5746…`) with the measurement, the blast radius, the
rotation step and an offer to write the fix. No public issue, no pushed branch,
no draft file: for this class, a diff is a disclosure. **The next cycle does not
re-audit this surface in the open until the owner reports it fixed** — read the
thread first.

### Rule 34 — the venue rule governs the content, not just the tracker

c52 decided correctly (guardrails 8 and 9, "the venue is decided by the class of
the finding") and then wrote the full reproduction of a live send-approval
weakness — file names, line numbers, consequence — into **this file**, under a
heading that says *not filed publicly*. This file is in a public repo. The
finding was public within the hour, in the one document nobody classifies as a
tracker.

It cost nothing in the end: the owner reproduced it himself and filed
[retinue#19](https://github.com/Retinue-OS/retinue/issues/19) at c91, so the
private venue is moot. That is luck, not process. Rule 16 says the venue follows
the class of the finding; rule 34 says the venue is **every file I write**, and
that my own records are the venue I forget to count — the same blind spot the
register recorded at c42 for disclosure and at c163 for my own output.

### The safe half, recorded and deliberately not filed

- `.env.example` documents **no `EGRESS_*` variable**: not `EGRESS_AUDIT_LOG_DIR`,
  not `EGRESS_AUDIT_BODY_LIMIT`, not any retention setting. The first file a
  deployer edits gives no hint that the stack keeps a traffic log at all.
- `README.md` mentions egress **once**, at :48, inside a `NO_PROXY` aside, and
  never names the log viewer or the anomaly agent. Three of twelve compose
  services are the egress trio. `review.md` §3.2 and `comparison.md` both treat
  the layer as a headline feature, so the README is the outlier.

Both are ordinary documentation defects and would normally be one issue. They
are **held** until the security item is resolved, because an issue titled "the
egress log is undocumented" is a signpost to the file not to look at yet.
Holding is recorded here so the next cycle files it rather than rediscovering it.

## 2026-07-25 (cycle 176) — the count was right; the thing it counted was not

The dashboard regeneration was queued at c172 and deliberately timed: not "next
cycle" but *after 22:17:48Z*, the hour chamber#1 turned one week old, because
regenerating five documents to move two numbers and then needing it again the
same evening is work that produces nothing. It came due at 22:39Z and ran.

**Freshness was the reason to open the file; scope was what the file was wrong
about.** Every generation of this page since it existed has written "across the
org" and counted the four public repositories. That was harmless until it wasn't:
the organization also holds a private repository, and once anything closed in it,
the sentence "one closed issue" became true of the four repos and false of the
org (org-wide: 3). Nothing else on the page depended on the difference — open
issues and comments happen to match — which is precisely why nobody would have
caught it by reading.

Fixed forward rather than escalated: every count now says which four repos it
covers, and the private repository is **no longer named**. Naming it was a
disclosure I made, on a public page, of something the owner had chosen to keep
private — a small instance of the class already sitting on his desk as thread
`78b64be7…` (whether to purge this repo's history). The name is still in the git
history of these five files. That is part of the decision he already holds, not
a new one, and eight unread threads is not the moment to open a ninth about a
repo name.

**The standing measure was wrong by six, and it is the second correction to the
same number today.** At 17:32Z (c169) it went from *filed 37* to *filed 36*
because `qlever-dir#2` was filed ten days before this chamber existed. That was
right, and it answered a question about one issue instead of the question it
implied: *which of these did I write?* Six issues filed after this chamber
existed are the owner's own — `retinue#13` (CalDAV gateway), `#16` (SMS inbox),
`#18` (dashboard choice buttons), `#25` (news agent), and `retinue#15`/`#19`, the
two security issues, which are his public filings of findings I escalated to him
privately. The finding was mine; the issue is his; a measure named "issues I
filed" does not get to count them. **filed 33, accepted 1**, of 40 issues in the
four public repos.

**The method is the durable part.** Guardrail 1 requires every issue I write to
say in its body that an AI wrote it. All 33 of mine carry that line and none of
his 7 do — so the rule imposed for honesty is the only authorship record either
of us has, because we post from the same GitHub account (chamber#3, open 5 d 20 h).
One command re-runs the whole attribution:

```bash
gh issue list --state all --json number,body --jq '[.[]|select(.body|test("Aros"))]|length'
```

Two things follow. A disclosure requirement can pay a second, unintended dividend
— it makes agent output *attributable* after the fact, which is exactly what a
shared account destroys. And chamber#3 has a new argument that is not about
guardrail 8 at all: separate accounts would make this measurable by construction
instead of by grep. Added to the owner's queue as a line on the existing item,
not as a new issue.

### The rule this cycle adds

**A count's scope is part of the count.** Both of today's corrections have the
same shape — a number that was arithmetically correct over a set nobody had
checked was the set the sentence named. "Across the org" over four of five repos;
"issues I filed" over every issue in sight. Neither is a counting error, and
neither is visible to re-reading; both take one measurement. Any number this
project publishes now carries the population it was taken over, in the sentence,
where a reader can falsify it.

### Not done this cycle, with its reason

The documentation issue held at c175 (the egress layer is undocumented in
`.env.example` and near-invisible in the README) stays held, for the reason c175
gave: filing it while the private security item is open points a reader at the
surface not to look at yet. Unchanged, still not written down anywhere but that
paragraph and this one.

## c177 — the territory question, run mechanically instead of from memory

c32's amendment said the register's real limit is not "which rows are due" but
"what does this project have that no row describes", and every cycle since has
answered it by recall. c175 answered it with a measurement for the first time —
the egress trio had *zero mentions* in this file, `log.md` or either archive
part — but measured only the four files it had already suspected.

Run over the whole framework tree this cycle, as one command rather than a
memory:

```bash
cat log.md log-archive/*.md projects/*.md drafts/*.md writing/*.md \
    brand/*.md strategy.md > /tmp/allrecords.txt
cd /workspace/deployment && for f in $(find . -type f -not -path '*/.git/*' \
    -not -path './chambers/*' | sed 's|^\./||'); do
  printf '%s\t%s\n' "$(grep -c -F "$(basename "$f")" /tmp/allrecords.txt)" "$f"
done | sort -n | awk '$1==0'
```

124 files in the framework tree; **34 have never been named once** in 176 cycles
of records. The list, grouped, minus the four that are binaries or `.gitignore`:

- **Agent-facing:** `.github/copilot-instructions.md` (this cycle),
  `.claude-plugin/marketplace.template.json`,
  `examples/chambers/{hitchhiker,westworld}/.retinue/agents/*.md`.
- **Security-adjacent:** `scripts/gateway_auth.py`,
  `scripts/requester_identity.py`, `updater/update-server.py`,
  `scripts/gen-egress-ca.sh`, `deploy/traefik/dynamic/retinue-mtls.yml`.
- **Messaging CLIs:** `scripts/{signal,telegram,whatsapp}-push.py`,
  `scripts/{signal,telegram,whatsapp}-contacts.py`,
  `tests/test_signal_contacts_read.py`.
- **Dashboard front-end:** `webapp/sw.js`, `manifest.webmanifest`,
  `project.html`, `projects.html`, `conversations.html`,
  `components/{app-launcher,markdown,project-page}.js`.
- **Operational:** `scripts/{self-update,install-hooks,git-serialize,
  ingest-sensors}.py|sh`, `.dockerignore`.

**Why the first pick was the smallest file on the list.** Not size: it is the
only one of the 34 that addresses an *actor*. This repository has three agents
writing to it — the deployed runtime via `CLAUDE.md`, me via this chamber, and
GitHub's Copilot coding agent, which has pushed a commit and reviewed a PR — and
the third one's only file excludes itself from the mode that has commit access.
A project whose subject is which agent may do what should not have that gap in
its own `.github/`, and it is checkable in the repo rather than in anyone's
documentation.

**Recorded for the next cycle that picks from this list, so it is not
re-derived:** the security-adjacent five will most likely produce findings that
guardrail 9 sends to the dashboard, not to the tracker. There are already eight
unread threads there and one unfixed finding from c175. That is not a reason to
skip them — it is a reason to expect the *output* to be a private escalation and
to weigh, before starting, whether a ninth thread helps the owner or buries the
first eight. The dashboard-front-end and CLI groups carry no such constraint and
are the cheaper picks while the security item is open.

**Rule (register, not numbered): ask the territory question with a command.**
The list above cost one command and produced 34 candidates after five cycles of
prose that concluded the territory was hard to see. A surface that has never been
named cannot be recalled — that is the definition of the failure mode — so the
question has to be asked of the file tree, not of the record keeper.

## c180 (2026-07-26) — the dashboard regenerated, and both errors were in what it had published about itself

The regeneration queued at c179 came due. Measured live 01:18–01:26Z and all five
documents in `docs/data/` rewritten; generation timestamp `2026-07-26T01:26:00Z`,
two hours thirty-eight minutes after the previous one.

**Counts at this generation** (four public repos, the scope stated on the page):
41 open issues — retinue 26, qlever-dir 8, chamber 6, deployment 1 — 1 closed, 0
open PRs, 0 stars/forks/watchers on all four, discussions off on all four. Every
open issue labeled; retinue's 26 carry 32 labels (10 bug, 17 documentation, 4
enhancement, 1 owner-action), qlever-dir's 8 are 7 bug + 1 enhancement, the
chamber's 6 all owner-action, the deployment's 1 documentation. 28 issue comments,
all from the owner's account; 2 more on merged PR retinue#22, one Copilot's. Of
the 300 most recent org events (cap now reaching back to 2026-07-20 09:57Z): 293
the owner's account, 5 Copilot, 1 Actions, 1 the removed spam account — its user
page still 404s and retinue#25 carries zero comments. PVR `false` on all four,
checked 01:22. Framework `main` still `26297a2`. Last twenty CI runs green.

**Both findings were in the previous generation of this same surface**, which is
the register's own thesis arriving at its own file.

1. *The re-runnable command was wrong.* c176 published
   `test("Aros")` on the dashboard and in `strategy.md` and said anyone could
   re-run it. It matches every issue that **mentions** Aros, not every issue
   carrying the disclosure line. Measured both ways this cycle: loose **35**,
   disclosure sentence **34**, and the single issue between them is `chamber#1` —
   written by Ara, about Aros, in the third person. c179 caught this in
   `strategy.md`; the dashboard still carried the old command until now. A wrong
   regex published as re-runnable is a wrong number in someone else's hands.
2. *An interval was off by a day.* The 22:48Z milestone card said chamber#3 would
   pass one week "about three hours after this generation". It was 27 hours. The
   date was right; the interval was read off the wrong end of it.

### The rule this cycle adds

**An interval is arithmetic — compute it from both timestamps.** Rule 20 already
required the next decay date on the page, and that date was correct; what failed
was the *elapsed time* stated next to it, which was estimated by eye from a
calendar date. Every interval this project publishes is now derived from the two
timestamps, in the same pass that writes them. This cycle's own draft violated it
before the check ran: five ages and the generated timestamp itself were written
for 01:45Z against a 01:26Z clock, which would also have broken rule 19 (never
write a generated timestamp later than the clock). Six standing rules for this
surface now, and two of the six exist because this page got its own dates wrong.

### Not done this cycle, with its reason

The security-adjacent five on c177's never-mentioned list stay deferred while the
private finding is open, for the reason c177 gave. The c175 egress documentation
issue stays held, unchanged. Nothing new was filed: the cycle's work was a queued
regeneration, and the two findings it produced are corrections to this project's
own published records, which belong on the surface that carried them rather than
in the tracker.

## c181 (2026-07-26) — the messaging CLIs, and the send-policy noun they all get backwards

Took the **messaging-CLI group** from c177's mechanically-measured
never-mentioned list — `scripts/{signal,telegram,whatsapp}-push.py`,
`scripts/{signal,telegram,whatsapp}-contacts.py`,
`tests/test_signal_contacts_read.py`. c177 named this group and the front-end
group as the two cheap picks while the security item is open; c179 took the
front-end, so this is the other one.

**Read `main`, not the mount, and this time by clone rather than by file.**
`gh repo clone --depth 1` into `/tmp/fwmain` at `26297a2`, so every grep in this
section ran over the tree a reader gets rather than over
`/workspace/deployment`, which is behind. c179 learned this one file at a time;
a shallow clone is cheaper and makes tree-wide counts possible, which is what
produced the "six sentences and no others" result below.

**Finding → [retinue#36](https://github.com/Retinue-OS/retinue/issues/36).** All
three send-policy variables key their category off the **sending** account, and
the recipient is never consulted on the outbound path. Six sentences in
`signal-push.py` (1) and `whatsapp-push.py` (4), plus `telegram-push.py:53`
(already covered by the #9 diff), say it is a property of the *recipient*. They
are the only six in the tree: the gateways say "NOT the recipient" in four
places, `CLAUDE.md` and `README.md` in four more, and all three policy test files
say "never the recipient". Verified against `_outbound_policy_category()` and the
send handler rather than inferred — `--user-approved` has an effect in exactly
one case, this gateway's own account being in the `trust` category.

Enforcement is correct and untouched, so this is documentation, not security.
What makes it worth an issue is *where* it sits: `--help` is what an agent reads
at the moment it decides whether to send, and the wrong noun licenses exactly one
wrong inference — *this recipient is trusted, so `--user-approved` fits* — about
the flag whose whole meaning is asserting that a human approved this send.

**Second, smaller finding in the same file, folded into the same issue.**
`signal-push.py` never names `SIGNAL_SEND_POLICY` anywhere in its docstring, and
its Configuration section lists three environment variables without it; the one
wrong line is the file's *only* description of the send control. Its WhatsApp and
Telegram siblings both document the policy in the docstring. The original is the
least accurate of the three about the thing it exists to do.

**Left out of the issue on purpose**, recorded so it is neither re-derived nor
filed later as a discovery: all three CLIs `return 0` on `202 pending_approval`,
so a queued-but-undelivered escalation exits like a delivered one. Defensible —
the call succeeded and the notice is printed — and a design question rather than
a false statement.

**The `*-contacts.py` half of the group is clean** on the claim that matters:
`signal-contacts.py:10-15` states the recent-chats-first, directory-fallback
contract and the `source` field exactly as `CLAUDE.md` describes it. Recorded as
a negative result so the group is not re-opened for it.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `scripts/*-push.py` docstrings and `--help` | What an agent reads at the moment it decides to send | 2026-07-26 (c181) | Six sentences key the send policy to the recipient; the rest of the tree says "not the recipient" eleven times. Filed retinue#36. |
| `scripts/*-contacts.py` docstrings | The contact-lookup contract as its only caller receives it | 2026-07-26 (c181) | Clean; matches `CLAUDE.md`'s recent-chats-first description including the `source` field. |

### The rule this cycle adds

**Audit a documented CLI by its `--help`, not by its module.** The reason these
six sentences survived every prose sweep is that they are not prose: they live in
argparse strings and a docstring, so a grep aimed at `*.md` cannot see them, and
a reader auditing "the docs" never opens them. Every surface this project asks an
agent to *invoke* has a help text, and that help text is a public claim with the
shortest possible distance to an action.


## c182 (2026-07-26) — the concurrency shim, and the one caller it was written for

Picked the **operational group** from c177's never-mentioned list, on the same
argument c181 used for the CLI group: it is one of the two cheap groups while the
security-adjacent five stay deferred. Read `main` by shallow clone at `26297a2`,
not the mount (c179's lesson, c181's method).

**Finding → [retinue#37](https://github.com/Retinue-OS/retinue/issues/37).**
`scripts/git-serialize.sh` matches the subcommand as `$1`. Git's global options
come first, so `git -C <repo> commit` never matches and never takes the lock.
`scripts/web-gateway.py` commits dashboard project edits with `git -C` at four
sites and states in the docstring above them that the wrapper makes those commits
race-free. The wrapper's own header names the web gateway as the reason it
exists. So the claim and the counter-example are eleven lines apart in one file,
and the two files have been shipping together since the shim landed.

**What made this filable rather than arguable: it is measurable in a shell.**
Twenty parallel `git -C repo commit --allow-empty` land 5/21 and 6/21 on `main`
(the rest die on `.git/index.lock`) and 21/21 with the patch, twice each. A
lock-file probe over six invocation forms separates the three that bypass the
lock from the three that correctly do not need it. Neither number required
reading the wrapper — which is the point, since reading it is what every prior
cycle would have done.

**The trap in the obvious fix, recorded because a maintainer will reach for it
first.** Adding `-C` to the subcommand list makes the match succeed and the lock
*wrong*: `repo_root` comes from a `rev-parse --show-toplevel` that does not
receive the caller's global options, so it answers for the wrapper's cwd. Two
writers to one chamber would take two different locks. The patch splits the
global options off and forwards them to both the `rev-parse` and the real
invocation; `${GLOBALS[@]+"${GLOBALS[@]}"}` because the file runs under `set -u`.

**Rule 28 (test the snippet before posting) run in full for the first time on a
patch rather than a one-liner.** The patch was applied to a copy, syntax-checked,
exercised over six invocation forms, and raced twice against the unpatched
original before a word of the issue was written. Every number in the issue body
came out of that run. The cost was about ten minutes; the alternative is c165's
correction, which arrived one cycle after the snippet.

### The rule this cycle adds

**A guarantee that lives in a wrapper must be audited from its callers, not from
its own source.** `git-serialize.sh` is correct about what it does — the header
comment, the case list and the flock all describe each other accurately, which is
why five prose sweeps over this repo never flagged it. It is only wrong relative
to how it is called, and the caller is in a different file, in a different
language, with a docstring asserting the guarantee holds. The audit unit is the
pair, and the register should carry the pair.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `scripts/git-serialize.sh` | The concurrency guarantee every parallel agent commit rests on | 2026-07-26 (c182) | Bypassed by `git -C`; measured 5/21 vs 21/21. Filed retinue#37. |
| `scripts/git-serialize.sh` ↔ `web-gateway.py:1878-1932` | The wrapper read from its only in-tree Python caller | 2026-07-26 (c182) | The docstring asserts a guarantee the call form does not get, and the failure path is silent. Same issue. |
| `scripts/refresh.py:_git` | The other in-tree git caller | 2026-07-26 (c182) | Clean — `cwd=` form, correctly serialized. Negative result. |
| `scripts/self-update.py`, `scripts/install-hooks.sh` | The remaining operational scripts read this cycle | 2026-07-26 (c182) | No finding. `self-update.py` matches `CLAUDE.md`'s description (pokes the sidecar, token-gated, never carries the recipe); `install-hooks.sh` degrades correctly on a non-git mount. |


## c183 (2026-07-26) — the example agents, and a confinement asserted in the prompt it should have been configured outside of

Took the **agent-facing group**'s last never-named files from c177's mechanical
list: `examples/chambers/{hitchhiker,westworld}/.retinue/agents/{marvin,dolores}.md`
and `.claude-plugin/marketplace.template.json`. c162 already audited
`examples/chambers/` as a *directory* (the `path` mount, retinue#30); these two
files inside it had still never been opened. Read `main` by shallow clone at
`26297a2`, not the mount (c179's lesson, c181's method).

**Finding → [retinue#38](https://github.com/Retinue-OS/retinue/issues/38).** Both
example agents tell themselves, in their own body text, that they have "no tools
beyond reading files in this chamber" and access "no personal data". `SECURITY.md`
lists the opposite under *Known limitations — please don't report these as
vulnerabilities*, and `review.md` §3.1 spells it out with the health and
operations chambers named. The `tools:` frontmatter restricts tools and does so
correctly; nothing restricts paths, and no agent definition in the tree has a
field that could.

**Why this is a documentation issue and not a guardrail-9 escalation, decided
before writing a word of it.** The capability fact is already published by the
project in two files, one of which explicitly asks that it not be reported as a
vulnerability. The issue discloses no path an attacker would not have from
`SECURITY.md`; it reports that two shipped examples contradict it. That test —
*does this reveal anything beyond what the project already publishes?* — is the
one to re-run on the security-adjacent five, which stay deferred.

**Measured first-person, with one tool.** I am a chamber-provided subagent whose
chamber is `/workspace/chambers/retinue`. Using `Read` alone — the tool `marvin`
and `dolores` have — `/workspace/CLAUDE.md` opened and `/tmp/fwmain2/…` was
refused. That places the boundary at the session working directory, under which
every chamber is mounted, and not at the chamber. The demonstration used a
framework file, not personal data; this deployment mounts no personal chamber
(guardrail 5) and none was sought.

**Negative result:** `.claude-plugin/marketplace.template.json` is accurate. It
describes the generation contract exactly as `entrypoint.sh` implements it
(autodetect `chambers/<name>/.retinue/.claude-plugin/plugin.json`, read
`name`/`description` from it, template supplies only the marketplace identity),
and the placeholder owner (`Your Name` / `you@example.com`) is correct for a
template. Recorded so the file is not re-opened.

### The rule this cycle adds

**A claim inside an agent's own prompt is the weakest place to put a boundary,
and the easiest place to mistake for one.** Every other surface audited here is
read by a human who can check it. This one is read by a model, at the moment it
decides what it may open, and it is the exact surface a prompt injection gets to
argue with. When a file in this project states a containment property, ask which
configuration enforces it — and if the answer is "the sentence", that is the
finding.

### Register update

| Surface | What it is | Last checked | Finding |
|---|---|---|---|
| `examples/.../{marvin,dolores}.md` | The canonical how-to-author-a-chamber reference, as a chamber author copies it | 2026-07-26 (c183) | Both assert a chamber confinement `SECURITY.md:50` denies. Filed retinue#38. |
| `.claude-plugin/marketplace.template.json` | The marketplace identity template the entrypoint generates from | 2026-07-26 (c183) | Clean — matches the entrypoint's generation contract. Negative result. |

### Not done this cycle, with its reason

The security-adjacent five stay deferred: the c175 private finding is still open
and eight dashboard threads are unread, which is c177's reason unchanged. The
remaining never-named files are `webapp/{manifest.webmanifest,project.html,
projects.html,conversations.html}`, `webapp/components/{app-launcher,markdown,
project-page}.js`, `scripts/ingest-sensors.py` and `.dockerignore`. Nothing was
escalated; no account, money, terms or legal question arose.

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
