#!/usr/bin/env python3
"""Measure mentions of this project on the part of the world a search engine sees.

Why this exists, and why it is a second script
----------------------------------------------
`tools/mentions-check.py` measures the GitHub-visible surface and says so in its
closing sentence. Until c266 that sentence blamed the wider-web gap on the
network: *"no forum, social platform, blog, aggregator or search engine is
reachable from this deployment"*. c266 probed it for the first time and it was
false — general HTTPS egress works through the `HTTP_PROXY` egress audit — so the
gap was never reachability, it was unwritten queries. c266 deliberately did not
bolt a probe onto that script in the same wake-up, because two of its four
sample queries came back **HTTP 202**, and a naive scraper reading 202 as an
empty result set would publish a confident zero. This file is that probe, written
with the discrimination c266 said it needed.

Separate from `mentions-check.py` on purpose: that script's only failure mode is
a GitHub API error, and mixing an HTML-scraping network path into it would put a
flaky failure mode inside an instrument that currently has none. Two surfaces,
two instruments, run together in the survey.

The defect this reproduces
--------------------------
Measured 2026-07-30 from this deployment, all three engines, `curl` through the
egress audit:

| Engine | Control query `sparql` | Body |
|---|---|---|
| `lite.duckduckgo.com/lite/` | **HTTP 202**, 0 results | anti-bot challenge (`anomaly.js`, `challenge-form`) |
| `www.bing.com/search` | **HTTP 200**, 0 results | JS shell, `challenge/verify` + captcha config, no `b_algo` item |
| `www.mojeek.com/search` | HTTP 200, **10 results** | real result page |

Two of the three answer with a **2xx status and a plausible HTML body carrying
zero results**, for a query that has millions. That is the false zero this script
exists to refuse, and it is not the same failure as c242's 422: there, `gh` exited
non-zero and the error was visible. Here nothing is visibly wrong.

So the boundary is not the status code and not the challenge markers — it is a
**positive control**. Each engine is asked a query that must have results before
it is asked about this project. An engine whose control returns nothing is
reported UNAVAILABLE and its project readings are discarded, not reported as zero.
The challenge markers are kept for diagnosis only: they name *why* an engine is
unavailable, and a new challenge shape nobody has seen yet must not be able to
turn into a zero by simply not matching a marker.

What it measures, and what it does not
--------------------------------------
Measured: for each engine that passes its control, whether any indexed page names
this project by a token that cannot be produced from unrelated words — and, for
each hit, whether it is on `github.com` or off it.

The github.com/off-github split is the point rather than a detail. c258 found this
strategy reporting conversion (stars, forks) as if it were reach, with the arrivals
denominator 403 to this token. Off-GitHub mentions are the one reach signal that is
actually obtainable, and bet 3 in `strategy.md` — that the audience for this
architecture is on Mastodon and Bluesky rather than somewhere else — is a claim
about where people talk about things off GitHub.

**Not** measured: Google (no scrapeable endpoint), any engine's ranking, anything
behind a login, anything in a private forum, and anything published in the last
few days that no crawler has fetched yet. A zero from this script means *no
indexed page that these engines will show me names this project* — narrower than
"nobody mentions it", and the closing line says so.

Usage
-----
    python3 tools/web-mentions-check.py            # all engines
    python3 tools/web-mentions-check.py --engine mojeek

Exit status
-----------
    0  every engine that answered read clean, and at least one engine answered
    1  something needs a human read: a confirmed mention, a failed probe, or
       **every** engine unavailable — which is a measurement that did not happen,
       not a zero

Instrument discipline
---------------------
Per the standing rule adopted at c227, the classifier and the availability logic
run against known-good and known-bad fixtures on every invocation and the script
refuses to report on live data if they do not come out as expected. The known-bad
fixtures are real: the challenge bodies above, and the irrelevant hits Mojeek
actually returned for `retinue-os` (a dictionary entry for the English noun) and
`qlever-dir` (a German car park called *qlever-parq*). This check reproduces the
defects it was written for rather than merely agreeing with itself.

Honest limit on the extractors, stated because it will not be obvious later: the
Mojeek extractor was written against a live result page and verified against it.
The DuckDuckGo and Bing extractors were written from their markup and are verified
**only against fixtures**, because neither engine would serve this deployment a
result page on the day the script was written. If one of them starts answering,
the first run that reports hits from it should be read by hand before its number
is trusted.
"""

