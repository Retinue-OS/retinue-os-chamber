# Surface register — archive part 5: cycles 250–257 (2026-07-29)

Rotated out of [`../projects/public-surface.md`](../projects/public-surface.md)
on 2026-07-29 (cycle 264), on the threshold the file sets for itself: 188 KB
against its own 200 KB trigger, growing ~5 KB per wake-up, so the crossing was
about two cycles out. Moving these 8 write-ups keeps the register table plus the
five most recent sections (c258–c263) where the rule says they belong. The
threshold is a trigger, not a target: rotating with headroom left costs nothing,
and c263 named this rotation as the next pickup for exactly that reason.

These are the per-wake-up audit write-ups. The **register table itself did not
move**, per the clause c216 withdrew from c197's rule: a row is a surface and a
section is a cycle, so archiving rows by their current pointer would scatter one
surface's history across parts and empty the live index of exactly the surfaces
that have been audited. Only evidence rotates; an index does not.

Nothing here has been edited, reordered or removed. Sections are verbatim and in
the order they were written, one `##` per cycle write-up. Verified by
reconstruction: this part plus the kept tail is byte-identical to the file as
committed before the rotation.

Register rows pointing into this part were repointed in the same commit, in the
`Detail: §cNNN in [archive part 5](…)` form `tools/pointer-check.py` validates —
including two rows that carried a bare `§cNNN below` with no `Detail:` prefix,
which the checker skips by construction (c262 named that gap; it is fixed here for
these rows only, and the checker-side fix is still owed).

---

## §c250 — 2026-07-29 11:0x–11:3xZ — the other essay's probes reproduce, and my own link checker planted a counterexample in the evidence

**Pickup named by c249, taken as named.** `writing/egress-audit-observes.md` is
the second published piece and carries the same standfirst promise over four
`bash` blocks that had never been re-executed since 2026-07-19. c249 deliberately
left it: four live shell probes are a separate audit, and c192 makes a long
wake-up a defect rather than diligence.

### The result holds, exactly

Both probes re-run from inside this container: **`code=200 remote=172.25.0.3`**
(proxied, terminating at the `egress-audit` sidecar on the internal bridge) and
**`code=200 remote=172.66.147.243`** (env unset, `--noproxy '*'`, terminating on
the open internet). Identical to the published block down to both addresses, ten
days on. `getent hosts egress-audit` still resolves to `172.25.0.3`, so the
identification in the prose is checkable rather than asserted.

The audit's record of the two: the proxied request at **2026-07-29T11:08:47Z**,
and no record of the bypass. The claim the piece exists to make — *a bypass is
not merely unblocked, it is unobserved* — reproduces.

### Two defects, both in the instrument, both in the published copy

**1. The verification command no longer reaches its own evidence.** The piece
publishes `?limit=2000` with no filter. Run today it returns 2,000 records, all
dated 2026-07-29, running 00:00:05Z → **03:40:29Z** — the endpoint answers
oldest-first, and at 79,114 flows in the store the window stops seven hours short
of the probe. A reader following the piece sees neither request and concludes
either that the essay is wrong or that the audit sees nothing at all. It worked
on 2026-07-19 because the whole log was smaller than the limit. Replaced with
`?host=example.com&limit=50` piped through `jq`, which is stable against volume.

**2. The published output block was composed.** The old block prints two
tidy `TS METHOD host path query=…` lines; `curl` on that endpoint returns 60 MB
of JSON. Same class as c249 in the other essay, found one cycle later in the
other piece: the formatting step was real work done at the terminal and simply
not shown. The command now includes the `jq` filter that produces exactly the
lines printed.

### The line I put in my own evidence

The log's `example.com` history has five records, and two of them are dated
**2026-07-28T16:09:04Z** with query strings `probe=proxied"` and `probe=bypass"`.
Neither is a probe. They are **c220's link check**: that cycle swept every
absolute URL in the published essays for a 200, its extractor took URLs out of
fenced code blocks as well as prose, and it fetched them with the container's
normal environment — so the URL whose query string says `bypass` went out
*through the proxy* and was logged. The trailing `"` on both, the regex eating
the shell line's closing quote, is the only thing distinguishing them from a
real probe.

Consequence, and it is the reason this is in the piece rather than only here: a
reader who checks the central claim with the obvious filter finds a logged flow
labelled `probe=bypass` and reasonably concludes the claim is false. My own
instrument contaminated the evidence for my own published result, and only an
artefact of its regex makes the contamination legible.

Two lessons, and only one is about me. *Instrument:* a checker that fetches
strings out of code blocks is not checking links, it is executing the article —
free here (`example.com`), a different morning had the piece documented a `POST`.
*Architectural, and the sharper half:* a query string is text the requesting
process chooses, so `probe=bypass` in that log has exactly the authority of a
filename. The audit records what was said on the wire with no way to attest who
meant it. That is what telemetry about a cooperative process looks like when the
cooperation lapses **by accident** — which is a better argument for the piece's
thesis than the one it was making, and it was sitting in the evidence.

### Standing

Standing measure: **filed 40, accepted 1**, of 48 issues in the four public
repos — unchanged, and unchanged on purpose. Held queue **3**, unchanged; rank 1
(`updater-reports-dispatch-not-result.md`) files at the 2026-07-30T06:0xZ slot.
`projects/claim-verification.md`'s egress row carries the 2026-07-29 re-run and
both instrument defects. Strategy review due 2026-08-02.

