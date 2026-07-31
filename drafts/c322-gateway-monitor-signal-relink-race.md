**Written by Aros, the project's AI agent, from my own account @aros-agent.**

Reviewed this branch before it becomes a PR, because the finding is cheaper to act on now. Measured by importing this commit's own `scripts/signal-gateway.py` and driving its state machine, not by reading the diff.

### `GET /qr` on the Signal gateway starts a second `signal-cli link` right after a successful pairing

`_relink_qr_response()` guards on:

```python
if _health_snapshot()["connected"] and not _RELINK_ACTIVE.is_set():
    return 409, {"status": "connected", ...}
```

`connected` is `(now - _link_state["last_ok"]) <= SIGNAL_HEALTH_MAX_AGE`, and `last_ok` is written only by the receive poll loop — the loop this same flow parks:

```python
while True:
    if _RELINK_ACTIVE.is_set():
        time.sleep(SIGNAL_POLL_INTERVAL)
        continue
```

`_relink_worker` on `returncode == 0` sets `_relink["error"] = None` and nothing in `_link_state`. So after a pairing succeeds, `connected` stays `False` until the loop resumes and completes one receive — `SIGNAL_POLL_INTERVAL` (3 s) plus the receive's `--timeout 5`, so roughly 3–13 s, and up to `SIGNAL_CLI_TIMEOUT` (30 s) worst case.

Meanwhile the `/gateways` page refreshes every rendered `img.qr` every 20 s, and only reloads itself at 60 s — so the `<img>` outlives the pairing it was shown for. A refresh landing in that window reads the guard while it still says "down".

Reproduced against this commit's file, worker stubbed to exit like a successful `link`, nothing else changed:

```
1. down, no relink active -> health.connected = False
2. first GET /qr -> 202 {'status': 'starting'}
3. after a successful pair: _RELINK_ACTIVE = False | health.connected = False
4. page auto-refresh of the SAME <img> -> 202 {'status': 'starting'} | relink started again = True
5. same GET after one successful receive poll -> 409 {'status': 'connected', ...}
```

Step 4 is the defect. Step 5 is what the guard is meant to do.

What follows, in order of cost:

- The second attempt sets `_RELINK_ACTIVE` again, so the receive loop stays parked and `last_ok` cannot advance. It is released only when the 180 s `SIGNAL_RELINK_TIMEOUT` timer kills the subprocess — after which there is another 3–13 s window before the loop records a success, which the next 20 s refresh can hit again. An open `/gateways` tab can hold a healthy gateway in this state, and inbound Signal is not polled while it lasts.
- `GATEWAY_MONITOR_FAILURES` (2) × `GATEWAY_MONITOR_INTERVAL` (60 s) = 120 s, inside that 180 s — so the monitor reports the channel down to the user shortly after they successfully re-paired it.
- The page keeps showing a QR, and once the second attempt mints its URI, a *new* one, to a user who has just scanned. That invites a second scan and a duplicate linked device.

**The fix is one line, and this branch already contains the right pattern.** Record the pairing's own outcome rather than waiting for the poll to notice it:

```python
if proc.returncode == 0:
    _note_receive_result(True)   # the pairing is the proof
```

Telegram's `_qr_login_loop` does exactly that — `_set_conn(authorized=True, ...)` runs before the `finally` clears `task_running`, so its guard reads state set by the pairing itself. WhatsApp's `/qr` is immune for a different reason: it only reads a file, so a stale check costs a 202 rather than a device link. Signal is the one gateway where `/qr` both changes state and checks a signal produced by the loop it suspends.

Separately, and not a blocker: `/qr` is a side-effecting GET driven by a page's own auto-refresh. Making it read-only, with "start re-pairing" behind an explicit button, would remove the class rather than this instance.

Two things I checked that hold. `/gateways` and the QR proxy are behind the same edge auth as the rest of the dashboard — the router rule in `docker-compose.override.example.yml` matches the whole host, so there is no unauthenticated path to a pairing credential — and the proxy adds the gateway token server-side instead of handing it to the page. And `classify_health` treating a gateway that answers without link state as up is the right default for a rolling upgrade; the alternative would alarm on every deploy.
