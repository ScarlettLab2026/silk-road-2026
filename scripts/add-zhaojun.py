#!/usr/bin/env python3
"""Add Wang Zhaojun related data: +3 cities +1 figure +23 edges for story17."""
import json
import sys

with open('data/silk-road.json', 'r') as f:
    d = json.load(f)

# ── New cities ──
new_cities = [
    {
        "id": "yanmenguan",
        "name": "雁门关",
        "name_en": "Yanmen Pass",
        "modern_name": "雁门关",
        "modern_name_en": "Yanmen Pass",
        "country": "中国",
        "country_en": "China",
        "lat": 39.18,
        "lng": 112.85,
        "era": "公元前 — 今",
        "dynasties": ["战国", "秦汉", "北朝", "隋唐", "宋", "明"],
        "role": "长城雄关",
        "role_en": "Great Wall Fortress Pass",
        "description": "位于山西代县北部的长城要塞，是汉朝北出草原的咽喉。王昭君出塞经由此关，在马上弹琵琶作别中原，传说大雁闻声坠落——「落雁」典故即源于此。后世成为长城九大名关之一。",
        "description_en": "A strategic Great Wall fortress in northern Shanxi, the gateway from Han China to the steppe. Wang Zhaojun passed through this pass on her journey north, playing the pipa atop her horse — legend says a wild goose heard the music, forgot to flap its wings, and fell from the sky, giving rise to her epithet 'luoyan' (bird-felling beauty). Later became one of the nine great passes of the Great Wall.",
        "significance": 4
    },
    {
        "id": "longting",
        "name": "匈奴龙庭",
        "name_en": "Xiongnu Longting (Royal Court)",
        "modern_name": "蒙古乌兰巴托以南",
        "modern_name_en": "South of Ulaanbaatar, Mongolia",
        "country": "蒙古",
        "country_en": "Mongolia",
        "lat": 41.0,
        "lng": 111.5,
        "era": "公元前3世纪 — 公元2世纪",
        "dynasties": ["匈奴"],
        "role": "匈奴单于王庭",
        "role_en": "Xiongnu Chanyu's Royal Court",
        "description": "匈奴帝国的心脏——单于的穹庐王帐所在地。没有城墙和宫殿，只有连绵的毡帐和成群的牛羊。公元前33年王昭君远嫁至此，被封为宁胡阏氏（使胡人安宁的王后）。此后六十余年间，这里成为汉匈两大文明的交汇点：南来的丝绸漆器、北往的骏马毛皮在此交换，是丝路北线最北端的重要节点。",
        "description_en": "The heart of the Xiongnu Empire — the Chanyu's royal encampment. No city walls, no palaces — only endless felt tents and herds. In 33 BCE, Wang Zhaojun arrived here to marry the Chanyu and was crowned Ninghu Yanzhi ('Queen Who Brings Peace to the Hu'). For over sixty years thereafter, this became a meeting point of Han and Xiongnu civilizations, where southern silks and lacquerwares exchanged for northern horses and furs — the northernmost key node of the northern Silk Road.",
        "significance": 4
    },
    {
        "id": "hohhot",
        "name": "青冢（呼和浩特）",
        "name_en": "Qingzhong (Hohhot)",
        "modern_name": "呼和浩特",
        "modern_name_en": "Hohhot",
        "country": "中国",
        "country_en": "China",
        "lat": 40.82,
        "lng": 111.75,
        "era": "公元前 — 今",
        "dynasties": ["西汉", "北魏", "唐", "辽", "元", "明", "清"],
        "role": "草原丝路重要节点",
        "role_en": "Grassland Silk Road Node",
        "description": "位于大青山南麓，阴山脚下的草原丝路驿站。城郊的「青冢」是王昭君墓——相传墓上青草四季不枯，在秋季枯黄的草原上尤为显眼。两千年来，青冢成为草原丝路上的重要地标。呼和浩特后来发展为漠南蒙古的政治与商业中心，是中原通往草原和蒙古高原的必经之地。",
        "description_en": "At the southern foot of the Daqing Mountains, a grassland Silk Road post station. The 'Qingzhong' (Green Tomb) on the outskirts is Wang Zhaojun's burial site — legend says the grass atop her tomb stays green year-round, visible against the autumn-yellowed steppe. For two millennia the Qingzhong has been a landmark on the grassland Silk Road. The city later developed into the political and commercial center of southern Mongolia, a gateway from China proper to the Mongolian Plateau.",
        "significance": 4
    }
]

# ── New figure: 呼韩邪单于 ──
new_figure = {
    "id": "huhanye",
    "name": "呼韩邪单于",
    "name_en": "Huhanye Chanyu",
    "type": "匈奴单于",
    "type_en": "Xiongnu Chanyu",
    "era": "西汉",
    "era_range": "? — 公元前31年",
    "description": "匈奴分裂后的南单于，第一位臣服汉朝的匈奴最高统治者。公元前53年率部归汉，三次亲赴长安朝见。公元前33年求娶汉女，王昭君自请出嫁，汉元帝以「竟宁」（边境安宁）为年号送嫁。此后汉匈边境六十余年无大战，商路畅通。他的臣服和联姻开启了汉匈关系的全新时代。",
    "description_en": "The Southern Chanyu after the Xiongnu split, and the first supreme Xiongnu ruler to submit to the Han Dynasty. He led his tribe to submit in 53 BCE and visited Chang'an three times in person. In 33 BCE he sought a Han bride; Wang Zhaojun volunteered, and Emperor Yuan adopted the era name 'Jingning' (Border Pacified) to mark the marriage. The Han-Xiongnu border saw no major warfare for over sixty years thereafter, keeping trade routes open. His submission and marriage alliance inaugurated an entirely new era in Han-Xiongnu relations.",
    "significance": 4
}

