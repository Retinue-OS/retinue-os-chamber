#!/usr/bin/env python3
"""Check the five public dashboard cards against their per-field length budgets.

Why this exists (c256). The budgets were measured at c226 against what
`docs/components/*.js` actually renders — every card puts one item on one line
and none of them clip, so a paragraph in a one-line slot is a wall of text on a
phone. They were written into the `aros-dashboard-refresh` prompt at
2026-07-28 20:08Z as prose ("check each file against these numbers before
committing"), i.e. as an instruction whose only enforcement was the generating
agent re-reading its own output. That is the failure mode c235/c239/c252 each
recorded in a different venue: **a rule in prose does not propagate; only an
instrument does.**

Scope, stated because a check's scope is part of its claim. This reads the
**disk** copies by default. That is sound only because `tools/delivery-check.py`
runs every wake-up and proves the served copies are byte-identical to disk; if
that check is failing, this one's reading says nothing about the reader. Pass
`--served` to fetch from the Pages site and remove the dependency.

The budgets live **here and nowhere else**. The job prompt points at this file
rather than repeating the numbers, because two copies of a budget drift and the
drift is silent.

Self-test (c227): a synthetic card set with every budgeted field exactly at its
budget must report 0 problems, and the same set with every field one byte over
must report exactly one problem per budgeted field instance. The check refuses
to report on real data if either direction fails.

Usage:
    python3 tools/card-budget-check.py [--served] [--data-dir docs/data]

Exit status: 0 when every budgeted field is within budget, 1 otherwise, 2 when
the self-test fails.
"""

import argparse
import json
import os
import sys
import urllib.request

SERVED_BASE = "https://retinue-os.github.io/retinue-os-chamber/data/"

# field spec: (file, json path, budget)
#   json path is a list of steps; "[]" means "every element of this list".
BUDGETS = [
    ("briefing.json", ["text"], 900),
    ("todo.json", ["top", "title"], 160),
    ("todo.json", ["others", "[]", "title"], 110),
    ("messages.json", ["items", "[]", "preview"], 140),
    ("messages.json", ["items", "[]", "from"], 40),
    ("messages.json", ["items", "[]", "channel"], 40),
    ("agenda.json", ["events", "[]", "location"], 90),
    ("agenda.json", ["events", "[]", "title"], 70),
    ("projects.json", ["mine", "[]", "next"], 140),
    ("projects.json", ["waiting", "[]", "next"], 140),
]

CARDS = sorted({f for f, _, _ in BUDGETS})


def walk(doc, path):
    """Yield (label, value) for every string reachable by `path`."""
    def rec(node, steps, label):
        if node is None:
            return
        if not steps:
            if isinstance(node, str):
                yield label, node
            return
        step, rest = steps[0], steps[1:]
        if step == "[]":
            if isinstance(node, list):
                for i, item in enumerate(node):
                    yield from rec(item, rest, f"{label}[{i}]")
            return
        if isinstance(node, dict) and step in node:
            yield from rec(node[step], rest, label)

    yield from rec(doc, path, "")


def measure(docs):
    """Return (rows, problems). One row per field class, one problem per instance."""
    rows, problems = [], []
    for fname, path, budget in BUDGETS:
        doc = docs.get(fname)
        if doc is None:
            continue
        values = list(walk(doc, path))
        field = f"{fname[:-5]}.{'.'.join(path)}"
        if not values:
            rows.append((field, budget, 0, 0, 0, 0))
            continue
        lengths = [len(v) for _, v in values]
        over = [(label, n) for (label, _), n in zip(values, lengths) if n > budget]
        rows.append((field, budget, len(lengths), max(lengths),
                     sum(lengths) // len(lengths), len(over)))
        for label, n in over:
            problems.append((field, label, n, budget))
    return rows, problems


def synthetic(offset):
    """A card set with every budgeted field exactly `budget + offset` bytes."""
    def s(fname, path):
        for f, p, b in BUDGETS:
            if f == fname and p == path:
                return "x" * (b + offset)
        raise KeyError(path)

    return {
        "briefing.json": {"text": s("briefing.json", ["text"])},
        "todo.json": {
            "top": {"title": s("todo.json", ["top", "title"])},
            "others": [{"title": s("todo.json", ["others", "[]", "title"])}
                       for _ in range(3)],
        },
        "messages.json": {"items": [
            {"preview": s("messages.json", ["items", "[]", "preview"]),
             "from": s("messages.json", ["items", "[]", "from"]),
             "channel": s("messages.json", ["items", "[]", "channel"])}
            for _ in range(2)]},
        "agenda.json": {"events": [
            {"location": s("agenda.json", ["events", "[]", "location"]),
             "title": s("agenda.json", ["events", "[]", "title"])}
            for _ in range(2)]},
        "projects.json": {
            "mine": [{"next": s("projects.json", ["mine", "[]", "next"])}],
            "waiting": [{"next": s("projects.json", ["waiting", "[]", "next"])}],
        },
    }


def self_test():
    """Known-good and known-bad, per c227. Returns (ok, detail)."""
    _, good = measure(synthetic(0))
    if good:
        return False, f"at-budget fixture reported {len(good)} problems, expected 0"
    _, bad = measure(synthetic(1))
    # one instance per budgeted field, counted from the fixture's own shape
    expected = 1 + 1 + 3 + 2 * 3 + 2 * 2 + 1 + 1
    if len(bad) != expected:
        return False, f"one-over fixture reported {len(bad)} problems, expected {expected}"
    # an empty document must not be read as clean-by-absence
    rows, _ = measure({"briefing.json": {}})
    if any(r[0] == "briefing.text" and r[2] != 0 for r in rows):
        return False, "empty document mis-measured"
    return True, f"pass ({len(BUDGETS)} field classes, {expected} known-bad instances)"


def load(data_dir, served):
    docs = {}
    for name in CARDS:
        if served:
            with urllib.request.urlopen(SERVED_BASE + name, timeout=30) as r:
                docs[name] = json.loads(r.read().decode())
        else:
            with open(os.path.join(data_dir, name), encoding="utf-8") as fh:
                docs[name] = json.load(fh)
    return docs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "data"))
    ap.add_argument("--served", action="store_true",
                    help="fetch the served copies instead of reading disk")
    args = ap.parse_args()

    ok, detail = self_test()
    print(f"self-test: {detail}")
    if not ok:
        print("REFUSING TO REPORT — the check cannot verify itself", file=sys.stderr)
        return 2

    docs = load(args.data_dir, args.served)
    rows, problems = measure(docs)

    print(f"\n  {'field':34} {'budget':>6} {'n':>3} {'max':>6} {'mean':>6} {'over':>5}")
    for field, budget, n, mx, mean, over in rows:
        flag = "  <-- over" if over else ""
        print(f"  {field:34} {budget:6} {n:3} {mx:6} {mean:6} {over:5}{flag}")

    total = sum(r[2] for r in rows)
    src = "served" if args.served else "disk"
    if problems:
        print(f"\n{len(problems)} of {total} budgeted values over budget ({src})")
        worst = sorted(problems, key=lambda p: p[2] / p[3], reverse=True)[:3]
        for field, label, n, budget in worst:
            print(f"  worst: {field}{label} — {n} B against {budget} "
                  f"({n / budget:.1f}x)")
        return 1
    print(f"\n{total} budgeted values, 0 over budget ({src})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
