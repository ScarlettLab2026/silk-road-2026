/* ── Silk Road Story Engine ── */
/* Shared by all story pages. Each page must define STORY and STORY_CONFIG before loading this file. */

const TOTAL = STORY.length;

/* ── Map init ── */
const map = L.map('map', {
  zoomControl: false, attributionControl: false,
  center: STORY_CONFIG.mapCenter, zoom: STORY_CONFIG.mapZoom
});

let tileLayer;
function setTileLayer(mode) {
  if (tileLayer) map.removeLayer(tileLayer);
  const tiles = mode === 'light'
    ? 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png'
    : 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png';
  tileLayer = L.tileLayer(tiles, { maxZoom: 12 }).addTo(map);
}

// Mobile: enable zoom controls on small screens
if (window.innerWidth < 768) {
  map.zoomControl = L.control.zoom({ position: 'bottomright' });
  map.addControl(map.zoomControl);
}

/* ── Theme ── */
function applyTheme(mode) {
  if (mode === 'light') {
    document.body.classList.add('light');
    document.getElementById('theme-toggle').textContent = '🌙';
  } else {
    document.body.classList.remove('light');
    document.getElementById('theme-toggle').textContent = '☀️';
  }
  setTileLayer(mode);
}

function toggleTheme() {
  const isLight = document.body.classList.contains('light');
  const next = isLight ? 'dark' : 'light';
  localStorage.setItem('silk-road-theme', next);
  applyTheme(next);
}

// Restore saved theme
const savedTheme = localStorage.getItem('silk-road-theme') || 'dark';
applyTheme(savedTheme);

/* ── Data + Progress ── */
let DATA = null;
let currentChapter = 0;
let routeLines = [];
let cityMarkers = [];
let highlightMarkers = [];

fetch('data/silk-road.json').then(r => r.json()).then(d => {
  DATA = d;
  initProgress();
  renderChapter(0);
}).catch(() => {
  fetch('https://scarlettlab2026.github.io/silk-road-2026/data/silk-road.json')
    .then(r => r.json()).then(d => { DATA = d; initProgress(); renderChapter(0); });
});

function initProgress() {
  const el = document.getElementById('progress');
  el.innerHTML = STORY.map((_, i) =>
    `<div class="dot${i===0?' active':''}" id="dot${i}"></div>`
  ).join('');
}

function updateProgress(idx) {
  for (let i = 0; i < TOTAL; i++) {
    const d = document.getElementById('dot'+i);
    if (!d) continue;
    d.className = 'dot' + (i === idx ? ' active' : i < idx ? ' done' : '');
  }
}

