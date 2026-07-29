#!/bin/sh
# Install this chamber's pre-commit hook.
#
# Why this exists
# ---------------
# A blank line inside a Markdown table terminates it, and the rows after the
# blank arrive on the public page as a paragraph of pipe characters. It has
# happened three times in `projects/public-surface.md` (c200, c227, c244), and
# the third time was *after* `tools/render-check.py` existed to catch it: the
# instrument was never wrong, it was never run on the wake-up that appended the
# row. A check that depends on remembering to run it has the reliability of the
# memory, not of the check.
#
# Git hooks are not tracked content — `.git/hooks/` is neither cloned nor
# committed — so the hook itself cannot live in the repository. This script is
# the tracked half: it is what makes the hook reproducible after a fresh clone,
# and it is what a reader of this chamber can see.
#
# Run once per checkout:
#     sh tools/install-hook.sh
#
# What the hook does, and deliberately does not do
# ------------------------------------------------
# It runs `render-check.py --offline`, a pure text scan: no network, no `gh`, no
# GitHub API.
#
# It also runs `private-name-check.py`, added at c251 after the same failure in a
# worse place. That cycle wrote the org's private repository name onto two public
# forward surfaces and *pushed*, then ran the check that exists to catch exactly
# that — the c245 lesson (an instrument that depends on being remembered has the
# reliability of the memory) repeated against a guardrail-5 defect rather than a
# cosmetic one. Redaction after a push does not unpublish anything; only not
# committing it does.
#
# That check needs the API, because its whole design is to derive the names at
# run time and never store them. So it is wired fail-open on every outcome except
# a located hit: no network, no token, a failed self-test — all warn and allow.
# A hook that can strand a wake-up over an API outage costs more than it saves
# (strategy.md, "Wake-up duration"), and the wake-up survey still runs the check
# with the network as its second pass.
#
# It blocks a commit only on exit 1 — a located defect, named by file and line.
# On exit 2 (the detector failed its own self-test) or any other error it warns
# and lets the commit through. That asymmetry is on purpose: the hook exists to
# stop one cheap, known defect, not to become a gate that can strand a wake-up
# with uncommitted work (strategy.md, "Wake-up duration": anything uncommitted
# at ~600 s is at risk of being destroyed with the cycle).
set -eu

root=$(git rev-parse --show-toplevel)
hook="$root/.git/hooks/pre-commit"

cat > "$hook" <<'HOOK'
#!/bin/sh
# Installed by tools/install-hook.sh — see that file for the reasoning.
root=$(git rev-parse --show-toplevel)
out=$(python3 "$root/tools/render-check.py" --offline "$root" 2>&1) || status=$?
status=${status:-0}

if [ "$status" -eq 1 ]; then
    printf '%s\n' "$out" >&2
    cat >&2 <<'MSG'

pre-commit: a Markdown table is broken at the line named above.
A blank line inside a table ends it; the rows after it render as a paragraph
of pipe characters on the public page. Remove the blank line and commit again.
Override with --no-verify if this is genuinely not a table.
MSG
    exit 1
fi

if [ "$status" -ne 0 ]; then
    printf '%s\n' "$out" >&2
    echo "pre-commit: render-check could not run (exit $status); allowing the commit." >&2
fi

# Second check: no private repository name on a public forward surface.
# Needs the GitHub API by design (the names are derived, never stored), so every
# outcome but a located hit is fail-open.
pstatus=0
pout=$(python3 "$root/tools/private-name-check.py" 2>&1) || pstatus=$?

if [ "$pstatus" -eq 1 ]; then
    printf '%s\n' "$pout" >&2
    cat >&2 <<'MSG'

pre-commit: a public forward surface names one of the organisation's private
repositories. Guardrail 5 — a repo the owner keeps private is not public, and
this chamber is. Names are masked above; run
  python3 tools/private-name-check.py --show-names
to see which, then redact and commit again. Pushing first and redacting after
does not unpublish it.
MSG
    exit 1
fi

if [ "$pstatus" -ne 0 ]; then
    echo "pre-commit: private-name-check could not run (exit $pstatus); allowing the commit." >&2
fi
exit 0
HOOK

chmod +x "$hook"
echo "installed $hook"
