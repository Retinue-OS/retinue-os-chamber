#!/usr/bin/env python3
"""Check that every baseline commit a held draft names is still reachable from `main`.

Why this exists
---------------
A held write-up in `drafts/` is a measurement with a date and a commit on it. The
c206 drain rule already says to re-verify one before filing, and cycles 224, 242,
246, 247 and 248 each did — by re-fetching the cited files and re-reading the
cited line numbers. Every one of those passes asked the same question: *did the
content move?*

None asked whether the **commit the write-up names** is still reachable. On
2026-07-29 at 12:45Z the maintainer replaced `retinue-os/retinue`'s `main` with a
line that has no common ancestor with the previous one. Nothing any held draft
cites changed by a single byte — and all three held baselines (`26297a2`) went
off the graph at once:

    $ gh api repos/Retinue-OS/retinue/compare/main...26297a2 --jq .status
    404: No common ancestor between main and 26297a2.

The object still resolves through the API, so every probe still re-runs and every
line number still holds. But an issue filed against that baseline names a commit
its reader cannot check out of a fresh clone, and no content check can see it.

**A baseline is a pointer, and a pointer can be invalidated with no file
changing.** That is `pointer-check.py`'s question asked about a commit instead of
a section, and it needs the network, so it lives in its own script.

What it checks
--------------
For every **held** draft (frontmatter `status: held`, or `**Held**` in the body —
filed and superseded drafts are skipped, since their baselines are history rather
than a claim someone is about to publish), every commit-ish it names in a
baseline context is resolved against the repository and classified:

* reachable from the default branch  -> fine
* resolves, but not reachable        -> off the current line (the c254 case)
* does not resolve at all            -> a typo, or a deleted fork

The **problem** reported is one per draft, not one per token: *this held draft
names no baseline a reader could check out.* A write-up accumulates re-verification
sections, each naming the commit it was measured at, and those older mentions stay
true as history — flagging them would make the check noisy in exactly the files
that are best maintained. What matters is whether at least one live commit is on
the page.

Usage
-----
    python3 tools/baseline-check.py [chamber-root] [--repo OWNER/NAME]

`--repo` sets the **fallback** repository for a bare SHA; it defaults to
`Retinue-OS/retinue`. A draft that names its repository inline — the
`repo@sha` form, e.g. `retinue-os-deployment@e773d2d5` or
`Retinue-OS/retinue@f1f8c72f`, with a bare name taken under the fallback's
owner — is resolved against **that** repository, per token.

*Corrected c375.* This paragraph used to say a draft targeting another repo is
"checked against the wrong one — stated plainly rather than guessed at". It was
not stated plainly anywhere a reader of the **output** would see: the report line
read *"names no commit a reader can check out"*, which is a claim about the draft,
while the thing measured was only that the SHA is absent from one repository the
draft never named. `drafts/c358-…` carried that false NO-BASELINE for four cycles;
its `e773d2d5` resolves `identical` against `retinue-os-deployment`. An error
message that names a cause is not a measurement of that cause — the c19/c343
shape, now found in this chamber's own instrument.

Exit status is 1 if any held draft names no reachable baseline at all.

Instrument discipline
---------------------
Per c227 a new instrument gets a known-good and a known-bad case before its first
result is believed. Two layers run on every invocation and the script refuses to
report on real files if either fails:

1. offline fixtures for the extractor and the held/filed classifier;
2. a **live** pair against the repository — the current tip of the default branch
   must come out `reachable`, and an all-zero SHA must come out `unknown`. An
   all-pass from a checker whose probe is broken looks exactly like a clean run.
"""

import json
import os
import re
import subprocess
import sys

DEFAULT_REPO = "Retinue-OS/retinue"

# A draft is live for this check while it is held; filed/superseded ones are
# history. `status: held` in frontmatter, or `**Held**` in prose (the older form).
HELD = re.compile(r"(?im)^status:\s*held\b|\*\*Held\*\*")
FILED = re.compile(r"(?im)^status:\s*(?:\*\*)?filed\b|^status:\s*\*\*FILED")

