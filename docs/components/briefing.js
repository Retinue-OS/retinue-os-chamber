// Briefing card — unchanged from the live dashboard except that the audio
// element is dropped: this mirror ships no spoken rendering.
import { RetinueCard, esc } from './base.js';

class RetinueBriefing extends RetinueCard {
  css() {
    return `
      .b-title { font-weight: 600; margin: 0 0 6px; }
      .b-text { color: var(--fg, #e7ebf2); margin: 0; white-space: pre-line; }
    `;
  }
  body(d) {
    const title = d.title ? `<p class="b-title">${esc(d.title)}</p>` : '';
    const text = d.text ? `<p class="b-text">${esc(d.text)}</p>` : '';
    if (!title && !text) return '<p class="muted">No briefing.</p>';
    return title + text;
  }
}
customElements.define('retinue-briefing', RetinueBriefing);
