// Community card — the live dashboard's messages card, unchanged. Each item is
// a piece of recent community activity: the "from" slot names the event, the
// "channel" slot names where it happened, and the dot turns accent-red for the
// items that want a human answer.
import { RetinueCard, esc } from './base.js';

class RetinueMessages extends RetinueCard {
  css() {
    return `
      li { display: flex; gap: 10px; align-items: baseline; }
      .dot { width: 8px; height: 8px; border-radius: 50%; flex: 0 0 auto; margin-top: 6px;
             background: var(--muted, #8b93a3); }
      .dot.high { background: var(--high, #ff6b6b); }
      .who { font-weight: 600; }
      .chan { color: var(--muted, #8b93a3); font-size: .78rem; }
    `;
  }
  body(d) {
    const items = Array.isArray(d.items) ? d.items : [];
    if (!items.length) return '<p class="muted">No recent activity.</p>';
    return '<ul class="list">' + items.map((m) =>
      `<li><span class="dot ${m.importance === 'high' ? 'high' : ''}"></span>` +
      `<span><span class="who">${esc(m.from || '')}</span> ` +
      `<span class="chan">${esc(m.channel || '')}</span>` +
      `<small>${esc(m.preview || '')}</small></span></li>`
    ).join('') + '</ul>';
  }
}
customElements.define('retinue-messages', RetinueMessages);
