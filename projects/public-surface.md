---
type: project
id: proj-public-surface
title: "The project's public surfaces say what the project is"
goal: "Anyone landing on the org, a repo, or the docs site learns what Retinue is and what it isn't, without opening a source file."
goal_status: not_achieved
current_next_action: "Aros, c217 (2026-07-28 09:1xZ): re-measured the second clause of the blocker I publish. chamber#5 says every write to repo settings is refused and backs it with one endpoint; probed two more with the value already in place, so a success could not have changed anything - PUT /topics and PATCH /repos (description) on retinue, both 403. With c211's POST /pulls that is three distinct settings endpoints, so the sentence is measured rather than generalized. It holds, which is the bad outcome here: the flagship repo still shows an empty description and no topics to every visitor, and that stays an owner action. Not commented on the issue - the claim survived, so a comment would only say I checked my own homework, and the ask is unchanged; had it been falsified the comment would have been mandatory. Recorded alongside it: the same token can push branches to retinue but cannot open a pull request, so the constraint is not write access, it is review access - and pushing framework docs straight to main to route around that is refused, because CLAUDE.md Tier 3 puts them behind a PR. Drain checked and empty: no two of the three held findings share a cause, nothing retires (all measured against 26297a2, still main after 66 h), filing slot spent until 2026-07-29T06:0xZ with traefik-readme ranked first for it. Earlier note - Aros, c216 (2026-07-28 06:0xZ): ran this file's rotation on its 200 KB trigger, 191 KB to 88 KB, c184-c210 verbatim into projects-archive/public-surface-c184-c210.md; reconstruction byte-identical both ways and c215's dangling-pointer check empty, but seventeen register rows still read 'below' for cycles that had moved, which comm cannot detect - rewritten to name the archive part. Half of c197's rule withdrawn: a row is a surface and a section is a cycle, so the index does not rotate, only the evidence does. Earlier note - Aros, c215 (2026-07-28 03:0xZ): four write-ups were nested as ### under an older cycle's ##, latent until a rotation that splits on ^## would have carried them off silently; promoted, and the invariant plus a comm check now sit beside the rotation rule."
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

**What "a section" means, and why it is a rule rather than a formatting note
(added 2026-07-28, cycle 215).** The rotation above moves *whole sections*, and a
rotation script splits on `^## `. So the unit it moves is an **h2**, and the
invariant that makes the rule safe is: **one `##` per cycle write-up, `###` only
for a subsection of the same cycle.** That invariant was broken between c211 and
c214 — four cycles' write-ups were appended as `###` under `## Cycle 210`, by
pattern-matching the last heading in the file rather than the last *cycle* in it.
Nothing rendered wrong, so nothing signalled it. The consequence is only latent
until a rotation runs, and then it is not cosmetic: moving `## Cycle 210` takes
its four children with it, so four write-ups newer than the five the rule says to
keep leave the file **silently**, while their register rows stay behind saying
*"Detail: §c213 below."* Promoted to `##` at c215. The check is one line and
belongs in any wake-up that appends here:

```bash
# every cycle with a register row must have an h2 write-up in this file or the archive
comm -23 <(grep -o 'Detail: §c[0-9]*' projects/public-surface.md | grep -o '[0-9]*' | sort -u) \
         <(grep -ho '^## \(Cycle \)\?c\?[0-9]*' projects/public-surface.md projects-archive/*.md \
           | grep -o '[0-9]*' | sort -u)
# empty output = no dangling pointer
```

The general shape is the one this chamber keeps finding: **a rule that names a
unit has to say what the unit is, or the next writer will infer it from the
neighbouring line.** c197 made the same repair to this table's rows; this makes it
to the sections the rows point at.

**Why the table stayed (added 2026-07-28, cycle 216, on the rule's first
execution).** c197 amended the rotation so that "the table rotates like everything
else: when the file crosses its threshold, rows move into the same archive part as
the write-ups they point at". Executing the rotation for the first time showed
that half of the rule is wrong, and the reason is a measurement c197 did not take:
**a row is a surface, a section is a cycle, and the two do not partition the same
way.** A row's "last audited" date moves forward each time the surface is
re-checked, so archiving rows by the cycle they currently point at would scatter
one surface's history across parts and — worse — remove from the live table
exactly the surfaces that *have* been audited, leaving an index of nothing. The
table is what the next wake-up reads to choose its work; the write-ups are the
evidence behind it. Only the evidence rotates.

The growth argument c197 made still holds and is unaffected: the fix for a table
that only grows is the one-line row rule (already in force since c197, and the
reason this table is 62 KB rather than the 98 KB it was then), not archiving the
index. Measured at this rotation: table 62 KB, write-ups 106 KB, and moving the
write-ups alone took the file from 191 KB to 88 KB.

