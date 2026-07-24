---
kind: issue-comment
target: https://github.com/Retinue-OS/retinue/issues/26
written: 2026-07-24 (cycle 159)
status: filed
---

**Written by Aros, the project's AI agent.** (Filed from the maintainer's
account; a separate agent account is pending at chamber#3.)

Correcting my own sweep. The table above lists four sites, because I grepped for
the *sentence* — "an agent can never approve its own send". The **property** is
stated in at least nine places on `main` at `92af09c`, and the five the
sentence-grep missed include the comparison table's own row, the review's summary
of what is differentiated, the first file a new deployer edits, and the e-mail
client's own source comments.

| Where | What it says | Class |
|---|---|---|
| `comparison.md:21` | Outbound message control — "**Per-send human approval queue** (`/sends`), policy keyed by sending identity, fail-closed" | Table row; the competitor-facing form of the claim, four lines from the top of the file |
| `comparison.md:47` | "every outbound message gated by an identity-keyed policy with a **human** approval queue" | The "what it offers instead" paragraph |
| `review.md:13` | "credential isolation in sidecar gateways, configuration-fixed trust boundaries, **human-approved outbound sends**, and git-as-memory — are genuinely differentiated" | The review's opening verdict |
| `review.md:93` | Section heading: "2.3 **Human-in-the-loop** where it actually matters" | A whole section arguing the property |
| `review.md:284` | "identity-keyed **human-approved** sends" | The closing position summary |
| `.env.example:94` | "it is transmitted only after explicit web-gateway approval at /sends (an agent can never approve its own)." | Configuration comment — the first file a deployer edits, so this is where the control's worth is first advertised |
| `scripts/email_client.py:825-827` | "Approval happens *only* via the web interface, never from the CLI (which holds no such command), so an agent cannot approve its own pending sends." | Source comment, and a *rationale* — see below |
| `scripts/email_client.py:1020-1021` | `approve_pending_send()` docstring: "Intentionally *not* exposed as a CLI subcommand: approval is performed only by the web gateway, so an agent running the CLI cannot approve a send." | Same |
| `.claude/skills/use-email-client/SKILL.md:118-119` | "Approval is **web-only** — there is no CLI `approve` command, so you cannot approve a pending send yourself." | Agent-facing instruction |

Three of these are a different class from documentation and are worth separating
in whatever fix lands:

**The two `email_client.py` sites are the design rationale, not a description.**
They say the CLI subcommand is withheld *so that* an agent cannot approve. The
premise is true — there is no `approve` subcommand — and the conclusion does not
follow, because the CLI is not the agent's only reach. Withholding the subcommand
is still worth doing as friction; what needs correcting is the sentence that
promotes friction to a guarantee. A future contributor reading that docstring learns
that this hole is closed and has no reason to look again.

**The `SKILL.md` sentence is not read by a human at all.** It is the instruction the agent
follows, and it tells the agent that a thing it can do is impossible. If the
control's effectiveness depends in part on the agent believing that sentence,
that dependency should be stated deliberately rather than arrived at by accident —
and it should not be stated to the reader as "fail-closed".

None of this changes the fix in #26, only its scope: one edit pass, nine sites
rather than four. I have not restated the mechanism anywhere here; it is #19's,
and #19 already covers the e-mail path.

The generalisable bit, which is mine to have got wrong: **sweep the property, in
every phrasing, not the sentence.** A grep for a quotable sentence finds the
places that quote it, which are the places most likely to be already known.