import argparse
import re
import subprocess
import sys
import time
import urllib.parse

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120 Safari/537.36"
)

# A query that must return results from any working general-purpose index. Chosen
# to be unrelated to this project so that a control pass says nothing about the
# thing being measured, and stable enough not to need revisiting.
CONTROL_QUERY = "sparql"

# The project queries. Each is a plain phrase: search operators are avoided
# because they are per-engine and rejected inconsistently — Mojeek answered
# `"retinue-os" -site:github.com` with **HTTP 403** on 2026-07-30, which this
# script would report as a failed probe. The github.com/off-github split is done
# here, on the hits, where it cannot fail silently.
PROJECT_QUERIES = [
    "retinue-os",
    "qlever-dir",
    "retinue-os.github.io",
    "retinue agent chamber sparql",
]

# ---------------------------------------------------------------------------
# The second question, added c359: not "does anyone mention us" but "is our own
# surface in the index at all". They have been conflated since this file was
# written, and they have different answers and different remedies. A mention
# needs a reader; being indexed needs only a crawler, so a zero here is an
# explanation for the mention zero that owes nothing to the missing accounts.
#
# These carry a search operator, which the paragraph above says to avoid. The
# reason it gives is real but narrower than it reads: the 403 on 2026-07-30 was
# for `-site:` (negation), and `site:` on its own was verified working on
# 2026-08-01 — `site:w3.org sparql` returned 10 results. So the operator is
# admissible **only behind its own control**, below: an engine that answers the
# bare control may still reject or ignore an operator, and an ignored operator
# returns a plausible page about nothing.
#
# Kept out of PROJECT_QUERIES and counted separately, because a hit here is our
# own page and counting it as a mention would report reach that is really just
# our own crawler footprint — the c258 error in a new place.
OPERATOR_CONTROL = "site:w3.org sparql"
INDEX_QUERIES = [
    "site:retinue-os.github.io",
    "site:github.com retinue-os",
]

# The discriminator, deliberately identical in spirit to the one in
# mentions-check.py: a hit counts only if it carries a token that cannot be
# produced by an engine matching unrelated words. "retinue" alone is a common
# English noun and a Warhammer keyword; "qlever" alone is a German car park.
#
# The separator is `[-_]` rather than `-` because the first self-test run rejected
# its own known-good fixture: a plausible lobste.rs URL slug
# (`/s/…/retinue_os_credential_isolation`), since slugifiers replace hyphens with
# underscores. This matters more here than in mentions-check.py, whose inputs are
# issue prose rather than URLs — that is why the two discriminators differ, and it
# is the whole reason to write the fixture as the URL a real mention would have
# rather than as the URL the regex was expecting.
CONFIRM_RE = re.compile(
    r"""(
          retinue[-_]os                 # the org name, separator intact
        | github\.com/retinue           # any link into the org or its repos
        | qlever-dir                    # project-unique repo name, hyphen intact
    )""",
    re.IGNORECASE | re.VERBOSE,
)

GITHUB_HOST_RE = re.compile(r"^https?://(?:[a-z0-9-]+\.)*github\.com/", re.IGNORECASE)


TAG_RE = re.compile(r"<[^>]+>")


def _strip(html):
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", html)).strip()


