#!/usr/bin/env python3
"""
从丝路知识图谱 JSON 自动生成多种内容形态。
用法:
  python3 scripts/generate-article.py article    # 生成公众号长文
  python3 scripts/generate-article.py poster     # 生成海报 HTML
  python3 scripts/generate-article.py cards      # 生成知识卡片（社交媒体用）
  python3 scripts/generate-article.py routes     # 生成人物路线描述
  python3 scripts/generate-article.py stats      # 打印数据统计
"""

import json
import sys
import os
from datetime import datetime

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'silk-road.json')

def load_data():
    with open(DATA_PATH) as f:
        return json.load(f)

def get(d, zh_key, en_key=None):
    """Bilingual field getter (defaults to zh)."""
    return d.get(zh_key, d.get(en_key or zh_key+'_en', ''))

# ─── 统计 ───
def print_stats(data):
    nodes = data['nodes']
    print(f"=== 丝路知识图谱统计 === (v{data['meta']['version']})")
    print(f"🏙  城市: {len(nodes['cities'])}")
    for c in nodes['cities']:
        print(f"   - {c['name']} ({c['name_en']}) [{c['era']}]")
    print(f"\n👤 人物: {len(nodes['figures'])}")
    for f in nodes['figures']:
        print(f"   - {f['name']} ({f['name_en']}) [{f['era']}]")
    print(f"\n📦 物产: {len(nodes['goods'])}")
    for g in nodes['goods']:
        print(f"   - {g['name']} ({g['name_en']}) [{g['direction']}]")
    print(f"\n⚡ 事件: {len(nodes['events'])}")
    for e in nodes['events']:
        print(f"   - {e['name']} ({e['name_en']}) [{e['dynasty']}]")
    print(f"\n🔗 关系边: {len(data['edges'])}")

# ─── 微信公众号长文 ───
def generate_article(data):
    nodes = data['nodes']
    out = f"""# 🐫 丝绸之路知识图谱：从长安到罗马

> 本文由丝路知识图谱 {data['meta']['version']} 版数据自动生成。
> 数据开放获取：https://github.com/ScarlettLab2026/silk-road-2026

---

## 一、丝路上的城市

丝路不是一条路，而是一张网。以下是沿线最重要的 {len(nodes['cities'])} 个节点城市：

"""
    for c in sorted(nodes['cities'], key=lambda x: x['significance'], reverse=True):
        out += f"""### {c['name']}（{c['name_en']}）

- 📍 今 {c['modern_name']}，{c['country']}
- 🕐 {c['era']}
- 🎯 {c['role']}
- {c['description']}

"""

    out += f"""---

## 二、推动丝路的人

{len(nodes['figures'])} 位人物，他们用脚步、信仰和野心编织了这张网：

"""
    for f in sorted(nodes['figures'], key=lambda x: x['significance'], reverse=True):
        out += f"""### {f['name']}（{f['name_en']}）

- 🏷 {f['type']} · {f['era_range']}
- {f['description']}

"""

    out += f"""---

## 三、丝路上的物产与技术

{len(nodes['goods'])} 种物产与技术，它们沿着丝路传播，改变了世界：

"""
    for g in sorted(nodes['goods'], key=lambda x: x['significance'], reverse=True):
        out += f"""### {g['name']}（{g['name_en']}）

- 📂 {g['category']} · 传播方向: {g['direction']}
- 🏠 原产地: {g['origin']}
- {g['description']}

"""

    out += f"""---

## 四、关键时刻

{len(nodes['events'])} 个历史事件，每一个都是丝路故事的转折点：

"""
    for e in sorted(nodes['events'], key=lambda x: x.get('year', 0)):
        year = e.get('display_year') or str(e.get('year', ''))
        out += f"""### {e['name']}（{e['name_en']}）

- 📅 {year} · {e['dynasty']}
- {e['description']}

"""

    out += """---

## 五、关系网络精选

"""
    # Pick the most interesting edges (connected to high-significance nodes)
    sig_map = {}
    for t in ['cities', 'figures', 'goods', 'events']:
        for n in nodes[t]:
            sig_map[n['id']] = n.get('significance', 3)
    ranked_edges = sorted(
        data['edges'],
        key=lambda e: sig_map.get(e['source'], 0) + sig_map.get(e['target'], 0),
        reverse=True
    )
    for e in ranked_edges[:15]:
        src_id = e['source']
        tgt_id = e['target']
        src_name = tgt_name = src_id
        for t in ['cities', 'figures', 'goods', 'events']:
            for n in nodes[t]:
                if n['id'] == src_id: src_name = n['name']
                if n['id'] == tgt_id: tgt_name = n['name']
        out += f"- **{src_name}** —{e['relation']}→ **{tgt_name}**\n"

    out += f"""

---

<p align="center">
  <i>凿空西域，连通世界。从长安到罗马，每一步都在创造历史。</i>
</p>

<p align="center" style="font-size:0.8em;color:#999">
  本文由丝路知识图谱自动生成 · 数据版本 {data['meta']['version']} · 生成时间 {datetime.now().strftime('%Y-%m-%d')}
</p>
"""
    return out

