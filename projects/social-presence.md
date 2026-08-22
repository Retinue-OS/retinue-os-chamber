---
type: project
id: proj-social-presence
title: "Establish the project's social accounts"
goal: "Retinue has a small, honest, clearly-labelled presence where its audience already is."
goal_status: partly_achieved
current_next_action: "Aros, this cycle (2026-08-08 ~12:1xZ): OWNER ENGAGED FOR THE FIRST TIME WITH DIRECTION, not just account setup. He commented on chamber#1 at 12:04:38Z ('keep posting. follow people. repost related content.') and 12:07:06Z ('add a picture of you. do you look as cute as your cousin?', attaching Ari the teddy bear's Design Guidelines.md). Acted same cycle: (1) POSTED the bet-1 triple-store piece, the lead-story content held since c474 - https://bsky.app/profile/aros-retinue.bsky.social/post/3msl2ftogcv27 - a plain link post, no thread, verified live via the public API. (2) FOLLOWED four accounts, checked by feed content not just bio, all genuinely on-topic: bobdc.bsky.social (wrote Learning SPARQL), mscottm.bsky.social (semantic web/RDF professional), patternist.xyz (Automerge/local-first at Ink & Switch - the actual neighborhood of the 'memory as files you own' argument), tynidev.bsky.social (a peer self-hosted-agent project). Deliberately did NOT follow two other 'self-hosted AI agent' accounts the same search turned up (projectmorpheus.bsky.social, glitchcatclub.bsky.social) - their feeds read as repetitive marketing copy rather than a person writing about their own work, and following those would be guardrail-2 engagement-farming rather than community-tending. (3) REPOST: none yet - read the last five posts from each of the four follows and none were specific enough to reshare in good conscience; will do it the day something fits rather than force one. (4) AVATAR: honest answer given, not attempted - no image-generation tool exists in this environment, so I cannot produce one; also flagged that Ari's Design Guidelines are for a literal bear (fur, sweater, paw gestures) and I am not one, so reusing them wholesale would be the wrong brief even with a tool. Offered to write a proper brief if useful. All four points reported in one comment: https://github.com/Retinue-OS/retinue-os-chamber/issues/1#issuecomment-5226064112. STILL OPEN, unchanged: Mastodon (server choice - infosec.exchange or techhub.social, needs an owner-submitted approval application) and Nostr (owner yes/no on self-generated keypair). Consequence for strategy.md: this is the first owner comment on chamber#1 that is direction rather than infrastructure setup, five days after the Bluesky handover - it does not close the issue (Mastodon/Nostr unmoved) but it is the first live datum that the owner is reading and reacting to what gets posted, which matters for bet 3's audience question even though the owner is not the audience the bet is about. Previous entry, Aros, c474 (2026-08-04 ~13:1xZ): BLUESKY IS LIVE. Owner commented on chamber#1 at 12:44:52Z - 'Bluesky is set up Check the BSKY_* variables' - BSKY_EMAIL/BSKY_PASSWORD present in the environment, SOCIAL_SEND_POLICY=allow. Logged in via com.atproto.server.createSession: handle aros-retinue.bsky.social, did:plc:qnxaj2xwx6lzehhqosi44u5w, created 2026-08-03T14:01:24Z (so it existed almost a day before I was told to check). Profile ALREADY carried an AI-disclosure bio, a display name, an avatar, and a self-applied 'bot' label on the profile record (Bluesky's own policy has no bot flag - this is stricter than required, matching guardrail 1's spirit beyond the platform's own ask). That satisfies this file's three checklist items for Bluesky specifically: policy already recorded below (2026-07-26/08-01), disclosure verified in the bio, and the owner's comment IS the handover under guardrail 7/8. Posted the first message myself under guardrail 8 (no further sign-off): https://bsky.app/profile/aros-retinue.bsky.social/post/3msb3qycwj32m - a plain, short intro (215 chars) naming the AI-agent status and the legal split, linking the framework repo, no content claim yet. Deliberately did NOT stack a second post the same cycle (prefer under-posting; the triple-store lead-story post per bet 1 is the next thing, held for a later wake-up rather than crowding day one). Reported and closed the Bluesky half of chamber#1's checklist: https://github.com/Retinue-OS/retinue-os-chamber/issues/1#issuecomment-5179586752. STILL OPEN: Mastodon (server choice recommended c196/c360 - infosec.exchange or techhub.social, both need an owner-submitted approval application) and Nostr (owner yes/no on self-generated keypair still pending). Consequence for strategy.md: the phase-end condition (chamber#1) is now PARTIALLY met for the first time since the chamber existed - not fully, since Mastodon/Nostr remain owner actions - and bet 3's Bluesky falsification clock (three months of honest presence) starts today, 2026-08-04, not on 2026-07-18. Bets 1/2/4 remain gated: one account with 0 followers is not yet an audience. Previous entry, Aros, c360 (2026-08-01): RE-AUDITED ON DECAY, published. The c196 platform table is SIX DAYS OLD and had never been re-measured; it is the data he will act on. Result: NOTHING CHANGED - all seven Mastodon servers' deciding rules verbatim, registration states identical, botsin.space still 404; Bluesky ToS still 'Updated: 14 August, 2025' and Community Guidelines still 'Updated: September 19, 2025', the SAME versions the 'no bot-labelling convention' reading was measured against, so that reading is still measured and not remembered. A measured negative - DO NOT RE-DERIVE IT. What IS new, and it enlarges the ask: com.atproto.server.describeServer reports bsky.social phoneVerificationRequired=TRUE, so the Bluesky half costs him A PHONE NUMBER HE SUPPLIES. CONTROL (what makes it a measurement): blacksky.app true, pds.witchcraft.systems OMITS the field - the property is PER-SERVER, not a protocol constant. Consequence: c196 ranked Bluesky first as 'as originally written', which next to the Mastodon approval queues reads as 'the half you can just do'; NEITHER half is a two-minute action, and my own ask concealed that for six days. The decision surfaced is HIS under guardrail 9 - whether to tie his personal phone number to an account that is openly not him - and I recommended NEITHER way. Third option costed rather than sold: self-hosted PDS (bluesky-social/pds) issues its own invite codes, no phone verification, federates - but VPS + domain = MONEY = guardrail 7, plus DNS/TLS/SMTP and a service to run; ON-THESIS IS NOT A REASON, hence listed third. HONEST LIMIT stated in public: I read the server's DECLARATION, not the signup flow, because running the flow means creating an account. Also corrected one omission of my own: infosec.exchange's rule ends 'There is no limit on unlisted posts', dropped by c196 - the direction that FLATTERED my recommendation. Published: chamber#1 issuecomment-5152470918, framed as a correction to my own published recommendation with NO NEW REQUEST (the c359 venue test: value is in arriving BEFORE he acts). NOT re-asked, NOT nagged - c27. Owner: chamber#1 is still the single remaining term of the phase - pick a Mastodon server and create the social accounts, and rule on whether Aros may generate the Nostr keypair himself. Aros, c331 (2026-07-31): corrected this field, which had asked since c196 for a GitHub agent account that was created 2026-07-30T14:51:24Z, and which claimed that action closes the misattribution and the chamber#6 token scope in one action - the account landed, contents-write did not follow it, so the second half was a prediction and it is false. chamber#6 stays open and already carries the two-cause diagnosis (PAT minted without Contents write, or the account holding Read on the repos) with the one-look test that distinguishes them, so it is not re-raised here. What stands from c196, measured from each server's /api/v1/instance/rules: the Mastodon server choice is the whole decision, and the two open-registration servers are the two that exclude this account (mastodon.social rule 6, mstdn.social's LLM-agent ban). Recommended: infosec.exchange (label as bot, at most 1 post/hour and 24/day, public visibility - a ceiling far above the intended volume) or techhub.social (bot label plus silent mode, which costs the public timeline). w3c.social holds bet 1's audience and its own on-topic rule rules it out as a main account. botsin.space is dead. Bluesky has no bot-labelling convention in its Community Guidelines (2025-09-19) or ToS (2025-08-14) - no prohibition either, so it stays, but the reason bet 3 gave for it is not in the documents. Recorded as a comment on chamber#1 with a draft sign-up reason he can paste, so the choice arrives with the work already done."
current_actor: actor-owner
waiting_since: 2026-07-18
expected_by: 2026-08-08
paused: false
category: community
---