# ── New edges ──
new_edges = [
    # 王昭君 ↔ 新城
    {"source": "wang-zhaojun", "target": "yanmenguan", "relation": "出塞途经", "relation_en": "passed through on journey north"},
    {"source": "wang-zhaojun", "target": "longting", "relation": "远嫁归宿", "relation_en": "marriage destination"},
    {"source": "wang-zhaojun", "target": "hohhot", "relation": "葬于青冢", "relation_en": "buried at Qingzhong"},
    # 王昭君 ↔ 已有城
    {"source": "wang-zhaojun", "target": "luoyang", "relation": "南郡秭归人 → 汉宫 → 出塞", "relation_en": "from Zigui to Han palace to beyond the pass"},
    {"source": "wang-zhaojun", "target": "liangzhou", "relation": "出塞途中", "relation_en": "on the route north"},
    # 王昭君 ↔ 呼韩邪
    {"source": "wang-zhaojun", "target": "huhanye", "relation": "和亲联姻", "relation_en": "heqin marriage"},
    # 呼韩邪 ↔ 城市
    {"source": "huhanye", "target": "changan", "relation": "三次朝见", "relation_en": "paid tribute three times"},
    {"source": "huhanye", "target": "longting", "relation": "单于王庭驻地", "relation_en": "Chanyu royal court seat"},
    {"source": "huhanye", "target": "yanmenguan", "relation": "迎亲南下", "relation_en": "traveled south to welcome bride"},
    # 呼韩邪 ↔ 事件
    {"source": "huhanye", "target": "zhaojun-marriage", "relation": "迎娶汉女", "relation_en": "married Han woman"},
    # 昭君出塞事件 ↔ 地点
    {"source": "zhaojun-marriage", "target": "changan", "relation": "出发地", "relation_en": "departure point"},
    {"source": "zhaojun-marriage", "target": "yanmenguan", "relation": "出关节点", "relation_en": "border crossing point"},
    {"source": "zhaojun-marriage", "target": "longting", "relation": "目的地", "relation_en": "destination"},
    {"source": "zhaojun-marriage", "target": "hohhot", "relation": "青冢所在", "relation_en": "burial site location"},
    # 丝路关联
    {"source": "changan", "target": "yanmenguan", "relation": "北出草原通道", "relation_en": "northern steppe route"},
    {"source": "yanmenguan", "target": "longting", "relation": "汉—匈通道", "relation_en": "Han-Xiongnu passage"},
    {"source": "longting", "target": "hohhot", "relation": "草原丝路节点", "relation_en": "grassland Silk Road nodes"},
    # 丝路北线商贸
    {"source": "hohhot", "target": "changan", "relation": "草原丝路南段", "relation_en": "southern grassland Silk Road"},
    {"source": "longting", "target": "changan", "relation": "朝贡与互市通道", "relation_en": "tribute and trade route"},
    # 王昭君 ↔ 事件
    {"source": "wang-zhaojun", "target": "zhaojun-marriage", "relation": "主角（和亲公主）", "relation_en": "protagonist (heqin princess)"},
    # 文化影响
    {"source": "wang-zhaojun", "target": "changan", "relation": "汉宫起点", "relation_en": "Han palace origin point"},
    # 汉匈和平与商贸
    {"source": "huhanye", "target": "longting", "relation": "统治中心", "relation_en": "seat of power"},
]

# ── Apply additions ──
added_cities = 0
existing_city_ids = {c['id'] for c in d['nodes']['cities']}
for city in new_cities:
    if city['id'] not in existing_city_ids:
        d['nodes']['cities'].append(city)
        added_cities += 1

added_figures = 0
existing_figure_ids = {f['id'] for f in d['nodes']['figures']}
if new_figure['id'] not in existing_figure_ids:
    d['nodes']['figures'].append(new_figure)
    added_figures += 1

# Deduplicate edges
existing_edge_keys = {(e['source'], e['target'], e['relation']) for e in d['edges']}
added_edges = 0
for edge in new_edges:
    key = (edge['source'], edge['target'], edge['relation'])
    if key not in existing_edge_keys:
        d['edges'].append(edge)
        added_edges += 1

# Update meta
d['meta']['version'] = 'v1.15.0'
d['meta']['last_updated'] = '2026-07-23'

# Write
with open('data/silk-road.json', 'w') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"✅ Added: {added_cities} cities, {added_figures} figures, {added_edges} edges")
print(f"📊 New totals: {len(d['nodes']['cities'])} cities, {len(d['nodes']['figures'])} figures, {len(d['edges'])} edges")
print(f"📦 Version: {d['meta']['version']}")
