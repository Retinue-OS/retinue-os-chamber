---
type: project
id: proj-social-presence
title: "Establish the project's social accounts"
goal: "Retinue has a small, honest, clearly-labelled presence where its audience already is."
goal_status: not_achieved
current_next_action: "Owner: decide which platforms, then create the accounts"
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
**Mastodon** and **Bluesky** first. Both have API access that suits an agent,
both have an audience that overlaps heavily with self-hosting and
semantic-web people, and both have clear bot-labelling conventions — which
matters when your pitch is honesty about what agents are.

**Not** Hacker News, Reddit or Lobsters. Their norms are hostile to
self-promotion by the project itself, and an agent operating a voting or comment
account there would violate guardrail 6 outright. Aros may draft a submission;
only the owner may post it, as its author.

## Why the accounts are an owner action
Creating an account means accepting terms of service, which requires legal
personhood Aros does not have. Some platforms also require a phone number or
payment method. See guardrail 7.

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