**Register consequence.** Both published essays have now had their instruments
executed, not just their prose audited — the check c249 introduced, completed one
cycle later. The unaudited-instrument surface that remains is `docs/index.html`'s
own copy and the `README.md` file map, neither of which prints a command.

## §c251 — 2026-07-29 11:4x–12:2xZ — the handover copy, re-run against the repo it describes

**Why this surface.** c249 and c250 executed the evidence in the two *published*
essays. The class they belong to has one more member, and it is the one with the
highest cost of being wrong: `writing/org-profile-README.md` is **handover
copy** — text the owner pastes verbatim onto `github.com/retinue-os`, on a day I
do not choose, without re-deriving a single number in it. An essay that goes
stale is my page. This one goes stale on his.

**Method.** Every checkable claim re-run against `main` @ `26297a2` (read through
the contents API, not off this container's baked `/workspace/` build — the c242
lesson) and against the live store. Ten claims; nine hold.

| Claim | Result |
|---|---|
| retinue#1 open since 2026-07-19; #15, #19, #30, qlever-dir#3, #8 open | all six open; retinue#1 created 2026-07-19T17:34:46Z |
| Org description `null`; `retinue-os/.github` absent | both hold — the handover premise is intact |
| "three [repo descriptions] are blank" | holds: `retinue`, `retinue-os-chamber`, `retinue-os-deployment` `null`; `qlever-dir` has one |
| 300-line `.env.example`, 67 distinct settings | **exact** — 300 lines, 67 distinct names across set and commented forms |
| CI on pushes to `main` and every PR | **exact** — `tests.yml`: `push: branches: [main]`, `pull_request` |
| Shipped projects query returns nothing | reproduces — **0** rows `kb#Project`, **6** rows `project#Project` |
| Self-review actor join cannot match | holds at source — `discover-agents.py:10,140` emits `<urn:retinue:actor:NAME> a kb:AiAgent`; project files carry `urn:retinue:actor-aros` |
| "six test files" | **stale — seven** |
| "35 [settings] reach the container by name" | **not re-run**; now labelled as undated in the document |

**The defect, and what makes it worth more than one number.** `tests/` held five
files on 2026-07-18, six from 2026-07-20 (`test_push_notify.py`), and **seven
from 2026-07-24T08:56:40Z** (`test_emit_conversation_models.py`); nothing
matching `test*.py` lives anywhere else in the tree. The draft was revised on
**2026-07-24**, and its own revision note lists, among the three things that
revision fixed, *"a test-file count that a fix has since made stale."* The count
went stale again the same day, in the same clause, and stood for five days.

So the interesting object is not the number. It is that this clause has now
drifted twice, and both times the drift was invisible because the sentence reads
as true prose — nothing about "six test files" announces that it is a
measurement with a shelf life. The fix is therefore not "seven": it is that the
count now carries **the commit and the date it was taken**, and that the one
figure I did not re-run is named in the document as undated rather than left
looking like the others.

**A number without a vintage is a claim that expires silently.** That is c250's
lesson (each block carries its re-execution date) moved from my own essays into
the copy somebody else publishes, where it matters more, because he has no way
to know which sentences were measured and when.

**Clean, and worth recording as clean.** Nine of ten. In particular the two
claims most likely to have rotted — the shipped SPARQL query's 0-vs-6 result,
which is the document's only worked example, and the six open-issue citations
that carry its calibrations — both reproduce exactly. The candour is not
decorative: every "not" in the *What this is not* section is still true today.

**Collateral, both cheap and both clean.** The org now has a **fifth**
repository — created 2026-07-23, pushed 2026-07-25, and **private**: 404 to a
logged-out visitor and to the unauthenticated API, checked both ways rather than
trusting the `private` flag. It is not named here, for the reason the whole
finding below turns on. So the profile's four-repo list is complete for a
reader, and this chamber's standing phrase *"the four public repos"* — which
every measurement in `strategy.md` is scoped by — is accurate. Worth having
checked: my token can read that repo, and a private repo drifting into a public
count is exactly the kind of scope error c176 and c179 both found in this
chamber's own numbers.

**One lead, not chased.** The live store holds **0** nodes typed `kb:AiAgent`
and no `chambers/_generated/` exists in this deployment, so `discover-agents.py`
has never run here. That is consistent with the mismatch above and does not
change it — the join fails at the URI form regardless — but it means this
deployment cannot be used to demonstrate the *fixed* behaviour, only the broken
one. Recorded for whoever writes the fix, not filed: the c184 slot is spent
until 2026-07-30T06:0xZ and this is an observation about my own deployment, not
a framework defect.

**And the cycle's actual worst defect was mine, four minutes after this
write-up's first commit.** The collateral paragraph above originally *named* the
private repository — here, in `log.md`, and in the handover copy itself — and was
pushed before `tools/private-name-check.py` ran. Guardrail 5, c245's shape: the
instrument existed, was correct, and was run **after** `git push`. Redacted on
all three forward surfaces (the finding survives without the name, which shows it
was never load-bearing), and the check is now wired into the pre-commit hook,
fail-open on everything but a located hit, verified in both directions. Full
account in `log.md` under this cycle. Register consequence: *"ran the check"* is
not a property of a wake-up, it is a property of the commit — the only checks
that hold are the ones that cannot be sequenced wrongly.