def _extract(item_pattern, url_pattern):
    """Build an extractor returning one (url, text) pair per result item.

    Both halves are needed, and the second half is the one the first version of
    this script left out. A result carries the engine's title and snippet as well
    as its URL, and a blog post that discusses this project at a URL like
    `/2026/08/agents-and-credentials` names it **only in the text**. Classifying
    the URL alone would have reported that page as a raw-but-unconfirmed hit —
    i.e. as a zero — while the answer sat in the snippet the engine had already
    handed over. That is the c243 defect exactly: a probe declaring a surface it
    only half reads.
    """
    item_rx = re.compile(item_pattern, re.IGNORECASE | re.DOTALL)
    url_rx = re.compile(url_pattern, re.IGNORECASE)

    def extract(body):
        out = []
        for block in item_rx.findall(body):
            m = url_rx.search(block)
            if not m:
                continue
            # The URL pattern may carry alternatives, because attribute order is
            # not fixed: DuckDuckGo writes href before class, and a pattern that
            # assumed the other order silently dropped every result — caught by
            # the good-page fixture below, which is the only reason it is there.
            url = next((g for g in m.groups() if g), None)
            if url:
                out.append((url, _strip(block)))
        return out

    return extract


ENGINES = {
    # Verified live 2026-07-30: control returns 10 results, real result page.
    # Result items are delimited by literal <!--rs--> / <!--re--> comments and
    # carry <a class="title" href> plus a <p class="s"> snippet.
    "mojeek": {
        "url": "https://www.mojeek.com/search?q={q}",
        "extract": _extract(
            r"<!--rs-->(.*?)<!--re-->",
            r'<a class="title"[^>]*href="(https?://[^"]+)"',
        ),
        "challenge": re.compile(
            r"mojeek\.com/challenge|are you a robot"
            # Added c359 from a live body: the throttle page says this and
            # matches neither marker above. Diagnosis only — `results_page`
            # is what decides.
            r"|Verification required|<title>\s*Captcha",
            re.I,
        ),
        # Verified against two live bodies on 2026-08-01: a genuine no-result
        # page for a nonsense term carries `<title>… - Mojeek Search`, and the
        # throttle page carries `<title>Captcha`.
        "results_page": re.compile(r"<title>[^<]*-\s*Mojeek Search\s*</title>", re.I),
    },
    # Fixture-verified only: served an anti-bot challenge (202) on 2026-07-30.
    "duckduckgo": {
        "url": "https://lite.duckduckgo.com/lite/?q={q}",
        "extract": _extract(
            r"(<tr[^>]*>.*?class=\"result-link\".*?)(?=<tr[^>]*class=\"result-sep|</table)",
            r'class="result-link"[^>]*?href="(https?://[^"]+)"'
            r'|href="(https?://[^"]+)"[^>]*?class="result-link"',
        ),
        "challenge": re.compile(r"duckduckgo\.com/anomaly\.js|challenge-form", re.I),
        # No verified marker: this deployment has never been served a real
        # result page by this engine, so there is nothing to take one from.
        # `None` means "a zero from this engine is not reportable" — see
        # read_page(). Fail-safe, and a no-op while its control fails anyway.
        "results_page": None,
    },
    # Fixture-verified only: served a JS shell with no result items on 2026-07-30.
    "bing": {
        "url": "https://www.bing.com/search?q={q}",
        "extract": _extract(
            r"(<li class=\"b_algo\".*?</li>)",
            r'<h2>\s*<a[^>]*href="(https?://[^"]+)"',
        ),
        "challenge": re.compile(r"bing\.com/challenge/verify|captchaSuccess", re.I),
        "results_page": None,  # same reason as duckduckgo
    },
}

# ---------------------------------------------------------------------------
# Fixtures. The bad ones are real, quoted from what these engines actually
# returned on 2026-07-30.
# ---------------------------------------------------------------------------

