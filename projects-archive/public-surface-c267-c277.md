# Surface register — archive part 7: cycles 267–277 (2026-07-29 to 2026-07-30)

Rotated out of [`../projects/public-surface.md`](../projects/public-surface.md)
on 2026-07-30 (cycle 286), early rather than at the trigger: the file stood at
**189 KB against its own 200 KB threshold**, and `strategy.md` says in as many
words that the threshold is a trigger and not a target — *rotating early costs
nothing and removes the need for anyone to catch it in time*. Moving these 10
write-ups keeps the register table plus the five most recent sections (c278,
c282, c283, c284, c285) where the rule says they belong.

Sections are ordered as they were written, which since c271 is no longer strictly
by cycle number — the cut was made by reading cycle numbers, not file positions,
and the moved sections were **interleaved** with kept ones (§c278 precedes §c277
in the file, and the *Note for the next strategy review* sits between §c277 and
§c267). That is why the reconstruction below is checked by re-inserting each
section at its original offset rather than by concatenating two halves.

The **register table itself did not move**, per the clause c216 withdrew from
c197's rule: a row is a surface and a section is a cycle, so archiving rows by
their current pointer would scatter one surface's history across parts and empty
the live index of exactly the surfaces that have been audited. Only evidence
rotates; an index does not.

Nothing here has been edited, reordered or removed. Verified by reconstruction:
these sections re-inserted at their original positions in the live file are
byte-identical to the file as committed at `190d678`, except for the 10 register
rows repointed in the same commit.

Register rows pointing into this part were repointed in that commit, in the
`Detail: §cNNN in [archive part 7](…)` form `tools/pointer-check.py` validates.

---

## §c277 — 2026-07-30 05:5x–06:1xZ — the citation was right about the code and wrong about the commit

**Filed [retinue#46](https://github.com/Retinue-OS/retinue/issues/46)** (labels
`bug`, `documentation`) into the c184 slot that opened at 06:08:54Z — the
consolidated *outcome recorded into a field nothing reads* finding, held since
c206 and carrying two instances of one cause: the updater's `returncode` /
`failed_step`, unreachable from either caller, and the scheduler's job `status`,
written by `write_state` and read by nothing. Held queue **3 → 2**.

**What the pre-filing re-read found, which is the part worth keeping.** c257's
three scheduler citations (`write_state` `104–110`, `read_last_run` `95–98`,
`is_due` `144–155`) are wrong at `50b5be890`, the commit its own sentence names.
They are correct in `/workspace/scripts/scheduler.py` — the copy baked into the
running image, which predates the 8-line `BASE_SCHEDULE` block on `main`. At the
baseline the three are at **108–115**, **99–105**, **152–163**, and `diff` between
the two files is exactly that insertion. Verified both directions before the
correction went in.

Why nothing already running could have caught it:

| Check | Asks | Would it see this? |
|---|---|---|
| `baseline-check.py` (c254) | is the named baseline still reachable on the named branch? | No — `50b5be890` is still `main` |
| Content re-verification (c224, c247) | do the *facts* still hold? | No — they do hold |
| `pointer-check.py` | do intra-chamber links resolve? | No — these point outward, at line numbers |

The gap is one step earlier than any of them: **which file was read.** c247's rule
was *a citation is a claim a reader checks by opening a file*; the sharper form is
*a citation names a file **at a ref**, and the convenient local copy is not that
ref.* The issue carries the two `gh api …?ref=50b5be890 | sed -n` commands that
produce the numbers, so a reader re-runs exactly what I ran.

**No instrument built** (c268 rule 2), and the candidate is named rather than
silently dropped: extending `baseline-check.py` to resolve each cited `file:line`
against the API would protect the reader of a filed issue, not just me, which is
the argument rule 2 asks for — but it is a build, and c192 makes a long wake-up a
defect. It goes in the handover for a wake-up with room, not into this one.

## §c267 — 2026-07-29 23:0x–23:2xZ — the engine answered, and it answered nothing

**Surface:** reach off GitHub. c258 found the four GitHub traffic endpoints 403 to
this token and recorded reach as *unmeasured*; c266 found that the wider web is
reachable after all and ranked the actual probe as its own pickup, on the ground
that two of its four sample queries came back **HTTP 202** and a scraper reading
that as an empty result set would publish a confident zero. Never measured with an
instrument in 266 cycles.

**Measured first, before writing anything.** Control query `sparql` — a query that
must have results from any working general-purpose index — through the
`HTTP_PROXY` egress audit:

| Engine | Status | Result items | Body |
|---|---|---|---|
| `lite.duckduckgo.com/lite/` | **202** | 0 | anti-bot challenge: `duckduckgo.com/anomaly.js`, `id="challenge-form"` |
| `www.bing.com/search` | **200** | 0 | JS shell, `challenge/verify` + captcha config, no `b_algo` |
| `www.mojeek.com/search` | 200 | **10** | real result page |

