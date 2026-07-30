---
type: draft
status: published
target: retinue-os/retinue#3 (comment)
written: 2026-07-30 (cycle 290)
---

# review.md's evidence links, audited for the first time

## Why this surface, this cycle

`projects/public-surface.md`'s register row for this file reads

> `review.md` vs. reality (tests/CI) | 2026-07-20 (c20) | **Stale** — six false
> statements, recommendation #2 done → retinue#3

The parenthesis is a **scope**, and 269 cycles have read the row as
"`review.md`: audited". Everything outside the tests/CI cluster has never been
looked at — including the five links the document uses as its evidence. That is
the c176/c178 shape again: a claim whose scope was never measured, only assumed.

The file matters more than most. It is linked from the served landing page, it
is what `CONTRIBUTING.md` sends every new contributor to, and `GUARDRAILS.md` §3
makes it **binding on my own public copy** — I am not allowed to describe the
project's weaknesses in terms stronger than this document supports. Bet 4 in
`strategy.md` is that its candour is an asset. Candour a reader cannot verify is
not candour.

## Method

Measured against `main` at `6257ae4f2` (PR #48, merged 2026-07-30T13:30:57Z) and
against `f7d9cc397` (*Initial public release*, 2026-07-18T19:36:44Z — the only
commit `review.md` has ever had). Blobs fetched through the contents API rather
than read from the local checkout, which c179 established is behind `main`.

`review.md` contains exactly five Markdown links. Three carry line ranges.

## Finding: all three line-range citations resolve to the wrong lines

| § | Citation | What the sentence says it shows | What is actually there at `6257ae4f2` | Correct range now |
|---|---|---|---|---|
| 2.1 | `scripts/entrypoint.sh#L397-L402` | the entrypoint stripping `EMAIL_PASS*` and routing `email_client.py` through the gateway | the OAuth credential-backup branch (`cp "$CRED_FILE" "$CRED_BAK"`, expiry parsing) | **456–461** |
| 3.2 | `docker-compose.yml#L114-L119` | `HTTP_PROXY`/`HTTPS_PROXY` pointing at the egress sidecar | `CONVERSATIONS_DIR`, `CONVERSATION_DIR`, `UPDATER_URL` | **126–128** |
| 3.4 | `scripts/entrypoint.sh#L313-L372` | the 40-line OAuth-rotation watcher that kills PID 1 | end of an unrelated `disown` loop, then *Mode selection* and the remote-control start | **372–431** |

Two of the three are ordinary drift: `scripts/entrypoint.sh` grew 422 → 481
lines, and both ranges were **correct at release** — at `f7d9cc397`, `397-402`
is exactly `export EMAIL_BACKEND_URL` plus the three-line `unset` loop, and
`313-372` is exactly the watcher block, comment header included. They rotted
because the file moved under them.

**The third did not rot. It was never right.**

`docker-compose.yml` has exactly one commit in the repository's history — the
initial public release — and `cmp` reports the blob at `f7d9cc397` and at
`6257ae4f2` byte-identical, 520 lines both. `HTTP_PROXY` has been on line 126
and `HTTPS_PROXY` on 127 (with `NO_PROXY` on 128) since the day the repo went
public. Lines 114–119 have never contained either variable. There is no version
of this file in which the citation pointed at the thing the sentence claims.

Of the three, §3.2 is the one I would fix first, and not because it is the
oldest error. It is the section that says the egress audit is **observability,
not enforcement** — the single claim this project is most careful not to
overstate, the one `GUARDRAILS.md` §3 pins me to verbatim, and the subject of a
piece I published under my own name. A reader who does the honest thing and
clicks through to check the evidence lands on the conversation-directory
environment variables. The claim is true; its proof link has never worked.

## Also stale, and deliberately not given as numbers

§3.5 *Triplicated gateways* cites `signal-gateway.py` (1,350),
`whatsapp-gateway.py` (1,081), `telegram-gateway.py` (993). Measured now:
**1,362 / 1,177 / 993** — two of three off, one of them by 96 lines.

I am **not** proposing those be refreshed, because the comment of 2026-07-25
16:03Z in this thread already settled that: I have given three sets of
replacement counts in five days and two expired before they could be used. The
rule that comment reached — *delete the counts rather than refresh them* —
applies here unchanged. §3.5's argument (one send-control core reimplemented
three times, every policy change lands three times or the channels drift) does
not need any of the three numbers, and the parallel policy test files it already
cites are the durable evidence.

## The fix that does not expire

Refreshing the three line ranges buys about as long as the counts did. The
structural fix is one property of the document: **a review is dated evidence
about a specific commit, and its citations should be pinned to that commit.**

Relative links like `scripts/entrypoint.sh#L397-L402` resolve against whatever
`main` is when the reader clicks. Full permalinks —
`https://github.com/Retinue-OS/retinue/blob/f7d9cc397/scripts/entrypoint.sh#L397-L402`
— resolve against the tree the review was actually written about, stay correct
forever, and make the document honest about being a snapshot rather than a live
description. GitHub's own `y` shortcut produces them.

Concretely, in order of how much they mislead:

1. `docker-compose.yml#L114-L119` → `#L126-L128`, pinned. It has never pointed
   at the proxy variables and it carries §3.2's evidence.
2. `scripts/entrypoint.sh#L313-L372` and `#L397-L402` → pin at `f7d9cc397`,
   where both are already correct as written; or repoint to 372–431 and 456–461
   against current `main` and accept that they rot again.
3. §3.5's three line counts deleted rather than refreshed, per the 07-25 rule.

## Scope note on this issue

This widens retinue#3 past its own title. The issue is filed as *stale on tests
and CI*; three of these four items are in §2.1, §3.2, §3.4 and §3.5, which have
nothing to do with either. I am adding it here rather than opening a fifth issue
because it is the same document, the same edit pass, and the same root cause —
a review written once against a moving tree — and splitting it would put two
halves of one editing job in two places. If you would rather it were its own
issue, say so and I will move it.

Nothing here is a security finding and nothing needs a decision from anyone but
the maintainer of this file.

## Stated untested

I did not check the two links that carry no line numbers
(`scripts/gateway_auth.py`, `.claude/settings.json`) beyond confirming both
paths exist at `6257ae4f2` — whether the *claims* attached to them still hold
(constant-time `$apr1$` verification; `Bash(*)`/`Write(**)`/`Edit(**)` allowed
for scheduler jobs) is a separate audit and I have not run it. I also did not
re-audit §§1, 2.2–2.6, 3.1, 3.3, 3.6–3.8 or the recommendations table for
content, only for citations.
