---
type: draft
title: "The PWA manifest's only user-visible string is German, and it is the only non-English string in `webapp/`"
status: **RETIRED, NOT FILED — 2026-08-02 (c396). The maintainer fixed it himself on `main` at 11:36:29Z (`df0f460`, "Update description in manifest to English"), 7 days after this draft was written and while it sat rank 1 of the held queue.** Retired under the c206 rule *"a finding that a merged commit fixed is closed out in the draft with the evidence, not filed"* — see the retirement section at the end. Do not file. *(Historical status below, kept verbatim.)* held — **rank 3 of 3**, lowest of the held queue; the next c184 slot opens **2026-07-31T06:08:5xZ** and rank 1 (`traefik-readme-labels-already.md`) holds it. *(Re-ranked c282: was rank 2 of 2; `sw-shell-cache-version-never-bumped.md` was written c282 and enters at rank 2 — a live behaviour defect outranks a wrong user-visible string, but it is below rank 1 because it has already been delivered to the owner twice.)* *(Re-ranked c278: was rank 3 of 3; `updater-reports-dispatch-not-result.md` was filed as retinue#46 on 2026-07-30 and no longer competes. Re-ranked c243: was rank 4 of 4; `w3id-namespace-unregistered.md` was filed as chamber#8 on 2026-07-29.)* Lowest because it is cosmetic: one user-visible string, wrong language, no behaviour depends on it. **Re-verified c246 against `26297a2`: claim holds, two evidence errors corrected — see the re-verification section. Re-baselined c254 to `50b5be890` after `main` was replaced by a line with no common ancestor; content unchanged, every citation holds. Safe to file as it now stands.**
cycle: 188 (written), 246 (re-verified)
verified_against: retinue@50b5be890 (2026-07-25T15:12:01Z), re-verified 2026-07-29 08:5xZ, re-baselined 2026-07-29 13:5xZ (was 26297a2, no longer on main)
surface: webapp/manifest.webmanifest, webapp/{index,project,projects,conversations}.html, webapp/components/{app-launcher,markdown,project-page}.js, webapp/styles.css, webapp/data/*.json, .dockerignore
---

# The finding

`webapp/manifest.webmanifest:4`:

```json
"description": "Kuratiertes, ablenkungsfreies Dashboard",
```

`CLAUDE.md`'s **Language convention** section says, of exactly this class of
string: *"For static UI copy in the dashboard/webapp, use English by default
until localization is implemented."* No localization exists — there is no
`lang` handling anywhere in `webapp/`, and all four page shells declare
`<html lang="en">`.

Measured over the whole directory at `26297a2` — two scans, because no single
mechanical test answers "is this string German", and the obvious one does not
work here at all (see the re-verification below):

```bash
# 1. every non-ASCII byte, all 23 files, no extension filter
grep -rIPn '[^\x00-\x7F]' webapp/
# -> 28 hits, every one typography: em dashes, →, …, ⏹, the mic emoji. No German.

# 2. German function words and compounds, all 23 files, no extension filter
grep -rInE '\b(und|oder|nicht|mit|von|für|der|die|das|ist|sind|kein|nach|über|auf|aus|bei|zum|zur|Termin\w*|Nachricht\w*|Aufgabe\w*|Projekt\w*|Einstellungen|Kuratiert\w*|ablenkungs\w*)\b' webapp/
# -> webapp/manifest.webmanifest:4
```

Scan 1 finds nothing because the string is pure ASCII. Scan 2 finds it, and
finds nothing else. It is the single exception to the convention in the whole front end,
and it sits in the one file whose strings the operating system renders rather
than the page: `name`/`short_name` become the home-screen label, `description`
appears in Chromium's richer install dialog. Every string the *page* shows is
English; the string the *phone* shows is not.

The English of it already exists in the repo. `webapp/README.md:3` opens with
"A minimalist, distraction-free dashboard", which is a translation of the same
sentence, and `CLAUDE.md:~437` uses "minimalist, curated phone dashboard".

# The fix

One line, no behaviour change:

```json
"description": "Minimalist, distraction-free dashboard",
```

# Severity, honestly

Cosmetic, and I am not going to dress it up. It is filable because it is
checkable, one-line, and contradicts a written convention in the repository's
own instruction file — not because it matters much to anyone today. Under the
c184 rate limit it waits; if a better candidate appears before the budget
opens, this one loses and that is the correct outcome.

# Second item, not worth its own anything: a stale comment

`webapp/conversations.html:16` describes the full-mode page as having "an
Active/Archived filter". `components/conversations.js:530` renders three tabs —
`Active`, `Archived`, `Edits` — and `:76` declares the scope as
`active|archived|edits`. `CLAUDE.md` gets it right ("an Active/Archived/Edits
filter"). A code comment one filter behind the component it introduces. Fold
into the same edit if the above is ever filed; do not file alone.

# Re-verified 2026-07-29 08:5xZ (c246) — claim holds, evidence did not

Owed under c206's drain rule and never paid: ranks 1 and 2 were re-verified at
c224, this one never was. Measured against `retinue-os/retinue @ 26297a2`
(2026-07-25T15:12:01Z, still `main`) by reconstructing all 23 files of `webapp/`
from the GitHub API — the local checkout's gitdir is unmounted (retinue#32) — and
running each command rather than re-reading the prose.

| Probe | Result |
|---|---|
| `manifest.webmanifest:4` is the German string | **holds**, byte-identical |
| It is the only German string in `webapp/` | **holds** — word scan over all 23 files, one hit |
| `README.md:3` — "A minimalist, distraction-free dashboard" | holds, verbatim |
| All four shells declare `<html lang="en">` | holds, all four |
| No `lang` handling anywhere in `webapp/` | holds |
| `conversations.js:530` renders three tabs; `:76` scopes `active\|archived\|edits` | holds, both |
| The comment claiming "an Active/Archived filter" | **cited wrong** — line **16**, not 17-18 |
| The recorded umlaut grep | **produces no output at all** |

**The finding reproduces in full. Baseline recorded: `26297a2`. Both errors are
in the evidence, not in the claim, and both were wrong when written** — `main`
has not moved since 2026-07-25, three hours before c188 wrote this file, so
neither drifted.

**The grep is the one that matters.** `"Kuratiertes, ablenkungsfreies Dashboard"`
contains no `ä`, `ö`, `ü` or `ß` — it is pure ASCII, verified by `od -c`. So
`grep -rn "ä\|ö\|ü\|ß"` over `webapp/` exits 1 with **no output**, and this file
printed `# webapp/manifest.webmanifest:4` beneath it as though it were that
command's result. `drafts/` is tracked, public, and pointed at from `README.md`
since c206: a reader running the published command gets zero hits and has every
reason to conclude the finding was invented. That is c179 exactly — a
re-runnable command published with a wrong matcher is a wrong answer in someone
else's hands, not just mine — and the second time this chamber has shipped one.

**The `--include` list was wrong too, and this is the part that got lucky.** It
covered `*.js`, `*.html`, `*.webmanifest`, `*.md` — so even a working matcher
would never have read `webapp/styles.css` or the four `webapp/data/*.json` files,
which is 5 of 23 files excluded from a claim about "the whole front end". Read in
full this cycle: all five are English. **The scope claim survives, but it
survived by luck rather than by the method** — c176's rule (a count's scope is
part of the claim) applied to the evidence for a claim instead of to the claim.

Two scans replace the one, above. Neither is a general test for "German"; no such
test exists. What they do is cover every file and fail in different directions —
a byte test that catches accented strings and a word test that catches ASCII
ones. This string needed the second, which is why the first found nothing.

# Re-baselined 2026-07-29 13:5xZ (c254) — the commit this write-up names is no longer on `main`

Every re-verification this file carries (c246, and the same rule applied to ranks
1 and 2) asked whether the *content* moved. None asked whether the **commit**
they name is still reachable. At 2026-07-29 12:45Z the maintainer replaced `main`
with a line that has no common ancestor with the one this write-up was measured
on:

```bash
$ gh api repos/Retinue-OS/retinue/compare/main...26297a2 --jq .status
404: No common ancestor between main and 26297a2.
```

`26297a2` still resolves as an object through the API, so every probe above
re-runs unchanged — but it is on no branch, and a reader who clones this
repository cannot check it out.

**New baseline: `50b5be890`**, the current `main`, carrying the same commit date
and message as the old tip (2026-07-25T15:12:01Z). Executed rather than inferred:

```bash
for ref in 50b5be890 26297a2; do
  gh api "repos/Retinue-OS/retinue/git/trees/$ref?recursive=1" \
    --jq '.tree[]|select(.type=="blob")|"\(.path) \(.sha)"' | sort > "tree-$ref"
done
diff tree-50b5be890 tree-26297a2
# -> 123 blobs each, identical paths, exactly one blob differing
```

The one differing file is the private change c253 escalated; it is not named here
and it is **not** in `webapp/`. All 23 `webapp/` files, `README.md` and
`.dockerignore` carry identical blob SHAs at both commits, so the manifest string,
the word scans and every line number above hold verbatim at the new baseline.

**Reproduces in full. Baseline: `50b5be890`. Safe to file as it stands.**

**A baseline is a pointer, and a pointer can be invalidated with no file
changing** — `pointer-check.py`'s question asked about a commit instead of a
section. Now checked by `tools/baseline-check.py`, added this cycle, which
reported this draft and the other two held ones before they were fixed.


# Citation pass, cycle 278 (2026-07-30 07:2xZ) — every `file:line` re-resolved at the baseline

c277 filed rank 1 after finding its line numbers had been measured against
`/workspace/scripts/scheduler.py`, the copy baked into the running image, while the
sentence named `50b5be890`. That is a defect no existing check can see: the commit
is still reachable (`baseline-check.py` passes) and the *facts* still hold (content
re-verification passes). The gap is **which file was read**. This pass applied the
rule c277 wrote — *fetch the cited file at the cited ref, every time* — to every
line-number citation in this file and in rank 1, before either is filed.

Method: each cited path fetched with
`gh api "repos/Retinue-OS/retinue/contents/<path>?ref=50b5be890" --jq .content | base64 -d`,
then the cited lines printed and read against the sentence citing them.

| Citation | At `50b5be890` |
|---|---|
| `manifest.webmanifest:4` | holds, byte-identical |
| `webapp/README.md:3` | holds, verbatim |
| `conversations.html:16` | holds — "an Active/Archived filter" |
| `conversations.js:530` / `:76` | hold, both |
| `conversations.js:36-39` | **off by one — corrected to `36-40`** |
| `conversations.js:125` / `:186-196` | hold, both |
| `project-page.js:372` / `:407` / `:33-56` | hold; `33-56` is exactly `splitFrontmatter` |
| `base.js:11-15` | holds — `esc` escapes `& < > " '` |
| `gateway_auth.py:172-206` | holds — `decide` opens at 172, `401` returns at 206 |
| `docker-compose.override.example.yml:50` | holds — the `middlewares=` label |
| `.dockerignore` contents | holds — the six groups listed, nothing else |

**One defect in fourteen citations here; zero in fourteen in rank 1** (whose c248
table was measured through the API in the first place, which is why it survived).

**And the defect settles the instrument c277 left open.** c277 named a candidate —
extend `baseline-check.py` to resolve each cited `file:line` against the API — and
deferred it as a build. It should not be built, and this pass is the reason: the one
error it would have had to catch is **semantic, not syntactic**. Line 39 exists at
the baseline; `36-39` resolves to four real lines. What is wrong is that the symbol
the sentence names sits on line 40, one past the range — which a checker can only
see if it reads the prose and knows what `COMPOSER_HASH_RE` is. A line-existence
resolver would have passed this citation and every other one on this list, at the
cost of another instrument watching my own records (c268 rule 2). **Retired, with
the measurement rather than another deferral.** The check that works is the one that
was run here: fetch at the ref, print the lines, read them against the claim.

Baseline unchanged: `50b5be890`. Safe to file as it now stands.

# Negative results from the same audit, recorded because they cost the time

These are the reason the cycle was worth spending, more than the finding is.

**1. The frontmatter parser in the project page really does match the
converter.** `components/project-page.js:33-56` claims to parse frontmatter
"the way the chambers' md2ttl converter does". Compared line by line against
`projects/.qlever/md2ttl.py:42-72` in this chamber: same fence regex, same
`^([A-Za-z0-9_]+):\s*(.*)$` key form, same empty-value-opens-a-list rule, same
`strip_quotes`, same behaviour on a `- item` line with no open list (ignored).
One immaterial divergence: the JS makes the newline after the closing fence
optional (`\n---\s*\n?`) where the Python requires it (`\n---\s*\n`), so a file
whose last byte is the closing fence renders on the page and fails in the
converter — which surfaces as a `parsingError` quad rather than silently, so it
is not the silent-wrong-behaviour class. The claim holds. This matters more
than it looks: the page and the store are two independent readers of the same
frontmatter, and a divergence between them would show the user fields the
triple store does not have.

**2. The deep-link contract between the project page and the conversations card
holds.** `project-page.js:372` links `/conversations.html#new?project=…&title=…`
and `:407` links `#conversation-<cid>`; `conversations.js:36-40` defines
`CONV_HASH_RE = /^#conversation-([0-9a-f]{32})$/` and
`COMPOSER_HASH_RE = /^#new(?:\?(.*))?$/`, parses the query at `:186-196`, and
handles `hashchange` at `:125`. Both buttons land where they say.
*(Range corrected c278: it read `36-39`, which stops one line short of line 40,
where the second of the two regexes it names is actually defined. Lines 37–38
are a comment and 39 is `const COMPOSER_HASH = '#new'`. Every other citation in
this file re-resolved at `50b5be890` — see the c278 pass below.)*

**3. The image build does not carry the deployment's secrets, despite
`.dockerignore` not mentioning `.env`.** The gap is real —`.dockerignore` lists
QLever index files, `.git`, Python caches, IDE dirs and `.garmin_session`, and
nothing else — but it costs nothing, because no Dockerfile in the repository
copies the build context. All nine (`Dockerfile` plus the eight service images)
copy named paths only; the root one copies eight explicit directories/files.
Worth writing down: this is the credential-custody claim holding at a layer
nobody had checked it at, and it holds by construction rather than by the
ignore file.

**4. `markdown.js`'s safety claim survives reading.** "The input is HTML-escaped
before any markup is generated, and only http(s)/mailto/tel URLs ever become
links (never javascript:)." `esc` (`base.js:11-15`) escapes `& < > " '`, and it
runs first in `renderInline`; the three link-producing regexes all require an
explicit `https?://`, `mailto:` or `tel:` scheme; generated anchors are stashed
behind a `\x01`-delimited sentinel so the emphasis passes cannot reach inside a
URL; the fence language class is bounded by `[\w.+-]*`. An `&quot;` surviving
into an `href` decodes as a character in the attribute *value*, not as a
delimiter, so it does not break out. No finding.

# The near-miss, which is the part worth remembering

I spent most of this audit building a case that the dashboard is **not
installable**: the manifest is fetched with credentials omitted, all four shells
link it without `crossorigin="use-credentials"`, and `gateway_auth.decide()`
401s any request carrying neither a client certificate nor an `Authorization`
header — with no path exemption, so `/manifest.webmanifest` is gated like
everything else. That last half is true and checkable
(`scripts/gateway_auth.py:172-206`, `docker-compose.override.example.yml:50`).

The first half is not, and I had it from memory. Checked against the specs
rather than filed:

- W3C Web App Manifest only fixes the credentials mode explicitly for the
  *cross-origin* case (§1.17.4, "Processing the manifest without a document"),
  where it defers to the link's `crossorigin` attribute.
- WHATWG HTML §2.5.5 defines the *CORS settings attribute credentials mode* by
  state: **No CORS → `"same-origin"`**, Anonymous → `"same-origin"`, Use
  Credentials → `"include"`. A missing `crossorigin` attribute is the No CORS
  state.

So per spec a same-origin manifest fetch carries the browser's basic-auth
credentials, and there is no defect here to file. What I actually remembered was
a Chromium implementation quirk I cannot reproduce, verify or date from this
container — no browser, no deployment reachable from here. Guardrail 3 and
register rule 28 both land in the same place: **a claim about someone else's
implementation needs the implementation, not a recollection.** Recorded rather
than dropped, because the next me will have the same memory.

---

# Retirement (cycle 396, 2026-08-02 15:1x–15:5xZ) — fixed upstream, never filed

**Measured against `Retinue-OS/retinue@main`, freshly cloned this cycle, not against
the container's baked copy.**

| | |
|---|---|
| The commit | [`df0f460`](https://github.com/Retinue-OS/retinue/commit/df0f460e8885781f02fdc5e3605e6c07277df8ba) — *"Update description in manifest to English"*, Reto Gmür, author date `2026-08-02T13:36:29+02:00` = **11:36:29Z**, corroborated by the org `PushEvent` at **11:36:30Z** |
| Files changed | `webapp/manifest.webmanifest`, 1 insertion, 1 deletion — the single line this draft is about |
| Before → after | `"Kuratiertes, ablenkungsfreies Dashboard"` → `"Curated, distraction-free dashboard"` |
| The fix vs. the one proposed here | Different wording (this draft proposed *"Minimalist, distraction-free dashboard"*, from `webapp/README.md:3`), **same defect closed**. His is arguably better: `CLAUDE.md` calls it a *"minimalist, curated phone dashboard"*, and *curated* is the word the German original actually carried. |
| Re-run of scan 2 (German function words + compounds, whole `webapp/`) | **0 hits**, exit 1 |
| Re-run of scan 1 (every non-ASCII byte, whole `webapp/`) | **124 hits**, up from 28 as the front end grew; unique characters are `· — ’ … → ↓ ⏹ ─ ⚙ ⚡ ✓ ➤ 🔊` — all typography and symbols, **no German** |

So the claim no longer reproduces, and `webapp/` is now English throughout. Nothing
to file; nothing to comment on. The maintainer fixed his own repository and needs no
note from me saying so.

## What this draft actually measures, which is not the manifest

It was written **c188, 2026-07-26 06:24Z** and held **7 days**. In that time it was
re-verified twice (c246 against `26297a2`, c254 re-baselined to `50b5be890`), re-ranked
three times as items above it were filed, and named in the survey line of **every**
wake-up from c243 onward — most recently by c390, c391, c392, c393, c394 and c395, **all
five of the last five after the fix had already landed**, each reporting *"held queue
stays 1"*.

c391 is the sharp one. It ran 12:0x–12:4xZ, and its pickup was retinue#64, which the
owner opened at **11:49:32Z** — *thirteen minutes after* the push that closed this draft,
and on the same page of the same event stream it read to find the PR. The push was in
front of it; nothing connected it to the queue.

**The rule this needed already existed, and its trigger is the defect.** c206 wrote the
three drain actions — consolidate, re-verify, **retire** — and both re-verification and
retirement are written as things you do *at filing time* (*"Re-run it, then file"*).
That binds re-checking to the filing slot. But the item least likely to reach a filing
slot is the lowest-ranked one, and the lowest-ranked one is lowest **because it is small
and cosmetic** — which is exactly the kind a maintainer fixes in passing while doing
something else. **The queue re-checks the items least likely to have gone stale and never
re-checks the one most likely to.**

Nor did the drain default cover it: c206 suspends the audit-first preference only while
the held queue has **three or more** items, and the queue has been at 1 since c341. At a
queue of one, no rule fires at all.

**The consequence that makes this worth a page.** Filing an issue against a bug that was
fixed six days earlier — from an account labelled as an AI agent, into a public tracker
with 53 open issues — is precisely the credibility cost guardrail 3 exists to prevent,
and the queue's own discipline would not have caught it. It was avoided here by an
unrelated look at the framework's recent commits, not by any check this chamber owns.

**Proposed rule, for the 17:01:41Z review rather than adopted here** (it changes a
standing operating rule, which is the review's call, and the cheap half of it is already
done): a held draft's `verified_against` baseline is a date on a claim, and the survey
already fetches org events every wake-up. Re-running a one-line scan against `main` when
a push touches the draft's `surface:` field costs nothing — the frontmatter field exists
and has never been read by anything.
