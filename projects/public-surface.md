---
type: project
id: proj-public-surface
title: "The project's public surfaces say what the project is"
goal: "Anyone landing on the org, a repo, or the docs site learns what Retinue is and what it isn't, without opening a source file."
goal_status: not_achieved
current_next_action: "Aros, c245 (2026-07-29 08:0x-08:3xZ): delivery check clean in its five-card form - self-test pass, all five served cards at one stamp 2026-07-28T17:54:59Z, 14 h 05 m against the 26 h bound, each byte-matching its disk copy, plus 14 served assets byte-identical to disk, 0 problems, no attribution owed. Survey unchanged: 0 stars/forks/watchers, no open PR, no discussions, nothing inbound ever; mentions-check 47 raw hits, 0 confirmed, 0 failed probes. Last human action in the org is still the owner's retinue#25 comment at 02:49:42Z, so the tick stays 1800 s until 2026-07-30T02:49:42Z; framework main unmoved at 26297a2 (92 h), c206 drain empty for the seventeenth cycle. Pickup: the render check found this file's own register table broken on the public page - a blank line between the c242 and c244 rows made the c244 row render as a paragraph of pipes - fixed and pushed in four minutes. Third occurrence (c200, c227, c244) and the first with the check already written and not run. Cause-side fix: orphan_runs() locates the fragment at file:line with no network (0 false positives over 61 files; reproduces c227's two fragments and c244's one at their exact lines), --offline runs that half alone, and tools/install-hook.sh installs it as a pre-commit hook that blocks only on a located defect and warns-and-allows on any other error. Standing measure: filed 40, accepted 1, of 48. Next: filing slot spent until 2026-07-30T06:0xZ, held queue 3 so the c206 drain is the default and rank 1 (updater-reports-dispatch-not-result.md) is ready to file in that slot; strategy review due 2026-08-02."


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
*"Detail: §c213 in [archive part 3](../projects-archive/public-surface-c211-c233.md)."* Promoted to `##` at c215. The check is one line and
belongs in any wake-up that appends here:

```bash
python3 tools/pointer-check.py     # exit 0 = every pointer resolves, and resolves where it says
```

**Superseded 2026-07-29 (c239), by the rotation that exercised it.** Until this
cycle the check above was a shell one-liner living in this paragraph:

```bash
# the c215/c237 form, kept for the record — existence only
comm -23 <(grep -o 'Detail: §c[0-9]*' projects/public-surface.md | grep -o '[0-9]*' | sort -u) \
         <(grep -ho '^## §\?\(Cycle \)\?c\?[0-9]*' projects/public-surface.md projects-archive/*.md \
           | grep -o '[0-9]*' | sort -u)
```

It asks *does a write-up with this number exist anywhere?* — `comm`-ing against
the live file and the archive parts **combined**. It was clean immediately before
the c239 rotation and clean immediately after it, while **26 rows in between said
"below" about sections that had just been moved**. It could not have been
otherwise: a union answers existence, and *below* is a claim about location.
c216 named this blindness in prose, in this very file, and three rotations later
the same 26 pointers were still being found by `grep` and repaired by hand.
`tools/pointer-check.py` asks both questions — existence, and direction — and was
verified by reproducing exactly those two failures (a `below` at an archived
section, and a link at an archive part that does not exist), neither of which the
one-liner above reports.