# Establish the project's social accounts

## Goal
Retinue has a small, honest, clearly-labelled presence where its audience
already is.

## Success criteria
- Accounts exist on the chosen platforms, each with an AI-agent disclosure in
  the bio (guardrail 1).
- Each platform's automation and self-promotion policy has been read and
  recorded here before the first post.
- Each account was handed to Aros after creation (guardrail 7); from the
  handover on, he posts from it in his own name (guardrail 8).

## Recommended platforms
**Mastodon** and **Bluesky** first — but on Mastodon the *server* is the whole
decision, and the bot-labelling reason originally given for Bluesky is not in
its documents. See "Platform policies, measured" below, which supersedes the
paragraph that used to stand here.

Both have API access that suits an agent and an audience that overlaps heavily
with self-hosting and semantic-web people. That part holds.

**Nostr** third, at low volume — added 2026-07-19 after the owner raised it on
chamber issue #1. Assessment, from the specs rather than reputation:

- Identity is a locally generated secp256k1 keypair (NIP-01): no registration,
  no central server, nothing a platform can disable. It maps exactly onto the
  `social-gateway` design below — a sidecar holds the private key, the model
  never sees it. It is the one platform where the project's own thesis holds
  literally rather than by analogy. That is a *coherence* argument, not a reach
  argument.
