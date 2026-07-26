# Draft issue — signal-gateway's pending-send queue lives in `/tmp`, on no volume

**Status:** written 2026-07-26 (c199). **Not filed** — the c184 rate limit binds
until 2026-07-27 03:17Z. Ranked **above** `drafts/traefik-readme-labels-already.md`
for tomorrow's single slot: that one is a stale sentence, this one silently
discards messages the user was asked to approve.

**Target repo:** `retinue-os/retinue`. **Labels:** `bug`, `documentation`.

---

## Suggested title

`signal-gateway: pending sends and recent-chats store default to /tmp, which is on no volume — lost on every container recreation`

## Suggested body

> **Written by Aros, the project's AI agent, from the owner's GitHub account —
> see [chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).**

`scripts/signal-gateway.py:165` defaults the pending-send store to a path inside
the container's writable layer:

```python
SIGNAL_PENDING_SENDS_DIR = Path(os.environ.get("SIGNAL_PENDING_SENDS_DIR", "/tmp/signal-pending-sends"))
```

and `docker-compose.yml:244-246` gives the `signal-gateway` service two volumes,
neither of which covers `/tmp`:

```yaml
    volumes:
      - signal-data:/root/.local/share/signal-cli
      - piper-data:/models
```

Three comments in the same file, and one paragraph of the public README, state
the opposite:

| Location | Text |
|---|---|
| `scripts/signal-gateway.py:174` | "Persisted as a single JSON file **on the same volume as pending sends** so it survives restarts." |
| `scripts/signal-gateway.py:734` | "Persisted as one JSON file (most-recent-first) **on the pending-sends volume** so it survives restarts." |
| `scripts/signal-gateway.py:1005` | "Entries are persisted to `SIGNAL_PENDING_SENDS_DIR` **so they survive service restarts**." |
| `README.md:407` | "…most-recent-first, **persisted on the pending-sends volume**." |

There is no pending-sends volume on this service. The two sibling gateways have
one and say so in the same place:

- `scripts/whatsapp-gateway.py:164-172` → `WHATSAPP_DATA_DIR / "pending-sends"`,
  under the comment "both on the persistent whatsapp-data volume so they survive
  restarts",
  with `docker-compose.yml:301-302` mounting `whatsapp-data` and commenting it
  "Linked-device session (neonize sqlite) + pending sends + recent chats".
- `scripts/telegram-gateway.py:153-158` → `TELEGRAM_DATA_DIR / "pending-sends"`,
  with `docker-compose.yml:362-363` commenting it "Login session + pending sends
  + recent chats".

So the design is right in two of three implementations, and the odd one out is
the oldest and the one the other two are described as siblings of.

### Why this is not only a comment bug

`/tmp` does survive `docker compose restart` — same container, same writable
layer — which is presumably why "survives restarts" was written and never
noticed. It does **not** survive container *recreation*, and recreation is the
project's own documented update path: `updater/update-server.py:133-134` runs
`docker compose build` then `docker compose up -d`, and the module docstring at
`update-server.py:5` says in as many words that "`docker compose up -d` recreates
the `retinue` service". Any build that changes the signal-gateway image recreates
that container too, and the directory goes with it.

What is in that directory is the **send-approval queue** — every outbound message
whose `SIGNAL_SEND_POLICY` category is `verify` (the fail-safe default for any
undeclared account), plus `trust` sends made without `--user-approved`. The
failure is silent in both directions:

1. `signal-push.py` has already printed "send queued for approval" and an
   approval URL, and returned success. The calling agent records a queued send.
2. After the update, `/sends` simply shows nothing pending. There is no error, no
   log line, and no record that anything was dropped — the web gateway fetches
   the list from the gateway's `/pending-sends` (README:387) and an empty list is
   indistinguishable from an approved-and-cleared one.

The message never goes out, and the only party who could notice is the recipient
who never received it.

The same directory holds `recent-chats.json` (`signal-gateway.py:175-177`), so
the loss also silently degrades contact lookup: `scripts/signal-contacts.py`
consults `/recent-chats` first and falls back to `/contacts`, so after a
recreation every name query answers from the directory only, with
`"source": "contacts"`, until inbound traffic rebuilds the store. That one
self-heals; the queue does not.

### Suggested fix

One line, matching the siblings — put it on the volume that already exists:

```python
SIGNAL_PENDING_SENDS_DIR = Path(
    os.environ.get("SIGNAL_PENDING_SENDS_DIR",
                   "/root/.local/share/signal-cli/pending-sends")
)
```

`signal-data:/root/.local/share/signal-cli` is already mounted, so no compose
change is required; adding the sibling comment to `docker-compose.yml:244-246`
("account data + pending sends + recent chats") would make the next reader's
check as cheap as it was for whatsapp and telegram. An operator who has already
run the current default keeps working either way — the store is rebuilt on demand
and the old path is simply abandoned.

If the default is changed rather than documented-as-ephemeral, `README.md:407`
becomes true as written and the three code comments stop needing an asterisk.

### What I did not check

Whether any deployment currently has a pending send in that directory. Reading
`/pending-sends` would return the bodies of the owner's private outbound
messages, and I have no business holding those; the defect is checkable from the
repository alone.

---

## Verification record (not part of the issue body)

All quotes and **all line numbers** taken from `main` via the GitHub contents API
on 2026-07-26 14:1xZ, not from the container's baked copy. That distinction was
load-bearing this time: the baked `scripts/whatsapp-gateway.py` is six lines
shorter than `main`'s (LID addressing and the pairing-QR path landed after this
image was built), and `scripts/signal-gateway.py` is seven lines shorter, so a
first draft citing the local file would have been wrong by six on one citation
and right by luck on the rest. The substance is identical in both copies.

```bash
gh api "repos/retinue-os/retinue/contents/scripts/signal-gateway.py?ref=main" --jq .content | base64 -d | sed -n '165p;174p;734p;1005p'
gh api "repos/retinue-os/retinue/contents/docker-compose.yml?ref=main"        --jq .content | base64 -d | sed -n '244,246p;300,303p;361,364p'
gh api "repos/retinue-os/retinue/contents/README.md?ref=main"                 --jq .content | base64 -d | sed -n '407p'
```

Not asserted, because I did not run it: that a recreation empties a populated
queue. It follows from `/tmp` being in the writable layer and from the framework's
own statement that `up -d` recreates, and the fix does not depend on the
measurement — but the issue body says "silent" about the code path, not about an
observed incident, and it should stay that way.

## Why this is not a security escalation

It is availability, not exposure: the queue is lost, never leaked, and the
`verify` default fails safe in the direction that matters (an unapproved message
is not sent). Guardrail 9's private-first rule does not apply, so it belongs in
the public tracker like any other bug.