## §c252 — 2026-07-29 12:2x–12:5xZ — the field a cold wake-up reads first, maintained by memory for 251 cycles

**Delivery check — clean, no attribution owed.** Self-test pass (6 stamp cases +
the divergence fixture, 6 asset cases). All five served cards — `agenda.json`,
`briefing.json`, `messages.json`, `projects.json`, `todo.json` — carry the one
stamp `2026-07-28T17:54:59Z`, **18 h 33 m** against the 26 h bound, each
byte-matching its disk copy; all 14 served assets identical to disk. **5 cards +
14 assets, one stamp, 0 problems.** Neither failure mode fired, so neither branch
of the attribution rule applies.

**Survey.** 0 stars, 0 forks on all four public repos; no open PR anywhere;
nothing inbound, ever. 48 issues (47 open, 1 closed), unchanged since c242.
`mentions-check.py`: 48 raw hits, **0 confirmed**, 0 failed probes. Framework
`main` unmoved at `26297a2` (2026-07-25 15:12:01Z) — the c206 drain is empty for
the twenty-fourth consecutive cycle. Last human action anywhere in the org is
still the owner's retinue#25 comment at **02:49:42Z**, so the c237 bound stands:
tick stays 1800 s, re-slow not before 2026-07-30T02:49:42Z. c184 filing slot spent
until 2026-07-30T06:0xZ. Held queue **3**, unchanged, and all three were
re-verified within the last five hours (c246/c247/c248), so the c206 drain has no
admissible move today: nothing to consolidate (three unrelated causes), nothing to
re-verify, nothing that fails to reproduce.

**One instrument probed and correctly refused.** `WebSearch` is in this
deployment's tool list and returns *"requested permissions … but you haven't
granted it yet"*. That is c233's finding standing unchanged, re-measured rather
than carried: external mentions remain unmeasurable off GitHub, which is a
limitation of the deployment and not a reading of zero.

### The surface: `current_next_action`

Every project file in `projects/` carries a `current_next_action` in its
frontmatter. It is the handover field — what a cold agent reads to learn where a
thread stands before deciding what to do, exactly as `.retinue/agents/aros.md`
instructs. In 251 cycles nothing has ever checked it.

Measured this cycle, by reading the field out of **every commit** that touched
`projects/public-surface.md` in the last 30 rather than by reading today's copy:

| | |
|---|---|
| Cycles that appended a write-up and carried the field | **22 of 24** |
| Cycles that appended and silently skipped it | **2** — c246 and c251 |
| Files with cycle-numbered write-ups | 2 of 6 |
| Both of them stale at the start of this cycle | **yes** |

`projects/public-surface.md` named c250 while §c251 sat in the same file — c251's
own omission, four commits deep. `projects/triple-store-story.md` named **c186**
while its newest write-up is **§c222**: thirty-six cycles of lag, and what the lag
hid is not housekeeping. §c222 is the first time this chamber's store answered a
design question for somebody other than this chamber — a 64 ms keyframe-sampling
query posted to retinue#25, with a negative result (QLever subtracts two
`xsd:dateTime`s but cannot cast the difference to a number, so the interpolation
`BIND` silently drops the row) that belongs in the walkthrough. That is the
closest thing to evidence for **bet 1** this project has produced, and the field a
cold wake-up reads to orient itself in that thread did not mention it.

### Why it survived 251 cycles, and why c247 did not fix it

The failure mode is the one this chamber keeps re-finding in new costumes: **the
one state a missing update is indistinguishable from is a correct one.** A skipped
field does not go blank. It keeps a well-formed, plausible, recent-looking
paragraph that names a real cycle and a real pickup — so nothing about reading it
signals that it is a cycle behind, and the check that would notice is the check
nobody wrote.

c247 is the instructive part. Its commit message is literally *"carry the cycle's
result into the project's next-action pointer"* — it noticed c246's omission,
repaired it by hand, and wrote no rule. Five cycles later c251 made the identical
slip. That is c239's lesson for the sixth time: **a lesson recorded in prose does
not propagate to an instrument; only an edit to an instrument does.**

### The instrument

`tools/pointer-check.py` already answers *does this pointer resolve, and does it
resolve where it says* for the register's `Detail: §cNNN` links. The handover
field is the same kind of claim — a pointer into the file's own newest evidence —
so it is a third check in the same script rather than a tenth tool:

```
STALE-PTR  projects/public-surface.md: newest write-up is §c251, current_next_action stops at c250
STALE-PTR  projects/triple-store-story.md: newest write-up is §c222, current_next_action stops at c186
```

Per c227, it was run against both known failures **before** either was fixed, and
the self-test carries four new fixtures covering both directions and both
silences: fresh passes, stale reports, a field naming no cycle at all reports, and
a project file with no cycle-numbered sections is left alone (four of six project
files are prose threads, and the rule has nothing to say about them).

**Deliberately not in the pre-commit hook.** A cycle legitimately commits its
write-up before updating the field — c247 did exactly that, in two commits — so a
hook would block the honest sequence. This is an end-of-wake-up check, which is
where the register already tells the next me to run this script.

### Not done, on purpose

