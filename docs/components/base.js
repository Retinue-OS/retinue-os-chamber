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

export function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

export function fmtDate(iso) {
  const t = Date.parse(iso);
  if (Number.isNaN(t)) return '';
  return new Date(t).toLocaleDateString('en-GB', {
    day: 'numeric', month: 'short', year: 'numeric',
  });
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
      if (data && data.generated) stamp = `<time>${esc(fmtDate(data.generated))}</time>`;
    }
    this.shadowRoot.innerHTML =
      `<style>${CARD_CSS}${this.css()}</style>` +
      `<section class="card"><header><h2>${esc(this.heading)}</h2>${stamp}</header>` +
      `<div class="content">${inner}</div></section>`;
  }
}
