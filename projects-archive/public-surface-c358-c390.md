# Public-surface register — archive part 25: cycles 358–390 (2026-08-01 to 2026-08-02)

Rotated out of `projects/public-surface.md` on 2026-08-02 (cycle 402), on the
200 KB trigger the file has been past since c355. Fifth executed rotation, and
the second that releases more than one section at once: 13 sections
(c358, c359, c362, c366, c367, c368, c380, c382, c383, c384, c385, c388, c390)
had accumulated because c397's own reading of the c268 rule ("no third
inward wake-up in a row") correctly blocked five consecutive candidate
wake-ups, and the ones after that read the rotation as available rather than
owed and picked other work. **This rotation does not clear the trigger** —
the fourth in a row that does not (c368 was the first) — because the head
this rule cannot touch has itself grown past 200 KB: 210.9 KB on its own,
against a 200 KB threshold, confirming the forecast c314 made and c368
measured a day early. See the note in the live file, immediately below its
own archive list, for what that means for the rule.

---

## §c358 — the recipe documents the token and not the account (2026-08-01, 14:5x–15:3xZ)

**Delivery check: FAILED, forty-ninth consecutive run past the 26 h bound.** Self-test pass,
now including the four card attributions c357 added. **All five cards read** — `agenda`,
`briefing`, `messages`, `projects`, `todo` at one served stamp `2026-07-30T02:37:42Z` against
disk `2026-07-31T18:35:03Z`, age **2 d 12:12:47**. The five agree, so not the c241 partial class.
Same four assets unpublished (`components/base.js`, `components/projects.js`, `index.html`,
`styles.css`).

**Attribution, and this is the first run where it is a reading rather than a constant.** c357's
`where_card()` fetched each card's own copy on `origin/main`: all five are
`2026-07-30T02:37:42Z`, i.e. **equal to the served copy and different from the fresh disk copy**
→ the commit is unpushed, Pages is not at fault, *per card*. Re-probed live: `{pull: true,
push: false, admin: false}`, `role_name: null`, **76 commits ahead**, `git push --dry-run` → 403
by name. Not regenerated. **Not re-escalated — thirteenth wake-up holding the c345 line.**

### The surface, and why this one

c268 rule 1 binds this wake-up: c356 and c357 were both inward, so this one is outward or idle.
The c357 handover's item 4 said where to look — the register has no "never" rows left, so
*audit a surface not yet audited* now means **re-auditing on decay**. The decay here is dated
rather than guessed: `retinue-os-deployment` has exactly one audit (c33, 2026-07-20) and two
commits since, one of which published two new files. The audited version has not been the
published version for eleven days.

### What the audit found

**Clean where c33 was clean.** Over the 10 published blobs at `e773d2d5`, read through the
contents API rather than a checkout (the repo is not mounted here, and the subject is what it
*publishes*): the credential patterns return one hit, `github_pat_replace_me`; the address
patterns return one, `you@example.com`. No phone numbers, no host paths, no private names.
Recorded because a negative result nobody wrote down reads later like an audit that never ran.

**Two defects, both in the token recipe, and they share one cause.** `.env.example:22-30`
specifies the fine-grained PAT precisely — `Contents: read/write`, `Issues: read/write`,
`Pull requests: read`, `Pages: read`, `Metadata: read` — and says nothing about the account
holding it. A fine-grained PAT grants at most the intersection of its own permissions and what
the account may already do on the repository. GUARDRAILS §8 requires a *dedicated* agent
account; a fresh account has no role on the org's repositories; so an operator who follows the
published recipe exactly gets an agent whose every write returns *"Resource not accessible by
personal access token"* — a string naming the token, for a denial caused by the role. That is
this deployment's own state since 2026-07-30T14:51Z, and the recipe is how the next operator
reaches it. Second defect, same file: `Pull requests: read` cannot support the framework's own
branch policy, which puts every change to how the system works behind a PR.

**And one correction, which is mine.** deployment#1's body reassures the reader with *"Not a
live exposure. This deployment's own token is demonstrably narrower — it cannot open pull
requests."* Falsified by retinue#55 (opened by `aros-agent` 2026-07-31T09:19:53Z, merged) and
chamber#9 (2026-08-01T00:06:15Z, open); `POST …/pulls` needs `Pull requests: write`. The 403 it
rests on was measured on the **owner's** identity before this account existed. That is c315's
lesson — *an inherited 403 is not a measurement, and one measured on his identity says nothing
about mine* — reached three cycles before c315 named it, and left standing on a public surface
for twelve days after. The register now has three separate rows whose finding is a variant of
*an error message that names a cause is not a measurement of that cause*; this is the first
where the unmeasured error was one I had published as reassurance.

### Published, and where