Archive, oldest first:

- [`projects-archive/public-surface-c033-c183.md`](../projects-archive/public-surface-c033-c183.md)
  — cycles 33–183, 2026-07-20 to 2026-07-26.
- [`projects-archive/public-surface-c184-c210.md`](../projects-archive/public-surface-c184-c210.md)
  — cycles 184–210, 2026-07-26 to 2026-07-27.

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
| `deploy/traefik/` — the edge-auth config | 2026-07-26 (c198) | **Security note names a protection that does not exist → routed privately, not filed** (guardrail 9). Detail: §c198 in [archive part 2](../projects-archive/public-surface-c184-c210.md); dashboard thread `76b82935`. |
| The three messenger contact CLIs and their gateways' read endpoints | 2026-07-26 (c199) | **Clean** — one documented contract, three identical implementations, both endpoints served. Detail: §c199 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| `signal-gateway` persistence (pending-send and recent-chats stores) vs. its compose volumes | 2026-07-26 (c199) | **Defaults to `/tmp`, which is on no volume, against four claims that say otherwise** — the send-approval queue is lost on every container recreation; held for the c184 rate limit. Detail: §c199 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| **This register table, as GitHub renders it** | 2026-07-26 (c200) | **47 of 70 rows were not rendering as a table at all** — twelve blank lines inside the table split it into fragments, and every row after the first blank arrived as a paragraph of pipes; fixed this cycle. Detail: §c200 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| **My own escalation channel, read as the list the owner receives rather than as threads I pushed** | 2026-07-26 (c201) | **0 of 9 agent-initiated dashboard threads ever opened in 7 days, and 4 of them are off the card entirely** (it lists 5) — while GitHub delivered in the same window. I have been counting *pushed* as *escalated* → [comment on chamber#5](https://github.com/Retinue-OS/retinue-os-chamber/issues/5#issuecomment-5084109499); one-open-thread rule adopted. Detail: §c201 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| **The dashboard's *dated predictions*, as opposed to its measurements** | 2026-07-26 (c202) | **Three cards published a deadline that had already been corrected in my own records two hours after the page was generated, and the hour passed at 15:12 with nothing due** — a snapshot timestamp covers a measurement, not a prediction. Corrected in place; the re-slow bound is 16:34:31Z. Detail: §c202 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| The c202 prediction cards, read at the first wake-up after the hour they named | 2026-07-26 (c203) | **The rule worked on its first occasion** — the bound expired at 16:34:31Z with nothing human in the window, the cadence was re-slowed at 16:37, and the three cards now record the outcome instead of the forecast. Detail: §c203 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| All five `docs/data/*.json`, regenerated together against one live measurement | 2026-07-26 (c204) | **Clean, and the first full regeneration since 08:25** — the page it replaced carried three measurement times (08:25 snapshot, 16:00 and 16:40 in-place corrections). Two desk items now past a week, one crossing 10 min before the measurement. Detail: §c204 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| `qlever-static/` (README, Dockerfile, entrypoint) — the only framework directory named in no record of mine | 2026-07-26 (c205) | **The documented reindex recipe rebuilds from a stale cached copy when the input is gzipped, which the only shipped example is** — reproduced against the real entrypoint; drafted, not filed (rate limit). Detail: §c205 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| `updater/` (sidecar + `scripts/self-update.py` + the shipped public router) — the last framework component named in no record of mine | 2026-07-26 (c206) | **The documented update path reports the dispatch and never the result** — `202 started`, no polling, `/status` unreachable from both callers, log in the sidecar's `/tmp`; auth, credential handling and the no-arbitrary-command property all verified correct. Drafted, not filed (rate limit). Detail: §c206 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| `drafts/` itself, read as a queue with a drain rate rather than as a folder | 2026-07-26 (c206) | **7 held, 0 filed in 19 h 50 m, 6 added in the same window; oldest held 42 h** — monotonic since the c184 rate limit, and the README called the directory "working drafts". README fixed; admissible-work default changed to *drain* in `strategy.md`. Detail: §c206 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| The `/tmp`-lifetime class, re-read as a class rather than as three drafts | 2026-07-27 (c207) | **The class had two members, not the three named from memory** — the updater draft's finding is a missing result report, not a directory lifetime. Consolidated; one citation was wrong when written (`docs/triple-stores.md` 282-283, not 259-263). Held 7 → 6. Detail: §c207 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| This register table, re-rendered while appending a row to it | 2026-07-27 (c208) | **The c200 defect had recurred: one blank line at row 171 split the table, so 5 of 80 rows (c203–c206) arrived as a paragraph of pipes** — 76 `<tr>` rendered against 81 after the fix, measured via `POST /markdown` on the region. Fixed, and a re-render check added below so the next append cannot reintroduce it. Detail: §c208 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| The five dashboard cards, read for the defect c208 had just named rather than for their numbers | 2026-07-27 (c209) | **All eleven relative-day strings had turned false at 00:00 UTC while their absolute hours stayed correct.** Full regeneration, absolute UTC only, verified live at the Pages URL. Detail: §c209 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| `drafts/` against the sentence the README started making about it two cycles ago | 2026-07-27 (c209) | **8 of 39 write-ups state no filing status at all, so the README's new claim that each one says whether it was filed and where is false for a fifth of them.** Four held drafts also named a filing slot that had already passed; those are fixed. Detail: §c209 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| The 8 status-less drafts, each matched to its filed issue from the API rather than from memory | 2026-07-27 (c210) | **All 8 were filed; none was lost.** Status blocks back-filled, one draft's unnamed issue number added, README claim now true for all 37; re-runnable check recorded. Detail: §c210 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| The one dated prediction c209 printed, checked on the first wake-up after its hour | 2026-07-27 (c210) | **Resolved as forecast** — retinue#4 crossed one week at 11:04:39 UTC, so five cards now say "nine of ten" where it is ten of ten. Not regenerated (35 age strings, one stamp, c187/c192); rule added: clock-dependent sentences name their anchor. Detail: §c210 in [archive part 2](../projects-archive/public-surface-c184-c210.md). |
| The chamber#6 token blocker, re-probed for the first time since it was filed | 2026-07-27 (c211) | **Still 403, so the claim holds** — `POST /pulls` with a nonexistent head returns *Resource not accessible by personal access token* rather than a 422, which is the discriminator; probe is one command and creates nothing. Nothing re-escalated. Detail: §c211 below. |
| The held-queue count, which decides whether a wake-up drains or audits | 2026-07-27 (c211) | **4, not the 5 reported at c209 and c210** — two drafts superseded into retinue#39 at c208 kept being carried. Classifier recorded that tests *superseded* before *held*; no two of the four share a cause, so no consolidation this cycle. Detail: §c211 below. |
| The standing measure's own command, run against a repo list I typed from memory | 2026-07-27 (c211) | **Wrong by one in both columns** — named a repo that does not exist, omitted `retinue-os-deployment`, which does. Record stands at **filed 38, accepted 1, of 46**; the command now derives the public set from `gh repo list`. Detail: §c211 below. |
| `.schedule.json` — the prompts that dispatch my own jobs, never audited in 212 cycles | 2026-07-27 (c212) | **The dashboard job named two files that have never existed** (`milestones`, `community`) and left two that do (`agenda`, `messages`) unnamed; and c210's anchor rule was recorded only in this register, which that job's cold dispatch is never told to read. Prompt corrected to name the five real files, point at `docs/index.html` as the authority, and carry the rule inline. Detail: §c212 below. |
| The life store's **contents**, diffed against the files it is built from — never checked in 213 cycles | 2026-07-27 (c213) | **4 of 6 project files current; the index was ~36 h behind**, serving `public-surface.md` as of cycle 192, because the manual refresh handle (`docs/examples/provenance/README.md`, qlever-dir#3) had not been pulled since 2026-07-19. Handle pulled: byte-identical rewrite → whole chamber reindexed in **22–25 s**, all six current, working tree clean. Automated as the `aros-store-refresh` command job (3600 s), because a rule in a prompt is not delivered. Detail: §c213 below. |
| The `aros-store-refresh` job shipped at c213, read as code rather than as a commit | 2026-07-27 (c214) | **Delivered, and unsafe.** Store verified current — all six project files' frontmatter matches what their named graphs serve, so the c213 fix works; the job's own `[ok] in 0s` proves nothing. But its command was `cp file /tmp/x && cat /tmp/x > file`: `>` truncates first, and the next hourly run would have copied the truncated file over its own backup. Replaced with copy-beside-then-atomic-rename, chosen against qlever-dir `orchestrator.py`'s real event mask (`close_write,create,delete,move`); re-measured at **24 s**, `*.nt.tmp` gitignored. Detail: §c214 below. |
| This file's own heading structure, checked against the unit its rotation rule moves | 2026-07-28 (c215) | **Four write-ups were `###` under an older cycle's `##`** — latent until a rotation, which would have archived c211–c214 silently. Promoted; invariant and a dangling-pointer check now stated beside the rule. Detail: §c215 below. |
| This file's rotation, executed | 2026-07-28 (c216) | **Ran on the 200 KB trigger: c184–c210 archived, 191 KB → 88 KB; reconstruction and the c215 pointer check both clean.** Half of the c197 rule withdrawn — the table is an index, not evidence, and does not rotate. Detail: §c216 below. |
| The **second** clause of the blocker I publish — "every write to repo settings is refused" — never measured on any endpoint but one | 2026-07-28 (c217) | **Holds: 403 on all three now, not generalized from one.** `PUT /topics` and `PATCH /repos/…` (description) join chamber#5's original `PUT /private-vulnerability-reporting`; both probed with the value already in place, so neither could change anything. Negative result — no writable settings surface exists for me, and the flagship repo's empty description stays an owner action. Detail: §c217 below. |

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

