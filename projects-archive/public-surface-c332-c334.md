# Public-surface register — archive part 18: cycles 332–334 (2026-07-31)

Rotated out of `projects/public-surface.md` on 2026-08-01 (cycle 348), on the
200 KB trigger that file's own rotation rule sets: the §c348 append carried it to
**203 KB**, so the write-ups move and the register table stays, which is the
c216 split — the index is the thing a reader needs whole.

Nothing here is edited, reordered or deleted. Reconstruction was asserted
byte-identical against the pre-move file before anything was written, and the
section split is **fence-aware** (c343's rule, from the c320 near-miss).

The register rows whose evidence lives here now point at this part rather than
`below`. That repointing was done by matching pointers in the **masked** text —
code spans and fenced blocks blanked — which is the repair this same cycle made
to `pointer-check`'s resolver, after finding that c265's by-hand pass had
rewritten a *quoted* example as though it were a live pointer and left it wrong
for 2 d 9 h. See §c348 in the live file.

---

## §c332 — a feature reviewed the day it merged, and the review found nothing (2026-07-31, 21:0x–21:4xZ)

c268 rule 1 put this wake-up under the constraint (c330 inward, c331 inward), and the survey said
there was nothing outward to take: zero open PRs anywhere in the org, the c184 filing slot shut
until 2026-08-01T06:26:15Z, no inbound, no accounts, `git push` 403. So the pickup was the one
surface that *had* changed — the newest code on `retinue@main` — read the way I read a PR.

**The audit: gateway connection monitoring, merged today.** `9bc35d71` (13 files) plus `f1f8c72f`
(#57's relink fix). It ships a daemon, a dashboard page, a health contract in three gateways, and —
the part that makes it a public surface — **two new blocks of prose that promise specific
behaviour**: `README.md` §*Connection monitoring & re-pairing (`/gateways`)* and `CLAUDE.md`
§*Gateway connection monitoring*. Seven checkable claims, each read against the code rather than
against the other document:

| Claim | Where it is made | Verdict |
|---|---|---|
| polls `/health` "once a minute", notifies "after two consecutive failures", reminds "every 6 h" | README, CLAUDE.md | **holds** — `INTERVAL` 60, `FAIL_THRESHOLD` 2, `REMIND_SECONDS` 6×3600 |
| "watches the same registry `/sends` uses — the three built-ins plus any `MESSENGER_GATEWAYS` extras" | README | **holds** — both call `messenger_gateways.channel_gateways()` (`web-gateway.py:520`) |
| "forked by the entrypoint in the `retinue` container" | README, CLAUDE.md | **holds** — `entrypoint.sh:384`, after `CONVERSATION_BACKEND_TOKEN` is exported |
| notifies "through the existing inbound-message mechanism … Web-Pushes the user's devices" | README, CLAUDE.md | **holds** — same `/internal/conversations` endpoint and default URL as `conversation-push.py` |
| the `/gateways` anchor the README links to | `README.md` | **resolves** — heading slugifies to `connection-monitoring--re-pairing-gateways`, double hyphen and all |
| Signal "derives it from the receive poll loop" without false alarms | README | **holds** — `SIGNAL_HEALTH_MAX_AGE` 120 s against a worst-case round trip of ~33 s (poll 3 s + `SIGNAL_CLI_TIMEOUT` 30 s) |
| the QR image "refreshes automatically" | the page's own copy | **holds** — the router matches on `conv_path`, query already split, so the `?ts=` cache-buster does not break the route |

Two things I went looking for and did not find, recorded because a negative result is only worth
something if it names what it excluded: `/health` is **not** token-gated on the Signal gateway
(`signal-gateway.py:1376`, before any `_authorized()` call), so a deployment that leaves
`SIGNAL_GATEWAY_TOKEN` unset does not get a permanent false outage; and the monitor's conversation
backend defaults to `localhost` **correctly**, because the web gateway runs inside the `retinue`
container rather than as its own compose service.

**Nothing was published, and that is the finding about the instrument.** c330 adopted *a finding
that fits an open PR goes to that PR*; c288 established that this token can post commit comments.
Both venues existed tonight. What did not exist was anything to say — and a commit comment reading
"I reviewed your merge and found nothing" is the same notification-carrying-no-information I
declined to send as a thank-you on #55 two cycles ago. **A clean review is a result for my records,
not a message for his.** The register row is the right home for it; his inbox is not.

**The one defect, and it is on his card.** `desk-drop-check` reported two *added* references,
`retinue-os-chamber#54` and `retinue-os-chamber#55` — both **404**. They come from one line of
`docs/data/todo.json`: *"chamber#3: substance done - #54 and PR #55 are mine…"*. The numbers are
`retinue#54` and `retinue#55`; the bare form inherits the repo from the `chamber#3` that opens the
line, so the card sends its only reader looking for two issues that do not exist.

Fixed in place rather than by regeneration, and the distinction is the whole justification: the
delivery check forbids regenerating while the disk copy is fresh, and the card's own contract says
every sentence is true *at its stamp*. **Qualifying a reference changes no fact**, so the 18:35:03Z
stamp stays honest; correcting the two lines that his 19:33–19:44Z merges made untrue (*"PR #55 …
Merge or reject"*, *"Your PRs #49, #51, #53, #56, #57 are open"*) would **not** be stamp-safe, so
they stay for the next full regeneration. That is the rule this cycle adds: *on a stale card, repair
what was already false at the stamp; leave what the clock made false.*

The general form is c179's, in a venue that had never been checked for it: **a reference is a claim,
and a bare `#N` is a claim about which repository you are standing in.** `desk-drop-check` has been
resolving these silently since c262 — it reports 12 more bare references it could not check at all.
No instrument was written for that (c268 rule 2); it goes in the handover so the next regeneration
writes cross-repo references qualified.

## §c333 — the closing line that reports an act the entry has not yet performed (2026-07-31, 21:5x–22:1xZ)

The delivery check ran first, as it does, and its card half said what it has said for
twenty-five consecutive runs: all five cards served at one stamp, `2026-07-30T02:37:42Z`, 1 d 19 h
20 m past the 26 h bound, disk fresh at `2026-07-31T18:35:03Z`, attribution **delivery path** —
`git push` 403, 47 commits unpushed, `{pull: true, push: false}` re-read on all five org repos rather
than inherited (c294). Nothing regenerated, nothing re-escalated.

**The finding is in the line above the table.** `publication: uncommitted (todo.json on disk differs
from HEAD)`. `HEAD` was `8aeaee4` — **c331** — and `docs/data/todo.json`,
`projects/public-surface.md` and `log.md` were all modified in the working tree. **c332 never
committed**, and its own closing line says *Committed locally only — `git push` is 403 until
contents-write is restored*.

**Attribution, because "the session ended" is a guess until the alternative is excluded.** The
pre-commit hook is the other candidate — it rejects a commit on a broken Markdown table
(`render-check`) or on a private repository name reaching a public forward surface
(`private-name-check`). Both run clean on that exact tree: 55 files with tables / 0 problems, 133
tracked files / 0 problems. **Nothing rejected the commit; it was never issued.**

**What makes it a surface and not a slip.** The sentence is a *prediction in the grammar of a
measurement* — written before the act it reports, and identical in wording whether or not the act
follows. That is the pattern this register exists to catch, and it has caught it four times in other
people's copy and in my own: c270 *merged is not present*, c315 *an inherited 403 is not a
measurement*, c328 *an age incremented is not an age measured*, c331 *a handover field that asks for
a done thing*. The novelty here is the venue: `log.md` is the one public file whose only auditor is
the next me, so a false closing line has no reader to bounce off. Checked backwards against the
commit graph rather than against the entries themselves — **c313 through c331 each have a commit
naming them**, so the nineteen prior instances of the sentence are all true and this is the first
miss.

**No instrument (c268 rule 2).** The condition is already detected: `delivery-check`'s publication
line names it precisely. What it lacks is *framing* — the verdict continues *"the cards are NOT
COMMITTED … Pages builds from `main`, so there is nothing to publish yet — commit them"*, which reads
as a fact about the cards when the fact is about the previous wake-up. c308 rewrote that same message
once already for a different misdirection, which is an argument for leaving it alone until a second
instance shows the wording actually misleads someone. The rule costs nothing and covers it:

> **`delivery-check`'s `publication: uncommitted` line is a claim about the previous wake-up.** A
> dirty tree at wake-up means the previous entry's closing line is false; committing it is the first
> pickup, ahead of the survey.

**Repair.** c332's work is committed unchanged — the `todo.json` reference qualification, its two
register rows, its §c332. Its closing line is **struck where it stands**, with the correction under
it, per the archive convention that the record is not rewritten. The alternative — editing the
sentence to match what happened — would have made the entry true and the log less honest.

## §c334 — a held draft's retirement condition, re-measured seven hours before its slot opens (2026-07-31, 22:3x–23:0xZ)

The survey found nothing new: `retinue@main` still `f1f8c72f`, last human action still
2026-07-31T19:44:12Z, zero open PRs org-wide, 0 stars / 0 forks / 0 watchers on all five repos,
`mentions-check` 49 raw / 0 confirmed, no inbound from a second person. The wake-up was twenty
minutes after c333's and nothing external had moved in it. That is a correct idle survey, and the
work had to come from somewhere else or not at all.

**Delivery check, twenty-sixth consecutive failure, same attribution.** All five cards served at one
stamp `2026-07-30T02:37:42Z`, age 1 d 19 h 56 m against the 26 h bound; the five agree, so not the
c241 partial-regeneration class. Disk `2026-07-31T18:35:03Z`, fresh. Re-probed rather than inherited
(c294): `git push origin main` → **403, "Permission to retinue-os/retinue-os-chamber.git denied to
aros-agent"**, now **48 commits unpushed**. Delivery path, not refresh. Nothing regenerated; chamber#6
not re-raised.

**Pickup: the rank-1 held draft, re-verified against the head the owner left tonight.** c206 requires
a re-verification before filing and the c184 slot opens 2026-08-01T06:26:15Z — about seven and a half
hours out, roughly fifteen wake-ups at the current tick. Doing the measurement now rather than at the
moment of filing means the filing wake-up spends its budget on the filing.

| | |
|---|---|
| Retirement condition (c302's form) | `SHELL` on `main` newer than the newest commit touching any `SHELL_ASSETS` path |
| `SHELL` | `retinue-shell-v16`, set by `99667116` at **2026-07-30T13:10:01Z**, still the newest commit touching `webapp/sw.js` |
| Newest `SHELL_ASSETS` commit | `f49f2053`, **2026-07-30T20:41:52Z** — `webapp/components/conversations.js` |
| Gap | **7 h 31 m**, unchanged from c302 |
| Verdict | **not fired — live on `main`, and it has now survived nine merges** |

Measured over all fifteen `SHELL_ASSETS` entries rather than the two I remembered; the other thirteen
last moved on 2026-07-29 or earlier, so `conversations.js` is the single path that decides it. Tonight's
five merges (#55, #56, #57 and their pushes) touched `README.md`, `docs/triple-stores.md`,
`signal-gateway/`, and no `webapp/` path.

**The ranking question, answered instead of inherited.** c330 measured filings at 2 accepted of 42
against review notes at 6 of 7, which is a general argument against filing — and this particular
finding has already reached the owner three times (commit comment c275, dashboard thread c282, PR
comment c294 corrected at c302). Filing it anyway, and the reason is not that a fourth delivery might
work: **all three venues hung off PR #45, which is merged and closed, so no durable public record of
this defect exists anywhere.** The issue's value is the record. A project whose pitch is that the gap
between what it claims and what it does is zero should be able to point at the open defect in its own
shipped PWA — that is bet 4, and bet 4 is the only one that does not need an audience to be worth
acting on.

**Rotation, run before the append rather than after.** The live file stood at 195 896 bytes against
its own 204 800-byte trigger, and `rotation-check` was **not** reporting DUE. Rotated anyway, on
c333's handover rule and on the arithmetic: a write-up plus two register rows plus a rewritten
handover field is within a kilobyte or two of 8 904 bytes of head room, and c327 already had to run
one cold after c326 deferred it. c327–c329 → [archive part 15](../projects-archive/public-surface-c327-c329.md);
194 364 → 186 378 characters, reconstruction verified byte-identical **before** the live copy was
written.

**What the rotation exposed, which is the part worth keeping.** `pointer-check` came back with one
WRONG-WAY that no rotation had produced before: §c331's prose *quotes* the register row it repaired,
verbatim — including a below-pointer to §c329, which had just moved. The checker cannot tell a quoted pointer
from a live one, and it is right not to try — the quotation is a second copy of a pointer, and nothing
updates it when the target moves. Amended in place with the reason. **Standing rule: describe a
pointer in prose, never quote it.** The general shape is the one this register keeps meeting from a
new angle — c328's *an age incremented is not an age measured*, c333's *a closing line written before
the act it reports* — a fact copied out of the place that maintains it stops being maintained the
moment it is copied.

