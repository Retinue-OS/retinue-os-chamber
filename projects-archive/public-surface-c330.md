# Surface register — archive part 16: cycle 330 (2026-07-31)

Rotated out of [`../projects/public-surface.md`](../projects/public-surface.md)
on 2026-08-01 (cycle 339), on the standing instruction c338 left: *the next
wake-up rotates first, whatever it writes.* The live file stood at **202 649
bytes on disk** against its own 200 KB (204 800 byte) trigger — it had already
crossed, without `rotation-check` reporting DUE at the previous cycle's
measurement, because c338 added 3 KB to the **handover field** rather than to the
write-ups.

Moving this one write-up (c330) keeps the register table plus the five most
recent sections (c331, c332, c333, c334, c336) where the rule says they belong.
It frees **3 015 characters** — which is the c314 finding restated by execution:
the rotation reaches the tail, and the tail is now 12% of the file. Live file
**201 102 → 198 086 characters**; reconstruction verified byte-identical before
the live copy was written.

---

## §c330 — the README link went live, and I checked the whole path rather than the grep (2026-07-31, 19:4x–20:1xZ)

**What was audited.** The end-to-end path a reader now takes from the framework README to
`writing/provenance-by-path.md`. The owner merged [#55](https://github.com/Retinue-OS/retinue/pull/55)
at **2026-07-31T19:33:40Z**, twelve minutes before this wake-up — the first PR merged in this org that
he did not open himself (§c328 measured that prior at n = 0), and the one that satisfies phase
objective 3.

**Why the obvious check is not enough.** Objective 3 has been re-measured for two days with
`grep -i provenance README.md`. That command passes the moment the line exists and says nothing about
whether the line *works*. Two ways it could have passed while the objective was still unsatisfied,
both live this cycle: the target could 404, and — because 45 of this chamber's commits are unpushed —
the target could resolve to a copy older than the one on disk here. Neither is visible from the
framework side at all.

| Check | Command | Result |
|---|---|---|
| Line present on `main` | `contents/README.md` @ `f1f8c72f` | `:42`, present |
| Survived later merges | #56 19:35:32Z, #57 19:44:08Z landed on top | still present |
| Target resolves | `curl -o /dev/null -w %{http_code}` | **200** |
| Target is the *current* text | `git rev-parse origin/main:writing/provenance-by-path.md` vs local | both `1fded9a9` — identical, so the push block does **not** touch this file |
| Links out of the piece | 8 GitHub URLs, followed | **8/8 → 200** |
| The claim the piece rests on | `qlever-dir#3` (watcher ignores converter extensions) | **still open** — so the reindex-latency caveat on `main` is not over-stated |
| Other two files of #55 | `docs/triple-stores.md:157` caveat, `signal-gateway/Dockerfile` | both restored |

**Result: clean, no defect.** Worth recording precisely because it is clean — the seven rows cost four
commands, and the register's job is to make the cheap check habitual before the expensive failure, not
after. The unpushed-commit row is the one that would not have occurred to me a week ago: **a link is a
join between two repos, and I can only push one of them.**

**Register rows added.** *Cross-repo link targets* — whenever a public surface in one repo starts
pointing at a file in another, check the target's served copy against the local one, not just its
status code; next due when any such link is added or the push block lifts. *Claims a published piece
depends on* — the walkthrough asserts a caveat whose truth is owned by `qlever-dir#3`; re-check on any
qlever-dir release.

**Not raised, deliberately.** The delivery blocker, though this is the cycle it bites hardest — the
five cards are 1 d 17 h stale on the served site and the fix is one permission. chamber#6 states it in
full, c318 verified it actionable, and he was active in the trackers for the whole hour before this
wake-up. Re-raising it tonight would be the c27 clock error committed on purpose.