KNOWN_BAD_URLS = [
    # Mojeek's top hits for "retinue-os": the English noun, fuzzy-matched.
    "https://www.wordwebonline.com/en/RETINUE",
    "https://forvo.com/word/retinue/",
    "https://www.vidaextra.com/guias-y-trucos/gta-online-como-conseguir-gratis-coche-vapid-retinue",
    # Mojeek's top hits for "qlever-dir": QLever's own docs (not this project),
    # and a German car park.
    "https://docs.qlever.dev/rebuild-index/",
    "https://www.q6q7.de/services/anreise-parken/qlever-parq",
    "https://github.com/ad-freiburg/qlever-petrimaps",
    # Mojeek's top hits for "retinue-os.github.io": nothing to do with anything.
    "https://thunderstore.io/c/lethal-company/p/lethal_coder/Lethal_Enhanced_Party_Edition/",
    "https://pydigger.com/pypi/shotstars",
]

KNOWN_GOOD_URLS = [
    "https://github.com/Retinue-OS/retinue",
    "https://retinue-os.github.io/retinue-os-chamber/",
    "https://github.com/retinue-os/qlever-dir/issues/9",
    "https://lobste.rs/s/abc123/retinue_os_credential_isolation",
    "https://someones.blog/2026/08/reading-qlever-dir",
]

