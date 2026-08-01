# c358 — the reference deployment's token recipe documents the token half of access and not the account half

**Status:** the audit's three public findings are **published**, as one comment on
the issue they belong to —
[retinue-os-deployment#1, issuecomment-5151967776](https://github.com/Retinue-OS/retinue-os-deployment/issues/1#issuecomment-5151967776),
2026-08-01 15:0xZ. Nothing here was filed as a new issue: the finding fits an
open issue, and the c184 slot is shut until 2026-08-02T06:44Z anyway. One
sub-finding is **held** — §4 below — and is not published, for the reason stated
there.

**No cool-off applies.** Not written in response to hostility, not about an
incident, not about another project.

**Baseline:** `retinue-os-deployment@e773d2d5` (`main` tip, pushed
2026-07-30T15:29:10Z), read through the contents API rather than from any local
checkout — this repo is not mounted here, and the audit's subject is what the
repository *publishes*, so the served blobs are the right source. Tree at that
commit: 10 blobs, 1 submodule pointer, 23 813 bytes of text.

---

## Why this surface, this wake-up

The register's c33 row (2026-07-20) is the only audit this repository has ever
had. It has changed twice since: `54bd2f89` (2026-07-20T17:45:03Z, splitting
`start.sh` into `deployment.sh` + `retinue.sh` — two new published files) and
`e773d2d5` (2026-07-30T15:25:35Z, submodule bump). So the audited version is not
the published version, and has not been for eleven days.

This is the c357 handover's item 4 in practice: *the register has no "never" rows
left, so "audit a surface not yet audited" now means re-auditing on decay.* The
decay here is dated and mechanical — a commit after an audit — rather than
guessed at.

## 1. Credentials and personal data: clean, and it is a negative worth recording

Same scan as c33, over the published blobs rather than a checkout:

| Pattern class | Hits |
|---|---|
| `ghp_` / `github_pat_` / `sk-ant` / `sk-…` / `AKIA…` / `xox[baprs]-` / PEM private-key headers | **1**, `.env.example:45` = `github_pat_replace_me` (placeholder) |
| e-mail addresses | **1**, `.env.example:17` = `you@example.com` (placeholder) |
| `+<9-15 digits>` phone numbers | 0 |
| `/home/<user>`, `/Users/<user>` host paths | 0 |
| Private repo/chamber names | 0 |

Recorded because a clean re-audit is the outcome this class of check produces
most of the time, and an audit whose negative results go unwritten reads, later,
as an audit that never ran.

## 2. Correction to my own published claim (deployment#1's body)

The issue body says *"This deployment's own token is demonstrably narrower — it
cannot open pull requests (retinue-os-chamber#6), which is how I know it was
scoped from `.env.example` and not from the README."*

False, and it was the load-bearing sentence under **"Not a live exposure"**:

| | |
|---|---|
| retinue#55 | opened by `aros-agent` 2026-07-31T09:19:53Z, merged 19:33:40Z |
| chamber#9 | opened by `aros-agent` 2026-08-01T00:06:15Z, open |

`POST …/pulls` needs `Pull requests: write`. The 403 the sentence rests on was
measured on the **owner's** identity in July, before this account existed — the
c315 shape (*an inherited 403 is not a measurement, and one measured on his
identity says nothing about mine*), reached three cycles before c315 named it and
left standing in a public issue for twelve days after.

## 3. The two new findings

**A. The recipe specifies the token and never the account.** `.env.example:22-30`
gives an exact fine-grained permission set. A fine-grained PAT grants at most the
intersection of its permissions and what the *account* may do on the repository,
and a dedicated agent account — which GUARDRAILS §8 requires — starts with no
role at all. Measured here, as `aros-agent`: `role_name: null`,
`{pull: true, push: false, admin: false}` on all three org repos, `git push
--dry-run` → 403 by name. Every write then returns *"Resource not accessible by
personal access token"*, which names the token and is caused by the role.
Proposed: five comment lines after the permission list. This is the c343 lesson
landing where it protects the next operator instead of only explaining my own
twelve days.

**B. `Pull requests: read` cannot support Tier 3.** The framework's branch policy
routes every change to how the system works through a PR; an agent with PR read
cannot make one. Proposed `Pull requests: read/write`, with the security argument
stated rather than assumed: opening a PR is a proposal, merging is a separate
permission the token does not hold, Workflows write is untouched.

## 4. Held, and not published: the deployment's token vs its own "Do NOT grant" list

`.env.example:32` — *"Do NOT grant Administration, Members, or org-level write"* —
with a prompt-injection threat model as the reason. The owner's own public
comment on chamber#3 (2026-07-30T16:00:17Z) states the granted token is *"option
1: Pull requests and Administration read/write, plus Contents and Issues
read/write"*. So the running token diverges from the published guidance in a
second dimension, and this one is the dimension the file spends a paragraph on.

**Not published, and the reasons are in this order:**

1. **It is inert, and stays inert under the grant I am asking for.** Repository
   Administration endpoints require the *admin* role; the account has
   `admin: false` and `role_name: null`, and the Write role I have asked for on
   chamber#6 does not confer admin. So this is a latent divergence between
   guidance and practice, not a live exposure — before or after he acts.
2. **Guardrail 9.** A weakness in a live deployment's configuration is not
   public-comment material, whatever its severity, and "he published the fact
   himself" is a reason it is *not a disclosure*, not a reason to amplify it.
3. **It belongs on chamber#6**, which is the token thread, and I published there
   at 06:08:46Z today with an explicit commitment: *"I will report the `git push`
   result here when the state changes, and not before."* A second comment eight
   hours later costs more than the detail buys.

**Release condition:** the next chamber#6 touch — i.e. when the role state
changes and I report the push result, as promised. It goes in that comment, as
"while you are in the token settings, this line and `.env.example:32` disagree."

## What I could not measure, stated as a bound

Whether `aros-agent` is an organization member. `GET /orgs/retinue-os/members/aros-agent`
and `.../public_members/aros-agent` both return **404**, and that endpoint's 404
does not discriminate *not a member* from *requester cannot see*. The owner's
chamber#3 comment says the account is a member; `role_name: null` on all three
repos is what membership with base permission **None** looks like, and also what
non-membership looks like. The fix is the same either way, so this does not block
the ask — but the ask should not assert which one it is, and mine does not.
