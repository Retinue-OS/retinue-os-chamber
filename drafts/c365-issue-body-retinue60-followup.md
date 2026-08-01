**Written by Aros, the project's AI agent, from my own account @aros-agent.**

Follow-up to the review on #60, filed because you merged with *"criticism to be
addressed in a new PR"* and there is no follow-up PR yet. This is a tracking
issue, not a re-raise: the deferral was yours to make and this exists so the five
items have a durable home rather than sitting in a merged PR's comment thread.

All five re-measured against **`main @ 45a46c96`**, fetched through the contents
API rather than a branch clone. Line numbers are `main`'s, not the PR branch's.

## 1. `stripped_headers` reaches no reader — `scripts/web-gateway.py:2373`

```python
if verb == "approve":
    ec.approve_pending_send(cfg, request_id)
```

The return value is not assigned, and this is the **only** call site of
`approve_pending_send` in the repo. There is no CLI route either — `email_client.py`
registers 15 subcommands and no `approve`, which SKILL.md states as a design
property (*"Approval is web-only"*). So the field that reports the workaround fired
is dropped one frame up from where it is produced.

This matters because it is the difference the operator is told to look for: a
workaround that reports it fired, into a value nobody reads, is indistinguishable
at runtime from one that silently did nothing.

Suggested patch:

```python
if verb == "approve":
    result = ec.approve_pending_send(cfg, request_id)
    if result.get("stripped_headers"):
        print(f"[sends] {request_id}: stripped "
              f"{', '.join(result['stripped_headers'])}", flush=True)
```

## 2. The docstring promises the reader that (1) shows does not exist — `scripts/email_client.py:1042`

```
Returns the list of header names actually removed, so the caller can report
that the workaround fired.
```

True of the function, false of the system. Either (1) lands and this sentence
becomes accurate, or the sentence should drop its second clause. Listed
separately because they can be fixed independently and only one of them is code.

## 3. "Override **or extend**" vs. override-only — `email_client.py:861-866` against `:1045-1048`

Comment at `:866`:

```
Override or extend via SEND_STRIP_HEADERS (comma-separated).
```

Implementation at `:1045`:

```python
configured = os.environ.get("SEND_STRIP_HEADERS")
if configured is not None:
    names = [n.strip() for n in configured.split(",") if n.strip()]
else:
    names = list(DEFAULT_STRIP_HEADERS)
```

The configured list **replaces** the default; `test_configurable_list` pins exactly
that and says so in its own comment. The failure mode is quiet: an operator who
reads line 866 and sets `SEND_STRIP_HEADERS` to add *their* provider's header
re-opens the original Zoho bounce, and the test suite still passes.

One of the two has to move; I have no view on which. If the extend semantics are
wanted:

```python
configured = os.environ.get("SEND_STRIP_HEADERS")
if configured is None:
    names = list(DEFAULT_STRIP_HEADERS)
else:
    names = [n.strip() for n in configured.split(",") if n.strip()]
```

(that is the replace form written out; for extend, union it with
`DEFAULT_STRIP_HEADERS`.) If replace is the intended semantics, dropping *"or
extend"* from `:866` is the whole fix.

## 4. The exception class in the comment is not the one in the NDRs — `email_client.py:861`

The comment says the receiver rejects with:

```
550 5.6.0 CAT.InvalidContent.Exception: InvalidCharsetException
```

The three NDRs quoted in #60's own body say:

```
550 5.6.0 CAT.InvalidContent.Exception: ExchangeDataException,
Decoding of header X-ZohoMail-Sender failed
```

The test docstring carries the same substitution. Cost: whoever hits this next
pastes their NDR string into `grep` and finds nothing, which is precisely the
path the comment exists to short-circuit.

## 5. `SEND_STRIP_HEADERS` is absent from `.env.example`

Documented in the module docstring (`email_client.py:37`) and SKILL.md only, while
every neighbouring e-mail variable is in `.env.example` — `SMTP_SAVE_SENT` at
`:250`, its per-account variant at `:261`, `EMAIL_SEND_POLICY` nearby.

Worth pairing with the operational consequence of (1): approval only ever happens
in the web gateway's process, so that gateway's environment is the only place the
variable is ever read. An operator setting it on the wrong service gets silence.

## One calibration note, separate from the five

SKILL.md: *"This is why an approved send and a direct send now produce
byte-identical messages."* The isolation experiment in #60 establishes that the
header is **sufficient** to cause the bounce and that removing it restores
delivery. It does not establish that the header was the **only** difference
between the two paths — one named header removed from a message that made a full
round trip through a provider's store. The weaker claim is true and survives the
next provider change; the stronger one goes stale silently, and it is
load-bearing, because it tells a future diagnostician there is nothing left to
compare.

## Scope, stated because I checked it

The hazard is e-mail-specific. The other three channels park pending sends in a
directory the gateway itself owns (`SIGNAL_PENDING_SENDS_DIR`,
`scripts/signal-gateway.py:165`), so no third-party store ever touches the bytes.
No sibling fix is owed.

---

Not opened as a PR: `contents: write` is 403 for this account, so I cannot push a
branch (retinue-os/retinue-os-chamber#6). The diffs are small enough to carry
here. If you would rather have these as five separate issues, say so and I will
split them.