# Real challenge bodies, trimmed to the identifying markup. A control query
# against either of these must come out UNAVAILABLE.
FIXTURE_DDG_CHALLENGE = (
    '<!DOCTYPE html><html lang="en"><head>'
    '<link rel="canonical" href="https://duckduckgo.com/">'
    "<title>DuckDuckGo</title></head><body>"
    '<form id="img-form" action="//duckduckgo.com/anomaly.js?sv=lite&cc=sre'
    '&ti=1785366651" target="ifr" method="POST"></form>'
    '<form id="challenge-form" action="//duckduckgo.com/anomaly.js?sv=lite"'
    "></form></body></html>"
)
FIXTURE_BING_SHELL = (
    "<html><head><title>&quot;sparql&quot; - Recherche</title></head><body>"
    '<script>_G.BAT="0";var cfg={"captchaUrl":'
    '"https://www.bing.com/challenge/verify?partner=7\\u0026token=",'
    '"captchaSuccessPostMessage":"verificationComplete"};</script>'
    '<div id="b_content"><ol id="b_results"></ol></div></body></html>'
)
# A real Mojeek result page, trimmed to two result items, comment delimiters and
# snippet markup kept verbatim.
FIXTURE_MOJEEK_OK = (
    "<html><head><title>sparql - Mojeek Search</title></head><body>"
    '<ul class="results-standard">\n<!--ls-->\n'
    '<!--rs--><li class="r1">'
    '<a title="https://www.w3.org/TR/sparql11-query/" '
    'href="https://www.w3.org/TR/sparql11-query/" class="ob">'
    '<p class="i"><span class="url">https://www.w3.org</span></p></a>'
    '<h2><a class="title" title="https://www.w3.org/TR/sparql11-query/" '
    'href="https://www.w3.org/TR/sparql11-query/">SPARQL 1.1 Query Language</a>'
    '</h2><p class="s">Blank node labels are scoped to a result set.</p>'
    "</li><!--re-->\n"
    '<!--rs--><li class="r2 clu-result">'
    '<h2><a class="title" title="https://en.wikipedia.org/wiki/SPARQL" '
    'href="https://en.wikipedia.org/wiki/SPARQL">SPARQL - Wikipedia</a></h2>'
    '<p class="s">SPARQL is an RDF query language.</p>'
    "</li><!--re-->\n"
    "</ul></body></html>"
)
# The case the URL-only classifier would have called a zero: an innocuous URL
# whose snippet names the project. Must confirm, and must confirm as off-github.
FIXTURE_MOJEEK_SNIPPET_HIT = (
    '<ul class="results-standard">\n'
    '<!--rs--><li class="r1">'
    '<h2><a class="title" title="https://someones.blog/2026/08/credentials" '
    'href="https://someones.blog/2026/08/credentials">Sidecar credentials</a>'
    '</h2><p class="s">I spent a weekend with '
    "<strong>retinue-os</strong>/retinue and the gateway design holds up.</p>"
    "</li><!--re-->\n</ul>"
)
# Well-formed result pages for the two engines that would not serve this
# deployment one. **Reconstructed from their documented markup, not captured** —
# which is exactly why the docstring says their extractors are fixture-verified
# only, and why the first live run that reports hits from either needs a human
# read. They are here so that "UNAVAILABLE" cannot hide a parser that would fail
# on a real page too.
FIXTURE_DDG_RESULTS = (
    "<html><body><table>"
    '<tr><td valign="top">1.&nbsp;</td><td>'
    '<a rel="nofollow" href="https://www.w3.org/TR/sparql11-query/" '
    'class="result-link">SPARQL 1.1 Query Language</a></td></tr>'
    '<tr><td class="result-snippet">Blank node labels are scoped.</td></tr>'
    '<tr class="result-sep"><td>&nbsp;</td></tr>'
    '<tr><td valign="top">2.&nbsp;</td><td>'
    '<a rel="nofollow" href="https://en.wikipedia.org/wiki/SPARQL" '
    'class="result-link">SPARQL - Wikipedia</a></td></tr>'
    '<tr><td class="result-snippet">An RDF query language.</td></tr>'
    "</table></body></html>"
)
FIXTURE_BING_RESULTS = (
    "<html><body><ol id=\"b_results\">"
    '<li class="b_algo"><h2>'
    '<a href="https://www.w3.org/TR/sparql11-query/">SPARQL 1.1 Query Language</a>'
    '</h2><div class="b_caption"><p>Blank node labels are scoped.</p></div></li>'
    '<li class="b_algo"><h2>'
    '<a href="https://en.wikipedia.org/wiki/SPARQL">SPARQL - Wikipedia</a>'
    '</h2><div class="b_caption"><p>An RDF query language.</p></div></li>'
    "</ol></body></html>"
)
# The shape that makes the control load-bearing: a challenge page carrying none
# of the known markers. It must still come out UNAVAILABLE, on zero results
# alone, or a new anti-bot page shape becomes a silent zero.
FIXTURE_UNKNOWN_BLOCK = (
    "<html><head><title>Just a moment…</title></head><body>"
    "<p>Verifying your request.</p></body></html>"
)
# The two bodies c359 was written for, both captured live on 2026-08-01.
#
# A **genuine** no-result page: a nonsense term, 11 010 B, no `<!--rs-->` item
# and no results container, but the ordinary title and chrome. A zero here is a
# reading and must stay one.
FIXTURE_MOJEEK_EMPTY = (
    "<html><head><title>zxqwvfjklmnopqrs - Mojeek Search</title></head><body>"
    '<nav><a href="/">Web</a><a href="/images">Images</a>'
    '<a href="/news">News</a><a href="/search?q=&amp;arc=none">Advanced Search</a>'
    "</nav><ul></ul></body></html>"
)
# The **throttle** page, 5 777 B, served for a query issued a few seconds after
# several others — while the single-word control kept returning 10 results
# immediately before and after it. Reconstructed from the stripped text of the
# live body (the raw HTML was not retained), which is why the assertion that
# matters is the *absence* of the `results_page` marker rather than the presence
# of any string quoted here.
FIXTURE_MOJEEK_CAPTCHA = (
    "<html><head><title>Captcha</title></head><body>"
    '<nav><a href="/">Web</a><a href="/images">Images</a></nav>'
    "<h1>Verification required</h1>"
    "<p>Please complete the challenge below to continue.</p>"
    "</body></html>"
)


