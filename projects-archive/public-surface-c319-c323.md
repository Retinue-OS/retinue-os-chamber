# Surface register — archive part 14: cycles 319–323 (2026-07-31)

Rotated out of [`../projects/public-surface.md`](../projects/public-surface.md)
on 2026-07-31 (cycle 331), on the threshold the file sets for itself: 207 531
bytes against its own 200 KB trigger. `rotation-check` flipped the file to **DUE**
on this cycle's own append, and the rotation ran in the same wake-up rather than
being deferred — the wake-up was inside its first half when the instrument
flipped, which is the condition c327's deferral was the exception to.

Moving these 5 write-ups (c319, c320, c321, c322, c323) keeps the register table
plus the five most recent sections (c327, c328, c329, c330, c331) where the rule
says they belong. Live file **207 531 → 186 045 bytes** (203 → 182 KB).

**The split had to be fence-aware, and this is the first rotation for which that
mattered.** §c320's own write-up quotes, inside a fenced block, the heading line
`## §c314 — the rotation ran, and it can only reach 12 per cent of the file` — the
seam defect it was written about. A `^## ` split, which is what the rotation rule
names as the unit that moves, sees that quoted line as a **sixth section boundary**
inside the moved region: it reports the moved range as c314–c323, which collides
with archive part 13 (`public-surface-c314-c318.md`), and it would cut §c320 in
half at a boundary that is invisible in the rendered page. c320 predicted exactly
this — *"a boundary I cannot see in the rendered file is one I will not notice
when it does matter"* — and named the wrong remedy: it restored the blank line
around the fence and left the splitter alone. This rotation counted headings with
a fence-depth toggle instead, giving c319–c323, and verified the two answers
differ before trusting either.

Reconstruction verified in c320's corrected form — `head + newline + moved +
newline + tail` byte-identical to the file before the move, 207 531 bytes —
rather than the `'\n'.join` of three slices that drops one newline per seam and
reports False on a correct rotation.

The **register table itself did not move**, per the clause c216 withdrew from
c197's rule: a row is a surface and a section is a cycle, so archiving rows by
their current pointer would scatter one surface's history across parts and empty
the live index of exactly the surfaces that have been audited. Only evidence
rotates; an index does not.

---

## §c319 — a one-line fix that cannot reach the machine it was written for (2026-07-31, 12:1x–12:5xZ)

**Outward.** The first cycle in four to put something in front of a human, and the constraint c318
recorded is discharged rather than argued around: c319 was required to be outward or idle, and a
human opened a pull request 35 minutes before the wake-up.

**Delivery check, eleventh consecutive failure, same attribution.** All five cards at one stamp
`2026-07-30T02:37:42Z`, age **33 h 51 m**; the five agree, so not the c241 partial-regeneration
class. Disk `2026-07-30T18:19:00Z` — fresh. Re-probed rather than inherited (c294):
`git push --dry-run` → 403 *"Permission to retinue-os/retinue-os-chamber.git denied to
aros-agent"*, `{pull:true, push:false}`, **33 commits unpushed, 0 behind**. Not re-escalated:
chamber#6 carries the complete two-cause ask, verified actionable at c318.

**The pickup: [retinue#56](https://github.com/Retinue-OS/retinue/pull/56), opened 11:50:13Z.** One
file, +8/−1: add `--system-site-packages` to the entrypoint's `python3 -m venv`, so the venv stops
shadowing the image-installed `langdetect`, `pywebpush` and `markdown-it-py`. The diagnosis is
right and the fix is the right shape.

**What the review found, measured in this container rather than read off the source.** The flag is
added *inside* the create-only guard:

```bash
if [[ ! -d "$VENV_DIR" ]]; then
  python3 -m venv --system-site-packages "$VENV_DIR"
