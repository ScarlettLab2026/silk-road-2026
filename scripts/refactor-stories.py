#!/usr/bin/env python3
"""Refactor story files to use shared CSS/JS with per-story STORY_CONFIG."""
import re, sys, json

CONFIGS = {
    'story.html': {
        'title': '凿空西域 · 张骞的丝路',
        'bg': '#0d0d12', 'accent': '#d4a853',
        'accent_r': 212, 'accent_g': 168, 'accent_b': 83,
        'map_center': [38, 85], 'map_zoom': 4,
        'start_cities': ['changan', 'luoyang'], 'restart_emoji': '🐫',
        'text': '#e2ddcc', 'text_dim': '#9b9480',
    },
    'story2.html': {
        'title': '鲸波万里 · 郑和下西洋',
        'bg': '#0a1014', 'accent': '#5ea3b8',
        'accent_r': 94, 'accent_g': 163, 'accent_b': 184,
        'map_center': [15, 95], 'map_zoom': 3.5,
        'start_cities': ['quanzhou', 'guangzhou'], 'restart_emoji': '🚢',
        'text': '#dde4e8', 'text_dim': '#8a959b',
    },
    'story3.html': {
        'title': '万里求法 · 玄奘西行',
        'bg': '#0f0d0c', 'accent': '#c47a38',
        'accent_r': 196, 'accent_g': 122, 'accent_b': 56,
        'map_center': [35, 85], 'map_zoom': 3.5,
        'start_cities': ['changan', 'luoyang'], 'restart_emoji': '🕉️',
        'text': '#e8ddd0', 'text_dim': '#9b8d78',
    },
    'story4.html': {
        'title': '白绢扇归 · 法显西行',
        'bg': '#0c1110', 'accent': '#5d8a7c',
        'accent_r': 93, 'accent_g': 138, 'accent_b': 124,
        'map_center': [35, 85], 'map_zoom': 3.5,
        'start_cities': ['changan', 'luoyang'], 'restart_emoji': '🪷',
        'text': '#dde8e0', 'text_dim': '#8a9b90',
    },
    'story5.html': {
        'title': '东方见闻录 · 马可波罗东游',
        'bg': '#0f0b0a', 'accent': '#c2714e',
        'accent_r': 194, 'accent_g': 113, 'accent_b': 78,
        'map_center': [40, 60], 'map_zoom': 3,
        'start_cities': ['venice', 'beijing'], 'restart_emoji': '🏛',
        'text': '#e8ddd0', 'text_dim': '#9b8d7a',
    },
    'story6.html': {
        'title': '万里俘踪 · 杜环经行记',
        'bg': '#0d0c0a', 'accent': '#b08040',
        'accent_r': 176, 'accent_g': 128, 'accent_b': 64,
        'map_center': [35, 55], 'map_zoom': 3,
        'start_cities': ['samarkand', 'guangzhou'], 'restart_emoji': '🏜',
        'text': '#e6ddd0', 'text_dim': '#9b8d78',
    },
}

def extract_story_array(text):
    """Extract the STORY = [...] array from a story file."""
    # Find STORY = [
    start = text.index('const STORY = [')
    # Find matching ]; by bracket counting
    depth = 0
    i = start + len('const STORY = ')
    for j in range(i, len(text)):
        if text[j] == '[':
            depth += 1
        elif text[j] == ']':
            depth -= 1
            if depth == 0:
                # Need ];
                if j+1 < len(text) and text[j+1] == ';':
                    return text[i:j+2]  # Include the ];
                return text[i:j+1] + ';'
    raise ValueError("Could not find end of STORY array")

# NAV links for each file (using its own nav)
NAV_LINKS = '''  <a href="story.html">📖 张骞</a>
  <a href="story4.html">🪷 法显</a>
  <a href="story3.html">🧘 玄奘</a>
  <a href="story2.html">🚢 郑和</a>
  <a href="story5.html">🏛 马可·波罗</a>
  <a href="story6.html">🏜 杜环</a>
  <a href="story7.html">⚓ 汪大渊</a>'''

def build_html(filename, config):
    """Build refactored story HTML."""
    with open(filename, 'r') as f:
        original = f.read()

    story_array = extract_story_array(original)

    cfg = config
    a = cfg['accent']
    r, g, b = cfg['accent_r'], cfg['accent_g'], cfg['accent_b']

    # Nav with active on this file
    nav = NAV_LINKS.replace(f'href="{filename}"', f'href="{filename}" class="active"')

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{cfg['title']}</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<link rel="stylesheet" href="css/story-common.css" />
<style>
:root {{
  --bg: {cfg['bg']}; --card-bg: rgba({r},{g},{b},0.93); --accent: {a};
  --text: {cfg['text']}; --text-dim: {cfg['text_dim']}; --border: rgba(255,255,255,0.08);
  --accent-r: {r}; --accent-g: {g}; --accent-b: {b};
}}
</style>
</head>
<body>

<div id="map"></div>

<div id="story-nav">
{nav}
</div>

<div id="progress"></div>

<a href="index.html" id="back">← 返回地图</a>
<button id="theme-toggle" onclick="toggleTheme()">☀️</button>
<button id="restart" onclick="restart()">🔄 重播</button>

<div id="narrative" onclick="advance()">
  <button id="toggle-card" onclick="event.stopPropagation();toggleCard()" title="收起/展开">─</button>
  <div class="chapter-num" id="chNum"></div>
  <h2 id="chTitle"></h2>
  <p id="chBody"></p>
  <div id="badges" style="margin:8px 0 0;line-height:1.8"></div>
  <div class="hint"><span class="arrow">→</span> 点击继续</div>
</div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
const STORY_CONFIG = {{
  accent: '{a}',
  accentRgb: '{r},{g},{b}',
  mapCenter: {cfg['map_center']},
  mapZoom: {cfg['map_zoom']},
  startCities: {json.dumps(cfg['start_cities'])},
  restartEmoji: '{cfg['restart_emoji']}',
  tileBg: '{cfg['bg']}'
}};

const STORY = {story_array}
</script>
<script src="js/story-engine.js"></script>
</body></html>
'''

if __name__ == '__main__':
    for fname, cfg in CONFIGS.items():
        html = build_html(fname, cfg)
        with open(fname, 'w') as f:
            f.write(html)
        print(f'  ✅ {fname} refactored ({len(html)} bytes)')
    print('\\nAll 6 story files refactored!')