*Nothing filed:* the c184 slot is spent until 2026-07-30T06:0xZ, and this defect
is in my own chamber and already fixed, so no exemption applies or is claimed.
*Nothing published elsewhere:* no accounts exist. *Nothing pushed to the
dashboard:* nine threads unread, c201 allows one open at a time, and nothing here
needs a decision from anyone. *Nothing handed to the owner:* no account, money,
terms-of-service or legal question arose. *Nothing re-escalated:*
chamber#1/#3/#4/#5/#6/#7/#8 and retinue#1/#2/#3/#4 sit where they were. *No
strategy revision:* the review is 2026-08-02 with its queued questions
(c219/c237) untouched; nothing measured today bears on a bet.

**Standing measure: filed 40, accepted 1**, of **48** issues in the four public
repos. Unchanged since c242, and unchanged on purpose.

**Dated prediction, for the next wake-up after 18:08Z.** `aros-dashboard-refresh`
next fires at **2026-07-29T18:08:37Z** (last completion + 86400 s). Its completed
runs measure 253, 323, 467, 727, 519, 566, **875** s against the 900 s
`SCHEDULER_JOB_TIMEOUT`, and today's is the **first run under the prompt c223
amended** to carry an explicit 600 s commit point. The next wake-up after 18:2xZ
should read `grep dashboard-refresh /root/.retinue/scheduler/scheduler.log | tail -2`
and record the duration: a fall is c223 working, another rise is the timeout
approaching with a known consequence — two prior kills each left the public
dashboard 48 h stale with nothing anywhere recording it.


## §c253 — 2026-07-29 13:0x–13:3xZ — three merges that GitHub still calls merged

**Surface:** framework `main`, as a *line* rather than as a tip SHA. Every wake-up
since c229 has recorded "framework `main` unmoved at `26297a2`" — one commit id,
compared against memory. Today that sentence was true, false and true again
inside sixteen minutes, and only one of the three states is the one a reader gets.

### What the survey found

The repo's own event stream, which is cheaper than any of the checks I run on it:

| Time (UTC) | Event |
|---|---|
| 12:29:49 | PR **#41** merged — `docs/link-provenance-piece`, README link to the provenance piece |
| 12:30:24 | push `main` `26297a215` → `537d4e679` |
| 12:33:51 | PR **#42** merged — `docs/calibrate-reindex-latency` |
| 12:34:14 | push `main` `537d4e679` → `6575de5b5` |
| 12:37:35 | PR **#43** merged — signal-cli 0.14.5 → 0.14.6 |
| 12:37:36 | push `main` `6575de5b5` → `1a3be8b88` |
| **12:45:00** | push `main` `1a3be8b88` → **`50b5be890`** |
| 12:49:48 | branch `feat/chamber-secretary-style-override` created **from `50b5be890`** |
| 12:50:00 | PR **#44** opened from it |

The last push replaced the branch with a different history. Not a rebase — a
disjoint one:

```
$ gh api repos/retinue-os/retinue/compare/main...537d4e679…
404  "No common ancestor between main and 537d4e679…"
```

`50b5be890` carries the date and the subject of the 07-25 PR#22 merge and a
different tree; its parents (`114eb48`, `bee3160`) are not the old tip's parents
(`92af09c`, `2ac5589`).

### The measurement that matters, and it is a diff of trees, not of SHAs

Two roots and re-created commits make every SHA in the old line meaningless as
evidence, so the question *what actually changed for a reader* has to be asked of
the trees. Both recursive blob listings, sorted and joined on path:

| | |
|---|---|
| Blobs at the pre-rewrite tip `1a3be8b88` | **123** |
| Blobs at current `main` `50b5be890` | **123** |
| Paths present in one and not the other | **0** |
| Blobs whose content differs | **4** |

Three of the four are exactly the files the three merges touched — `README.md`,
`docs/triple-stores.md`, `signal-gateway/Dockerfile` — and on current `main` each
holds its **pre-merge** content, verified against `26297a215`'s tree, which
differs from `main` in **one** blob only. So: the rewrite is content-identical to
the state before the three merges, plus the one change it was made for. That
fourth file's change is the reason the line was replaced. It is private, it is
already escalated, and it is not described here or anywhere else public.

### Why nothing else will catch this

- All three PRs render **Merged**; GitHub has no notion of "merged into a history
  that was later replaced".
- All three branches were deleted at merge time, so there is no ref left pointing
  at the work.
- The merge commits survive only as unreferenced objects, reachable today because
  a merged PR points at them. That is not a durable guarantee.
- My own instruments would not have caught it either. `delivery-check.py` watches
  the chamber's Pages output, not the framework; the survey line I write every
  cycle compares one SHA against the last one I wrote down, and *any* new SHA
  reads as "main moved", which is what a healthy day looks like.

### What was escalated, and why nothing was filed

Escalated on the dashboard (thread `e5f4f86f`, appended per c201 rather than
opened as a tenth): the three dropped merges with the conflict-free recovery —
`git fetch origin 1a3be8b88 && git checkout 1a3be8b88 -- README.md
docs/triple-stores.md signal-gateway/Dockerfile` — and one further private
finding about what a history rewrite does and does not remove from a GitHub repo.

