---
type: draft
title: "The PWA manifest's only user-visible string is German, and it is the only non-English string in `webapp/`"
status: held — **rank 3 of 3**, lowest of the held queue; the next c184 slot opens **2026-07-30T06:0xZ** and rank 1 (`updater-reports-dispatch-not-result.md`) holds it. *(Re-ranked c243: was rank 4 of 4; `w3id-namespace-unregistered.md` was filed as chamber#8 on 2026-07-29.)* Lowest because it is cosmetic: one user-visible string, wrong language, no behaviour depends on it.
cycle: 188
surface: webapp/manifest.webmanifest, webapp/{index,project,projects,conversations}.html, webapp/components/{app-launcher,markdown,project-page}.js, .dockerignore
---

# The finding

`webapp/manifest.webmanifest:4`:

```json
"description": "Kuratiertes, ablenkungsfreies Dashboard",
```

`CLAUDE.md`'s **Language convention** section says, of exactly this class of
string: *"For static UI copy in the dashboard/webapp, use English by default
until localization is implemented."* No localization exists — there is no
`lang` handling anywhere in `webapp/`, and all four page shells declare
`<html lang="en">`.

Measured over the whole directory at `26297a2`:

```bash
grep -rn "ä\|ö\|ü\|ß" webapp/ --include=*.js --include=*.html \
  --include=*.webmanifest --include=*.md
# webapp/manifest.webmanifest:4
```

One hit. It is the single exception to the convention in the whole front end,
and it sits in the one file whose strings the operating system renders rather
than the page: `name`/`short_name` become the home-screen label, `description`
appears in Chromium's richer install dialog. Every string the *page* shows is
English; the string the *phone* shows is not.

The English of it already exists in the repo. `webapp/README.md:3` opens with
"A minimalist, distraction-free dashboard", which is a translation of the same
sentence, and `CLAUDE.md:~437` uses "minimalist, curated phone dashboard".

# The fix

One line, no behaviour change:

```json
"description": "Minimalist, distraction-free dashboard",
```

# Severity, honestly

Cosmetic, and I am not going to dress it up. It is filable because it is
checkable, one-line, and contradicts a written convention in the repository's
own instruction file — not because it matters much to anyone today. Under the
c184 rate limit it waits; if a better candidate appears before the budget
opens, this one loses and that is the correct outcome.

# Second item, not worth its own anything: a stale comment

`webapp/conversations.html:17-18` describes the full-mode page as having "an
Active/Archived filter". `components/conversations.js:530` renders three tabs —
`Active`, `Archived`, `Edits` — and `:76` declares the scope as
`active|archived|edits`. `CLAUDE.md` gets it right ("an Active/Archived/Edits
filter"). A code comment one filter behind the component it introduces. Fold
into the same edit if the above is ever filed; do not file alone.

# Negative results from the same audit, recorded because they cost the time

These are the reason the cycle was worth spending, more than the finding is.

**1. The frontmatter parser in the project page really does match the
converter.** `components/project-page.js:33-56` claims to parse frontmatter
"the way the chambers' md2ttl converter does". Compared line by line against
`projects/.qlever/md2ttl.py:42-72` in this chamber: same fence regex, same
`^([A-Za-z0-9_]+):\s*(.*)$` key form, same empty-value-opens-a-list rule, same
`strip_quotes`, same behaviour on a `- item` line with no open list (ignored).
One immaterial divergence: the JS makes the newline after the closing fence
optional (`\n---\s*\n?`) where the Python requires it (`\n---\s*\n`), so a file
whose last byte is the closing fence renders on the page and fails in the
converter — which surfaces as a `parsingError` quad rather than silently, so it
is not the silent-wrong-behaviour class. The claim holds. This matters more
than it looks: the page and the store are two independent readers of the same
frontmatter, and a divergence between them would show the user fields the
triple store does not have.

**2. The deep-link contract between the project page and the conversations card
holds.** `project-page.js:372` links `/conversations.html#new?project=…&title=…`
and `:407` links `#conversation-<cid>`; `conversations.js:36-39` defines
`CONV_HASH_RE = /^#conversation-([0-9a-f]{32})$/` and
`COMPOSER_HASH_RE = /^#new(?:\?(.*))?$/`, parses the query at `:186-196`, and
handles `hashchange` at `:125`. Both buttons land where they say.

**3. The image build does not carry the deployment's secrets, despite
`.dockerignore` not mentioning `.env`.** The gap is real —`.dockerignore` lists
QLever index files, `.git`, Python caches, IDE dirs and `.garmin_session`, and
nothing else — but it costs nothing, because no Dockerfile in the repository
copies the build context. All nine (`Dockerfile` plus the eight service images)
copy named paths only; the root one copies eight explicit directories/files.
Worth writing down: this is the credential-custody claim holding at a layer
nobody had checked it at, and it holds by construction rather than by the
ignore file.

**4. `markdown.js`'s safety claim survives reading.** "The input is HTML-escaped
before any markup is generated, and only http(s)/mailto/tel URLs ever become
links (never javascript:)." `esc` (`base.js:11-15`) escapes `& < > " '`, and it
runs first in `renderInline`; the three link-producing regexes all require an
explicit `https?://`, `mailto:` or `tel:` scheme; generated anchors are stashed
behind a `\x01`-delimited sentinel so the emphasis passes cannot reach inside a
URL; the fence language class is bounded by `[\w.+-]*`. An `&quot;` surviving
into an `href` decodes as a character in the attribute *value*, not as a
delimiter, so it does not break out. No finding.

# The near-miss, which is the part worth remembering

I spent most of this audit building a case that the dashboard is **not
installable**: the manifest is fetched with credentials omitted, all four shells
link it without `crossorigin="use-credentials"`, and `gateway_auth.decide()`
401s any request carrying neither a client certificate nor an `Authorization`
header — with no path exemption, so `/manifest.webmanifest` is gated like
everything else. That last half is true and checkable
(`scripts/gateway_auth.py:172-206`, `docker-compose.override.example.yml:50`).

The first half is not, and I had it from memory. Checked against the specs
rather than filed:

- W3C Web App Manifest only fixes the credentials mode explicitly for the
  *cross-origin* case (§1.17.4, "Processing the manifest without a document"),
  where it defers to the link's `crossorigin` attribute.
- WHATWG HTML §2.5.5 defines the *CORS settings attribute credentials mode* by
  state: **No CORS → `"same-origin"`**, Anonymous → `"same-origin"`, Use
  Credentials → `"include"`. A missing `crossorigin` attribute is the No CORS
  state.

So per spec a same-origin manifest fetch carries the browser's basic-auth
credentials, and there is no defect here to file. What I actually remembered was
a Chromium implementation quirk I cannot reproduce, verify or date from this
container — no browser, no deployment reachable from here. Guardrail 3 and
register rule 28 both land in the same place: **a claim about someone else's
implementation needs the implementation, not a recollection.** Recorded rather
than dropped, because the next me will have the same memory.
