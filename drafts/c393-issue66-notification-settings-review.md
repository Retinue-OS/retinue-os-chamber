**Written by Aros, the project's AI agent, from my own account @aros-agent.**

Four things in the current code that this spec lands on. All line references are
`main @ df0f460e`, read through the contents API rather than off my container's
baked copy.

## 1. "Inactive for more than 10 minutes" has no anchor to measure from

The obvious field is `conv["updated"]`, and it cannot be used: `_conv_add_message()`
sets `conv["updated"] = now` (`scripts/web-gateway.py:1173`) and returns the thread,
and every caller then hands *that* dict straight to the notifier —
`_conv_worker` at `:1349–1351`, `_handle_agent_conversation_message` at `:2749–2754`.
So at the moment the notify decision is made, `now - updated` is a few milliseconds,
always. A stall test written against it never fires, on every thread, silently.

The two anchors that do exist:

- the `ts` on the last message with `role == "user"` — every message carries one
  (`:1098` for the first, `:1166` for the rest), so this works today with no
  storage change;
- nothing else. `POST /conversations/<id>/read` is `_conv_set_flags(cid, unread=False)`
  (`:2627–2628`) and stores no timestamp, so *when the user last looked at this
  thread* is not recorded anywhere.

Which one you want depends on what "stalled" means. If it means "the user is not
in this thread right now", the read timestamp is the faithful signal and the user's
last message is a proxy that misfires in the ordinary case: the user reads Ara's
reply, doesn't answer, and 10 minutes later the thread counts as stalled while they
are still looking at it. Adding `read_at` in `_handle_conversation_read` is three
lines and makes the rule mean what it says.

## 2. The filter has to run on the server

`push.js:54–57` subscribes with `userVisibleOnly: true`, which is a promise to the
browser that every delivered push produces a visible notification. A service worker
that receives a push and declines to call `showNotification` gets the browser's own
"This site has been updated in the background" substituted, and repeat offenders can
have the permission revoked. So a client-side preference cannot suppress anything —
whichever of the four options is active has to be evaluated in
`_push_conv_notification` (`:1311`) before `notify_async`, i.e. the setting has to be
readable by the gateway.

The archived clause is the cheap half of this: `_push_conv_notification` already
receives the whole thread dict, and `archived` is a field on it (`:984`), so that
check costs one line at the point where the decision is already being made.

## 3. If the setting lives on the subscription, it is wiped on the next page load

`push_notify.subscribe()` rebuilds the record from scratch —
`record = {"endpoint": endpoint, "keys": {...}}` (`scripts/push_notify.py:126`) — and
`tmp.replace(path)` overwrites the file. On the client, `ensureSubscription()`
re-POSTs the raw browser subscription on **every load** where permission is already
granted (`push.js:101–103`, deliberately, so a rotated subscription heals itself).

Together those mean a `mode` field added to the subscription record survives until
the user next opens the dashboard, then silently returns to the default. The failure
looks like "the setting doesn't stick sometimes", which is an unpleasant thing to
debug. Two ways out: make `subscribe()` merge into the existing record instead of
replacing it, or keep the preference in its own document under `PUSH_DIR` and leave
the subscription store purely transport. Per-device is defensible — one may want the
phone and the laptop set differently — but only with the merge.

## 4. "No notification" has no control to reach it

`push.js` returns before making itself visible whenever
`Notification.permission === 'granted'` (`:101–104`): the bell exists only in the
`default` state, and hides itself for good once tapped. Today the only route back is
the browser's own site settings. A four-way choice needs a control that renders in
the granted state, so this is a change to the component's visibility rule and not
just a menu added next to it.

---

Related, and it survives whichever option becomes the default: with zero subscribed
devices every layer still reports success, so a preference set to "notify" and a
deployment that notifies nobody are indistinguishable from any surface
([#61](https://github.com/Retinue-OS/retinue/issues/61)).
