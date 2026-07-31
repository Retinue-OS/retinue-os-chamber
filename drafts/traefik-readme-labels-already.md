# Draft issue — `deploy/traefik/README.md`: "the labels already reference …" is false on a fresh clone

status: filed (retinue#54, 2026-07-31T06:26:15Z, from @aros-agent; label dropped — 403)

Written 2026-07-26 (c198). **FILED 2026-07-31T06:26:15Z as
[retinue#54](https://github.com/Retinue-OS/retinue/issues/54)** (c311), from `@aros-agent`
— the first issue in this project's history filed from my own account. Baseline
`f49f2053` re-checked immediately before filing; the security instance c303 found stays
excluded and unnamed. **The label did not land:** `gh issue create --label documentation`
returned exit 0 with `labels: []`, and `POST …/issues/54/labels` is 403; the issue's
closing line now says so, added by editing my own issue. No longer held, no longer ranked.

*(Historical status, kept for the record: Written 2026-07-26 (c198). **Held**, not filed:
the c184 rate limit allows one new issue per 24 h. **Rank 1 of 3**; the next slot opens
**2026-07-31T06:08:5xZ** and this file holds it.)* *(Re-verified and re-baselined to `f49f2053` at c303 — see that
section; still rank 1, still safe to file.)* *(Held at rank 1 by c282, which added
`sw-shell-cache-version-never-bumped.md` at rank 2 — a live behaviour defect, which
would normally outrank a docs inaccuracy, but it has been delivered to the owner
twice already (a commit comment and a dashboard message) and this file has been
delivered nowhere. The ranking question is what he has not yet read.)* *(Re-ranked c278: was rank 2 of 3;
`updater-reports-dispatch-not-result.md` was filed as retinue#46 on 2026-07-30 and no
longer competes. Re-ranked c243: was rank 3 of
4; `w3id-namespace-unregistered.md` was filed as chamber#8 on 2026-07-29 and no
longer competes.)* **Re-verified c248 (2026-07-29 09:5xZ) against `26297a2`, re-baselined c254 to `50b5be890` (the old commit is no longer on `main`; content identical): every
claim in the body holds verbatim, and the *operator check* the body publishes was
wrong — it expects three lines where a correctly wired deployment prints four, and
its threshold passes one specific broken configuration. Corrected below; safe to
file as it now stands.** *(Re-ranked c232: this file previously
read "ranked second, behind `ingest-sensors-unreachable-chamber-root.md`", which was
filed as retinue#40 on 2026-07-28 and no longer competes for a slot.)* Below
`updater-reports-dispatch-not-result.md` on the standing preference for silent
failures: a reader following this README hits a visible failure — the labels are not
there — while the updater's caller cannot tell success from failure at all.

Target repo: `retinue-os/retinue`. Label: `documentation`.

**Re-verified 2026-07-28 18:5xZ (c224), and the re-verification was owed for a
reason the write-up itself created: it recorded no baseline commit.** Three cycles
have reported the drain queue as "empty because `main` is unmoved at `26297a2`".
That inference needs each held write-up's own baseline, and this one named none —
so the claim covered it by assumption rather than by measurement. Same shape as
c179 and c221: a proxy is a claim.

Measured against `retinue-os/retinue @ 26297a2` (2026-07-25T15:12:01Z, still
`main`), fetched from the GitHub API rather than from the local checkout, whose
gitdir is unmounted (retinue#32):

| Probe | Result |
|---|---|
| `deploy/traefik/README.md:49` — "the `retinue` service's labels already reference" | present, unchanged |
| `labels:` keys anywhere in `docker-compose.yml` | **0** |
| `retinue-mtls@file` in `docker-compose.yml` | **0** |
| `agents-clientcert` / `agents-auth` in `docker-compose.override.example.yml` | ~~lines 45–60~~ **the two names appear at 45–53; the retinue service's `labels:` block is 39–60** (corrected c248), as an example |

**Reproduces in full. Baseline recorded: `26297a2`.**

## Re-verification, cycle 248 (2026-07-29 09:5x–10:0xZ)

c246 set the standard that a held write-up's evidence is **executed**, not
re-read, and c247 added that a corrected number has to be carried into the prose
a reader meets first. This pass applied both. `main` is still `26297a2`
(2026-07-25T15:12:01Z), so the baseline is unmoved and the c224 probes stand.

Every claim in the body below, fetched from the GitHub API at that commit and
opened line by line:

| Claim in the body | Verified at |
|---|---|
| The quoted closing paragraph | `deploy/traefik/README.md:49–51`, verbatim |
| `retinue` service declares no `labels:` key | `docker-compose.yml`: **0** occurrences of `labels:` anywhere in the file; 0 of `retinue-mtls@file` |
| "the comment immediately above its `networks:` block says the opposite" | comment at `docker-compose.yml:136–139`, `networks:` at **140** — immediately above, verbatim |
| The example's header says "copy to docker-compose.override.yml" | `docker-compose.override.example.yml:1`, and line 7 states it is git-ignored |
| …and that target is git-ignored | `.gitignore:6` |
| Labels live only in the example, lines 40–60 | `labels:` at 39, the ten label entries at **40–60** |
| `VerifyClientCertIfGiven`, so the browser is still served | `deploy/traefik/dynamic/retinue-mtls.yml:21` |
| No cert header → `decide()` falls to the basic-auth branch | `scripts/gateway_auth.py:172` (`decide`), cert branch 193–200, basic-auth fallback 202–206, `401` at 206 |
| The README's own CA-collision warning | `deploy/traefik/README.md:68–74`, verbatim |

**The defect this pass found is in my own suggested check, not in the project.**
The body closed with a `docker inspect … | grep -E
'passtlsclientcert|forwardauth|tls.options'` and the sentence *"Three lines of
output means the certificate half is wired; fewer means it is not."* Executed
against the example's own labels rather than counted by eye:

```bash
python3 - <<'PY'
import re
src = open('docker-compose.override.example.yml').read().splitlines()
start = next(i for i, l in enumerate(src) if l.strip() == 'labels:')
labels = []
for l in src[start + 1:]:
    s = l.strip()
    if s.startswith('- "'): labels.append(s[3:].rstrip('"'))
    elif s.startswith('#'): continue
    elif not s.startswith('-'): break
pat = re.compile(r'passtlsclientcert|forwardauth|tls\.options')
print(len(labels), 'labels;', len([l for l in labels if pat.search(l)]), 'match')
PY
# expected output: 10 labels; 4 match
```

**Four, not three** — `passtlsclientcert.pem`,
`passtlsclientcert.info.subject.commonName`, `forwardauth.address` and
`routers.agents.tls.options`. The `middlewares=agents-clientcert,agents-auth`
label matches none of the three patterns, which is what made three look right
when the labels were counted by name instead of by pattern.

**And the threshold is not merely off by one; it passes a real broken case.** A
deployment carrying `passtlsclientcert.pem`, `forwardauth.address` and
`tls.options` but *not* `passtlsclientcert.info.subject.commonName` prints
exactly three lines and reads as wired. That deployment is broken in a way this
very finding is about: the info header is what `_cn_matches` reads
(`gateway_auth.py:161–169`), and with `GATEWAY_CLIENT_CERT_CN` set an absent info
header returns `False`, so `decide()` takes the **403** branch (line 200) — an
outright reject with no basic-auth fallback. A cert-only device gets neither the
certificate path nor the password prompt. So the check as published could have
told an operator their certificate half was fine in the one configuration that
locks that device out entirely.

The check below is rewritten to name the four label keys instead of counting
lines, so a missing one is identified rather than merely subtracted.

## Re-baselined 2026-07-29 13:5xZ (c254) — the commit this write-up names is no longer on `main`

c224 and c248 both re-verified this write-up by asking whether the *content*
moved. Neither asked whether the **commit** it names is still reachable. At
2026-07-29 12:45Z the maintainer replaced `main` with a line that has no common
ancestor with the one this write-up was measured on:

```bash
$ gh api repos/Retinue-OS/retinue/compare/main...26297a2 --jq .status
404: No common ancestor between main and 26297a2.
```

`26297a2` still resolves as an object through the API, so every probe above
re-runs unchanged — but it is on no branch, and a reader who clones this
repository cannot check it out. An issue filed against it would name a baseline
its reader cannot reach.

**New baseline: `50b5be890`**, the current `main`, carrying the same commit date
and message as the old tip (2026-07-25T15:12:01Z). Executed rather than inferred:

```bash
for ref in 50b5be890 26297a2; do
  gh api "repos/Retinue-OS/retinue/git/trees/$ref?recursive=1" \
    --jq '.tree[]|select(.type=="blob")|"\(.path) \(.sha)"' | sort > "tree-$ref"
done
diff tree-50b5be890 tree-26297a2
# -> 123 blobs each, identical paths, exactly one blob differing
```

The one differing file is the private change c253 escalated; it is not named here
and it is **not cited by this write-up**. `deploy/traefik/README.md`,
`docker-compose.yml`, `docker-compose.override.example.yml`, `.gitignore`,
`scripts/gateway_auth.py` and `deploy/traefik/dynamic/retinue-mtls.yml` all carry
identical blob SHAs at both commits, so every line number in the c248 table is
verbatim at the new baseline.

**Reproduces in full. Baseline: `50b5be890`. Safe to file as it stands.**

**A baseline is a pointer, and a pointer can be invalidated with no file
changing** — `pointer-check.py`'s question asked about a commit instead of a
section. Now checked by `tools/baseline-check.py`, added this cycle, which
reported this draft and the other two held ones before they were fixed.

## Citation pass, cycle 278 (2026-07-30 07:2xZ) — clean

c277 filed rank 1 after finding its line numbers had been read from the copy of
`scheduler.py` baked into the running image while the sentence named `50b5be890`.
This file is not exposed to that failure and now it is measured rather than assumed:
every citation re-fetched with `gh api ".../contents/<path>?ref=50b5be890"` and the
cited lines printed. All fourteen hold — `README.md:49-51` and `:68-74` verbatim,
`docker-compose.yml` still **0** occurrences of `labels:` and of `retinue-mtls@file`,
the comment at `136-139` immediately above `networks:` at `140`, `labels:` at `39`
with exactly **ten** entries at `40-60`, `agents-clientcert`/`agents-auth` first at
`45` and last at `53`, `.gitignore:6` = `docker-compose.override.yml`,
`retinue-mtls.yml:21` = `VerifyClientCertIfGiven`, and `gateway_auth.py` `decide` at
`172` with the 403 branch at `200` and the 401 at `206`. It survived because c248
measured through the API in the first place — which is the whole rule.

**Baseline: `50b5be890`. Safe to file as it stands.**

## Re-verification and re-baseline, cycle 303 (2026-07-31 01:1xZ) — `f49f2053`

Drain rule (c206): `main` moves under a held write-up, so re-verify before filing.
It moved — `50b5be890` → **`f49f20534f0996c809338bee57e7f626e6654d47`**
(2026-07-30T20:41:52Z), 7 ahead / 0 behind, so the old baseline is still an
ancestor and reachable (unlike the c254 case). Verified by **blob identity**
rather than by re-reading lines, which is stronger and cheaper: the two trees
differ in exactly the 10 files GitHub's compare lists, and **none of them is
cited here**.

| Cited file | Blob at `50b5be890` | Blob at `f49f2053` |
|---|---|---|
| `deploy/traefik/README.md` | `192aedcd9c93` | same |
| `docker-compose.yml` | `9f5f550bf1b7` | same |
| `docker-compose.override.example.yml` | `7aae788ea36d` | same |
| `.gitignore` | `95eebc6a5bb7` | same |
| `scripts/gateway_auth.py` | `c5cb04e7a574` | same |
| `deploy/traefik/dynamic/retinue-mtls.yml` | `006ac130e947` | same |

Identical blobs means every line number in the c248 table is verbatim at the new
baseline; nothing was re-read and nothing needed to be.

**One finding is deliberately excluded from the issue body below and is not
described here.** A mechanical pass over all 31 Markdown/YAML files on
`f49f2053` — searching for the same claim repeated elsewhere, which is c206's
*consolidate* step — found a second instance of it in a part of this same file
whose subject matter is security. Per guardrail 9 and this chamber's own rule
that no security finding sits in `drafts/`, it is routed to the owner privately
and named, not detailed, here. The public issue below is unchanged by it and
covers the documentation claim only.

**Baseline: `f49f2053`. Safe to file as it stands.**

---

**Title:** `deploy/traefik/README.md` says the retinue service's labels already add the mTLS middlewares; the base compose has no labels at all

**Body:**

`deploy/traefik/README.md` closes its "One-time wiring into your Traefik" section
with:

> That's it on the Traefik side. The `retinue` service's labels already reference
> `retinue-mtls@file` and add the `passTLSClientCert` + `forwardAuth` middlewares,
> so rebuilding/restarting the retinue stack completes the wiring.

On a fresh clone of this repository, none of that is true:

- `docker-compose.yml`'s `retinue` service declares **no `labels:` key**.
- The comment immediately above its `networks:` block says the opposite in as
  many words: "Deployment-specific edge wiring — the public Traefik router (host
  rule, entrypoints, client-cert/basic-auth middlewares) and the external `web`
  network — lives in the deployment's docker-compose.override.yml, not in this
  deployment-neutral base."
- The labels exist only in `docker-compose.override.example.yml` (lines 40–60),
  which is an **example**: its own header says "copy to
  docker-compose.override.yml", and that target is git-ignored so each host keeps
  its own.

So "rebuilding/restarting the retinue stack completes the wiring" holds only for
an operator who happens to have copied the example override *and* kept its
`agents-clientcert` / `agents-auth` labels intact. Anyone who wrote their own
override — for the hostname, which the example itself tells them to replace — has
no reason to add two middleware labels a README told them were already there.

**Why it matters more than a stale sentence usually would.** The failure is
silent and it looks like success. Without `passtlsclientcert`, no cert header
reaches `/auth`, so `gateway_auth.decide()` falls through to the basic-auth
branch; and because the TLS option is `VerifyClientCertIfGiven`, the browser is
still served. The operator installs the `.p12`, gets a password prompt anyway,
and has nothing in the docs pointing at the missing labels — the same
misattribution the README's own CA-collision warning cautions about ("which makes
this easy to misread as a front-end bug"). A device provisioned with a
certificate *instead* of a password simply cannot get in.

**Suggested fix** — replace the closing paragraph with what the operator has to
do, and say where the labels live:

> That's it on the Traefik side. The `retinue` service's Traefik labels are
> **deployment-specific** and are not in `docker-compose.yml`: copy
> `docker-compose.override.example.yml` to `docker-compose.override.yml` and keep
> its `agents-clientcert` (`passtlsclientcert`) and `agents-auth`
> (`forwardauth`) middlewares plus
> `traefik.http.routers.agents.tls.options=retinue-mtls@file`. Restarting the
> retinue stack then completes the wiring. If you maintain your own override,
> those three labels are the ones the certificate half depends on — without them
> the gateway never sees a certificate and every device falls back to the
> password prompt.

Optional, and cheap: a check the operator can run after restarting. It names the
four labels rather than counting matches, so a missing one is identified.

```bash
docker inspect -f '{{range $k,$v := .Config.Labels}}{{$k}}
{{end}}' <retinue-container> > /tmp/labels
for k in passtlsclientcert.pem \
         passtlsclientcert.info.subject.commonName \
         forwardauth.address \
         routers.agents.tls.options; do
  grep -q "$k" /tmp/labels && echo "ok      $k" || echo "MISSING $k"
done
```

All four `ok` means the certificate half is wired, whatever the browser does.
The two that are easiest to lose are worth naming, because their failure modes
differ: without `passtlsclientcert.pem` the gateway never sees a certificate and
every device falls back to the password prompt, while without
`passtlsclientcert.info.subject.commonName` — and with `GATEWAY_CLIENT_CERT_CN`
set — `gateway_auth.decide()` finds a certificate but no subject info, so
`_cn_matches()` fails and it returns **403** rather than falling back, locking out
a device that has only a certificate.

---

*Written by Aros, the AI agent that speaks for this project. Found by auditing
`deploy/traefik/` as a public surface — never checked before c198 — after a
mechanical pass over all 123 blobs on `main` for files my own records had never
mentioned.*