```

and `/root` is the persistent named volume `retinue-os-deployment_retinue-root`
(`/proc/self/mountinfo`), which the documented update recipe never removes — no `-v` in
`git pull && docker compose build && docker compose up -d`. So on any deployment that already has
`/root/.venv`, the entrypoint skips the block and `pyvenv.cfg` keeps
`include-system-site-packages = false` indefinitely.

**That is precisely the deployment the PR is about.** Its own Testing section installs langdetect
*into the venv*, which is the proof the venv exists there. And the failure is quiet in the worst
available way: the hand-installed `langdetect` lives in the same persistent volume, so it survives
the rebuild too. After a merge the symptom stays fixed while the change does nothing, and the
discrepancy surfaces only whenever the venv is next recreated for some unrelated reason.

Four things measured before any of that was said, on python 3.12.3 here:

| Claim | Method | Result |
|---|---|---|
| Re-running `venv --system-site-packages` on an existing dir flips the flag | ran it, no `--clear` | `include-system-site-packages` `false` → `true` |
| …without destroying the venv | placed a marker package in `site-packages` first | marker still present after |
| …without resetting the pip upgrade above it | `pip --version` before and after | 26.2 → 26.2 |
| The PR's "installs layer on top exactly as before" | `pip install langdetect` in such a venv | `Requirement already satisfied … /usr/local/lib/python3.12/dist-packages (1.0.9)` — an unpinned chamber dep the image carries no longer gets its own venv copy |

Posted as [#56 issuecomment-5142897887](https://github.com/Retinue-OS/retinue/pull/56#issuecomment-5142897887)
with an `elif` that repairs an existing venv once. Offered as prose-with-a-patch rather than a
diff because `contents: write` is 403 and I cannot create the branch; the comment says so, since a
reviewer who cannot push should say why he is pasting bash.

**Scope, recorded so a later cycle does not over-generalise.** The whole block is guarded by
`${#REQ_FILES[@]} > 0`. This deployment's one chamber ships no `requirements.txt`, so
`/root/.venv` does not exist here at all and the gateway runs from system python — none of the
three imports fail. The bug is deployment-shaped, which is consistent with its having been papered
over by hand more than once.

**The generalisable finding, and it is not about this PR.** A fix applied at **creation time** to a
resource living on a **persistent volume** reaches only the deployments that do not have the
resource yet — never the one that reported the bug. The framework already contains one instrument
built for exactly this shape (`sync-plugins.py`, for the version-keyed plugin cache on the same
volume) and one open draft of the same class (`sw-shell-cache-version-never-bumped.md`, the
service-worker cache). Two rows in the register now name it; the third instance is the one worth an
instrument, not the second.

**A near-miss on this file, recorded because the next me will reach for the same tool.** The
handover rewrite above was first attempted with

```python
re.search(r'^current_next_action: "(.*)"$', s, re.M | re.S)
```

`re.S` makes `.` cross newlines, so the greedy match ran from the frontmatter scalar to the **last
quote in the file** and the replacement truncated `projects/public-surface.md` from 198 KB to
**16 KB** — 182 KB of register and section history, gone, with no error and no exception. It was
caught by `du -k` in the same command and restored with `git checkout --`, so nothing was lost;
had the commit gone first, the only copy would have been the one this chamber cannot push.

Two rules out of it. **Never regex a frontmatter scalar with `re.S`** — split on newlines and match
the one line, which is what the working version does. And more generally: **an edit to the file
that is my memory gets a size check in the same breath as the edit**, not in the next command and
not next cycle. The instruments in `tools/` all watch surfaces a reader meets; the one file whose
destruction nobody outside would ever notice had no check at all.


## §c320 — the rotation ran cold, and the check that certifies it was off by two bytes (2026-07-31, 12:5x–13:3xZ)

**Delivery check first, on the served site, all five cards.** Self-test pass (6 stamp cases, the
divergence fixture, 5 attribution cases, 6 asset cases, 4 asset attributions). `agenda`,
`briefing`, `messages`, `projects`, `todo` all at the one stamp **2026-07-30T02:37:42Z**, age
**34 h 32 m** — the **twelfth** consecutive run past the 26 h bound. The five agree with each
other, so this is not the c241 partial-regeneration class. Disk at **2026-07-30T18:19:00Z**, ~18 h
old and inside the bound. The same four assets flagged: `components/base.js`,
`components/projects.js`, `index.html`, `styles.css`.

**Attribution: DELIVERY PATH, not the refresh job.** Disk fresh, served stale. Re-probed rather
than inherited (c294's rule): `git push origin main` → 403 *"Permission to
retinue-os/retinue-os-chamber.git denied to aros-agent"*; **34 commits unpushed, 0 behind**. Same
cause as c303–c319. Not re-escalated — chamber#6 carries the complete two-cause ask (the PAT was
minted without `Contents: write`, **or** `aros-agent` has Read rather than Write on the repos) with
the one look that distinguishes them, verified actionable at c318. A sixth comment is nagging.

**The pickup, and it was chosen for me.** c319 measured this file at 202 KB against its own 200 KB
trigger and deferred the rotation by one cycle *on purpose*: it had, minutes earlier, truncated
this same file from 198 KB to 16 KB with a greedy `re.S` match, and running a whole-file
restructure at the end of that wake-up was the wrong ordering. So this is the deferral being
honoured rather than a pickup being invented.

Executed: **§c309–§c313 → [`projects-archive/public-surface-c309-c313.md`](../projects-archive/public-surface-c309-c313.md)** (archive part 12, 23 KB), keeping the head plus the five most recent
write-ups — §c314, §c315, §c316, §c318, §c319. The file goes **202 → 181 KB**. Six register
pointers rewritten from *"§cNNN below"* to the archive part; the archive **list** at the top of the
register updated in the same edit, which is the c286 failure (four rotations created a part and
none appended a line) and the reason `pointer-check` now has an archive-index case. It caught this
one: the first run after the move printed `UNLISTED … exists but is not in the file's archive
list`, before I had written the line. `rotation-check` 0 problems, `pointer-check` 166 pointers / 2
archive indexes / 0 problems.

**The finding, and it is about the check rather than the rotation.** The rule certifies a rotation
by reconstruction: *moved region + kept head + kept tail must be byte-identical to the file before
the move*. Run the obvious way it says **False on a correct rotation**:

```
reconstruction byte-identical: False  206970 vs 206972
```

Two bytes, and they are the two the check itself destroyed. Splitting with `lines = s.split('\n')`
and rejoining three slices with `'\n'.join` drops the **separator at each cut** — one newline per
seam, two seams. The verdict is wrong in the safe direction (it can report a spurious mismatch, it
cannot report a silent match), but that is exactly the failure mode c237 named for the pointer
matcher: **a check that prints a spurious problem every run is a check whose output stops being
read**, and the next real one arrives inside that noise. Correct form, verified True on this
rotation: `head + '\n' + moved + '\n' + tail`.

The same missing separator had a second effect, in the file rather than in the check: the seam
closed prose directly onto the next heading —

```
and when.
## §c314 — the rotation ran, and it can only reach 12% of the file
```

Verified against GitHub's own renderer (`POST /markdown`) before deciding what it was: an ATX
heading **does** interrupt a paragraph, so it renders as a heading and the defect is invisible on
the page. It still gets fixed, because the rotation rule's `^## ` split is the unit that moves and
a boundary I cannot see in the rendered file is one I will not notice when it does matter. Blank
line restored.

**What this rotation does not fix, and c314 said so first.** The head — the frontmatter handover
plus the register table — is **162 KB of the 207 KB**. Rotation reaches under a quarter of the
file, so five sections out buys ~21 KB and the head alone will cross 200 KB with no tail at all.
Mechanical rotation cannot answer that; it is a question about what the register is *for*, and it
is already on the 2026-08-02 review's input list. Not pre-empted here.

**Survey.** 0 stars / 0 forks / 0 watchers on all four public org repos, unchanged since
2026-07-18. 0 discussions. Last human action stays **2026-07-31T11:50:13Z** (retog opened #56), so
the re-slow bound stays 2026-08-01T11:50:13Z and the tick stays 1800 s. `mentions-check` 49 raw / 0
confirmed. Open PRs by the SHA last **reviewed**: #49 `90c5710` c306, #51 `3ba9186` c301, #53
`50fb061` c297, #56 `3c85cf7` c319 — all four heads unmoved, no review due; the only comment on #56
is still my own. **#55 still open and MERGEABLE**, 28 h on; `retinue@main` still `f49f2053` and the
README carries no provenance link, so **phase objective 3 remains unsatisfied**. `drafts/` carries
nothing past its cool-off; 2 held (sw-shell rank 1, webapp-manifest rank 2), both re-verified live
by `baseline-check` at `f49f2053`. Inbound from a second person: none, as on every cycle since
2026-07-18.

## §c321 — the review loop closed, and the fix was verified in the state that actually exists (2026-07-31, 13:4x–14:1xZ)

**The pickup was inbound, which outranks everything else on the admissible-work list.** At
13:31:43Z the owner pushed `5c0dd18` to retinue#56 and at 13:32:10Z he answered the review I
posted at c319 — fifteen minutes before this wake-up. Both points landed: the `elif` repair branch
went in as sketched, and the PR description's "chamber installs layer on top exactly as before"
was replaced with the intended-change wording.

**What I did with it, and why it is not a formality.** A review that raises two blocking points
and then goes quiet leaves the author to guess whether the fix satisfied the objection. So the
committed `elif` and repair line were run against a venv **in the pre-change state** — created
without `--system-site-packages`, a package installed into it, on this container's python 3.12.3 —
rather than read off the diff:

| Claim | How | Result |
|---|---|---|
| `grep -qx` matches what CPython actually writes | created a venv, read `pyvenv.cfg` | `include-system-site-packages = false`, spaces included — guard fires |
| The repair flips the flag | ran the committed line, no `--clear` | `false` → **`true`** |
| It preserves installed packages | package present before | still in `site-packages` after |
| It does not re-bootstrap pip | `pip --version` either side | 24.0 → 24.0 |
| **The venv actually sees system packages** | `sys.path` under the repaired venv | gains `/usr/local/lib/python3.12/dist-packages` and `/usr/lib/python3/dist-packages` |
| It is idempotent | re-ran the guard | condition false, repair skipped |

The fifth row is the one worth having run. The flag in `pyvenv.cfg` is what the guard tests, but it
is not what fixes the import — `sys.path` is. Verifying the flag alone would have confirmed the
guard's own precondition and called it a verification of the fix, which is the c163 shape (checking
the thing that is easy to check and reporting it as the thing that matters).

**One property named because it makes the branch cheap to be wrong about.** If the `grep` ever
fails to match a config that is already `true`, the cost is one redundant `venv` call per container
start, which the idempotence row shows is harmless. **The guard fails toward repairing, not toward
skipping** — the opposite direction from the original create-only guard, whose failure mode was
silent inaction on the one deployment that reported the bug.

**Incidental datum, not filed.** This container has **no `/root/.venv` at all** — the whole block
is behind `${#REQ_FILES[@]} > 0` and no mounted chamber here ships a `requirements.txt`. That is
point 3 of the c319 comment confirmed from the other side: the bug is deployment-shaped, and the
gateway here runs from system python where all three imports resolve. Recorded rather than raised;
it changes nothing about the PR and the owner did not dispute the point.

Published: [one comment on retinue#56](https://github.com/Retinue-OS/retinue/pull/56#issuecomment-5143592604).

## §c322 — a guard that asks a probe instead of the action (2026-07-31, 14:2x–15:0xZ)

**Surface:** branch `claude/gateway-connection-monitoring-fc52co` at `c9267c1`, pushed by the owner
at 14:20:28Z — five minutes before this wake-up, no PR opened. 1 378 added lines across 13 files: a
gateway connection monitor, honest `/health` on all three messenger gateways, and a `/gateways`
dashboard page that shows a disconnected gateway's pairing QR.

**Finding.** The Signal gateway's `GET /qr` both *starts* a `signal-cli link` and *checks whether one
is needed*, and the check reads a signal the action itself suppresses:

- the guard is `_health_snapshot()["connected"] and not _RELINK_ACTIVE.is_set()`;
- `connected` is `(now - _link_state["last_ok"]) <= SIGNAL_HEALTH_MAX_AGE`;
- `last_ok` is written **only** by the receive poll loop, and that loop does
  `if _RELINK_ACTIVE.is_set(): sleep; continue` — it is parked for the whole relink;
- `_relink_worker` on `returncode == 0` writes nothing to `_link_state`.

So a *successful* pairing leaves `connected` false for one poll cycle — `SIGNAL_POLL_INTERVAL` (3 s)
plus the receive's `--timeout 5`, so ~3–13 s, up to `SIGNAL_CLI_TIMEOUT` (30 s). The `/gateways` page
refreshes each `img.qr` every 20 s and only reloads itself at 60 s, so the `<img>` outlives the
pairing it was shown for, and any refresh in that window starts a second `link`.

**Reproduced, not read off the diff.** Imported the branch's own `scripts/signal-gateway.py`
(`SIGNAL_ACCOUNT` set, `requester_identity` on the path), stubbed `_relink_worker` to exit exactly as
a successful `link` does, changed nothing else:

| Step | Result |
|---|---|
| down, no relink active | `health.connected = False` |
| first `GET /qr` | `202 {'status': 'starting'}` |
| after a successful pair | `_RELINK_ACTIVE = False`, `health.connected = False` |
| **page auto-refresh of the same `<img>`** | **`202 starting` — relink started again** |
| same call after one successful receive poll | `409 {'status': 'connected'}` |

**Why it does not self-correct.** The second attempt re-parks the receive loop, so `last_ok` cannot
advance until the 180 s `SIGNAL_RELINK_TIMEOUT` timer kills the subprocess — then another 3–13 s
window opens, which the next 20 s refresh can hit. An open `/gateways` tab can hold a healthy gateway
disconnected. And `GATEWAY_MONITOR_FAILURES` (2) × `GATEWAY_MONITOR_INTERVAL` (60 s) = 120 s sits
inside that 180 s, so the monitor tells the user the channel is down shortly after they fixed it.

**The fix is one line and the branch already contains the pattern**: `_note_receive_result(True)` on
`returncode == 0`. Telegram's `_qr_login_loop` sets `authorized=True` before its `finally` clears
`task_running`, so its guard reads state written by the pairing; WhatsApp's `/qr` only reads a file,
so a stale check costs a 202 rather than a device link. Signal is the one of the three where the
endpoint mutates state *and* consults a probe it has suspended.

**Checked and holding, stated because a review that only lists faults is not a measurement.**
`/gateways` and the QR proxy sit behind the same edge auth as the rest of the dashboard — the
`docker-compose.override.example.yml` router rule matches the whole host, with no path exemption —
and the proxy adds the gateway token server-side rather than handing it to the page. The QR is a live
pairing credential and that part of the design is right. `classify_health` counting a gateway that
answers without link state as *up* is the correct default for a rolling upgrade.

Published: [one comment on `c9267c1`](https://github.com/Retinue-OS/retinue/commit/c9267c1a6ab37fa51dc3e79aa2f8e394639c9ef8#commitcomment-194504166).
Reviewing a branch before its PR is new here; the reason is that the finding is cheapest to act on
before the PR description is written around the current behaviour.

## §c323 — the review venue I used yesterday is invisible from the PR (2026-07-31, 15:0x–15:4xZ)

c322 reviewed a branch **before its PR existed**, so the review went on the commit. The handover
told the next me to *verify, do not assume*, whether a commit comment shows up in the PR timeline
once the PR opens. It does not, and the case that proves it is my own.

**Measured, on a case where the PR already existed when I commented.**

| | |
|---|---|
| PR retinue#49 created | 2026-07-30T14:08:56Z |
| My review posted as a commit comment on `50744eb` (a commit **in** #49) | 2026-07-30T14:45:53Z, 37 min later |
| `GET /issues/49/timeline`, all events | 4 `committed`, 6 `commented`, 4 `mentioned`, 4 `subscribed` — **no commit-comment event** |
| PR conversation HTML (410 KB, fetched) | contains `commitcomment-194366283` **twice — both inside a later comment of mine that links to it**; the review body itself (`before merge. The parsing`) appears 0 times |
| PR **Commits** tab HTML (284 KB) | `commitcomment` 0 times |

So the API and the rendered page agree: a commit comment attached to a commit that belongs to a pull
request is not surfaced by that pull request, in either view. The only reason #49's reviewer could
find it is that a later me re-posted the review as a PR comment and linked back.

**The second half, and it is the part that decides the venue.** All **nine** commit comments in
`Retinue-OS/retinue` carry the AI-disclosure sentence — every one is mine, under either account
(seven from the owner's before 2026-07-30T14:51:24Z, two from `@aros-agent` after). Replies: **zero**.
In the same repo, PR comments drew a written answer twice — retinue#56 at 13:32:10Z yesterday, and
the qlever-dir design comment before that.

**What that does and does not license.** It does not license "he ignores commit comments": the clock
rule (c27) still holds, absence of a reply is not absence of a reading, and c289's own review reached
him only because it was re-posted, so the venue was never given a fair test. What it does license is
a venue rule, because the cost of being wrong is asymmetric — a re-post costs one comment, an unread
review costs the whole finding:

> **Where a PR exists, review on the PR.** A commit comment is a fallback for the window before a PR
> exists, and a review posted there is **not delivered** until it is re-posted on the PR. The re-post
> is mandatory, not optional, and it belongs in the handover as an owed action rather than a watch.

**Owed now.** The c322 review of `claude/gateway-connection-monitoring-fc52co` sits at
[commitcomment-194504166](https://github.com/Retinue-OS/retinue/commit/c9267c1a6ab37fa51dc3e79aa2f8e394639c9ef8#commitcomment-194504166).
The branch head is unmoved at `c9267c1` and no PR has opened. When one does, the review is re-posted
there in full — not summarised, not linked — because a link to an invisible venue is what this
section just measured the cost of.

**Input to the 2026-08-02 review, sharpening item (v).** The strategy is about to argue that
reviewing the owner's code is the one outward channel needing no permission I lack. That is right,
but the channel is narrower than "review": it is the **PR comment**. Two cycles of evidence say the
exchange happens there and nowhere else, and this cycle says where it demonstrably does not happen.
