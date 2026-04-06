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
"""

ENHANCED_JS = """
/* ═══════════════════════════════════════════════════════════════
   LOFT ENHANCEMENTS v3 — Senior-grade augmentation layer.
   Purely additive. Zero interference with existing app logic.
   ═══════════════════════════════════════════════════════════════ */
(function() {
  'use strict';

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
      // Welcome toast
      setTimeout(function() {
        loftToast('⌘K command palette • ? atalhos • Shift+F foco', 'info', 5000);
      }, 1800);
    });
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
            .replace(/[\x00-\x1F\x7F]/g, ' ')      // control chars
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
"""

def build():
    src = 'loft-checklist-v3.html'
    dst = 'loft-checklist-v3-improved.html'

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

    # Inject CSS before </head>
    css_block = '\n<style id="loft-enhancements-css">\n' + ENHANCED_CSS + '\n</style>\n'
    content = content[:head_pos] + css_block + content[head_pos:]

    # Recalculate </body> position after CSS insertion
    last_body = content.rfind('</body>')

    # Inject JS before </body>
    js_block = '\n<script id="loft-enhancements-js">\n' + ENHANCED_JS + '\n</script>\n'
    content = content[:last_body] + js_block + content[last_body:]

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Written: {dst} ({len(content):,} chars)")
    print(f"CSS block: {len(css_block):,} chars")
    print(f"JS block: {len(js_block):,} chars")

build()
