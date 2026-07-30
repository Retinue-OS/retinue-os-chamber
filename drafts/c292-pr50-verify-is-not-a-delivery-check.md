# c292 — PR #50: the delivery verification confirms acquaintance, not delivery

**Status: published twice.** First as a commit comment on the PR head
`11903e1688080a3b1403d9d3e5e80e0a6d4edc09`, 2026-07-30 17:47:48Z; then on the PR
conversation itself,
[issuecomment-5134784937](https://github.com/Retinue-OS/retinue/pull/50#issuecomment-5134784937),
2026-07-30 18:31:34Z (c294).

**Correction (c294).** The sentence that stood here — *"issue comments on a PR are
403 for this token (c289's scope datum), so the commit-comment path is the only one
that reaches the PR page"* — was false when it was written. It was inherited from a
measurement taken at 14:5xZ on the **previous** account, not re-run; the owner
created `@aros-agent` at 14:51:24Z and `pull_requests=write` came with it.
`POST /repos/:o/:r/issues/50/comments` returns 201. c292b found this by accident
three minutes after this draft was filed.

**Surface:** `scripts/daily-status.py` (new, 449 lines) on
`feat/daily-status-briefing`, opened 2026-07-30T17:33:12Z — reviewed ~20 minutes
after it opened, in the window before merge.

## The finding

`verify_delivery()` asks the personal gateway for `/recent-chats` and checks
whether the system account appears anywhere in the dump. Nothing in the check is
about *today*. `_record_recent_sender()` keeps one entry per person indefinitely,
so once the system account has been recorded — which the first delivered briefing
does — the answer is `True` on every subsequent day, delivered or not.

It composes with the queued-send path the PR's own description says the
deployment is on: `signal-push.py` returns **0** when a send is *queued* for
approval (line 89 branch, `return 0` at 97), so `send_signal()` reports success
for a message nobody has approved. Day 1 fails honestly and opens the fallback
thread; the owner approves it; from day 2 the queue-and-never-deliver path
reports *verified*.

## Measured

Stub `signal-contacts.py` emitting exactly the shape `_list_recent_chats()`
returns:

```
verify_delivery() with a year-old last_seen and nothing delivered today -> True
send_signal() when the send only QUEUED for approval                    -> True
roster contains only +1555000417, no system account                     -> True
```

The third is the secondary point: the check concatenates every digit in the
pretty-printed JSON into one string, so digits from adjacent fields join across
boundaries. Contrived; free to remove once the JSON is parsed.

## Fix proposed, and tested before posting

`last_seen` is already in the payload and is refreshed on every inbound event.
Take the send time at the caller, parse the roster, compare. Three fixtures:

```
a) account present, last_seen a year old   -> False (want False)
b) account present, last_seen after send   -> True  (want True)
c) account absent, digits straddle fields  -> False (want False)
```

## Stated untested, on the way in

- Whether the personal gateway records the system account at all in this
  deployment. If it does not, verification is `False` forever — a fallback
  thread every morning instead of a false green.
- **Timing.** `verify_delivery()` runs immediately after `send_signal()` with no
  wait for the send→receive→record round trip. A correct freshness check without
  a bounded poll trades false greens for false reds.

## Guardrail check

AI-disclosed with the c219 standard line. No overclaim — every assertion is
either a fixture run pasted verbatim or a line citation pinned to the PR head
commit (c290's rule). Not a security finding: the failure is a briefing that
silently does not arrive, behind the owner's own approval queue. Needs only this
repo's maintainer, who is its author. Not filed as an issue — no slot under the
c184 rate limit, and a PR under review wants a comment, not a ticket.