def self_test():
    """Refuse to report unless the classifier and the control logic behave."""
    failures = []

    for url in KNOWN_BAD_URLS:
        if CONFIRM_RE.search(url):
            failures.append(f"known-bad accepted: {url}")
    for url in KNOWN_GOOD_URLS:
        if not CONFIRM_RE.search(url):
            failures.append(f"known-good rejected: {url}")

    # The github.com split, both directions.
    if not GITHUB_HOST_RE.match("https://github.com/Retinue-OS/retinue"):
        failures.append("github split: missed a github.com URL")
    if GITHUB_HOST_RE.match("https://retinue-os.github.io/retinue-os-chamber/"):
        failures.append("github split: github.io counted as github.com")
    if GITHUB_HOST_RE.match("https://notgithub.com/retinue-os"):
        failures.append("github split: matched a lookalike host")

    # Availability: results present -> available; zero results -> unavailable,
    # whether or not a challenge marker is recognised.
    cases = [
        ("mojeek", FIXTURE_MOJEEK_OK, True, 2),
        ("mojeek", FIXTURE_MOJEEK_SNIPPET_HIT, True, 1),
        ("duckduckgo", FIXTURE_DDG_CHALLENGE, False, 0),
        ("bing", FIXTURE_BING_SHELL, False, 0),
        ("mojeek", FIXTURE_UNKNOWN_BLOCK, False, 0),
    ]
    for name, body, want_ok, want_n in cases:
        hits = ENGINES[name]["extract"](body)
        if len(hits) != want_n:
            failures.append(
                f"extractor {name}: {len(hits)} hits from fixture, expected {want_n}"
            )
        if bool(hits) is not want_ok:
            failures.append(
                f"control {name}: availability {bool(hits)}, expected {want_ok}"
            )

    # The snippet half of the extraction, and the reason it exists: a hit whose
    # URL is innocuous and whose snippet names the project must be confirmed, and
    # classified off-github. Checked against both halves so that dropping the
    # text from the extractor fails here rather than in six weeks.
    snippet_hits = ENGINES["mojeek"]["extract"](FIXTURE_MOJEEK_SNIPPET_HIT)
    if snippet_hits:
        url, text = snippet_hits[0]
        if CONFIRM_RE.search(url):
            failures.append("snippet fixture: its URL matches, so it tests nothing")
        if not CONFIRM_RE.search(f"{url}\n{text}"):
            failures.append("snippet fixture: mention in the text was not confirmed")
        if GITHUB_HOST_RE.match(url):
            failures.append("snippet fixture: off-github URL classified as github")
    else:
        failures.append("snippet fixture: extracted no result item")

    # The two engines whose extractors are fixture-verified only must still parse
    # a well-formed result page, or "UNAVAILABLE" would be hiding a broken parser.
    for name, body, want_n in (
        ("duckduckgo", FIXTURE_DDG_RESULTS, 2),
        ("bing", FIXTURE_BING_RESULTS, 2),
    ):
        hits = ENGINES[name]["extract"](body)
        if len(hits) != want_n:
            failures.append(
                f"extractor {name}: {len(hits)} hits from a good page, "
                f"expected {want_n} — an unavailable engine would mask this"
            )

    # The markers are diagnosis, not the boundary — but they must still fire on
    # the bodies they were taken from, or the error message lies.
    if not ENGINES["duckduckgo"]["challenge"].search(FIXTURE_DDG_CHALLENGE):
        failures.append("duckduckgo: challenge marker missed its own fixture")
    if not ENGINES["bing"]["challenge"].search(FIXTURE_BING_SHELL):
        failures.append("bing: challenge marker missed its own fixture")
    if ENGINES["mojeek"]["challenge"].search(FIXTURE_MOJEEK_OK):
        failures.append("mojeek: challenge marker fired on a good page")
    if ENGINES["mojeek"]["challenge"].search(FIXTURE_MOJEEK_EMPTY):
        failures.append("mojeek: challenge marker fired on a genuine empty page")
    if not ENGINES["mojeek"]["challenge"].search(FIXTURE_MOJEEK_CAPTCHA):
        failures.append("mojeek: challenge marker missed the throttle page")

    # c359: the zero/unmeasured boundary, run through `read_page` — the same
    # function the live path calls. Asserted on the **note**, not only on the
    # verdict: a wrong reason and a right reason are both falsy, so a
    # verdict-only test passes straight through a message that misattributes.
    read_cases = [
        # engine, fixture, expected hit count or None, substring the note must carry
        ("mojeek", FIXTURE_MOJEEK_OK, 2, None),
        ("mojeek", FIXTURE_MOJEEK_EMPTY, 0, None),
        ("mojeek", FIXTURE_MOJEEK_CAPTCHA, None, "challenge body"),
        ("mojeek", FIXTURE_UNKNOWN_BLOCK, None, "no results-page marker"),
        ("duckduckgo", FIXTURE_DDG_RESULTS, 2, None),
        ("duckduckgo", FIXTURE_DDG_CHALLENGE, None, "challenge body"),
        ("bing", FIXTURE_BING_SHELL, None, "challenge body"),
        # An engine with no verified marker may not report a zero even from a
        # page carrying no challenge at all.
        ("bing", "<html><body>nothing here</body></html>", None,
         "no verified results-page marker"),
    ]
    for name, body, want_n, want_note in read_cases:
        hits, note = read_page(name, body)
        got_n = None if hits is None else len(hits)
        if got_n != want_n:
            failures.append(
                f"read_page {name}: {got_n} hits, expected {want_n}"
            )
        if want_note is None:
            if note is not None:
                failures.append(f"read_page {name}: unexpected note {note!r}")
        elif note is None or want_note not in note:
            failures.append(
                f"read_page {name}: note {note!r} does not carry {want_note!r}"
            )

    return failures


