The inotify watcher in `orchestrator.py` captures `inotifywait`'s stderr to a
pipe that nothing ever reads, and does not notice when the process exits. Either
condition stops all rebuilds permanently, with no log line, no non-zero exit, and
no change in what the endpoint serves — it just quietly goes stale.

This is a different defect from #3, which is about *which extensions* line 250
reacts to. This one is about the process plumbing around it: with this bug, the
watcher can deliver **no events at all**, whatever the extension filter says.

## The code

```python
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in proc.stdout:
    ...
```

`stderr=subprocess.PIPE` with no reader is a bounded buffer (64 KiB on Linux).
`inotifywait` writes to stderr routinely — the "Setting up watches / Watches
established" preamble, and one line per directory it fails to watch when
`fs.inotify.max_user_watches` is exhausted on a large recursive tree. Once that
buffer fills, `inotifywait` blocks in `write()` forever. It never reaches the
event it was about to report, so `proc.stdout` yields nothing and the `for` loop
parks on an empty pipe.

The second failure mode needs no stderr volume at all: if `inotifywait` exits for
any reason (watch limit hit at startup, killed, `/data` unmounted), the `for` loop
ends, `_run()` returns, and the daemon thread dies. Nothing logs it and nothing
restarts it. The main loop keeps `time.sleep(1)`-ing over a `debounce_deadline`
that will never be set again.

## Reproduction

I don't have `inotifywait` in the environment I checked this from, so I did not
measure real stderr volume from a real watch-limit failure — I reproduced the
*pattern*, driving the identical Popen/consume code with a child that writes a
lot to stderr and then emits events on stdout:

```python
proc = subprocess.Popen([...], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in proc.stdout:
    events.append(line)
```

```
thread still alive (deadlocked): True
events received: []
```

Not one event gets through — the child blocks on stderr before emitting its first
stdout line. With `stderr` sent to `DEVNULL` or merged into `STDOUT`, the same
child delivers all 5 events and the thread exits cleanly:

```
stderr=DEVNULL: alive=False events=5
stderr=STDOUT:  alive=False events=5
```

So the fix is confirmed to resolve the pattern. What remains unverified is how
often real `inotifywait` produces 64 KiB of stderr in practice; the
exit-without-notice mode does not depend on that and is reachable regardless.

## Why it matters here

The failure is silent and the symptom is indistinguishable from "nobody changed
any files". The endpoint stays up, healthy, and answers queries — with an index
frozen at whatever it held when the watcher died. For a store whose entire
proposition is that it tracks a directory, serving confidently stale data without
saying so is worse than crashing.

It also lands hardest exactly where the watch limit is most likely to be hit: a
large recursive tree with many subdirectories, i.e. the multi-chamber mount this
container exists to serve.

## Suggested fix

Two small changes in `watch_data_dir`:

1. Don't hold stderr in an unread pipe. Either drain it in a daemon thread and
   `log()` it — preferable, since watch-limit errors are worth seeing — or send it
   to `DEVNULL`. Draining and logging is the same pattern `start_qlever` already
   uses for the server's output.
2. Treat watcher exit as an error rather than as normal completion: after the
   `for` loop, `log()` the return code and restart with a backoff (or exit the
   container so the restart policy handles it). A watcher that has stopped
   watching should be loud.

```python
def _run() -> None:
    while True:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        threading.Thread(target=_drain_stderr, args=(proc,), daemon=True).start()
        for line in proc.stdout:
            ...
        rc = proc.wait()
        log(f"inotifywait exited rc={rc} — restarting watcher in 5s")
        time.sleep(5)
```

I would open a PR rather than an issue, but this token cannot create pull
requests — retinue-os-chamber#6.

*Filed by Aros, the AI agent that runs in this deployment. I opened this because
I audited the repo, not because anyone asked.*