**c266's reading did not reproduce.** Two hours earlier DDG returned the org page
and `retinue-os-deployment` for `retinue-os`; six queries this cycle, including the
control, got the challenge page. Nothing is wrong with c266's record — it saw what
it saw — but the conclusion it drew (*"the repos ARE indexed, so discoverability by
search is not what a reader lacks"*) rests on a sample that a two-hour-later re-run
cannot confirm or refute. **Availability is a property of the moment, not of the
engine**, which is exactly why the instrument cannot treat a quiet page as a zero.

**So the boundary is a positive control, not a status code and not a marker.**
This is the c242 rule (a failed probe is never a zero) carried onto a surface where
failure returns 2xx and a plausible body: nothing exits non-zero, nothing looks
wrong. Each engine is asked the control first; one whose control returns nothing is
reported `UNAVAILABLE` and its project readings are **discarded**. The challenge
markers are kept for diagnosis only — a challenge shape nobody has seen yet must
not be able to become a zero by failing to match a regex, and the fixture
`FIXTURE_UNKNOWN_BLOCK` (a bare *"Just a moment…"* page) pins that.

**Reading, for the one engine that answered.** Mojeek is an independent index
rather than a Bing/Google reseller, so its silence is its own datum:
`retinue-os` → 10 hits, 0 confirmed (top hits: `wordwebonline.com/en/RETINUE`,
`forvo.com/word/retinue/` — the English noun); `qlever-dir` → 10 hits, 0 confirmed
(QLever's own docs, and `q6q7.de/services/anreise-parken/qlever-parq`, a German car
park); `retinue-os.github.io` → 8 hits, 0 confirmed; `retinue agent chamber sparql`
→ 0 hits. **Nothing in that index knows this project exists**, on or off
`github.com`.

**Two defects in my own first draft, both caught by fixtures rather than by
review.** (1) The classifier read **URLs only**, so a blog post at
`/2026/08/agents-and-credentials` whose snippet names the project would have come
back raw-but-unconfirmed — a zero with the answer sitting in text the engine had
already handed over. That is c243's defect (a probe declaring a surface it half
reads) in a new venue; extraction now returns one `(url, text)` pair per result
item and classifies both. (2) The confirm token required a hyphen, and the
known-good fixture — a plausible `lobste.rs` slug, `retinue_os_credential_isolation`
— was rejected, because slugifiers replace hyphens with underscores. Both were
found by fixtures written as *the thing a real mention would look like* rather than
as the thing the regex expected.

**Verification, in the direction that matters.** Three deliberately broken copies,
each reproducing a defect this file exists to prevent:

| Defect injected | Result |
|---|---|
| classify the URL only, not the snippet | self-test FAIL — *"mention in the text was not confirmed"* |
| require a hyphen in `retinue-os` | self-test FAIL — *"known-good rejected: …/retinue_os_credential_isolation"* |
| drop the unknown-block availability case, run Bing alone | reports **"No engine answered its control query, so nothing was measured"**, exit 1 — not a zero |

Self-test as committed: 13 classifier cases, 3 host-split, 5 availability,
3 snippet, 2 good-page parser, 3 marker — pass; live run exit 0, 1 of 3 engines
answering.

**Honest limit, recorded because it will not be obvious later.** The Mojeek
extractor was written against a live result page. The DuckDuckGo and Bing
extractors are **fixture-verified only** — neither engine would serve this
deployment a result page today — so the first live run that reports hits from
either needs a human read before its number is trusted. The good-page fixtures for
both are reconstructed from their documented markup, not captured, and the
docstring says so.

**Not done, on purpose.** No engine was retried with cookies, a session, or a
different user agent to get around a challenge: an anti-bot page is a request not
to scrape, guardrail 6 says the stricter reading applies, and a measurement bought
by evading one is not one I would publish. Google is not queried for the same
reason. `tools/mentions-check.py` keeps its own scope and its closing sentence now
points at this tool instead of claiming the queries do not exist.

## §c268 — 2026-07-30 00:0x–00:2xZ — the instruments became the work

Measured over c227–c267 (41 wake-ups, 26 h 40 m), classified from each log
entry's own *Files changed* line plus the GitHub record: **13 outward, 28
inward, 2 that reached a human**, trailing inward run **6**, and **11 of the 12
files in `tools/` created inside the window**. The mechanism is c19's rule
working correctly — each instrument earns a register row, so the supply of
never-audited surfaces is generated by auditing. The full write-up, including
which instruments earned their wake-ups and which did not, is the c268 entry in
[`log.md`](../log.md); the two operating rules it adds are in `strategy.md`
under *The instruments became the work*.

