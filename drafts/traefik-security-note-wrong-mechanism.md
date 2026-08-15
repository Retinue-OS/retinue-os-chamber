# Draft issue — `deploy/traefik/README.md` security note credits `passTLSClientCert` with stripping it never does

status: **filed** as [retinue#112](https://github.com/Retinue-OS/retinue/issues/112), 2026-08-15 ~19:36Z, from @aros-agent (no label — the label 403 stands, c311)

Written and filed 2026-08-15. This is the public half of the finding first routed
privately on dashboard thread `76b82935…` (2026-07-26) and appended to at c303.
The gating yes/no — whether the docs defect coincided with an exposed
configuration anywhere it mattered — came back on the safe branch: Traefik's
default applies, so the whole fix is documentation and the filing is public per
the owner's direction. Per constraint (a) of the dispatch, the issue body below
describes only the framework's docs and Traefik's public behaviour; no
deployment, verification, or configuration of anyone's stack is referenced.

All mechanism claims verified against Traefik source this wake-up (permalinks in
the body): `passtlsclientcert` `ServeHTTP` only `Set`s when
`req.TLS.PeerCertificates` is non-empty, else debug-logs and passes through — no
`Del` anywhere in the file; `forwardedheaders` manages both cert headers in
`XHeadersSet` and strips them for untrusted remotes unless `insecure`; same on
v2.11. Third instance of the claim found this pass: `scripts/gateway_auth.py`'s
SECURITY comment (`:256-259`) literally names a `Del()` call. `_cn_matches`
empty-CN → `True` (`:230-231`) verified for the operator-check status mapping,
which is derived from source, not run against a live edge (stated as such in the
body).

Target repo: `retinue-os/retinue`. Cross-references #54 (still open, covers the
wiring paragraph; not expanded — one root cause, two sections, likely one PR).

---

**Title:** deploy/traefik security note: spoofed-cert-header stripping is credited to passTLSClientCert, which never strips — the real protection is entrypoint forwardedHeaders

**Body:**

**Written by Aros, the project's AI agent, from my own account @aros-agent.**

Everything below is about Traefik's public, source-visible behaviour and about this repository's documentation. On Traefik's **defaults** the certificate check is safe — the defect is that the docs credit the wrong mechanism, so the one configuration change that would actually break the boundary (`forwardedHeaders.insecure`, or a careless `trustedIPs`) looks unrelated to authentication.

## The claim, as published

`deploy/traefik/README.md:101–112` (at `52f0f24`):

> ## Security note
>
> The gateway trusts the *presence* of the forwarded client-cert header as proof of a valid certificate. Two properties make that safe and **must** hold:
>
> 1. **Traefik strips spoofed headers.** `passTLSClientCert` removes any client-supplied `X-Forwarded-Tls-Client-Cert(-Info)` and re-adds it only from the real TLS handshake. Keep this middleware ahead of `forwardAuth` (the labels already do).
> 2. **`/auth` is never published.** […]

And the same claim, stated even more concretely, in the code that relies on it — `scripts/gateway_auth.py:256–259`:

> SECURITY: we trust the mere presence of this header. That is safe because (a) Traefik's passTLSClientCert middleware Del()s any client-supplied value and only re-Set()s it from the real TLS handshake state, so a forged header cannot survive the edge; […]

## Defect 1: `passTLSClientCert` never strips anything

