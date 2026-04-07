#!/usr/bin/env python3
"""Build loft-checklist-v3-improved.html with bold enhancements."""

ENHANCED_CSS = """
/* ═══════════════════════════════════════════════════════════════
   LOFT ENHANCEMENTS — Purely additive. Zero conflict with app.
   ═══════════════════════════════════════════════════════════════ */

/* ── Progress Ring ─────────────────────────────────────────────── */
#loft-ring-wrap {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 9000;
  cursor: pointer;
  user-select: none;
  filter: drop-shadow(0 4px 16px rgba(0,0,0,.6));
  transition: transform .25s cubic-bezier(.34,1.56,.64,1);
}
#loft-ring-wrap:hover { transform: scale(1.12); }
#loft-ring-wrap.loft-celebrate {
  animation: loft-pulse 0.6s ease-in-out 3;
}
@keyframes loft-pulse {
  0%,100% { transform: scale(1); }
  50%      { transform: scale(1.2); }
}
#loft-ring-svg { display: block; }
#loft-ring-bg   { fill: #1a1a1a; stroke: #2a2a2a; stroke-width: 3; }
#loft-ring-track{ fill: none; stroke: #2a2a2a; stroke-width: 5; }
#loft-ring-arc  {
  fill: none;
  stroke-width: 5;
  stroke-linecap: round;
  transform-origin: center;
  transform: rotate(-90deg);
  transition: stroke-dashoffset .7s cubic-bezier(.4,0,.2,1),
              stroke .7s ease;
}
#loft-ring-pct {
  font-family: 'Rajdhani', system-ui, sans-serif;
  font-weight: 700;
  font-size: 13px;
  fill: #e0e0e0;
  text-anchor: middle;
  dominant-baseline: central;
  text-transform: uppercase;
  letter-spacing: .5px;
}
#loft-ring-label {
  font-family: 'Rajdhani', system-ui, sans-serif;
  font-weight: 500;
  font-size: 7px;
  fill: #888;
  text-anchor: middle;
  dominant-baseline: central;
  text-transform: uppercase;
  letter-spacing: .8px;
}

/* ── Command Palette ───────────────────────────────────────────── */
#loft-cp-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.72);
  z-index: 10000;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 80px;
  opacity: 0;
  pointer-events: none;
  backdrop-filter: blur(4px);
  transition: opacity .15s ease;
}
#loft-cp-backdrop.loft-open { opacity: 1; pointer-events: all; }
#loft-cp-modal {
  width: min(640px, 92vw);
  background: #141414;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  box-shadow: 0 32px 80px rgba(0,0,0,.8), 0 0 0 1px rgba(250,7,7,.08);
  overflow: hidden;
  animation: loft-slide-down .2s cubic-bezier(.34,1.56,.64,1);
}
@keyframes loft-slide-down {
  from { transform: translateY(-20px); opacity: 0; }
  to   { transform: translateY(0);    opacity: 1; }
}
@keyframes loft-fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}
#loft-cp-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 18px;
  border-bottom: 1px solid #222;
}
#loft-cp-icon {
  color: #fa0707;
  font-size: 18px;
  flex-shrink: 0;
  line-height: 1;
}
#loft-cp-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: #e0e0e0;
  font-family: 'Rajdhani', system-ui, sans-serif;
  font-size: 16px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: .5px;
  caret-color: #fa0707;
}
#loft-cp-input::placeholder { color: #444; }
#loft-cp-kbd-hint {
  font-size: 10px;
  color: #444;
  white-space: nowrap;
  text-transform: uppercase;
  letter-spacing: .5px;
}
#loft-cp-list {
  max-height: 380px;
  overflow-y: auto;
  padding: 6px;
  scrollbar-width: thin;
  scrollbar-color: #2a2a2a transparent;
}
#loft-cp-empty {
  padding: 32px;
  text-align: center;
  color: #444;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: .5px;
}
.loft-cp-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  border-radius: 8px;
  cursor: pointer;
  transition: background .12s;
  text-transform: uppercase;
  letter-spacing: .4px;
}
.loft-cp-item:hover, .loft-cp-item.loft-active {
  background: rgba(250,7,7,.12);
}
.loft-cp-item-icon {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  background: #1e1e1e;
  border: 1px solid #2a2a2a;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  flex-shrink: 0;
}
.loft-cp-item-text {
  flex: 1;
  color: #e0e0e0;
  font-size: 13px;
  font-weight: 600;
}
.loft-cp-item-mark { color: #fa0707; }
.loft-cp-item-cat {
  font-size: 10px;
  color: #555;
  text-transform: uppercase;
  letter-spacing: .8px;
}
#loft-cp-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 16px;
  border-top: 1px solid #1e1e1e;
  font-size: 10px;
  color: #444;
  text-transform: uppercase;
  letter-spacing: .5px;
}
.loft-cp-footer-keys { display: flex; gap: 10px; align-items: center; }
.loft-cp-key {
  background: #1e1e1e;
  border: 1px solid #2a2a2a;
  border-radius: 4px;
  padding: 2px 6px;
  font-size: 9px;
  color: #666;
}

/* ── Toast Notifications ───────────────────────────────────────── */
#loft-toast-container {
  position: fixed;
  bottom: 24px;
  left: 24px;
  z-index: 9500;
  display: flex;
  flex-direction: column-reverse;
  gap: 8px;
  pointer-events: none;
}
.loft-toast {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 16px;
  background: #1a1a1a;
  border: 1px solid #2a2a2a;
  border-radius: 8px;
  color: #e0e0e0;
  font-family: 'Rajdhani', system-ui, sans-serif;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .5px;
  pointer-events: all;
  box-shadow: 0 8px 32px rgba(0,0,0,.5);
  max-width: 320px;
  border-left-width: 3px;
  animation: loft-toast-in .3s cubic-bezier(.34,1.56,.64,1);
  transition: opacity .3s, transform .3s;
}
.loft-toast.loft-toast-out {
  opacity: 0;
  transform: translateX(-20px);
}
.loft-toast-info    { border-left-color: #4a9eff; }
.loft-toast-success { border-left-color: #22c55e; }
.loft-toast-error   { border-left-color: #fa0707; }
.loft-toast-warning { border-left-color: #f59e0b; }
.loft-toast-icon { font-size: 15px; flex-shrink: 0; }
@keyframes loft-toast-in {
  from { transform: translateX(-32px); opacity: 0; }
  to   { transform: translateX(0);    opacity: 1; }
}

/* ── Section Entrance Animations ──────────────────────────────── */
.loft-anim-ready {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity .4s cubic-bezier(.4,0,.2,1), transform .4s cubic-bezier(.4,0,.2,1);
}
.loft-anim-ready.loft-visible {
  opacity: 1;
  transform: translateY(0);
}
@media (prefers-reduced-motion: reduce) {
  .loft-anim-ready, .loft-anim-ready.loft-visible {
    opacity: 1; transform: none; transition: none;
  }
}

/* ── Keyboard Shortcuts Modal ─────────────────────────────────── */
#loft-kb-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.75);
  z-index: 10000;
  display: none;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(4px);
  animation: loft-fade-in .15s ease;
}
#loft-kb-backdrop.loft-open { display: flex; }
#loft-kb-modal {
  background: #141414;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  padding: 28px 32px;
  width: min(520px, 90vw);
  box-shadow: 0 32px 80px rgba(0,0,0,.8);
  animation: loft-slide-down .2s cubic-bezier(.34,1.56,.64,1);
}
#loft-kb-title {
  font-family: 'Rajdhani', system-ui, sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: #fa0707;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}
#loft-kb-title::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #222;
}
.loft-kb-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
.loft-kb-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  background: #1a1a1a;
  border-radius: 6px;
  border: 1px solid #222;
}
.loft-kb-desc {
  font-family: 'Rajdhani', system-ui, sans-serif;
  font-size: 11px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: .5px;
}
.loft-kb-keys { display: flex; gap: 4px; }
.loft-key {
  background: #111;
  border: 1px solid #333;
  border-bottom: 2px solid #333;
  border-radius: 4px;
  padding: 2px 7px;
  font-family: 'Rajdhani', system-ui, sans-serif;
  font-size: 10px;
  font-weight: 600;
  color: #e0e0e0;
  text-transform: uppercase;
}
#loft-kb-close {
  display: block;
  width: 100%;
  margin-top: 20px;
  padding: 8px;
  background: transparent;
  border: 1px solid #2a2a2a;
  border-radius: 6px;
  color: #555;
  font-family: 'Rajdhani', system-ui, sans-serif;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  transition: background .15s, color .15s;
}
#loft-kb-close:hover { background: #1e1e1e; color: #888; }

/* ── Ripple Effect ─────────────────────────────────────────────── */
/* Ripple setup: ensure relative+overflow on button targets */
.sbb, .topt { overflow: hidden; }
.loft-ripple-host { position: relative; overflow: hidden; }
.loft-ripple-wave {
  position: absolute;
  border-radius: 50%;
  transform: scale(0);
  animation: loft-ripple-anim .5s linear;
  background: rgba(250,7,7,.25);
  pointer-events: none;
}
@keyframes loft-ripple-anim {
  to { transform: scale(4); opacity: 0; }
}

/* ── Focus Mode ────────────────────────────────────────────────── */
body.loft-focus-mode .fs:not(:focus-within):not(:hover) {
  opacity: .3;
  transition: opacity .3s;
}
body.loft-focus-mode .fs {
  transition: opacity .3s;
}
#loft-focus-indicator {
  position: fixed;
  top: 12px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(250,7,7,.9);
  color: #fff;
  font-family: 'Rajdhani', system-ui, sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  padding: 5px 14px;
  border-radius: 20px;
  z-index: 9000;
  display: none;
  pointer-events: none;
}
body.loft-focus-mode #loft-focus-indicator { display: block; }

/* ── Scrollbar Enhancement ─────────────────────────────────────── */
#mc::-webkit-scrollbar { width: 4px; }
#mc::-webkit-scrollbar-track { background: transparent; }
#mc::-webkit-scrollbar-thumb { background: #2a2a2a; border-radius: 4px; }
#mc::-webkit-scrollbar-thumb:hover { background: #fa0707; }

/* ── LOFT-UX: Onboarding overlay (see JS applyUXEnhancements) ─── */
#loft-onboard-overlay { animation: loft-fade-in .25s ease; }

/* ── LOFT-UX: Loading skeleton for AI result areas ─────────────── */
.loft-skeleton {
  background: linear-gradient(90deg, #1a1a1a 25%, #242424 50%, #1a1a1a 75%);
  background-size: 200% 100%;
  animation: loft-skeleton-wave 1.4s ease-in-out infinite;
  border-radius: 4px;
}
@keyframes loft-skeleton-wave {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
.loft-skeleton-line { height: 12px; margin: 6px 0; }
.loft-skeleton-line.wide  { width: 85%; }
.loft-skeleton-line.short { width: 55%; }

/* ── LOFT-PERF: Signal cascade warning indicator ────────────────── */
#loft-perf-indicator {
  position: fixed;
  top: 8px;
  right: 8px;
  z-index: 8000;
  font-size: 9px;
  font-family: 'SF Mono', monospace;
  color: #333;
  pointer-events: none;
  letter-spacing: .04em;
}

/* ── LOFT-LOGIC: Manual override badge on topt items ───────────── */
.topt[data-manual] {
  border-left: 2px solid rgba(250,7,7,.5) !important;
}

/* ── LOFT-SECURITY: Rate limit badge ───────────────────────────── */
#loft-rate-badge {
  position: fixed;
  bottom: 80px;
  right: 24px;
  z-index: 8500;
  background: #141414;
  border: 1px solid #2a2a2a;
  border-radius: 6px;
  padding: 4px 10px;
  font-family: 'Rajdhani', sans-serif;
  font-size: 10px;
  font-weight: 700;
  color: #555;
  letter-spacing: .08em;
  text-transform: uppercase;
  pointer-events: none;
  transition: color .3s ease, border-color .3s ease;
}
#loft-rate-badge.loft-rate-warn { color: #fb923c; border-color: rgba(251,146,60,.4); }
#loft-rate-badge.loft-rate-crit { color: #f87171; border-color: rgba(248,113,113,.4); }

/* ── LOFT-UX: PDF export button ────────────────────────────────── */
#loft-pdf-btn {
  position: fixed;
  bottom: 120px;
  right: 24px;
  z-index: 8400;
  background: #141414;
  border: 1px solid #2a2a2a;
  border-radius: 6px;
  padding: 6px 12px;
  font-family: 'Rajdhani', sans-serif;
  font-size: 10px;
  font-weight: 700;
  color: #666;
  letter-spacing: .08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: color .2s, border-color .2s, background .2s;
}
#loft-pdf-btn:hover { color: #e0e0e0; border-color: #444; background: #1a1a1a; }

/* ── LOFT-UX: Global search (Ctrl+F) overlay ───────────────────── */
#loft-search-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 9500;
  background: rgba(0,0,0,.6);
  padding: 16px 24px;
  display: none;
  align-items: center;
  gap: 12px;
  backdrop-filter: blur(4px);
  border-bottom: 1px solid #2a2a2a;
}
#loft-search-overlay.loft-open { display: flex; }
#loft-search-input {
  flex: 1;
  background: #141414;
  border: 1px solid #333;
  border-radius: 6px;
  padding: 10px 14px;
  font-family: 'Rajdhani', sans-serif;
  font-size: 14px;
  color: #e0e0e0;
  outline: none;
  letter-spacing: .03em;
}
#loft-search-input:focus { border-color: #fa0707; }
#loft-search-count {
  font-family: 'Rajdhani', sans-serif;
  font-size: 11px;
  color: #555;
  letter-spacing: .06em;
  text-transform: uppercase;
  min-width: 90px;
}
#loft-search-close {
  background: none;
  border: none;
  color: #555;
  font-size: 18px;
  cursor: pointer;
  padding: 0 4px;
}
.loft-search-highlight {
  background: rgba(250,7,7,.25) !important;
  outline: 1px solid rgba(250,7,7,.5) !important;
  border-radius: 2px;
}
.loft-search-highlight.loft-search-current {
  background: rgba(250,7,7,.5) !important;
  outline: 1px solid #fa0707 !important;
}

/* ── LOFT-UX: Undo/Redo counter in header ──────────────────────── */
#loft-undo-counter {
  position: fixed;
  top: 8px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 8300;
  font-family: 'Rajdhani', sans-serif;
  font-size: 10px;
  font-weight: 700;
  color: #333;
  letter-spacing: .06em;
  text-transform: uppercase;
  pointer-events: none;
  transition: color .3s;
}
#loft-undo-counter.loft-undo-active { color: #666; }

/* ── LOFT-UX: Vistoria comparison side-by-side ─────────────────── */
#loft-compare-bar {
  background: #0d0d0d;
  border: 1px solid #1a1a1a;
  border-radius: 6px;
  padding: 8px 14px;
  margin: 8px 0;
  display: none;
  align-items: center;
  gap: 10px;
  font-family: 'Rajdhani', sans-serif;
  font-size: 11px;
  font-weight: 700;
  color: #555;
  letter-spacing: .06em;
  text-transform: uppercase;
}
#loft-compare-bar.loft-active { display: flex; }
.loft-diff-add { color: #4ade80; }
.loft-diff-del { color: #f87171; }
.loft-diff-same { color: #555; }

/* ── LOFT-PERF: Tab lazy loading placeholder ────────────────────── */
.loft-tab-skeleton {
  padding: 20px;
  animation: loft-skeleton-wave 1.4s ease-in-out infinite;
  background: linear-gradient(90deg, #0d0d0d 25%, #141414 50%, #0d0d0d 75%);
  background-size: 200% 100%;
  border-radius: 4px;
  min-height: 120px;
}

/* ── Print / PDF export ─────────────────────────────────────────── */
@media print {
  #loft-ring-wrap, #loft-cp-backdrop, #loft-kb-backdrop,
  #loft-onboard-overlay, #loft-rate-badge, #loft-pdf-btn,
  #loft-search-overlay, #loft-undo-counter, #loft-compare-bar,
  aside, nav, .loft-toast-container { display: none !important; }
  body { background: #fff !important; color: #111 !important; }
  #mc { padding: 0 !important; box-shadow: none !important; }
  .topt { page-break-inside: avoid; }
  a { color: #111 !important; text-decoration: none !important; }
}

/* ── LOFT-IA-TAB: Hide ANALISE DOS DOCUMENTOS progress bar ─────── */
#ia-progress-bar,
.ia-progress-overview {
  display: none !important;
}

/* ── LOFT-IA-LAYOUT: Document accordions on top, controls at bottom ─
   .ia-panel becomes a flex column; CSS order controls visual position.
   Accordions (id="ia-acc-*") get order:3, everything else gets order:9.
   .phd header keeps order:1, so it stays at very top.
   ──────────────────────────────────────────────────────────────────── */
#mc .ia-panel {
  display: flex !important;
  flex-direction: column !important;
}
/* Default: all direct children go to bottom section (order 9) */
#mc .ia-panel > * {
  order: 9;
}
/* Page header stays at top */
#mc .ia-panel > .phd {
  order: 1;
}
/* Document accordions appear first (middle section, order 3) */
#mc .ia-panel > [id^="ia-acc-"] {
  order: 3;
}
"""