# Commit-ish tokens, taken only from lines that are talking about a baseline.
# The context test is what keeps conversation-thread ids and other hex-looking
# tokens out; `?ref=` is included because those lines are commands a reader runs.
CONTEXT = re.compile(
    r"(?i)baseline|verified_against|read_against|measured\s+(?:now\s+)?against|"
    r"re-verified[^\n]*against|\bmain\b[^\n]*@|@\s*`|[?&]ref="
)
SHA = re.compile(r"\b([0-9a-f]{7,40})\b")
# Tokens that are hex but never a commit here.
NOT_A_SHA = re.compile(r"(?i)thread|conversation|issue #|blob\b")
# `repo@sha` / `owner/repo@sha`, the form the drafts already use to say which
# repository a baseline belongs to. The name must sit directly against the `@`
# (so "`main` @ `26297a2`" does not read as a repo named `main`), and must carry
# at least one character no short SHA can (`-`, `_`, `.`, `/`, or a letter past
# `f`), so a sha-looking prefix is never mistaken for a repository.
QUALIFIED = re.compile(
    r"(?<![A-Za-z0-9_./-])((?:[A-Za-z0-9_.-]+/)?[A-Za-z0-9_.-]+)@`?([0-9a-f]{7,40})\b"
)
REPO_ISH = re.compile(r"[g-zG-Z_./-]")


def held_drafts(root):
    """Tracked files under drafts/ that are held rather than filed."""
    out = subprocess.run(
        ["git", "-C", root, "ls-files", "drafts/*.md"], capture_output=True, text=True
    )
    for path in [p for p in out.stdout.split("\n") if p]:
        try:
            text = open(os.path.join(root, path), encoding="utf-8").read()
        except OSError:
            continue
        if is_held(text):
            yield path, text


def is_held(text):
    """Held wins over filed only when no filed status is present."""
    if FILED.search(text):
        return False
    return bool(HELD.search(text))


def baselines(text):
    """Distinct commit-ish tokens named in a baseline context.

    Returns a list of `(repo_or_None, sha)`. `repo_or_None` is set only when the
    draft wrote the `repo@sha` form on that line; otherwise the caller's fallback
    repository applies. A SHA that appears both bare and qualified keeps the
    qualified reading — the draft said which repository it meant.
    """
    seen, qualified = [], {}
    for line in text.split("\n"):
        if not CONTEXT.search(line) or NOT_A_SHA.search(line):
            continue
        for name, sha in QUALIFIED.findall(line):
            if REPO_ISH.search(name):
                qualified.setdefault(sha, name)
        for sha in SHA.findall(line):
            if sha not in seen:
                seen.append(sha)
    return [(qualified.get(sha), sha) for sha in seen]


def gh_json(path):
    """GET one API path. Returns parsed JSON, or None on any failure."""
    out = subprocess.run(
        ["gh", "api", path], capture_output=True, text=True
    )
    if out.returncode != 0:
        return None
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return None


def classify(repo, sha, cache):
    """'reachable' | 'unreachable' | 'unknown' for one commit-ish.

    Cached on `(repo, sha)`, not `sha`: the same short SHA can exist in one
    repository and not another, and a sha-keyed cache would carry the first
    repository's verdict into the second.
    """
    if (repo, sha) in cache:
        return cache[(repo, sha)]
    verdict = "unknown"
    if gh_json(f"repos/{repo}/commits/{sha}"):
        cmp_ = gh_json(f"repos/{repo}/compare/HEAD...{sha}")
        # 'identical'/'behind' mean the tip contains it; 'ahead'/'diverged' and a
        # 404 (no common ancestor) mean it is off the current line.
        status = (cmp_ or {}).get("status")
        verdict = "reachable" if status in ("identical", "behind") else "unreachable"
    cache[(repo, sha)] = verdict
    return verdict


def qualify(name, fallback):
    """`retinue-os-deployment` -> `Retinue-OS/retinue-os-deployment`."""
    if name is None:
        return fallback
    return name if "/" in name else f"{fallback.split('/')[0]}/{name}"