/* ── Render Chapter ── */
function renderChapter(idx) {
  const ch = STORY[idx];
  currentChapter = idx;
  updateProgress(idx);

  document.getElementById('chNum').textContent = `第 ${idx+1} 章 / ${TOTAL}`;
  document.getElementById('chTitle').textContent = ch.subtitle;
  document.getElementById('chBody').textContent = ch.body;

  const card = document.getElementById('narrative');
  card.classList.add('fading');
  setTimeout(() => { card.classList.remove('fading'); }, 200);

  document.querySelector('#narrative .hint').innerHTML =
    idx < TOTAL - 1
      ? '<span class="arrow">→</span> 点击继续'
      : `<span style="font-size:1rem">${STORY_CONFIG.restartEmoji}</span> 点击重播`;

  map.flyTo([ch.lat, ch.lng], ch.zoom, { duration: 1.8, easeLinearity: 0.25 });

  routeLines.forEach(l => map.removeLayer(l)); routeLines = [];
  cityMarkers.forEach(m => map.removeLayer(m)); cityMarkers = [];
  highlightMarkers.forEach(m => map.removeLayer(m)); highlightMarkers = [];

  // Route polylines
  if (ch.route && DATA) {
    const pts = [];
    ch.route.forEach(nid => {
      const c = DATA.nodes.cities.find(cc => cc.id === nid);
      if (c) pts.push([c.lat, c.lng]);
    });
    if (pts.length >= 2) {
      routeLines.push(L.polyline(pts, {
        color: `rgba(${STORY_CONFIG.accentRgb},0.12)`, weight: 2, dashArray: '8 6'
      }).addTo(map));
      routeLines.push(L.polyline(pts, {
        color: `rgba(${STORY_CONFIG.accentRgb},0.8)`, weight: 3.5, dashArray: '12 4'
      }).addTo(map));
    }
  }

  // City markers
  if (ch.showCities && DATA) {
    ch.showCities.forEach(nid => {
      const c = DATA.nodes.cities.find(cc => cc.id === nid);
      if (!c) return;
      const isKey = nid === ch.marker || (ch.highlight && ch.highlight.includes(nid));
      const isStart = STORY_CONFIG.startCities.includes(nid);
      const m = L.circleMarker([c.lat, c.lng], {
        radius: isStart ? 8 : isKey ? 7 : 5,
        fillColor: isStart ? '#fff' : `var(--accent, ${STORY_CONFIG.accent})`,
        color: STORY_CONFIG.tileBg, weight: 1.5, fillOpacity: isKey ? 1 : 0.7
      }).addTo(map);
      m.bindTooltip(c.name, { direction: 'top', offset: [0, -6] });
      cityMarkers.push(m);
    });
  }

  // Highlight marker
  if (ch.marker && DATA) {
    const c = DATA.nodes.cities.find(cc => cc.id === ch.marker);
    if (c) {
      highlightMarkers.push(L.circleMarker([c.lat, c.lng], {
        radius: 14, fillColor: 'rgba(255,255,255,0.25)',
        color: 'transparent', fillOpacity: 0.6
      }).addTo(map));
      highlightMarkers.push(L.circleMarker([c.lat, c.lng], {
        radius: 8, fillColor: '#fff', color: STORY_CONFIG.tileBg, weight: 2, fillOpacity: 1
      }).addTo(map));
    }
  }

  // Badges
  const badgeRow = document.getElementById('badges');
  if (ch.highlight && DATA) {
    const colors = { figure: '#5b9bd5', goods: '#6aad6a', event: '#c75b3a' };
    badgeRow.innerHTML = ch.highlight.filter(id => id !== (ch.marker || '')).map(eid => {
      let entity = null, cat = '';
      for (const c of ['figures','goods','events']) {
        entity = DATA.nodes[c].find(n => n.id === eid);
        if (entity) { cat = c === 'figures' ? 'figure' : c === 'goods' ? 'goods' : 'event'; break; }
      }
      if (!entity) return '';
      const color = colors[cat];
      const label = entity.type || entity.category || entity.dynasty || '';
      return `<span style="display:inline-block;padding:4px 10px;margin:2px;border-radius:10px;font-size:0.73rem;border:1px solid ${color};color:${color};background:rgba(255,255,255,0.03)"><strong>${entity.name}</strong> <span style="opacity:0.7">${label}</span></span>`;
    }).join('');
  } else {
    badgeRow.innerHTML = '';
  }
}

/* ── Card toggle ── */
function toggleCard() {
  const card = document.getElementById('narrative');
  const btn = document.getElementById('toggle-card');
  card.classList.toggle('collapsed');
  btn.textContent = card.classList.contains('collapsed') ? '＋' : '─';
}

function advance() {
  const card = document.getElementById('narrative');
  if (card.classList.contains('collapsed')) {
    toggleCard();
    return;
  }
  if (currentChapter < TOTAL - 1) {
    renderChapter(currentChapter + 1);
  } else {
    restart();
  }
}

function restart() {
  routeLines.forEach(l => map.removeLayer(l)); routeLines = [];
  cityMarkers.forEach(m => map.removeLayer(m)); cityMarkers = [];
  highlightMarkers.forEach(m => map.removeLayer(m)); highlightMarkers = [];
  renderChapter(0);
}

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === ' ' || e.code === 'Space') {
    e.preventDefault(); advance();
  }
  if (e.key === 'ArrowLeft') {
    e.preventDefault();
    if (currentChapter > 0) renderChapter(currentChapter - 1);
  }
});
