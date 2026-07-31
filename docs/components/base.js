// Shared base for the cards on the public Retinue dashboard.
//
// Copied from the live dashboard (webapp/components/base.js) and trimmed for a
// static mirror. The contract is unchanged: a card fetches one JSON document
// (its `src` attribute), renders it inside a styled <section>, and degrades to
// a quiet placeholder when the fetch fails. Subclasses override
// body(data) -> HTML string and optionally css() -> extra CSS string.
//
// One deliberate difference from the live dashboard: the timestamp slot shows
// an absolute date rather than a relative age. The live cards are regenerated
// continuously, so "12 min ago" is meaningful there; this page is a snapshot
// committed to a repository, and a relative age would only ever grow.
//
// That decision holds for the normal case and is kept. What it did not cover is
// the abnormal one, measured 2026-07-31: the served copies froze at
// 2026-07-30T02:37:42Z because the commits could not be pushed, and a reader
// comparing "30 Jul 2026" against today had no way to tell a normal daily
// snapshot from a delivery path that had broken. The date is honest and it is
// not sufficient. So the age is shown only once it passes the same 26 h bound
// `tools/delivery-check.py` fails the page at — silent while the page is
// current, explicit when it is not.
//
// The date is rendered in UTC, not in the reader's local zone. The `generated`
// stamps are written in UTC and the page header formats them that way; without
// the pin, a document generated between 00:00 and ~08:00 UTC renders one day
// earlier in every card for readers in the Americas, while the header still
// shows the UTC day. Same document, two dates on one screen.

export function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

export function fmtDate(iso) {
  const t = Date.parse(iso);
  if (Number.isNaN(t)) return '';
  return new Date(t).toLocaleDateString('en-GB', {
    day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC',
  });
}

// The chamber regenerates these five documents daily and `delivery-check.py`
// fails the served page at 26 h, so 26 h is the one bound both the instrument
// and the page use. Exported so a reader of either can see they are the same
// number rather than two copies that drift.
export const STALE_AFTER_MS = 26 * 60 * 60 * 1000;

// '' while the document is within the bound; otherwise a short age. Hours up to
// two days, then whole days — a page frozen for a week should say "7 days old",
// not "183 h old". A clock skewed into the future yields a negative age, which
// is below the bound and therefore silent: a wrong reader clock must not
// manufacture a staleness warning about a document that is in fact current.
export function staleLabel(iso, now = Date.now()) {
  const t = Date.parse(iso);
  if (Number.isNaN(t)) return '';
  const age = now - t;
  if (age < STALE_AFTER_MS) return '';
  const hours = Math.floor(age / 3600000);
  return hours < 48 ? `${hours} h old` : `${Math.floor(hours / 24)} days old`;
}

const STALE_TITLE =
  'Generated more than 26 hours ago. The daily regeneration, or its delivery ' +
  'to this page, has not completed.';

// The one place a card's timestamp is built, so the two render paths (this
// class and projects.js, which carries its own CSS) cannot disagree.
export function stampHtml(iso, now = Date.now()) {
  const date = fmtDate(iso);
  if (!date) return '';
  const stale = staleLabel(iso, now);
  if (!stale) return `<time>${esc(date)}</time>`;
  return `<time class="stale" title="${esc(STALE_TITLE)}">` +
         `${esc(date)} &middot; ${esc(stale)}</time>`;
}

const CARD_CSS = `
  :host { display: block; }
  .card {
    background: var(--card, #151922);
    border-radius: var(--radius, 16px);
    padding: 14px 16px;
  }
  header { display: flex; align-items: baseline; justify-content: space-between; gap: 8px; }
  h2 { font-size: .82rem; font-weight: 600; letter-spacing: .04em; text-transform: uppercase;
       color: var(--muted, #8b93a3); margin: 0 0 10px; }
  time { font-size: .72rem; color: var(--muted, #8b93a3); }
  time.stale { color: var(--high, #ff6b6b); }
  .content { color: var(--fg, #e7ebf2); }
  .muted { color: var(--muted, #8b93a3); margin: 4px 0; }
  ul.list { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 10px; }
  small { display: block; color: var(--muted, #8b93a3); font-size: .8rem; }
`;

export class RetinueCard extends HTMLElement {
  connectedCallback() {
    if (!this.shadowRoot) this.attachShadow({ mode: 'open' });
    this.renderState({ state: 'loading' });
    this.load();
  }

  get dataUrl() { return this.getAttribute('src'); }
  get heading() { return this.getAttribute('heading') || ''; }

  async load() {
    if (!this.dataUrl) { this.renderState({ state: 'ok', data: {} }); return; }
    try {
      const res = await fetch(this.dataUrl);
      if (!res.ok) throw new Error(String(res.status));
      const data = await res.json();
      this.renderState({ state: 'ok', data });
    } catch (_err) {
      this.renderState({ state: 'offline' });
    }
  }

  // Override in subclasses.
  body(_data) { return ''; }
  css() { return ''; }

  renderState({ state, data }) {
    let inner;
    let stamp = '';
    if (state === 'loading') {
      inner = '<p class="muted">&#8230;</p>';
    } else if (state === 'offline') {
      inner = '<p class="muted">Offline &ndash; no current data.</p>';
    } else {
      inner = this.body(data || {});
      if (data && data.generated) stamp = stampHtml(data.generated);
    }
    this.shadowRoot.innerHTML =
      `<style>${CARD_CSS}${this.css()}</style>` +
      `<section class="card"><header><h2>${esc(this.heading)}</h2>${stamp}</header>` +
      `<div class="content">${inner}</div></section>`;
  }
}