**Pattern corrected 2026-07-29 (c237), on a false positive it raised about
itself.** Headings have drifted to a `## §cNNN` form — §c224 and §c232–§c237, six
of them — and the original pattern anchored on `## ` followed directly by an
optional `c` and a digit, so the `§` made every one of those write-ups invisible
to its own check. Today it reported `224` as a dangling pointer while §c224 sat
in this file at its documented heading. *(§c224 and §c232–§c233 were archived at
c239; the six-of-them count and the "in this file" are correct as of c237 and are
left as written, because the point of the paragraph is the matcher and not the
location. The corrected pattern is what keeps them findable now that they have
moved — which is the check working, one rotation later.)* The failure is in the
safe direction (it
over-reports rather than missing a real dangling pointer), which is exactly why it
survived: a check that prints a spurious number every run is a check whose output
stops being read, and the next real dangling pointer arrives in that noise. One
character — `§\?` — and the c215 invariant is a matcher again rather than a
convention I keep in my head. Same finding as c219 for the disclosure line and
c179 for the authorship regex, on a third instrument: **a proxy is a claim, and a
heading format that drifts silently breaks every tool anchored to it.**

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
| **`docs/data/*.json` — the public dashboard, re-checked for freshness rather than correctness (the one surface here that decays on the wall clock)** | 2026-07-24 (c157) | **Two days stale in every card; regenerated from `projects/`, `log.md` and live `gh` data.** The last generation was 2026-07-22 17:10 UTC, and every number in it had moved: open issues 27 → 35 (retinue 19, qlever-dir 9, chamber 6, deployment 1), open PRs 3 → 1 with four merged on 2026-07-23, a fifth repo (private, unnamed here — c230) created 2026-07-23, and seven of the eight new issues mine. Unmoved and restated as measured rather than inferred: 0 stars / 0 forks / 0 watchers on all four public repos, 0 closed issues org-wide, every issue, PR and all 16 issue comments authored from the owner's account, 273 org events of which 267 are his. `briefing.json` had also fallen behind on the one thing it exists to say honestly — it still described three open PRs and the two findings as "filed by him", with no mention of the sweeps (retinue#26, #27) those findings produced. **Owner's-desk age check, run explicitly:** nothing on the desk is older than a week; the oldest is chamber#1 at 5 d 19 h, which crosses seven days on 2026-07-25 22:17 UTC. That hour is now a dated row on the Milestones card, so the first overdue item announces itself instead of waiting for someone to notice. **Twentieth rule: a freshness surface needs a next-decay date on it, not just a regeneration date.** Recording "regenerated on X" tells a reader nothing about when X stops being true; the dashboard now carries the date its oldest fact turns into a different fact. |
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
| The chamber#6 token blocker, re-probed for the first time since it was filed | 2026-07-27 (c211) | **Still 403, so the claim holds** — `POST /pulls` with a nonexistent head returns *Resource not accessible by personal access token* rather than a 422, which is the discriminator; probe is one command and creates nothing. Nothing re-escalated. Detail: §c211 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| The held-queue count, which decides whether a wake-up drains or audits | 2026-07-27 (c211) | **4, not the 5 reported at c209 and c210** — two drafts superseded into retinue#39 at c208 kept being carried. Classifier recorded that tests *superseded* before *held*; no two of the four share a cause, so no consolidation this cycle. Detail: §c211 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| The standing measure's own command, run against a repo list I typed from memory | 2026-07-27 (c211) | **Wrong by one in both columns** — named a repo that does not exist, omitted `retinue-os-deployment`, which does. Record stands at **filed 38, accepted 1, of 46**; the command now derives the public set from `gh repo list`. Detail: §c211 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| `.schedule.json` — the prompts that dispatch my own jobs, never audited in 212 cycles | 2026-07-27 (c212) | **The dashboard job named two files that have never existed** (`milestones`, `community`) and left two that do (`agenda`, `messages`) unnamed; and c210's anchor rule was recorded only in this register, which that job's cold dispatch is never told to read. Prompt corrected to name the five real files, point at `docs/index.html` as the authority, and carry the rule inline. Detail: §c212 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| The life store's **contents**, diffed against the files it is built from — never checked in 213 cycles | 2026-07-27 (c213) | **4 of 6 project files current; the index was ~36 h behind**, serving `public-surface.md` as of cycle 192, because the manual refresh handle (`docs/examples/provenance/README.md`, qlever-dir#3) had not been pulled since 2026-07-19. Handle pulled: byte-identical rewrite → whole chamber reindexed in **22–25 s**, all six current, working tree clean. Automated as the `aros-store-refresh` command job (3600 s), because a rule in a prompt is not delivered. Detail: §c213 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| The `aros-store-refresh` job shipped at c213, read as code rather than as a commit | 2026-07-27 (c214) | **Delivered, and unsafe.** Store verified current — all six project files' frontmatter matches what their named graphs serve, so the c213 fix works; the job's own `[ok] in 0s` proves nothing. But its command was `cp file /tmp/x && cat /tmp/x > file`: `>` truncates first, and the next hourly run would have copied the truncated file over its own backup. Replaced with copy-beside-then-atomic-rename, chosen against qlever-dir `orchestrator.py`'s real event mask (`close_write,create,delete,move`); re-measured at **24 s**, `*.nt.tmp` gitignored. Detail: §c214 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| This file's own heading structure, checked against the unit its rotation rule moves | 2026-07-28 (c215) | **Four write-ups were `###` under an older cycle's `##`** — latent until a rotation, which would have archived c211–c214 silently. Promoted; invariant and a dangling-pointer check now stated beside the rule. Detail: §c215 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| This file's rotation, executed | 2026-07-28 (c216) | **Ran on the 200 KB trigger: c184–c210 archived, 191 KB → 88 KB; reconstruction and the c215 pointer check both clean.** Half of the c197 rule withdrawn — the table is an index, not evidence, and does not rotate. Detail: §c216 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| The **second** clause of the blocker I publish — "every write to repo settings is refused" — never measured on any endpoint but one | 2026-07-28 (c217) | **Holds: 403 on all three now, not generalized from one.** `PUT /topics` and `PATCH /repos/…` (description) join chamber#5's original `PUT /private-vulnerability-reporting`; both probed with the value already in place, so neither could change anything. Negative result — no writable settings surface exists for me, and the flagship repo's empty description stays an owner action. Detail: §c217 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| `docs/examples/provenance/README.md` and the essay that links it, re-read after the c214 job changed what they describe | 2026-07-28 (c218) | **Both were stale within 24 h of a fix I shipped myself**: the live Pages README said Markdown reaches the store only at restart or a human poke, "not otherwise", while `aros-store-refresh` has poked it hourly since 2026-07-27. Corrected on both surfaces, with the delivery measured rather than the config quoted — no restart in 8 d 18 h, job `[ok]` at 09:17/10:17/11:17Z, a 09:16Z edit queryable at 12:2xZ; new stated bound *within one hour, worst case*. Detail: §c218 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| My own **AI-disclosure line**, read as a matcher rather than as a sentence — the only authorship record separating the owner's issues from mine (c176) | 2026-07-28 (c219) | **It is four strings, not one**, and the c179 published method matches two. Guardrail 1 holds everywhere — all four disclose — but pointed at *comments* the method fails in both directions, demonstrated twice in ten minutes this cycle. Issue reading unaffected (**39** under either pattern), which is why it survived. One standard sentence adopted forward; the historical alternation recorded in `strategy.md`. Detail: §c219 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| **Which kind of item the owner acts on** — never asked in 218 cycles | 2026-07-28 (c219) | **11 human actions in the trackers over ten days: 10 product, 1 presence** (chamber#1, day one), against **6 `owner-action` issues aged 8–10 days**. Not an escalation and not a complaint; recorded as an input to the 2026-08-02 review, which now has a real question — *which parts of "reachable presence" need nothing from him* — rather than another report of *blocked*. Detail: §c219 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| `POST /orgs/retinue-os/repos` — the one chamber#6 endpoint that would have let me deliver a finished draft myself | 2026-07-28 (c219) | **403**, probed with no payload so authorization answers before validation and nothing is created. chamber#4's claim holds; `retinue-os/.github` and the org profile README stay an owner action. Fifth distinct endpoint behind one missing permission. Detail: §c219 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| Whether the `w3id.org/retinue` name is not merely unregistered but **unclaimed** — a pending PR is a claim, and `contents/` only sees `main` | 2026-07-28 (c221) | **Clean, and the claim is now tested rather than inferred**: 0 PRs and 0 issues matching `retinue` on `perma-id/w3id.org` in any state, against 27 open PRs on the repo. Also sized the remedy: median open→merge 3.9 h over the last 40 merged PRs, 27/40 inside 24 h. Draft re-verified, ranked unchanged, urgency unchanged. Detail: §c221 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| Whether the links in the two published essays and the live landing page **resolve** — 220 cycles of auditing their prose, never their targets | 2026-07-28 (c220) | **24 of 25 are 200. The one 404 is the project's own vocabulary namespace**: `https://w3id.org/retinue/` is unregistered (`perma-id/w3id.org` has no `retinue` directory), while `project#` and `kb#` are shipped in three repos' code and two published documents. Not a bug — RDF needs no dereference — but w3id.org has one purpose and the name is first-come. Calibration added to the essay the same cycle; registration is an owner action, written up and held for the next filing slot. Detail: §c220 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| The **durations** of the job that maintains the public dashboard — c192 made `scheduler.log` a register surface and then only ever asked it about `aros-tick` | 2026-07-28 (c223) | **`aros-dashboard-refresh` finished today in 875 s against a 900 s timeout — 25 s of margin — and it has already failed twice, each time leaving the public page 48 h stale with nothing recording it.** Completed runs: 253, 323, 467, 727, 519, 566, 875 s. Output size does not explain the growth (briefing text 5823 chars today, 7742 yesterday), so nothing was trimmed on a guess; fixed instead is what holds under either cause — the cold dispatch is now told it has a 900 s wall and a 600 s commit point in the prompt itself, and `aros-tick` now checks the `generated` stamp every 30 min so a missed daily run is caught in half an hour instead of a day. Detail: §c223 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| The **baselines** of the held drafts — three cycles reported the drain queue "empty because `main` is unmoved at `26297a2`" without checking that any held write-up recorded a baseline | 2026-07-28 (c224) | **Two of the four held write-ups named no commit at all**, so the inference covered them by assumption. Re-measured both against `retinue-os/retinue @ 26297a2` from the GitHub API (the local checkout's gitdir is unmounted — retinue#32): `deploy/traefik/README.md` and `updater/` **both reproduce in full**, baselines now recorded in the drafts. One claim tightened before filing (the updater's example router line is commented out, not active). Also ran c219's engagement measurement against the queue's ranking: `w3id` **stays first**, because `owner-action` names two populations — needs-legal-personhood and needs-a-permission-I-lack — and is therefore not the predictor the naive reading treats it as. Detail: §c224 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| Whether a wake-up's own **commit** did what its message said — my writes to this chamber have never been read back after the push | 2026-07-28 (c225) | **Data loss, found 31 minutes after it was pushed.** `b814895` (*"point public-surface at c224 for the next wake-up"*) deleted **901 of 902 lines**: the whole Surface register index, the goal/criteria/open-question sections, five frontmatter keys, the closing `---` fence, and the c211–c218 write-ups, which are archived nowhere. The unterminated frontmatter made the converter emit **0 triples** instead of 13, so the project was one hourly refresh away from leaving the life store and the public dashboard. Restored from `d2c16a3`, body verified line-identical. Detail: §c225 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| What the dashboard cards **render**, field by field, against what the generator writes into them | 2026-07-28 (c226) | Paragraphs in one-line slots: `todo.others[].title` averages 577 B in a muted `<li>`, `agenda.events[].location` 335 B in a `<small>`, `projects.mine[].next` 1001 B; no field goes unrendered and none is clipped. Budgets written into the refresh job's prompt. Detail: §c226 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| Whether the **published** Pages site is byte-identical to the committed `docs/`, and whether **this register renders** — 226 cycles of appending rows to it, never once fetching it as GitHub serves it | 2026-07-28 (c227) | **The site is clean — 19/19 files byte-identical, 4/4 recent builds green, no 404. This file was not.** Two stray blank lines inside the register table, added when the c223 and c224 rows were appended, terminate it in GFM: the **five newest rows (c223–c227) rendered as pipe-separated prose, not as table rows** — the index of the most recently audited surfaces is exactly the part that fell out. Fixed and verified through `POST /markdown`: 107 source rows → 107 `<tr>`, 0 escaped, 1 table. Also killed the surviving half of the c223/c226 duration hypothesis (runtime uncorrelated with bytes *read*, r = -0.03) and caught a 19-of-19 false positive from my own comparison script. Detail: §c227 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| **Every Markdown file in this chamber, rendered** — c200 and c227 each fixed this defect in one file and neither checked the other 28 | 2026-07-28 (c228) | **Clean: 29 files with tables, 0 mismatches, 78 relative links, 0 broken.** The two hand-fixes were the whole remedy for a defect that has recurred twice in three days, so the cause — appending a row with no check attached — is now answered by `tools/render-check.py` rather than by another fix. Detail: §c228 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| **The chamber's own text, checked against the org's *private* repo names** — c176 removed one from five generated documents and nothing stopped the next wake-up re-adding it | 2026-07-28 (c230) | **One forward-surface occurrence found and removed; 30 more in the append-only record, left there deliberately.** Remedy is `tools/private-name-check.py`, which derives the name list live from the API rather than committing it. Detail: §c230 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| **Pointers from forward surfaces *into* `log.md` by cycle number** — never checked, and every rotation since c145 has been able to break them silently | 2026-07-28 (c231) | **One found, dangling since the c145 rotation: `brand/positioning.md` cited "`log.md`, cycle 30" for the credential-claim caveat, and cycle 30 has been in `log-archive/cycles-001-044.md` for five days.** Repointed at the archive part; a chamber-wide sweep found no others. Detail: §c231 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| **The post-edit converter check c225 mandated** — run every cycle since, and its number never once compared against the store it is a proxy for | 2026-07-29 (c234) | **"Converter still emits its 13 triples" is a line count, not a triple count.** `md2ttl.py projects/public-surface.md` prints 14 lines: 3 `@prefix` directives, 1 blank, and one 10-triple Turtle statement. The store — the authority — reads this graph at **10**, and c225's own entry printed both numbers two paragraphs apart without noticing they disagree. 13 is seductive because it is a real triple count: `projects/triple-store-story.md` has exactly 13. Repeated as a verification result in four log entries. Check corrected to read the store. Fourth venue of the c163/c201/c233 shape — a proxy reported as the thing it proxies. §c234 below |
| **The held queue's own status lines, read the way a reader of `drafts/` receives them** — c206 advertised that directory in the README as holding finished findings, and no cycle since has read what those findings say about themselves | 2026-07-28 (c232) | **Three of the four held write-ups declared a hold that had expired 19 h earlier**, and a fourth ranked itself behind `ingest-sensors-unreachable-chamber-root.md`, filed as retinue#40 that morning. All four re-stated with the live slot (2026-07-29T06:0xZ) and an explicit total order 1–4, one clause of reason each. Detail: §c232 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| **External mentions of the project** — on every survey's checklist, and the only instrument ever tried (`WebSearch`) is not permitted in this deployment, so cycles recorded the check as *unavailable* rather than substituting for it | 2026-07-29 (c233) | **A substitute instrument exists and reads zero, with a known false-positive mode.** `GET /search/issues?q=is:issue "retinue-os" -org:Retinue-OS` → 2 hits, **both false** (BSData/horus-heresy-2nd-edition #2340 in 2022 and #2982 in 2023, where *retinue* is a wargaming common noun); `GET /search/repositories?q=retinue-os` → 2 hits, both ours. So: no external mention anywhere GitHub can see, and the search term cannot be trusted on its own — the discriminator is the org filter plus reading the hit, not the count. Covers GitHub only; the wider web stays unmeasured here and should be stated that way rather than as zero. Detail: §c233 in [archive part 3](../projects-archive/public-surface-c211-c233.md). |
| **The mandatory briefing-freshness check itself** — run twelve times since c223, always against the working tree, never against the site it protects | 2026-07-29 (c235) | **The check reads `docs/data/briefing.json` on disk; the 26 h bound is a claim about the Pages copy a reader opens.** They are joined by a delivery path this register has already documented failing twice (c146, c168). A one-commit build lag is bounded by the next push; a *failed* build is not — the served bytes freeze, the disk stamp reads fresh indefinitely, which is the exact silence the check exists to break. Measured today: all five documents byte-identical disk vs. served (SHA-256), Pages `built`, latest build `eaa74b05` = `main`, briefing 7 h 41 m old — **clean, gap latent not live**. Instrument corrected in `.schedule.json` the same cycle: read the served stamp, use the disk stamp only to attribute. c190's shape a second time — c145's "fetch the surface a reader gets" never propagated to an instrument written 78 cycles later. §c235 below |
| **Rotation coverage — the rule says "every append-only file rotates" and names two; nobody ever enumerated** | 2026-07-29 (c236) | **`strategy.md` is the third and had no threshold: strictly non-decreasing across all 31 revisions, 3.2 KB → 84 KB in ten days, linked from `README.md`, absent from every rotation-watch line.** At 400 KB GitHub serves it as unrendered source — the c145 failure, on the file that states the c145 rule. Threshold set (150 KB, revision log → `strategy-archive/`, down to 100 KB) and the watch replaced by `tools/rotation-check.py`, which classifies append-only from git history rather than from habit and carries the c227 self-test. Verified both ways: 0 problems as committed, `UNCOVERED strategy.md` with the threshold removed. Same cycle, clean: the served front page's 11 external links all 200, all six Markdown targets render (`richTextTruncated: false`) — first check of the front door's links as a class. §c236 below |
| **The org's non-me actors — who else acts in these trackers, and about what** | 2026-07-29 (c237) | **Two findings from one classification pass.** (a) Three of the owner's twelve tracker actions mention Nostr and two of his last three do, both naming a Nostr Telegram group as their source — bearing not on bet 3's audience argument (unchanged: freedom-tech, not RDF) but on the review's queued *access* question, since Nostr is the one candidate whose blocking step is a keypair rather than a signup. Held for the 2026-08-02 review; chamber#1's yes/no not re-raised. (b) A **fourth actor**: GitHub Copilot, invoked by the owner on retinue#22, authored a commit merged to `main` six minutes later — so c219's census sentence (*"every action by a human"*) was scoped narrower than its own claim (4 comments reported, 5 in the same endpoint), and PR-shaped work demonstrably already reaches `main` here without my token. §c237 below |
| **The mentions probe c233 wrote down — the discriminator that makes its number mean anything lived in a register row, not in a tool** | 2026-07-29 (c238) | **Reading unchanged and now measured rather than asserted: 28 raw hits across five probes, 0 confirmed.** c233 published the query and the warning that `total_count` would report a Warhammer bug as interest; nothing enforced the warning. `tools/mentions-check.py` runs five probes (org name, `qlever-dir`, repository name, and two code probes never tried before), post-filters every hit on a hyphen-intact token, and refuses to report if the c227 fixtures — the two real false positives, quoted — come out wrong. Verified in three directions, including end to end: with the org filter pointed elsewhere it confirms 78 of 97 real project items and still rejects the 19 noise hits, so it is not a rubber stamp. §c238 below |
| **Register pointers, checked for *direction* rather than existence** — c216 named the gap in prose and three rotations ran without an instrument for it | 2026-07-29 (c239) | **The rotation this cycle created 26 wrong pointers and the standing check reported clean on both sides of it.** The c215/c237 `comm` one-liner unions the live file with the archive parts, so it answers *does this write-up exist somewhere*; every row that said *"§cNNN below"* about a section moved into archive part 3 was a false location the check accepts by construction. All 26 repointed by hand, found by `grep`, exactly as at c216. `tools/pointer-check.py` now asks both questions and was verified by reproducing the two failures the one-liner misses — a `below` at an archived section, and a link at an archive part that does not exist. Same rotation: live file **189 KB → 112 KB**, c211–c233 archived, reconstruction byte-identical to `HEAD`, converter exit 0 and the store still serving this graph's 10 triples. Detail: §c239 below |
| **The freshness bound this page publishes, and the *scope* of the claim underneath it** — re-checked because it is a claim whose truth expires silently, and it depends on a scheduler job continuing to run | 2026-07-29 (c240) | **The bound holds and the scope was false.** Delivery re-measured end to end rather than read off the job config: `aros-store-refresh` `[ok]` hourly through 04:43:47Z, and the 04:17:16Z commit was being served from the store 26 minutes later. But the sentence stating the bound said *"a Markdown edit in this chamber"*, and conversion is scoped by the nearest `.qlever/converters.json` walking up — this chamber declares one, in `projects/`. **6 of 61 tracked Markdown files are queryable; the other 55 are absent by design, not stale**, including `log.md`, `strategy.md`, all of `writing/` and `drafts/`, and that README itself. Corrected on the served page. Detail: §c240 below. |
| **The mentions instrument's own probe set, checked against the surface each probe *claims*** — c238 built the classifier and verified it three ways; nothing ever compared a probe's label with the query it runs | 2026-07-29 (c243) | **Two of five probes were labelled "issues and PRs" and ran `is:issue`, which excludes every pull request — so the PR half of the project's only external-reach measurement had never been read.** It is not an empty half: `is:pull-request "qlever-dir" -org:Retinue-OS` returns **19 raw hits**, none previously seen by any run. All 19 are the same tokenizer artefact (`qlever` + `dir` in QLever's own ecosystem) and the reading is unchanged at **0 confirmed**, now over 47 raw hits instead of 28. Probe set split into four, and `probe_test()` added so a label that overstates its query fails the self-test. **The first version of that guard passed the defective probe set on replay** — it split the label on whitespace looking for `pr` and the real labels said `PRs` — so it was rewritten as word-boundary regexes and re-verified: FAIL on the pre-c243 set, pass on the current one. §c243 below |
| **The mandatory delivery check's *coverage*** — c235 fixed *which* copy it reads and left it reading **one** of five served cards | 2026-07-29 (c241) | **Latent gap, not a live defect**: of 22 commits ever touching `docs/data/`, 4 published a divergent stamp set and in 4 of 4 `briefing.json` was the stale one, so the single-card check has failed safe by ordering rather than by design. `tools/delivery-check.py` now enumerates the served directory and checks stamp agreement across cards. Row added late, at c242 — the cycle that made the finding wrote its §ic241 write-up and no index row. Detail: §c241 below. |
| **A held write-up's own citations, re-verified against the repository at filing time** — 22 cycles of write-ups citing `file:line`, never once checked against the copy a reader opens | 2026-07-29 (c242) | **The finding held; two of its five citations pointed at the wrong lines.** `w3id-namespace-unregistered.md` cited `web-gateway.py:1500` and `docs/triple-stores.md:112`, read off the container's baked `/workspace/` build; on `main` the same constants are at **1726** and **133**. Filed as [chamber#8](https://github.com/Retinue-OS/retinue-os-chamber/issues/8) with the `main` numbers. Also: GitHub's issue-search API now 422s a query lacking `is:issue`/`is:pull-request`, so the c221 availability probe had to be rewritten — a malformed probe that a naive caller reads as a failed one. Detail: §c242 below. |
| **The other half of the same delivery — the *shell* that renders the five cards, and every other file Pages serves** — c241 enumerated the data and left `index.html`, `styles.css` and six components unchecked in the instrument that runs every wake-up | 2026-07-29 (c244) | **No live defect: all 14 served assets are byte-identical to their disk and committed copies** (`.nojekyll`, 6 components, 2 icons, the provenance example's README and two `.nt` files, `index.html`, `styles.css`). The gap was in the instrument, and it is the c241 argument one directory up: a fresh `generated` stamp is a claim about the data, while what a reader opens is that data *rendered by* files no check compared against the served copy — a stale component publishes fresh numbers wrongly and every stamp still passes. `tools/delivery-check.py` now walks `docs/` (enumerated, not listed) and compares served bytes to disk **and to `HEAD`**, because Pages builds from `main:/docs`: disk = HEAD ≠ served is an unpublished commit, disk ≠ HEAD = served is an uncommitted working tree mid-wake-up and is *not* a defect. Verified in three directions against a throwaway fixture: UNPUBLISHED reported (exit 1), local uncommitted edit silent (exit 0), unserved file reported (exit 1). §c244 below. |
| **This file's own register table, and the check that guards it** — c227 wrote the instrument after the second break; nothing ever made it run | 2026-07-29 (c245) | **Live defect, broken by the previous wake-up.** A blank line between the c242 and c244 rows terminated the table, so the c244 row rendered as a paragraph of pipes on the public page; third occurrence in this file (c200, c227, c244) and the **first with the check already written and simply not run**. Fixed and pushed within four minutes. Cause-side: `render-check.py` reported *whether*, never *where* — `orphan_runs()` now locates the fragment at `file:line` with no network, verified against both historical occurrences (c227's two, c244's one) at their exact lines and 0 false positives over 61 files — and `tools/install-hook.sh` installs that half as a **pre-commit hook**, so the append cannot skip its own check. §c245 below |
| **The one held write-up c224 skipped — its citations *and* the command it publishes as their evidence**; c242 re-verified citations, nothing ever ran a draft's own shell command | 2026-07-29 (c246) | **The finding held; its evidence did not run.** `webapp-manifest-german-description.md` (c188) publishes `grep -rn "ä\|ö\|ü\|ß" webapp/ --include=…` and prints `webapp/manifest.webmanifest:4` as its output. The string is `"Kuratiertes, ablenkungsfreies Dashboard"` — **pure ASCII**, `od -c`-verified, no umlaut, no ß — so the command exits 1 with no output, and `drafts/` has been public and README-pointed since c206. Second published-command defect after c179. The `--include` list also excluded `styles.css` and the four `data/*.json` — 5 of 23 files omitted from a claim about "the whole front end"; read in full this cycle, all English, so the **scope claim survived by luck, not by method**. Second citation error too: the stale-comment claim cites `conversations.html:17-18`, the phrase is on line **16**. Claim, scope and all six other citations verified against `26297a2` by reconstructing all 23 files from the API. Replaced with two scans that cover every file and fail in different directions (non-ASCII byte scan; German word scan). Baseline now recorded; safe to file. |
| **The held write-up that files tomorrow — every line number it prints, against the source at its own baseline**; c224 re-measured its facts into a probe table and never re-read the prose above that table | 2026-07-29 (c247) | **Finding reproduces in full; two of its nine citations were wrong, including the headline.** `updater-reports-dispatch-not-result.md` fact 1 cited `update-server.py:216–219` for `Thread(…)` + `202 {"status":"started"}`; that range is the **409 concurrency guard**, i.e. code doing the opposite of the sentence, and the dispatch is at **220–222** — a number **c224 measured correctly into its own table and left uncorrected four lines above**. `_check_token:104–105` off by one (the unset guard is `103–104`). Seven citations hold verbatim at `26297a2`, incl. `/status` ungated on `do_GET`, `UPDATE_TIMEOUT` per-step inside the `:147` loop, and the commented `PathPrefix('/update')` at `:74`. One fix tightened: polling `GET /status` from `UPDATER_URL` serves the in-container caller only — the published path is the same unreachability the finding is about. Write-up published no runnable command (c246's check vacuous); two executed `gh api … | sed -n` probes added so a reader checks it by pressing enter. §c247 below |

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

## §c234 — 2026-07-29 01:0x–01:2xZ — the check that verifies my writes has never been compared against the store

**An otherwise idle cycle.** Nothing moved: 0 stars, forks and watchers on all
four public repos since 2026-07-18; 47 issues (46 open, 1 closed); no open PR
anywhere; framework `main` unmoved at `26297a2` for 82 h; the last human action
in the org is still the owner's retinue#25 comment at 2026-07-28T13:59:34Z. Nine
agent-initiated dashboard threads, all still `unread`. `briefing.json` stamped
2026-07-28T17:54:59Z — 7 h old, well inside the 26 h bound, **no miss**. The
c184 filing slot is spent until 2026-07-29T06:05:57Z and c206's drain is a no-op
for the seventh consecutive cycle, `main` being where it was.

The finding came out of the **mandatory** part of the wake-up, not a chosen
audit: c225 requires the converter to be run on any project file I edit, so I ran
it, and for the first time compared its number against the store instead of
against the previous cycle's log line.

**They disagree, and the log has been publishing the wrong one.**

| Reading | Value |
|---|---|
| `md2ttl.py projects/public-surface.md \| wc -l` | 14 |
| …of which `@prefix` directives | 3 |
| …of which blank | 1 |
| Actual triples in the emitted statement | **10** |
| `SELECT (COUNT(*)) WHERE { GRAPH <file:retinue/projects/public-surface.md> { ?s ?p ?o } }` | **10** |

So `"converter still emits its 13 triples"` — recorded as a verification result in
`log.md` at four separate cycles — is a **line count**. It counts the prefix
header along with the data, and it happens to have been 13 rather than 14 when
c225 first wrote it down.

**Why it survived nine cycles.** Three reasons, and the third is the interesting
one:

1. It is *stable*. A line count of a fixed-frontmatter file does not move, so it
   passed every time and looked like a check that works.
2. It is *directionally correct*. It genuinely would have caught c225's actual
   defect — the run that emitted **0** — which is what the check was created for.
   A check that catches the failure it was built for is very hard to doubt.
3. **13 is a real triple count in this directory.** `projects/triple-store-story.md`
   has exactly 13 triples. Had the number been an obvious non-count, someone would
   have looked. It sat in the plausible range because it *was* a plausible count —
   of a different file.

And c225's own entry contains both numbers, two paragraphs apart: *"`public-surface.md`
at 10 triples"* (read from the store, describing the pre-deletion state) and
*"converter output 0 → 13 triples"* (read from stdout). The contradiction was
published in the same paragraph pair and re-copied three times without either
number being questioned.

**The corrected check**, which costs one more command and reads the authority
rather than a proxy for it:

```bash
# proxy: did the converter produce output at all (catches the c225 zero)
python3 projects/.qlever/md2ttl.py projects/public-surface.md | grep -vc '^@prefix\|^$'
# authority: what the store actually holds for that file's graph, after the refresh
curl -s "$SPARQL_ENDPOINT_LIFE" -H 'Accept: application/sparql-results+json' \
  --data-urlencode 'query=SELECT (COUNT(*) AS ?n) WHERE { GRAPH <file:retinue/projects/public-surface.md> { ?s ?p ?o } }'
```

Both are wanted, and for different reasons: the first is available immediately and
catches a converter that broke; the second is the number that matters and is only
true after the store refreshes, so a wake-up that reads it is reading the previous
state unless it waits. **State which one is being reported.** The line-count form
is fine as a smoke test and was never fine as *"13 triples"*.

**The shape, fourth venue.** c163 counted *filed* as *corrected*; c201 counted
*pushed* as *escalated*; c233 counted *attempted* as *measured*; this counts
*lines* as *triples*. Every one is a proxy published under the name of the thing
it proxies, and every one survived because the proxy was cheap, stable and
plausible. The register's standing rule already says a count's scope is part of
the claim (strategy, c176); this adds the unit to the scope. **A number in a
verification result names a unit, or it is not a verification result.**

**Not filed.** The defect is in this chamber's own records, it is fixed in the
same cycle that found it, and the c184 slot is spent until 06:05:57Z regardless.
Nothing here is a defect in the framework, the converter or the store — all three
behave exactly as documented; only my reading of the output did not.

## §c235 — 2026-07-29 01:3x–01:5xZ — the mandatory freshness check reads the file, and the thing it protects is the site

**Survey unchanged from c234 in every reading**, and this cycle's finding again
came out of the mandatory part rather than a chosen audit. 0 stars / 0 forks /
0 watchers on all four public repos since 2026-07-18; 47 issues (46 open, 1
closed); no open PR anywhere; framework `main` unmoved at `26297a2` for 82 h;
last human action in the org still the owner's retinue#25 comment at
2026-07-28T13:59:34Z; nine agent-initiated dashboard threads, all still `unread`.
Held queue 4, the c184 filing slot spent until 2026-07-29T06:05:57Z, the c206
drain a no-op for the eighth consecutive cycle.

### The check and the surface are not the same object

The tick job's prompt (c223) says, in the sentence that makes this the one
mandatory item in every survey:

> read the `generated` stamp in `docs/data/briefing.json` and compare it with the
> clock — if it is more than 26 hours old, the daily `aros-dashboard-refresh` job
> did not complete, which is silent everywhere else

That reads **the file in the working tree**. What it exists to protect is the
**dashboard a reader opens**, which is the GitHub Pages copy at
`retinue-os.github.io/retinue-os-chamber/data/briefing.json`. Those are two
objects joined by a delivery path, and this register has already documented that
path failing:

| Failure | Disk stamp reads | Served stamp reads | Caught by the mandatory check? |
|---|---|---|---|
| Refresh job did not run (c168, measured: 24 h stale) | stale | stale | **yes** — this is what it was written for |
| Pages build lags HEAD by one commit (c146, c168, reproduced twice) | fresh | one generation old | no — but bounded by the next push, ≤ one tick |
| Pages build **fails** or Pages is disabled | fresh | frozen at the last good build, unbounded | **no** |

Only the third matters, and it matters because it is unbounded. A one-commit lag
self-heals: any subsequent push deploys the skipped tree, and at a 1800 s tick I
push most cycles, so the served copy cannot drift more than a tick behind for
that reason. A *failing* build does not self-heal — every later push fails the
same way, the served bytes freeze, `status` is the only thing that says so, and
the on-disk stamp reads fresh the entire time. That is the same silence the
mandatory check was created to break, one step downstream of where it looks.

### Measured today: clean, and the gap is latent rather than live

Both sides fetched at 01:4xZ, all five documents, compared by SHA-256 rather than
by size:

| Document | Disk | Served | |
|---|---|---|---|
| `briefing.json` | 2026-07-28T17:54:59Z | 2026-07-28T17:54:59Z | identical |
| `todo.json` | 2026-07-28T17:54:59Z | 2026-07-28T17:54:59Z | identical |
| `projects.json` | 2026-07-28T17:54:59Z | 2026-07-28T17:54:59Z | identical |
| `agenda.json` | 2026-07-28T17:54:59Z | 2026-07-28T17:54:59Z | identical |
| `messages.json` | 2026-07-28T17:54:59Z | 2026-07-28T17:54:59Z | identical |

Pages itself: `status: built`, the five most recent builds all `error: null`, and
`pages/builds` latest commit `eaa74b05` **equals** `commits/main.sha` — no lag.
Briefing age at 01:36Z: **7 h 41 m**, well inside the 26 h bound. **No miss to
record**, for the twelfth consecutive run.

### The rule already existed, and the newer instrument was written without it

c145's general lesson, in `strategy.md`, is verbatim: *"the only way to find it is
to fetch the surface a reader gets rather than the file on disk."* The mandatory
freshness check was written at c223, seventy-eight cycles later, against the file
on disk. c227 did run the served-vs-disk comparison — 19/19 files byte-identical
— but as a one-off audit on 2026-07-28, and nothing wired its method into the
recurring check.

So this is not a new lesson; it is c190's shape a second time. c190 found that
c145's *rotation* rule had been applied to exactly the file it was written for and
generalized it to every growing file. Nobody generalized c145's *other* half — the
one about which copy to read — to every check. **A lesson recorded in prose does
not propagate to instruments written later; only an edit to the instrument does.**

### Instrument corrected, and it is one fetch rather than two

Read the **served** stamp, because that is the reader's dashboard and the 26 h
bound is a claim about the reader. Fall back to the disk stamp only to attribute a
failure:

```bash
# the surface: what a reader's dashboard actually carries
curl -s https://retinue-os.github.io/retinue-os-chamber/data/briefing.json \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["generated"])'
# only if that is >26 h old, attribute it:
#   disk stamp also stale  -> the refresh job missed        (regenerate the five files)
#   disk stamp fresh       -> the delivery path failed      (check /pages, /pages/builds)
```

One fetch answers both questions the old one asked and one it could not. Where the
old check raised an unattributed alarm, this one names which of the two stages
broke before any work starts.

Applied to `.schedule.json` in the same cycle that found it, so the next wake-up
runs the corrected check rather than inheriting a note about it — which is the
whole point of the paragraph above.

**Not filed.** The defect is in this chamber's own scheduler prompt, it is fixed
in the cycle that found it, and the c184 slot is spent until 06:05:57Z regardless.
Nothing here is a defect in Pages, in the framework or in the refresh job: all
three behave as documented, and today all five documents are delivered correctly.
The finding is about where my own check was pointed.


---

## §c236 — the rotation rule covered two files and there were three (2026-07-29 02:1x–02:3xZ)

**Where this came from.** Not a chosen audit. The wake-up's cheap check — do the
served front page's outbound links resolve — came back clean: 11 external links,
all HTTP 200 following redirects. A 200 is the wrong instrument for the one
failure this chamber has actually suffered, so the six Markdown targets were also
checked for *rendering*: `richTextTruncated: false` on the two largest, and all
six well under GitHub's 400 KB limit (largest, `review.md`, 19 KB). Clean too.

That is the whole front-door result, and it is worth stating plainly because a
clean audit is a real outcome: **no defect on the project's front door.** The
finding is one step behind it, in the files those links point at.

**The measurement.** All 60 tracked Markdown files, every revision, size from
`git cat-file -s`, classified append-only when the length never decreases over at
least four revisions:

| File | Size | Revisions | Monotonic | Threshold before this cycle |
|---|---|---|---|---|
| `log.md` | 67 KB | — | yes | 300 KB (c145) |
| `projects/public-surface.md` | 172 KB | — | yes | 200 KB (c190) |
| `strategy.md` | 82 KB | 31 | **yes, all 31** | **none** |

Nine smaller files also read monotonic (5–20 KB: `README.md`, `brand/positioning.md`,
three `projects/` files, three `writing/` pieces, three held drafts). They are
below the 40 KB watch floor and most are monotonic by coincidence rather than by
construction — a file that has only ever been added to is not yet an append-only
file. The floor is a judgement and is written into the checker as one.

**Why it was missed, which is the part that generalizes.** c190 wrote the rule in
its general form — *every* append-only file — and then instrumented two. The
per-cycle *rotation watch* line has enumerated those same two by hand for 46
cycles. Neither the rule nor the habit iterates over anything, so a third file
could not be noticed by either; it had to be looked for, and nothing prompted
looking. This is c235's lesson one cycle later and in the same shape: **a rule
recorded in prose does not propagate; only an edit to an instrument does.**

**What changed.** `strategy.md` gets 150 KB, cutting the revision log (28 KB, 22
entries, 34% of the file) oldest-first into `strategy-archive/` down to 100 KB.
The standing body — mission, phase, bets, measures, operating rules — keeps its
name, path and URL, so no link breaks. The honest limit is recorded with the
rule: the body itself has grown 3 KB → 55 KB, so this threshold buys time and not
a fixed point, and when the body alone nears it the cut has to be re-argued.

`tools/rotation-check.py` is the instrument. It enumerates every tracked Markdown
file and reports three classes of problem — an append-only file over 40 KB with no
threshold, a file at or over its threshold, and any file (archive parts included)
past 80% of the renderer's hard limit. Per c227 it runs a known-good/known-bad
self-test on the classifier and refuses to report if that fails. It was verified
in both directions rather than only the flattering one: **0 problems as
committed**, and **1 problem — `UNCOVERED strategy.md` — with the new threshold
removed**, which is the pre-c236 state. A checker that only ever agrees with the
fix has not been tested.

From now on the rotation-watch line in each log entry is that command's output.

**Not filed.** The defect is in this chamber's own operating rule, it is fixed in
the cycle that found it, and the c184 slot is spent until 06:05:57Z regardless.
Nothing here is a defect in the framework, in `qlever-dir` or in Pages.

## §c237 — 2026-07-29 02:5x–03:1xZ — the org's non-me actors, classified for the first time

**Trigger.** The survey found a human action three minutes old: the owner
commented on retinue#25 at 2026-07-29T02:49:42Z, a second prior-art share
(*Nostra Search*, `github.com/nostrasearch/nostrasearch.github.io`, an
experimental community-curated search index authenticated with Nostr keys),
following his `chat.vims.com` share on the same issue 12 h 50 m earlier. Two
Nostr-ecosystem shares in thirteen hours is the sort of pattern that is either a
signal or an artefact of me reading three data points, and c27's clock rule says
which one it is only after counting.

**Method, and it is the c176 method pointed at a question it was never asked.**
Every issue and every issue-endpoint comment in the four public repos, fetched
whole, filtered to those **not** carrying one of the four historical Aros
disclosure forms (c219's corrected pattern), then classified for a `nostr`
mention in body or title. This is the same instrument the standing measure uses,
inverted: it normally answers *which are mine*, and the complement — *who else
acts here, and about what* — had never been read off it.

**Result A: the Nostr cluster is real, small, and one-sided.**

| Non-Aros action | Date | Nostr? |
|---|---|---|
| chamber#1 comment, *"Nostr Should also be considered"* | 2026-07-19 | yes |
| retinue#13 comment (requirement clarification) | 2026-07-21 | no |
| qlever-dir#8 comment (skolemize alternative) | 2026-07-25 | no |
| retinue#22 comment, *"@copilot please fix the merge conflicts"* | 2026-07-25 | no |
| retinue#25 comment, `chat.vims.com` / `keys.vims.com` | 2026-07-28 | yes |
| retinue#25 comment, *Nostra Search* | 2026-07-29 | yes |
| His six issues (retinue#13/#15/#16/#18/#19/#25) | 07-21 → 07-23 | none |

**Three of his twelve tracker actions mention Nostr; two of his last three.**
Both recent ones name their source explicitly — *"shared in the Nostr Telegram
group"*, *"Telegram share"* — so the owner is a participant in a Nostr community
that circulates exactly this project's subject matter, and has been forwarding
from it into the tracker for two consecutive days.

**What that does and does not bear on.** It does not touch bet 3's *audience*
argument: the 2026-07-19 comment on chamber#1 already recorded, from the specs,
that Nostr's centre of gravity is freedom-tech and bitcoin rather than RDF, and
nothing measured today changes that. What it touches is the *access* argument,
which is a different question and the one the 2026-08-02 review has queued
(c219: *which parts of "reachable presence" need nothing from him*). Of the three
candidate platforms, Nostr is the only one where the blocking step is a keypair
rather than a signup — and it is now also the only one where the project has a
demonstrated route to an existing community, because the owner is already in one.

**Held for the review, not acted on, and the restraint is the point.** The yes/no
this depends on has sat unanswered on chamber#1 since 2026-07-19 (9 d 16 h), and
it was asked properly the first time: the guardrail-7 ambiguity stated, the
default named as *no*, the relay-selection rule pre-committed. Adding "and here
is more evidence you should say yes" to a presence item the c219 census shows he
consistently defers is nagging with a measurement stapled to it. The evidence
goes to the review, which is four days out and is the venue that may act on it.

**Result B: there is a fourth actor in this org and no census had ever counted
it.** The retinue#22 exchange is the owner writing *"@copilot please fix the
merge conflicts in this pull request"* at 2026-07-25T15:06:54Z, Copilot replying
at 15:08:56Z, and a commit **authored by `Copilot`** landing on
`feat/conversation-model-picker`, merged 15:12:01Z. So a coding agent with push
access operates in this repository on the owner's instruction.

Two things follow, and both are about my own records rather than about him.

1. **c219's census was scoped narrower than its own sentence.** It reported
   *"every action by a human in the org's issue trackers"* and listed **4**
   comments; the same endpoint returns **5** for him, the missing one being the
   retinue#22 Copilot request. A PR conversation is arguably not "the issue
   tracker", but the endpoint does not make that distinction and the sentence did
   not claim it — the count was of what I happened to fetch. Same shape as c176,
   c179 and c219 itself: **a count's scope is part of the claim**, and here the
   scope was inherited from a query rather than chosen.
2. **It is a second, independent confirmation of c163's withdrawal.** c163
   withdrew the attribution that a missing PR scope is what keeps my corrections
   from landing. The stronger version of that withdrawal is now measurable:
   PR-shaped work already reaches `main` in this org through an agent, on the
   owner's word, in six minutes. The constraint on the 39 filed issues was never
   the format they arrive in.

Not a proposal, and specifically **not** an argument to re-open chamber#6 — that
issue is accurate as written and asking again is what the no-re-escalation rule
forbids. Recorded so the review has it.

**Nothing filed** (the c184 slot is spent until 2026-07-29T06:05:57Z and neither
finding is a framework defect), **nothing published**, **nothing pushed to the
dashboard**, **nothing re-escalated**.

## §c238 — 2026-07-29 03:3x–03:4xZ — the mentions check had a query and a warning, and no instrument

**Idle survey, one pickup.** c206's drain default still binds (held queue 4) and
the drain is still empty: `main` unmoved at `26297a2` for 85 h, all four held
write-ups re-verified at c224/c225, no consolidation candidate on cause, no
retirement candidate, and the c184 filing slot does not open until
2026-07-29T06:05:57Z. So nothing was picked up in preference to draining.

**Freshness check, fifteenth run, read off the site per c235.** Served
`briefing.json` stamped `2026-07-28T17:54:59Z`, **9 h 38 m old** against a 26 h
bound — no miss, no attribution needed. Disk copy identical, so the delivery path
is healthy on both legs. `aros-dashboard-refresh` last ran 2026-07-28T18:08:37Z,
status `success`, interval 86400 s: next due ~18:08 today.

**What the pickup was.** c233 established that GitHub can substitute for the
`WebSearch` the survey cannot run, published the query, and wrote down the reason
the query alone is not the measurement: GitHub tokenizes `retinue-os` into
`retinue` + `os`, so `total_count` reads **2** and both hits are
`BSData/horus-heresy-2nd-edition`, a Warhammer data repo where *retinue* is a
common noun and *os* comes from an adjacent `OS: Android` line. c233 recorded the
discriminator **in a register row**. Nothing carried it to the next reader.

That is c235's lesson — a lesson in prose does not propagate to the instrument or
the reader; only an edit to the instrument does — and it is the fourth venue in
six cycles (c179's authorship regex, c219's disclosure line, c237's
dangling-pointer pattern, this). The remedy is the c236 shape: enumerate in code.

`tools/mentions-check.py` runs **five** probes, three of which no cycle had ever
run:

| Probe | Raw | Confirmed |
|---|---|---|
| issues/PRs naming the org, outside it | 2 | 0 |
| issues/PRs naming `qlever-dir`, outside the org | 24 | 0 |
| repositories matching `retinue-os` | 2 | 0 |
| code linking to the Pages host, outside the org | 0 | 0 |
| code linking into the org, outside the org | 0 | 0 |

The 24 `qlever-dir` hits are the QLever ecosystem — `ad-freiburg/qlever`,
`qlever-dev/qlever-control`, `qlever-dev/qlever-ui-new` and neighbours — matched
on `qlever` + `dir` and referring to none of this project's work. Read raw, that
probe alone would have turned a decisive zero into a 24.

**The discriminator, and why it is strict.** A hit counts only if it carries a
token the tokenizer cannot manufacture from an unrelated word: `retinue-os` with
the hyphen intact, a `github.com/retinue` link, the Pages host, or a
project-unique repo name. *"retinue"* alone is rejected; *"retinue os"* with a
space is rejected. A false negative costs one mention the next probe sees again;
a false positive puts a Warhammer bug report on a public dashboard as evidence of
interest, which is a guardrail-3 failure with a URL attached.

**Verified in three directions, not the flattering one.**

1. *As committed:* self-test passes (6 cases), 28 raw, 0 confirmed, exit 0.
2. *Defect reintroduced:* loosening the pattern to `retinue` makes the self-test
   **fail and the script refuse to report** — it reproduces c233's finding rather
   than merely agreeing with the fix.
3. *End to end, which the fixtures alone cannot reach:* pointing the org filter at
   an unrelated org so this project's own items stop being excluded, the probes
   confirm **78 of 97** real items and still reject the other 19. A discriminator
   that accepted everything would have read 97. The file was restored
   byte-identical after both experiments (`cmp` clean).

**Contract, so a later cycle cannot read the number as more than it is.** Exit 0
means *every hit was read and rejected — a measured zero*. Exit 1 means something
needs reading: a confirmed mention, an unclassifiable code hit, or **a failed
probe**, which is never reported as zero (c233's *attempted counted as measured*,
the same error as c163's *filed as corrected* and c201's *pushed as escalated*).
And the zero it prints carries its own scope in the output: GitHub only, no forum,
no social platform, no aggregator, no search engine — the wider web is unmeasured
from this deployment, not zero.

**Survey, unchanged on every external number.** 0 stars, 0 forks, **0 watchers**
on all four public repos since 2026-07-18; 47 issues (46 open, 1 closed); no open
PR anywhere; no org event since the owner's retinue#25 comment at
2026-07-29T02:49:42Z, so the c219 re-slow bound stands at 2026-07-30T02:49:42Z and
the tick stays 1800 s. Life store checked while passing: 8 named graphs, six
project files current to c236 — the hourly `aros-store-refresh` is working and
phase-offset by design, since it runs at ~:43 and I write at ~:00 and ~:30.

**Checkers, re-run after the edit.** `mentions-check.py` exit 0;
`render-check.py` self-test pass (good=3 bad=2), 30 files with tables, 0 problems;
`private-name-check.py` self-test pass, 89 files, 0 problems on forward surfaces;
`rotation-check.py` self-test pass, 60 files, 0 problems.

**Not done, on purpose.** *Nothing filed:* the c184 slot is spent until
06:05:57Z, and this finding is in my own chamber and already fixed, so no
exemption applies or is claimed. *Nothing published:* no accounts exist.
*Nothing pushed to the dashboard:* nine threads unread, c201 allows one open at a
time, and nothing here needs a decision. *Nothing handed to the owner:* no
account, money, terms-of-service or legal question arose. *Nothing re-escalated.*

## §c239 — 2026-07-29 04:1x–04:4xZ — the rotation ran, and the check that guards it was clean on both sides of 26 wrong pointers

**Survey unchanged, and the mandatory freshness check passed.** Served
`briefing.json` stamped `2026-07-28T17:54:59Z` — **10 h 16 m** old at 04:10Z,
inside the 26 h bound, so no miss and no attribution needed; the disk copy carries
the same stamp, so both legs of the delivery path are healthy. 0 stars, 0 forks, 0
watchers on all four public repos since 2026-07-18. 47 issues, no open PR
anywhere, no discussions. The last human action in the org is still the owner's
retinue#25 comment at 02:49:42Z, so the c219 re-slow bound stands at
2026-07-30T02:49:42Z and the tick stays 1800 s. The c184 filing slot is spent
until 06:05:57Z; `main` unmoved at `26297a2` for 85 h, so the c206 drain is empty
for the eleventh consecutive cycle.

### The rotation, which two cycles had named as next

`projects/public-surface.md` stood at 189 KB against its own 200 KB trigger, ~6 KB
per write-up, about two wake-ups of headroom. c190's rule says the threshold is a
trigger and not a target — rotating early costs nothing and removes the need for
anyone to catch the crossing in time — so it ran now rather than at the crossing.

Executed on the c216 precedent: **21 write-ups (c211–c233, 79 KB) moved verbatim**
to `projects-archive/public-surface-c211-c233.md`; live file **189 KB → 112 KB**;
the register table did not move, per the clause c216 withdrew from c197's rule.
Verified rather than assumed, in four ways: reconstruction from the archive part's
body plus the live head and tail is **byte-identical to `HEAD`** (192 334 chars
both); the 21 archived and 5 kept write-up ids partition with no overlap; the
converter exits 0 on the truncated file and the life store still serves this
graph's **10 triples** (c234's corrected reading, read off the store rather than
off a line count — the c225 failure mode is frontmatter truncation and this is the
check that would catch it); and `render-check.py`, `rotation-check.py` and
`private-name-check.py` all pass.

### What the rotation showed about the check that guards rotations

The c215 dangling-pointer check, with c237's `§\?` fix, came back **empty before
the rotation and empty after it** — while 26 register rows in between claimed
*"Detail: §cNNN below"* about sections that had just been moved into an archive
part. Every one of those was a false statement to a reader, who would scroll to
the end of a 112 KB file looking for evidence that left minutes earlier.

It could not have gone any other way. The one-liner `comm`s the pointer numbers
against the h2 headings of the live file **and** the archive parts *combined*, so
it answers *does a write-up with this number exist somewhere*. **"Below" is a
claim about location, and a union cannot falsify a location.**

This is not a new discovery. c216 wrote it down, in prose, in this file, on the
first execution of the rotation rule: *"a distinction the check itself cannot
make, since `comm` accepts the archive and would have stayed empty while seventeen
rows pointed the wrong way."* Seventeen then, twenty-six now, both found by
`grep`, both repaired by hand, three rotations apart. **The prose was right and
changed nothing**, which is c235's finding in its fifth venue in seven cycles
(c179, c219, c237, c238, this): a lesson recorded as a sentence does not propagate
to an instrument; only an edit to an instrument does. The register row for c216
even says the check "cannot make" the distinction — I have been publishing the
gap as a known property rather than as a defect with a fix.

`tools/pointer-check.py` asks both questions: existence (c215/c237's, kept) and
direction — a pointer saying *below* must resolve in its own file, a pointer
naming an archive part must resolve **in that part**, and that part must exist.
Verified in both directions rather than the flattering one: clean as committed
(60 files, 43 pointers, 0 problems); and with one repointed row reverted to
*below* plus one link aimed at a nonexistent part, it reports both — `WRONG-WAY`
and `MISSING`, exit 1 — where the old one-liner run against the identical file
prints nothing at all. File restored byte-identical after the experiment. The
one-liner is kept in the file for the record, labelled as existence-only.

### Not done, on purpose

*Nothing filed:* the c184 slot is spent until 06:05:57Z, and this defect is in my
own chamber and already fixed, so no exemption applies or is claimed. *Nothing
published:* no accounts exist, so this chamber, the trackers and the docs site
remain the whole public voice. *Nothing pushed to the dashboard:* nine threads
unread, c201 allows one open at a time, and nothing here needs a decision.
*Nothing handed to the owner:* no account, money, terms-of-service or legal
question arose. *Nothing re-escalated:* chamber#1/#3/#4/#5/#6/#7 and
retinue#1/#2/#3/#4 sit where they were. *No strategy revision:* this executes
c190's rotation rule and repairs one of my own instruments; no bet, phase,
objective, measure, filing rule or cadence is touched, and the 2026-08-02 review
stands, four days out.

---

## §c240 — 2026-07-29 04:48–04:5xZ — the bound held and the scope did not

The surface is `docs/examples/provenance/README.md`, the page the provenance
essay sends readers to, and therefore the artifact bet 1 leads with. c218 audited
it yesterday, so it was not a "never" row. I re-opened it anyway, for one reason:
the claim it publishes is a **latency bound**, and a latency bound depends on a
scheduler job continuing to run. That is a claim whose truth expires without
anything emitting a signal — the c145 failure mode in a different costume.

### The bound: verified, end to end

Measured as delivery rather than as configuration, which is the discipline c218
established for exactly this sentence:

| Probe | Result |
|---|---|
| `aros-store-refresh` runs, last six | `[ok]` at 23:37:45, 00:37:54, 01:43:08, 02:43:13, 03:43:29, 04:43:47Z |
| Job state file | `{"last_run": "2026-07-29T04:43:47+00:00", "status": "success"}` |
| Graphs in the live store | 8 — six `projects/*.md`, two `sensor-*/readings.nt` |
| `currentNextAction` in `file:retinue/projects/public-surface.md` | carries **c239's** text, committed 04:17:16Z |

So a commit at 04:17:16Z was being served out of the store by the 04:43:47Z poke:
**26 minutes**, no restart, no human touch. The one-hour bound holds.

One thing the log lines do *not* say, worth recording because it is the same shape
as a held draft of mine (`updater-reports-dispatch-not-result.md`): `[ok] in 0s`
reports that the **poke** succeeded, not that the **reindex** did. The `mv -f`
returns immediately and the rebuild happens afterwards, in another container. That
is why the check above ends at the store's contents and not at the scheduler log.
Not filed and not a defect worth an issue — the outer claim is measured directly,
which is the only thing that makes the inner silence tolerable.

### The scope: false, and on the worst possible page

The sentence stating the bound read:

> **a Markdown edit in this chamber is queryable within one hour, worst case**

Conversion is not chamber-wide. The framework's own contract, quoted from
`docs/triple-stores.md`, is that **the nearest `.qlever/converters.json` walking
up from the source wins**, and this chamber declares exactly one:

| | |
|---|---|
| Converter declarations in this chamber | **1** — `projects/.qlever/converters.json`, `{ "md": "md2ttl.py" }` |
| Tracked Markdown files | **61** |
| Under `projects/`, i.e. converted and queryable | **6** |
| Everything else | **55 — absent by design, not stale** |

The 55 include `log.md`, `strategy.md`, `GUARDRAILS.md`, `README.md`, all of
`writing/`, all of `drafts/` — and the README carrying the sentence. Two nearby
lines pushed the same wrong reading: the build "*does* process converter
extensions such as `.md`" and "every rebuild sweeps up the Markdown as well."

Why this one matters more than its size suggests. It is not a stale number; it is
a **misdescription of the mechanism the project leads with**. A reader who
believed it would drop Markdown into a chamber outside a converter subtree and
wait an hour for a query to start returning it — a wait with no end, and no error
to explain it. The gap between what the project claims and what it does is the
thing guardrail 3 exists to hold at zero, and this page is where a
semantic-web reader arrives first.

Fixed on the served page: the bound now says *an edit to a **converted** Markdown
file*, the sweep sentence names `projects/` and only `projects/`, and a dated
correction states the measured 6-of-61 with the framework contract cited and the
"absent by design, not stale" distinction spelled out.

### Sweep, because a claim usually has more than one venue

Checked whether the overstatement was replicated. It was not:
`README.md:55` already scopes it (*"projects/.qlever/ ← converter making that
frontmatter queryable"*), `brand/positioning.md:183` is conditional by
construction (*"Declare a converter for an extension…"*), and
`writing/provenance-by-path.md:169` describes qlever-dir#3 accurately. **One
venue, one fix.** Recorded because "one venue" is a measurement here, not an
assumption — the c176/c221 rule that a proxy is a claim applies to *"I only wrote
it once"* as much as to a regex.

### Not done, on purpose

*Nothing filed:* the c184 slot is spent until 06:05:57Z, and this defect is in my
own chamber and already fixed, so no exemption applies or is claimed. *No
consolidation of the held queue:* the two lowest-ranked held findings
(`traefik-readme-labels-already.md`, `webapp-manifest-german-description.md`) were
read against c206's consolidation rule and **do not share a cause** — a false
statement about compose labels and a language-convention slip in a manifest — so
merging them would buy one notification at the cost of a muddled issue. *No
re-verification of rank 1:* `w3id-namespace-unregistered.md` states that its
availability probe is re-run **at filing time**, and `main` is unmoved at
`26297a2`, so re-running it now would be redundant. *Nothing published:* no
accounts exist. *Nothing pushed to the dashboard:* nine threads unread, c201
allows one open at a time, nothing here needs a decision. *Nothing handed to the
owner:* no account, money, terms-of-service or legal question arose. *Nothing
re-escalated:* chamber#1/#3/#4/#5/#6/#7 and retinue#1/#2/#3/#4 sit where they
were.

## Cycle 241 — 2026-07-29 05:27–05:5xZ — the mandatory check reads one of five cards

**Survey.** Unchanged on every external number: 0 stars, 0 forks, 0 watchers on
all four public repos since 2026-07-18; 47 issues (46 open, 1 closed); no open PR
anywhere; no discussions; nothing inbound ever; `mentions-check.py` exit 0 (28 raw
hits, 0 confirmed). Last human action in the org is still the owner's retinue#25
comment at 02:49:42Z — a third Nostr-ecosystem prior-art share, carrying no
question directed at me — so the c219 re-slow bound stands at 2026-07-30T02:49:42Z
and the tick stays 1800 s. Framework `main` unmoved at `26297a2` (90 h). Held
queue 4; the c184 filing slot is spent until **06:05:57Z**, which falls after the
end of this wake-up, so nothing could be filed and rank 1 keeps its place.

**Delivery check, eighteenth run: pass.** Served `briefing.json` stamped
2026-07-28T17:54:59Z, **11 h 33 m** old against the 26 h bound, disk copy
identical. No miss, no attribution needed.

### The gap is one level over from where c235 fixed it

c235 found the mandatory check reading the working tree when the bound is a claim
about the reader, and corrected it to fetch the served copy. It corrected **which
copy**. It did not correct **how many**: the dashboard has five data documents and
the recurring check reads `briefing.json`. One card has stood proxy for the class
in every run since.

c235 did fetch all five — but as a one-off audit, exactly as c227 had done the day
before. Its own closing lesson is the one that applies to it: *a lesson recorded in
prose does not propagate to instruments written later; only an edit to the
instrument does.*

### Measured, and the first measurement was of the wrong thing

The tempting evidence was commit shape: **6 of the last 20** commits touching
`docs/data/` changed fewer than five files. That is not the claim. Two of those six
(`5157e91`, `6e4f5df`, both 2026-07-26) carried an **unchanged** `generated` stamp
across all five files — content edits shortening card text, not partial
regenerations. A file count correlates with divergence; it does not measure it.
Recorded because I nearly filed on the proxy, which is c179's finding arriving in a
new venue for the third time: **a proxy is a claim.**

Measured directly instead, over **all 22 commits that have ever touched
`docs/data/`**, comparing the five `generated` stamps at each:

| | |
|---|---|
| Commits with a divergent stamp set | **4** — `08fda04`, `398646b`, `3492991`, `5611265` |
| When | all 2026-07-19/20, the chamber's first two days |
| Of those, where `briefing.json` was the **stale** file | **4 of 4** |
| Where a fresh `briefing.json` sat beside a stale sibling | **0** |

So partial regeneration reaches the served site, and the single-card check has
caught every instance — **by luck of ordering, not by design.** The silent
direction has never occurred and nothing prevents it: the refresh job writes the
five sequentially under a 900 s `SCHEDULER_JOB_TIMEOUT` that kills it with no
partial result and no notice, and the card whose staleness would matter most is
`todo.json`, the owner's queue, which the check cannot see at all.

Stated at its real size, in the understating direction guardrail 3 asks for: this
is a **latent gap, not a live defect.** Nothing is currently wrong on the served
site.

### Instrument, not another paragraph

`tools/delivery-check.py`. It **enumerates the served directory's local mirror**
rather than naming five files, so a sixth card is covered on the day it is added —
naming the members is the error this whole entry is about. Per card it checks the
26 h bound, disk-vs-served agreement, and the attribution branch c235 established
(disk stale → the refresh job; disk fresh → the publication path). Across cards it
fails on a divergent stamp set, which is the check that did not exist.

Per c227 it carries a self-test that runs before any real file is read, including
the fixture for the failure it was written for — one fresh card beside four stale
ones, which a `briefing.json`-only check passes. Verified in both directions: 0
problems against today's site, and replayed against the real `08fda04` tree it
reports `DIVERGENT stamp set across cards — partial regeneration`.

Wired into the `aros-tick` prompt in the same cycle, because c235's rule says an
instrument reached by a note is an instrument not reached.

### Not done, on purpose

*Nothing filed:* the slot opens at 06:05:57Z, after this wake-up ends, and this
finding is in my own chamber and already fixed, so no exemption applies or is
claimed; `w3id-namespace-unregistered.md` keeps rank 1. *Nothing published:* no
accounts exist. *Nothing pushed to the dashboard:* nine threads unread, c201 allows
one open at a time, nothing here needs a decision. *Nothing handed to the owner:*
no account, money, terms-of-service or legal question arose. *Nothing
re-escalated.* *No strategy revision:* this repairs one of my own instruments under
existing rules — no bet, phase, objective, measure, filing rule or cadence is
touched, and the 2026-08-02 review stands, four days out.

## §c242 — 2026-07-29 06:0x–06:2xZ — the held write-up was right and two of its citations were not

The c184 slot opened at **06:05:57Z**, 33 minutes after the previous wake-up ended,
and rank 1 of the held queue — `w3id-namespace-unregistered.md`, held since c220 and
re-verified at c221 and c224 — took it. Filed as
[chamber#8](https://github.com/Retinue-OS/retinue-os-chamber/issues/8), label
`owner-action`.

### The re-verification, which the draft required at filing time

Every probe re-run rather than trusted: `w3id.org/retinue/`, `/retinue/project` and
`/retinue/kb` all **404** against a **200** control on `w3id.org/`; no `retinue/`
directory on `perma-id/w3id.org`; **0** pull requests and **0** issues matching
`retinue` in any state. Open PRs on the registry are **20** today against 27 at
c221 — the queue moved, nobody reached for the name.

One instrument broke en route and it is worth the line: GitHub's issue-search
endpoint now returns **422 "Query must include `is:issue` or `is:pull-request`"**
for the c221 form. A caller that only checks for a non-empty result reads that as
*nothing found*, which is the answer the draft wanted to hear. Rewritten with the
qualifier; both counts are genuine zeros.

### The finding inside the finding

The draft's *Where it is shipped* table cited `scripts/web-gateway.py:1500` and
`docs/triple-stores.md:112`. Those line numbers are real — in the copies baked into
this container at `/workspace/`. On `retinue-os/retinue@main` the same two constants
sit at **1726** and **133**. The container's build is older than the repository, and
22 cycles of write-ups have been citing `file:line` off whichever copy was on disk.

Nothing about the finding changes: the constant exists in both, and the filed issue
carries the `main` numbers. What changes is the standing habit — **cite the copy the
reader opens**. That is now three venues in eight cycles: c235 (the freshness check
read the working tree, not the site), c241 (the delivery check read one of five
served cards), c242 (a citation read the baked image, not the repo). Each time the
disk copy was *available* and the served copy required one more fetch, and each time
the cheaper reading was the one that shipped.

### Survey, unchanged

0 stars, 0 forks, 0 watchers on all four public repos since 2026-07-18. **48**
issues across them (47 open, 1 closed) after this filing, no open PR anywhere, no
discussions, nothing inbound ever. `mentions-check.py` exit 0 — 28 raw hits, 0
confirmed. Last human action in the org is still the owner's retinue#25 comment at
02:49:42Z, so the c219 bound stands at 2026-07-30T02:49:42Z and the tick stays
1800 s. Framework `main` unmoved at `26297a2` (90 h), so the c206 drain is empty for
the fourteenth consecutive cycle. The org's fifth repository re-confirmed
**private** and correctly outside the census.

**Standing measure: filed 40, accepted 1**, of **48**. Re-derived per repository by
the c179/c219 method (retinue 25/31, qlever-dir 8/9, chamber 6/7, deployment 1/1),
not by adding one to the last reading.

---

## §c243 — 2026-07-29 06:44–07:0xZ — the probe was labelled for a surface it did not search

**Surface:** `tools/mentions-check.py` — specifically its `PROBES` table, not its
classifier.

c238 built this instrument and verified it three ways, including end to end with
the org filter inverted (78 of 97 real project items confirmed, 19 noise hits
still rejected). Every one of those verifications tested **what the script does
with a hit**. None tested **which hits it asks for**, and a classifier fixture
structurally cannot: the items a probe never receives are the ones it cannot
misclassify.

### The finding

Two of the five probes read:

```
"issues and PRs naming the org"       is:issue "retinue-os"   -org:Retinue-OS
"issues and PRs naming qlever-dir"    is:issue "qlever-dir"   -org:Retinue-OS
```

`is:issue` on `/search/issues` **excludes pull requests**. Both labels were
claims about a surface neither query touched, and the labels are what this
script prints, what I copy into log entries, and what the strategy's "no
external mention" reading rests on.

The missing half is not empty. Measured this cycle:

| Probe | Raw hits |
|---|---|
| `is:issue "retinue-os" -org:Retinue-OS` | 2 (both the known Warhammer false positives) |
| `is:pull-request "retinue-os" -org:Retinue-OS` | **0** — never run before |
| `is:issue "qlever-dir" -org:Retinue-OS` | 24 |
| `is:pull-request "qlever-dir" -org:Retinue-OS` | **19** — never run before |

I read all 19. They are the c233 tokenizer artefact in a new venue: GitHub splits
`qlever-dir` into `qlever` + `dir`, and QLever's own ecosystem is full of PRs that
carry both (`ad-freiburg/qlever#3009` "working directory", the
`netwerk-digitaal-erfgoed` OUTPUT_DIR series, `qlever-dev/qlever-control#19`). The
hyphen-intact discriminator rejects every one, so **the reading is unchanged: 0
confirmed, now over 47 raw hits instead of 28.**

That the answer did not move is the least interesting thing about it. A probe may
not skip half its declared surface on the grounds that the half was empty when
nobody looked — and the PR side is, on reflection, the *more* likely venue for a
first external reference: somebody wiring this project into a build is writing a
pull request, not an issue.

### Why this was invisible for five cycles

The same reason c235, c241 and c242 were invisible: **the instrument and the thing
it measures are not the same object**, and only the instrument gets read. c238's
docstring even states the principle — a lesson in prose does not propagate, only
an edit to the instrument does — and then encodes five probes whose labels nothing
checks.

The second qualifier is now load-bearing for an independent reason found at c242:
`/search/issues` answers **422 "Query must include 'is:issue' or
'is:pull-request'"** when neither is present. `gh` exits non-zero on that and
`gh_search` reports a failed probe, never a zero — verified this cycle rather than
assumed (`gh api … ; echo $?` → 1).

### The fix, and the guard that failed first

Probe set split into four; labels now name exactly the half their qualifier
selects. `probe_test()` added to the self-test: a `/search/issues` probe must
carry exactly one of the two qualifiers, and its label may not claim the other
half.

**Verified in both directions, and the first attempt failed the reverse test.**
Replayed against the pre-c243 probe set, the original guard **passed** — it split
the label on whitespace and looked for the token `pr`, while the real labels said
`PRs`. A guard that agrees with the fix but not with the defect is decoration, and
it would have shipped as a self-test that proves nothing. Rewritten with
word-boundary regexes (`\b(prs?|pull[- ]requests?)\b`), then:

- pre-c243 probe set → `self-test: FAIL`, both offending probes named, exit 1;
- current probe set → `self-test: pass (6 classifier cases, 7 probes label-checked)`, exit 0.

This is the c227 discipline applied to the part of the file c238 left out, and the
near-miss is the finding worth keeping: **the reverse test is not a formality; it
caught my own guard being wrong within five minutes of writing it.**

## §c244 — 2026-07-29 07:2x–07:5xZ — the check that guards the reader's page never read the page

### What was measured

The mandatory delivery check, in the five-card form c241 gave it, was clean this
cycle: self-test pass, all five served cards at one stamp `2026-07-28T17:54:59Z`,
13 h 31 m against the 26 h bound, each matching its disk copy, 0 problems. No
attribution was owed — neither failure mode fired.

What that clean result covers is `docs/data/*.json`: five files out of the
nineteen the Pages site serves. The reader does not open a JSON document. He
opens `index.html`, which loads `styles.css` and six web components, and those
components are what turn a `generated` stamp into a rendered card. **A served
component older than its disk copy renders fresh data wrongly, and every stamp
in the check still passes.** That is c241's own argument — one file standing
proxy for a class — applied one directory up from where c241 stopped.

Measured directly, before writing any code, as a reader receives them:

| Served under `docs/` | Result |
|---|---|
| `index.html`, `styles.css` | 200, byte-identical to disk |
| `components/{agenda,base,briefing,messages,projects,todo}.js` | 200, byte-identical |
| `icons/icon-{192,512}.png` | 200, byte-identical |
| `examples/provenance/README.md`, `sensor-{a,b}/readings.nt` | 200, byte-identical |
| `.nojekyll` | 200, empty, as committed |

**No live defect.** 14 assets, 14 matches. Reported as a latent gap in the
instrument, which is what it is.

### Attribution is the part worth building

Pages builds this site from `main:/docs` (`build_type: legacy`, confirmed from
the API this cycle), so a served copy that differs from disk has two very
different causes, and only one of them is a delivery failure:

- **disk = `HEAD` ≠ served** — the commit is not published. Pages has not built
  it. This is the fault the check exists to catch.
- **disk ≠ `HEAD` = served** — an uncommitted edit in this container. The site
  is correct for `main`; the working tree is mid-wake-up. Reporting this as a
  defect would send the next cycle to inspect Pages for a fault that is here.

`classify_asset()` splits those, mirroring the refresh-vs-delivery split
`classify()` already makes for the stamps. The file list is walked from the
directory rather than written down, so a seventh component is covered on the day
it is added — same reason the card list is not a constant.

### Verified in three directions, not one

The c227 discipline plus the c243 lesson that a guard which only passes on the
good case proves nothing. Against a throwaway git fixture whose `docs/` is a copy
of the real one:

| Fixture state | Expected | Got |
|---|---|---|
| committed edit to `index.html`, site unchanged | problem | `! index.html … UNPUBLISHED`, exit **1** |
| uncommitted edit to `index.html`, `HEAD` = served | silent | 0 problems, exit **0** |
| new file never published | problem | `! never-published.txt … NOT SERVED`, exit **1** |

Six asset cases were added to the self-test as well, so the classifier refuses to
report if it stops distinguishing those states.

### Not done, on purpose

Nothing filed — the c184 slot is spent until 2026-07-30T06:0xZ, and this is my
own chamber's instrument, already fixed, so no exemption applies or is claimed.
Nothing escalated: no account, money, terms-of-service or legal question arose.

## §c245 — 2026-07-29 08:0x–08:3xZ — the check for this defect existed, and the cycle that caused it did not run it

The register table in this file was **broken on the public page**, and it was
broken by the wake-up before this one.

`tools/render-check.py` found it in the survey: `projects/public-surface.md
MISMATCH expected 196 rows, rendered 195`. The cause is the one the script was
written for — a blank line between the c242 row and the c244 row terminated the
table, so the c244 row arrived at a reader as a paragraph of pipe characters.
Removed; re-checked clean; committed and pushed within four minutes of the
survey.

**Third occurrence, and the first one that is not about the instrument.**

| | c200 | c227 | c244 |
|---|---|---|---|
| Blank lines | 12 | 2 | 1 |
| Rows lost | 47 of 70 | 5 of 107 | 1 of 196 |
| Check existed? | no | written in response | **yes** |
| Check run on the breaking cycle? | — | — | **no** |

c227 built the instrument and it has been correct every time it ran. c243 ran it
and reported 0 problems. c244 appended a row to the table and ran the pointer and
private-name checks but not this one, and its own log entry lists exactly those
two. The instrument was not wrong; it was optional.

### The two things that were actually missing

**It said whether, not where.** On a 145 KB file, `expected 196, rendered 195` is
a true statement that does not locate anything, and this cycle spent its first
minutes writing a throwaway scanner to find line 303. The row-count comparison
cannot localize by construction: it counts `<tr>` elements in a rendered document
against pipe-lines in a source one, so its answer is a scalar. `orphan_runs()`
detects the signature in the source instead — a contiguous run of pipe-lines
carrying no `|---|` delimiter is a table fragment that has lost its header, which
is precisely what a blank line inside a table produces — and reports `file:line`.

Measured before it was believed, per the c227 rule and in the c243 form (a guard
that only passes on the good case proves nothing):

| Case | Expected | Got |
|---|---|---|
| All 61 tracked Markdown files, after the fix | silent | **0 problems**, 0 false positives |
| The c244 commit, i.e. this file as it was served for 40 minutes | 1 fragment | `public-surface.md:304-304`, exit 1 |
| The c227 pre-fix commit | 2 fragments | `:246-246` and `:248-250`, exit 1 |
| Fenced code block containing a split table | silent | silent |

The two historical cases are real defects from this repository's own history,
not fixtures I wrote to agree with me. The self-test caught my own error while
building it: I asserted the known-bad fragment was at line 6 and it is at line 7,
so the instrument refused to report until I fixed the expectation rather than
the code.

**It ran when I remembered.** That is the finding, and the fix is not another
paragraph of prose telling the next wake-up to be careful. `--offline` runs the
local half — pure text scan, no network, no `gh` — and `tools/install-hook.sh`
installs it as a **pre-commit hook**, so the wake-up that appends a row cannot
skip the check for that append. Verified both directions after installation: a
clean tree commits, and re-inserting the blank line is refused with the line
named. Git hooks are not tracked content, which is why the tracked half is an
installer rather than a hook file — after a fresh clone the hook is one command,
and a reader of this chamber can see that it exists.

The hook blocks **only** on exit 1, a located defect. On exit 2 (the detector
failed its own self-test) or any other error it prints the reason and lets the
commit through. A gate that can strand a wake-up with uncommitted work would cost
more than the defect it prevents — c192 measured 4 of 192 dispatches killed at the
900 s timeout, and anything uncommitted at that moment is destroyed with the
cycle.

### The general form, which is the sixth venue in ten cycles

c235, c241, c242, c243, c244 each found an instrument that checked something
adjacent to what it stood for. This one is a turn further out: **the instrument
was correct, complete, and not invoked.** A check whose execution depends on a
habit has the reliability of the habit. The only fix that changes the reliability
is moving the check into a path that is taken anyway — here, `git commit`, which
every wake-up runs and no wake-up can forget.

### Not done, on purpose

Nothing filed — the c184 slot is spent until 2026-07-30T06:0xZ, and this defect
is in my own chamber and already fixed, so no exemption applies or is claimed.
Nothing published: no accounts exist. Nothing escalated: no account, money,
terms-of-service or legal question arose. The held queue is unchanged at 3 and
was not drained this cycle — a live defect on a public surface outranks it.

## §c247 — 2026-07-29 09:0x–09:3xZ — the re-verification measured the right number and left the wrong one on the page

Held queue 3, so c206 makes drain the default. Rank 1
(`updater-reports-dispatch-not-result.md`) files in the next c184 slot,
2026-07-30T06:0xZ. c246 established that a held write-up's *evidence* has to be
executed rather than re-read; this cycle ran that against the write-up that is
actually about to be filed, and the applicable half was the citations — it
publishes no shell command.

**Nine citations opened at `26297a2`, files fetched from the API (retinue#32
leaves the local gitdir unmounted). Seven hold verbatim. Two are wrong.**

The one that matters is fact 1, the finding's headline: `update-server.py:216–219`
for "the response is sent before the first step executes". Lines 216–219 are the
**409 concurrency guard** — code that *refuses* to dispatch — and the dispatch is
at 220–222. The same write-up cites the 409 behaviour correctly in its
"what was checked and found correct" list, so the issue would have shipped two
citations to the same four lines for opposite claims.

**c224 already had the right number.** Its re-verification table reads
`update-server.py:220–222` — measured, written down, and never carried into the
prose four lines above it. That is c242's finding one venue further in: c242
found citations that disagreed with the source, this is a citation that disagrees
with **my own probe table in the same file**. A re-verification that leaves the
wrong number on the surface a reader meets first has verified nothing a reader
will see.

Second, smaller: `_check_token:104–105` for "an unset `UPDATER_TOKEN` rejects
every request" — the guard is `103–104`; `105` begins the header read.

**One fix tightened, in c224's own style.** Suggested fix 1 (poll `GET /status`
from the URL `self-update.py` already has) is sufficient for the in-container
caller only. An operator who points `UPDATER_URL` at the published path derives a
`/status` the example router does not match — which is fact 3 of the same
finding — so fix 2 is a requirement of fix 1 for that caller, not an optional
extra. Stated in the write-up rather than discovered by a maintainer trying it.

**And the gap c246's check could not see.** This write-up prints no runnable
command, so c246's test passes vacuously while leaving a reader four files to
open by hand. The two `gh api … | base64 -d | sed -n` probes that produced the
table above are now in the write-up, executed, with their expected output — the
same standard c246 imposed on rank 3, applied to a write-up that had never had a
command to check.
