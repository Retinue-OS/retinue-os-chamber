// Projects card — the promotion and community projects in flight, grouped into
// "Our move" and "Waiting on others".
//
// This is the live dashboard's projects card (webapp/components/projects.js)
// with two changes, both consequences of being a static mirror:
//  - it reads a baked JSON document from its `src` attribute instead of the
//    gateway's live GET /projects endpoint (which computes the answer with a
//    SPARQL query over the life triple store);
//  - the rows are plain elements rather than links, because there are no
//    per-project pages here to open, and nothing on this page is editable.
// The chrome, grouping, accent bar and typography are unchanged, including the
// card's habit of going frameless edge-to-edge on phones and picking up a
// border again on wider screens.

import { esc, fmtDate, stampHtml } from './base.js';

const CSS = `
  :host { display: block; }
  .card { padding: 2px; }
  @media (min-width: 700px) {
    .card {
      background: var(--card, #151922);
      border: 1px solid var(--line, rgba(231, 235, 242, .08));
      border-radius: var(--radius, 16px);
      padding: 14px 16px;
    }
  }
  header { display: flex; align-items: baseline; justify-content: space-between; gap: 8px; }
  h2 { font-size: .82rem; font-weight: 600; letter-spacing: .04em; text-transform: uppercase;
       color: var(--muted, #8b93a3); margin: 0 0 10px; }
  time { font-size: .72rem; color: var(--muted, #8b93a3); }
  time.stale { color: var(--high, #ff6b6b); }
  .muted { color: var(--muted, #8b93a3); margin: 4px 0; }
  .group-label { font-size: .72rem; font-weight: 600; letter-spacing: .04em;
       text-transform: uppercase; color: var(--muted, #8b93a3); margin: 14px 0 8px; }
  .group-label:first-of-type { margin-top: 2px; }
  ul { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 8px; }
  .row { display: block; padding: 8px 10px; border-radius: 10px;
         background: var(--card-2, #1c2230); }
  /* "Our move": accent bar on the left, like an unread/active marker. */
  li.mine .row { border-left: 3px solid var(--accent, #6ea8fe); }
  li.waiting .row { border-left: 3px solid transparent; }
  li.waiting { opacity: .92; }
  .title { color: var(--fg, #e7ebf2); font-weight: 600; }
  .meta { display: block; color: var(--muted, #8b93a3); font-size: .8rem; margin-top: 2px; }
  .next { display: block; color: var(--fg2, #c3cad6); font-size: .84rem; margin-top: 3px; }
`;

function projectLi(p, cls) {
  const bits = [];
  if (p.next) bits.push(`<span class="next">${esc(p.next)}</span>`);
  const meta = [];
  if (cls === 'waiting') {
    meta.push(p.waitingOn ? `Waiting on ${esc(p.waitingOn)}` : 'Waiting');
    if (p.since) meta.push(`since ${esc(fmtDate(p.since) || p.since)}`);
  } else if (p.expected) {
    meta.push(`Due ${esc(fmtDate(p.expected) || p.expected)}`);
  }
  if (meta.length) bits.push(`<span class="meta">${meta.join(' &middot; ')}</span>`);
  return `<li class="${cls}"><div class="row">` +
    `<span class="title">${esc(p.title)}</span>${bits.join('')}</div></li>`;
}

class RetinueProjects extends HTMLElement {
  connectedCallback() {
    if (!this.shadowRoot) this.attachShadow({ mode: 'open' });
    this.render({ state: 'loading' });
    this.load();
  }

  get dataUrl() { return this.getAttribute('src'); }
  get heading() { return this.getAttribute('heading') || 'Projects'; }

  async load() {
    try {
      const res = await fetch(this.dataUrl);
      if (!res.ok) throw new Error(String(res.status));
      this.render({ state: 'ok', data: await res.json() });
    } catch (_err) {
      this.render({ state: 'offline' });
    }
  }

  render({ state, data }) {
    let inner = '';
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
      `<style>${CSS}</style>` +
      `<section class="card"><header><h2>${esc(this.heading)}</h2>${stamp}</header>` +
      `<div class="content">${inner}</div></section>`;
  }

  body(d) {
    const mine = Array.isArray(d.mine) ? d.mine : [];
    const waiting = Array.isArray(d.waiting) ? d.waiting : [];
    if (!mine.length && !waiting.length) return '<p class="muted">No running projects.</p>';
    const out = [];
    if (mine.length) {
      out.push('<div class="group-label">Our move</div><ul>' +
        mine.map((p) => projectLi(p, 'mine')).join('') + '</ul>');
    }
    if (waiting.length) {
      out.push('<div class="group-label">Waiting on others</div><ul>' +
        waiting.map((p) => projectLi(p, 'waiting')).join('') + '</ul>');
    }
    return out.join('');
  }
}
customElements.define('retinue-projects', RetinueProjects);