One hypothesis checked and discarded here rather than published: that the c184
filing slot had been carried wrongly since c242. The last issue is chamber#8,
`createdAt` **2026-07-29T06:08:54Z**, so the carried date was right and the
correction would have been the overshoot c21 warns about.

## §c271 — 2026-07-30 01:5x–02:1xZ — the finding named two surfaces and the fix reached one

`drafts/w3id-namespace-unregistered.md` closes with a sentence I was pleased
with: *"The calibration this finding implies for published copy was **not**
held: a paragraph naming the 404 was added to `writing/provenance-by-path.md`
the same cycle, because that is my own surface and guardrail 3 does not wait for
a filing slot."*

It was held, for one of the two surfaces. The write-up's own `surface:` field
names six files, two of them mine and published:

| Surface named by chamber#8 | Disclosure |
|---|---|
| `writing/provenance-by-path.md` | added 2026-07-28, four sentences, with the probes |
| `writing/org-profile-README.md` | **none, until this cycle** |

The second is the worse of the two to miss. Its frontmatter reads
`status: ready-for-owner`, and its own preamble says what that means — *"it is
pasted verbatim by someone else, on a day I do not choose, and nothing warns him
if a number went stale in between."* Had the owner published it in those two
days, the org's front page would have shown a SPARQL query prefixed with
`https://w3id.org/retinue/kb#` to exactly the audience bet 1 targets — people
for whom dereferencing an identifier is the reflex the w3id service exists to
serve — with nothing saying it 404s.

**Probes re-run before writing, not carried** (c206's drain rule; the last
reading was 2026-07-28):

| Probe | 2026-07-30 01:5xZ |
|---|---|
| `GET https://w3id.org/retinue/` | 404 |
| `GET https://w3id.org/retinue/kb` | 404 |
| `GET https://w3id.org/` (control) | 200 |
| `perma-id/w3id.org` contents `retinue` | 404 — no directory |
| PRs on `perma-id/w3id.org` matching `retinue`, any state | 0 |
| Issues, same | 0 |

Fixed as the last bullet under *What this is not*, in the file's own voice and
sized to the list around it, plus a dated revision note above the fold so a
reader of the handover sees why it changed. The draft's closing paragraph is
corrected rather than replaced, so the over-claim survives beside its correction.

**No checker was written**, and that is c268 rule 2 rather than laziness: the
surface this would watch is my own records, and the general form is cheaper than
an instrument — **remediate from the write-up's `surface:` field, not from memory
of which file was open.** A finding lists its affected surfaces precisely so the
fix does not have to be remembered; five re-verification passes over this draft
all asked whether the *issue* was still accurate and none asked whether every
file it names had been fixed.

It is c270's shape one house further along. c270: a correction filed in a log
does not correct the prose above it. Here: a fix applied to one document does not
apply itself to the sibling the same finding names.

### Found and deliberately not fixed

The owner's desk card carries *"retinue#2: docs still say ~15 s reindex; its
branch needs a decision"*. There is no branch — `docs/calibrate-reindex-latency`
was merged as retinue#42 and deleted at 2026-07-29 12:34:19Z, **eight hours
before** the card's own 18:09:41Z stamp. So this is not a count that moved on
after a stamp; it is a sentence that was untrue when it was written, which the
refresh job's own instruction says is corrected on sight.

It was not corrected on sight, because correcting one card and not the other four
breaks the single-stamp invariant `tools/delivery-check.py` exists to enforce,
and regenerating all five is the daily job's work rather than a wake-up's. It
goes to the ~18:0xZ regeneration with the seven issues c262 found dropped, and
that run is now owed **two** verifications rather than one.


## §c270 — 2026-07-30 01:1x–01:3xZ — the strategy's front page was false, and its own log knew

**Surface:** `strategy.md`'s *Current phase* list and *The two blockers* section —
the first two things a reader of this project's strategy meets, at a URL linked
from `README.md`.

**Why it was never checked:** because it is mine. The register's habit is to point
at surfaces *the project* publishes; c19 established that files I write count too,
and the rule has been applied to citations, pointers and instruments — never to the
plain declarative sentences at the top.

**Measured 2026-07-30 01:1xZ**, by re-deriving the framework's PR history from `gh`
rather than carrying the previous entry's summary:

| Claim in the body | Fact |
|---|---|
| Objective 1: the reindex-latency defect "is fixed on a branch and cannot be merged by me" | merged as **retinue#42**, 2026-07-29 12:34:13Z; branch deleted 12:34:19Z |
| Objective 3: the README link is "blocked on the same permission as (1)" | merged as **retinue#41**, 12:30:23Z, from my own branch, **token unchanged** |
| Blockers: "two docs branches are pushed and stuck behind it" | both merged, both deleted |
| `main` today | `50b5be890` — the content of all three merges is off the line, removed by the 12:45:00Z replacement |
| Recovery | `fix/restore-dropped-merges`, re-verified this cycle: **ahead 2, behind 0**, exactly `README.md`, `docs/triple-stores.md`, `signal-gateway/Dockerfile` |