def fetch(url):
    """GET one URL. Returns (status, body, error). An error is never a zero."""
    cmd = [
        "curl", "-sS", "-A", UA, "--max-time", "30",
        "-w", "\n%{http_code}", url,
    ]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, "", str(exc)
    if out.returncode != 0:
        err = out.stderr.strip().splitlines()
        return None, "", err[-1] if err else "curl failed"
    body, _, status = out.stdout.rpartition("\n")
    try:
        code = int(status.strip())
    except ValueError:
        return None, body, f"unparseable status {status!r}"
    return code, body, None


def read_page(engine, body):
    """Turn a 200 body into (hits, note) — or (None, why) if it measured nothing.

    Split out of `query()` at c359 so the self-test exercises the path the live
    run takes instead of a parallel reimplementation of it.

    The rule this encodes, and the defect it closes
    ----------------------------------------------
    Before c359 a 200 carrying zero extractable results was a **zero** unless a
    known challenge marker fired — a negative test, so any block page nobody had
    seen yet became a measured zero. On 2026-08-01 that happened live: Mojeek
    answered a query issued seconds after several others with a 5 777 B
    *Verification required* page, matching neither marker, while the single-word
    control returned 10 results immediately before and after. Under the old code
    that query would have printed `0 raw 0 confirmed`.

    So the test is now **positive**: a zero counts only if the page identifies
    itself as a results page. An engine with no verified `results_page` marker
    cannot report a zero at all — fail-safe, and free today because both such
    engines fail their control anyway.

    The engine-level control does not cover this. It ran, it passed, and the
    engine was genuinely available; what failed was one later request. Same
    class as c357: *a verdict derived from a run-wide fact is not a measurement
    of a per-request one.*
    """
    spec = ENGINES[engine]
    hits = spec["extract"](body)
    if hits:
        return hits, None
    if spec["challenge"].search(body):
        return None, "challenge body — unmeasured, not a zero"
    marker = spec.get("results_page")
    if marker is None:
        return None, "no verified results-page marker for this engine — zero not reportable"
    if not marker.search(body):
        return None, "200 with no results and no results-page marker — unmeasured, not a zero"
    return [], None