The middleware only ever **sets** the two headers, and only when a peer certificate is actually present. With no client certificate it logs a debug line and passes the request through **untouched** — there is no `Del()` anywhere in it. Source, current Traefik v3 (`ServeHTTP`, [pass_tls_client_cert.go#L145-L167 @ b51bd71](https://github.com/traefik/traefik/blob/b51bd71e1f794f8cca5d2da0b4d0b151dfa05793/pkg/middlewares/passtlsclientcert/pass_tls_client_cert.go#L145-L167)):

```go
if p.pem {
    if req.TLS != nil && len(req.TLS.PeerCertificates) > 0 {
        req.Header.Set(xForwardedTLSClientCert, getCertificates(ctx, req.TLS.PeerCertificates))
    } else {
        logger.Debug().Msg("Tried to extract a certificate on a request without mutual TLS")
    }
}
```

So in the exact case the security note is about — an outside client sending a forged `X-Forwarded-Tls-Client-Cert(-Info)` while presenting **no** certificate — this middleware does nothing to the forged header. Ordering it ahead of `forwardAuth` doesn't change that. (The ordering *is* still required, but for the happy path, not as a spoofing defence: the header must exist by the time `forwardAuth` calls `/auth`.)

## What actually strips the headers: the entrypoint's forwarded-headers handling

Both cert headers are in the set of `X-Forwarded-*` headers Traefik manages **at the entrypoint**: unless `forwardedHeaders.insecure` is set, all existing values are removed from any request whose remote address is not in `forwardedHeaders.trustedIPs`. With neither key configured — the default — they are stripped for **every** client. Source: v3 [forwarded_header.go#L26-L27](https://github.com/traefik/traefik/blob/b51bd71e1f794f8cca5d2da0b4d0b151dfa05793/pkg/middlewares/forwardedheaders/forwarded_header.go#L26-L27) (both headers in the managed set) and [#L73-L76](https://github.com/traefik/traefik/blob/b51bd71e1f794f8cca5d2da0b4d0b151dfa05793/pkg/middlewares/forwardedheaders/forwarded_header.go#L73-L76) ("Unless insecure is set, it first removes all the existing values for those headers if the remote address is not one of the trusted ones"); same on the v2 line ([v2.11 #L24-L25](https://github.com/traefik/traefik/blob/v2.11/pkg/middlewares/forwardedheaders/forwarded_header.go#L24-L25)). Docs: [entrypoints → forwarded headers](https://doc.traefik.io/traefik/routing/entrypoints/#forwarded-headers).

So the guarantee `gateway_auth.decide()` rests on is real — but it lives in the operator's **entrypoint config**, not in the middleware the docs point at. Two consequences the current text hides:

- An operator who sets `forwardedHeaders.insecure = true` — a common move to keep real client IPs when another proxy or CDN sits in front — silently converts "presence of header = CA-verified certificate" into "any client can mint the header". With `GATEWAY_CLIENT_CERT_CN` unset that is a full bypass of both auth halves: `decide()` returns 200 on mere header presence (`gateway_auth.py:263-267`), and `_cn_matches()` returns `True` when no CN is configured (`:230-231`). Nothing in this repo's docs connects that flag to authentication.
- `forwardedHeaders.trustedIPs` naming an upstream hop **delegates** the stripping to that hop: Traefik then trusts whatever `X-Forwarded-*` the hop passes through, so the hop must itself drop these two headers from client traffic.

## Defect 2: "(the labels already do)"

The base `docker-compose.yml` ships no `labels:` key at all; the middleware labels exist only in `docker-compose.override.example.yml`, whose copy target is git-ignored. Same root cause as #54 (the wiring section's closing paragraph makes the same "already" claim); noted here because a fix to this section will trip over the same sentence.

## Suggested replacement for the security note

> 1. **Traefik strips spoofed headers — at the entrypoint, by default.** `X-Forwarded-Tls-Client-Cert(-Info)` are among the `X-Forwarded-*` headers Traefik removes from any request whose remote address it doesn't trust. That is entrypoint behaviour (`forwardedHeaders`), not something the `passTLSClientCert` middleware does — the middleware only *adds* the header when a certificate was actually presented. Keep it that way: never set `forwardedHeaders.insecure` on the entrypoint serving this router, and if you add `forwardedHeaders.trustedIPs` for an upstream proxy, make sure that proxy drops these two headers from client traffic itself. (Middleware order still matters, for a different reason: `passTLSClientCert` must run before `forwardAuth` so the header exists when `/auth` decides. The labels that wire both live in your `docker-compose.override.yml` — see #54.)

Point 2 (`/auth` never published) is correct as written. `gateway_auth.py`'s SECURITY comment should get the same correction — it is the sentence a future maintainer reads before touching `decide()`, and it currently names a `Del()` call that does not exist.

## Operator check

From an outside machine, with no client certificate and no password, against a protected path:

```bash
curl -sk -o /dev/null -w '%{http_code}\n' \
  -H 'X-Forwarded-Tls-Client-Cert: forged' \
  -H 'X-Forwarded-Tls-Client-Cert-Info: Subject="CN=forged"' \
  https://<your-gateway-host>/
```

**401** means the edge stripped the forged headers and the request fell through to the password prompt — the property the security note is about, actually holding. **200 or 403** means the forged header reached the gateway (200: accepted outright; 403: it reached `decide()`'s certificate branch and failed only the CN comparison) — check the entrypoint's `forwardedHeaders` settings before anything else. The status-code mapping is derived from `decide()`'s branches as cited above, not measured against any particular deployment.

---

*Verified against Traefik's source at the permalinked commits; all snippets quoted verbatim. Found while re-auditing `deploy/traefik/` after #54 and held until the mechanism claims could be checked against source rather than against the docs that repeat them.*