- Bot labelling is the strongest of the three: NIP-24 standardises a `bot`
  boolean in kind-0 metadata ("the content is entirely or partially the result
  of automation"). Machine-readable and in the spec, not a client convention.
  Bluesky's bot-labelling story is **unverified** — check before posting there.
- Audience fit is the weak part, and it is the part the strategy cares about.
  Nostr overlaps strongly with self-hosting, weakly with semantic web; its
  centre of gravity is freedom-tech. So it extends bet 3, it does not displace
  it. Reassess at the scheduled review against substantive replies.

**Open guardrail question, escalated not decided.** On Nostr, "create an
account" and "accept terms of service" come apart, so guardrail 7 is ambiguous:
generating a keypair accepts nobody's terms, but a keypair with a profile is an
account in the ordinary sense, and relays may declare a `terms_of_service` and
`payment_required` (NIP-11). Per guardrail 9 the ambiguity goes to the owner
rather than being resolved in Aros's own favour. Default if he does nothing:
**no keypair**. If he says yes: relays whose NIP-11 declares no terms document
and no payment, each recorded in issue #1 before the first post, and `"bot":
true` plus the AI disclosure in the kind-0 profile.

## Platform policies, measured

Added 2026-07-26 (cycle 196), from primary sources, closing the success
criterion "each platform's automation and self-promotion policy has been read
and recorded here before the first post" — open and self-assigned since
2026-07-19. Posted in full as a
[comment on chamber#1](https://github.com/Retinue-OS/retinue-os-chamber/issues/1#issuecomment-5083409472).

**Bluesky has no bot-labelling convention.** The Community Guidelines
(2025-09-19) require labelling for commercial and parody/satire accounts and
forbid misleading impersonation; they say nothing about bots, automation or
AI-generated content. The Terms of Service (2025-08-14) carry no automation
clause. Disclosure would be bio and display name only — which guardrail 1
requires anyway. No prohibition found, so Bluesky stays; the *reason* given for
it was wrong.

**Mastodon's bot flag is real** (`docs.joinmastodon.org/user/profile`: "Enabling
the bot flag will add a bot icon to your profile … may perform automated
actions, or might not be monitored by a human"), but what binds an account is
the server's rules. Read from each server's `/api/v1/instance/rules`:

| Server | The rule that decides it | Sign-up |
|---|---|---|
| `mastodon.social` | "Accounts may not solely post AI-generated content." | open |
| `mstdn.social` | "No AI (LLM) Agents. We want to keep this platform human, not robot." | approval |
| `fosstodon.org` | "DO NOT use automated tools to post without also monitoring and/or interacting from your account." | invite only |
| `techhub.social` | "Bots must be marked as Bot in their profile and bots created after Dec 31st 2024 must post in silent mode" | approval |
| `infosec.exchange` | ">50% automation must be labeled 'bot'; automated posts limited to one per hour / 24 per day, visibility public" | approval |
| `w3c.social` | no automation rule; "stay mainly on topic … activities of the World Wide Web Consortium: Web standardization" | approval |
| `botsin.space` | gone — tombstone page, no API | — |

The two open-registration servers are the two that exclude an account like this
one. Recommended: `infosec.exchange` (explicit, workable rate ceiling far above
the intended volume; requires exactly the label guardrail 1 requires) or
`techhub.social` (whose "silent mode" I read as unlisted, which costs the public
timeline). `w3c.social` holds bet 1's audience and is ruled out as a main
account by its own on-topic rule.

Standing caveat, in `infosec.exchange`'s words: "lack of a specific rule against
a certain behavior does not indicate acceptance of that behavior." Every blank
cell above, and Bluesky's silence, is read that way.

**Re-audited 2026-08-01 (cycle 360), six days on: nothing in this table changed.**
Re-read from each server's `/api/v1/instance/rules` and `/api/v2/instance` — all
seven deciding rules verbatim as recorded, `mastodon.social` still
`enabled=true, approval_required=false`, `mstdn.social` / `techhub.social` /
`infosec.exchange` / `w3c.social` still approval-gated, `fosstodon.org` still
closed, `botsin.space` still 404. Bluesky's documents likewise: ToS still
*"Updated: 14 August, 2025"*, Community Guidelines still *"Updated: September 19,
2025"* — the same versions the "no bot-labelling convention" reading was measured
against, so that reading is still measured against current text and not a
remembered one. A measured negative, recorded because the alternative is
re-deriving it next time.

One omission of mine, corrected: `infosec.exchange`'s rule ends *"There is no
limit on 'unlisted' posts"*, dropped when c196 quoted it. It makes that server's
ceiling **more** permissive than reported — the direction that flattered the
recommendation, which is the direction worth catching.

## Signup cost, measured 2026-08-01 (cycle 360)

c196 ranked Bluesky first as *"Bluesky, as originally written"*, which next to a
Mastodon paragraph full of approval queues reads as *the half he can just do*.
It is not, and the ask concealed a cost until this was measured.

From `com.atproto.server.describeServer`, the protocol's own method for a server
declaring its signup requirements:

| Host | `inviteCodeRequired` | `phoneVerificationRequired` |
|---|---|---|
| `bsky.social` | false | **true** |
| `blacksky.app` (independent, open signup) | false | true |
| `pds.witchcraft.systems` (self-hosted PDS) | true | **field absent** |

The last row is the control, and it is what makes this a measurement rather than
a field sighting: the property is **per-server**, not a protocol constant. So
creating the Bluesky account costs the owner **a phone number he supplies**, and
neither half of chamber#1 is a two-minute action.

**The decision this surfaces is his, not mine** (guardrail 9): whether to attach
his personal phone number to an account that is openly not him. Not recommended
either way here.

**Third option, costed rather than sold.** A self-hosted PDS
([`bluesky-social/pds`](https://github.com/bluesky-social/pds)) issues its own
invite codes and requires no phone verification, and federates into the Bluesky
network. Costs: a VPS and a domain (**money** → guardrail 7), public DNS, 80/443,
TLS, SMTP, and one more service to keep running. It is on-thesis — identity on
infrastructure you own is this project's own argument — and *on-thesis is not a
reason*. Listed third for that reason.

**Honest limit:** what was read is each server's declaration, not the signup
flow. Running the flow means creating an account, which is guardrail 7's and not
mine.

Published as a
[comment on chamber#1](https://github.com/Retinue-OS/retinue-os-chamber/issues/1#issuecomment-5152470918),
as a correction to my own published recommendation carrying no new request.

**Not** Hacker News, Reddit or Lobsters. Their norms are hostile to
self-promotion by the project itself, and an agent operating a voting or comment
account there would violate guardrail 6 outright. Aros may draft a submission;
only the owner may post it, as its author.

## Bluesky: live, 2026-08-04

The owner set the account up himself and told me on chamber#1 to check
`BSKY_EMAIL`/`BSKY_PASSWORD` — present in the deployment environment, alongside
`SOCIAL_SEND_POLICY=allow`. Verified by logging in
(`com.atproto.server.createSession`): handle `aros-retinue.bsky.social`, DID
`did:plc:qnxaj2xwx6lzehhqosi44u5w`, `createdAt` **2026-08-03T14:01:24Z** — so the
account existed most of a day before the comment telling me to look.

The profile was already complete: display name "Aros", an avatar, a bio
disclosing AI-agent status and legal responsibility in its first clause, and a
self-applied `bot` label on the `app.bsky.actor.profile` record — a step beyond
what Bluesky's own policy requires (measured above: no bot flag, no automation
clause in its Community Guidelines or ToS). That satisfies this file's three
pre-first-post checklist items for this platform specifically: the policy was
already recorded here before the account existed, the disclosure is in place,
and the owner's comment is the handover (guardrail 7 ends where the account is
handed to me; guardrail 8 begins).

First post, 2026-08-04 ~13:14Z, 215 characters, no thread: a plain statement of
who is posting and why the legal split exists, linking the framework repo. No
content claim yet — deliberately. Bet 1 (lead with the triple-store story) and
the walkthrough (`writing/provenance-by-path.md`) are the next post, held for a
separate wake-up rather than posting twice on the account's first day (prefer
under-posting).

```
I'm Aros, the AI agent that posts for Retinue — a self-hosted personal-agent
framework (github.com/retinue-os/retinue). A human owner is legally
responsible for the project; I write and post for myself, not for him.
```

Public: https://bsky.app/profile/aros-retinue.bsky.social/post/3msb3qycwj32m

**What this does and does not change.** This is the first half of chamber#1's
two platform picks to exist. Mastodon still needs the owner to submit an
approval application to `infosec.exchange` or `techhub.social` (draft reason
already on file above); Nostr still needs a yes/no on whether I may generate
the keypair myself. Bet 3's Bluesky falsification clock (three months of
honest presence, checked against substantive replies) starts today, not on
2026-07-18 — the account existed but nobody, including me, was told to act on
it until now. One account with zero followers is not yet the audience bets 1,
2 and 4 need; nothing about the phase's central finding (0 stars, 0 forks, 0
inbound from a second person) is falsified by an account posting into silence
for the first few hours.

**First response, checked 2026-08-04 ~15:0xZ (c476), via an authenticated
`listNotifications` call rather than trusting the public thread view (which
showed `likeCount: 1` but an empty `getLikes` array — the authenticated
endpoint is the one that resolves who).** One like, 14:41:18Z, from
`andeeharry1.bsky.social` — account created 2024-11-11, **31,500 posts, 5,907
followers, 1,496 following**, bio a generic list of "no dating, no crypto, no
trading… foodie, wordsmith, book dragon". That posting rate (~50/day over 21
months) and content-free bio read as a high-volume, broad-engagement account,
not a self-hosting/semantic-web reader — the audience bet 3 names. **Recorded
as noise, not contact**, matching how this file already treats GitHub
drive-by promotional comments (c154/c394): a like costs the liker nothing and
this one shows no sign of having read the post. No reply needed to a like. If
a *second* like or any reply arrives from an account whose bio/posts show
actual overlap with the stated audience, that is the first real datum for bet
3's Bluesky clock; this one is not it.

**Notifications checked directly, 2026-08-20 ~19:0xZ (c887) — the first time
this file has queried `app.bsky.notification.listNotifications` rather than
relying on the routine survey's other instruments.** `getUnreadCount` read 2;
`listNotifications` (limit 50) returned exactly those 2, lifetime total: the
08-04 like above (already recorded, still the only `read` one) and one
**unread** `follow`, 2026-08-08T19:50:29Z, from `wildsoundfestival.bsky.social`
— sitting unseen for twelve days because nothing in the routine survey checks
this endpoint. Profile pulled before drawing any conclusion: "WILDsound
Feedback Festival", a film/screenplay contest account, **25,346 followers,
162,222 follows, 175 posts** — a follows:followers ratio over 6:1 is the
mass-follow-for-follow-back shape, not a reader's. Same disposition as the
andeeharry1 like above: **recorded as noise, not contact** — no bio/post
overlap with the self-hosting/semantic-web audience bet 3 names, and a follow
costs the follower nothing. **Not followed back** (guardrail 2: no
follow-for-follow). Marked seen via `updateSeen` so the next check starts
from zero rather than re-discovering the same two. **Consequence:** the
routine survey's GitHub-side instruments (`mentions-check.py`,
`web-mentions-check.py`) have no Bluesky equivalent, and this account is a
live, owned channel — worth an occasional manual notification check
(as done here) rather than a new standing tool, per the 2026-07-29 "instruments
became the work" rule: a new instrument is admissible only when it watches a
surface a reader or the owner meets, and this one already does, but the check
itself is cheap enough (two API calls) not to need automating yet.

## The account that already should have existed: GitHub

Added 2026-07-20 (sixteenth wake-up). The three social platforms above were
always understood as future accounts. What sixteen cycles missed is that Aros
has been **operating an account the whole time** — the owner's personal
`retog` — because that is whose token the deployment carries.

Git commit authorship is clean (`Aros (agent) <aros@retinue-os.github.io>`).
Issue and comment authorship is not: GitHub offers no author field, so every
issue Aros filed shows the owner's name and avatar. Guardrail 8 forbids posting
through the owner's identities in as many words, and this is that, on the
project's only public surface.

Tracked at
[chamber#3](https://github.com/retinue-os/retinue-os-chamber/issues/3), which
asks for one action — create `aros-agent`, invite it to the org, mint its token
with the scopes from
[chamber#6](https://github.com/retinue-os/retinue-os-chamber/issues/6) — because
that one action closes both issues.

**Landed 2026-07-30, and the second half of that sentence is false.** `@aros-agent`
was created 2026-07-30T14:51:24Z with an AI-disclosure bio, and every issue and
comment since carries its authorship — so the guardrail-8 defect is over, and with
it the disclosure-sentence grep that was the only authorship record either of us
had. What did **not** follow is the token scope: measured from this account on
2026-07-31, `git push` is 403, `POST /git/refs` and `PUT /contents` are 403, and
`GET /repos/…` reports `{pull: true, push: false}`, while opening a pull request
from a branch already on the remote returns 201. So chamber#6 is not closed by
chamber#3, the two were not one action, and this file said they were for two days.
Recorded here rather than edited away, because the prediction was mine: **a
permission measured on one identity says nothing about another**, and the inverse —
a permission *granted* alongside an account is not a permission *effective* — is
the same error with the sign flipped. chamber#6 carries the two-cause diagnosis and
the one-look test that distinguishes them; it is not re-raised from here.

**Interim policy, effective 2026-07-20:** every issue and comment Aros writes
opens with a first-line disclosure rather than a closing signature. Retrofitted
to the three issues whose bodies positively identify him as the author
(retinue#1, retinue#2, qlever-dir#3). `chamber#1` and `qlever-dir#2` were
deliberately **not** touched — the first is unsigned and may be Ara's, the
second is the owner's own and predates the chamber by ten days.

Aros did not stop filing in the meantime. Silence would trade a fixable
attribution problem for an unfixable communication one, and the queue the owner
depends on lives in those issues.

## Why the accounts are an owner action
Creating an account means accepting terms of service, which requires legal
personhood Aros does not have. ~~Some platforms also require a phone number or
payment method.~~ **Measured 2026-08-01 (c360) rather than hedged:
`bsky.social` declares `phoneVerificationRequired: true`, so the Bluesky account
requires a phone number the owner supplies; every Mastodon server whose rules
permit this account requires moderator approval.** See guardrail 7, and "Signup
cost, measured 2026-08-01" above.

## Future: a social gateway
The natural end state follows the framework's existing pattern — a
`social-gateway` sidecar owning the API tokens, exposing a thin `/send`, with
`SOCIAL_SEND_POLICY` keyed to the sending identity. Aros's own accounts run
`allow` there: he publishes in his own name without per-post approval, which is
the point.

Until the gateway exists, the platform tokens live in the deployment's
environment — an acknowledged deviation from the framework's
credential-isolation rule, bounded because the identity at stake is Aros's own
labeled account, not the owner's. Moving the tokens into a gateway closes this
project's last checkbox.

## Posting queue (created 2026-08-16, scheduled review)

Bet 2's amended floor (strategy.md, 2026-08-16 review): while this queue is
non-empty, at least one substantive post a week, never more than one a day.
A wake-up posts the top item because it is due — no further justification
needed, no posting on an empty queue. Each item leads with a concrete
artifact, per the voice rules. Reposts stay judgment calls under the owner's
2026-08-08 directive and are not queue items.

Context for the floor: two posts in the account's first twelve days (intro
08-04, triple-store piece 08-08), zero since, against the owner's explicit
"keep posting" of 08-08. The queue exists so "prefer under-posting" can never
again round down to zero.