# ─── 海报 HTML ───
def generate_poster(data):
    nodes = data['nodes']
    stats = f"{len(nodes['cities'])}城 · {len(nodes['figures'])}人物 · {len(nodes['goods'])}物产 · {len(nodes['events'])}事件 · {len(data['edges'])}关联"
    cities_html = '\n'.join(
        f'<div class="city"><span class="dot"></span><strong>{c["name"]}</strong><small>{c["role"]}</small></div>'
        for c in sorted(nodes['cities'], key=lambda x: x['lng'])
    )
    figures_html = '\n'.join(
        f'<div class="figure"><span class="dot2"></span><strong>{f["name"]}</strong><small>{f["type"]}</small></div>'
        for f in sorted(nodes['figures'], key=lambda x: x['significance'], reverse=True)[:8]
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><title>丝路知识图谱 · 海报</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{display:flex;justify-content:center;align-items:center;min-height:100vh;background:#111;
  font-family:"Noto Serif SC","STSong",serif}}
.poster{{width:800px;min-height:1200px;background:linear-gradient(180deg,#1a1208 0%,#2a1f10 30%,#1a1208 100%);
  color:#e0d5c0;padding:60px;position:relative;overflow:hidden}}
.poster::before{{content:'';position:absolute;top:0;left:0;width:100%;height:100%;
  background:url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1200"><path d="M100,600 Q400,100 700,600" stroke="rgba(212,168,83,0.08)" fill="none" stroke-width="0.5"/><path d="M0,400 Q400,300 800,500" stroke="rgba(212,168,83,0.06)" fill="none"/></svg>');pointer-events:none}}
h1{{font-size:2.2em;text-align:center;font-weight:900;letter-spacing:0.15em;color:#d4a853;margin-bottom:6px}}
.sub{{text-align:center;font-size:0.9em;color:#9a9790;margin-bottom:30px}}
.stats{{text-align:center;font-size:0.85em;color:#d4a853;border:1px solid rgba(212,168,83,0.3);
  display:inline-block;padding:8px 20px;border-radius:20px;margin:0 auto 40px;display:block;width:fit-content}}
.section-title{{font-size:1.1em;color:#d4a853;border-bottom:1px solid rgba(212,168,83,0.2);padding-bottom:8px;margin-bottom:20px;margin-top:36px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px 24px}}
.city,.figure{{display:flex;align-items:center;gap:10px;font-size:0.85em;padding:6px 0}}
.dot,.dot2{{width:8px;height:8px;border-radius:50%;flex-shrink:0}}
.dot{{background:#d4a853}}
.dot2{{background:#5b9bd5}}
.city strong,.figure strong{{font-weight:600;color:#e0d5c0}}
.city small,.figure small{{color:#9a9790;margin-left:6px}}
.footer{{margin-top:40px;text-align:center;font-size:0.75em;color:#9a9790;border-top:1px solid rgba(212,168,83,0.1);padding-top:20px}}
.footer a{{color:#d4a853;text-decoration:none}}
</style></head>
<body>
<div class="poster">
<h1>🐫 丝绸之路 · 知识图谱</h1>
<div class="sub">Silk Road Knowledge Graph</div>
<div class="stats">{stats}</div>

<div class="section-title">🏙 沿线城市（东→西）</div>
<div class="grid">{cities_html}</div>

<div class="section-title">👤 关键人物</div>
<div class="grid">{figures_html}</div>

<div class="section-title">📦 物产传播</div>
<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:12px">
{"".join(f'<span style="background:rgba(106,173,106,0.2);color:#6aad6a;padding:4px 14px;border-radius:12px;font-size:0.8em">{g["name"]} <small style="color:#9a9790">{g["direction"]}</small></span>' for g in nodes['goods'][:8])}
</div>

<div class="section-title">⚡ 重大事件</div>
{"".join(f'<div style="padding:4px 0;font-size:0.82em"><span style="color:#c75b3a">●</span> {e["display_year"]} <strong>{e["name"]}</strong> <span style="color:#9a9790">{e["dynasty"]}</span></div>' for e in nodes['events'][:8])}

<div class="footer">
  数据开放获取 · CC BY-SA 4.0 · <a href="https://github.com/ScarlettLab2026/silk-road-2026">GitHub</a>
</div>
</div></body></html>"""

# ─── 知识卡片 ───
def generate_cards(data):
    """Generate social-media-friendly knowledge cards as text."""
    cards = []
    nodes = data['nodes']
    for f in sorted(nodes['figures'], key=lambda x: x['significance'], reverse=True)[:5]:
        cards.append(f"""📇 {f['name']}
🏷 {f['type']} · {f['era']}
📜 {f['description'][:120]}…
🔗 丝路知识图谱 · scarlettlab2026.github.io/silk-road-2026
""")
    return '\n---\n'.join(cards)

# ─── 人物路线描述 ───
def generate_routes(data):
    nodes = data['nodes']
    id_to_name = {}
    for t in ['cities', 'figures', 'goods', 'events']:
        for n in nodes[t]:
            id_to_name[n['id']] = n['name']

    figures_of_interest = ['zhang-qian', 'xuanzang', 'faxian', 'ban-chao', 'marco-polo']
    out = ''
    for fid in figures_of_interest:
        fig = next((f for f in nodes['figures'] if f['id'] == fid), None)
        if not fig: continue
        edges = [e for e in data['edges'] if e['source'] == fid or e['target'] == fid]
        cities_visited = []
        for e in edges:
            other = e['source'] if e['target'] == fid else e['target']
            name = id_to_name.get(other, other)
            rel = e['relation']
            if '途经' in rel or 'site' in rel.lower() or '经' in rel or 'point' in rel.lower():
                cities_visited.append(name)
        if cities_visited:
            out += f"### {fig['name']}的路线\n"
            out += f"长安 → {' → '.join(cities_visited)}\n\n"

    return out

# ─── Main ───
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python3 generate-article.py [article|poster|cards|routes|stats]")
        sys.exit(1)

    data = load_data()
    mode = sys.argv[1]

    if mode == 'article':
        out_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
        os.makedirs(out_dir, exist_ok=True)
        article = generate_article(data)
        path = os.path.join(out_dir, 'wechat-article.md')
        with open(path, 'w') as f:
            f.write(article)
        print(f"✅ 公众号文章已生成: {path}")

    elif mode == 'poster':
        out_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
        os.makedirs(out_dir, exist_ok=True)
        poster = generate_poster(data)
        path = os.path.join(out_dir, 'poster.html')
        with open(path, 'w') as f:
            f.write(poster)
        print(f"✅ 海报 HTML 已生成: {path}")

    elif mode == 'cards':
        print(generate_cards(data))

    elif mode == 'routes':
        print(generate_routes(data))

    elif mode == 'stats':
        print_stats(data)
