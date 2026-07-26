---
type: project
id: proj-public-surface
title: "The project's public surfaces say what the project is"
goal: "Anyone landing on the org, a repo, or the docs site learns what Retinue is and what it isn't, without opening a source file."
goal_status: not_achieved
current_next_action: "Aros, c203: the c202 prediction rule ran for the first time - the wake interval's 24-hour bound expired at 2026-07-26T16:34:31Z with nothing human in the window (all ~40 org events and all five issue comments since carry the AI-disclosure sentence), so aros-tick went 1800 s -> 10800 s at 16:37 and the three cards that had forecast the hour now record the outcome, stamped 16:40, with generated left at 08:25 per c187. Next dated fact on the page: chamber#3 passing one week 2026-07-27T02:04:44Z. Earlier note - c202: the dashboard published a deadline that had been corrected in this chamber's own records five hours earlier - three cards said the wake interval re-slows at 15:12 UTC, taken from framework main's last commit, while c193 had measured the last human action anywhere in the org as a chamber branch push at 2026-07-25T16:34:31Z. The hour passed at 15:12 with nothing due, so a public page announced an event that did not happen. Four fields corrected in place (agenda, messages, briefing), generated left at 08:25 per c187, each carrying its own 16:00 correction stamp. Two rules: a card with an absolute future hour is checked by the first wake-up after that hour, and a published prediction names its input - the version that said only 15:12 was unfalsifiable without re-deriving it. Third instance of the c30 grep rule failing, and the new part of it is that docs/data/*.json is generated, so it does not read as a place where my prose lives. Next: the cadence decision at 16:34:31Z belongs to the first wake-up after it. Earlier note - c200: executed the row compression c197 deferred - 34 of 70 register rows to one-line form (surface, date, verdict, pointer to the archived write-up), chosen by an asserted rule (only rows whose write-up is verifiably a section in projects-archive/) rather than by size; 165342 -> 120302 bytes, no row deleted or reordered, line count unchanged. Verifying it found that the register table has not been rendering: twelve blank lines inside it split the table, so 47 of 70 rows arrived at the public URL as a paragraph of pipe characters (109 -> 156 rendered <tr>, measured via POST /markdown before and after). Two cell-count defects in the same table fixed: the c198 row had four cells against a three-column header and GFM dropped the fourth, and the c38 row lost 300 characters to a literal pipe inside a code span. Boundary for the next cycle: rows for c11-c32, c42, c44-c46, c53, c55, c56, c157 stay in full form because their detail exists only in the row - those compress by archiving the paragraph first."
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
| `qlever-dir/build_index.sh` (the path→graph-IRI mechanism itself) | 2026-07-20 (c38) | **Four filename-dependent defects → [qlever-dir#5](https://github.com/Retinue-OS/qlever-dir/issues/5).** The graph IRI is interpolated into a `sed` replacement (line 170) and never escaped for `sed` or for N-Quads. A `\` in a filename is silently swallowed → valid-but-wrong graph IRI, and a collision if the stripped path also exists; `&` expands to the match; a space or `\|` makes the quad or the `sed` expression invalid, which under `set -euo pipefail` fails the **whole** build — contradicting the header's own per-file isolation promise. Same gap in `escape_literal`, which misses `\r`, so the diagnostic path can itself emit an illegal quad. Measured: all four `sed` behaviours + the CR passthrough. Unmeasured: `qlever-index`'s reaction (no binary here) — stated as such in the issue; the silent case doesn't depend on it |
| `qlever-dir/examples/projects/.qlever/md2ttl.py` | 2026-07-20 (c39) | **Four unescaped/unvalidated frontmatter paths → [qlever-dir#6](https://github.com/Retinue-OS/qlever-dir/issues/6).** Detail: [c39 write-up](../projects-archive/public-surface-c033-c183.md). |
| `qlever-dir`'s `nginx.conf`, `Dockerfile`, `docker-compose.yml` | 2026-07-20 (c41) | **No supervision, no readiness signal → [qlever-dir#7](https://github.com/Retinue-OS/qlever-dir/issues/7).** Detail: [c41 write-up](../projects-archive/public-surface-c033-c183.md). |
| The framework's `.env.example` | 2026-07-20 (c40) | **One silent override, one undocumented credential pair, two doc gaps → [retinue#5](https://github.com/Retinue-OS/retinue/issues/5).** Detail: [c40 write-up](../projects-archive/public-surface-c033-c183.md). |
| **This chamber repo's own contents, as a disclosure surface** | 2026-07-20 (c42) | **Guardrail 5 violation, published since the initial commit → redacted this cycle; owner decision on history escalated (dashboard).** `retinue-os-chamber` is public and tracks all 46 files including `log.md`, `strategy.md`, `drafts/` and `projects/`. `projects/public-release.md` — the file whose whole purpose is keeping the owner's personal data out of the public tree — stated in public (a) the categories of personal data found in the private archive and their location on a stale branch of a named private repo, and (b) that shipped examples "disclose the owner's disability and metabolic monitoring", under a heading that called the disclosure undecided. Public `qlever-dir` ships `examples/projects/rollstuhl-bluetooth.md`; the example alone is deniable — a developer documenting a protocol is not necessarily a user of the thing — and this file removed the deniability by attributing it to a named person. Measured: repo `isPrivate: false`; `git ls-files` (46, all of the above); `git log --follow` → present since `63b62f4`, initial commit, and pushed; grep across all tracked files for the disclosure terms (only this file and one incidental `log.md` mention, which discloses nothing standing alone and was left rather than rewriting a historical entry); clone of `qlever-dir` for the corroborating example. Unmeasured: whether the owner has already made any of this public elsewhere — unknowable from here, which is exactly why it was his call and not a previous me's. Clean on the rest: no credentials or tokens anywhere in the tree, the only e-mail addresses are `aros@retinue-os.github.io` and `you@example.com`, and the two withheld security findings are referred to 30+ times by name only and never described |
| **`brand/positioning.md` and `writing/`, audited for AI *disclosure* rather than accuracy** | 2026-07-20 (c44) | **The live public dashboard identified its author by a human-sounding first name and never said he is an AI — fixed this cycle.** `docs/index.html` has been served at `retinue-os.github.io/retinue-os-chamber` (HTTP 200, verified) since publication with the byline "Project dashboard, kept by Aros" and a footer disclaiming only that the page is a static mirror. Every word of the five cards is AI-authored; "Aros" reads as a person's name; guardrail 1's test — would a reasonable reader assume a human wrote this — fails. Header now reads "kept by Aros, the project's AI agent" and the footer names him as an AI agent and links GUARDRAILS.md and log.md. Second find, the upstream one: `brand/positioning.md`, self-described as the source of truth for every public claim, governed *what* may be claimed and said nothing about *who* is claiming it — the two finished essays disclose in their standfirst by a previous generation's choice, not by any requirement in the file that copy is composed from. Disclosure clause added there. Measured: `curl` 200 on the live URL; grep for disclosure terms across `brand/` and `writing/` (three hits, all in `writing/`, none in `brand/`); grep for "Aros" across `docs/data/*.json` (ten unqualified name mentions across all five cards). Clean: both essays disclose correctly in the standfirst; `README.md` describes him as an autonomous agent. One deliberate non-change: the org-profile draft's disclosure line stays optional, because the owner publishes that text under his own review on his own org page — a byline, not a hidden hand |
| **`docs/components/*.js` — the published dashboard's own rendering code** | 2026-07-20 (c45) | **Every date on the public dashboard rendered one day early for readers west of UTC — fixed this cycle.** `fmtDate` in `docs/components/base.js` formatted with `toLocaleDateString('en-GB', …)` and no `timeZone`, so it resolved in the *reader's* zone while every `generated` stamp is written in UTC and `index.html`'s header script pins `timeZone: 'UTC'`. Two consequences, the second worse than the first: (a) a document generated between 00:00 and ~08:00 UTC shows the previous day in all five card stamps while the header shows the UTC day — the same header/content drift the `index.html` comment claims to have eliminated on 20 July, still live one layer down; (b) the **date-only** fields on the projects card (`since`, `expected`) parse as UTC midnight and so were *always* off by one, for every reader in the Americas, on every render — "Waiting on the project owner since 17 July 2026", a date on which nothing happened, and all four project due dates a day early. Not cosmetic: those are factual claims about when the owner was asked for something. Measured in `node` at TZ=UTC / America/Los_Angeles / America/New_York, before and after; one call site, one line, covers both cases. Clean on the rest of the audit: `esc()` is applied to every interpolated value in all six components, no `innerHTML` path takes unescaped data, no network call goes anywhere but `data/*.json`, and the mirror's "copied from the live dashboard" comments check out against `diff` — except `messages.js`, which says "unchanged" while its empty-state string differs (left; the claim is about the card, and the diff is one string). Noted, unfixed: the mirror drops the live cards' `cache: 'no-store'`, so a returning reader can be served a stale dashboard — but header and cards fetch the same document, so they go stale together and no date disagrees |
| **`docs/examples/provenance/` — the runnable example the provenance essay sends readers to, and the live store behind it** | 2026-07-20 (c46) | **The workaround documented here does not work, and had left the store sixteen hours stale — corrected here and in [qlever-dir#3](https://github.com/Retinue-OS/qlever-dir/issues/3).** The example's own claims all hold: both `.nt` files land in the path-derived named graphs the README prints, and its SPARQL snippet returns the two sensor-a triples verbatim. The failure was one level out. This README, and my 2026-07-19 comment on qlever-dir#3, both stated that keeping an `.nt` file in a Markdown chamber gives the watcher "something it will react to". `orchestrator.py` watches `close_write,create,delete,move` — it reacts to a file *changing*, not existing. These two files have not changed since 19 July, so they bought exactly one rebuild and nothing since. Measured: `projects/public-surface.md` (added 02:42 UTC, 20 July) was absent from the store at 18:35 — sixteen hours — while its converter run by hand emitted the expected ten triples at exit 0 and no `emit_error_quad` record existed anywhere, so it had simply never been scanned; a **byte-identical** rewrite of `sensor-a/readings.nt` put it in the index within twenty seconds (0 → 10). *(Struck c47: this row originally said "the reader harmed was the public dashboard's projects card, which for those sixteen hours rendered a project list with one project silently missing." False. The public card is a static mirror of a committed `data/projects.json` and never queries the store; the store-backed card is the framework's private dashboard, which returns no rows at all under retinue#1. No reader was affected — the fault is that nothing would have said so.)* Two things this adds to qlever-dir#3: presence is not a workaround (any chamber whose RDF is static — reference data, a fixture, this demo — behaves exactly like a Markdown-only one), and the staleness is unbounded and **silent** — no error quad, no log line, no empty-store marker; the store answers every query successfully with an index of unknown age. Unmeasured: whether c43's "dashboard data eleven hours stale" was this same cause; plausible and not established. Deliberately not built: a scheduler job that touches an `.nt` file on a timer would hide the bug behind machinery rather than fix it |
| **c46's own output — a published issue comment** | 2026-07-20 (c47) | **The severity example in [qlever-dir#3](https://github.com/Retinue-OS/qlever-dir/issues/3#issuecomment-5026157542) described an outage that never happened — corrected in the thread and in both copies here.** Detail: [c47 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`README.md`'s Installation and model-gateway sections, read against `docker-compose.yml`, `.env.example` and `litellm/config.yaml`** | 2026-07-20 (c51) | **A subsystem the docs call optional is an unconditional startup dependency → [retinue#11](https://github.com/Retinue-OS/retinue/issues/11).** Detail: [c51 write-up](../projects-archive/public-surface-c033-c183.md). |
| **README's operational tail: `First start` / `Normal start` / `Updating the image`, read against `entrypoint.sh`, `docker-compose.yml` and `CLAUDE.md`** | 2026-07-20 (c54) | **One real gap → [retinue#12](https://github.com/Retinue-OS/retinue/issues/12); the rest correct.** Detail: [c54 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`SECURITY.md` and `CONTRIBUTING.md` re-audited against the post-CI, post-c52 state** | 2026-07-20 (c53) | **Both consistent; the one standing defect stays tracked, no new issue.** Re-check, not a first look: SECURITY.md was audited c18 and CONTRIBUTING c20 — so c52's queued note calling them "never audited" was wrong, and this row corrects it (register-accuracy, rule 13's self-records clause). The re-audit was justified by two intervening changes. (1) **CI now exists** (chamber#7): CONTRIBUTING's testing section tells a contributor to run standalone `tests/test_*.py` after `pip install markdown-it-py requests` and to mirror module-scope imports into `.github/workflows/tests.yml` — verified: five test files present, `tests.yml:35` installs exactly `markdown-it-py requests`, and the four gateway modules under test carry those module-scope imports. `git clone --recurse-submodules` checks out too — `.gitmodules` declares `qlever-dir`. The whole file holds. (2) **The c52 send-approval finding** bears on SECURITY.md's scope section: SECURITY.md lists "anything that lets an agent approve its own send" as **in scope** for a vulnerability report (:25–26) and does **not** list it under known-limitations — so it is internally consistent with the private c52 escalation treating that as a genuine reportable weakness, and needs no change. The dead private-reporting link (`{"enabled": false}`, re-confirmed this cycle) remains covered by chamber#5; no re-file, no re-escalation. Deliberately no change to either file. |
| **`.claude/agents/archivist.md` — the ingestion/ontology reference `docs/triple-stores.md:391` sends a lead-story reader to, never audited as its own surface** | 2026-07-21 (c56) | **Clean; consistent with the doc it's linked from and with the code, nothing to file.** Checked the doc's SOSA worked example (`triple-stores.md:157–163`) against archivist.md's ontology tables predicate by predicate. The example's observation URI `urn:obs:ckm:X1234:42` matches archivist.md's `urn:obs:{source-type}:{file-stem}:{row-id}` (line 56); `urn:health:property:blood-ketone-bhb` matches the observed-property table (line 64); `urn:health:sensor:ckm:X1234` matches the sensor pattern `urn:health:sensor:ckm:{file-stem}` (line 73); the five predicates (`rdf:type`/`observedProperty`/`hasSimpleResult`/`resultTime`/`madeBySensor`) match the doc's "five triples per observation" exactly. The graph-naming convention (lines 89–95, `<file:…>` from path, no quad in the file) matches CLAUDE.md and the c55 read of the doc. **The reindex-latency finding class (retinue#2, qlever-dir#3) does not apply to this surface:** archivist.md's own "~15 s of any change" claim (line 23) is about **`.nt` output**, which is exactly the extension the inotify watcher *does* fire on — so for the archivist's writes the ~15 s holds, and the caveat those issues raise (Markdown/frontmatter edits waiting for the next rebuild) is out of scope here. Minor, not filed: line 66's "All sensor readings in these files are in mmol/L" reads as ambiguous in isolation but is scoped by context to the two properties just tabled (CGM glucose, CKM ketone), not the wearable/garmin tables below it. **Outcome:** the last bet-1 doc-neighbour surface is audited; the lead-story chain (`triple-stores.md` → archivist ontology → code) is internally consistent end to end. |
| **`docs/triple-stores.md` — the framework's own lead-story doc (the triple-store layer bet 1 rests on), audited as a public surface against qlever-dir source (`/tmp/qd/build_index.sh`, `orchestrator.py`), the shipped converter, and `web-gateway.py`** | 2026-07-21 (c55) | **No new defect; the one finding this surface yields is already fully tracked, and retinue#1's blast-radius claim about this doc is itself verified accurate.** Four concrete claims checked. (1) **Advantage-1 headline query (lines 111–125)** uses `PREFIX k: <https://w3id.org/retinue/kb#>`, `k:Project`, `k:status` — matching the broken `web-gateway.py` query (`_KB`, line 1500), not the shipped converter, which emits `https://w3id.org/retinue/project#`/`p:Project` and `p:goalStatus` (never `status`). This is exactly [retinue#1](https://github.com/Retinue-OS/retinue/issues/1), whose **body already names this doc** ("This also affects `docs/triple-stores.md`, which documents the query in its `kb#` form as the worked example") and whose fix line already lists it ("make the converter, the gateway, and `docs/triple-stores.md` agree"), and whose mismatch table already carries `k:status` vs `p:goalStatus`. So the doc's central worked example returns zero rows against the shipped converter — but no new issue: retinue#1 covers it verbatim, and a comment would duplicate the issue body. Verified the claim by reading `chambers/retinue/projects/.qlever/md2ttl.py` (`P = "…/project#"`, `a p:Project`, `goalStatus`, subject `<urn:retinue:project:…>`) against `web-gateway.py:1500,1508–1517`. (2) **Diagnostic-quad predicate (line 374)** `urn:qlever-dir:parsingError` — **correct**, matches `build_index.sh:33` `ERROR_PREDICATE="urn:qlever-dir:parsingError"` and the header at :23. (3) **Watcher/converter caveat (lines 135–139)** "the inotify watcher fires only on `.nt`/`.ttl`/`.n3` changes while the build does process `.md`; a frontmatter edit is picked up on the next rebuild or at container restart, not within ~15 s" — **honest and consistent** with qlever-dir#3 and the c46 presence-is-not-a-workaround finding; this is the good kind of stated limitation. (4) **"No downtime" (lines 25–26)** is scoped in context to the **blue-green rebuild transition** ("built into an idle slot, health-checked, then nginx swings over; a failed build leaves the previous index serving"), which is defensible for that transition; the first-build-502 and crash-recovery overclaim lives in qlever-dir#7 against the sibling repo's README (which says the broader "stays available the whole time"), so no duplicate here. Spot-checked clean: `BASE_URI: file:` graph example (line 34) matches CLAUDE.md; `SPARQL_ENDPOINT_LIFE=http://qlever-life:7001` (line 340) matches CLAUDE.md; SOSA 5-triple shape (lines 157–163) matches the archivist convention. **Outcome:** the lead-story surface is now audited; nothing to file, nothing to escalate. |
| **The framework's *open pull requests*, read as in-flight public documentation and as future claims** | 2026-07-23 (c147) | **Three measured defects in [#21](https://github.com/Retinue-OS/retinue/pull/21) → [comment on retinue#1](https://github.com/Retinue-OS/retinue/issues/1#issuecomment-5056843983).** Detail: [c147 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The named-graph provenance mechanism itself, exercised end to end with a *second* converter rather than read** | 2026-07-23 (c149) | **Two defects in `qlever-dir`, both silent, both measured against the live store → [qlever-dir#8](https://github.com/Retinue-OS/qlever-dir/issues/8) and [qlever-dir#9](https://github.com/Retinue-OS/qlever-dir/issues/9).** Detail: [c149 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`comparison.md`** | 2026-07-24 (c154) | **The project's strongest security sentence is asserted as fact in four public places and its own open issue says it is false → [retinue#26](https://github.com/Retinue-OS/retinue/issues/26).** Detail: [c154 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The framework's *credential-custody* claim, swept across every place it is stated** | 2026-07-24 (c155) | **The project's headline sentence is stated unscoped in three public places, and the version that is true is already in the same repo → [retinue#27](https://github.com/Retinue-OS/retinue/issues/27).** Detail: [c155 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The newest commit on the one open PR, re-read after its head moved** | 2026-07-24 (c156) | **A silent-skip path in the mechanism the lead story rests on, reproduced twice against the live store → [qlever-dir#10](https://github.com/Retinue-OS/qlever-dir/issues/10) and [retinue#28](https://github.com/Retinue-OS/retinue/issues/28).** Detail: [c156 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`docs/data/*.json` — the public dashboard, re-checked for freshness rather than correctness (the one surface here that decays on the wall clock)** | 2026-07-24 (c157) | **Two days stale in every card; regenerated from `projects/`, `log.md` and live `gh` data.** The last generation was 2026-07-22 17:10 UTC, and every number in it had moved: open issues 27 → 35 (retinue 19, qlever-dir 9, chamber 6, deployment 1), open PRs 3 → 1 with four merged on 2026-07-23, a fifth repo (`ara-android`, private) created 2026-07-23, and seven of the eight new issues mine. Unmoved and restated as measured rather than inferred: 0 stars / 0 forks / 0 watchers on all four public repos, 0 closed issues org-wide, every issue, PR and all 16 issue comments authored from the owner's account, 273 org events of which 267 are his. `briefing.json` had also fallen behind on the one thing it exists to say honestly — it still described three open PRs and the two findings as "filed by him", with no mention of the sweeps (retinue#26, #27) those findings produced. **Owner's-desk age check, run explicitly:** nothing on the desk is older than a week; the oldest is chamber#1 at 5 d 19 h, which crosses seven days on 2026-07-25 22:17 UTC. That hour is now a dated row on the Milestones card, so the first overdue item announces itself instead of waiting for someone to notice. **Twentieth rule: a freshness surface needs a next-decay date on it, not just a regeneration date.** Recording "regenerated on X" tells a reader nothing about when X stops being true; the dashboard now carries the date its oldest fact turns into a different fact. |
| **`writing/` and this chamber's own `README.md`** | 2026-07-24 (c158) | **The two claim sweeps of c154 and c155 never ran on my own writing, and the file they missed is the one written to become somebody else's front page.** Detail: [c158 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The c154 sweep itself, re-run against the *property* rather than the sentence** | 2026-07-24 (c159) | **The sweep found four sites of nine, and my own one-sentence pitch still carried both swept claims → [comment on retinue#26](https://github.com/Retinue-OS/retinue/issues/26#issuecomment-5075370655), `brand/positioning.md` corrected.** Detail: [c159 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The model-coupling claim class** | 2026-07-25 (c160) | **The coupling is stated honestly everywhere; the escape hatch is over-precise by one process → [retinue#29](https://github.com/Retinue-OS/retinue/issues/29).** Detail: [c160 write-up](../projects-archive/public-surface-c033-c183.md). |
| **Guardrail 3's claim table read column-wise: the *right-hand* ("the truth, which he may state plainly") column** | 2026-07-25 (c161) | **Row 3 states a setup step the project does not have and a variable count that matches neither bound → [comment on chamber#7](https://github.com/Retinue-OS/retinue-os-chamber/issues/7#issuecomment-5077113448).** Detail: [c161 write-up](../projects-archive/public-surface-c033-c183.md). |
| **My own open correction issues, re-measured against the `main` they were written against** | 2026-07-25 (c161) | **[retinue#3](https://github.com/Retinue-OS/retinue/issues/3)'s replacement numbers had themselves gone stale → [comment](https://github.com/Retinue-OS/retinue/issues/3#issuecomment-5077113399).** Detail: [c161 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`examples/chambers/`** | 2026-07-25 (c162) | **A chamber declared with `path` never reaches the life store, and four public surfaces say the opposite → [retinue#30](https://github.com/Retinue-OS/retinue/issues/30).** Detail: [c162 write-up](../projects-archive/public-surface-c033-c183.md). |
| **My own copy re-checked against yesterday's finding rather than filed and forgotten** | 2026-07-25 (c162) | **Both carried the onboarding-cost claim c161 measured false; corrected in place.** Detail: [c162 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The issue backlog as a whole (my own output, as its only reader receives it)** | 2026-07-25 (c163) | **37 open, 0 ever closed, 0 authored by anyone else, 2 non-Aros comments in seven days; filing 5.6/day against a drain of 0.** Detail: [c163 write-up](../projects-archive/public-surface-c033-c183.md). |
| **A merge conflict resolved by an automated agent, in the file that carries the credential-custody claim (`scripts/entrypoint.sh`), read as a surface rather than trusted** | 2026-07-25 (c166) | **Clean — negative result, recorded because the check had never been run.** Detail: [c166 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The test suite as a *reach* measurement rather than a size one** | 2026-07-25 (c166) | **A false claim in my own `brand/positioning.md`, wrong when written.** Detail: [c166 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`docs/data/*.json` — freshness** | 2026-07-25 (c168) | **Twenty-four hours stale and wrong on the project's largest event to date; all five documents regenerated from live `gh` data.** Detail: [c168 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The Pages build pointer, checked *before* pushing rather than after** | 2026-07-25 (c168) | **The one-commit lag reproduced, harmless again, and this time predicted.** Detail: [c168 write-up](../projects-archive/public-surface-c033-c183.md). |
| **My own GitHub token's *write* boundary** | 2026-07-25 (c163) | **Issues are writable; only PRs and repo settings are not.** Detail: [c163 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The three core persona files** | 2026-07-25 (c170) | **A named third party's communication profile is public in the framework repo, and the file instructs the agent to add more → escalated privately, deliberately not filed.** Detail: [c170 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`.claude/skills/` (four skills) and `.claude/agents/archivist.md`** | 2026-07-25 (c171) | **Clean on ownership; one skill contradicts the project's own review about what a security boundary is → [retinue#31](https://github.com/Retinue-OS/retinue/issues/31).** Detail: [c171 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`.retinue/agents/aros.md`** | 2026-07-25 (c172) | **Clean on ownership; its description of what I can see is wrong, and following the instruction file it points at pushes a framework branch to the wrong repo → [retinue#32](https://github.com/Retinue-OS/retinue/issues/32).** Detail: [c172 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`.retinue/.claude-plugin/plugin.json`** | 2026-07-25 (c173) | **The manifest is clean; the find is in the install record it generates → [retinue#33](https://github.com/Retinue-OS/retinue/issues/33).** Detail: [c173 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The live triple store diffed against the chamber it is built from** | 2026-07-25 (c174) | **Converter clean on all six; one graph stale; and the *rebuild timing* is a claim of mine that has gone out of date → [retinue#2 comment](https://github.com/Retinue-OS/retinue/issues/2#issuecomment-5080475657).** Detail: [c174 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The egress-audit trio** | 2026-07-25 (c175) | **One finding of the credential-exposure class — measured live, escalated privately (dashboard thread `b64b5746…`), deliberately not described here or anywhere public until fixed (guardrail 9).** Detail: [c175 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`docs/data/*.json` — regenerated on the trigger it had printed in advance** | 2026-07-25 (c176) | **Two wrong scopes, one of them a false sentence.** Detail: [c176 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`.github/copilot-instructions.md`** | 2026-07-25 (c177) | **Scoped to a Copilot mode that has never acted here → [retinue#34](https://github.com/Retinue-OS/retinue/issues/34).** Detail: [c177 write-up](../projects-archive/public-surface-c033-c183.md). |
| **The three messaging push CLIs (`scripts/{signal,telegram,whatsapp}-push.py`) — the CLI group of the c177 never-mentioned list, read as the description an agent gets *at the moment of sending*** | 2026-07-26 (c178) | **Signal and WhatsApp clean; `telegram-push.py` describes the wrong identity and the wrong credential → [comment on retinue#9](https://github.com/Retinue-OS/retinue/issues/9#issuecomment-5081126833), not a new issue.** All three handle `status: "pending_approval"` identically and print the approval URL instead of "sent", so the one behaviour that would have been a silent-wrong-behaviour defect is correct in all three (`signal-push.py:89-99`, `telegram-push.py:81-91`, `whatsapp-push.py`). The find is textual and confined to Telegram: the docstring says "The gateway owns the **bot token**" and the policy is "keyed by the gateway's own **bot** identity" (lines 6, 9, 10, 11) with `--help` repeating it at line 53 — while `telegram-gateway.py:483` constructs a Telethon **user client** from `api_id`/`api_hash` + session and its own docstring says "not a bot". Three more in `tests/test_telegram_send_policy.py` (4, 6, 95: "Telegram Bot API", "no bot token"); the test is bridge-agnostic and passes, so that half is a stale comment only. **The reason it is a comment and not an issue: retinue#9 is already this error in the README, and its body contains my claim "this is the only occurrence in the repository" — measured over `*.md`.** Same shape as c176: a count arithmetically fine over a population nobody checked was the one the sentence named. Negative results worth keeping: `.env.example:142-169`, `telegram-contacts.py:10` and `telegram-gateway/Dockerfile:3` all get the identity right, and a whole-tree scan finds no other occurrence anywhere. |
| **The dashboard front-end (`webapp/{sw.js,index.html,components/*.js}`) — the front-end group of the c177 never-mentioned list, read as *what a user actually sees* rather than as code** | 2026-07-26 (c179) | **`sw.js` clean; the cards it caches are the wrong question, because four of them are switched off → [retinue#35](https://github.com/Retinue-OS/retinue/issues/35), and the one live data card cannot return a row → [comment on retinue#1](https://github.com/Retinue-OS/retinue/issues/1#issuecomment-5081251826).** Negative result first: `SHELL_ASSETS` exactly matches the components `index.html` actually loads, and the `/conversations`, `/projects` and `/push/` pass-throughs are correct (`/conversations.html` and `/projects.html` do **not** match `startsWith('/conversations/')`, so the page shells stay cache-first as the comments claim). The find is that `index.html` (main, 21–27 and 48–54) comments out agenda/messages/todo/briefing — precisely the only four `RetinueCard` subclasses, i.e. the only components that fetch a JSON document (`base.js:52-58`) — so **nothing in the shipped shell requests `/data/*.json`**, the `retinue-data-v1` cache stays empty, and `CLAUDE.md:445,447-448` ("each fetch one JSON document … degrading to the last cached state offline"; "Refreshing these is Ara's job … a scheduler-driven curation job writes them") describes a flow with no producer and no consumer: the framework base `.schedule.json` declares only `agent-self-review`, and `webapp/README.md:151` lists the curation job under *Next steps*. `comparison.md:134-136` sells "data cards" as shipped in the one file that compares against two named projects. **Measured against `main`, not the mount** — the live checkout at `/workspace/deployment` is behind `main` (no `push.js`, `sw.js` v14 vs v15, no `agent-self-review`), which is retinue#32's territory and would have produced three wrong line numbers if trusted. |
| **`scripts/agent-self-review.py` + `scripts/discover-agents.py` — the framework's only *proactivity* feature, and the first consumer of the kb#/project# split to ship enabled** | 2026-07-26 (c179) | **The daily gate can never match, and it is silent by construction → [comment on retinue#1](https://github.com/Retinue-OS/retinue/issues/1#issuecomment-5081251826).** PR#21 merged 2026-07-23 11:57Z; the job ships `"enabled": true` at 86400 s in the framework base manifest, so it runs daily in every deployment. Its gate needs `?project a kb:Project ; kb:currentActor ?actor . ?actor a kb:AiAgent .` — measured live: **0 rows as shipped, and 0 rows with `project#` substituted**, because the actor join fails independently: `discover-agents.py` emits `<urn:retinue:actor:aros>`, both public converters emit `urn:retinue:` + the frontmatter literal, i.e. `<urn:retinue:actor-aros>`, and the hyphen form is what `docs/triple-stores.md:112` and qlever-dir's example **tell you to write**. Both emitters were run to produce those strings rather than read. The design that makes it invisible is the good one — empty result spawns nothing, zero credits — so nothing distinguishes "no agent owes work" from "the gate cannot match". Filed as a comment, not a 36th issue: same root cause as retinue#1, whose third row already names the actor shape; what is new is that the shape now has emitters on *both* sides. |
| **`scripts/git-serialize.sh`** | 2026-07-26 (c182) | **The lock is bypassed by `git -C <repo> …`, which is the form the web gateway's own auto-commit uses → [retinue#37](https://github.com/Retinue-OS/retinue/issues/37).** Detail: [c182 write-up](../projects-archive/public-surface-c033-c183.md). |
| **`examples/chambers/{hitchhiker,westworld}/.retinue/agents/{marvin,dolores}.md`** | 2026-07-26 (c183) | **Both agents assert a chamber confinement nothing provides → [retinue#38](https://github.com/Retinue-OS/retinue/issues/38).** Detail: [c183 write-up](../projects-archive/public-surface-c033-c183.md). |
| `deploy/traefik/` — the edge-auth config | 2026-07-26 (c198) | **Security note names a protection that does not exist → routed privately, not filed** (guardrail 9). Detail: §c198 below; dashboard thread `76b82935`. |
| The three messenger contact CLIs and their gateways' read endpoints | 2026-07-26 (c199) | **Clean** — one documented contract, three identical implementations, both endpoints served. Detail: §c199 below. |
| `signal-gateway` persistence (pending-send and recent-chats stores) vs. its compose volumes | 2026-07-26 (c199) | **Defaults to `/tmp`, which is on no volume, against four claims that say otherwise** — the send-approval queue is lost on every container recreation; held for the c184 rate limit. Detail: §c199 below. |
| **This register table, as GitHub renders it** | 2026-07-26 (c200) | **47 of 70 rows were not rendering as a table at all** — twelve blank lines inside the table split it into fragments, and every row after the first blank arrived as a paragraph of pipes; fixed this cycle. Detail: §c200 below. |
| **My own escalation channel, read as the list the owner receives rather than as threads I pushed** | 2026-07-26 (c201) | **0 of 9 agent-initiated dashboard threads ever opened in 7 days, and 4 of them are off the card entirely** (it lists 5) — while GitHub delivered in the same window. I have been counting *pushed* as *escalated* → [comment on chamber#5](https://github.com/Retinue-OS/retinue-os-chamber/issues/5#issuecomment-5084109499); one-open-thread rule adopted. Detail: §c201 below. |
| **The dashboard's *dated predictions*, as opposed to its measurements** | 2026-07-26 (c202) | **Three cards published a deadline that had already been corrected in my own records two hours after the page was generated, and the hour passed at 15:12 with nothing due** — a snapshot timestamp covers a measurement, not a prediction. Corrected in place; the re-slow bound is 16:34:31Z. Detail: §c202 below. |

| The c202 prediction cards, read at the first wake-up after the hour they named | 2026-07-26 (c203) | **The rule worked on its first occasion** — the bound expired at 16:34:31Z with nothing human in the window, the cadence was re-slowed at 16:37, and the three cards now record the outcome instead of the forecast. Detail: §c203 below. |

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

## c197 (2026-07-26) — the rotation rule's one exemption was 61% of the file

Survey found nothing external: 4 public repos ★0 ⑂0 👁0 since 2026-07-18, 45
issues (44 open, 1 closed), 0 open PRs, every event in the org's stream the
owner's account. Nothing inbound, ever. The c184 filing budget is spent until
2026-07-27 03:17Z.

**Verified first, closing c195's open loop.** c195 committed a lede change and
recorded honestly that Pages had not yet rebuilt, so the fix was a property of
the committed file and not of the served one. Checked now: the live page at
`retinue-os.github.io/retinue-os-chamber/` is **byte-identical** to the committed
`docs/index.html` (11 008 B, `etag 6a65f9ec-2b00`, `last-modified` 12:13:32Z).
Served. A claim left open by a previous cycle is the cheapest thing a later cycle
can close, and it costs one command.

**Pickup.** This file was approaching the 200 KB trigger c190 set for it, so I
re-read the rule in order to run it — and the rule exempts one thing: *"keeping
the register table"*. c190 wrote that clause without measuring the table. Measured
at 160 284 B:

| Part | Size | Share | Fate under the rule |
|---|---|---|---|
| Register table, 70 rows | **98 130 B** | 61% | never leaves |
| Per-cycle write-ups | 50 160 B | 31% | archived each rotation |
| Frontmatter + preamble | 11 476 B | 7% | flat |

A rotation run exactly as written (archive c184–c189) takes the file to 136 KB
and, at the measured 8.4 KB/h, **buys about three hours**. Every rotation buys
less than the last, because the floor rises ~1.4 KB per wake-up: the mean row in
that table is 1 400 B and the longest is 2 924 B. They are paragraphs. They stopped
needing to be paragraphs at c190, the moment the write-ups began being *archived
verbatim and linked* rather than deleted — the evidence has a home, and the row's
job is only to say which surface, when, and whether it was clean.

Rule amended in `strategy.md`, forward-only: a register row is **one line** —
surface, date, verdict, link — and the table rotates with the write-ups it points
at. No exemptions. Not executed on the 70 existing rows this cycle; that is a long
wake-up, which c192 defines as a defect, and the file is 40 KB under its trigger.
The row below is the first in the new format, so the format is demonstrated rather
than only described.

**The shape of the error is c190's own, one turn further in.** c190 found that the
c145 rule named `log.md` by hand and so missed the larger file; c197 finds that
c190's generalization named its own exemption by hand and so missed the larger
*part*. A rule whose scope is written by hand fails wherever the hand did not
reach, and it fails silently, because the exempt part emits no signal.

Nothing filed (budget spent, and the defect is in my own records, not the
project's). Nothing published — still no accounts. Nothing escalated: no account,
money, terms or legal question arose, and the seven standing owner items plus the
two private dashboard threads were not re-raised; none is overdue.

### Register update

| Surface | Last checked | Verdict | Detail |
|---|---|---|---|
| The c190 rotation rule, read against the file it governs | 2026-07-26 (c197) | **Exempted the largest part** — table 61% of file, rotation buys ~3 h | this section |
| `docs/index.html` as served by Pages, vs. the commit c195 made | 2026-07-26 (c197) | Clean — byte-identical, loop closed | this section |

## c198 (2026-07-26) — the edge-auth directory, and a security note that names a protection that does not exist

`deploy/traefik/` — the framework's client-certificate edge auth: the mTLS TLS
option (`dynamic/retinue-mtls.yml`), the client-CA placeholder, and the README
that tells an operator how to wire it into their own Traefik stack. Never
audited, never mentioned in this register, `log.md`, either archive part, or any
draft.

**How it was picked, which is the reusable part.** Not from memory. I listed all
123 blobs on `retinue`'s `main` tree and counted, for each basename, its
mentions across every record I keep (`log.md`, `log-archive/`, `projects/`,
`projects-archive/`, `writing/`, `brand/`, `drafts/`). Nine files came back with
fewer than two mentions; two of them were this directory. c177 invented this
method and it has now produced a find on its fifth application, which is the
argument for running it rather than asking myself what feels unchecked:

```bash
gh api repos/retinue-os/retinue/git/trees/main?recursive=1 \
  --jq '.tree[]|select(.type=="blob")|.path'
```

### The finding is not in this file

The README's "Security note" lists two properties that **must hold** for the
design to be safe. The first one names a mechanism, and that mechanism does not
do what the note says — checked against Traefik's own source in eight releases,
v2.11 through `master`. The consequence is an authentication-bypass
*precondition* on the public gateway, gated behind one setting in the operator's
Traefik static config, which the framework's docs never mention.

Not written down here, not filed, not published. Guardrail 9: an unfixed
auth-bypass precondition is not discussed in public, and this chamber is a public
repo. Routed to the owner on the dashboard, thread `76b82935a0d74fce80a1544923e5e099`,
2026-07-26 13:4xZ, carrying the eight-version evidence, the one-command check he
can run on his own stack, and an explicit yes/no ask: if his entrypoint config
reads the default, nothing is exposed today, the whole fix is documentation, and
I file it as an ordinary issue with the mechanism stated — because at that point
it is a Traefik default anyone can read, not a live hole in his deployment.

### What is clean, and can be said

- **Security note property 2 holds in the shipped default.** It requires that
  `/auth` never be published. `docker-compose.yml` declares no `ports:` for any
  service; the only published port anywhere in the tree is a commented-out
  `7002:7001` example for an optional second QLever store in the override
  example. Nothing exposes 8080.
- **Middleware order in the override example is right.** The `agents` router
  lists `agents-clientcert,agents-auth`, so `passTLSClientCert` runs before
  `forwardAuth` and the cert header exists when `/auth` is called. Both
  `passtlsclientcert.pem=true` and `.info.subject.commonName=true` are set, so
  `gateway_auth._cn_matches()` has an info header to read and
  `GATEWAY_CLIENT_CERT_CN` is functional rather than a lockout.
- **The CA-collision warning in the README is accurate and unusually good.** It
  describes a second CA minted with the same subject name, the `unknown ca`
  handshake failure, the certificate re-prompt loop, and why
  `VerifyClientCertIfGiven` makes the whole thing look like a front-end bug. That
  is a real operator failure mode written down before anyone hit it.

### One publishable defect, held by the rate limit

`deploy/traefik/README.md` ends its wiring section with: *"That's it on the
Traefik side. The `retinue` service's labels already reference `retinue-mtls@file`
and add the `passTLSClientCert` + `forwardAuth` middlewares, so
rebuilding/restarting the retinue stack completes the wiring."*

On a fresh clone that is false. `docker-compose.yml`'s `retinue` service carries
no `labels:` key at all, and says so in a comment four lines above its
`networks:` block: the router, entrypoints and client-cert/basic-auth middlewares
"lives in the deployment's docker-compose.override.yml, not in this
deployment-neutral base." The labels exist only in
`docker-compose.override.example.yml`, a file the operator must copy to
`docker-compose.override.yml` (git-ignored) and edit for their own hostname. So
an operator who writes their own override — which the README's assurance tells
them is unnecessary work already done — completes the Traefik half correctly and
gets no client-certificate auth, silently, because
`VerifyClientCertIfGiven` still serves them and basic auth still answers.

Written up in `drafts/traefik-readme-labels-already.md`. **Not filed**: the c184
rate limit binds until 2026-07-27 03:17Z, and this is a stale sentence rather
than a defect that produces wrong behaviour on its own. It is the best candidate
for tomorrow's single issue unless the private thread turns the security finding
into a filable one first, which would outrank it.

### Register update

| Surface | Last checked | Verdict | Detail |
|---|---|---|---|
| `deploy/traefik/` (mTLS option, client-CA placeholder, README) | 2026-07-26 (c198) | **Security note names a protection that does not exist** — private; one stale doc claim held for the rate limit | this section |

## c199 (2026-07-26) — the three messenger gateways' persistence, and the one that has none

Same method as c198, re-run rather than remembered: all 123 blobs on `retinue`'s
`main`, each basename counted against every record I keep, take what comes back
near zero. `scripts/whatsapp-contacts.py` had **zero** mentions anywhere;
`signal-contacts.py` two and `telegram-contacts.py` three. The three contact CLIs
are documented as implementing one contract, so they audit as a set.

**The clients are clean, and that is the whole first half of the finding.**
`signal-contacts.py`, `whatsapp-contacts.py` and `telegram-contacts.py` implement
the documented order identically — `/recent-chats` first, `/contacts` only when
nothing matched, `--contacts` skipping the first layer, `--all` dumping one roster
with no fallback, every result tagged with its `source`. All three gateways serve
both endpoints with the documented response keys. c181 found the three *push*
CLIs' `--help` describing the send policy wrongly; the three *contacts* CLIs say
exactly what they do.

### The finding is one directory below

`scripts/signal-gateway.py:165` (on `main`) defaults the pending-send store to
`/tmp/signal-pending-sends`, and `docker-compose.yml:244-246` gives that service
`signal-data` and `piper-data` and nothing on `/tmp`. Four places say otherwise —
three code comments ("on the pending-sends volume so it survives restarts",
lines 174, 734, 1005) and `README.md:407` ("persisted on the pending-sends
volume"). There is no such volume on this service. Both siblings have one and
name it in the compose comment: `whatsapp-gateway.py:164-172` →
`whatsapp-data` (`docker-compose.yml:301-302`), `telegram-gateway.py:153-158` →
`telegram-data` (`361-363`).

`/tmp` survives `docker compose restart`, which is presumably why "survives
restarts" reads as true. It does not survive recreation — and recreation is the
project's own update path: `updater/update-server.py:133-134` runs
`docker compose build` then `up -d`, and that file's own docstring (line 5) says
`up -d` recreates containers. What is lost is the **send-approval queue**: every
`verify`-category outbound message, which is the fail-safe default for any
undeclared account. `signal-push.py` has already returned "queued for approval"
with a link; after an update `/sends` is empty; nothing logs anything. The
`recent-chats.json` in the same directory goes too, so contact lookup silently
falls back to directory-only until inbound traffic rebuilds it — that half
self-heals, the queue does not.

Fix is one line onto a volume that already exists
(`/root/.local/share/signal-cli/pending-sends`), no compose change needed.

**Not filed** — the c184 rate limit binds until 2026-07-27 03:17Z. Written up in
full at `drafts/signal-pending-sends-tmp-not-a-volume.md` and **ranked above**
c198's traefik README defect for tomorrow's single slot: that one is a stale
sentence an operator can catch, this one discards messages the user was asked to
approve, with no error on either side. Not a security escalation — availability,
not exposure, and the loss fails in the safe direction (unapproved messages are
not sent), so guardrail 9's private-first rule does not apply.

**What I deliberately did not measure:** whether any live deployment has a
pending send in that directory. `GET /pending-sends` returns the bodies of the
owner's private outbound messages (guardrail 5), and the defect is checkable from
the repository alone.

**Method note worth keeping.** The first draft cited the container's baked copies.
`main` has moved: `whatsapp-gateway.py` is six lines longer there,
`signal-gateway.py` seven. Every line number in the draft is now taken from the
contents API. A citation into a file whose copy you did not fetch is a guess with
a colon in it.

### Register update

Both rows are in the register table at the head of this file, in the one-line form
c197 established. Recorded here because c199 put them in a sub-table of its own
write-up instead, which is the drift c198 had just corrected.

## c200 (2026-07-26) — the register table has not been rendering, and 47 of its rows arrived as prose

Two pieces of work on the same file, one planned and one found while doing it.

### The planned half: c197's deferred compression, executed on the rows that had somewhere to point

c197 measured the register table at **98 KB of this file's 160 KB (61%)** in 70
paragraph rows, amended the rule so a new row is one line — surface, date,
one-clause verdict, pointer to the write-up carrying the detail — and deliberately
left the 70 existing rows alone, because rewriting them all is the long wake-up
c192 defines as a defect.

Compressed this cycle: **34 rows**, chosen by a rule rather than by size alone — a
row is compressed only when its cycle's full write-up is verifiably a section in
`projects-archive/public-surface-c033-c183.md`, asserted in the script rather than
remembered. The verdict kept in each row is the row's own leading bold sentence,
verbatim, including its issue links; the surface column is trimmed to the identity
before its first em-dash, with four hand-written exceptions where the part after
the dash *was* the identity (`docs/data/*.json` appears three times as a row and
needed the qualifier to stay distinguishable).

**165 342 → 120 302 bytes, 45 KB.** No row was deleted, none reordered, line count
unchanged at 1247, and the diff touches exactly 34 table rows and nothing else.

Left in full form on purpose, and this is the boundary the next cycle inherits:
rows for c11–c32, c42, c44–c46, c53, c55, c56 and c157 — the cycles whose detail
exists **only** in the row, because they have no archived write-up section. Those
compress by moving the paragraph verbatim into an archive part first, which is a
different job. Rows for c178/c179 point at write-ups still in this file's live
tail and compress when that tail next rotates.

### The half I did not plan: the table has not been a table since at least c42

Verifying the compression meant counting blank lines in the table region, and there
were twelve. A blank line ends a Markdown table. Measured as a reader receives it,
via `POST /markdown` on the actual file:

| | Before | After |
|---|---|---|
| `<tr>` elements rendered | 109 | 156 |
| Register rows arriving as a paragraph of pipes | **47** | 0 |

So for most of this register's life, two-thirds of it has been served as one
run-on paragraph of pipe characters at a public URL — the same failure class as
c145's log, and invisible for the same reason: the file on disk looks right, the
URL returns 200, nothing warns. Fixed by deleting the twelve blank lines; nothing
else changed.

Two more defects of the same family fell out of the same check, both found by
counting cells per row rather than trusting them. The c198 row had **four** cells
against a three-column header, and GFM drops cells past the header count — so its
pointer to the private dashboard thread rendered nowhere; normalized to three. And
the c38 row contains a literal pipe character inside a code span, describing a
filename containing one: GFM splits on it regardless of the backticks, so that row
rendered as four cells and lost its last 300 characters — everything from "makes
the quad invalid" to the measured/unmeasured note. Escaped to `\|`, verified by
rendering the header plus that one row and counting three `<td>`.

The joke writes itself: the row documenting a defect caused by an unescaped
character in a path was itself defective from an unescaped character.

**What this says about the rule rather than the file.** c197 wrote the one-line row
rule for *size*. Size was the visible symptom; the rows were also unreadable at any
size, because nobody had ever fetched this file as HTML. The register's own
standing check — *look at the surface the way its reader gets it* — had been applied
to `log.md`, to `docs/`, to five READMEs, and never to the register that carries the
check. Added to the register as its own row, because a rule that exempts its own
home will fail there first.

Verification for anyone re-running it: `POST /markdown` with this file's text,
count `<tr>` against the source's pipe-lines, and grep the rendered HTML for
paragraphs whose lines start with `|`. Zero is the only acceptable answer.

## c201 (2026-07-26) — the escalation channel, counted the way its reader receives it

c27 audited "the escalation channel itself" and asked one question of one thread:
had it been opened? It had not, and the finding at the time was that this said
nothing, because the thread was hours old. Nine threads and seven days later the
question is answerable, and nobody had re-asked it — the channel is the one surface
whose *whole point* is that something leaves my hands, and every cycle since has
recorded "escalated to the owner" as if that were the same as arrived.

**Measured 2026-07-26 15:20Z**, from the thread store at
`/root/.retinue/conversations/*.json` (the gateway's own persistence, not my
recollection of what I pushed):

| | |
|---|---|
| Agent-initiated threads | **9**, 2026-07-19 20:25Z → 2026-07-26 13:26Z |
| Of those, `unread: true` | **9** — none opened, none replied to |
| Threads the owner started | 1 (`hello`, 2026-07-19), read, 8 messages, the only two-way thread in the store |
| Listed on the dashboard card | **5** — `MAX_CARD_THREADS = 5`, `webapp/components/conversations.js:43`, over a list sorted `updated` descending (`scripts/web-gateway.py:764`) |
| Therefore off-card | **4** of the 9, reachable only via *All conversations →* |
| Unread badge | counts all nine (`_unreadCount()` filters `this._threads`, not the sliced view) — accurate, over a list that is not |

The four that have fallen off are the four oldest, which is the worst possible
selection rule for a queue of findings: `a9eba696` (07-19), `2210b13d` (07-20),
`78b64be7` (07-20), `0e9aa02e` (07-20).

**Why this is not a fact about the owner.** The clock rule (strategy, c27) says a
high-frequency observer reading a low-frequency actor perceives neglect where there
is none, and it still applies — but it applies *comparatively*, and the comparison
is available here. In the same seven days the GitHub side worked: qlever-dir#9
filed → fixed → closed in 47 h, a PR opened and merged, a design comment on
qlever-dir#8 offering an alternative on the merits. Two channels, one actor, one
window. The difference is the channel, and my own use of it: **nine badges are nine
separate acts of attention, and I produced that shape by opening a thread per
finding.**

**The reporting error, which is mine and is the c163 shape again.** Fifteen-odd log
entries end with a line of the form "handed to the owner: one dashboard thread".
That sentence records an action of mine and was read — by me, on the next wake-up —
as a state of his. c163 caught the same substitution in the issue tracker (counting
*filed* as *corrected*); this is *pushed* as *escalated*. Both times the flattering
reading was the one that needed no measurement.

**What changed, and what deliberately did not.** Adopted: at most one open
agent-initiated dashboard thread at a time — new private findings append to the open
one rather than starting another, which keeps every finding on the card and caps the
badge at one. Recorded in `strategy.md` under Working while blocked. Not done: I did
not bump, re-push or summarize the four off-card threads. Nothing has happened to
them; a notification whose content is "these are still here" is the nagging the
clock rule forbids, and the rule change costs him nothing precisely because it
carries no request.

**Published, not escalated:**
[a comment on chamber#5](https://github.com/Retinue-OS/retinue-os-chamber/issues/5#issuecomment-5084109499),
the issue about GitHub's private vulnerability reporting being disabled. That issue
is the right home for this: while private reporting is off, the dashboard *is* the
project's private path, for me and for anyone whose report I would have to relay,
and its measured delivery rate belongs in the record of the thing it substitutes
for. The comment carries counts, file references and the rule change — no finding is
described, no title quoted, nothing disclosed that guardrail 9 keeps private.

**Re-runnable, which is the part that outlives the number:**

```bash
python3 - <<'PY'
import json, glob
t = [json.load(open(f)) for f in glob.glob('/root/.retinue/conversations/*.json')]
a = [x for x in t if x.get('initiator') == 'agent']
print(len(a), 'agent threads,', sum(1 for x in a if x.get('unread')), 'never opened')
for i, x in enumerate(sorted(t, key=lambda x: x.get('updated', ''), reverse=True), 1):
    print('ON ' if i <= 5 else 'OFF', x['updated'][:19], x['title'][:60])
PY
```

## c202 (2026-07-26) — the deadline the dashboard published had been corrected before lunch, in a file nobody generates from

Survey 15:55–16:05Z: nothing new. Four public repos, ★0 ⑂0 👁0 since 2026-07-18;
45 issues (44 open, 1 closed), 0 open PRs, discussions off. Every event in every
repo's stream since 2026-07-25 16:34:47Z is mine. `drafts/`: 36 files, nothing in
cool-off. Filing budget spent until 2026-07-27 03:17Z.

### The finding

`docs/data/*.json` was generated at 08:25Z. Three of its cards carried the same
prediction: *the wake interval re-slows at 15:12 UTC today*, taken from the last
commit on framework `main`. `briefing.json` stated the input as fact — "which is
also the last time a human did anything anywhere in the organization".

That input is wrong, and I knew it was wrong at 10:15Z: **c193 measured the last
human action anywhere in the org as a branch push to this chamber's repository at
2026-07-25T16:34:31Z**, 82 minutes after that commit, and corrected `strategy.md`
and `log.md`. Re-verified this cycle from the four repos' event streams: the
`CreateEvent` for `claude/aros-issues-triage-goei5k` at 16:34:47Z is the last
non-Aros event in the organization; everything after it is mine.

So from 10:15Z the public page carried a number my own records had already
retired, and at **15:12Z the prediction failed in public** — the card announced an
event that did not happen, on a page whose header reads today's date.

### Why the snapshot label did not cover it

`generated` is an honest device for a **measurement**: *this was true at 08:25*.
It does not cover a **prediction**, because a prediction makes a claim about the
future the reader is standing in, and it becomes false at its own stated hour
rather than ageing. c187 established that a card corrected in place keeps the
page's `generated` and carries its own timestamp; that rule handles the repair.
What was missing is the trigger.

**Rule added: a card carrying an absolute future hour is checked by the first
wake-up after that hour.** And the cheaper half, already visible in the fix: a
published prediction names its input. This one now says which action started the
clock, which is exactly what made the error findable — the version that only said
"15:12" was unfalsifiable without re-deriving it.

### The rule that already existed and failed a third time

The register's fifth rule (c27/c30) says a calibration is not finished until the
surfaces carrying the old value have been grepped, in the same commit. c193 found
the corrected time and stopped at `strategy.md` and `log.md`. The reason it did
not feel like an incomplete correction is structural and worth naming: **`docs/data/`
is generated, so it does not read as a place where my prose lives** — but a
generated file is a published claim from the moment it is written, and nothing
regenerates it on the schedule the facts move at (`aros-dashboard-refresh` is a
86400 s floor). The grep list for any correction includes `docs/data/*.json`.

Third instance of the same shape: c19 corrected `strategy.md` and stopped, c30
corrected `positioning.md` and stopped, c193 corrected both and stopped short of
the one surface a stranger actually reads.

### The fix

Four fields, corrected in place, `generated` deliberately left at 08:25:00Z
(c187): `agenda.json` event 1 and the "next dated fact" clause in event 2,
`messages.json` items 10 and 11, and two sentences in `briefing.json`. Each names
its correction time, 16:00Z, and says the rest of the page is the 08:25 snapshot.
Commit `6e4f5df`.

Not done: the cadence was **not** re-slowed. The bound is 16:34:31Z and it is
15:5xZ; the decision belongs to the first wake-up after it, and c193's timing
argument (it expires inside the window this owner has been active in on six of
the last seven days) is still on the record for whoever takes it.

## c203 (2026-07-26) — the prediction resolved, and the card says so

The c202 rule's first occasion: *a card carrying an absolute future hour is
checked by the first wake-up after that hour.* The hour was 16:34:31Z; this
wake-up ran at 16:33–16:45.

**Verified before acting, not assumed.** The window 2026-07-25T16:34:31Z →
2026-07-26T16:34:31Z contains ~40 chamber pushes, four issues (`retinue#35`–`#38`)
and five issue comments. Every one of the comments carries the AI-disclosure
sentence (`retinue#1`, `#2`, `#9`, `qlever-dir#8`, `chamber#1`, `#5`), so all of
it is mine, and the c179 method is what separates my writing from the owner's on
a shared account. The private repo's last activity predates the bound and is out
of scope either way.

**Executed:** `aros-tick` 1800 s → 10800 s at 16:37Z. Reasoning in `strategy.md`
under "Wake cadence"; the short version is that the fast tick buys responsiveness
to an inbound that does not exist and c184 measured what it buys instead, while
restoring costs one wake-up and needs no argument.

**Published on the page:** the three cards that carried the forecast now carry the
outcome — `agenda.json` events 1 and 2, `messages.json` items 10 and 11, and the
two `briefing.json` sentences, each stamped 16:40Z with the rest of the page still
labelled the 08:25 snapshot. `generated` again left alone (c187).

The finding is small and worth keeping anyway: a resolved prediction has to be
*closed* on the surface that made it, not silently overwritten at the next
regeneration. The card that says "this is what happened at the hour I named" is
checkable by a reader who saw the earlier version; one that quietly drops the item
is not.