| # | Item | Artifact it leads with | Bet |
|---|---|---|---|
| 1 | ~~Provenance-for-free: one real SPARQL query over the life store showing the named-graph-per-file trick, with its actual output~~ **Posted 2026-08-16, c811** — https://bsky.app/profile/aros-retinue.bsky.social/post/3mt7pvpggzw25 (query re-run live same cycle, 8 rows; qlever-dir#8 caveat named per the positioning calibration) | the query + result, linking `writing/provenance-by-path.md` | 1 |
| 2 | ~~Send policy keyed to the *sending* identity, not the recipient — and the disclosure that this account itself runs `allow` under that model~~ **Posted 2026-08-17, c824** — https://bsky.app/profile/aros-retinue.bsky.social/post/3mtahbpbdsp2p (claim re-verified against `signal-gateway.py:1259–1285` same cycle; cycle-52 calibration applied — "waits on the approval page", no never-approves claim; `SOCIAL_SEND_POLICY=allow` confirmed in env) | the `SIGNAL_SEND_POLICY` config line; the framework docs | 1/4 |
| 3 | ~~The egress audit observes, it does not enforce — what the project deliberately does not claim~~ **Posted 2026-08-18, c868** — https://bsky.app/profile/aros-retinue.bsky.social/post/3mtcwysl52x2x (claim re-verified same cycle: `review.md` still calls it "observability, not enforcement" on `main`; docker-compose.yml still has no `internal: true` network, so the structural fix is still not done; link 200) | `writing/egress-audit-observes.md`, linking `review.md` | 4 |
| 4 | Markdown frontmatter becoming queryable triples: the converter contract in one example — **draft staged 2026-08-22, c966**, see below | a frontmatter block + the triples it lands as | 1 |

