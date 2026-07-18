// Milestones card — the live dashboard's agenda card, verbatim in structure.
// On the personal dashboard the leading accent column is a clock time; here it
// is a short date, since these are dated project milestones rather than
// appointments in a single day.
import { RetinueCard, esc } from './base.js';

class RetinueAgenda extends RetinueCard {
  css() {
    return `
      li { display: flex; gap: 12px; align-items: baseline; }
      .time { font-variant-numeric: tabular-nums; color: var(--accent, #6ea8fe); font-weight: 600;
              min-width: 4.2em; }
    `;
  }
  body(d) {
    const events = Array.isArray(d.events) ? d.events : [];
    if (!events.length) return '<p class="muted">No dated milestones.</p>';
    return '<ul class="list">' + events.map((e) =>
      `<li><span class="time">${esc(e.time || '')}</span>` +
      `<span><strong>${esc(e.title || '')}</strong>` +
      (e.location ? `<small>${esc(e.location)}</small>` : '') +
      `</span></li>`
    ).join('') + '</ul>';
  }
}
customElements.define('retinue-agenda', RetinueAgenda);