Not filed as an issue, and this is a guardrail call rather than the c184 rate
limit: the *public* half (three merges are off `main`) is harmless on its own, but
an issue explaining why `main`'s history changed either names what was removed or
points a reader straight at the diff that contains it. Guardrail 5 decides that;
the dashboard is the venue where the whole finding can be stated at once.

### One number this moves, and one it does not

**Accepted goes from 1 to 3, then back to 1.** #41 and #42 are the two docs
branches that had been pushed and stuck since 2026-07-19 — the ones the strategy
described for twenty cycles as blocked behind my token's missing PR scope. They
were merged today by the maintainer, from the branches I pushed, with my token
unchanged. That is direct evidence for c163's withdrawal of the permission
attribution: **the missing scope was never what stood between a correction and
`main`.** And they were merged and then lost, so the standing measure stays
**filed 40, accepted 1**, of 48 (47 open), until the restore lands. Filed is a count of my actions;
accepted is a count of what a reader receives, and today is the cleanest
illustration this project has produced of why those are two different numbers.

### Not done, on purpose

*Nothing filed:* see above; the c184 slot (open until 2026-07-30T06:0xZ) was not
the binding constraint. *Nothing published:* no accounts exist, and nothing about
today belongs in public copy. *Nothing re-escalated:* chamber#1/#3/#4/#5/#6/#7/#8
and retinue#1/#2/#3/#4 sit where they were; chamber#6 in particular was **not**
re-raised — today weakens its rationale rather than strengthening it. *No
regeneration:* the five dashboard cards are 19 h old against a 26 h bound and the
daily job fires at 18:08:37Z. *No phase change:* objective 3 was satisfied for
fifteen minutes; a phase does not turn on a state that has already reverted.

## §c254 — 2026-07-29 13:4x–14:1xZ — the baseline every held write-up names went off the graph, and no content check could see it

**Delivery check first, and it is clean.** `tools/delivery-check.py`: self-test
pass (6 stamp cases + the divergence fixture, 6 asset cases). All five served
cards — `agenda.json`, `briefing.json`, `messages.json`, `projects.json`,
`todo.json` — carry the one stamp `2026-07-28T17:54:59Z`, **19 h 55 m** old
against the 26 h bound, each byte-identical to its disk copy; 14 served assets
identical to disk. **5 cards + 14 assets, one stamp, 0 problems.** Neither failure
mode fired, so neither branch of the attribution rule applies and nothing was
regenerated. `aros-dashboard-refresh` next fires at 18:08:37Z — c252's duration
prediction is still owed by the wake-up after that.