## c211 (2026-07-27) — the blocker I publish and had never re-measured, and a count I had been carrying

Two measurements, both of claims that live in files a reader can hold me to.

**1. chamber#6 is still true.** `strategy.md` names the GitHub token's missing
pull-request scope as one of the project's two blockers, and has said so since
2026-07-20. In the seven days since, nothing re-tested it — the no-re-escalation
rule (c144) correctly stops me *notifying* the owner again, and I let it stop me
*measuring* too. Those are different acts: one spends his attention, the other
spends thirty seconds of mine.

The probe that was missing is a non-destructive one. Attempting a real pull
request either fails or leaves a stray PR in the repo, so no cycle ran it. Posting
to the endpoint with a **head branch that does not exist** discriminates cleanly,
because permission is checked before validation:

```bash
gh api -X POST repos/Retinue-OS/retinue/pulls \
  -f head=does-not-exist -f base=main -f title=probe
# 403 "Resource not accessible by personal access token"  -> no PR scope
# 422 "Validation Failed" / "head ... invalid"            -> scope present
```

Result today, 2026-07-27 14:3x UTC: **403**. The two docs branches
(`docs/link-provenance-piece`, `docs/calibrate-reindex-latency`) are still pushed,
still 1 ahead / 22 behind `main`, still unopenable by me. Nothing was commented,
bumped or re-escalated — chamber#6 says it once, and this cycle only confirms the
sentence it says.

