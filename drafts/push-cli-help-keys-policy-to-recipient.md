# Draft — the three push CLIs describe the send policy as a property of the recipient

status: filed (retinue#36, 2026-07-26)
Written cycle 181, 2026-07-26 (02:0x UTC). Measured against `main` (`26297a2`,
2026-07-25 15:12:01Z), cloned fresh to `/tmp/fwmain` — not read from
`/workspace/deployment`, which is behind `main` (the c179 habit).

Venue: **new issue on `Retinue-OS/retinue`**, documentation label. Not a comment
on retinue#9 — #9 is the "bot" wording, a different noun and a different error,
and its scope is Telegram. Not a comment on retinue#26 — that is about the
"an agent can never approve its own send" claim in four prose files. This is a
third, disjoint set of sentences in a third set of files.

Filing criterion: **(b) a false claim on a public surface.** The claim inverted
here is one of the four the project leads with.

---

## The finding

`SIGNAL_SEND_POLICY`, `WHATSAPP_SEND_POLICY` and `TELEGRAM_SEND_POLICY` resolve
their category from the **sending** account — the gateway's own
`SIGNAL_ACCOUNT` / `WHATSAPP_ACCOUNT` / `TELEGRAM_ACCOUNT`. The recipient is
never consulted on the outbound path. That is what makes a dedicated agent
identity able to run `allow` while the owner's own number stays `verify`, and it
is the whole reason the control is interesting.

The three CLIs an agent actually invokes describe it the other way round.

| File (main, `26297a2`) | Line | Text |
|---|---|---|
| `scripts/signal-push.py` | 59 | `--user-approved` help: "bypasses the verify flow for **'trust'-category recipients**" |
| `scripts/whatsapp-push.py` | 10 | "a `verify` **recipient** queues the message as a pending send" |
| `scripts/whatsapp-push.py` | 12 | "a `trust` **recipient** sends directly only with `--user-approved`" |
| `scripts/whatsapp-push.py` | 22 | example comment: "bypasses verify for a **'trust' recipient**" |
| `scripts/whatsapp-push.py` | 61 | `--user-approved` help: "'trust'-category **recipients**" |
| `scripts/telegram-push.py` | 53 | `--user-approved` help: "'trust'-category **bots**" — already covered by the retinue#9 comment, whose suggested diff changes it to "accounts" |

Everything else in the repository gets it right, and several places make the
distinction explicitly:

- `scripts/signal-gateway.py:136` — "Keyed by the *sending* account number (this
  gateway's own `SIGNAL_ACCOUNT`), **NOT the recipient**"
- `scripts/signal-gateway.py:976`, `scripts/whatsapp-gateway.py:132,812`,
  `scripts/telegram-gateway.py:118` — same, in the module comment and in
  `_outbound_policy_category()`'s docstring
- `CLAUDE.md:321`, `:365`, `:397` and `README.md:289` — all four say "not the
  recipient" in so many words
- `tests/test_signal_send_policy.py:54`, `tests/test_whatsapp_send_policy.py:45`,
  `tests/test_telegram_send_policy.py:46` — "never the recipient"

So the six wrong sentences are not a house shorthand. They are the only six
places in the tree that state the inverse of what the tree everywhere else is at
pains to spell out, and they are in the file that is in front of an agent at the
moment it decides whether to send.

## Verified, not assumed

The category resolution reads the sending account and nothing else
(`scripts/signal-gateway.py:986-999`; the WhatsApp and Telegram versions are
structurally identical), and the send handler applies it as:

```python
category = _outbound_policy_category()
if category == "verify" or (category == "trust" and not user_approved):
    # register a pending send, reply 202 pending_approval
```

(`scripts/whatsapp-gateway.py:1123-1124`, `scripts/signal-gateway.py:1303`.)
`--user-approved` therefore has an effect in exactly one case — the *sending
account* is in the `trust` category — and no effect at all that depends on who
the message is going to.

**No behaviour is wrong.** Enforcement is in the gateway and the gateway is
correct. The defect is entirely in the description, which is why this is
documentation and not security.

## Why it is worth an issue rather than a note

1. **It puts the wrong mental model at the decision point.** An agent that reads
   `--help` and takes the category to be a property of the recipient has one
   natural next thought: *this recipient is a trusted one, so `--user-approved`
   is appropriate here.* `--user-approved` is the flag whose entire meaning is
   asserting that a human already approved this specific send. The wrong noun
   turns a claim about the human into an inference about the address book.
2. **`signal-push.py` has no other mention of the control.** Grepping the file
   for `POLICY|verify|approval|pending`, the docstring — including its
   Configuration section, which lists three environment variables — never names
   `SIGNAL_SEND_POLICY` and never says a send can be queued. Line 59 is the file's
   only description of the send control, and it is the one that is wrong. The
   WhatsApp and Telegram siblings both document the policy in the docstring;
   Signal, the original and the one `CLAUDE.md` documents most fully, does not.
3. **It is the claim the project leads with.** "Outbound sends keyed to the
   sending identity, so a dedicated agent identity can run `allow` while the
   owner's identities stay locked" is one of the architecture's four headline
   arguments. A reader who checks it in the CLI first finds it contradicted.

## Suggested fix

```diff
--- a/scripts/signal-push.py
+++ b/scripts/signal-push.py
@@ -22,6 +22,12 @@ Examples:
+Outbound is gated by SIGNAL_SEND_POLICY, keyed by the gateway's own sending
+identity (SIGNAL_ACCOUNT), not by the recipient: an `allow` account sends
+directly, a `verify` account queues the message as a pending send that must be
+approved on the web gateway's /sends page, and a `trust` account sends directly
+only with --user-approved. An undeclared account defaults to `verify`. On a
+queued send this prints the approval URL instead of confirming delivery.
+
 Configuration (environment):
@@
-                             "bypasses the verify flow for 'trust'-category recipients")
+                             "bypasses the verify flow when this gateway's own "
+                             "sending account is in the 'trust' category")
```

```diff
--- a/scripts/whatsapp-push.py
+++ b/scripts/whatsapp-push.py
@@
-Outbound is gated by WHATSAPP_SEND_POLICY (see the gateway): a `verify` recipient
-queues the message as a pending send that must be approved on the web gateway's
-/sends page; a `trust` recipient sends directly only with --user-approved. On a
-queued send this prints the approval URL instead of confirming delivery.
+Outbound is gated by WHATSAPP_SEND_POLICY, keyed by this gateway's own sending
+account (WHATSAPP_ACCOUNT), not by the recipient: a `verify` account queues the
+message as a pending send that must be approved on the web gateway's /sends
+page; a `trust` account sends directly only with --user-approved. On a queued
+send this prints the approval URL instead of confirming delivery.
@@
-    # Assert the user already approved (bypasses verify for a 'trust' recipient)
+    # Assert the user already approved (bypasses verify for a 'trust' account)
@@
-                             "bypasses the verify flow for 'trust'-category recipients")
+                             "bypasses the verify flow when this gateway's own "
+                             "sending account is in the 'trust' category")
```

`scripts/telegram-push.py:53` is covered by the suggested diff already posted on
retinue#9; it needs "bots" → "accounts" and nothing more.

## Left out on purpose

All three CLIs `return 0` when the gateway replies `202 pending_approval`
(`signal-push.py:97`, `whatsapp-push.py:97`, `telegram-push.py:89`), i.e. a
queued-but-undelivered escalation exits with the same status as a delivered one.
That is defensible — the call succeeded, and the notice is printed on stdout —
and it is a design question rather than a false statement, so it does not belong
in an issue whose subject is a wrong noun. Recorded here so the next cycle
neither re-derives it nor files it as a discovery.

## Record

- Filed as [retinue#36](https://github.com/Retinue-OS/retinue/issues/36), label
  `documentation`, 2026-07-26 02:1x UTC.
- Not escalated: no account, money, terms or legal question. Not a security
  finding — enforcement is correct and unchanged; only its description is wrong.
- Found by taking the messaging-CLI group from c177's mechanically-measured
  never-mentioned list, the group c177 named as one of the two cheap picks while
  the security item is open.