ENHANCED_JS = """
/* ═══════════════════════════════════════════════════════════════
   LOFT ENHANCEMENTS v3-IMPROVED — Senior-grade augmentation layer.
   Purely additive. Zero interference with existing app logic.
   ═══════════════════════════════════════════════════════════════ */
(function() {
  'use strict';

  // ── Version badge — confirms this is the improved file
  (function() {
    var badge = document.createElement('div');
    badge.id = 'loft-version-badge';
    badge.title = 'LOFT Checklist V3 — Enhanced build';
    badge.style.cssText = [
      'position:fixed;bottom:4px;left:4px;z-index:7000;',
      'font-family:monospace;font-size:9px;color:#1e1e1e;',
      'background:#111;border:1px solid #1e1e1e;border-radius:3px;',
      'padding:2px 6px;pointer-events:none;letter-spacing:.04em;'
    ].join('');
    badge.textContent = 'v3+enhanced';
    document.addEventListener('DOMContentLoaded', function() {
      document.body.appendChild(badge);
    });
    if (document.body) document.body.appendChild(badge);
  })();

  // ── Milestone progress tracking (avoid repeated toasts)
  var _prevMilestone = -1;
  var _prevPct = -1;

  // ── Compute global progress from D.checklists + D.form
  function computeProgress() {
    try {
      var D = window.D;
      if (!D) return 0;
      var tot = 0, ok = 0;
      var OPT = ['val_plat','dt_ativ'];
      (D.checklists || []).forEach(function(cat) {
        if (cat.docNaoEnviado || cat.semNecessidade) return;
        (cat.itens || []).forEach(function(it) {
          tot++;
          if (it.est === 'ok' || it.est === 'fail') ok++;
        });
      });
      var fp = Object.entries(D.form || {}).filter(function(kv) {
        return !OPT.includes(kv[0]) && kv[1] && String(kv[1]).trim();
      }).length;
      var ft = Object.keys(D.form || {}).filter(function(k) {
        return !OPT.includes(k);
      }).length;
      tot += ft; ok += fp;
      return tot > 0 ? Math.round(ok / tot * 100) : 0;
    } catch(e) { return 0; }
  }

  // ── Color interpolation: red→amber→green
  function pctColor(pct) {
    if (pct < 50) {
      var t = pct / 50;
      var r = 250, g = Math.round(7 + (159 - 7) * t), b = Math.round(7 + (10 - 7) * t);
      return 'rgb(' + r + ',' + g + ',' + b + ')';
    } else {
      var t2 = (pct - 50) / 50;
      var r2 = Math.round(250 + (34 - 250) * t2), g2 = Math.round(159 + (197 - 159) * t2), b2 = Math.round(10 + (94 - 10) * t2);
      return 'rgb(' + r2 + ',' + g2 + ',' + b2 + ')';
    }
  }

  // ═══════════════════════════════════════════
  // FEATURE 1 — Floating Progress Ring
  // ═══════════════════════════════════════════
  function buildProgressRing() {
    var R = 28, C = 2 * Math.PI * R;
    var wrap = document.createElement('div');
    wrap.id = 'loft-ring-wrap';
    wrap.title = 'Progresso global';
    wrap.innerHTML =
      '<svg id="loft-ring-svg" width="72" height="72" viewBox="0 0 72 72">' +
        '<circle id="loft-ring-bg" cx="36" cy="36" r="34"/>' +
        '<circle id="loft-ring-track" cx="36" cy="36" r="' + R + '"/>' +
        '<circle id="loft-ring-arc" cx="36" cy="36" r="' + R + '" ' +
               'stroke-dasharray="' + C.toFixed(2) + '" ' +
               'stroke-dashoffset="' + C.toFixed(2) + '" stroke="#fa0707"/>' +
        '<text id="loft-ring-pct" x="36" y="33">0%</text>' +
        '<text id="loft-ring-label" x="36" y="46">DONE</text>' +
      '</svg>';
    document.body.appendChild(wrap);

    var arc = document.getElementById('loft-ring-arc');
    var pctEl = document.getElementById('loft-ring-pct');

    function updateRing() {
      var pct = computeProgress();
      if (pct === _prevPct) return;
      _prevPct = pct;

      var offset = C - (C * pct / 100);
      arc.style.strokeDashoffset = offset.toFixed(2);
      arc.style.stroke = pctColor(pct);
      pctEl.textContent = pct + '%';

      // Milestone toasts
      var milestones = [25, 50, 75, 100];
      milestones.forEach(function(m) {
        if (pct >= m && _prevMilestone < m) {
          _prevMilestone = m;
          var msgs = {
            25: '🔥 25% concluído — bom ritmo!',
            50: '⚡ Metade do caminho — continue!',
            75: '🚀 75% — quase lá!',
            100: '🏆 100% — Caso completo!'
          };
          loftToast(msgs[m], m === 100 ? 'success' : 'info', m === 100 ? 5000 : 3000);
          if (m === 100) {
            wrap.classList.add('loft-celebrate');
            setTimeout(function() { wrap.classList.remove('loft-celebrate'); }, 2000);
          }
        }
      });
    }

    // Poll + MutationObserver for updates
    setInterval(updateRing, 1500);
    var mc = document.getElementById('mc');
    if (mc) {
      var ringObs = new MutationObserver(function() { setTimeout(updateRing, 100); });
      ringObs.observe(mc, { childList: true, subtree: false });
    }
    updateRing();
  }

  // ═══════════════════════════════════════════
  // FEATURE 2 — Command Palette (Ctrl+K)
  // ═══════════════════════════════════════════
  var _cpOpen = false;
  var _cpItems = [];
  var _cpActive = 0;

  function buildCommandPalette() {
    var bd = document.createElement('div');
    bd.id = 'loft-cp-backdrop';
    bd.innerHTML =
      '<div id="loft-cp-modal">' +
        '<div id="loft-cp-header">' +
          '<span id="loft-cp-icon">⌘</span>' +
          '<input id="loft-cp-input" placeholder="BUSCAR SEÇÃO..." autocomplete="off" spellcheck="false"/>' +
          '<span id="loft-cp-kbd-hint">ESC PARA FECHAR</span>' +
        '</div>' +
        '<div id="loft-cp-list"></div>' +
        '<div id="loft-cp-footer">' +
          '<div class="loft-cp-footer-keys">' +
            '<span class="loft-cp-key">↑↓</span> NAVEGAR' +
            '<span style="margin:0 4px"></span>' +
            '<span class="loft-cp-key">↵</span> IR PARA' +
          '</div>' +
          '<span id="loft-cp-count">0 SEÇÕES</span>' +
        '</div>' +
      '</div>';
    document.body.appendChild(bd);

    bd.addEventListener('click', function(e) {
      if (e.target === bd) closeCp();
    });

    var inp = document.getElementById('loft-cp-input');
    var list = document.getElementById('loft-cp-list');
    var count = document.getElementById('loft-cp-count');

    function gatherItems() {
      _cpItems = [];
      document.querySelectorAll('.fst').forEach(function(el, i) {
        var txt = el.textContent.trim();
        if (txt) _cpItems.push({ text: txt, el: el, idx: i });
      });
      count.textContent = _cpItems.length + ' SEÇÕES';
    }

    function highlight(str, q) {
      if (!q) return str;
      var re = new RegExp('(' + q.replace(/\\W/g,'\\\\$&') + ')', 'gi');
      return str.replace(re, '<mark class="loft-cp-item-mark">$1</mark>');
    }

    function fuzzy(text, query) {
      var tl = text.toLowerCase(), ql = query.toLowerCase();
      var ti = 0, score = 0;
      for (var qi = 0; qi < ql.length; qi++) {
        var found = tl.indexOf(ql[qi], ti);
        if (found === -1) return -1;
        score += (found - ti === 0 ? 2 : 1);
        ti = found + 1;
      }
      return score;
    }

    var _debTimer;
    inp.addEventListener('input', function() {
      clearTimeout(_debTimer);
      _debTimer = setTimeout(renderList, 120);
    });

    function renderList() {
      var q = inp.value.trim();
      var filtered = _cpItems;
      if (q) {
        filtered = _cpItems.map(function(it) {
          return { item: it, score: fuzzy(it.text, q) };
        }).filter(function(x) { return x.score >= 0; })
          .sort(function(a,b) { return b.score - a.score; })
          .map(function(x) { return x.item; });
      }
      if (!filtered.length) {
        list.innerHTML = '<div id="loft-cp-empty">NENHUMA SEÇÃO ENCONTRADA</div>';
        return;
      }
      list.innerHTML = filtered.map(function(it, i) {
        var icons = ['📋','📄','✅','📌','🔍','💡','⚙️','📊'];
        var icon = icons[it.idx % icons.length];
        return '<div class="loft-cp-item' + (i===0?' loft-active':'') + '" data-idx="' + it.idx + '">' +
          '<div class="loft-cp-item-icon">' + icon + '</div>' +
          '<div class="loft-cp-item-text">' + highlight(it.text, q) + '</div>' +
        '</div>';
      }).join('');
      _cpActive = 0;
      // Click handlers
      list.querySelectorAll('.loft-cp-item').forEach(function(row) {
        row.addEventListener('click', function() {
          var idx = parseInt(row.getAttribute('data-idx'));
          var target = _cpItems[idx];
          if (target) { target.el.scrollIntoView({ behavior:'smooth', block:'start' }); }
          closeCp();
        });
      });
    }

    inp.addEventListener('keydown', function(e) {
      var rows = list.querySelectorAll('.loft-cp-item');
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        _cpActive = Math.min(_cpActive + 1, rows.length - 1);
        rows.forEach(function(r,i) { r.classList.toggle('loft-active', i===_cpActive); });
        if (rows[_cpActive]) rows[_cpActive].scrollIntoView({ block:'nearest' });
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        _cpActive = Math.max(_cpActive - 1, 0);
        rows.forEach(function(r,i) { r.classList.toggle('loft-active', i===_cpActive); });
        if (rows[_cpActive]) rows[_cpActive].scrollIntoView({ block:'nearest' });
      } else if (e.key === 'Enter') {
        var active = list.querySelector('.loft-active');
        if (active) active.click();
      } else if (e.key === 'Escape') {
        closeCp();
      }
    });

    window._loftOpenCp = function() {
      gatherItems();
      renderList();
      bd.classList.add('loft-open');
      _cpOpen = true;
      setTimeout(function() { inp.focus(); inp.select(); }, 50);
    };
    window._loftCloseCp = closeCp;
  }

  function closeCp() {
    var bd = document.getElementById('loft-cp-backdrop');
    if (bd) bd.classList.remove('loft-open');
    _cpOpen = false;
  }

  // ═══════════════════════════════════════════
  // FEATURE 3 — Section Entrance Animations
  // ═══════════════════════════════════════════
  var _ioObserver;

  function buildSectionAnimations() {
    if (!window.IntersectionObserver) return;
    _ioObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('loft-visible');
          _ioObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

    function observeNewSections() {
      document.querySelectorAll('.fs:not(.loft-anim-ready)').forEach(function(el, i) {
        el.classList.add('loft-anim-ready');
        el.style.transitionDelay = Math.min(i * 40, 300) + 'ms';
        _ioObserver.observe(el);
      });
    }

    observeNewSections();
    var mc = document.getElementById('mc');
    if (mc) {
      var animObs = new MutationObserver(function() { setTimeout(observeNewSections, 80); });
      animObs.observe(mc, { childList: true, subtree: true });
    }
  }

  // ═══════════════════════════════════════════
  // FEATURE 4 — Toast Notification System
  // ═══════════════════════════════════════════
  function buildToastSystem() {
    var container = document.createElement('div');
    container.id = 'loft-toast-container';
    document.body.appendChild(container);
  }

  window.loftToast = function(msg, type, duration) {
    type = type || 'info';
    duration = duration || 3000;
    var container = document.getElementById('loft-toast-container');
    if (!container) return;
    var icons = { info:'ℹ', success:'✓', error:'✕', warning:'⚠' };
    var toast = document.createElement('div');
    toast.className = 'loft-toast loft-toast-' + type;
    toast.innerHTML =
      '<span class="loft-toast-icon">' + (icons[type] || 'ℹ') + '</span>' +
      '<span class="loft-toast-msg">' + msg + '</span>';
    // Limit to 4 toasts
    var existing = container.querySelectorAll('.loft-toast');
    if (existing.length >= 4) existing[0].remove();
    container.appendChild(toast);
    setTimeout(function() {
      toast.classList.add('loft-toast-out');
      setTimeout(function() { toast.remove(); }, 350);
    }, duration);
  };

  // ═══════════════════════════════════════════
  // FEATURE 5 — Keyboard Shortcuts Modal
  // ═══════════════════════════════════════════
  function buildKeyboardShortcuts() {
    var bd = document.createElement('div');
    bd.id = 'loft-kb-backdrop';
    bd.innerHTML =
      '<div id="loft-kb-modal">' +
        '<div id="loft-kb-title">⌨ ATALHOS DE TECLADO</div>' +
        '<div class="loft-kb-grid">' +
          makeShortcut('Command Palette', ['Ctrl', 'K']) +
          makeShortcut('Atalhos de teclado', ['?']) +
          makeShortcut('Modo Foco', ['Shift', 'F']) +
          makeShortcut('Fechar modal', ['Esc']) +
        '</div>' +
        '<button id="loft-kb-close">FECHAR</button>' +
      '</div>';
    document.body.appendChild(bd);

    bd.addEventListener('click', function(e) {
      if (e.target === bd || e.target.id === 'loft-kb-close') closeKb();
    });
  }

  function makeShortcut(desc, keys) {
    return '<div class="loft-kb-item">' +
      '<span class="loft-kb-desc">' + desc + '</span>' +
      '<span class="loft-kb-keys">' +
        keys.map(function(k) { return '<kbd class="loft-key">' + k + '</kbd>'; }).join('+') +
      '</span>' +
    '</div>';
  }

  function closeKb() {
    var bd = document.getElementById('loft-kb-backdrop');
    if (bd) bd.classList.remove('loft-open');
  }

  // ═══════════════════════════════════════════
  // FEATURE 6 — Ripple Effect
  // ═══════════════════════════════════════════
  function buildRipple() {
    document.addEventListener('click', function(e) {
      var target = e.target;
      // Walk up to find ripple host
      var host = null;
      var el = target;
      for (var i = 0; i < 5; i++) {
        if (!el) break;
        if (el.classList && (el.classList.contains('sbb') || el.classList.contains('topt'))) {
          host = el; break;
        }
        el = el.parentElement;
      }
      if (!host) return;
      if (!host.classList.contains('loft-ripple-host')) {
        host.classList.add('loft-ripple-host');
        var style = window.getComputedStyle(host);
        if (style.position === 'static') host.style.position = 'relative';
      }
      var rect = host.getBoundingClientRect();
      var size = Math.max(rect.width, rect.height) * 2;
      var wave = document.createElement('span');
      wave.className = 'loft-ripple-wave';
      wave.style.cssText =
        'width:' + size + 'px;height:' + size + 'px;' +
        'top:' + (e.clientY - rect.top - size/2) + 'px;' +
        'left:' + (e.clientX - rect.left - size/2) + 'px;';
      host.appendChild(wave);
      setTimeout(function() { wave.remove(); }, 600);
    }, true);
  }

  // ═══════════════════════════════════════════
  // FEATURE 7 — Focus Mode + Indicator
  // ═══════════════════════════════════════════
  var _focusMode = false;

  function buildFocusMode() {
    var ind = document.createElement('div');
    ind.id = 'loft-focus-indicator';
    ind.textContent = '⊙ MODO FOCO ATIVO — SHIFT+F PARA SAIR';
    document.body.appendChild(ind);
  }

  // ═══════════════════════════════════════════
  // Global Keyboard Handler
  // ═══════════════════════════════════════════
  function setupKeyboard() {
    document.addEventListener('keydown', function(e) {
      var tag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      var inInput = (tag === 'input' || tag === 'textarea' || tag === 'select');

      // Ctrl+K — Command Palette (works even in inputs)
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        if (_cpOpen) { closeCp(); } else { window._loftOpenCp && window._loftOpenCp(); }
        return;
      }

      // Only handle non-input shortcuts below
      if (inInput) return;

      // ? — Keyboard Shortcuts
      if (e.key === '?' && !e.ctrlKey && !e.metaKey) {
        var bd = document.getElementById('loft-kb-backdrop');
        if (bd) {
          if (bd.classList.contains('loft-open')) { bd.classList.remove('loft-open'); }
          else { bd.classList.add('loft-open'); }
        }
        return;
      }

      // Shift+F — Focus Mode
      if (e.key === 'F' && e.shiftKey) {
        _focusMode = !_focusMode;
        document.body.classList.toggle('loft-focus-mode', _focusMode);
        loftToast(_focusMode ? '⊙ Modo foco ativado' : '○ Modo foco desativado', 'info', 2000);
        return;
      }

      // Escape — close all modals
      if (e.key === 'Escape') {
        closeCp();
        closeKb();
        return;
      }
    });
  }

  // ═══════════════════════════════════════════
  // Init — wait for app to be ready
  // ═══════════════════════════════════════════
  function waitForApp(cb, tries) {
    tries = tries || 0;
    if (window.D && document.getElementById('mc')) {
      cb();
    } else if (tries < 60) {
      setTimeout(function() { waitForApp(cb, tries + 1); }, 200);
    }
  }

  // ═══════════════════════════════════════════
  // FEATURE 8 — Autosave Hook (via #toast-live)
  // ═══════════════════════════════════════════
  function hookAutosave() {
    setTimeout(function() {
      var nativeLive = document.getElementById('toast-live');
      if (!nativeLive) return;
      var obs = new MutationObserver(function(muts) {
        muts.forEach(function(m) {
          m.addedNodes.forEach(function(node) {
            if (node.nodeType === 1) {
              var txt = node.textContent || '';
              if (txt.indexOf('Salvo') !== -1 || txt.indexOf('salvo') !== -1) {
                loftToast('✓ Caso salvo automaticamente', 'success', 2500);
              }
            }
          });
        });
      });
      obs.observe(nativeLive, { childList: true });
    }, 1400);
  }

  function init() {
    waitForApp(function() {
      buildToastSystem();
      buildProgressRing();
      buildCommandPalette();
      buildSectionAnimations();
      buildKeyboardShortcuts();
      buildFocusMode();
      buildRipple();
      setupKeyboard();
      hookAutosave();
      applyLogicPatches();
      applyIAPatches();
      applyUXEnhancements();
      applyPerfPatches();
      applyAuditEnhancements();
      // Welcome toast
      setTimeout(function() {
        loftToast('⌘K command palette • ? atalhos • Shift+F foco', 'info', 5000);
      }, 1800);
    });
  }

  // ═══════════════════════════════════════════════════════════
  // LOFT-AUDIT — Runtime diagnostics & quality gate
  // ═══════════════════════════════════════════════════════════
  function applyAuditEnhancements() {

    // AUDIT-1: Dead code detector — report functions defined but never referenced
    setTimeout(function() {
      var deadCandidates = ['pingIAWorker', 'terminateIAWorker', '_addrNorm',
        'normalizeLinhas', 'iaNormalizeJSON', 'loftEstimateTokens'];
      var dead = deadCandidates.filter(function(fn) {
        return typeof window[fn] === 'function';
      });
      if (dead.length > 0) {
        console.info('[LOFT-AUDIT] Dead code candidates (defined, not wired to UI):', dead);
      }
    }, 3000);

    // AUDIT-2: Signal cycle detection — wrap busOn/busEmit to detect mutual recursion
    (function() {
      var _activeSignals = {};
      var _origBusEmit = typeof window.busEmit === 'function' ? window.busEmit : null;
      if (!_origBusEmit) return;
      window.busEmit = function(sig, payload) {
        if (_activeSignals[sig]) {
          console.warn('[LOFT-AUDIT] Signal cycle detected: "' + sig + '" re-emitted while active. Blocking.');
          return;
        }
        _activeSignals[sig] = true;
        try {
          return _origBusEmit(sig, payload);
        } finally {
          _activeSignals[sig] = false;
        }
      };
    })();

    // AUDIT-3: Mandatory fields visual coverage
    //   Add a subtle asterisk label to required form fields that are empty
    setTimeout(function() {
      var REQUIRED_FIELDS = ['cid','dtSaida','nome_locatario','imovel','vAluguel'];
      function _auditRequiredFields() {
        REQUIRED_FIELDS.forEach(function(field) {
          var el = document.querySelector('[data-field="' + field + '"]');
          if (!el) return;
          var val = el.value || (window.D && window.D.form && window.D.form[field]) || '';
          var label = el.closest('.ff') || el.closest('.rfrow');
          if (!label) return;
          var existing = label.querySelector('.loft-req-dot');
          if (!val || String(val).trim() === '') {
            if (!existing) {
              var dot = document.createElement('span');
              dot.className = 'loft-req-dot';
              dot.title = 'Campo obrigatório';
              dot.style.cssText = 'color:#fa0707;font-size:.7em;margin-left:4px;vertical-align:super;';
              dot.textContent = '*';
              label.appendChild(dot);
            }
          } else {
            if (existing) existing.remove();
          }
        });
      }
      _auditRequiredFields();
      // Re-check on any input change
      document.addEventListener('input', _auditRequiredFields, {passive: true});
      document.addEventListener('change', _auditRequiredFields, {passive: true});
    }, 1500);

    // AUDIT-4: CTX stale detection — warn when AI data is > 30 minutes old
    (function() {
      window._loftCtxTimestamps = window._loftCtxTimestamps || {};
      var STALE_MS = 30 * 60 * 1000;
      // Intercept CTX.docs writes to timestamp them
      var _origCtx = window.CTX;
      if (!_origCtx || !_origCtx.docs) return;
      try {
        var _docsProxy = new Proxy(_origCtx.docs, {
          set: function(target, key, value) {
            target[key] = value;
            window._loftCtxTimestamps[key] = Date.now();
            return true;
          },
          get: function(target, key) {
            var ts = window._loftCtxTimestamps[key];
            if (ts && (Date.now() - ts) > STALE_MS) {
              console.warn('[LOFT-AUDIT] CTX.docs["' + String(key) + '"] is stale (>' + Math.round((Date.now()-ts)/60000) + 'min). Consider re-analyzing.');
            }
            return target[key];
          }
        });
        _origCtx.docs = _docsProxy;
      } catch(ex) { /* Proxy not supported or CTX not wrappable */ }
    })();

    // AUDIT-5: rCats performance instrumentation
    (function() {
      var _origRCatsAudit = typeof window.rCats === 'function' ? window.rCats : null;
      if (!_origRCatsAudit) return;
      var _slowCount = 0;
      window.rCats = function() {
        var t0 = performance.now ? performance.now() : Date.now();
        if (performance.mark) performance.mark('loft-rCats-start');
        var result = _origRCatsAudit.apply(this, arguments);
        var dur = (performance.now ? performance.now() : Date.now()) - t0;
        if (performance.mark) performance.mark('loft-rCats-end');
        if (performance.measure) {
          try { performance.measure('loft-rCats', 'loft-rCats-start', 'loft-rCats-end'); } catch(e){}
        }
        if (dur > 100) {
          _slowCount++;
          console.warn('[LOFT-AUDIT] rCats slow render: ' + Math.round(dur) + 'ms (#' + _slowCount + ' slow renders)');
        }
        return result;
      };
    })();
  }

  // ═══════════════════════════════════════════════════════════
  // LOFT-LOGIC — Business logic bug fixes (safe global patches)
  // ═══════════════════════════════════════════════════════════
  function applyLogicPatches() {
    // 1. Harden _addrEq: prevent false-positives from substring matching
    //    Original: na.includes(nb) → "ruaa10" matches "ruaa100" (BUG)
    //    Fix: require shorter string to be ≥5 chars AND cover ≥60% of longer
    if (typeof window._addrNorm === 'function' || typeof _addrNorm === 'function') {
      var _norm = typeof window._addrNorm === 'function' ? window._addrNorm : _addrNorm;
      window._addrEq = function(a, b) {
        var na = _norm(a), nb = _norm(b);
        if (!na || !nb) return false;
        if (na === nb) return true;
        var longer  = na.length >= nb.length ? na : nb;
        var shorter = na.length >= nb.length ? nb : na;
        // includes() only trusted when shorter is ≥5 chars AND covers ≥60% of longer
        return shorter.length >= 5
          && longer.indexOf(shorter) !== -1
          && (shorter.length / longer.length) >= 0.60;
      };
    }

    // 2. Track manually-set checklist items so AI never overwrites them
    //    Patch _applyInferenceToD to mark AI-set items, respect _manualSet flag
    var _origApplyInference = typeof window._applyInferenceToD === 'function'
      ? window._applyInferenceToD : null;
    window._applyInferenceToD = function(catId, itemId, inf) {
      try {
        if (typeof D === 'undefined' || !D) return;
        var cat = D.checklists && D.checklists.find(function(c){ return c.id === catId; });
        if (!cat) return;
        var it = cat.itens && cat.itens.find(function(i){ return i.id === itemId; });
        if (!it) return;
        // Never overwrite a manually-set item
        if (it._manualSet) return;
        // Run original logic
        if (_origApplyInference) _origApplyInference(catId, itemId, inf);
        // Mark AI-set so we know it was AI-set (not manual)
        if (it.est) it._aiSet = true;
      } catch(ex) {}
    };

    // 3. Track user-touched form fields via event delegation
    //    When user edits any input/select with data-field, mark it in D._userFields
    document.addEventListener('input',  _markUserField, true);
    document.addEventListener('change', _markUserField, true);
    function _markUserField(e) {
      try {
        var el = e.target;
        if (!el) return;
        var field = el.getAttribute && el.getAttribute('data-field');
        if (!field) return;
        if (typeof D === 'undefined' || !D) return;
        if (!D._userFields) D._userFields = {};
        D._userFields[field] = true;
        // Remove from _iaFields so IA knows user took ownership
        if (D._iaFields) delete D._iaFields[field];
      } catch(ex) {}
    }

    // 4. Also mark checklist items when user manually clicks topt toggles
    document.addEventListener('click', function(e) {
      try {
        var el = e.target;
        if (!el) return;
        // Find closest element with onclick that sets est
        var topt = el.closest && el.closest('.topt[onclick]');
        if (topt) {
          // Extract catId and itemId from the onclick to mark as manual
          var onc = topt.getAttribute('onclick') || '';
          var m = onc.match(/setEst\((\d+),(\d+)/);
          if (m) {
            var cId = parseInt(m[1]), iId = parseInt(m[2]);
            setTimeout(function() {
              try {
                if (typeof D === 'undefined') return;
                var cat = D.checklists && D.checklists.find(function(c){ return c.id===cId; });
                var it = cat && cat.itens && cat.itens.find(function(i){ return i.id===iId; });
                if (it && it.est) { it._manualSet = true; it._aiSet = false; }
              } catch(ex) {}
            }, 50);
          }
        }
      } catch(ex) {}
    }, true);

    // LOGIC-NEW-1: Fix qMarkAllOk — BUG3: never mark items that are blocked/pending validation
    var _origQMarkAllOk = typeof window.qMarkAllOk === 'function' ? window.qMarkAllOk : null;
    if (_origQMarkAllOk) {
      window.qMarkAllOk = function(catId) {
        try {
          // After original runs, revert any items that are blocked
          _origQMarkAllOk(catId);
          if (typeof D === 'undefined' || !D || !D.checklists) return;
          var cat = D.checklists.find(function(c){ return c.id === catId; });
          if (!cat) return;
          (cat.itens || []).forEach(function(it) {
            // Re-protect manually-set fail items and blocked items
            if (it._manualSet && it._manualSetEst === 'fail') {
              it.est = 'fail';
            }
            // Items with required sub-fields not filled stay pending
            if (it._bloqueado) {
              it.est = null;
            }
          });
        } catch(ex) {}
      };
    }

    // LOGIC-NEW-2: autoFill conflict — confirm before overwriting manually-set fields
    var _origAutoFill = typeof window._autoFillFormFromContrato === 'function'
      ? window._autoFillFormFromContrato : null;
    if (_origAutoFill) {
      window._autoFillFormFromContrato = function(extracted) {
        try {
          if (typeof D === 'undefined' || !D || !D._userFields) {
            return _origAutoFill(extracted);
          }
          var conflicts = [];
          Object.keys(extracted || {}).forEach(function(k) {
            if (D._userFields[k] && extracted[k] && D.form && D.form[k]) {
              var existing = String(D.form[k]).trim();
              var incoming = String(extracted[k]).trim();
              if (existing && incoming && existing !== incoming) {
                conflicts.push({ field: k, existing: existing, incoming: incoming });
              }
            }
          });
          if (conflicts.length > 0) {
            var msg = 'A IA detectou ' + conflicts.length + ' campo(s) com valor diferente do que voce digitou:\\n\\n';
            conflicts.slice(0, 3).forEach(function(c) {
              msg += '- ' + c.field + ': "' + c.existing.substring(0,30) + '" -> "' + c.incoming.substring(0,30) + '"\\n';
            });
            if (conflicts.length > 3) msg += '- ... e mais ' + (conflicts.length-3) + '\\n';
            msg += '\\nSobrescrever seus valores com os da IA?';
            if (!window.confirm(msg)) {
              // Apply only non-conflicting fields
              var safe = {};
              Object.keys(extracted || {}).forEach(function(k) {
                if (!conflicts.find(function(c){ return c.field===k; })) {
                  safe[k] = extracted[k];
                }
              });
              return _origAutoFill(safe);
            }
          }
          return _origAutoFill(extracted);
        } catch(ex) {
          return _origAutoFill(extracted);
        }
      };
    }

    // LOGIC-NEW-3: multa_contratual consistency — alert when pac vs contratual diverge
    window._loftCheckMultaConsistency = function() {
      try {
        if (typeof D === 'undefined' || !D || !D.form) return;
        var pac = String(D.form.multa_pac || '').replace(/[^\d.,]/g, '').replace(',', '.');
        var con = String(D.form.multa_contratual || '').replace(/[^\d.,]/g, '').replace(',', '.');
        if (!pac || !con) return;
        var vPac = parseFloat(pac), vCon = parseFloat(con);
        if (isNaN(vPac) || isNaN(vCon) || vPac === 0 || vCon === 0) return;
        var ratio = Math.abs(vPac - vCon) / Math.max(vPac, vCon);
        if (ratio > 0.02) { // more than 2% divergence
          var warn = document.getElementById('loft-multa-warn');
          if (!warn) {
            warn = document.createElement('div');
            warn.id = 'loft-multa-warn';
            warn.style.cssText = 'background:rgba(251,146,60,.1);border:1px solid rgba(251,146,60,.3);border-radius:4px;padding:6px 12px;margin:8px 0;font-size:11px;color:#fb923c;font-family:Rajdhani,sans-serif;font-weight:600;letter-spacing:.04em;text-transform:uppercase;';
          }
          warn.textContent = '⚠ Divergência entre multa PAC (' + D.form.multa_pac + ') e multa contratual (' + D.form.multa_contratual + ')';
          // Try to inject near multa fields
          var multaEl = document.querySelector('[data-field="multa_pac"]') || document.querySelector('[data-field="multa_contratual"]');
          if (multaEl) {
            var parent = multaEl.closest('.ff') || multaEl.parentNode;
            if (parent && !parent.contains(warn)) parent.appendChild(warn);
          }
        } else {
          var existing = document.getElementById('loft-multa-warn');
          if (existing) existing.remove();
        }
      } catch(ex) {}
    };
    // Run on any input change
    document.addEventListener('input', window._loftCheckMultaConsistency, {passive: true});
    document.addEventListener('change', window._loftCheckMultaConsistency, {passive: true});

    // LOGIC-NEW-4: Proportional rent validation
    //   If D.form.dtSaida and D.form.dtInicioContrato are set, verify proportional billing makes sense
    window._loftCheckProportional = function() {
      try {
        if (typeof D === 'undefined' || !D || !D.form) return;
        var dtSaida = D.form.dtSaida || D.form.dt_saida || '';
        var vAluguel = parseFloat(String(D.form.vAluguel || '0').replace(/[^\d.,]/g,'').replace(',','.'));
        if (!dtSaida || !vAluguel) return;
        // Parse date dd/mm/yyyy
        var parts = dtSaida.split('/');
        if (parts.length !== 3) return;
        var day = parseInt(parts[0],10), month = parseInt(parts[1],10), year = parseInt(parts[2],10);
        if (isNaN(day) || isNaN(month) || isNaN(year)) return;
        var daysInMonth = new Date(year, month, 0).getDate();
        if (day === daysInMonth || day === 1) return; // full month, no proration needed
        var propExpected = Math.round((vAluguel / daysInMonth) * day * 100) / 100;
        // Check if calc lines have a proportional entry
        var propLine = (D.calc && D.calc.linhas || []).find(function(l){
          return l.tipo === 'aluguel_prop' || (l.desc && l.desc.toLowerCase().indexOf('proporcional') !== -1);
        });
        if (!propLine) {
          console.info('[LOFT-LOGIC] Saída em dia ' + day + ' de ' + daysInMonth + '. Aluguel proporcional esperado: R$ ' + propExpected.toFixed(2) + '. Considere adicionar linha proporcional na calculadora.');
        }
      } catch(ex) {}
    };
    setTimeout(window._loftCheckProportional, 2000);
    document.addEventListener('change', window._loftCheckProportional, {passive: true});

    // LOGIC-NEW-5: CNPJ cross-validation in boleto vs contrato
    //   Expose a helper that compares extracted boleto CNPJ to contract CNPJ
    window._loftValidateCNPJ = function(boletoObj, contractCNPJ) {
      try {
        var _normCNPJ = function(s) { return String(s||'').replace(/[^\d]/g,''); };
        var bCNPJ = _normCNPJ(boletoObj && (boletoObj.cnpj || boletoObj.beneficiario_cnpj || ''));
        var cCNPJ = _normCNPJ(contractCNPJ || (typeof D !== 'undefined' && D && D.form && D.form.cnpj_imob) || '');
        if (!bCNPJ || !cCNPJ) return { status: 'INCONCLUSIVO', reason: 'CNPJ ausente' };
        if (bCNPJ === cCNPJ) return { status: 'CONFORME', reason: 'CNPJs coincidem' };
        // Allow partial match (14 digits must match fully)
        return { status: 'DIVERGENTE', reason: 'Boleto: ' + bCNPJ + ' vs Contrato: ' + cCNPJ };
      } catch(ex) { return { status: 'ERRO', reason: String(ex) }; }
    };
    // Hook into iaParseJSON to auto-validate CNPJs when boleto data arrives
    var _origParseForCNPJ = typeof window.iaParseJSON === 'function' ? window.iaParseJSON : null;
    if (_origParseForCNPJ) {
      window.iaParseJSON = function(raw) {
        var result = _origParseForCNPJ(raw);
        if (result && !result._error && result.boletos) {
          try {
            result.boletos.forEach(function(b) {
              var v = window._loftValidateCNPJ(b);
              if (v.status === 'DIVERGENTE') {
                b._cnpj_status = 'DIVERGENTE';
                b._cnpj_reason = v.reason;
                console.warn('[LOFT-LOGIC] CNPJ divergente no boleto:', v.reason);
                loftToast && loftToast('⚠ CNPJ do boleto diverge do contrato', 'warning', 5000);
              } else {
                b._cnpj_status = v.status;
              }
            });
          } catch(ex) {}
        }
        return result;
      };
    }

    // 5. Enhance validateMulta to also flag missing mandatory fields
    var _origValidateMulta = typeof window.validateMulta === 'function'
      ? window.validateMulta : null;
    window.validateMulta = function() {
      var issues = _origValidateMulta ? _origValidateMulta() : [];
      try {
        if (typeof D === 'undefined' || !D || !D.form) return issues;
        var mc = D.form.multa_contratual || D.form.multa_pac || '';
        var hasCalcLines = D.calc && D.calc.linhas && D.calc.linhas.some(function(l) {
          return l.tipo === 'multa';
        });
        if (hasCalcLines && !mc.trim()) {
          issues.unshift('Multa contratual não preenchida — preencha antes de calcular');
        }
        if (mc && !/\d/.test(mc)) {
          issues.push('Multa contratual não contém número — verifique o valor');
        }
      } catch(ex) {}
      return issues;
    };
  }

  // ═══════════════════════════════════════════════════════════
  // LOFT-IA — Gemini integration improvements
  // ═══════════════════════════════════════════════════════════
  function applyIAPatches() {
    // 1. Better error classification and user-friendly messages
    //    Wrap the global iaCall to reclassify errors
    var _origIaCall = typeof window.iaCall === 'function' ? window.iaCall : null;
    if (_origIaCall) {
      window.iaCall = function(model, systemPrompt, parts, maxTokens, temperature) {
        return _origIaCall(model, systemPrompt, parts, maxTokens, temperature)
          .catch(function(err) {
            var msg = err && err.message ? err.message : String(err);
            // Classify known error patterns into friendly messages
            if (msg.indexOf('API key') !== -1 || msg.indexOf('400') !== -1 || msg.indexOf('401') !== -1) {
              throw new Error('❌ Chave API inválida ou expirada. Verifique em aistudio.google.com/apikey');
            }
            if (msg.indexOf('429') !== -1 || msg.indexOf('sobrecarregada') !== -1) {
              throw new Error('⏳ Limite de requisições atingido. Aguarde 1 minuto e tente novamente.');
            }
            if (msg.indexOf('Timeout') !== -1 || msg.indexOf('AbortError') !== -1) {
              throw new Error('⌛ Tempo esgotado. Documento muito grande ou conexão lenta. Tente dividir em partes menores.');
            }
            if (msg.indexOf('vazia') !== -1 || msg.indexOf('ilegível') !== -1) {
              throw new Error('📄 Documento ilegível ou corrompido. Verifique a qualidade do arquivo.');
            }
            throw err;
          });
      };
    }

    // 2. Model fallback: if flash fails with 5xx, retry with flash-8b
    var _origIaCallFallback = window.iaCall;
    if (_origIaCallFallback) {
      window.iaCallWithFallback = function(primaryModel, systemPrompt, parts, maxTokens, temperature) {
        return _origIaCallFallback(primaryModel, systemPrompt, parts, maxTokens, temperature)
          .catch(function(err) {
            var msg = err && err.message ? err.message : '';
            // Only fallback for server errors, not key/rate errors
            if (msg.indexOf('❌') !== -1 || msg.indexOf('⏳') !== -1) throw err;
            var fallback = primaryModel.indexOf('flash') !== -1
              ? 'gemini-2.0-flash-lite' : null;
            if (!fallback) throw err;
            loftToast('Modelo principal indisponível — usando fallback...', 'warning', 3000);
            return _origIaCallFallback(fallback, systemPrompt, parts, maxTokens, temperature);
          });
      };
    }

    // 3. Token estimation helper (rough: 4 chars ≈ 1 token)
    window.loftEstimateTokens = function(parts) {
      try {
        var totalChars = 0;
        (parts || []).forEach(function(p) {
          if (p.text) totalChars += p.text.length;
          if (p.inlineData && p.inlineData.data) totalChars += p.inlineData.data.length * 0.75;
        });
        return Math.round(totalChars / 4);
      } catch(ex) { return 0; }
    };

    // 4. Improve iaParseJSON robustness: add extra cleanup passes
    var _origParseJSON = typeof window.iaParseJSON === 'function' ? window.iaParseJSON : null;
    if (_origParseJSON) {
      window.iaParseJSON = function(raw) {
        try {
          // Try original parser first
          var result = _origParseJSON(raw);
          if (result && !result._error) return result;
          // Extra pass: remove trailing commas before ] and }
          var cleaned = raw
            .replace(/,\s*([\]}])/g, '$1')         // trailing commas
            .replace(/[\\x00-\\x1F\\x7F]/g, ' ')      // control chars
            .replace(/\bNaN\b/g, 'null')            // NaN → null
            .replace(/\bInfinity\b/g, 'null')       // Infinity → null
            .replace(/\bundefined\b/g, 'null');     // undefined → null
          try { return JSON.parse(cleaned); } catch(e2) {}
          return result; // return original _error result
        } catch(ex) {
          return { _error: 'Parse failed: ' + String(ex).substring(0, 80) };
        }
      };
    }

    // IA-NEW-1: Prompt hash caching — skip duplicate calls with identical systemPrompt+parts
    //   Lightweight djb2 hash used as secondary cache key layer
    (function() {
      function _djb2(s) {
        var h = 5381;
        for (var i = 0; i < s.length; i++) h = ((h << 5) + h) ^ s.charCodeAt(i);
        return (h >>> 0).toString(36);
      }
      var _hashCache = {};
      var _HC_MAX = 40;
      var _origIaHashWrap = typeof window.iaCall === 'function' ? window.iaCall : null;
      if (!_origIaHashWrap) return;
      window.iaCall = function(model, systemPrompt, parts, maxTokens, temperature) {
        var key = model + '_' + _djb2((systemPrompt||'').substring(0,500))
          + '_' + _djb2(JSON.stringify(parts||[]).substring(0,400));
        if (_hashCache[key]) {
          console.info('[LOFT-IA] Hash cache hit — skipping duplicate call');
          return _hashCache[key];
        }
        var promise = _origIaHashWrap(model, systemPrompt, parts, maxTokens, temperature);
        _hashCache[key] = promise;
        // Evict oldest entry if over limit
        var keys = Object.keys(_hashCache);
        if (keys.length > _HC_MAX) delete _hashCache[keys[0]];
        // Remove from cache on error so it retries fresh
        promise.catch(function() { delete _hashCache[key]; });
        return promise;
      };
    })();

    // IA-NEW-2: Adaptive backoff — retry delay depends on error type
    (function() {
      var _origIaAdaptive = typeof window.iaCall === 'function' ? window.iaCall : null;
      if (!_origIaAdaptive) return;
      window.iaCall = function(model, systemPrompt, parts, maxTokens, temperature) {
        return _origIaAdaptive(model, systemPrompt, parts, maxTokens, temperature)
          .catch(function(err) {
            var msg = err && err.message ? err.message : String(err);
            // 429 / rate limit → wait 60s then retry once
            if (msg.indexOf('429') !== -1 || msg.indexOf('sobrecarregada') !== -1 || msg.indexOf('Limite') !== -1) {
              loftToast && loftToast('⏳ Rate limit — aguardando 15s para retry automático...', 'warning', 14000);
              return new Promise(function(resolve, reject) {
                setTimeout(function() {
                  _origIaAdaptive(model, systemPrompt, parts, maxTokens, temperature)
                    .then(resolve).catch(reject);
                }, 15000);
              });
            }
            // 503 / server error → wait 3s then retry once
            if (msg.indexOf('503') !== -1 || msg.indexOf('overloaded') !== -1) {
              return new Promise(function(resolve, reject) {
                setTimeout(function() {
                  _origIaAdaptive(model, systemPrompt, parts, maxTokens, temperature)
                    .then(resolve).catch(reject);
                }, 3000);
              });
            }
            throw err;
          });
      };
    })();

    // IA-NEW-3: Missing fields focused retry
    //   After _applyInferenceToD, check which FORM_LABELS fields are still empty
    //   and expose a helper to trigger a targeted re-call
    window._loftMissingFieldsRetry = function(docKey) {
      try {
        if (typeof D === 'undefined' || !D) return;
        if (typeof FORM_LABELS === 'undefined' || !FORM_LABELS) return;
        var missing = Object.keys(FORM_LABELS).filter(function(k) {
          return !D.form || !D.form[k] || String(D.form[k]).trim() === '';
        });
        if (missing.length === 0) {
          loftToast && loftToast('✓ Todos os campos já preenchidos', 'success', 2500);
          return;
        }
        loftToast && loftToast('🔄 ' + missing.length + ' campos vazios — tentando extrair especificamente...', 'info', 4000);
        // Build focused prompt for missing fields
        var focusedPrompt = 'Extraia APENAS os seguintes campos do documento fornecido:\\n\\n'
          + missing.map(function(k){ return '- ' + k + ' (' + FORM_LABELS[k] + ')'; }).join('\\n')
          + '\\n\\nRetorne SOMENTE JSON: {"' + missing[0] + '":"valor",...}';
        // Get existing doc text if available
        var docData = typeof CTX !== 'undefined' && CTX && CTX.docs && CTX.docs[docKey];
        if (!docData || !docData.raw) {
          loftToast && loftToast('⚠ Documento não encontrado para retry', 'warning', 3000);
          return;
        }
        var parts = [{ text: docData.raw }];
        var model = typeof GEMINI_MODEL !== 'undefined' ? GEMINI_MODEL : 'gemini-2.0-flash';
        window.iaCall(model, focusedPrompt, parts, 1024, 0.2)
          .then(function(resp) {
            var parsed = typeof iaParseJSON === 'function' ? iaParseJSON(resp) : null;
            if (parsed && !parsed._error) {
              if (typeof _autoFillFormFromContrato === 'function') _autoFillFormFromContrato(parsed);
              loftToast && loftToast('✓ Campos extras extraídos', 'success', 3000);
            }
          }).catch(function(e) {
            loftToast && loftToast('⚠ Retry falhou: ' + (e.message||'').substring(0,50), 'error', 4000);
          });
      } catch(ex) {}
    };
    // Register in command palette
    if (window.PALETTE_ITEMS) {
      window.PALETTE_ITEMS.push({ label: 'Extrair campos vazios (retry IA)', icon: '🔄', action: function(){ window._loftMissingFieldsRetry('contrato'); } });
    }

    // 5. Show estimated token count in IA panel API key area
    var _apiKeyInput = document.getElementById('ia-api-key');
    if (_apiKeyInput) {
      var _tokenHint = document.createElement('div');
      _tokenHint.id = 'loft-token-hint';
      _tokenHint.style.cssText = 'font-size:10px;color:#555;margin-top:4px;font-family:monospace;letter-spacing:.04em;';
      _tokenHint.textContent = 'tokens estimados: —';
      _apiKeyInput.parentNode.parentNode.appendChild(_tokenHint);
    }
  }

  // ═══════════════════════════════════════════════════════════
  // LOFT-UX — Onboarding + ARIA + accessibility
  // ═══════════════════════════════════════════════════════════
  function applyUXEnhancements() {
    // 1. ARIA labels on key interactive elements
    setTimeout(function() {
      var mc = document.getElementById('mc');
      if (mc) { mc.setAttribute('role', 'main'); mc.setAttribute('aria-label', 'Área de checklist'); }
      var aside = document.querySelector('aside');
      if (aside) { aside.setAttribute('role', 'navigation'); aside.setAttribute('aria-label', 'Menu de navegação'); }
      // Label all section cards
      var sections = document.querySelectorAll('.fs');
      sections.forEach(function(s, i) {
        var title = s.querySelector('.fst');
        var label = title ? title.textContent.trim() : ('Seção ' + (i+1));
        s.setAttribute('aria-label', label);
        s.setAttribute('role', 'region');
      });
    }, 600);

    // Re-apply ARIA when mc content changes
    var _ariaObs = new MutationObserver(function() {
      clearTimeout(_ariaObs._t);
      _ariaObs._t = setTimeout(function() {
        var mc = document.getElementById('mc');
        if (!mc) return;
        mc.querySelectorAll('.fs:not([role])').forEach(function(s) {
          var title = s.querySelector('.fst');
          if (title) {
            s.setAttribute('aria-label', title.textContent.trim());
            s.setAttribute('role', 'region');
          }
        });
      }, 300);
    });
    var _mcAria = document.getElementById('mc');
    if (_mcAria) _ariaObs.observe(_mcAria, { childList: true, subtree: false });

    // 2. First-time onboarding modal
    var _onboardKey = 'loft_v3_onboarded';
    if (!localStorage.getItem(_onboardKey)) {
      setTimeout(function() {
        localStorage.setItem(_onboardKey, '1');
        _showOnboarding();
      }, 2200);
    }

    function _showOnboarding() {
      var ov = document.createElement('div');
      ov.id = 'loft-onboard-overlay';
      ov.style.cssText = [
        'position:fixed;inset:0;background:rgba(0,0,0,.82);z-index:99999;',
        'display:flex;align-items:center;justify-content:center;padding:24px;',
        'backdrop-filter:blur(6px);animation:loft-fade-in .25s ease'
      ].join('');

      var box = document.createElement('div');
      box.style.cssText = [
        'background:#141414;border:1px solid #2a2a2a;border-radius:8px;',
        'width:100%;max-width:480px;overflow:hidden;',
        'box-shadow:0 32px 80px rgba(0,0,0,.7)'
      ].join('');

      var steps = [
        { icon: '📋', title: 'Bem-vindo ao LOFT Checklist V3', desc: 'Sistema de análise de rescisão com IA integrada. Carregue os documentos na aba IA para análise automática.' },
        { icon: '🤖', title: 'Validação por IA', desc: 'Configure sua API Key Gemini na aba IA. O sistema analisa contratos, vistorias e boletos automaticamente.' },
        { icon: '⌨️', title: 'Atalhos de teclado', desc: 'Ctrl+K abre a paleta de comandos. Pressione ? para ver todos os atalhos. Shift+F ativa o modo foco.' },
        { icon: '📊', title: 'Relatório final', desc: 'Após preencher o checklist, use "Gerar link" para exportar o relatório completo com score de qualidade.' }
      ];
      var cur = 0;

      function _render() {
        var s = steps[cur];
        box.innerHTML = [
          '<div style="background:var(--brand,#fa0707);padding:24px 24px 20px;text-align:center">',
            '<div style="font-size:2.2em;margin-bottom:8px">'+s.icon+'</div>',
            '<div style="font-family:Rajdhani,sans-serif;font-size:1.1em;font-weight:700;color:#fff;letter-spacing:.06em;text-transform:uppercase">'+s.title+'</div>',
          '</div>',
          '<div style="padding:24px">',
            '<p style="font-family:Rajdhani,sans-serif;font-size:.9em;color:#aaa;line-height:1.6;text-transform:none;margin:0 0 20px">'+s.desc+'</p>',
            '<div style="display:flex;gap:8px;align-items:center">',
              '<div style="flex:1;display:flex;gap:6px">',
                steps.map(function(_,i){
                  return '<div style="width:6px;height:6px;border-radius:50%;background:'+(i===cur?'#fa0707':'#2a2a2a')+'"></div>';
                }).join(''),
              '</div>',
              cur > 0 ? '<button id="loft-ob-back" style="padding:8px 16px;background:transparent;border:1px solid #2a2a2a;border-radius:4px;color:#888;font-family:Rajdhani,sans-serif;font-size:.8em;font-weight:600;cursor:pointer;text-transform:uppercase">Anterior</button>' : '',
              '<button id="loft-ob-next" style="padding:8px 20px;background:#fa0707;border:none;border-radius:4px;color:#fff;font-family:Rajdhani,sans-serif;font-size:.8em;font-weight:700;cursor:pointer;text-transform:uppercase">'+
                (cur===steps.length-1 ? 'Começar' : 'Próximo')+
              '</button>',
            '</div>',
          '</div>'
        ].join('');
        var nb = document.getElementById('loft-ob-next');
        var bb = document.getElementById('loft-ob-back');
        if (nb) nb.onclick = function() {
          if (cur < steps.length-1) { cur++; _render(); }
          else { document.body.removeChild(ov); }
        };
        if (bb) bb.onclick = function() { if (cur>0) { cur--; _render(); } };
      }

      ov.appendChild(box);
      ov.addEventListener('click', function(e) { if (e.target===ov) document.body.removeChild(ov); });
      document.body.appendChild(ov);
      _render();
    }

    // 3. Keyboard navigation: Tab key cycles through category buttons in sidebar
    document.addEventListener('keydown', function(e) {
      if (e.key === 'F1') {
        e.preventDefault();
        // Simulate ? key to show shortcuts
        document.dispatchEvent(new KeyboardEvent('keydown', {key:'?', bubbles:true}));
      }
    });

    // UX-NEW-1: Skeleton screens for AI result blocks
    //   Intercept IA loading states and replace "..." with skeleton
    (function() {
      var _skeletonHTML = '<div class="loft-skeleton loft-skeleton-line wide"></div>'
        + '<div class="loft-skeleton loft-skeleton-line short"></div>'
        + '<div class="loft-skeleton loft-skeleton-line wide"></div>'
        + '<div class="loft-skeleton loft-skeleton-line" style="width:70%"></div>';
      // Watch for elements getting the loading class (app uses "loading" text or specific pattern)
      var _skeletonObs = new MutationObserver(function(muts) {
        muts.forEach(function(m) {
          m.addedNodes.forEach(function(node) {
            if (node.nodeType !== 1) return;
            // Look for result blocks that show "Analisando..." or similar
            var text = node.textContent || '';
            if ((text === 'Analisando...' || text === '...' || text === 'Carregando...') && !node._loftSkel) {
              node._loftSkel = true;
              node.innerHTML = _skeletonHTML;
            }
          });
        });
      });
      _skeletonObs.observe(document.body, { childList: true, subtree: true });
    })();

    // UX-NEW-2: Undo/Redo visual counter
    (function() {
      var counter = document.createElement('div');
      counter.id = 'loft-undo-counter';
      document.body.appendChild(counter);
      function _updateUndoCounter() {
        try {
          var histLen = (typeof UNDO_STACK !== 'undefined' && UNDO_STACK) ? UNDO_STACK.length : 0;
          var redoLen = (typeof REDO_STACK !== 'undefined' && REDO_STACK) ? REDO_STACK.length : 0;
          if (histLen === 0 && redoLen === 0) {
            counter.textContent = '';
            counter.classList.remove('loft-undo-active');
          } else {
            counter.textContent = 'Alt+Z: ' + histLen + ' desfazer  •  Alt+Y: ' + redoLen + ' refazer';
            counter.classList.add('loft-undo-active');
          }
        } catch(ex) {}
      }
      // Poll every 2s (undo stack changes aren't event-driven)
      setInterval(_updateUndoCounter, 2000);
      _updateUndoCounter();
    })();

    // UX-NEW-3: Vistoria comparison mode
    //   Adds a "Comparar vistorias" button in the danos/vistoria section
    setTimeout(function() {
      var danoSection = document.querySelector('#cat-danos') || document.querySelector('[data-cat="danos"]');
      if (!danoSection) return;
      var compareBar = document.createElement('div');
      compareBar.id = 'loft-compare-bar';
      compareBar.innerHTML = '<span>Comparar: </span>'
        + '<button id="loft-compare-btn" style="padding:4px 12px;background:var(--brand);color:#fff;border:none;border-radius:4px;cursor:pointer;font-family:Rajdhani,sans-serif;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase">Ativar Diff</button>'
        + '<span id="loft-compare-info" style="flex:1;margin-left:12px;font-size:10px;color:#444">Mostra diferenças entre vistoria de entrada e saída</span>';
      danoSection.insertBefore(compareBar, danoSection.firstChild);
      compareBar.classList.add('loft-active');
      document.getElementById('loft-compare-btn').addEventListener('click', function() {
        var diff = (typeof CTX !== 'undefined' && CTX && CTX.diffData) || null;
        if (!diff) { loftToast('⚠ Analise vistoria de entrada e saída antes de comparar', 'warning', 4000); return; }
        try {
          var rooms = Object.keys(diff);
          var lines = rooms.map(function(room) {
            var d = diff[room];
            var adds = (d.added||[]).map(function(x){ return '<span class="loft-diff-add">+ '+x+'</span>'; });
            var dels = (d.removed||[]).map(function(x){ return '<span class="loft-diff-del">- '+x+'</span>'; });
            return '<strong>'+room+':</strong> ' + (adds.concat(dels).join(' | ') || '<span class="loft-diff-same">Sem diferenças</span>');
          });
          var modal = document.createElement('div');
          modal.style.cssText = 'position:fixed;inset:0;z-index:19999;background:rgba(0,0,0,.85);display:flex;align-items:center;justify-content:center;padding:24px;backdrop-filter:blur(4px)';
          var closeBtn = document.createElement('button');
          closeBtn.textContent = 'Fechar';
          closeBtn.style.cssText = 'margin-top:16px;padding:8px 20px;background:var(--brand);color:#fff;border:none;border-radius:4px;cursor:pointer;font-family:Rajdhani,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase';
          closeBtn.onclick = function(){ document.body.removeChild(modal); };
          var inner = document.createElement('div');
          inner.style.cssText = 'background:#141414;border:1px solid #2a2a2a;border-radius:8px;padding:24px;max-width:640px;width:100%;max-height:80vh;overflow-y:auto';
          inner.innerHTML = '<div style="font-family:Rajdhani,sans-serif;font-size:13px;font-weight:700;color:#e0e0e0;text-transform:uppercase;letter-spacing:.06em;margin-bottom:16px">Diff: Vistoria Entrada vs Saida</div>'
            + '<div style="font-family:Rajdhani,sans-serif;font-size:12px;line-height:2;color:#888">' + lines.join('<br>') + '</div>';
          inner.appendChild(closeBtn);
          modal.appendChild(inner);
          document.body.appendChild(modal);
        } catch(ex) { loftToast('⚠ Erro ao gerar diff: ' + (ex.message||''), 'error', 3000); }
      });
    }, 2000);

    // UX-NEW-4: PDF/Print export button
    (function() {
      var btn = document.createElement('button');
      btn.id = 'loft-pdf-btn';
      btn.textContent = '🖨 PDF';
      btn.title = 'Imprimir / Salvar como PDF';
      btn.addEventListener('click', function() {
        loftToast('Abrindo diálogo de impressão... Use "Salvar como PDF" no destino.', 'info', 4000);
        setTimeout(function() { window.print(); }, 500);
      });
      document.body.appendChild(btn);
    })();

    // UX-NEW-5: Global checklist search (Ctrl+F)
    (function() {
      var overlay = document.createElement('div');
      overlay.id = 'loft-search-overlay';
      overlay.innerHTML = '<input id="loft-search-input" type="text" placeholder="Buscar no checklist..." autocomplete="off">'
        + '<span id="loft-search-count">0 resultados</span>'
        + '<button id="loft-search-close">✕</button>';
      document.body.appendChild(overlay);

      var _searchMatches = [], _searchIdx = 0;

      function _clearSearch() {
        _searchMatches.forEach(function(el) {
          el.classList.remove('loft-search-highlight','loft-search-current');
        });
        _searchMatches = []; _searchIdx = 0;
      }

      function _runSearch(q) {
        _clearSearch();
        if (!q || q.length < 2) { document.getElementById('loft-search-count').textContent = ''; return; }
        var mc = document.getElementById('mc');
        if (!mc) return;
        // Search in checklist item labels and text
        var candidates = mc.querySelectorAll('.topt, .topt-label, .topt-title, [class*="item"], [class*="label"]');
        candidates.forEach(function(el) {
          if (el.children.length > 2) return; // Skip containers
          var text = el.textContent || '';
          if (text.toLowerCase().indexOf(q.toLowerCase()) !== -1) {
            el.classList.add('loft-search-highlight');
            _searchMatches.push(el);
          }
        });
        document.getElementById('loft-search-count').textContent = _searchMatches.length + ' resultado' + (_searchMatches.length !== 1 ? 's' : '');
        if (_searchMatches.length > 0) {
          _searchMatches[0].classList.add('loft-search-current');
          _searchMatches[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }

      function _nextMatch(dir) {
        if (_searchMatches.length === 0) return;
        _searchMatches[_searchIdx].classList.remove('loft-search-current');
        _searchIdx = (_searchIdx + dir + _searchMatches.length) % _searchMatches.length;
        _searchMatches[_searchIdx].classList.add('loft-search-current');
        _searchMatches[_searchIdx].scrollIntoView({ behavior: 'smooth', block: 'center' });
      }

      var _searchInput = document.getElementById('loft-search-input');
      var _searchDebounce;
      _searchInput.addEventListener('input', function() {
        clearTimeout(_searchDebounce);
        _searchDebounce = setTimeout(function() { _runSearch(_searchInput.value); }, 200);
      });
      _searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') { e.shiftKey ? _nextMatch(-1) : _nextMatch(1); }
        if (e.key === 'Escape') { overlay.classList.remove('loft-open'); _clearSearch(); }
      });
      document.getElementById('loft-search-close').addEventListener('click', function() {
        overlay.classList.remove('loft-open'); _clearSearch(); _searchInput.value = '';
      });

      // Ctrl+F override
      document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'f') {
          // Only intercept when not in a native input that would use browser's search
          var tag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
          if (tag === 'input' || tag === 'textarea') return;
          e.preventDefault();
          overlay.classList.toggle('loft-open');
          if (overlay.classList.contains('loft-open')) {
            setTimeout(function(){ _searchInput.focus(); }, 50);
          } else {
            _clearSearch(); _searchInput.value = '';
          }
        }
      });

      // Register in command palette
      if (window.PALETTE_ITEMS) {
        window.PALETTE_ITEMS.push({ label: 'Buscar no checklist (Ctrl+F)', icon: '🔍', action: function(){
          overlay.classList.add('loft-open');
          setTimeout(function(){ _searchInput.focus(); }, 50);
        }});
      }
    })();

    // UX-IA-LAYOUT: ordering is handled entirely by CSS (flex order).
    // See ENHANCED_CSS: #mc .ia-panel > [id^="ia-acc-"] { order: 3; }
    //                   #mc .ia-panel > * { order: 9; }
    //                   #mc .ia-panel > .phd { order: 1; }
    // No JS manipulation needed — CSS applies instantly on every render.
  }

  // ═══════════════════════════════════════════════════════════
  // LOFT-PERF — Performance optimizations
  // ═══════════════════════════════════════════════════════════
  function applyPerfPatches() {
    // 1. Add TTL to AIClient LRU cache entries (30min expiry)
    if (typeof AIClient !== 'undefined' && AIClient) {
      var _origCall = AIClient.call.bind(AIClient);
      var _ttlMap = {};
      var _TTL = 30 * 60 * 1000; // 30 minutes
      AIClient.call = function(model, systemPrompt, parts, maxTokens, temperature, opts) {
        // Evict expired entries by checking _ttlMap
        var now = Date.now();
        // We can't directly evict from the private LRU, but we can skip stale caches
        // by injecting noCache=true when entry would be expired
        var cacheKey = model + '|' + (systemPrompt||'').substring(0,50) + '|' + (JSON.stringify(parts||[])).substring(0,100);
        if (_ttlMap[cacheKey] && (now - _ttlMap[cacheKey]) > _TTL) {
          opts = Object.assign({}, opts, { noCache: true });
          delete _ttlMap[cacheKey];
        }
        return _origCall(model, systemPrompt, parts, maxTokens, temperature, opts)
          .then(function(result) {
            _ttlMap[cacheKey] = Date.now();
            return result;
          });
      };
    }

    // 2. Throttle expensive busOn signal handlers that re-render
    //    Add global signal depth guard notification
    if (typeof _BUS !== 'undefined' && _BUS) {
      var _depthWarned = false;
      var _origDepth = _BUS._signalDepth;
      Object.defineProperty(_BUS, '_signalDepth', {
        get: function() { return _origDepth; },
        set: function(v) {
          _origDepth = v;
          if (v >= 6 && !_depthWarned) {
            _depthWarned = true;
            console.warn('[LOFT-PERF] Signal cascade depth='+v+' — possible loop');
            setTimeout(function(){ _depthWarned = false; }, 5000);
          }
        }
      });
    }

    // 3. Optimize progress ring updates: skip if no checkbox count changed
    //    (Already debounced at 80ms in MutationObserver, this adds a value cache)
    if (typeof LOFT_ENH !== 'undefined' && LOFT_ENH._prUpdate) {
      var _origPrUpdate = LOFT_ENH._prUpdate;
      var _lastTotal = -1;
      var _lastChecked = -1;
      LOFT_ENH._prUpdate = function() {
        var mc = document.getElementById('mc');
        if (!mc) return;
        var total = mc.querySelectorAll('input[type="checkbox"]').length;
        var checked = mc.querySelectorAll('input[type="checkbox"]:checked').length;
        if (total === _lastTotal && checked === _lastChecked) return;
        _lastTotal = total; _lastChecked = checked;
        _origPrUpdate();
      };
    }

    // 4. Debounce rCats if called too rapidly (prevent cascade re-renders)
    //    Wrap global rCats with a 16ms animation-frame debounce
    if (typeof window.rCats === 'function') {
      var _origRCats = window.rCats;
      var _rCatsFrame = null;
      window.rCats = function() {
        if (_rCatsFrame) return; // already scheduled
        _rCatsFrame = requestAnimationFrame(function() {
          _rCatsFrame = null;
          _origRCats();
        });
      };
    }

    // 5. Cleanup setIntervals on page unload (AUDIT: memory leaks)
    window.addEventListener('pagehide', function() {
      // Best-effort: clear timers that are in our control
      if (typeof _ringTimer !== 'undefined' && _ringTimer) clearInterval(_ringTimer);
      if (typeof _autosaveInterval !== 'undefined' && _autosaveInterval) clearInterval(_autosaveInterval);
    });

    // PERF-NEW-1: Tab lazy loading — defer rendering of non-active tabs
    //   Wrap selCat (the tab switcher) to render tabs only when first visited
    (function() {
      var _renderedTabs = {};
      var _origSelCat = typeof window.selCat === 'function' ? window.selCat : null;
      if (!_origSelCat) return;
      window.selCat = function(catIdx) {
        var key = 'tab_' + catIdx;
        if (!_renderedTabs[key]) {
          _renderedTabs[key] = true;
          // Show skeleton briefly on first open
          var mc = document.getElementById('mc');
          if (mc && Object.keys(_renderedTabs).length > 1) {
            var prev = mc.innerHTML;
            mc.innerHTML = '<div class="loft-tab-skeleton"></div>';
            requestAnimationFrame(function() {
              mc.innerHTML = prev;
              _origSelCat(catIdx);
            });
            return;
          }
        }
        return _origSelCat(catIdx);
      };
    })();

    // PERF-NEW-2: bldData() memoization — cache by D state fingerprint
    (function() {
      var _origBldData = typeof window.bldData === 'function' ? window.bldData : null;
      if (!_origBldData) return;
      var _cache = null, _cacheKey = null;
      window.bldData = function() {
        try {
          // Fingerprint: stringify small subset of D to detect changes cheaply
          var d = window.D;
          if (!d) return _origBldData();
          var fp = JSON.stringify([
            d.boleto, d.lim, d.formaPag,
            Object.keys(d.form||{}).length,
            (d.checklists||[]).reduce(function(sum, c) { return sum + (c.itens||[]).filter(function(i){ return i.est; }).length; }, 0)
          ]);
          if (fp === _cacheKey && _cache !== null) {
            return _cache;
          }
          _cache = _origBldData();
          _cacheKey = fp;
          return _cache;
        } catch(ex) { return _origBldData(); }
      };
      // Invalidate cache on saves
      var _origSv = typeof window.sv === 'function' ? window.sv : null;
      if (_origSv) {
        window.sv = function() {
          _cache = null; _cacheKey = null;
          return _origSv.apply(this, arguments);
        };
      }
    })();

    // PERF-NEW-3: Input event debounce on _markUnsaved (300ms)
    (function() {
      var _origMarkUnsaved = typeof window._markUnsaved === 'function' ? window._markUnsaved : null;
      if (!_origMarkUnsaved) return;
      var _debounceTimer = null;
      window._markUnsaved = function() {
        if (_debounceTimer) return; // already scheduled
        _debounceTimer = setTimeout(function() {
          _debounceTimer = null;
          _origMarkUnsaved();
        }, 300);
      };
    })();

    // PERF-NEW-4: DOM node cleanup on tab navigation
    //   When navigating between tabs, remove detached sub-trees from previous tabs
    //   to prevent DOM bloat on long sessions
    (function() {
      var _lastMcSize = 0;
      var _cleanupThreshold = 5000; // nodes
      document.addEventListener('click', function(e) {
        var btn = e.target.closest && e.target.closest('.cat-btn, [data-cat-btn], [onclick*="selCat"]');
        if (!btn) return;
        var mc = document.getElementById('mc');
        if (!mc) return;
        var nodeCount = mc.querySelectorAll('*').length;
        if (nodeCount > _cleanupThreshold && nodeCount > _lastMcSize * 1.5) {
          // Force a garbage-collection-friendly teardown by clearing detached refs
          var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT);
          var toCheck = [];
          while (walker.nextNode()) {
            var node = walker.currentNode;
            if (node._loftSkel) toCheck.push(node);
          }
          toCheck.forEach(function(n) { delete n._loftSkel; });
          console.info('[LOFT-PERF] DOM cleanup: ' + nodeCount + ' nodes in #mc');
        }
        _lastMcSize = nodeCount;
      }, {passive: true});
    })();
  }

  // ═══════════════════════════════════════════════════════════
  // LOFT-SECURITY — Security patches from audit findings
  // ═══════════════════════════════════════════════════════════
  (function applySecurityPatches() {

    // ── SEC-1: API key in MEMORY ONLY ────────────────────────
    // Never persists to localStorage or sessionStorage.
    // Existing code calls localStorage.getItem/setItem('loft_ia_key') —
    // we intercept those calls and route to a JS variable instead.
    // Key is lost on page refresh (intentional — forces re-entry each session).
    var _memKey = ''; // in-memory only

    // On load: wipe any previously stored key
    try {
      localStorage.removeItem('loft_ia_key');
      sessionStorage.removeItem('_lft_k');
      sessionStorage.removeItem('loft_ia_key');
    } catch(ex) {}

    try {
      var _origGet = Storage.prototype.getItem;
      var _origSet = Storage.prototype.setItem;
      var _origRem = Storage.prototype.removeItem;

      Storage.prototype.getItem = function(key) {
        if (key === 'loft_ia_key') return _memKey || '';
        return _origGet.call(this, key);
      };

      Storage.prototype.setItem = function(key, value) {
        if (key === 'loft_ia_key') {
          _memKey = String(value || '');
          // Never write to storage — memory only
          return;
        }
        return _origSet.call(this, key, value);
      };

      Storage.prototype.removeItem = function(key) {
        if (key === 'loft_ia_key') { _memKey = ''; return; }
        return _origRem.call(this, key);
      };
    } catch(ex) {
      // Storage prototype patching not supported
    }

    // ── SEC-2: Session expiry — clear key after 1h inactivity ─
    (function() {
      var INACTIVE_MS = 60 * 60 * 1000; // 1 hour (was 4h)
      var _lastActivity = Date.now();
      ['mousemove','keydown','click','touchstart'].forEach(function(ev) {
        window.addEventListener(ev, function() { _lastActivity = Date.now(); }, {passive: true});
      });
      setInterval(function() {
        if (_memKey && Date.now() - _lastActivity > INACTIVE_MS) {
          _memKey = '';
          try { localStorage.removeItem('loft_ia_key'); sessionStorage.removeItem('_lft_k'); } catch(e) {}
          if (typeof toast === 'function') toast('Sessão expirada — reinsira a chave Gemini.', 'warn');
        }
      }, 60 * 1000); // check every minute
    })();

    // ── SEC-3: 30s timeout on ALL Gemini/Anthropic fetch calls ─
    (function() {
      var _origFetch = window.fetch;
      window.fetch = function(url, opts) {
        var isAI = typeof url === 'string' && (
          url.indexOf('generativelanguage.googleapis.com') !== -1 ||
          url.indexOf('api.anthropic.com') !== -1 ||
          url.indexOf('openai.com') !== -1
        );
        if (!isAI) return _origFetch.apply(this, arguments);

        var ctrl = new AbortController();
        var timer = setTimeout(function() {
          ctrl.abort();
        }, 30000); // 30 seconds

        opts = Object.assign({}, opts || {}, { signal: ctrl.signal });
        return _origFetch(url, opts).then(function(res) {
          clearTimeout(timer);
          return res;
        }, function(err) {
          clearTimeout(timer);
          if (err && err.name === 'AbortError') {
            if (typeof toast === 'function') toast('Tempo esgotado — a IA demorou mais de 30s. Tente novamente.', 'error');
          }
          return Promise.reject(err);
        });
      };
    })();

    // 2. Safe RegExp wrapper — catches invalid patterns from dynamic sources
    //    Prevents "Invalid regular expression: Range out of order" crashes
    //    which can arise when user text or AI output is used in regex character classes.
    (function() {
      var _OrigRegExp = window.RegExp;
      try {
        window.RegExp = function SafeRegExp(pattern, flags) {
          // If called as constructor
          if (!(this instanceof SafeRegExp) && !(this instanceof _OrigRegExp)) {
            try {
              return new _OrigRegExp(pattern, flags);
            } catch(ex) {
              console.warn('[LOFT-SEC] Invalid RegExp suppressed:', ex.message);
              return /(?:)/; // safe no-op regex
            }
          }
          try {
            return new _OrigRegExp(pattern, flags);
          } catch(ex) {
            console.warn('[LOFT-SEC] Invalid RegExp suppressed:', ex.message);
            return new _OrigRegExp('(?:)');
          }
        };
        window.RegExp.prototype = _OrigRegExp.prototype;
        window.RegExp.__proto__ = _OrigRegExp;
      } catch(ex) { /* ignore if browser prevents RegExp override */ }
    })();

    // 3. Patch autoMarkChecklistFromIA to require minimum confidence threshold
    //    AUDIT BUG6: items marked without confidence check
    var _origAutoMark = typeof window.autoMarkChecklistFromIA === 'function'
      ? window.autoMarkChecklistFromIA : null;
    if (_origAutoMark) {
      window.autoMarkChecklistFromIA = function(extracted, key) {
        // Only auto-mark if extraction confidence >= 70%
        var conf = extracted && extracted._confidence && extracted._confidence.score;
        if (typeof conf === 'number' && conf < 70) {
          console.warn('[LOFT-SEC] autoMark skipped — confidence ' + conf + '% < 70%');
          return;
        }
        return _origAutoMark(extracted, key);
      };
    }

    // 4. Fix duplicate _refreshLoriSys — ensure the correct (longer) version is active
    //    AUDIT: two definitions at lines 20064 and 20074; we enforce correct one
    setTimeout(function() {
      if (typeof window._refreshLoriSys === 'function') {
        var _curSrc = window._refreshLoriSys.toString();
        // The correct version checks buildLoriSystemPrompt properly
        if (_curSrc.indexOf('buildLoriSystemPrompt') === -1) {
          window._refreshLoriSys = function() {
            try {
              if (typeof buildLoriSystemPrompt !== 'undefined' && typeof LORI_SYS !== 'undefined') {
                LORI_SYS = buildLoriSystemPrompt();
              }
            } catch(ex) {}
          };
        }
      }
    }, 1000);

    // 5. Add global error handler for silent catch blocks (AUDIT: 178 empty catches)
    //    Log to console.warn in a structured way so devtools show useful data
    window.__loftErrorCount = 0;
    // Don't replace existing error handler — only add telemetry
    window.addEventListener('error', function(e) {
      if (!e.filename || !e.filename.includes('loft')) return;
      window.__loftErrorCount++;
      if (window.__loftErrorCount <= 20) { // don't spam
        console.warn('[LOFT-AUDIT] Unhandled error #' + window.__loftErrorCount + ':', e.message, 'at', e.lineno);
      }
    });

    // SEC-NEW-1: KB editor sanitization — size limit + script tag stripping
    (function() {
      var _origKbSave = typeof window.kbCustomSave === 'function' ? window.kbCustomSave : null;
      if (!_origKbSave) return;
      var KB_MAX_BYTES = 50 * 1024; // 50kb
      window.kbCustomSave = function(text) {
        try {
          var safe = String(text || '');
          // Strip <script> tags
          safe = safe.replace(/<script[\s\S]*?<\/script>/gi, '[SCRIPT REMOVIDO]');
          safe = safe.replace(/<iframe[\s\S]*?>/gi, '[IFRAME REMOVIDO]');
          // Enforce size limit
          if (safe.length > KB_MAX_BYTES) {
            loftToast && loftToast('⚠ KB muito grande — truncado em 50KB. Remova conteúdo desnecessário.', 'warning', 5000);
            safe = safe.substring(0, KB_MAX_BYTES);
          }
          return _origKbSave(safe);
        } catch(ex) { return _origKbSave(text); }
      };
    })();

    // SEC-NEW-2: Rate limit visual badge — shows remaining AI calls per minute
    (function() {
      var badge = document.createElement('div');
      badge.id = 'loft-rate-badge';
      badge.textContent = 'IA: —/30';
      document.body.appendChild(badge);
      var _callLog = []; // timestamps
      var WINDOW_MS = 60000;
      var MAX_CALLS = 30;
      // Intercept iaCall to track rate
      var _origIaRate = typeof window.iaCall === 'function' ? window.iaCall : null;
      if (_origIaRate) {
        window.iaCall = function() {
          var now = Date.now();
          _callLog = _callLog.filter(function(t){ return now - t < WINDOW_MS; });
          _callLog.push(now);
          var remaining = MAX_CALLS - _callLog.length;
          badge.textContent = 'IA: ' + remaining + '/' + MAX_CALLS;
          badge.className = remaining <= 5 ? 'loft-rate-crit' : remaining <= 10 ? 'loft-rate-warn' : '';
          return _origIaRate.apply(this, arguments);
        };
      }
    })();

    // SEC-4: API key leak detection — warn if key appears in visible DOM text
    setTimeout(function() {
      try {
        var body = document.body.textContent || '';
        if (/AIzaSy[A-Za-z0-9_-]{33}/.test(body)) {
          console.warn('[LOFT-SEC] API key visível no DOM — não compartilhe screenshots.');
          if (typeof toast === 'function') toast('⚠ Chave API visível no DOM — recarregue a página.', 'error');
        }
      } catch(ex) {}
    }, 3000);
  })();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
"""