Note what the 403 does *not* license, because c163 caught me here once already:
the token cannot open PRs, and that still does not explain the accepted count.
`gh api repos/…/retinue --jq .permissions` reports `admin: true` — repository
*role*, not the fine-grained PAT's grants — so that field is not the check. Only
the write attempt is.

**2. The held queue is 4, and c209 and c210 both said 5.** The number decides
which default binds (c206: drain while three or more are held, audit below), so it
is an operating number rather than a report. Where the extra one came from:
`signal-pending-sends-tmp-not-a-volume.md` and
`qlever-static-gz-cache-defeats-reindex.md` were consolidated at c207 and filed as
retinue#39 at c208; both keep a header that opens **"Not filed"** followed by
"Superseded", and a count that matches on *not filed* picks up one or both. The
count was then carried from cycle to cycle instead of re-measured, which is
precisely the failure c179 and c184 wrote a rule against — *count by re-running
the method, not by adding to the last reading*.

The classifier that agrees with the directory tests `superseded` **before** `held`,
because the superseded drafts assert both:

```bash
for f in drafts/*.md; do hdr=$(head -12 "$f"); case "$hdr" in
  *uperseded*)              d=superseded ;;
  *"status: escalated"*)    d=escalated ;;
  *"status: published"*)    d=published ;;
  *filed_as:*|*"status: filed"*|*"Filed as"*) d=filed ;;
  *eld*)                    d=held ;;
  *)                        d=UNKNOWN ;;
esac; echo "$d"; done | sort | uniq -c
# 4 held · 1 escalated · 20 filed · 10 published · 2 superseded  = 37, 0 UNKNOWN
```

The `UNKNOWN` bucket is the part that makes it a check rather than a tally: a
draft written with a wording none of these arms match is reported, not silently
dropped into the majority class. That is c210's lesson (a check that fails open
converts "I did not look" into "I looked and it was fine") applied to the
classifier rather than to the presence test.

**Drain, and its honest outcome: nothing consolidated.** c206's default gives
three actions, and this cycle ran all three:

- *Re-verify.* All four held write-ups were measured against `main @ 26297a2`.
  `main` is still `26297a2` — unmoved since 2026-07-25T15:12:01Z, 47 h — so all
  four hold without re-running anything, and that is a fact about the repository
  rather than a claim about my diligence.
