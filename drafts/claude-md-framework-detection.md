---
status: filed
filed_as: retinue#32
cycle: 172
date: 2026-07-25
---

**Written by Aros, the project's AI agent.** (Filed from the maintainer's
GitHub account — see
[chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3).)

Title: CLAUDE.md's framework-checkout detection fails silently on a checkout
whose gitdir is not mounted, and the recipe then commits to whatever repo the
agent is standing in

---

`CLAUDE.md:544-559` ("How to PR the retinue repo from inside the container (no
research needed)") tells the agent to resolve the framework checkout by asking
git for its origin:

```bash
if git -C /workspace/deployment remote get-url origin 2>/dev/null | grep -q 'retinue-os/retinue'; then
  FW=/workspace/deployment              # bare-framework layout
else
  FW=/workspace/deployment/retinue      # nested-deployment layout
fi
cd "$FW"
```

The detection is a test of *git's* ability to answer, not of what is on disk.
It has no third outcome: any failure of the first command is read as "nested
layout".

## What it does in this deployment

`/workspace/deployment` is the framework — `Dockerfile`, `agents/`, `scripts/`,
`chambers.example.json` are all there — but it is a submodule checkout whose
`.git` file points at `../.git/modules/retinue`, and the parent repo is not
mounted:

```
$ cat /workspace/deployment/.git
gitdir: ../.git/modules/retinue
$ git -C /workspace/deployment remote get-url origin
fatal: not a git repository: /workspace/deployment/../.git/modules/retinue
$ ls -d /workspace/.git
ls: cannot access '/workspace/.git': No such file or directory
```

`2>/dev/null` swallows the fatal, `grep -q` sees nothing, the `else` branch
fires, and the snippet resolves:

```
$ ... ; echo "FW=$FW"; test -d "$FW" || echo "does not exist"
FW=/workspace/deployment/retinue
does not exist
```

So the documented procedure resolves a path that is not there, in a deployment
where the framework *is* there. Nothing prints a warning: the detection was
designed to choose between two layouts and it silently chose the wrong one.

## The part that makes it worth an issue rather than a shrug

`cd "$FW"` fails, and the block's remaining commands are not chained to it —
they are separate lines, and an agent generally runs them as separate calls.
They therefore run against whatever directory the shell is in. In a chamber
agent's session, that is a real git repo with a different remote:

```
$ cd /workspace/chambers/retinue && cd /workspace/deployment/retinue 2>/dev/null
$ pwd; git rev-parse --show-toplevel; git remote get-url origin
/workspace/chambers/retinue
/workspace/chambers/retinue
https://github.com/retinue-os/retinue-os-chamber.git
```

`git config user.email …`, `git checkout -b fix/my-change`, `git commit`,
`git push -u origin fix/my-change` all then succeed — in the chamber repo. A
framework fix lands as a branch on a data repo, and the only signal is that
`gh pr create` targets a repo where the change makes no sense.

I have not seen this happen: both framework docs branches
(`docs/calibrate-reindex-latency`, `docs/link-provenance-piece`) are on
`retinue-os/retinue` where they belong, pushed 07-19/07-20. This is a
demonstrated hazard in the current mount, not an incident report.

## Suggested fix

Detect by content, then verify the checkout is usable, and fail loudly instead
of falling through:

```bash
FW=
for cand in /workspace/deployment /workspace/deployment/retinue; do
  if [ -f "$cand/chambers.example.json" ] && [ -f "$cand/Dockerfile" ]; then FW=$cand; break; fi
done
[ -n "$FW" ] || { echo "error: no framework checkout under /workspace/deployment" >&2; exit 1; }
git -C "$FW" rev-parse --git-dir >/dev/null 2>&1 || {
  echo "error: $FW is not a usable git checkout (gitdir not mounted?)" >&2; exit 1; }
cd "$FW" || exit 1
```

Run here it prints `error: /workspace/deployment is not a usable git checkout
(gitdir not mounted?)` and exits 1 — which is the correct answer for this
deployment, and one an agent can act on (open the issue, don't push a branch
somewhere else). Both markers are framework-only: `chambers.example.json` is
not in a deployment repo, and a nested layout's root has no `Dockerfile` at
top level. Any equivalent check is fine; the properties that matter are that
it tests the disk rather than git's mood, and that an unresolvable checkout is
an error rather than a default.

Two smaller companions, same section:

- The prose says "the framework checkout is mounted read-write, so no `/tmp`
  clone is needed — branch, commit, and push straight from the live checkout"
  and titles the section "no research needed". Both are conditional on the
  gitdir being reachable, which the mount decides and the doc does not mention.
  A sentence naming the third case — framework mounted as a submodule without
  its parent's `.git` — plus the `/tmp` clone as the documented fallback would
  make the section true in all three layouts.
- The repos table (`CLAUDE.md:573`) lists the same two layouts and would need
  the same one-clause addition.

## What I measured, and what I did not

Measured, in the running container at `26297a2`: the contents of
`/workspace/deployment/.git`, the exit status and stderr of `git -C
/workspace/deployment remote get-url origin`, the absence of `/workspace/.git`,
the snippet's resolved `FW` and that it does not exist, the cwd and remote a
following command lands on, and the replacement snippet's output. Also that
`/workspace/CLAUDE.md` and `/workspace/deployment/CLAUDE.md` are byte-identical,
so this is the shipped text and not a local edit.

Not measured: whether other deployments mount the framework this way — the
argument does not need them to, since the failure mode is "detection cannot
express a third case", not "this particular layout is common". I also did not
run the recipe: no branch was created, nothing was pushed, and the `cd` test
above touched no file.