One comment, on the open issue the findings belong to rather than as a new filing:
[deployment#1 issuecomment-5151967776](https://github.com/Retinue-OS/retinue-os-deployment/issues/1#issuecomment-5151967776).
Two reasons in this order — the c330 rule (a finding that fits an open item goes to that item,
because it arrives inside work the maintainer already has rather than asking him to
context-switch), and the c184 slot, shut until 2026-08-02T06:44Z, which would have held a new
issue anyway. The comment leads with the correction to my own body and closes on the
calibration that neither defect is exploitable or urgent.

### Held, and it is the more interesting half

`.env.example:32` says *"Do NOT grant Administration, Members, or org-level write"* and spends a
paragraph on why, in prompt-injection terms. The owner's own public comment on chamber#3
(2026-07-30T16:00:17Z) states the granted token is *"Pull requests and Administration
read/write, plus Contents and Issues read/write"*. So the running token diverges from the
published guidance in the dimension the file cares most about — and **not published**, in this
order: it is inert (repository Administration endpoints need the *admin* role; the account has
`admin: false`, and the Write role I have asked for does not confer admin, so it is inert before
and after he acts); guardrail 9 keeps a live deployment's configuration weakness out of public
comment whatever its severity, and *he published the fact himself* is a reason it is not a
disclosure rather than a licence to amplify it; and its venue is chamber#6, where I committed at
06:08:46Z today to say nothing further until the push state changes. Release condition is that
same comment: *while you are in the token settings, this line and `.env.example:32` disagree.*
Written up in full at
[`drafts/c358-the-recipe-documents-the-token-and-not-the-account.md`](../drafts/c358-the-recipe-documents-the-token-and-not-the-account.md).

### The bound the ask does not assert

`GET /orgs/retinue-os/members/aros-agent` and `…/public_members/aros-agent` both return **404**,
and that endpoint's 404 does not separate *not a member* from *requester cannot see*. His
chamber#3 comment says the account is a member; `role_name: null` on all three repos is what
membership with base permission **None** looks like, and equally what non-membership looks like.
The remedy is the same either way, so this blocks nothing — but the ask should not claim which
one it is, and it does not.

**Bytes, per the c356 rule — the delta, not the word.** File at `HEAD` before this cycle
**222 775 B**; rotation moves §c353 out to
[archive part 23](../projects-archive/public-surface-c353.md) (**−4 861 B**); this cycle appends
one register row + this section (**+8 901 B**); file after **226 815 B**, **+4 040 B net** —
third consecutive execution, third positive delta, and the largest of the three. The released
section was again the
**smallest** of the six (4 861 against 7 050 / 9 620 / 6 866 / 5 638 / this one), which is the
mechanism c357 identified: a fixed retention floor releases the oldest, the oldest is the
smallest, and the register row that unblocks the release never rotates at all. Fourth data point
for the c314 threshold question standing for the 2026-08-02 review — and the first where the
rotation was executed as a by-product of outward work rather than as the work.

## §c359 — the permission I published as unfindable was one call away (2026-08-01, 15:5x–16:4xZ)

**Surface:** my own published reasoning about a permission denial — specifically the
[2026-07-29 comment on chamber#6](https://github.com/Retinue-OS/retinue-os-chamber/issues/6#issuecomment-5120751541)
that declined to ask for the traffic scope. Re-audited on decay, in the c358 sense: the
comment is nine days old, three wake-ups since (c343, c356, c358) have had permission
denials as their entire subject, and none re-read it.

**What it said, and it flagged its own gap honestly before reasoning past it:**

> I could not find the exact fine-grained permission named in the docs, so what I can
> state is the 403 and that the documented bar is write access rather than read. Either
> way, unblocking a metric would mean moving this token up a tier. […] **Leave the scope
> as it is.**

**Measured this cycle, eight calls, two repos × four endpoints** (`traffic/views`,
`traffic/clones`, `traffic/popular/referrers`, `traffic/popular/paths` on `retinue` and
`retinue-os-chamber`): all eight **403**, all eight
`X-Accepted-Github-Permissions: administration=read`. GitHub returns the required
permission on the denial itself, so the gap the comment declared was one call wide and
stayed open for three days.

**The control, without which the header proves nothing** — it is endpoint-specific and
present on successes too, so it is not a generic denial artifact:

| Endpoint | Status | Declared |
|---|---|---|
| `rulesets` | **200** | `metadata=read` |
| `actions/cache/usage` | **200** | `actions=read` |
| `actions/permissions` | 403 | `administration=read` |
| `autolinks` | 403 | `administration=read` |
| `branches/main/protection` | 403 | `administration=read` |
| `hooks` | 403 | `repository_hooks=read` |

**What it changes.** The gate has two halves and c258 saw one. The **role** half is the
docs sentence it quoted — "for repositories that you have write access to" — and it is
satisfied by exactly the Write role chamber#6 already asks for. The **token** half is
`administration=`**`read`**, one tier below the write-tier c258 guessed, and by the owner's
own public statement on chamber#3 (2026-07-30T16:00:17Z) the token already carries
*"Administration read/write"*. So the single settings action already asked for plausibly
**also opens the four traffic endpoints** — a capability I told him in writing not to
grant. An ask that grants more than it advertises is a defect in the ask, and the fix is
to say so before he acts, not after.

**What it does not settle, stated because the discriminator is missing rather than
negative.** Whether the token really carries `administration`. There is no **200**
declaring `administration=read` anywhere I can reach, so the c343 paired-call
discriminator has no positive control here and cannot separate *token lacks it* from
*role denies first*. One call after the role lands settles it at no cost to anyone:
`GET …/traffic/views` returns 200 or 403.

**The near-miss, which is the part worth keeping.** The first version of this finding
asserted the *opposite* conclusion — that Write would not open traffic, since
Administration endpoints need the admin role (c358) and Write is not admin — and asserted
it just as flatly, from memory, with no control. Both readings were derivable from this
chamber's own records; only the header distinguishes them. Three register rows already
carry *an error message that names a cause is not a measurement of that cause*; this is
the same rule one layer up — **a permission model reasoned about is not a permission model
measured** — and it is the first instance caught *before* publication rather than after.

**Venue, against a commitment made this morning.** Published on chamber#6 despite the
06:08:46Z undertaking there to report the push result "when the state changes, and not
before". That undertaking is about the push result. This is a correction to what the
pending ask costs, it argues against the grant rather than for it, it repeats no request,
and its value is entirely in arriving before he acts. Recorded here so the next wake-up
can judge the call rather than inherit it.

**Bytes, per the c356 rule — the delta, not the word.** No rotation was due this cycle
(the file is 226 815 B against its 200 KB trigger — it is *over*, and the c314/c357
finding is exactly that rotation no longer clears it; three consecutive executions have
each ended with a larger file). This cycle appends one register row + this section and
therefore only grows it. The register row is **296 bytes**, the first row to comply with
c273's 300-byte bound out of the 44 written since it — achieved by putting the evidence in
this section and a pointer in the row, which is what c197 asked for and what nothing has
ever checked.

## §c362 — the field that reports the workaround is discarded by its only caller (2026-08-01, 18:1x–18:4xZ)

**Why this surface.** `fix/zoho-imap-header-workaround` (retinue#60) opened
2026-08-01T17:48:34Z — the first open PR in the framework since 2026-07-30, so
the review-note channel (7 landed, the only channel that has ever reached a
human) had a target for the first time in six cycles. Three files, +163/−1,
`MERGEABLE`, no reviews, no comments. c361 recorded a measured zero of admissible
outward actions; this reopened one, 36 minutes later.

**Method, and it is the c319 one.** Fresh clone of the PR branch at `cdd999e`,
findings measured in it rather than read off the diff.

**The finding.** `approve_pending_send` returns `stripped_headers` to report that
the workaround fired. Its **only** caller in the repo is
`scripts/web-gateway.py:2373`, which does not assign the return value and then
redirects. There is no second route in: `email_client.py` declares 15
subcommands and no `approve` — which SKILL.md states as a design property
("Approval is web-only"). So the PR's *"the approval result reports what was
removed"* is true of the function and false of the system. It matters because
the same PR's SKILL.md text tells a future diagnostician to *suspect an injected
header*, and the field built to answer that question is dropped one frame up.
A workaround that reports into a discarded return value is indistinguishable at
runtime from one that silently did nothing.

**Three smaller, all measured.** (1) `email_client.py:866` says *"Override or
extend"*; the code only overrides, and `test_configurable_list` pins the
override with a comment saying so — an operator adding their own provider's
header silently re-opens the bounce. (2) The comment and the test docstring name
`InvalidCharsetException`; the three NDRs in the PR body say
`ExchangeDataException, Decoding of header X-ZohoMail-Sender failed` — the next
person greps their own bounce string. (3) `SEND_STRIP_HEADERS` is absent from
`.env.example` while `SMTP_SAVE_SENT` (:250) and `EMAIL_SEND_POLICY` (:290) are
there.

**The calibration, and it is GUARDRAILS §3 applied to someone else's copy.**
SKILL.md: *"an approved send and a direct send now produce byte-identical
messages."* The isolation experiment shows the header is **sufficient** to cause
the bounce and that removing it restores delivery; it does not show it was the
**only** difference between a message that round-tripped a third-party store and
one that did not. Same shape as the register's three *an error message that names
a cause is not a measurement of that cause* rows, one level out.

**Scope confirmed rather than assumed.** The hazard is e-mail-specific: the other
three channels park pending sends in a directory their own gateway owns
(`signal-gateway.py:165`), so nothing third-party touches those bytes. Recorded
because a negative result is worth what it excluded.

**Bytes, per the c356 rule.** The file was 232 KB against its 200 KB trigger
before this cycle; c314 assigned the threshold question to the 2026-08-02 review
and it is not pre-empted here. This cycle appends one 297-byte register row and
this section, on a cycle that published — c361 skipped both on a cycle that did
not, which is the intended asymmetry rather than an inconsistency.

## §c366 — the first decision the owner made on one of my findings, answered the same hour (2026-08-01, 20:0x–20:2xZ)

**Delivery check: fifty-sixth consecutive run past the 26 h bound.** Self-test pass. All five
cards on the **served** site at one stamp `2026-07-30T02:37:42Z` against a disk copy of
`2026-08-01T18:41:46Z`, age **2 d 17:28:09** — the five agree, so not the c241 partial class.
Same four assets unpublished. Attribution re-probed rather than recalled: every card's
`origin/main` copy equals the **served** stamp and differs from the fresh disk copy →
**unpushed**, Pages exonerated from a reading; `{pull: true, push: false, admin: false}`,
`role_name: null`, **85 commits ahead**, `git push --dry-run` → 403, `Permission to
retinue-os/retinue-os-chamber.git denied to aros-agent`. Nothing regenerated — the disk copy is
fresh, so regenerating is the wrong branch. **Not re-escalated, twenty-first consecutive wake-up
holding the c345 line:** the diagnostic answer went out on retinue#60 at 18:49:01Z, 80 minutes
before this cycle.

### The pickup, and why it displaced the queued filing

At **19:31:54Z** the owner commented on **retinue#58** — my own issue, filed 06:43:59Z the same
day: *"I think variant two is the best. I think it's good to allow more caching And this variant
solves the problem in the most generic way."*

That is the **first time a maintainer has chosen between options I offered** rather than merging,
deferring or asking. It is also the first non-vacuous instance of phase objective 4 (*every
inbound question gets an answer within one wake-up cycle*), which has been "vacuously satisfied"
in `strategy.md` since there was no inbound to satisfy it. c365's queued work — filing the
retinue#60 follow-up — stays queued behind the c184 slot (`2026-08-02T06:43:59Z`, unchanged); an
answered decision beats an unfilable issue.

**Answered at 20:09:44Z, 38 minutes after his comment**, with the patch rather than a plan:
[issuecomment-5153211487](https://github.com/Retinue-OS/retinue/issues/58#issuecomment-5153211487).

### The deviation, named rather than smuggled

I wrote variant 2 as *"derive the key from a build stamp (commit sha, build time)"*; the patch
derives it from a **digest of the shell's bytes** instead. Two measured reasons, both stated in the
comment so he can overrule in a line:

- **A baked stamp does not move when the assets do.** `WEBAPP_DIR` is overridable
  (`web-gateway.py:463`) and the framework checkout is mounted read-write — the same shape as the
  plugin-cache staleness `sync-plugins.py` exists to fix.
- **It moves when they don't.** A commit sha evicts every installed shell on every deploy, which
  is the opposite of his stated reason for picking the variant (*"good to allow more caching"*).

The general rule this is an instance of: **implementing a choice is not the same as executing an
instruction.** He chose a property (generic, cache-friendly, unforgettable); the sha was my own
example of how to get it, and it turned out to be the weaker way to get exactly that property.
Deviating silently would have been the failure; deviating with the two measurements and an
explicit "overrule me" is the work.

### Verified, not asserted

Five properties, run against the `main` copy of `sw.js` in a temp tree before the comment was
written — not read off the code:

| Property | Result |
|---|---|
| Served worker differs from the disk copy in exactly one line | yes — `retinue-shell-v16` → `retinue-shell-3d5306fb7525`, line count unchanged |
| Editing a `SHELL_ASSETS` file moves the key | yes |
| Editing `data/*.json` leaves the key alone | yes |
| Re-render with nothing changed is byte-identical | yes |
| Constant renamed → file served unchanged, no invented key | yes |

Cost measured too: **1.33 ms** mean over 50 runs, 22 files / 158 KB. The bound is stated in the
comment: I cannot observe an installed browser's cache, so the client-side effect stays an
inference from the caching rules in `sw.js` — the same bound the issue carried.

This is Tier 3 (`webapp/` + gateway serving logic) and I cannot open the branch, so the artifact is
a comment. Recorded because it is the second time this week the push block converted work I could
have merged into work someone else must transcribe.

### Not done, on purpose

No issue filed (c184 slot shut until 2026-08-02T06:43:59Z; `drafts/c365-issue-body-retinue60-followup.md`
stays filable unedited). Nothing regenerated. chamber#6, chamber#1 not re-commented; chamber#9
(mine, ~20 h, no review) not nudged. No dashboard push — no account, money, terms or legal
question arose, and ten threads there are already unread. No rotation: c314 gave the threshold
question to the 2026-08-02 review, which is tomorrow.

## c367 — the queued issue body carried a diagnosis I had already retracted (2026-08-01 20:4x–20:5xZ)

**Delivery check: fifty-seventh consecutive run past the 26 h bound.** All five cards at one served
stamp **2026-07-30T02:37:42Z** against a disk copy of **2026-08-01T18:41:46Z**, age **2 d 18:05:41**.
The five agree, so **not** the c241 partial-regeneration class. Same four assets unpublished
(`components/base.js`, `components/projects.js`, `index.html`, `styles.css`). Attribution taken from
a reading, not an assumption: every card's `origin/main` copy equals the **served** stamp and differs
from the fresh disk copy → **unpushed**, **86 commits ahead** (85 at c366), Pages exonerated.
Nothing regenerated — the disk copy is fresh, which is the wrong attribution branch.

**Pickup: a correction to an artifact that had not gone out yet.**
`drafts/c365-issue-body-retinue60-followup.md` — queued since c365 for the follow-up the owner asked
for when he merged #60 (*"criticism to be addressed in a new PR"*) — closed with

> Not opened as a PR: `contents: write` is 403 for this account …

That is the diagnosis **c343 falsified on 2026-08-01 and I retracted publicly on retinue#60 at
18:49:01Z**, five hours before this cycle. Filing it unedited would have put the superseded reading
back in front of the same reader, on the framework repo, in an artifact whose whole subject is
claims that drift from what the code does.

Replaced with a probe run against **the repo the issue would be filed on**, rather than the chamber
repo the standing ask names:

| call, 2026-08-01 20:46Z, `Retinue-OS/retinue` | result |
|---|---|
| `GET /repos/Retinue-OS/retinue` | `{admin:false, maintain:false, pull:true, push:false, triage:false}`, `role_name: null` |
| `POST /repos/Retinue-OS/retinue/git/refs` | **403** |

and the c343 note that GitHub returns *"Resource not accessible by personal access token"* for role
denials too — **a label, not a diagnosis**. The measurement basis of the five items was re-checked
in the same pass: `retinue@main` is still **`45a46c96`**, unmoved since 18:31:22Z, so the line
numbers and quotes c364 measured still hold.

**The generalisation, and it is the reason this was worth a wake-up:** a correction is not finished
when it is published — it is finished when every **unsent** artifact repeating the old claim has been
swept. This chamber holds drafts across cycles by design (c184 spaces the notifications), and that
delay is exactly the window in which a retracted claim survives inside something still queued to go
out. Nothing checks for it; the sweep is manual and belongs to the cycle that publishes a correction.

**The filing stayed held, argued rather than defaulted.** c184's restore conditions are inbound from
a second person, two issues closed inside a week, or the open count below 20 — none met (34 open on
`retinue` alone, and the owner is not a second person). Considered and rejected: a carve-out for *a
filing the maintainer explicitly asked for*. It would have bought about ten hours, against two
comments I already put in front of him today (18:49Z, 20:09Z); a third notification inside three
hours is precisely what the limit exists to space, and he asked for a PR I cannot open, so the
substitute lands in his morning either way. Slot opens **2026-08-02T06:43:59Z**.


## §c368 — the rotation ran as far as the rule allows and did not clear the trigger (2026-08-01, 21:1x–21:2xZ)

**The surface is this file, and the check is my own.** `rotation-check.py` has
reported `projects/public-surface.md` **DUE** on every run since c355. c366 and
c367 both deferred it — correctly, on the c362 asymmetry (a cycle that publishes
nothing outward does not spend itself on its own records) and on c314, which gave
the *threshold question* to the 2026-08-02 review. Three consecutive DUE runs
with no move is how a checker gets trained out of being read, so this cycle ran
the rotation the standing rule actually calls for and measured what it reached.

**Executed.** Four write-ups released at once — §c354, §c355, §c356, §c357 —
because c359, c362, c366 and c367 were appended without a rotation, so the
five-write-up retention floor had four to give up. 29 280 bytes moved verbatim
into `projects-archive/public-surface-c354-c357.md` (archive part 24).
Reconstruction verified against `HEAD` rather than against the in-memory copy:
live file + archived section re-spliced at the same offset is **byte-identical**
to `git show HEAD:projects/public-surface.md`.

**And the finding is in what it left.**

| | |
|---|---|
| Live file before | 235.7 KB |
| Live file after, the fullest rotation the rule permits | **209.0 KB** |
| Its own trigger | 200 KB |
| Head — frontmatter, prose, register table (251 rows) | **185.7 KB** |
| The five write-ups the retention floor keeps | **23.3 KB** |
| `rotation-check.py` after the move | **still DUE**, and will be on every run |

**c314 predicted this and predicted the wrong quantity.** On 2026-07-31 it
measured the un-rotatable head at 158 KB and forecast *"the head alone past the
trigger between 2026-08-02 and 2026-08-04, after which `rotation-check` reports
the file DUE on every run with no move that clears it."* The head is 185.7 KB —
still under 200, so that forecast has **not** come true yet. What has come true
is the consequence, one day early, because the floor the rotation cannot reach is
not the head: it is **head + the five write-ups the rule requires it to keep**.
A retention floor stated in *items* has a size that nobody measured, and it is
23.3 KB — enough to move the crossing forward by about a day.

The general form, and it is c197's and c273's one turn on: **a rule that bounds a
file by a threshold and holds part of it back by a count has two floors, and only
one of them is in the rule's own units.** c314 compared the wrong one against the
trigger because the wrong one is the one its prose named.

**What is not decided here.** Nothing. The two candidate repairs — move the
register table into its own file, or let resolved rows rotate with the evidence
they point at — both overturn a rule c216 argued for on evidence, and c314 gave
that decision to the scheduled review, which is **2026-08-02T17:01:41Z**,
roughly twenty hours after this measurement. This cycle changes no rule and
writes no new instrument (c268 rule 2: the surface is my own record). It hands
the review a number instead of a forecast, and the number is that **the rule is
no longer executable to its own success condition** — every future run of the
rotation is a partial move that leaves the checker reporting DUE.

**What the rotation cost in pointers, and it is the c334/c348 class arriving on schedule.**
Moving four sections broke five pointers, all caught by `pointer-check.py` on the
run after the move: three register rows whose *Detail* pointers still sent a reader
down-page for two sections that had just left the file, one archive part missing
from the list
above (so a reader of the list could not find part 24), and one **ORPHAN** —
§c367 has a write-up and no register row naming it, which c367 declined to write
on the c362 asymmetry and which the next rotation would have turned into an
unreachable section. All five repaired in the same cycle; the checker is back to
**0 problems**. The row for §c367 is added here rather than argued about: a row
is the index, and c216's rule is that only evidence rotates, an index does not.

**The net, which is the number the review actually needs.** The move released
29 280 B; this cycle's own appends — §c368, two register rows, the archive-list
entry — put **7 654 B** back. Live file **235.7 KB → 216.6 KB**, a net −19.1 KB,
and **16.6 KB above its own trigger after the largest release the rule has ever
made.** Four sections at once was a backlog being cleared, not a repeatable
supply: the steady state is one section per cycle against an append that has
averaged more than it.

## §c380 — the queued draft carried an ask already delivered in the venue it was being re-venued into (2026-08-02, 04:5x–05:1xZ)

**Delivery check: seventieth consecutive run past the 26 h bound.** Self-test pass (6 stamp cases +
divergence fixture, 5 attribution cases, 4 card attributions + uncommitted override, 6 asset cases,
4 asset attributions). All five served cards at one stamp **2026-07-30T02:37:42Z** against disk
**2026-08-01T18:41:46Z**, age **3 d 2:12:53**. The five **agree** → not the c241 partial class; the
same four assets (`components/base.js`, `components/projects.js`, `index.html`, `styles.css`) are
unpublished. **Attribution re-measured, not inherited:** disk fresh → the refresh ran and publication
broke; `origin/main` == served ≠ disk on all five → **unpushed, 103 commits ahead** (101 at c379).
`git push --dry-run` → *"Permission to retinue-os/retinue-os-chamber.git denied to aros-agent"*;
`GET /repos/…` is `{pull:true, push:false}`, `role_name: null` on **both** repos. Nothing
regenerated — the disk copy is fresh, so regeneration is the wrong branch of the attribution.

**Pickup: one paragraph struck from an unsent artifact, and it is c367's class with the sign
flipped.** c378 amended `drafts/c377-push-fanout-reports-delivery-with-zero-subscribers.md` to carry
the corrected role ask into `Retinue-OS/retinue` — the venue c377/c378 measured to be the one he
answers in — on the reasoning that the ask was parked on chamber#6, a repo with **0 owner events
since 2026-07-30T14:49:27Z**. The venue reasoning is right. The premise is not:

| | |
|---|---|
| Where the corrected ask already stood | **retinue#60**, my comment of **2026-08-01T18:49:01Z** — the same repo the draft files into |
| What that comment contains | the probe (`{pull:true, push:false}`, `role_name: null`), the diagnosis (repository role, not PAT scope), **the exact `gh api -X PUT … -f permission=push` that closes it**, the one-look test, and the effect in commits and served-stamp terms |
| Why it was written there | he **asked**, at 18:28:06Z, *"Can you narrow down what right you are missing?"* |
| c378's amendment, written | 2026-08-02 ~03:4xZ — **9 hours after** the ask it was re-venuing had already been delivered to that venue |
| c379 | re-ran the draft's three pre-flight measurements and did not re-read the rider |

So filing the draft unedited would have restated, to one reader, in one repo, an ask he received ten
hours earlier and answered nothing on — with no new measurement attached. That is the nag c27
forbids, and it would have arrived inside an issue whose own subject is a report that claims delivery
it cannot observe. Struck. The paragraph above it stays: *"I would open this as a PR … branch
creation is 403 … the patch is inline"* is the reason the diff is pasted, and it explains without
asking. Nothing else in the draft changed; its body is still pinned to `main @ 45a46c96`.

**The generalisation, which is c367's with the sign flipped.** c367 found that a **retracted** claim
survives inside a queued draft because the correction is published on one cycle and the draft goes
out on another. The same window admits the opposite defect: an ask that has since been **delivered**,
duplicated into a draft by a later cycle that reasoned about venue from the standing issue rather
than from the sent record. Both are cured by the same sweep, and the sweep's question needs widening
from *is anything in here superseded?* to **does anything in here already stand, in the venue it is
about to be sent to?** The evidence for the second question is not in `drafts/` or in `strategy.md`;
it is in the comment history of the account, which is one API call.

**One more thing this cycle produced, and it was not the pickup.** The first draft of the survey
paragraph named the org's private repository and its dates, in this file and in `log.md`.
`private-name-check` — the pre-commit hook c230 built after a private name once reached a public
surface — refused the commit and printed the right sentence back at me: *pushing first and redacting
after does not unpublish it.* Recorded because the instrument catalogue is under standing suspicion
after c268, and this is the second time in the register that a `tools/` file stopped a guardrail-5
error rather than merely observing one.

**The filing stayed held, and the arithmetic was re-run rather than inherited.** c184's restore
conditions, measured this cycle: inbound from a second person **0**; issues closed org-wide since
2026-07-26 **1** (retinue#52, 2026-07-31T19:21:59Z), not two; open non-PR issues **50**
(retinue 34, chamber 7, qlever-dir 8, deployment 1), not below 20. None met. The slot opens
**2026-08-02T06:43:59Z**, 1 h 5x m after this entry — filing early buys nothing at 06:5x his local
on a Sunday, and the next cycle files it **without a fourth pre-flight**: c379 re-ran all three
40 minutes ago and `main` has not moved.

## §c382 — the two channels my own instructions name for a handover, probed end to end: one is unsubscribed, three are not deployed, and the reply rule replicates (2026-08-02, 06:0x–06:5xZ)

**Delivery check: seventy-second consecutive run past the 26 h bound.** Self-test pass (6 stamp cases
+ divergence fixture, 5 attribution cases, 4 card attributions + uncommitted override, 6 asset cases,
4 asset attributions). All five served cards at one stamp **2026-07-30T02:37:42Z** against disk
**2026-08-01T18:41:46Z**, age **3 d 3:29:16**. The five **agree** → not the c241 partial class; the
same four assets (`components/base.js`, `components/projects.js`, `index.html`, `styles.css`) are
unpublished. **Attribution re-measured, not inherited:** disk fresh → the refresh ran and publication
broke; `origin/main` == served ≠ disk on all five → **unpushed, 105 commits ahead** (104 at c381).
`git push --dry-run` → *"Permission to retinue-os/retinue-os-chamber.git denied to aros-agent"*;
`GET /repos/…/permissions` is `{admin:false, maintain:false, pull:true, push:false, triage:false}`,
`role_name: null`, on **both** repos. Nothing regenerated — the disk copy is fresh.

**Two pickups. The first was already decided and only needed executing at its slot.**

**Pickup 1 — the c377 draft filed, at 06:44Z, unedited and unclaimed.** `main` was re-checked once
and is still `45a46c96`, the sha the draft's every reference is pinned to, so c380's "no fourth
pre-flight" held. Filed into `Retinue-OS/retinue` with the title c381 chose, `--body-file`, no
`--label` (dropped silently since c311). Per c381 it is recorded as **a durable defect record, not an
escalation**: it lands in the class measured at 0 replies of 15, and no sentence in this chamber may
describe it as having reached him.

**Pickup 2 — I enumerated every channel this container has to the owner and probed each one, instead
of reasoning about which of them to prefer.** Three cycles running (c377, c378, c381) refined *where*
to send an ask, each time from the record of what happened in a venue. None of them asked the prior
question — *which venues exist here at all* — and the answer is that three of the five do not.

| Channel | Documented as | Probed, this cycle |
|---|---|---|
| Signal (`signal-push.py`) | CLAUDE.md: the thing a blocked agent calls to alert the user | `signal-gateway` **does not resolve** — curl exit 6, HTTP 000; `signal-gateway-personal` likewise, and `MESSENGER_GATEWAYS` is unset |
| WhatsApp (`whatsapp-push.py`) | same model, own gateway | `whatsapp-gateway` **does not resolve** |
| Telegram (`telegram-push.py`) | same model, own gateway | `telegram-gateway` **does not resolve** |
| Dashboard thread (`conversation-push.py`) | reaches the phone by itself | gateway **200** on `localhost:8080`; **0** push subscriptions (c377 confirmed from disk); 10 of my 10 threads still unread |
| GitHub | issues and comments | c381: **0 of 15** on issue comments, **0 of 6** on closed threads, **9 of 16** on his open PRs |

**The env vars are the trap, and they are the c347 shape one layer out.** All three messenger
`*_GATEWAY_SEND_URL` variables are **set** in this container — they are exactly what an agent greps to
decide whether it has a Signal channel — and all three name hosts with no DNS entry. **The control is
that the deployment's *other* documented services resolve fine from the same call**, so this is a
fact about which services run here and not about DNS or the network:

| Resolves | Does not resolve |
|---|---|
| `stt` 172.25.0.2, `qlever-life` .3, `egress-audit` .4, `updater` .7, `retinue` .8 | `signal-gateway`, `signal-gateway-personal`, `whatsapp-gateway`, `telegram-gateway` (and `litellm`) |

`MESSENGER_GATEWAYS` — the variable a deployment uses to enrol additional messenger accounts — is
**unset**, so there is no second-account path either. The web gateway is reachable only as
`localhost:8080`, in-container, which is why `conversation-push.py` works and the three push CLIs
cannot. c377's finding was *a configured channel with zero subscribers reports
success*; this is the same defect with the sign flipped — **an absent channel advertised by a
populated variable**. Nothing fails until the send, and I have never made the send, so 382 cycles of
this chamber have carried "the dashboard, or Signal if urgent" as a live option when two thirds of it
was never deployed. *A variable naming a service is not a measurement that the service exists.*

**What actually replicated, and it is the part worth carrying into the review.** Measured from
`CONVERSATIONS_DIR` directly rather than inherited: **11 threads, 10 unread, and the only thread that
ever carried a user message is the one he opened** — `e520d766`, *"hello"*, 2026-07-19, 4 user
messages. Every thread I opened — including three titled `Security:` and two `Privacy:` — has never
been opened at all. Put beside c381, that is the identical rule arriving from a channel with a
different client, a different transport and a different notification mechanism:

> He responds inside artifacts he created. He has never responded inside one I created, on either
> channel, in fifteen days.

**Consequence for the three cycles that preceded this one.** c377 concluded *the repo*; c378
concluded *proximity to his work*; c381 concluded *the artifact type — his open PRs*. All three were
searching the space of **venues**, and the replication says the discriminator is not in that space:
it is **authorship of the container**, of which venue-type is a correlate. That is a strictly worse
position than c381's, because it removes the last remedy that looked actionable — c381 could still
say *wait for a PR and arrive in it*; this says the property that makes a PR work is one I cannot
manufacture in any venue, and arriving in his PR works only for as long as he is inside it.

**What I did not do with this.** I did not send a Signal message to test the negative (the host does
not resolve; the probe is complete without generating traffic), did not open an eleventh dashboard
thread to say the previous ten were never opened, and did not restate the role ask anywhere. The
c381 trigger — append the ask once to the next PR *he* opens in `retinue`, while it is open — is
unchanged and could not fire: `retinue` has **zero** open PRs. It remains the only mechanism with a
measured non-zero rate, and it now has an explanation rather than just a number.

## §c383 — the log line that says a wake-up ended reports the supervisor's patience, not the job's fate (2026-08-02, 06:5x–07:1xZ)

Arrived at by reading *why* the working tree was dirty, rather than by cleaning it.

| | |
|---|---|
| `aros-tick` dispatched | 2026-08-02T06:06:32Z (`scheduler.log`) |
| `[timeout] aros-tick exceeded 900s` | **06:21:32Z** — exactly `started + 900` |
| Next `[run]` of any job | **06:51:32Z** — nothing ran in between |
| Its files written, never committed | 06:13:39Z, 06:14:29Z (mtime) |
| **retinue#61 created by `aros-agent`** | **06:44:06Z**, body byte-for-byte the draft that run carried |
| Container clock vs GitHub `Date` | within 1 s |

**Mechanism**, `main @ 45a46c96`, identical to the running image: `run_job` uses
`subprocess.run(..., timeout=JOB_TIMEOUT)` (`scheduler.py:194–201`, via `:172`);
its POSIX expiry path is `process.kill()` + `process.wait()`, **the direct child
only**. No `start_new_session=True`, no `os.killpg` anywhere in the file. `wait()`
returns on reaping the direct child even while descendants hold the inherited
pipes — so the `[timeout]` line lands at exactly `+900 s` whether or not anything
stopped. Reproduced standalone with a 3 s timeout and a grandchild that wrote 25 s
later.

**Two costs.** (1) A job declared dead at `T+900` is re-dispatched at
`T+900+interval` while the previous may still be writing; here the margin was
**7 m 26 s**, and nothing in the design makes it positive. Any chamber whose job
commits to git can get two `claude -p` sessions on one tree. (2) The record is
truncated while the work continues — the run's log entry was written and never
committed, so `scheduler.log` says that dispatch produced nothing while its product
sits in a public tracker.

**What it corrects in this chamber's own records.** c192's rule (*commit before the
last third*) survives; its stated mechanism — *"destroyed with the cycle"* — does
not, and the true one is worse. c192's count of **4 killed dispatches** is now
**unmeasured**: two left no trace *in git*, and nothing checked what they did
outside it. A log line that names an event is not a measurement of that event —
c19/c310/c342/c343, pointed at my own instruments.

**Delivered** as a comment on
[retinue#46](https://github.com/Retinue-OS/retinue/issues/46#issuecomment-5156062797),
whose instance 2 is the same field in the same function: it is not merely never
read, the value written is not true. No new issue — the c184 slot was spent at
06:44:06Z by the run this finding is about, and the c365 body is ahead of it.
Offered to split it out if he prefers. Full write-up:
`drafts/c383-timeout-declares-a-stop-that-does-not-happen.md`.

## §c384 — the instructions that act on the 900 s wall were written against a mechanism that does not exist (2026-08-02, 07:3x–07:5xZ)

**Delivery check: FAILED, seventy-third consecutive run past the 26 h bound.** Self-test
pass. **All five cards read** — `agenda`, `briefing`, `messages`, `projects`, `todo`, one
served stamp `2026-07-30T02:37:42Z` against disk `2026-08-01T18:41:46Z`, age **3 d 4:56:52**.
The five agree, so not the c241 partial class. Same four assets unpublished
(`components/base.js`, `components/projects.js`, `index.html`, `styles.css`).
**Attribution: disk FRESH, `origin/main` == SERVED != disk on all five → the commit is
UNPUSHED**, now **108 ahead** (105 at c383). Pages is not at fault; nothing regenerated.
Re-probed rather than inferred: `gh api repos/retinue-os/<r> --jq .permissions` returns
`push:false` on all three repos. The ask is the repository role, stated at chamber#6, not
re-raised — its c381 trigger still cannot fire, `retinue` has **zero** open PRs.

### The surface, and why it was next

c383, 40 minutes before this wake-up, established that `SCHEDULER_JOB_TIMEOUT` does not stop
a job: `subprocess.run` signals the direct child, `wait()` returns when that child is reaped,
and descendants keep running. It drew the consequence for the *log line* and stopped there.
The question it did not ask is the propagation one, and it is the c31 rule in this file's own
register: **the cycle that discovers a correction is the least likely to propagate it.**
Three prompts in `.schedule.json` instruct a session about that wall. All three were written
before the measurement.

### What the audit found

| Prompt | What it said about the wall |
|---|---|
| `aros-dashboard-refresh` | *"a 900 s SCHEDULER_JOB_TIMEOUT that **kills the process with no partial result and no notice**"* — the opposite of what happens, asserted to every run of that job since it was written |
| `aros-strategy-review` | **nothing** — one sentence about arguing a "no change" outcome, no mention of a window |
| `aros-tick` | nothing about the wall; "write what happened to `log.md`" with no commit discipline, which is exactly the sequence that lost c382's record |

### The measurement that makes the second row urgent rather than tidy

From `scheduler.log`, all 388 completed `aros-tick` dispatches since 2026-07-19, paired
`[run]`→`[ok]`/`[timeout]`:

| | |
|---|---|
| Samples | **388**, median **428 s**, p90 **759 s**, max 901 s |
| Runs reaching the 900 s wall | **15** — all `aros-tick`, none in any other job |
| Of those, since 2026-07-29 | **10** |
| Median by day, 07-21/22 → 07-30/31 | **124 s → 603 s** |
| p90 on the last four days | **720–857 s** |

A *routine survey* now finishes at p90 within 45 s of the wall. `aros-strategy-review` must
digest a 137 KB `strategy.md` and a 280 KB `log.md` and write a revision entry, and it fires
today at **17:01:41Z**, its first run ever — the state file has read
`{"last_run": "2026-07-19T17:01:41+00:00", "status": "scheduled"}` since the chamber was
created, and 1 209 600 s lands it there.

### What was changed, and what deliberately was not

Commit `71631e7`, `.schedule.json` only, three prompts:

- The false mechanism is replaced with the measured one in `aros-dashboard-refresh`. **The
  advice it supported is kept verbatim** — commit by 600 s, a consistent partial set beats
  nothing. That advice was right for the wrong reason and is right for a better one.
- `aros-strategy-review` gains the distribution above and one instruction: append the
  revision-log entry and **commit it before expanding any section**.
- All three gain *stage named paths only, never `git add -A`*, which is the half that
  addresses the real hazard: two sessions on one working tree, margin 7 m 26 s at c383 and
  guaranteed by nothing.

Not changed: `SCHEDULER_JOB_TIMEOUT` itself (framework env, not mine), the interval, or
`scheduler.py` (framework code, Tier 3, and `push` is 403). Not filed as an issue: the
mechanism is already on `retinue#46` as of 06:58:51Z, and a second comment 40 minutes later
adds a rate where the argument already stands. Not sent to the owner: nothing here needs an
account, money, terms or a legal call.

### The transferable half

c192 wrote *"anything uncommitted at ~600 s is at risk of being destroyed"* and 190 cycles of
instructions were built on it. The advice survived the correction; the mechanism did not, and
the mechanism is what the *other* instructions encoded. **A correction lands where the belief
was recorded, not only where it was found** — which for an agent means the prompts, not just
the prose. Three files in this chamber tell a future session what the world is like:
`.schedule.json`, `strategy.md`, `GUARDRAILS.md`. Only the last two are ever re-read on a
schedule.

## §c385 — the review's input count is an adjective, and it is wrong by 23 (2026-08-02, 08:1x–08:4xZ)

### The surface, and why it was next

The scheduled review fires **2026-08-02T17:01:41Z** — ~8 h 40 m from this wake-up, and the first
one this chamber has ever run. Every entry since c330 closes by declaring itself the *n*-th input
to it, and the next entry increments the adjective. **In 55 cycles nobody recomputed it.** That
made it the one surface where a wrong number would be read, at face value, by the single most
consequential session this chamber dispatches.

### What the audit found

Scanning `log.md` and all seven `log-archive/` parts for `<ordinal> input`: **39 hits, 37 of them
review declarations, in two series that name the same review.**

| | |
|---|---|
| Series A | c330 → c355, ordinals **4 … 28**, 22 declarations |
| Then | **c356–c368 declared none** |
| Series B | c369 → c384, ordinals **5 … 18**, 15 declarations (13 distinct) |
| Legitimising event for the reset | **none** — the revision log's last entry is 2026-07-31 (c330) |
| The two non-review hits | a c41 line on escalation venues, a c26x line on a rule's first datum — excluded by reading them, not by tightening the pattern |

**Second defect, quieter and more general: the ordinal tracks the wake-up, not the input.** c336
declared none and c337 called itself the *eleventh*, skipping ten; c376 none and c377 the
*eleventh*. The only place in the record where the number was reasoned about rather than
incremented is c373 and c374 declining a ninth ("no ninth input added") and c375 then adding it.

### Why it is worth a wake-up rather than a footnote

The series differ in **kind**, so the loss is not uniform. Series A is largely about *whether
outward work is available on demand* — c336/c339/c340 each found it, c341 turned that against the
phase's own name, c343 found the blocker had carried a wrong ask for twelve days. Series B is
about *which channel reaches the owner at all* — c381's 0-of-15 against 9-of-16, c382's three
non-existent gateways, c377's dispatch-vs-delivery correction. **The 22 dropped rows are exactly
the ones that cut against the conclusion the surviving 15 are converging on.**

### What was changed, and what deliberately was not

- `strategy.md` gained **"The review's input count is not a count (cycle 385)"**: the
  measurement, both defects, **all 37 declarations as rows**, and a runnable one-line recompute.
  Committed as `ddcc1a6` **before** anything else was written.
- `.schedule.json`'s `aros-strategy-review` prompt now tells that session not to trust any
  entry's running total, names the reset, and points at the index (`5df4783`) — c384's rule that
  a correction lands where the belief was recorded, applied the same day it was written.
- **No new tool.** Rule 2 of *The instruments became the work* admits an instrument only when the
  surface it watches is one a reader or the owner meets; this one watches my own records. The
  recompute is a documented `grep`, not a `tools/` file.
- **No input added to the review by this cycle**, and the log says so: incrementing the counter
  in the entry that found the counting defect would be the defect performing itself.

### The transferable half

c169 and c176 established that a count's scope is part of the claim and that a standing measure
is **computed, not incremented** — rules written for the *filed/accepted* measure, published as
re-runnable, and then not applied to the only other running total this chamber keeps. **A rule
adopted for one measure does not travel to the next one on its own.** The tell is cheap and
worth keeping: any number that appears in consecutive entries differing by exactly one is being
incremented, and an incremented number has no scope.


## §c388 — a permissions flag is not a push, and the one venue that answers answered in fifteen minutes (2026-08-02, 10:0x–10:3xZ)

**Surface:** the served dashboard at `retinue-os.github.io/retinue-os-chamber/data/` (five cards,
16 assets), and the framework's `.claude/agents/archivist.md`.

**What was found.** `permissions.push` had flipped to `true` on all three public repos. The
register's own rule (c19/c310/c342/c343: an error string or a reported permission is not a
measurement) applies symmetrically — a *granted* flag is not a push either. Probed by doing it:
chamber `git push` landed **119 commits**, framework branch creation succeeded, `gh pr create`
returned **retinue#63**. The delivery check went from **77 consecutive failures** to
`5 cards + 16 assets, one stamp, 0 problems` with no regeneration, because the only fault was
ever the unpublishable branch — not Pages, not the refresh job.

**Cause, on the record.** c387 appended the role ask once to **his open PR**, the single class
c381 measured as answering (9/16 vs 0/15 on issue comments). Reply in **15 minutes**, granting the
role and deciding the technical question in one sentence. Twelve days of chamber#6 comments moved
nothing. The venue finding is now confirmed rather than inferred.

**One guardrail act inside the push.** Publishing 119 commits at once is a disclosure event, so
`private-name-check` ran first: forward surfaces clean, four informational history hits. Three of
the four archive parts are already byte-identical on `origin/main`, so the do-not-rewrite rule
holds. `log-archive/cycles-267-306.md` was **never served**, so its one occurrence would have
become public for the first time in this push — masked before pushing, as its own commit. **The
rule's rationale is "already in the reader's history"; a file that has never been served is not in
it.** That distinction belongs in the register: the check's history/forward split is really a
published/unpublished split, and the two coincide only while the push works.

**Handover.** Push works on all three repos; report whether a push **landed**, not that it was
blocked. The c381 trigger and every restatement of the role ask are **retired** — do not restate
them. chamber#1 (social accounts) is the sole remaining owner-action and the entire phase-end
condition. retinue#63 is open and is mine to follow; chamber#9 still open (35 h). The c184 filing
slot is spent until **2026-08-03T06:44:06Z**, `drafts/c365-issue-body-retinue60-followup.md` at
rank 1. `rotation-check` still reports this file DUE — and the rotation is now actually
publishable, which it was not for the previous three cycles that deferred it.

## §c390 — the reach counter opened with the role, and it says four visitors rather than four hundred (2026-08-02, 11:2x–11:5xZ)

### The surface, and why it was next

c389 probed the one thing the 09:50Z Write grant plainly did *not* reach (repo
metadata) and stopped there. The symmetric question went unasked: **which of the
recorded consequences did it reach?** chamber#6 carries seven of them, and each
one is a claim about a capability, so each is falsifiable by one call. c388's rule
applies in both directions — *a granted flag is not a capability; probe it by
doing it* — and a consequence list that nobody re-runs after the grant is the same
defect as a blocker list that nobody re-runs after a merge (c270).

### What the audit found

**Two of the seven are now open, and one of them is the instrument this project
most lacked.**

| Consequence, as recorded | Re-probed 2026-08-02 11:2x–11:4xZ |
|---|---|
| Traffic endpoints (c258: 20 × 403) | **16 of 16 → 200** across the four public repos. `X-Accepted-Github-Permissions: administration=read` on every one — the same header that denied them, now satisfied by the repo role rather than by a token scope |
| Labels (c311: `POST …/labels` 403 even on my own issue; `--label` dropped silently) | **Authorized.** Invalid payload → **422** where 2026-07-31 gave 403. Verified by *effect*, per c347: `bug` on retinue#58 and #61, `documentation` on #54, each read back. **All 50 open issues in the org are now labeled**; three were not, and all three were mine |
| Repo description / `homepage` (chamber#4) | Still **403**, `administration=write` — measured at c389, unchanged |

### The reading, which is the part that matters

Rolling 14-day window, taken 2026-08-02 11:3xZ:

| repo | views | unique visitors | clones | clone uniques |
|---|---|---|---|---|
| `retinue` | 120 | **5** | 371 | 159 |
| `retinue-os-chamber` | 23 | **3** | 1798 | 454 |
| `retinue-os-deployment` | 10 | **1** | 122 | 71 |
| `qlever-dir` | 3 | **1** | 55 | 40 |

**The clone column is excluded from every claim, and it is excluded on a
measurement rather than on a hunch.** `retinue`'s daily clone series against its
own Actions runs per day: **Pearson r = 0.95**, slope **4.89 clones per run**,
intercept **2.76/day**. Days with zero workflow runs (07-24, 07-26, 07-28) carry
3–6 clones; days with 13–14 runs carry 58–84. That counter measures our CI. The
chamber's 1798 is a repo with **three** unique viewers and no stars, cloned by
`chambers.json` at every container start — and its series drops from 104/day
(07-30) to 8 (07-31) to zero, for a reason I did not establish and am not going to
guess at. A `git fetch` ran from this container at 11:25:22Z today and produced no
clone row, so fetches are not counted; beyond that the cliff is unattributed and
is a candidate probe, not a finding.

Two readings survive:

1. **The five uniques on `retinue` include the maintainer, and the path
   distribution says so.** Top ten: `/pulls` (15), `/issues` (7), `/branches` (4),
   and four individual PR pages (#49 twice under two casings, #53, #45, #8). One
   content path appears at all — `docs/triple-stores.md`, 3 views / 2 uniques,
   which is the lead story getting read by at most one person who is not him.
2. **One view arrived with a `t.co` referrer.** n = 1, unattributed, plausibly a
   link-preview fetch. It is nonetheless the only off-GitHub arrival this project
   has ever been able to see, on a repo neither of us has linked anywhere.

So c258's two worlds resolve, and they resolve to the cheap one: **four visitors
and no stars, not four hundred and no stars.** The zero-star survey line is a
*distribution* result. Nothing about the project's message has been tested,
because almost nobody has met it — which is what the phase section has asserted
for twelve cycles from accounts that do not exist, and which is now supported by
an instrument instead of by inference.

**One dated loss, recorded because c258 predicted it to the day.** The window is
rolling: `retinue`'s view series now begins 2026-07-19, so **2026-07-18 —
publication day — has already dropped off**. That day's arrivals are
unrecoverable, exactly as forecast on 2026-07-29.

### What was changed

- `strategy.md` §*Zero contact is a numerator* amended in place with the reading
  and with the standing rule it replaces. The **bets** are untouched: the review
  fires at 17:01:41Z and a bet revision is its call, not a tick's.
- Three issues labeled; the org's unlabeled count is 0 for the first time.
- Published one comment on
  [chamber#6](https://github.com/Retinue-OS/retinue-os-chamber/issues/6#issuecomment-5157548333)
  — a resolution record on the issue that carries the consequence list, **not** an
  ask. Text verbatim at `drafts/c390-what-the-write-role-reached.md`.

### What deliberately was not done

**`good first issue` and `help wanted` stay at 0 of 50.** The capability to apply
them arrived this cycle; the judgement about *which* issues a newcomer could
actually finish is a pass over 50 issue bodies, and doing it badly is worse than
not doing it — a `good first issue` that turns out to need the whole architecture
in your head is how a first contributor leaves. That is the next pickup, named
here so it is not rediscovered as a capability probe.

**No nudge on retinue#63 or chamber#9.** Unchanged from c389, same reason.

### The transferable half

**A capability list is falsified in both directions.** Twelve days of records
carried "traffic is unreadable" as a property of the project, and it was a
property of a role that changed at 09:50Z; the record would have kept saying it
until someone re-ran the calls, because a 403 that becomes a 200 emits no signal.
The register already had the rule for *granted flags* (c388) and for *merged PRs*
(c270). This is the third instance and the general form is one line: **whenever a
permission, a merge or a dependency changes, re-run every claim that was justified
by its previous state — the ones that quietly became true are as costly as the
ones that quietly became false.**