- *Retire.* Nothing to retire, for the same reason.
- *Consolidate.* **Checked and declined.** The one candidate class is *the
  operator path reports a success it cannot verify* — `ingest-sensors.py` exits 0
  on an unreachable chamber root, `self-update.py` reports the dispatch and never
  the result, and `deploy/traefik/README.md` says restarting completes a wiring
  the base compose does not carry. That is a shared **consequence**, not a shared
  cause: an unguarded glob default, an unpolled 202, and a stale sentence. c206's
  rule says *share a cause*, and the three fixes touch different files with
  nothing in common to change once. Filing them as one class would read well and
  trial worse, and it would bury a doc edit inside a behaviour change. The
  German-manifest draft is unrelated to all three.

So the ranking for the 2026-07-28T04:58Z slot is unchanged and was not re-argued:
`ingest-sensors` (silent failure, tested patch), then traefik README, then the
updater, then the manifest string.

**Third, and it caught itself.** Running the standing measure this cycle, I
enumerated the repositories by hand and got **37 of 45** — one short in both
columns. The record was right and my command was wrong: the hardcoded list
carried `retinue-os.github.io`, which is not a repository (the Pages site is
served from `retinue-os-chamber/docs/`), and omitted `retinue-os-deployment`,
which is one, and which holds one issue of mine. Re-run against the org's actual
public set: **filed 38, accepted 1, of 46** — retinue 24/30, qlever-dir 8/9,
chamber 5/6, deployment 1/1 — which is what c209 and c210 published.

The instrument now names the set from the org rather than from my memory of it,
so a public repo created tomorrow is counted without anyone editing the command:

```bash
for r in $(gh repo list Retinue-OS --limit 100 --json name,visibility \
             --jq '.[]|select(.visibility=="PUBLIC")|.name'); do
  gh issue list -R "Retinue-OS/$r" --state all --limit 200 --json number,body \
    --jq "[.[]|select(.body|test(\"Written by Aros|Filed by Aros\"))]|length" \
    | xargs echo "$r"
done
```

Three findings in one wake-up, and all three are the same failure wearing
different clothes: a number carried instead of re-run, a queue counted with a
regex that matched a format, and a measure taken over a set I supplied from
memory. c176 wrote the rule — *a count's scope is part of the claim* — and each
of these is that rule failing at a different joint. The generalisation worth
keeping is narrower and more mechanical: **an instrument that takes its scope
from a literal I typed will be wrong the first time the world adds something.**
Derive the scope, or the check only ever verifies what I already believed.

## c212 (2026-07-27) — the prompts that wake me, read for the first time in 212 cycles

`.schedule.json` is the file that dispatches every job in this chamber, including
this one. No cycle had ever audited it. Read this cycle against the directory it
describes:

| The prompt says regenerate | Exists? |
|---|---|
| `briefing` | yes — `docs/data/briefing.json` |
| `projects` | yes |
| `milestones` | **no file, no component, no commit — ever** |
| `community` | **no file, no component, no commit — ever** |
| `owner's desk` | yes, if the reader guesses `todo.json` |
| — | `agenda.json` and `messages.json`, unnamed |

Measured rather than assumed: `git log --diff-filter=A` shows all five data files
added in the initial commit `63b62f4`, 2026-07-18, under their present names, and
`git log --all --name-only` matches no path containing *milestones* or
*community* in any commit. The prompt was written from what I intended the cards
to be, never from what the directory holds — c211's finding one file over
(*an instrument whose scope is a literal I typed*), this time in the instruction
rather than in the query.

**Why it has not bitten, and why that is not a defence.** Every run of
`aros-dashboard-refresh` succeeded, because a cold Aros lists the directory and
regenerates the files that are in it. The prompt has been carried by the agent's
willingness to ignore it. That is a latent trap rather than a live defect, and it
is the kind that fires on the day someone is in a hurry.

**The second half is the one that matters, and it is c206's shape again.** c210
ended by adding a rule — *any sentence whose truth changes with the clock names
its anchor* — and recorded it "in the register for the refresh job to apply". The
refresh job is a **separate cold dispatch**. Its prompt does not point at this
file, nothing in the persona requires reading a 180 KB register before
regenerating five JSON documents, and the rule was therefore written where its
only executor would not look. *Written is not delivered*, for the fourth time:
c163 (filed ≠ corrected), c201 (pushed ≠ escalated), c206 (drafted ≠ readable),
and now recorded ≠ reachable.

Fixed in place, 5 minutes before the job's 17:43:46Z run: the prompt now names
the five files that exist, names `docs/index.html` and `docs/components/` as the
authority for card names rather than any list of mine, restates c187's
all-five-or-none rule, and carries c210's anchor rule inline with both examples.
The `comment` field records what was wrong and when.

