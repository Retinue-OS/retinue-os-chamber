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
# It runs `render-check.py --offline`, which is a pure text scan: no network, no
# `gh`, no GitHub API. The network half of the check stays in the wake-up survey
# where an outage can only delay a report.
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
exit 0
HOOK

chmod +x "$hook"
echo "installed $hook"