HELD_FM = '---\nstatus: held — rank 1\n---\nMeasured against `main` @ `26297a2`.\n'
FILED_FM = '---\nstatus: filed 2026-07-27 as retinue#39\n---\nBaseline `26297a2`.\n'
HELD_PROSE = "Written c198. **Held**, not filed.\nBaseline recorded: `abc1234`.\n"
NOISE = "Escalated on dashboard thread e5f4f86f (c201).\nNo baseline here.\n"
CMD = "    gh api 'repos/x/y/contents/f.py?ref=deadbee' -q .content\n"
# A well-maintained write-up names its history *and* its current baseline; both
# must be extracted, and the aggregation is what decides.
LAYERED = (
    "Measured against `main` @ `26297a2` (c224).\n"
    "Re-baselined c254. New baseline: `50b5be890`, current `main`.\n"
)
# The c375 case: the draft names its repository inline, and it is not the default.
CROSS = "**Baseline:** `retinue-os-deployment@e773d2d5` (`main` tip, pushed\n"
CROSS_OWNED = "Baseline: `Retinue-OS/qlever-dir@abc1234`.\n"
# A sha-looking prefix must never be read as a repository name.
CROSS_NOISE = "Baseline `deadbee@abc1234`.\n"


def self_test():
    checks = [
        is_held(HELD_FM),
        is_held(HELD_PROSE),
        not is_held(FILED_FM),
        not is_held(NOISE),
        baselines(HELD_FM) == [(None, "26297a2")],
        baselines(HELD_PROSE) == [(None, "abc1234")],
        baselines(NOISE) == [],  # a thread id is not a baseline
        baselines(CMD) == [(None, "deadbee")],  # a ?ref= in a runnable command is
        # history and current, and `main` @ `sha` is not a repo qualifier
        baselines(LAYERED) == [(None, "26297a2"), (None, "50b5be890")],
        baselines(CROSS) == [("retinue-os-deployment", "e773d2d5")],
        baselines(CROSS_OWNED) == [("Retinue-OS/qlever-dir", "abc1234")],
        baselines(CROSS_NOISE) == [(None, "deadbee"), (None, "abc1234")],
        qualify(None, "Retinue-OS/retinue") == "Retinue-OS/retinue",
        qualify("retinue-os-deployment", "Retinue-OS/retinue")
        == "Retinue-OS/retinue-os-deployment",
        qualify("a/b", "Retinue-OS/retinue") == "a/b",
    ]
    return all(checks)


def live_test(repo, cache):
    """Known-good and known-bad against the real repository."""
    head = gh_json(f"repos/{repo}/commits/HEAD")
    if not head:
        return False, "cannot reach the repository"
    good = classify(repo, head["sha"], cache)
    bad = classify(repo, "0" * 40, cache)
    if good != "reachable":
        return False, f"tip of {repo} classified {good}, expected reachable"
    if bad != "unknown":
        return False, f"all-zero SHA classified {bad}, expected unknown"
    return True, head["sha"]


def main():
    args = [a for a in sys.argv[1:]]
    repo = DEFAULT_REPO
    if "--repo" in args:
        i = args.index("--repo")
        repo = args[i + 1]
        del args[i : i + 2]
    root = args[0] if args else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if not self_test():
        print("self-test FAILED — refusing to report on real files", file=sys.stderr)
        return 2
    cache = {}
    ok, detail = live_test(repo, cache)
    if not ok:
        print(f"live probe FAILED ({detail}) — refusing to report", file=sys.stderr)
        return 2
    print(f"self-test: pass (12 offline cases, live pair against {repo} @ {detail[:9]})")

    problems, drafts, probed = [], 0, 0
    for path, text in held_drafts(root):
        drafts += 1
        verdicts = {}
        for name, sha in baselines(text):
            probed += 1
            target = qualify(name, repo)
            verdicts[(target, sha)] = classify(target, sha, cache)
        live = {}
        for (target, sha), v in verdicts.items():
            if v == "reachable":
                live.setdefault(target, []).append(sha)
        if live:
            where = "; ".join(f"{', '.join(s)} on {t}" for t, s in live.items())
            print(f"  ok  {path}: {where}")
        else:
            detail = (
                ", ".join(f"{s} ({v}, {t})" for (t, s), v in verdicts.items())
                or "none named"
            )
            problems.append(
                f"NO-BASELINE  {path}: names no commit a reader can check out "
                f"— {detail}"
            )

    if not problems:
        print(f"{drafts} held draft(s), {probed} baseline reference(s), 0 problems.")
        return 0
    print()
    for line in problems:
        print(line)
    print(f"\n{drafts} held draft(s), {probed} baseline reference(s), {len(problems)} problem(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