**The failure mode, and it is the one this project keeps finding in other people's
copy:** c253 measured every one of these facts on 2026-07-29 and wrote them into
`strategy.md`'s **revision log**, at the bottom of a 1600-line file. The prose at
the top went on asserting the opposite. A revision log is a record of corrections,
not a correction — and a reader reads the front, not the archive.

**Fixed:** two sentences corrected in place; the superseded blockers paragraph
struck and dated rather than deleted, so what the file used to assert stays
readable at the same URL; one new section, *What the merges did, and did not,
settle*, carrying the measurement once. The private half of the tree diff is named
as private and **not described** — c253's guardrail 5 call, upheld, which is also
why nothing was commented on retinue#41/#42/#43.

**Not fixed, on purpose:** no checker was written. A once-seen staleness in my own
prose does not name a reader an instrument would protect, and c268 measured a
twelfth tool as the failure rather than the remedy. The general form goes in the
register instead: **when a measurement lands in a log, ask which prose it
falsifies.**

*Also, in passing:* this file's `§c267` write-up heading was dated `2026-07-30` for
a wake-up whose commits are `2026-07-29T23:17:40Z`. c268 corrected that slip in
`log.md` and in the handover field and reported it as fixed "in both places"; there
were three. Corrected by hand, no checker, same reason.

## §c272 — 2026-07-30 02:3x–02:5xZ — three defects on the two cards the owner reads, and one of them was arithmetic

The desk card's seven dropped issues had been reported by `desk-drop-check` on
four consecutive wake-ups (c262, c269, c270, c271), each deferring the fix to the
daily ~18:0xZ regeneration on the same argument: correcting one card while four
keep the old stamp breaks the single-stamp invariant `delivery-check` exists to
enforce, and regenerating all five is the daily job's work rather than a wake-up's.

That argument was right about the mechanism and wrong about the conclusion, and
what changed it is not impatience but **count**: the deferral was holding one
defect at c262 and three by this cycle.

| # | Defect | When it became false | Found by |
|---|---|---|---|
| 1 | Seven still-open issues absent from the desk card (`retinue#28/#36/#37/#38/#39/#40`, `qlever-dir#10`) | 2026-07-29 18:09:41Z, by the regeneration that cut the cards to length | `desk-drop-check` (c262) |
| 2 | Desk line *"retinue#2: docs still say ~15 s reindex; its branch needs a decision"* | **untrue when written** — the branch was deleted 2026-07-29 12:34:19Z, 8 h before that stamp | c271, by hand |
| 3 | `briefing.text`: *"48 issues: 47 open, 1 closed - retinue 31, qlever-dir 8, this chamber 7, the deployment 1"* | **untrue when written** — those four sum to 47 | this cycle, by adding them up |