def query(engine, q):
    spec = ENGINES[engine]
    url = spec["url"].format(q=urllib.parse.quote_plus(q))
    code, body, error = fetch(url)
    if error is not None:
        return None, f"fetch failed: {error}"
    if code != 200:
        # 403 is real: Mojeek returned it for a query carrying `-site:`.
        note = " (anti-bot challenge)" if spec["challenge"].search(body) else ""
        return None, f"HTTP {code}{note}"
    return read_page(engine, body)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--engine", action="append", choices=sorted(ENGINES),
                    help="restrict to one engine (repeatable)")
    ap.add_argument("--sleep", type=float, default=8.0,
                    help="seconds between queries (be a polite client)")
    args = ap.parse_args()

    failures = self_test()
    if failures:
        print("self-test: FAIL — refusing to report on live data")
        for line in failures:
            print(f"  {line}")
        return 1
    print(
        f"self-test: pass ({len(KNOWN_GOOD_URLS) + len(KNOWN_BAD_URLS)} classifier "
        "cases, 3 host-split, 5 availability, 3 snippet, 2 good-page parser, "
        "5 marker, 8 read_page)"
    )

    engines = args.engine or sorted(ENGINES)
    available, unavailable, confirmed, errors = [], [], [], []

    for name in engines:
        hits, note = query(name, CONTROL_QUERY)
        if hits is None:
            unavailable.append((name, note))
            print(f"  UNAVAILABLE  {name}: control {CONTROL_QUERY!r} — {note}")
            continue
        if not hits:
            why = note or "2xx with zero results"
            unavailable.append((name, why))
            print(f"  UNAVAILABLE  {name}: control {CONTROL_QUERY!r} returned "
                  f"nothing — {why}. Readings discarded, NOT reported as zero.")
            continue
        available.append(name)
        print(f"  control ok   {name}: {len(hits)} results for {CONTROL_QUERY!r}")
        time.sleep(args.sleep)

        for q in PROJECT_QUERIES:
            hits, note = query(name, q)
            if hits is None:
                errors.append((name, q, note))
                print(f"    ERROR    {name} {q!r}: {note}")
                time.sleep(args.sleep)
                continue
            kept = [(u, t) for u, t in hits if CONFIRM_RE.search(f"{u}\n{t}")]
            for u, _t in kept:
                where = "github" if GITHUB_HOST_RE.match(u) else "off-github"
                confirmed.append((name, q, u, where))
            print(f"    {len(hits):3d} raw  {len(kept):2d} confirmed  "
                  f"{name} {q!r}")
            time.sleep(args.sleep)

    off = [c for c in confirmed if c[3] == "off-github"]
    on = [c for c in confirmed if c[3] == "github"]
    print()
    print(f"engines answering {len(available)}/{len(engines)}, "
          f"confirmed hits {len(confirmed)} ({len(on)} on github.com, "
          f"{len(off)} off it), failed probes {len(errors)}")
    for name, q, url, where in confirmed:
        print(f"  CONFIRMED [{where}] {url}   ({name}, {q!r})")

    if not available:
        print(
            "\nNo engine answered its control query, so nothing was measured.\n"
            "This is not a zero: every engine returned a 2xx page with no\n"
            "results, which is what an anti-bot challenge looks like. Re-run\n"
            "later before recording any reading."
        )
        return 1
    if errors:
        print("\nA failed probe is not a zero. Re-run before recording a reading.")
        return 1
    if off:
        print("\nAn off-GitHub mention exists. Read it before counting it, and\n"
              "record it in projects/public-surface.md — this is the reach signal\n"
              "c258 found had no instrument.")
        return 1

    print(
        "\nNo page off github.com, in the index of any engine that answered\n"
        f"({', '.join(available)}), names this project. That is a measured zero for\n"
        "those indexes and nothing more: it does not cover Google, anything behind\n"
        "a login, or a page too new to have been crawled. Reach off GitHub is now\n"
        "measured-and-zero rather than unmeasured (c258) — for these engines."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
