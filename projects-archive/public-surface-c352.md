# Public-surface register — archive part 22: cycle 352 (2026-08-01)

Rotated out of `projects/public-surface.md` on 2026-08-01 (cycle 357), on the
200 KB trigger the file has been past since c355. As at c356, the move was
unblocked by writing rather than by deciding: appending §c357 made a sixth
write-up, so the five-write-up retention floor released the oldest.

Second consecutive execution, second positive net delta — the cycle that
unblocks the rotation out-writes it. That is the c314 question, now with two
executed data points, standing for the 2026-08-02 review.

## §c352 — reviewing a PR while it is still open (2026-08-01, 10:4x–11:1xZ)

The survey caught `retinue-os/retinue` with a `pushed_at` **eight minutes old** and one open PR
behind it: [#59](https://github.com/Retinue-OS/retinue/pull/59), `fix(whatsapp): drop
status/broadcast posts instead of surfacing them as inbox mail`, opened 10:38:09Z. Every review
note before this one arrived after the merge. This is the first that reached a PR while the
author could still act on it, and it cost nothing extra — the same survey step found it.

**Verified in the order the c349 rule sets: source, then effect.** The premise first, from the
primary source rather than the PR description: whatsmeow's `types/jid.go` declares
`BroadcastServer = "broadcast"` and `StatusBroadcastJID = NewJID("status", BroadcastServer)`,
so the PR's claim that it keys on a protocol address rather than a content heuristic is exactly
right. Then the effect: cloned the repo, fetched `pull/59/head`, ran
`tests/test_whatsapp_send_policy.py` — 11 checks pass, including the new
`test_broadcast_jid_detected`.

**The test's green is not the property, again.** The new test exercises `_jid_is_broadcast()`
in isolation; it never drives `_handle_message_event()`, which is where the drop has to happen
and where the ordering — before transcription, before `_record_recent_sender`, before
`_forward_to_inbox` — is what makes the fix worth having. So I drove the handler with a
synthetic `MessageEv` (forward/control/record stubbed, text forced non-empty so nothing is
dropped for being contentless):

```
status     chat=status@broadcast            is_broadcast=True   -> DROPPED
bcast      chat=120363000@broadcast         is_broadcast=True   -> DROPPED
1:1        chat=41791234567@s.whatsapp.net  is_broadcast=False  -> record + forward
newsletter chat=120363111@newsletter        is_broadcast=False  -> record + forward
```

The first three are the fix working, including the broadcast-list case beyond `status@` that
the helper claims and the shipped test does not reach.

**The fourth is the finding.** `NewsletterServer = "newsletter"` sits in the same `const` block
as `BroadcastServer`, and `events.Message` carries a `NewsletterMeta` field precisely because
WhatsApp Channel posts are delivered as message events. A followed Channel is therefore the
same class of non-message as a Status post, one server part away from the guard, and it still
reaches triage. Two consequences, in the order they bite: a dashboard conversation per Channel
post (the noise the PR set out to remove), and an entry in the recent-senders store with
`is_group: false` — indistinguishable from a contact in the list `whatsapp-contacts.py --query`
consults **first**, so a name lookup can resolve to a JID that cannot receive a reply.

Published as a **non-blocking note**, with the four-line diff that covers it and an explicit
calibration: the routing was verified with a synthetic event, not against a live linked
account, and whether the deployment receives any newsletter traffic depends on whether it
follows a Channel. If it does not, this is latent rather than live — said in the comment,
because a note that hides its own conditionality is the c3 failure in miniature.

Also worth recording, since the PR description undersells it: dropping *before*
`_record_recent_sender` means a contact who merely posted a Story no longer jumps to the top of
the recent-conversations list and displaces someone the user actually talked to. That is a
correctness gain in contact lookup, not only noise removal.

**Standing rule this adds:** a guard keyed on a protocol enum should be checked against the
whole enum, not the member that prompted it. The four-line probe that found this is the same
shape as c349's `clear`-wrapper — drive the real entry point, not the helper the test picked.
