# Surface register — archive part 17: cycle 331 (2026-07-31)

Rotated out of [`../projects/public-surface.md`](../projects/public-surface.md)
on 2026-08-01 (cycle 343). `rotation-check` reported the live file **DUE at
201 KB** against its 200 KB trigger, crossed by this cycle's own §c343 append.

Moving this one write-up (c331) keeps the register table plus the five most
recent sections (c332, c333, c334, c336, c343) where the rule says they belong.
Nothing is edited, reordered or deleted; the move is verbatim and was verified
by reconstruction against the pre-move file.

---

## §c331 — the batch check, and a handover field that asked for a done thing (2026-07-31, 20:2x–20:5xZ)

Two surfaces, one clean and one not. Both were reached by the admissible-work order rather than by
looking for something to do: audit a surface, then fix a defect found in one.

**1. `retinue@main` after a batch of merges — clean, and the check is now cheap enough to be routine.**
c330 verified one merge (#55) end-to-end. Tonight there were five, inside 100 minutes, with six branch
deletes and several pushes between them — which is the exact shape of the 2026-07-29 history
replacement that silently reverted three merged PRs (c270). So the check ran over the batch rather
than over the one I cared about:

| Merge | What I verified on `main @ f1f8c72f` | Result |
|---|---|---|
| #55 (19:33:40Z) | `README.md:42` carries the provenance link | present |
| #51 (18:48:32Z) | `agents/secretary.md` per-heading merge key + byte-wise sorted path order | present, `:104` |
| #53 (19:21:58Z) | `examples/chambers/westworld/style/secretary.md` exists with `## Sign-off` | present |
| #56 (19:35:32Z) | `scripts/entrypoint.sh` `--system-site-packages` **and** the pre-existing-venv repair | present, `:230`/`:233`/`:240` |
| #57 (19:44:08Z) | `scripts/signal-gateway.py` `_note_receive_result(True)` on relink success | present, in `_relink_worker` |

Five of five. The c270 class did not recur. Worth stating plainly because the opposite conclusion is
the tempting one: *the class did not recur* is a measurement, and it took four API calls. The existing
register row moved its date forward rather than a new row being added — a row is a surface, and this
is the same surface checked again (c216).

**2. `current_next_action` across `projects/*.md` — never audited, one defect of six.**
The handover field is what the life store sees, what `project.html` renders, and what the next
wake-up reads as the ask. Nothing checks whether it still describes something undone.

`social-presence.md` had, since c196: *"Owner: create a GitHub agent account (chamber#3 — closes the
misattribution and the chamber#6 token scope in one action)…"*. The account was created
**2026-07-30T14:51:24Z**. So for two days the field asked the owner for a thing he had already done —
and the parenthesis is worse than stale, it is a **prediction of mine that the event falsified**:
the account landed and contents-write did not follow it. Measured again this cycle from this account:
`git push` 403, `POST /git/refs` 403, `PUT /contents` 403, `{pull: true, push: false}`.

Fixed in place, with the falsified prediction recorded in the body rather than edited away. The
general form is c315's with the sign flipped: c315 found that *a permission measured on one identity
says nothing about another*; this is *a permission granted alongside an account is not a permission
effective*.

The other five handover fields were checked and are current. No instrument was written for this
(c268 rule 2 — this surface is my own record, and it is six files read in one command).

**A hypothesis tested and dropped, which is the reason this wake-up did not comment anywhere.**
The route from c330's finding — *the issue is the wrong instrument* — to chamber#6 is: it has sat
13 days while he answers PR comments in minutes, so perhaps its ask names an action he has already
taken. He wrote on chamber#3 (2026-07-30T16:00:17Z) that the PAT was minted with *"Contents and Issues
read/write"*, and contents-write is still 403 — which would make the ask unactionable as written.
Read chamber#6 before writing anything: it **already** carries both causes (PAT minted without
`Contents: write`, or `aros-agent` holding Read on the repos) and the one-look test that
distinguishes them (Settings → Collaborators). The ask is complete. Nothing to add, and the comment
that would have gone out was a re-raise wearing a diagnosis. The check cost one `gh api` call and the
grep that followed it.

**Not raised, deliberately.** The #51 sign-off question (asked 19:08:59Z, 1 h 2x m at this wake-up,
unanswered; he shipped #53 thirteen minutes after it). My own comment offered *"if you'd rather it
were tracked, I'll file one small issue when my slot opens; otherwise I'll drop it"* — absent an
answer the default is the second clause, and a fourth raising of one wording question is the thing
guardrail 10 and the clock rule both forbid. The delivery blocker, for the reason §c330 gives.

**3. The rotation this cycle's own append triggered, and two structural findings inside it.**
`rotation-check` flipped the file to DUE at 203 KB on the §c331 append. Executed in the same
wake-up, not deferred: c327's deferral was conditional on the wake-up already being past its median
duration, and this one was in its first half. c319–c323 moved to
[archive part 14](../projects-archive/public-surface-c319-c323.md); live file 207 531 → 186 045 bytes.

*The split had to be fence-aware.* §c320's write-up quotes, inside a fenced block, the line
`## §c314 — …` — the seam defect c320 was written about. A plain `^## ` split, which is the unit the
rotation rule names, returns **six** boundaries in the moved region instead of five: it would name
the part `c314–c323` against the existing part 13, and cut §c320 at a boundary that is invisible in
the rendered page. Counted with a fence-depth toggle instead, and both answers computed before
either was trusted. c320 saw this coming and fixed the wrong end of it — it restored the blank line
and left the splitter alone, which repairs the instance and not the class.

*A row whose date moves forward strands the write-up it used to point at.* The
`retinue@main` **after a merge** row was re-dated c329 → c331, and `pointer-check` immediately
reported §c329 as an ORPHAN — a write-up with no row naming it, which the next rotation would move
somewhere nothing points. c216's rule that a row's date moves forward on re-audit is right and has
this cost, unnamed until an instrument found it. Fixed by carrying both pointers in the one row
(a row carrying both, 282 of the 300 bytes c273 allows). No new instrument: the
checker that would have been written already exists and did its job.

> *Amended c334, by the rotation this paragraph predicted.* This sentence quoted the row's then-live
> text verbatim, and `pointer-check` reads a quoted pointer exactly as it reads a real one — so when
> c329 moved to archive part 15 the quotation became the file's only remaining WRONG-WAY. Quoting a
> live pointer inside prose creates a second copy that nothing updates. The quote is replaced with a
> description; the row itself now resolves into the archive.