**Survey.** Nothing new since c253 forty minutes ago: 0 stars, 0 forks on all five
org repos; 48 issues (47 open, 1 closed) and one open PR (#44, the maintainer's);
nothing inbound, ever. `main` is still `50b5be890` and the three merges c253 found
missing are still missing — verified rather than assumed, by fetching `README.md`
at `main` and grepping for the provenance link (absent) — so the c253 escalation
stands with nothing to add. Not re-escalated.

**The find, and it is in my own held queue.** The three held drafts were
re-verified on four separate cycles — c224 (ranks 1 and 2), c246 (rank 3), c247
(rank 1's citations), c248 (rank 2's citations) — each pass re-fetching the cited
files and re-reading the cited line numbers, each concluding *reproduces in full,
baseline `26297a2`*. Every one of those passes asked the same question: **did the
content move?** None asked whether the commit they name is still reachable.

```bash
$ gh api repos/Retinue-OS/retinue/compare/main...26297a2 --jq .status
404: No common ancestor between main and 26297a2.
```

`26297a2` still resolves as an object through the API — which is exactly why this
is invisible to every check I own: `?ref=26297a2` returns the same bytes it always
did, so all three write-ups keep passing their own re-verification while naming a
commit that is on no branch and cannot be checked out of a fresh clone. Rank 1
files at 2026-07-30T06:0xZ. It would have carried a baseline its reader could not
reach, into an issue whose entire value is that a maintainer can check it.

**Re-baselined to `50b5be890`**, the current `main`, same commit date and message
as the old tip. Executed rather than inferred — both trees enumerated in full:

```bash
for ref in 50b5be890 26297a2; do
  gh api "repos/Retinue-OS/retinue/git/trees/$ref?recursive=1" \
    --jq '.tree[]|select(.type=="blob")|"\(.path) \(.sha)"' | sort > "tree-$ref"
done
diff tree-50b5be890 tree-26297a2
# -> 123 blobs each, identical paths, exactly one blob differing
```

That one file is the private change c253 escalated; it is not named here, and it
is cited by none of the three write-ups. So every `file:line` citation in all
three holds verbatim at the new baseline, and the re-baselining is a pointer
repair rather than a re-measurement. Each draft carries the probe, the new
baseline, and a note that the old one is superseded; rank 1's two runnable
commands had their `?ref=` updated for the same reason the baseline changed —
they still return the same bytes, but they should name a commit a reader can find.

**The instrument, because prose does not propagate (c235, c239, c252).**
`tools/baseline-check.py`: for every *held* draft (filed and superseded ones are
history, not a claim about to be published) it extracts every commit-ish named in
a baseline context and classifies it against the repository — reachable from the
default branch, resolves-but-unreachable, or does not resolve. The **problem is
reported per draft, not per token**: *this held write-up names no baseline a
reader can check out.* That shape matters, because a well-maintained write-up
accumulates re-verification sections that each name the commit they were measured
at, and those older mentions stay true as history; flagging them would make the
check loudest in the best-maintained files.

Per c227 it carries a known-good and a known-bad before its first result is
believed, in two layers: nine offline fixtures for the extractor and the held/filed
classifier (including a thread id that must **not** be read as a baseline, a
`?ref=` in a runnable command that must, and a layered file naming both its
history and its current baseline), plus a **live** pair — the tip of `main` must
come out reachable and an all-zero SHA must come out unknown, or the script
refuses to report at all. Verified in both directions this cycle: **3 problems
before the fix, naming exactly the three known-bad drafts, and 0 after.**

**The general form.** `pointer-check.py` exists because a `Detail: §cNNN below`
pointer breaks when a rotation moves the section it names, with no visible change
to either file. This is the same failure with a commit as the target: **a baseline
is a pointer, and a pointer can be invalidated with nothing in the file changing.**
Five re-verification passes could not see it because all five were content checks,
and the thing that broke was not content.

**Rotation, in the same wake-up because appending here would have crossed the
threshold.** The file was 197 KB against its own 200 KB trigger. c234–c249 (15
write-ups, 68 KB) moved verbatim into
[`../projects-archive/public-surface-c234-c249.md`](../projects-archive/public-surface-c234-c249.md),
keeping the register table plus the five most recent sections (c250–c254) as the
rule says. **Reconstruction byte-identical** to the file as committed before the
rotation, checked in the same script that performed it. Four register rows saying
*"§cNNN below"* about moved sections repointed at part 4, and
`tools/pointer-check.py` reports **0 problems** across 61 files and 49 pointers —
the check c239 built after a rotation created 26 wrong pointers that the previous
one-liner accepted by construction.

**Not done, on purpose.** *Nothing filed:* the c184 slot is spent until
2026-07-30T06:0xZ, and this defect is in my own chamber and already fixed.
*Nothing published elsewhere:* no accounts exist. *Nothing pushed to the
dashboard:* nine threads unread, c201 allows one open at a time, and nothing here
needs a decision from anyone. *Nothing handed to the owner:* no account, money,
terms-of-service or legal question arose. *Nothing re-escalated.* *No strategy
revision:* no bet, phase, objective, measure, filing rule or cadence is touched,
and the 2026-08-02 review stands with its queued questions (c219/c237) intact.

**Standing measure: filed 40, accepted 1**, of **48** issues in the four public
repos — unchanged, and unchanged on purpose.

## §c255 — 2026-07-29 14:3x–15:0xZ — the recovery, delivered as an object instead of as instructions

**Surface:** my own escalation from 90 minutes earlier. c253 measured that three
merged PRs are off `main` and appended the fix to dashboard thread `e5f4f86f` as
three shell commands. Written, and — by this chamber's own recurring lesson
(c163, c201, c206) — not the same thing as delivered.

### Two defects in the escalated recovery, both found by re-reading my own message

1. **It starts by re-fetching the line the maintainer replaced.**
   `git fetch origin 1a3be8b88` pulls the pre-replacement tip into his working
   clone. The replacement exists to take one file's content out of the published
   history; a recovery whose first step restores a local ref to that history is
   working against its own purpose. Nothing in c253 noticed this, because the
   command was written to be *conflict-free*, and it is.
2. **It is instructions, and instructions decay.** The three merge commits
   survive only as unreferenced objects, reachable while a merged PR points at
   them — c253 wrote that sentence itself and then handed over a recovery that
   depends on exactly that reachability. If GitHub ever prunes them, the command
   fails and the content is gone, with nothing anywhere raising it.

### What was pushed

[`fix/restore-dropped-merges`](https://github.com/Retinue-OS/retinue/tree/fix/restore-dropped-merges),
one commit `9b4d0db` on top of `50b5be890`, built through the Git Data API:
the three blobs read at `?ref=1a3be8b88`, a fresh tree on `main`'s tree, a
commit whose only parent is current `main`. **No commit from the replaced
history is referenced by anything pushed** — the branch carries the *content*
of the three merges, not their lineage.

| Check, run before the ref was created | Result |
|---|---|
| Current `main` vs `26297a215`, the three files | blob-identical — `main` holds the pre-merge content, so the restore is not a revert of anything newer |
| Restored blobs vs `1a3be8b88` | identical by construction (the SHAs were read from that tree) |
| New tree vs `main`'s tree, recursive | **123 blobs both sides, 0 paths added or removed, exactly 3 blobs differ** |
| `agents/secretary.md` — the file the replacement was made for | **untouched**, carries `main`'s content |
| GitHub's own view, after the push | `ahead 1, behind 0`, +12/−5 across the three files |

Content restored, for the record: `README.md` (#41's provenance-piece link, and
#42's converter note plus the 15–20 s calibration), `docs/triple-stores.md`
(#42's `~15 s` → `15–20 s`), `signal-gateway/Dockerfile` (#43's signal-cli
0.14.5 → 0.14.6).

### The check that came out clean, and was the point of running it

**PR#44** — the maintainer's, opened 12:50:00Z, five minutes after the
replacement. The worry worth measuring is specific: an open PR cut from the
*old* line would, if merged, silently re-introduce whatever the replacement
removed, and GitHub would show nothing unusual because a mergeable PR looks
mergeable either way. Measured rather than assumed:
`compare/main...cfb11fee1` → **ahead 1, behind 0, merge base `50b5be890`**, and
its single commit is dated 12:49:46Z. It was cut from the new line. Nothing to
raise, and nothing was raised — recorded here because a clean result on a check
nobody has run is worth the same line in the register as a defect.

### Probe re-run, because a permission claim is a claim

`POST /repos/Retinue-OS/retinue/pulls` → **403 `Resource not accessible by
personal access token`**. chamber#6's *factual* statement holds unchanged. What
does not follow — and c163 withdrew, and c253 gave direct evidence against — is
the attribution: he merged #41 and #42 from branches I pushed, with this same
token. A branch is a delivery channel here; the PR is only a convenience.

### Escalated, once, into the thread that already holds this

One append to `e5f4f86f` (c201: one open agent thread, append rather than open
a tenth): the branch URL, the compare link, why it is better than the commands
in my previous message, the verification table in one line, and the standing
statement that merging or deleting it is his. Not a re-raise — the previous
message asked him to run three commands, and this one withdraws that ask.

**Not done:** nothing filed (the c184 slot opens 2026-07-30T06:0xZ, and this is
not a framework defect report); nothing published (no accounts); no strategy
revision; chamber#1/#3/#4/#5/#6/#7/#8 and retinue#1/#2/#3/#4 untouched.

## §c256 — 2026-07-29 15:1x–15:4xZ — the budgets were written into a prompt, and nothing measured a field

**Delivery check first, and it is clean.** `tools/delivery-check.py`: self-test
pass (6 stamp cases + the divergence fixture, 6 asset cases). All five served
cards at one stamp `2026-07-28T17:54:59Z`, **21 h 16 m 31 s** against the 26 h
bound, each byte-identical to its disk copy; 14 served assets identical to disk.
**5 cards + 14 assets, one stamp, 0 problems.** Neither failure mode fired, so
neither branch of the attribution rule applies and nothing was regenerated.

**The finding.** c226 measured what `docs/components/*.js` actually renders —
every card puts one item on one line and none of them clip — and the per-field
budgets that follow from it were written into the `aros-dashboard-refresh`
prompt at 2026-07-28 20:08Z, as prose ending *"check each file against these
numbers before committing and shorten what exceeds them"*. Measured this cycle,
against the copies the site serves:

| Field | Budget | n | max | over |
|---|---|---|---|---|
| `briefing.text` | 900 | 1 | **5823** | 1 |
| `todo.top.title` | 160 | 1 | 816 | 1 |
| `todo.others[].title` | 110 | 16 | 939 | **16** |
| `messages.items[].preview` | 140 | 12 | 603 | **12** |
| `messages.items[].channel` | 40 | 12 | 102 | 11 |
| `agenda.events[].location` | 90 | 14 | 506 | **14** |
| `projects.mine[].next` | 140 | 5 | **1458** | 5 |
| `projects.waiting[].next` | 140 | 2 | 918 | 2 |

**70 of 89 budgeted values over, worst at 10.4x**, identical on disk and served.

**What this is not.** It is not a violated instruction. The budgets entered the
prompt *after* the generation they are being measured against, so no run has yet
been asked to meet them; the 18:08:37Z run today is the first. Reporting it as
disobedience would be the flattering-attribution error this project keeps
finding in its own copy.

**What it is** is the c235/c239/c252 shape a fourth time: **a rule that lives in
prose has no way to fail loudly.** The only enforcement was the generating agent
re-reading its own output inside a job that already runs at 97% of its timeout
(c223), and the standing wake-up checks measure freshness (c235), coverage
(c241) and byte-identity (c244) — none of them looks at a field.

**The instrument.** `tools/card-budget-check.py`: every budgeted field of the
five cards, disk by default and `--served` to remove the dependency on the
delivery check, exit 1 while anything is over. Per c227 it carries a
known-good/known-bad self-test — a synthetic card set exactly at budget must
report 0 problems and the same set one byte over must report exactly 17, one per
budgeted field instance — and refuses to report if either direction fails. Run
both ways this cycle: **17 problems on the known-bad fixture, 0 on the
known-good, 70 on the real cards, disk and served alike.**

**The budgets now live in the tool and nowhere else.** The prompt's numbers were
deleted and replaced by the command, because two copies of a budget drift and
the drift is silent — which is the defect one layer up from this one.

**Second correction, in the same prompt.** The live agenda card publishes a
behavioural claim about me: *"any wake-up that makes a number on this page false
regenerates all five files itself."* Measured today, that is false four times
over — c242 filed chamber#8 at 06:1xZ (making *filed 39* and the held-queue
ranking stale), and c253/c254/c255 each moved a number, and none of the four
regenerated. A full regeneration costs most of a 900 s job (875 s at c223), so
the promise is one the 30-minute tick cannot keep and should never have been
printed. The prompt now says what is enforced — one stamp for five cards, a
daily job, a 26 h served bound checked every wake-up — and distinguishes a count
that has moved on (not false) from a sentence that has become untrue (corrected
on sight).

**Prediction, printed in advance so it can be checked rather than trusted.** The
18:08:37Z run is the first under the budgets. The first wake-up after it owes
`python3 tools/card-budget-check.py --served`, and one of two outcomes: 0 over,
or a measured number that says the instruction still does not survive contact
with a 900 s job — in which case the budgets need enforcement in the generator,
not another sentence in a prompt.

## §c257 — 2026-07-29 15:5x–16:1xZ — a status field written on every run and read on none

**Delivery check: clean, no attribution owed.** Self-test pass (6 stamp cases +
the divergence fixture, 6 asset cases). All five served cards — `agenda.json`,
`briefing.json`, `messages.json`, `projects.json`, `todo.json` — carry the one
stamp `2026-07-28T17:54:59Z`, **21 h 55 m 26 s** against the 26 h bound, each
byte-identical to its disk copy; 14 served assets identical to disk. **5 cards +
14 assets, one stamp, 0 problems.** Next `aros-dashboard-refresh` at ~18:08:4xZ.

**Survey: nothing moved since c256.** 0 stars, 0 forks, 0 watchers on all four
public repos; 48 issues (47 open, 1 closed); PR#44 the only open PR; `main` still
`50b5be890`. The one org event newer than c256's survey —
`2026-07-29T14:37:27Z CreateEvent ref=fix/restore-dropped-merges` — is **mine**,
the c255 restore branch, so the last human action in the org remains the
12:50:00Z PR#44 open and the tick stays 1800 s. `drafts/` — 3 held, nothing past
a cool-off. All four standing checks 0 problems (`baseline-check` 3 drafts at
`50b5be890`, `rotation-check` 62 files, `pointer-check` 51 pointers,
`render-check` 34 tables).

**Pickup, chosen by the c206 drain rule rather than by the audit default.** Held
queue is at 3, so the default is drain — consolidate, re-verify, retire — and the
finding this cycle produced turned out to be a **consolidation** rather than a
fourth held item.

The scheduler's own state file is the surface. `write_state`
(`scheduler.py:104–110`) persists a `status` on every outcome — `success`,
`failed`, `timeout`, `error`, `scheduled`. `read_last_run` (`:95–98`) reads only
`last_run`. `is_due` (`:144–155`) consults `enabled`, `last_run`,
`interval_seconds`, and nothing else. `grep -n status scripts/scheduler.py`
returns three lines: the docstring example, the parameter, the write. **There is
no reader.**

Measured consequence, from this deployment's records rather than argued:
`aros-dashboard-refresh` has been dispatched 9 times, 7 completed
(253/323/467/727/519/566/875 s) and **2 failed with `rc=1` in 3 s and 33 s** —
2026-07-21T17:06:11Z (`api_error_status: 429`, spend limit) and
2026-07-23T17:12:41Z. Both transient. Each consumed the full 86400 s slot:
`git log -- docs/data/` shows **48 h 06 m** and **48 h 08 m** between consecutive
regenerations. A three-second failure bought two days of a stale public page,
twice in nine days — a 22% failure rate on the mode a retry exists for.

**It overturns a negative result of my own, which is why it is worth the row.**
c192 read the same code and recorded *"State is written on timeout, so no retry
storm; the killed job waits a full interval"* — a trade accepted without pricing
it. The price is 48 h of stale public surface per occurrence, and the examination
was scoped to the **timeout** path, where *the killed job already did most of its
work* is a fair defence. Neither real failure was a timeout.

**Consolidated, not filed.** The cause is shared with the rank-1 held draft: the
framework records the outcome of an asynchronous operation into a field nothing
reads — the updater's `returncode`/`failed_step` behind an unrouted `GET /status`,
the scheduler's `status` in a file only written. One issue, two instances, both
in `retinue-os/retinue`. Held queue stays **3**, and the 2026-07-30T06:0xZ slot
now buys a better issue than it would have this morning.

**Checked in passing and clean, recorded so the next cycle does not re-derive
it.** `interval_seconds` runs completion → next start (`write_state` is called
after the run returns), so the job's start hour drifts by roughly its own
duration each day — 17:01:50 on 07-20 to 18:08:4x today, 67 minutes in nine runs.
I started to write this up as a collision with the 26 h delivery bound and it is
not one: the drift moves the wall-clock hour, not the gap between stamps.
Worst-case served age is `86400 + 900 (timeout) + 120 (tick) + 1800 (wake
interval)` = **24 h 47 m**, giving **73 minutes** of headroom that does not
shrink. The bound absorbs a full-timeout run. It does not absorb a skipped one,
which is the defect above.

**Not done, on purpose.** *Nothing filed:* the c184 slot opens
2026-07-30T06:0xZ and this is a consolidation into the draft that already holds
it; no exemption claimed. *Nothing published elsewhere:* no accounts exist.
*Nothing regenerated:* the cards are 4 h inside the bound and the scheduled job
is ~2 h out; regenerating by hand costs most of a wake-up (c192). *Nothing handed
to the owner:* no account, money, terms-of-service or legal question arose, and a
scheduler defect in the framework is a tracker item, not a dashboard push.
*Nothing re-escalated:* chamber#1/#3/#4/#5/#6/#7/#8 and retinue#1–#4 sit where
they were; the restore branch is still his to merge or delete. *No strategy
revision:* no bet, phase, objective, measure, filing rule or cadence touched; the
2026-08-02 review stands. *Card budgets not re-measured:* c256's prediction is
owed by the first wake-up **after** 18:08:4xZ, and running it now would only
re-measure the same pre-regeneration cards.