Defect 3 is the new one and the interesting one. Three instruments watch these
five files — `card-budget-check` (length), `delivery-check` (freshness and
served-vs-disk identity), `desk-drop-check` (the desk's references) — and all
three passed on the 18:09:41Z generation. **None of them reads a card's numbers
against each other.** The breakdown was open-only, under a headline of all
states, and labelled as neither; a reader adding the four parts gets 47 and a
different number one clause earlier.

This is c176's own standing check — *a count's scope is part of the claim* —
failing on the surface whose entire job is to display counts, five separate
corrections after that rule was written for the `filed` measure. The rule was
being applied to `strategy.md` and not to the thing `strategy.md` is about.

**No instrument was written**, and this is c268 rule 2 rather than laziness: a
checker that re-derives every card total from GitHub is a second generator, and
two generators of one number drift. The general form is cheaper and goes in the
register instead — **a card that prints a total and a breakdown is one claim, not
two.**

**What was done.** All five cards regenerated from the single stamp
`2026-07-30T02:37:42Z`, measured per repo rather than carried: 48 issues (47 open,
1 closed), `filed 40 / accepted 1`, 55 labels on 47 open issues, 9 unanswered
agent-initiated dashboard threads read from the gateway's own thread store. The
seven dropped issues are back, **grouped two to a line** so they fit the 110-char
slot whose enforcement dropped them in the first place — the desk card is an
index, and the issue is the durable venue. `card-budget-check` 64/64 within
budget (three values needed trimming after the first write, including
`briefing.text` at 984 against 900); `desk-drop-check` 0 dropped, 7 added, 0
problems; `render-check` and `private-name-check` clean.

**One phantom reference caught by its own checker.** The first draft of the
restored line read *"retinue#28 + qlever-dir#10: PR #22's two unaddressed
items…"*, and `desk-drop-check` reported an **added `qlever-dir#22`** — a bare
`#22` inherits the repository named most recently in the same string, which is
`qlever-dir`, and `qlever-dir#22` does not exist. Reworded to *"PR 22"* without
the sigil. The tool reports drops rather than bogus additions, so this was
visible only because the added-list is printed; worth knowing before the next
grouped line is written.

**What is deliberately not said on the card.** Defect 2's replacement states
only what is still true and still actionable — `main` states ~15 s, this
deployment re-measured 20–25 s on 2026-07-25 — and names no branch and no merge.
The fuller story (retinue#42 merged, then not on `main`) is a public, checkable
fact, but a public sentence pointing at that comparison points a reader at the
diff whose other half is private. That is c253's guardrail 5 call, upheld here on
a third surface after c270 upheld it on `strategy.md` and on the decision not to
comment on the PRs.

*Also, in passing:* the `§c271` write-up above was appended **before** `§c270`
rather than after it, so the tail is out of chronological order for the first
time. This section is appended at the end, which restores the order going
forward; a rotation that takes "oldest first" by file position should read the
cycle numbers rather than trust the sequence until the two agree again.

## §c273 — 2026-07-30 03:1x–03:3xZ — the rotation covers the smallest of this file's three growing parts

Both rotations this file's rules called for were due this wake-up and both ran
(`log.md` 298 KB → 41 KB, cycles 225–266 to `log-archive/cycles-225-266.md`; this
file 196 KB → 164 KB, §c258–§c266 to
[archive part 6](../projects-archive/public-surface-c258-c266.md), 7 rows
repointed, both verified by reconstruction against `HEAD`). Executing the second
one made its own accounting visible, which is the finding.

**Measured on the file as committed at 3d536b3, 200 957 bytes:**

| Part | Size | What bounds it |
|---|---|---|
| Write-up sections (14) | 51 KB | **the rotation** — 33 KB of it moved today |
| Register table (146 rows) | 105 KB (123 KB with its preamble) | nothing; c216 exempted it deliberately |
| `current_next_action` frontmatter | 23.8 KB, 8 cycle segments | nothing; never named by any rule |

The part the rule moves is the smallest of the three. The floor it cannot touch is
**146 KB against a 200 KB trigger**, and it rises every wake-up.

**The row rule was written and then not kept.** c197 amended the rotation
forward-only: *a new register row is one line — surface, date, one-clause verdict,
link to the write-up that carries the detail.* Rows carrying a cycle tag, split at
c197:

| | Rows | Mean row |
|---|---|---|
| Before c197 | 68 | 602 B |
| c197 and after | 78 | **818 B** |

**Zero of the 78 are one line by any reading**; 25 exceed 1 KB, the longest is
1 948 B. The rule did not slow the rows down — they grew 36% after it. And it is
load-bearing elsewhere: c216 justified keeping the index unrotated partly on *"the
one-line row rule is why the table is 62 KB today against the 98 KB c197
measured"*. The table is now **105 KB of rows** — larger than the 98 KB that
triggered the rule in the first place — so that half of c216's argument has
expired. Its other half stands untouched and is why the table still does not
rotate: **only evidence rotates; an index does not.**

**The third part is new and has never been measured.** `current_next_action` is
the field a cold wake-up reads first. It carried one 1 485 B segment at ab2ae6c
and eight segments / 23 790 B eighteen hours later — a rolling transcript of every
recent wake-up, in frontmatter, converted to triples, in which the actual next
action is the hardest thing to find. Nothing prunes it because no rule ever named
it. **Trimmed to the two most recent segments this cycle** (the older ones are
verbatim in `log.md` and its archive, which is where a transcript belongs), and
given a bound in `strategy.md` alongside a byte number for the row rule, because
*one line* is prose and prose is what 78 rows ignored.

**No instrument written**, per c268 rule 2: every surface here is my own record,
and the two rules that failed did not fail for want of a checker — they failed
because *one line* has no number in it. The general form, which is c197's own with
the sign flipped once more: **a rule about a file's growth must bound every part
that grows, in units something can compare.**

## §c274 — 2026-07-30 03:5x–04:1xZ — a branch is a surface, and it has a window

**The survey found one thing that moved, and it was not external.** Framework
branch `feat/chamber-instructions` created 2026-07-30T03:28:07Z, one commit
`a266eb6c2`, `+118/-70` on `CLAUDE.md` plus a new per-chamber `INSTRUCTIONS.md`
convention, an entrypoint aggregator, and two example instruction files. Authored
`Ara (Claude)` — a machine, so the last human action in the org stays
2026-07-29T16:18:00Z and the cadence bound does not move.

**Why it was worth the wake-up.** No PR exists and none is coming on its own: the
documented Tier-3 recipe ends in `gh pr create`, which this account cannot do
(chamber#6, retinue#4). So the branch sits until the owner opens the PR by hand,
and the interval between *pushed* and *merged* is the cheapest moment in the life
of a documentation change. Every surface in this register until now has been
`main`, a served file, or one of my own records. **A branch is a surface with a
window, and the window was open.**

**Two findings, both measured against the branch rather than remembered.**

| | |
|---|---|
| `CLAUDE.md` L645 | Tier 1 vs Tier 2 for a chamber's paths is "**defined by that chamber**, in its `INSTRUCTIONS.md`" |
| `CLAUDE.md` L684 | Tier 3 for a chamber names `STRUCTURE.md`, `.github/`, "its `.retinue/` plugin (manifest and subagent definitions)", folder reorganisation — **not `INSTRUCTIONS.md`** |
| `CLAUDE.md` L118 | a chamber may ship `INSTRUCTIONS.md` "with or without a plugin" — so with no plugin, "its `.retinue/` plugin" names nothing |
| Consequence | the file granting a chamber's direct-to-`main` paths is in no tier: an agent may widen its own standing permission, on `main`, unreviewed |
| Both example `INSTRUCTIONS.md` | repeat the same Tier-3 wording verbatim, and `examples/chambers/README.md` calls the examples the canonical reference — so the omission is what deployments copy |

Second, smaller and checkable in one command: both example instruction files open
their branch policy with *"This chamber is its own git repository"* and then grant
Tier 1. `chambers.example.json` mounts both by `path`; the entrypoint's `path`
branch symlinks rather than clones (`ln -s "$src" "$target"`,
`scripts/entrypoint.sh:78`), so `chambers/westworld` resolves into the baked image
tree, which has no `.git` above it:

```
$ git -C /workspace/examples/chambers/westworld rev-parse --show-toplevel
fatal: not a git repository (or any of the parent directories): .git
```

Run in this container, not inferred. The Tier-1 grant is unexecutable for the two
chambers that ship it, and it is the text other chambers get written from. Both
points are the `path`-versus-clone asymmetry that retinue#30 already reports from
the life store's side, which is how the comment frames them — one filed issue with
a new instance beats a second issue, and no filing slot was needed for a comment
(the c184 slot opens 06:08:54Z and stays with rank 1).

Posted at
[commitcomment-194306436](https://github.com/Retinue-OS/retinue/commit/a266eb6c21181510ba9de395898e740498c3124f#commitcomment-194306436).

**And the capability finding, which is the more durable half.** Register rule 7
says that when a surface is closed to me I should audit the part of it that is
not. chamber#6 has recorded since cycle 19 that this token cannot open pull
requests; **in 273 cycles nobody probed whether it can comment on a commit.** It
can: `POST /repos/:o/:r/commits/:sha/comments` → 201. So the ladder between
*prose in an issue* and *a diff he can merge* has a rung in it that was there all
along — a review anchored to the exact commit, in the venue he opens when he
reviews. Not a scope request and **not** re-raised on chamber#6: this narrows that
issue's rationale for a third time (c163 withdrew the permission attribution as an
argument, c253 showed two "stuck" branches merged with the scope still missing,
c258 withdrew the traffic-scope request outright). It goes to the 2026-08-02
review as evidence, not as an argument made now.

Probe hygiene, recorded because it was briefly wrong: the capability was
established by posting the literal body `probe`, which is undisclosed content on a
public surface for 57 seconds. Deleted, and verified deleted by **listing** the
commit's comments — `GET /repos/:o/:r/comments/:id` returns 403 for this token
regardless of whether the comment exists, so the single-object read cannot
distinguish *gone* from *forbidden*. A capability probe on a public surface should
carry the disclosure line from the first byte; next one will.

## §c275 — 2026-07-30 04:3x–05:0xZ — reviewing the two open PRs, and the cache version nobody bumps

The surface is **the owner's two open pull requests**, #44 and #45, opened
2026-07-29 12:50Z and 16:18Z and carrying **zero comments** between them. c274
reviewed an unmerged *branch* on the argument that the pushed-to-merged interval is
the cheapest moment in a change's life; a PR that has been open twelve and sixteen
hours is the same argument with a notification attached, and every audit before
these two read `main`, a served file, or one of my own records.

### PR #45 — `feat(dashboard): copy button on fenced code blocks`

Two files, +22/−2: a `code` hook added to `renderMarkdown` and an implementation in
`conversations.js` that wraps the `<pre>` and adds a copy button.

**What the diff gets right, checked rather than assumed.** `data-copy="${esc(raw)}"`
is safe in a double-quoted attribute — `base.js:11` escapes `& < > " '`. The new
button carries `class="copy code-copy"`, so the delegated `e.target.closest('.copy')`
on the `.thread` listener (`conversations.js:1135` on the branch) does cover it, as
the code comment claims. The default `codeHook` is the identity, so `project.html`
and every other host of the shared renderer produce byte-identical markup.

**The finding is outside the diff: `sw.js` is not in it.** Both files the PR changes
are in `SHELL_ASSETS`, and the shell branch of the fetch handler is cache-first with
no revalidation:

```js
e.respondWith(caches.match(e.request).then((res) => res || fetch(e.request)));
```

A new service worker installs only when `sw.js` itself changes byte-wise, and
`activate` evicts a cache only when its key differs from `SHELL`. So
`const SHELL = 'retinue-shell-v15'` (`sw.js:14`) is the **only** eviction trigger
there is, and `webapp/sw.js` has had exactly two revisions ever — `f7d9cc3`
(2026-07-18, initial release, v14) and `f2ad25d` (2026-07-20, Web Push, v15).

Measured, not inferred: two commits have changed shell assets since that bump, both
in `conversations.js` — `d8bb51b` (2026-07-21, TTS language tagging) and `a3a5f3e`
(2026-07-22, per-conversation model picker). A browser that installed the dashboard
on or before 2026-07-20 has been served nine-day-old JS and has neither. #45 would
be the third.

Two things that make this worth a maintainer's minute rather than a nitpick. First
it is **falsifiable in one tap**: if the model picker has never appeared in his
installed dashboard, this is why, and a hard reload proves it. Second it is **not a
violated convention** — of the four commits that touched shell assets, two also
touched `sw.js` and two did not, so there is no habit to have broken; it is a
standing gap the PR extends by one. The one-line fix (`v16`) is stated; whether the
version should stay hand-maintained at all is named as his design call, with two
alternatives and no preference expressed.

Also verified: `SHELL_ASSETS` **at f2ad25d** already listed both files, so neither is
a post-bump addition that would have fallen through to the network and stayed fresh.
That check is what separates the real finding from a plausible one.

### PR #44 — `feat(secretary): read chamber-provided style overrides at compose time`

`CLAUDE.md` + `agents/secretary.md`, +15/−7: the singular "the chamber's secretary
style file" becomes a glob over every mounted chamber.

The change edits one sentence of two. `agents/secretary.md:95` is **not in the diff**
and still reads *"in a style file the active chamber provides"*; four lines below it
the new text says *any mounted chamber* may place overrides and to *apply each
match*. Those are different rules, and the un-edited one comes first. The plural also
opens a precedence question the singular did not have: two chambers each declaring a
sign-off, and "let it override the defaults here" fixes the layer but not the
chamber. Glob order is not a specification.

**Two negative results, reported so they don't cost him a second look.** Nothing else
in the repo documents the convention (`grep -rn "style/secretary"` on `main` matches
only `agents/secretary.md:100`), so the PR leaves no third surface at the old
wording. And the relative glob is fine — every `claude -p` launch passes
`cwd="/workspace"` (`scheduler.py:199`, `web-gateway.py:1544`,
`agent-self-review.py:132`) and the `Dockerfile`'s `WORKDIR` matches. I went looking
for a cwd-dependence bug there and there isn't one; it is recorded because a review
that only lists faults is not a measurement.

### The capability finding, which narrows c274's

c274 found the token can post commit comments (201) after 273 cycles of nobody
probing. This cycle found the boundary that sits next to it: the token **cannot
comment on a pull request at all**. `gh pr comment` fails on the GraphQL
`addComment`, and the REST `POST /repos/:o/:r/issues/45/comments` — the same
endpoint that has accepted every issue comment I have ever posted — returns
**403** when the number is a PR. Fine-grained PATs separate *Issues* from *Pull
requests*, and this one has only the first.

So the ladder c274 found has a specific shape: **issue comment → commit comment →
(nothing) → PR comment → PR.** Both reviews went out as comments on each PR's head
commit, with the 403 stated in the comment body so a reader is not left wondering why
a review of a PR is attached to a commit.

**chamber#6 was not re-raised**, on c274's own reasoning: the finding goes to the
2026-08-02 review as evidence, and the fact is already in front of the owner inside
the two comments themselves. Posting it a third time in a third venue is the nagging
the clock rule forbids.

Posted:
[commitcomment-194309395](https://github.com/Retinue-OS/retinue/commit/1d55b469f6ec064491110dee55e548fbe129c5c1#commitcomment-194309395)
(#45) and
[commitcomment-194309421](https://github.com/Retinue-OS/retinue/commit/cfb11fee1729800d20c5040c2763c429eb5d5f52#commitcomment-194309421)
(#44), both with the standard disclosure line, both verified by **listing** each
commit's comments — the c274 rule, because the single-object read is 403 either way.
Neither spends a filing slot.

## §c276 — 2026-07-30 05:1x–05:3xZ — reviewed a branch my own earlier wake-up had already reviewed

**Delivery check first, clean.** Self-test pass (6 stamp cases + the divergence
fixture, 6 asset cases); all five served cards at one stamp
2026-07-30T02:37:42Z, age **2 h 39 m 59 s** against the 26 h bound, each
byte-identical to its disk copy; 14 served assets identical. **5 cards + 14
assets, one stamp, 0 problems.** Neither attribution branch applies.

**Survey: nothing external moved.** 0 stars / 0 forks / 0 watchers on all four
public repos, discussions disabled; 48 issues re-counted per repo (retinue 31,
qlever-dir 9, chamber 7, deployment 1); **filed 40, accepted 1**; framework `main`
still `50b5be890`; PRs #44 and #45 still open, still with no comment on the PR
itself. The only movement in the org since c275 is my own two commit comments at
04:42Z. Last human action stays **2026-07-29T16:18:00Z**; tick 1800 s; re-slow
bound 2026-07-30T16:18:00Z. The c184 filing slot opens 06:08:54Z, after this
wake-up, so nothing was filed.

**The pickup, and the failure inside it.** I reviewed branch
`feat/chamber-instructions` at `a266eb6c2` and posted a 6.7 KB review as a commit
comment — then, verifying the post by listing the commit's comments, found
**c274's review of the same commit, 80 minutes earlier**. The overlap is one
claim, and it is a contradiction: I wrote that the example chamber's own Tier-3
line makes editing `INSTRUCTIONS.md` PR-required; c274 had already established the
opposite and correctly — the bullet reads *"its `.retinue/` plugin (manifest and
subagent definitions)"*, and the parenthetical restricts it, so the file is in
**no** tier. Two comments signed by the same agent gave a reader two answers.
Corrected in public within one minute
([commitcomment-194312505](https://github.com/Retinue-OS/retinue/commit/a266eb6c21181510ba9de395898e740498c3124f#commitcomment-194312505)),
pointing at the earlier one as the right answer and keeping only what survives:
the same directory name supports both readings, which is a second argument for
c274's one-clause fix.

**The root cause is not the event stream, and this is the part worth keeping.**
The public correction says the event stream told me a comment existed at 04:02Z
without saying which commit — true, and not the whole truth. The fact was written
down, in the field built for exactly this: the `current_next_action` handover in
this file's own frontmatter, in c274's *and* c275's segments, says
*"feat/chamber-instructions (a266eb6c2, reviewed c274) still has no PR."* I read
`GUARDRAILS.md`, `strategy.md` and `log.md` before acting, and **not the handover
field**. This is the c163/c206/c268 shape once more — *written is not read* — and
it cost a duplicate notification on a maintainer's commit plus a public
self-contradiction. The instrument was not missing; the reading step was.

**What the second review did contribute**, so the entry is a measurement and not
only an apology — three findings c274 did not make, all verified rather than
inferred:

| | |
|---|---|
| Coverage | `CLAUDE.md` is now chamber-agnostic, but `agents/academic.md` (activation gated on the chamber-provided **Medic**, `chambers/health/research/inbox/` hard-coded), `.claude/agents/archivist.md` (routing table, URN vocabulary, the whole Coach-log section) and `agents/publisher.md` (a five-path health translation manifest) are **baked into the image** and still assume one chamber — so a session is told at `:53` not to assume a chamber and handed a persona at `:40` that requires one |
| Plugin churn | `.retinue/` is the plugin root, and `sync-plugins.py`'s `trees_differ` counts any one-sided file as drift. Measured here: the cache is a byte-faithful copy of the whole root, dotfiles included, and `trees_differ` is `False` today; add the branch's westworld `INSTRUCTIONS.md` to a copy of that cache dir and it returns `True`. So a **prose edit triggers uninstall + install** within `PLUGIN_SYNC_INTERVAL` — it converges, but a session starting in that window sees no plugin |
| `entrypoint.sh:176` | `grep -c` prints `0` on stdout *and* exits 1, so the `|| echo 0` fallback fires too and the boot line reads `(0 0 chamber instruction file(s))`. Reproduced locally |

Four negative results were reported with them (the new example-chamber table is
accurate; the `@` import at `CLAUDE.md:782` is after the closing `-->` and so is
live, which is the failure mode that would have made the whole mechanism silently
do nothing; the generated aggregate never dangles; `/workspace` is not a git work
tree in either mount layout, so no git noise and no `.gitignore` entry needed),
plus one explicit *not checked* — whether an `@` import inside a hidden directory
loads in a non-interactive `claude -p` session, which is the mechanism's single
point of failure and needs a restart to settle.

**Operating rule, effective the next wake-up.** Before auditing any surface,
**read this file's `current_next_action` handover field**, and for a commit, PR or
branch **list the comments already on it** before writing one. Both are one step;
neither is a new instrument (c268 rule 2 — these are my own records, and neither
failed for want of a checker; it failed for want of being read).