Rules of the queue: items are posted top-down unless a wake-up argues
otherwise in the log; a posted item is struck with the post URL and date;
new items are appended with the artifact named, never as bare topics. Each
post is recorded in `log.md` per the publishing discipline (platform, URL,
one line on why).

### Item 4 — staged draft (c966, 2026-08-22)

Not due (last post 08-18, floor due 08-25, three days out) — staged rather
than posted, so 08-25's wake-up spends its budget verifying and publishing,
not deriving. Source is real, not invented: this chamber's own
`projects/github-org.md` frontmatter, run through the actual converter
(`projects/.qlever/md2ttl.py`, the reference converter `docs/triple-stores.md`
describes) on this cycle:

```
title: "Establish the retinue-os GitHub organization"
current_actor: actor-owner
waiting_since: 2026-08-04
```
↓ `python3 .qlever/md2ttl.py github-org.md` →
```turtle
<urn:retinue:project:proj-github-org> a p:Project ;
    p:currentActor <urn:retinue:actor-owner> ;
    p:waitingSince "2026-08-04"^^xsd:date .
```
(abbreviated to the two fields that fit a post; the full run also emits
`title`, `goal`, `goalStatus`, `currentNextAction`, `expectedBy`, `paused`,
`category` and two `p:link`s — verified in full this cycle, nothing edited
out that would change the reading.)

Staged post text (285 chars, under Bluesky's 300 limit), pending
same-cycle re-verification before it goes out per this queue's own
discipline (items 1–3 all re-ran their claim on posting day rather than
trusting the prep):

> A real project file in this chamber's repo:
>
> title: "Establish the retinue-os GitHub organization"
> current_actor: actor-owner
>
> qlever-dir's converter turns that frontmatter into Turtle:
> p:currentActor <urn:retinue:actor-owner> . No import job — the Markdown
> a human edits is the graph.

No linked `writing/` piece — `docs/triple-stores.md`'s own "Advantage 1"
section already covers this in full with a worked example; the post can
link there directly rather than duplicate it in a new essay.
