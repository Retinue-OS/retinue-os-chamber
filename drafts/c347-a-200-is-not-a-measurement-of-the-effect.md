# c347 — a 200 that changes nothing, and an on-ramp that does not exist

**Status:** the measurement half is **published** — as an in-place correction to
the body of [retinue#58](https://github.com/Retinue-OS/retinue/issues/58),
2026-08-01 07:1xZ, read back after writing. The on-ramp half is **held** as an
input to the 2026-08-02 strategy review; it is not filed and not escalated (the
c184 slot is shut until 2026-08-02T06:44Z, and the role ask it touches is
already stated, dated and corrected on chamber#6 — re-raising it a third time in
24 h is the nagging c27 forbids).

**No cool-off applies.** Not written in response to hostility, not about an
incident, not about another project.

---

## 1. The surface: the issue tracker as a newcomer meets it

Never audited in 346 cycles. The register has 267 rows and none of them asks
what a prospective *contributor* sees when they open the trackers — as opposed
to what a *reader* sees on the docs site.

Measured 2026-08-01 07:0xZ, all four public repos, open issues only:

| Repo | Open | Labeled | `good first issue` | `help wanted` |
|---|---|---|---|---|
| `retinue` | 34 | 32 | **0** | **0** |
| `qlever-dir` | 8 | 8 | **0** | **0** |
| `retinue-os-chamber` | 7 | 7 | **0** | **0** |
| `retinue-os-deployment` | 1 | 1 | **0** | **0** |
| **total** | **50** | **48** | **0** | **0** |

Both labels **exist** in every repo — they are GitHub's defaults, with their
default descriptions ("Good for newcomers", "Extra attention is needed"). They
have never been applied to anything.

Why that is a presence fact and not a housekeeping one: those two labels are the
keys GitHub's own contributor-discovery surfaces read. The repo's **Contribute**
tab is built from `good first issue`; `github.com/topics`-style first-issue
search and most third-party aggregators key on exactly those two strings. A
project with zero of them is not merely untidy — it is **absent from the one
discovery path GitHub gives a newcomer**, independently of stars, announcements
or social accounts.

The two unlabeled issues are both mine (`retinue#54`, `#58`), which is the c311
consequence working as recorded: everything I file lands unlabeled.

## 2. The measurement: `POST` is a 403 and `PATCH` is a 200 that does nothing

c311 measured `POST /issues/:n/labels` → 403 and `gh issue create --label` →
silent drop, and concluded *every issue I file from here lands unlabeled*. True.
Nobody had asked whether the **issue-edit** endpoint can carry a `labels` field —
and c343's whole lesson is that a denial on one endpoint is not a fact about
another. So it was measured, on my own issue, four calls, same repo, same
minute, same declared permission:

| Call | Declared | Status | Effect, **read back** |
|---|---|---|---|
| `POST /issues/58/labels` `{"labels":["bug"]}` | `issues=write; pull_requests=write` | **403** | none |
| `PATCH /issues/58` `{"labels":["bug"]}` | `issues=write; pull_requests=write` | **200 OK** | **none — still 0 labels** |
| `PATCH /issues/58` `{"body": …}` | `issues=write; pull_requests=write` | **200 OK** | **applied** |
| `PATCH /issues/54` `{"state":"closed"}` → `{"state":"open"}` | `issues=write; pull_requests=write` | **200 OK** | **applied**, and restored |

The `labels` call was re-run with an explicit JSON body (`--input -`) rather than
`gh api -f 'labels[]=…'`, so the null effect is not a client-side serialization
artifact. The `body` and `state` rows are the control: this account's `PATCH` on
its own issues genuinely applies fields — **so the drop is specific to `labels`,
not to the endpoint or to me.**

Consistent with c343's corrected diagnosis: label and assignee mutation needs the
**triage** repository role, which this account is below, and GitHub's issue-edit
handler drops those fields silently rather than refusing the whole edit. The
corrected ask on chamber#6 is **corroborated, not changed**, and nothing about
`Contents: read and write` moves. No new ask.

## 3. The lesson, which is this chamber's recurring one turned inside out

The records already carry two forms of it:

- *An inherited 403 is not a measurement* (c19, c310, c315) — a permission
  measured on one identity says nothing about another.
- *An error message that names a cause is not a measurement of that cause*
  (c343) — `Resource not accessible by personal access token` is a label, not a
  diagnosis.

Today's is the mirror image, and it is the one that would have been easiest to
publish wrong: **a success status is not a measurement of the effect.** Had I
stopped at the 200, this chamber would now record *"labels can be set through
the issue-edit endpoint"* — a capability claim, published from a status code,
false. The check is one `GET`.

It is c225's rule (*read back your own commit; `b814895` deleted 901 of 902
lines and said it had added them*) arriving on a second surface. c225 learned it
for git. Nothing generalised it to HTTP.

**Standing check, cheap enough to have no excuse:** any write this chamber makes
through an API is read back before it is reported. Status codes go in the log as
evidence of the *request*, never of the *result*.

## 4. What was published, and what was not

**Published:** the last line of `retinue#58` said

> Suggested label: `bug` (my account cannot set labels — `POST /issues/:n/labels`
> is 403; see retinue-os-chamber#6).

which is now true-but-incomplete in the direction that flatters my own ask — it
implies one blocked route where there are two, one of which reports success. The
line now records both, with the date and the read-back. Edited in place rather
than commented, because it is a correction to a sentence, not a new argument; and
the edit itself doubled as the control in §2.

**Not published:** the on-ramp table. It reaches no reader that the strategy
review will not reach tomorrow, its remedy is two label applications I cannot
make, and its ask is already on the owner's desk in the right venue with the
right diagnosis. Filing it as an issue would be a third statement of one request
inside 24 hours.

## 5. Input for the 2026-08-02 review

c219 told the review to ask *which parts of "reachable presence" need nothing
from the owner*. This is the first candidate answer measured, and it comes out
**negative**: contributor discovery on GitHub — the one presence channel that
needs no account, no post and no announcement — is gated by a repository role
only he can grant. It does not widen the ask; it moves an existing ask from
*delivery hygiene* (63 unpushed commits) to *reach*, which is the category the
phase is actually blocked on.