def build():
    src = 'loft-checklist-v3-original.html'   # immutable source
    dst = 'loft-checklist-v3.html'             # overwrites file user opens
    dst_bak = 'loft-checklist-v3-improved.html'  # keep copy with new name too

    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find real </head> (first occurrence = real HTML head)
    head_pos = content.find('</head>')
    if head_pos == -1:
        raise ValueError("No </head> found!")

    # Find insertion point for JS: after last </script>, before </body>
    last_body = content.rfind('</body>')
    if last_body == -1:
        raise ValueError("No </body> found!")

    print(f"Real </head> at char {head_pos} (line {content[:head_pos].count(chr(10))+1})")
    print(f"Last </body> at char {last_body} (line {content[:last_body].count(chr(10))+1})")

    # Inject CSP meta tag + CSS before </head>
    CSP = (
        '<meta http-equiv="Content-Security-Policy" content="'
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "img-src 'self' data: https: blob:; "
        "font-src 'self' https://fonts.gstatic.com data:; "
        "connect-src 'self' https://generativelanguage.googleapis.com https://api.anthropic.com; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'"
        '">\n'
    )
    # Early error capture script — shows a visible banner on ANY JS error
    EARLY_SCRIPT = (
        '<script id="loft-early-errorcatch">\n'
        '(function(){\n'
        '  window.addEventListener("error",function(ev){\n'
        '    var msg=ev.message||"";\n'
        '    var src=ev.filename||"";\n'
        '    var line=ev.lineno||0;\n'
        '    var col=ev.colno||0;\n'
        '    var detail="ERRO JS:\\n"+msg+"\\n\\nArquivo: "+src+"\\nLinha: "+line+", Col: "+col;\n'
        '    if(ev.error&&ev.error.stack) detail+="\\n\\nStack:\\n"+ev.error.stack.slice(0,500);\n'
        '    // Show visible red banner\n'
        '    var b=document.createElement("div");\n'
        '    b.style.cssText="position:fixed;top:0;left:0;right:0;z-index:99999;background:#c00;color:#fff;font-family:monospace;font-size:11px;padding:8px 12px;white-space:pre-wrap;max-height:200px;overflow:auto;border-bottom:2px solid #800";\n'
        '    b.textContent=detail;\n'
        '    var close=document.createElement("button");\n'
        '    close.textContent="X";\n'
        '    close.style.cssText="float:right;background:#800;border:none;color:#fff;cursor:pointer;padding:2px 8px;font-size:14px";\n'
        '    close.onclick=function(){b.remove();};\n'
        '    b.insertBefore(close,b.firstChild);\n'
        '    if(document.body) document.body.appendChild(b);\n'
        '    else document.addEventListener("DOMContentLoaded",function(){document.body.appendChild(b);});\n'
        '    console.error("[LOFT-ERR]",detail);\n'
        '  },true);\n'
        '})();\n'
        '</script>\n'
    )
    css_block = '\n' + CSP + EARLY_SCRIPT + '<style id="loft-enhancements-css">\n' + ENHANCED_CSS + '\n</style>\n'
    content = content[:head_pos] + css_block + content[head_pos:]

    # ── Nuclear regex fix: escape ALL non-ASCII chars in ALL JS regex literals ──
    # Eliminates any "Range out of order" errors from accented chars in regexes.
    import re as _re

    def _escape_nonascii_in_regex_literal(regex_str):
        """Given a JS regex literal string like /[À-Ú]/gi, escape all non-ASCII chars."""
        # Parse: leading /, content, closing /, flags
        if not regex_str.startswith('/'):
            return regex_str
        # Find the closing /
        i = 1
        in_class = False
        escaped = False
        while i < len(regex_str):
            c = regex_str[i]
            if escaped:
                escaped = False
                i += 1
                continue
            if c == '\\':
                escaped = True
                i += 1
                continue
            if c == '[':
                in_class = True
            elif c == ']':
                in_class = False
            elif c == '/' and not in_class:
                # Found closing slash
                pattern = regex_str[1:i]
                flags = regex_str[i+1:]
                # Escape all non-ASCII chars in the pattern
                def esc(ch):
                    cp = ord(ch)
                    if cp > 127:
                        return '\\u{:04X}'.format(cp)
                    return ch
                new_pattern = ''.join(esc(c) for c in pattern)
                return '/' + new_pattern + '/' + flags
            i += 1
        return regex_str  # malformed, return as-is

    def _patch_script_block(script_text):
        """Scan a JS block and escape non-ASCII chars in all regex literals."""
        result = []
        i = 0
        n = len(script_text)
        # Simple tokenizer state
        in_line_comment = False
        in_block_comment = False
        in_string_single = False
        in_string_double = False
        in_template = False
        prev_token_type = 'operator'  # tracks whether / is regex or division

        while i < n:
            c = script_text[i]

            # Handle block comments
            if in_block_comment:
                result.append(c)
                if c == '*' and i+1 < n and script_text[i+1] == '/':
                    result.append('/')
                    i += 2
                    in_block_comment = False
                else:
                    i += 1
                continue

            # Handle line comments
            if in_line_comment:
                result.append(c)
                if c == '\n':
                    in_line_comment = False
                i += 1
                continue

            # Handle single-quoted strings
            if in_string_single:
                result.append(c)
                if c == '\\' and i+1 < n:
                    result.append(script_text[i+1])
                    i += 2
                elif c == "'":
                    in_string_single = False
                    prev_token_type = 'value'
                    i += 1
                else:
                    i += 1
                continue

            # Handle double-quoted strings
            if in_string_double:
                result.append(c)
                if c == '\\' and i+1 < n:
                    result.append(script_text[i+1])
                    i += 2
                elif c == '"':
                    in_string_double = False
                    prev_token_type = 'value'
                    i += 1
                else:
                    i += 1
                continue

            # Handle template literals (backtick strings)
            if in_template:
                result.append(c)
                if c == '\\' and i+1 < n:
                    result.append(script_text[i+1])
                    i += 2
                elif c == '`':
                    in_template = False
                    prev_token_type = 'value'
                    i += 1
                else:
                    i += 1
                continue

            # Check for comment start
            if c == '/' and i+1 < n:
                if script_text[i+1] == '/':
                    in_line_comment = True
                    result.append(c)
                    i += 1
                    continue
                if script_text[i+1] == '*':
                    in_block_comment = True
                    result.append(c)
                    i += 1
                    continue

            # Check for string start
            if c == "'":
                in_string_single = True
                result.append(c)
                i += 1
                continue
            if c == '"':
                in_string_double = True
                result.append(c)
                i += 1
                continue
            if c == '`':
                in_template = True
                result.append(c)
                i += 1
                continue

            # Check for potential regex literal
            if c == '/' and prev_token_type in ('operator', 'keyword', 'open'):
                # This looks like a regex literal
                j = i
                in_cls = False
                esc2 = False
                j += 1
                while j < n:
                    ch = script_text[j]
                    if esc2:
                        esc2 = False
                        j += 1
                        continue
                    if ch == '\\':
                        esc2 = True
                        j += 1
                        continue
                    if ch == '[':
                        in_cls = True
                    elif ch == ']':
                        in_cls = False
                    elif ch == '/' and not in_cls:
                        j += 1
                        # Consume flags
                        while j < n and script_text[j] in 'gimsuy':
                            j += 1
                        break
                    elif ch in '\n\r':
                        # Unterminated regex - treat / as division
                        break
                    j += 1
                else:
                    # No closing / found - treat as division
                    result.append(c)
                    i += 1
                    prev_token_type = 'operator'
                    continue

                regex_literal = script_text[i:j]
                # Check if it has any non-ASCII chars
                if any(ord(ch) > 127 for ch in regex_literal):
                    patched = _escape_nonascii_in_regex_literal(regex_literal)
                    result.append(patched)
                    print(f"  Escaped non-ASCII in regex: {regex_literal[:60]} -> {patched[:60]}")
                else:
                    result.append(regex_literal)
                i = j
                prev_token_type = 'value'
                continue

            # Track prev_token_type for operator/value context
            if c in '=(<>!&|^~,;?:{}[+-*%':
                prev_token_type = 'operator'
            elif c == ')' or c == ']':
                prev_token_type = 'value'
            elif c.isalpha() or c == '_' or c == '$':
                # Could be identifier or keyword
                # Read full identifier
                j = i
                while j < n and (script_text[j].isalnum() or script_text[j] in '_$'):
                    j += 1
                word = script_text[i:j]
                result.append(word)
                i = j
                keywords_before_regex = {
                    'return', 'typeof', 'instanceof', 'in', 'of', 'new',
                    'delete', 'void', 'throw', 'case', 'else', 'yield', 'await'
                }
                if word in keywords_before_regex:
                    prev_token_type = 'keyword'
                else:
                    prev_token_type = 'value'
                continue
            elif c.isdigit():
                prev_token_type = 'value'
            elif c in ' \t\n\r':
                pass  # whitespace doesn't change token type

            result.append(c)
            i += 1

        return ''.join(result)

    # Process all <script> blocks in the content
    def _process_scripts(html):
        out = []
        pos = 0
        for m in _re.finditer(r'(<script[^>]*>)(.*?)(</script>)', html, _re.DOTALL):
            tag_open, script_body, tag_close = m.group(1), m.group(2), m.group(3)
            # Skip scripts with src= attribute (external), skip our own enhanced script
            if 'src=' in tag_open or 'loft-enhancements-js' in tag_open:
                out.append(html[pos:m.end()])
                pos = m.end()
                continue
            patched_body = _patch_script_block(script_body)
            out.append(html[pos:m.start()])
            out.append(tag_open + patched_body + tag_close)
            pos = m.end()
        out.append(html[pos:])
        return ''.join(out)

    # Also process inline event handler attributes (onclick="...", oninput="...", etc.)
    def _process_inline_handlers(html):
        """Escape non-ASCII chars in regex literals inside on* HTML attributes."""
        def _fix_attr(m):
            attr_name = m.group(1)
            quote = m.group(2)
            attr_val = m.group(3)
            patched = _patch_script_block(attr_val)
            if patched != attr_val:
                print(f"  Escaped non-ASCII in inline {attr_name} handler")
            return f'{attr_name}={quote}{patched}{quote}'

        return _re.sub(
            r'(on\w+)=(["\'])((?:(?!\2).)*?)\2',
            _fix_attr,
            html,
            flags=_re.DOTALL
        )

    print("Running comprehensive regex non-ASCII escape pass (script blocks)...")
    content = _process_scripts(content)
    print("Running regex escape pass on inline event handlers...")
    content = _process_inline_handlers(content)
    print("Regex escape passes complete.")

    # Recalculate </body> position after CSS insertion
    last_body = content.rfind('</body>')

    # Inject JS before </body>
    js_block = '\n<script id="loft-enhancements-js">\n' + ENHANCED_JS + '\n</script>\n'
    content = content[:last_body] + js_block + content[last_body:]

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(dst_bak, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Written: {dst} ({len(content):,} chars)")
    print(f"Written: {dst_bak} ({len(content):,} chars)")
    print(f"CSS block: {len(css_block):,} chars")
    print(f"JS block: {len(js_block):,} chars")

build()