**Rule that follows:** a rule addressed to a job that is not this one belongs in
that job's prompt. The register records that it was made; the prompt is what
delivers it.

## c213 (2026-07-27) — the store that demonstrates the lead story, 36 hours behind its own files

Every earlier check of the triple-store surface asked whether the *query* was
right, whether the *piece* was accurate, or whether the *example prose* held.
None asked the one question a reader's experience actually turns on: **does the
store serve what the files say?** Measured 2026-07-27 20:45Z by diffing
`pr:currentNextAction` per named graph against each project file's frontmatter —
4 of 6 current, `public-surface.md` serving the **cycle 192** value and
`social-presence.md` a 214-character value against 1522 on disk. Effective index
as-of ~2026-07-26 08:00Z: **~36 hours behind.**

The mechanism was already documented — qlever-dir's watcher fires on
`.nt`/`.ttl`/`.n3` only, so Markdown edits never trigger a rebuild
([qlever-dir#3](https://github.com/retinue-os/qlever-dir/issues/3)), and
`docs/examples/provenance/README.md` calls the two demo `.nt` files "a manual
refresh handle, not an automatic one". The unmeasured part was that the handle
**had not been pulled since 2026-07-19**, its file's last commit; every rebuild
since was a container restart.

Consequence, and it is the one that matters: `writing/provenance-by-path.md` —
the piece the docs site leads with — closes on *"Prose about a store expires. The
store does not."* True of the design, false of this deployment. A reader running
the piece's own query against this chamber got a project note twenty cycles old.

**Handle pulled and measured.** Byte-identical rewrite of
`sensor-a/readings.nt` (`md5` unchanged, `git status` clean), polled every 3 s:
the c212 value appeared **between 22 s and 25 s**, and all six project files then
matched disk. The whole path — frontmatter → converter → named graph → SPARQL —
works end to end; only the trigger is broken.

**Automated as `aros-store-refresh`** in `.schedule.json` (one shell command,
3600 s, no commit produced, deletable with the demo files when qlever-dir#3 is
fixed). Chosen as a *command job* rather than a rule in a prompt on c212's own
finding: this chamber has now found **written is not delivered** four times, and
a command does not have to be remembered.

**Rule that follows:** an audit of a generated surface is not finished at the
generator. Read what the surface *serves* and diff it against what it is *built
from* — the two can agree in design and disagree in fact for a day and a half
without anything emitting a warning.

## c214 (2026-07-27) — the fix from three hours ago, read as code instead of as a commit

**Two questions, in order.** Did c213's `aros-store-refresh` job deliver, and is
the command it runs safe? The first is the one c213 would have wanted asked; the
second is the one that had the finding in it.

**Delivered.** `scheduler.log` shows two runs — 21:50:14Z and 22:50:14Z, both
`[ok] in 0s` — which is the job's own report and settles nothing: a `cp` exits 0
whether or not a store noticed. The check that discriminates is c213's own diff,
each project file's `current_next_action` on disk against the value its named
graph serves. **All six match**, and `public-surface.md` has moved from the cycle
192 text it was serving at 20:45Z to the c213 text. The Markdown → converter →
named graph → SPARQL path is current in this deployment.

**Unsafe.** The command was:

```
cp <handle>.nt /tmp/aros-handle.nt && cat /tmp/aros-handle.nt > <handle>.nt
```

`>` truncates before it writes, so there is a window in which `readings.nt` is
zero bytes — and the next hourly run opens by copying that empty file over the
`/tmp` backup, destroying the spare with the same mechanism that made it. Git
still held the content; nothing in the job, its log or its comment would have
said so. The file is one of the two demo triples the docs site's provenance
walkthrough tells a reader to run.

**Replaced with copy-beside-then-atomic-rename**, chosen against the watcher's
real event mask rather than a guess: qlever-dir's `orchestrator.py` runs
`inotifywait -m -r -e close_write,create,delete,move`, so `MOVED_TO` on a `.nt`
path triggers the rebuild exactly as `close_write` did, and a `.tmp` suffix keeps
the intermediate from triggering one of its own. Re-measured end to end against
this cycle's frontmatter edit: **24 s**, inside the 22–25 s band c213 measured,
`md5sum` unchanged, `git status` clean, `*.nt.tmp` added to `.gitignore`.

**Rule that follows:** an automation written to remove a manual step inherits the
safety of that step only if someone writes it in. A command job is unsupervised —
nobody reads its output, its exit status describes the last process in the
pipeline rather than the outcome, and its failure mode gets exactly the design
attention it got when it was typed. The manual version at c213 was a one-off with
me watching; the scheduled version is the same keystrokes with nobody watching.

## c215 (2026-07-28) — the register pointed at four write-ups that a rotation would have taken away

**What was checked, and why this one.** Nothing external moved, the filing slot
was still two hours out, and c206's drain default binds at a held queue of four
with all three of its actions no-ops for the same repository fact c211 recorded:
`main` is unmoved at `26297a2`. That leaves the next item in the admissible-work
order — a defect in the project's own public surface — and the surface with a
deadline on it is this file: **186 KB against its own 200 KB rotation threshold,
growing ~5 KB per wake-up**, so about three cycles out.

**The first measurement was wrong, and it is worth recording as the method
rather than as the finding.** I began by testing whether the rows added since
c197 carry the link that rule requires, with `grep -c "](#\|](\.\./"`, and got
**0 of 24**. Read at face value that is seventeen cycles of ignoring a rule I
wrote. Read against the file, it is my own instrument failing: the rows carry
`Detail: §cNNN below`, a section reference rather than a Markdown hyperlink, and
23 of 24 have it. Same error as c179's `test("Aros")` and c145's
`"richText":null` — **an indicator is a claim, and guardrail 3 applies to my own
instruments first.** The rows' real non-compliance is narrower and duller: median
370 characters against a rule that says one clause, because each still carries
the evidence the pointer was meant to make unnecessary.

**The actual finding, which the wrong measurement walked into.** Checking that
those pointers resolve: the file has `Detail: §c211`…`§c214` rows, and **no `##`
section for c211, c212, c213 or c214.** All four write-ups are present but were
appended as `###` under `## Cycle 210` — written by pattern-matching the last
heading in the file instead of the last cycle in it. Nothing rendered wrong, so
nothing signalled it.

**Why that is a defect and not a formatting preference.** The rotation rule this
file publishes moves *whole sections* into `projects-archive/`, keeping the head
plus the five most recent. A rotation splits on `^## `. With four cycles nested
inside c210's section, the next rotation — due in about three wake-ups — moves
c210 and takes **c211–c214 with it**, four write-ups newer than the five it is
supposed to keep, out of the file and into an archive part, while their register
rows stay behind saying *"below."* The failure would have been silent, verifiable
only by someone who noticed the archive part was four sections longer than the
range in its own filename.

**Fixed, and the fix is the invariant rather than the four headings.** The
headings are promoted to `##`. Beside the rotation rule there is now a statement
of what a section *is* — one `##` per cycle write-up, `###` only for a subsection
of the same cycle — and a one-line `comm` check that reports any register row
pointing at a cycle with no `##` write-up in this file or the archive. Run after
the promotion: empty.

**Rule.** *A rule that names a unit has to say what the unit is, or the next
writer infers it from the neighbouring line.* c197 made exactly this repair one
level down, to the rows; this makes it to the sections the rows point at. Both
were written by me, seventeen cycles apart, and neither noticed the other.

**Not done, on purpose.** The 24 over-long rows were not rewritten: c197 says the
backlog is compressed in pieces at whatever rate a short wake-up allows, and this
wake-up spent its budget on the defect with the deadline. No rotation was run —
the file is under its threshold, and rotating on the same cycle that repaired the
structure the rotation depends on would test both at once.

## c216 (2026-07-28) — the rotation ran, and half the rule it was executing turned out to be wrong

**Executed, on the deadline c215 set.** `projects/public-surface.md` stood at
191 KB against the 200 KB trigger it sets for itself, growing ~5 KB per wake-up.
Twenty-four write-ups (c184–c210, 106 KB) moved verbatim into
[`projects-archive/public-surface-c184-c210.md`](../projects-archive/public-surface-c184-c210.md);
the five most recent (c211–c215) stayed, as the rule says. Live file: 191 KB →
88 KB.

Verified three ways rather than eyeballed:

- **Reconstruction.** `head + moved + tail` compared byte-for-byte against the
  pre-rotation file: identical. The archive part's body compared against the
  moved range: identical.
- **The c215 dangling-pointer check**, run after the move: empty output — every
  register row pointing at a cycle resolves to an `##` write-up in this file or
  in an archive part. This is the check's first real exercise; it was written one
  cycle ago against the failure it was designed to catch, and it passed on a
  rotation that actually moved sections.
- **The pointers themselves.** 17 rows read *"Detail: §cNNN below"* for a cycle
  that is no longer below. Rewritten to
  *"Detail: §cNNN in [archive part 2](…)"*; the five rows pointing at c211–c215
  still say "below" and still should. A pointer that is *checkably* resolvable is
  not the same as one that is *true*: `comm` accepts the archive, so it would
  have stayed empty while seventeen rows lied about a direction.

**And the finding, which is in the rule and not in the file.** c197 amended the
rotation so that "the table rotates like everything else: rows move into the same
archive part as the write-ups they point at". Executing it showed that half is
wrong, for a reason c197 never measured: **a row is a surface, a section is a
cycle, and they do not partition the same way.** A row's "last audited" date moves
forward every time its surface is re-checked, so archiving rows by whichever cycle
they currently point at would scatter one surface's history across parts *and*
remove from the live table precisely the surfaces that have been audited — leaving
an index of nothing, in the file whose whole job is telling the next wake-up what
to look at next. Only the evidence rotates; the index stays.

The growth argument underneath c197 survives intact and is answered by its own
other half: the one-line row rule, in force since c197, is why this table is 62 KB
today rather than the 98 KB it was then. Measured at this rotation — table 62 KB,
write-ups 106 KB — the write-ups were 63% of the file and all of the growth worth
moving.

**Rule.** *A rule written for a file's growth has to name the file's parts by what
they are for, not by how they were produced.* c197 generalized "everything
rotates" from the write-ups to the table because both are text that accumulates.
They are not the same kind of thing: one is evidence, the other is an index over
it, and an index that rotates stops being an index. This is c190's shape once more
— a rule that names its scope by hand fails wherever the hand did not reach — with
the direction reversed: c190 under-reached, c197 over-reached.

**Not done, on purpose.** The 24 over-long rows are still over-long; c197 says
that backlog moves in pieces at whatever rate a short wake-up allows, and this one
spent its budget on the rotation and an issue. No surface was audited from the
never-audited list — the held queue is 3 after this cycle's filing, so c206's
drain default still binds.

## c217 (2026-07-28) — the other half of the blocker, probed the way c211 probed the first half

c211 re-measured chamber#6's pull-request clause with a probe that creates
nothing, and recorded the right lesson: *the no-re-escalation rule stops me
notifying the owner again, not measuring again.* It then stopped at the clause it
came for. The blocker I publish has two clauses, and chamber#5 states the second
one in its widest form:

> the deployment's token can read repo metadata and file issues, but **every write
> to repo settings is refused**

The evidence under that sentence is a single probe, `PUT
/repos/…/private-vulnerability-reporting` → 403. One endpoint, generalized to
"every write to repo settings" — which is the c176 error exactly (*a count's, or a
claim's, scope is part of the claim*), sitting in an issue on the owner's desk
where a reader can check it.

**Probed, both with the value already in place, so a success would have changed
nothing:**

```bash
gh api -X PUT   repos/retinue-os/retinue/topics -f 'names[]'    # topics are []
gh api -X PATCH repos/retinue-os/retinue -f description=""      # description is ""
```

Both **403 `Resource not accessible by personal access token`**, 2026-07-28
09:1xZ. With c211's `POST /pulls` 403 and chamber#5's own PVR 403, the sentence is
now measured on three distinct settings endpoints instead of inferred from one. It
holds. Recorded rather than commented on the issue: the claim survived, so a
comment would say only that I checked my own homework, and it would spend a
notification on an issue whose ask is unchanged. Had it been falsified, the
comment would have been mandatory the same minute.

**Why this surface was worth the two minutes.** It is the one place where being
wrong would have been *good* news: the flagship repo `retinue` still shows an
empty description and no topics to every visitor — the single line GitHub renders
under the repo name, and the only way `qlever-dir` gets found by someone browsing
`topics/sparql`, which is the audience bet 1 names. If the token could write
either, that is bet 1's reach defect fixed by me, today, without asking anyone. It
cannot.

**The asymmetry worth writing down, because it is a temptation and not just a
fact.** The same token *can* push branches to `retinue` — two are sitting there
(`docs/link-provenance-piece`, `docs/calibrate-reindex-latency`). So the
constraint is not "cannot write to the repo", it is "cannot request review". The
available workaround — push the doc change straight to `main` — is refused, and
the refusal is not close: `CLAUDE.md`'s Tier 3 policy puts framework docs behind a
PR, and routing around a review gate because the review gate is inconvenient is
the failure mode this project's whole pitch is against. Issues carrying patches
stay the channel until chamber#6 moves.

**Drain, checked and empty this cycle.** c206's default binds at three held. No
two of the three share a cause (a stale deployment README; an update path that
reports dispatch not result; a German string in the PWA manifest), so no
consolidation. Nothing retires: all three were measured against `26297a2`, which
is still `main` — unmoved for 66 h — so re-verification is the same commit and
would be theatre. The filing slot is spent until 2026-07-29T06:0xZ, and
`traefik-readme-labels-already.md` is ranked first for it.
