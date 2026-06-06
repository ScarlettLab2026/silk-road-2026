#!/usr/bin/env python3
"""修复孤立引用：+4城市 + 修正2条边"""

import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'silk-road.json')

with open(DATA_PATH, 'r') as f:
    data = json.load(f)

# ============================================================
# 1. 新增4个城市
# ============================================================
new_cities = [
    {
        "id": "balkh",
        "name": "巴里黑",
        "name_en": "Balkh",
        "modern_name": "巴尔赫",
        "modern_name_en": "Balkh",
        "country": "阿富汗",
        "country_en": "Afghanistan",
        "lat": 36.7550,
        "lng": 66.8975,
        "era": "公元前 — 13世纪",
        "dynasties": ["贵霜", "萨珊", "阿拉伯", "蒙古"],
        "role": "佛教中心 / 贸易枢纽",
        "role_en": "Buddhist Center / Trade Hub",
        "description": "中亚最古老的城市之一，古称蓝氏城、缚喝罗。贵霜帝国时期为大乘佛教重镇，拥有著名的Naw Bahār佛寺。青金石矿产地巴达赫尚即在其东南，是丝路上宝石贸易的源头城市。",
        "description_en": "One of Central Asia's most ancient cities, known in Chinese records as Lanshi or Boheluo. A major Mahayana Buddhist center under the Kushan Empire, home to the famed Naw Bahār monastery. The Badakhshan lapis lazuli mines lie to its southeast — Balkh sits at the source of the Silk Road's gemstone trade.",
        "significance": 4
    },
    {
        "id": "isfahan",
        "name": "伊斯法罕",
        "name_en": "Isfahan",
        "modern_name": "伊斯法罕",
        "modern_name_en": "Isfahan",
        "country": "伊朗",
        "country_en": "Iran",
        "lat": 32.6539,
        "lng": 51.6660,
        "era": "萨珊 — 萨法维",
        "dynasties": ["萨珊", "塞尔柱", "萨法维"],
        "role": "波斯手工业中心",
        "role_en": "Persian Craft Center",
        "description": "波斯帝国的核心城市之一，以地毯、银器、细密画和建筑艺术闻名世界。伊斯法罕的地毯和金属器皿经丝路传入中国和欧洲，被誉为'世界的一半'。",
        "description_en": "One of the Persian Empire's core cities, world-renowned for carpets, silverware, miniatures, and architecture. Isfahan's carpets and metalwork traveled the Silk Road to China and Europe — the city was called 'half the world.'",
        "significance": 4
    },
    {
        "id": "mecca",
        "name": "麦加",
        "name_en": "Mecca",
        "modern_name": "麦加",
        "modern_name_en": "Mecca",
        "country": "沙特阿拉伯",
        "country_en": "Saudi Arabia",
        "lat": 21.3891,
        "lng": 39.8579,
        "era": "7世纪 — 至今",
        "dynasties": ["倭马亚", "阿拔斯", "法蒂玛", "奥斯曼"],
        "role": "伊斯兰教圣城 / 朝圣中心",
        "role_en": "Islamic Holy City / Pilgrimage Center",
        "description": "伊斯兰教第一圣城，全球穆斯林朝觐（Hajj）目的地。阿拉伯半岛的贸易十字路口，连接红海、印度洋与地中海商路。杜环《经行记》是最早记录伊斯兰教和麦加朝觐的中文文献。",
        "description_en": "Islam's holiest city and destination of the Hajj pilgrimage. A crossroads of Arabian Peninsula trade, connecting the Red Sea, Indian Ocean, and Mediterranean routes. Du Huan's 'Jingxingji' is the earliest Chinese text to record Islam and the Meccan pilgrimage.",
        "significance": 5
    },
    {
        "id": "lhasa",
        "name": "拉萨",
        "name_en": "Lhasa",
        "modern_name": "拉萨",
        "modern_name_en": "Lhasa",
        "country": "中国",
        "country_en": "China",
        "lat": 29.6500,
        "lng": 91.1000,
        "era": "7世纪 — 至今",
        "dynasties": ["唐", "宋", "元", "明", "清"],
        "role": "吐蕃文化中心 / 茶马古道终点",
        "role_en": "Tibetan Cultural Center / Tea-Horse Road Terminus",
        "description": "吐蕃王朝都邑，藏传佛教圣地。茶马古道的终点站——云南和四川的茶叶经横断山脉运至此地，换取藏马和麝香。藏人'宁可三日无粮，不可一日无茶'，是丝路茶叶贸易的最大消费市场之一。",
        "description_en": "Capital of the Tibetan Empire and sacred city of Tibetan Buddhism. The Tea-Horse Road's terminus — tea from Yunnan and Sichuan crossed the Hengduan Mountains to reach Lhasa, traded for Tibetan horses and musk. Tibet's tea obsession ('better three days without food than one without tea') made it one of the Silk Road's largest tea markets.",
        "significance": 4
    },
]

# Add cities
existing_city_ids = {c['id'] for c in data['nodes']['cities']}
for city in new_cities:
    if city['id'] not in existing_city_ids:
        data['nodes']['cities'].append(city)
        print(f'  + 城市: {city["name"]} ({city["id"]})')

# ============================================================
# 2. 修正2条孤立边 (用已有城市替换region引用)
# ============================================================
edge_fixes = {
    ('faxian', 'sri-lanka'): 'colombo',    # 法显在师子国 → 科伦坡（斯里兰卡最大港）
    ('faxian', 'sumatra'): 'palembang',    # 法显在苏门答腊 → 室利佛逝（今巨港）
}

fixed = 0
for e in data['edges']:
    key = (e['source'], e['target'])
    if key in edge_fixes:
        old = e['target']
        e['target'] = edge_fixes[key]
        print(f'  ~ 边修正: {e["source"]} -> {old} → {e["target"]}')
        fixed += 1

# ============================================================
# 3. 追加新城市的关系边
# ============================================================
new_city_edges = [
    # 巴里黑
    {"source": "balkh", "target": "samarkand", "relation": "丝路节点", "relation_en": "Silk Road Node",
     "description": "巴里黑和撒马尔罕是粟特-巴克特里亚商路的两大枢纽"},
    {"source": "balkh", "target": "kashgar", "relation": "贸易路线", "relation_en": "Trade Route",
     "description": "巴里黑北越帕米尔高原可至喀什，是阿富汗通往西域的北线"},
    {"source": "balkh", "target": "buddhism", "relation": "佛教中心", "relation_en": "Buddhist Center",
     "description": "贵霜时期的巴里黑是大乘佛教在中亚的重要中心，Naw Bahār寺闻名丝路"},
    {"source": "balkh", "target": "xuanzang", "relation": "途经参访", "relation_en": "Visited",
     "description": "玄奘《大唐西域记》详细记录了巴里黑（缚喝罗国）的佛教遗迹"},

    # 伊斯法罕
    {"source": "isfahan", "target": "baghdad", "relation": "波斯文化圈", "relation_en": "Persian Cultural Sphere",
     "description": "伊斯法罕和巴格达是伊斯兰波斯文化的双城，手工业产品和艺术品互通"},
    {"source": "isfahan", "target": "samarkand", "relation": "丝路东传", "relation_en": "Silk Road Eastward",
     "description": "伊斯法罕的地毯和金属器皿经撒马尔罕沿丝路东传至中国"},
    {"source": "isfahan", "target": "nisapur", "relation": "呼罗珊商路", "relation_en": "Khurasan Trade Route",
     "description": "伊斯法罕和尼沙普尔是波斯高原东西两大商业中心，共同构成呼罗珊商路"},

    # 麦加
    {"source": "mecca", "target": "jeddah", "relation": "海上门户", "relation_en": "Maritime Gateway",
     "description": "吉达是麦加的红海门户港，朝圣者和商旅由此登陆前往麦加"},
    {"source": "mecca", "target": "aden", "relation": "红海-印度洋贸易", "relation_en": "Red Sea–Indian Ocean Trade",
     "description": "麦加商人与亚丁港连接红海和印度洋贸易圈，阿拉伯香料和非洲象牙由此北上"},
    {"source": "mecca", "target": "damascus", "relation": "朝圣商路", "relation_en": "Pilgrimage Trade Route",
     "description": "大马士革的朝圣商队每年经阿拉伯沙漠抵达麦加，形成固定商路"},
    {"source": "mecca", "target": "du-huan", "relation": "文字记录", "relation_en": "Textual Record",
     "description": "杜环《经行记》记录了伊斯兰教早期仪式和麦加天房，为最早的中文伊斯兰教记录之一"},

    # 拉萨
    {"source": "lhasa", "target": "changan", "relation": "唐蕃关系", "relation_en": "Tang-Tibetan Relations",
     "description": "拉萨和长安通过唐蕃古道相连，文成公主即由此入藏"},
    {"source": "lhasa", "target": "dunhuang", "relation": "青藏-丝路交汇", "relation_en": "Tibet–Silk Road Intersection",
     "description": "吐蕃强盛时期曾控制敦煌数十年，敦煌文书中有大量藏文文献"},
    {"source": "lhasa", "target": "samarkand", "relation": "麝香-茶叶贸易", "relation_en": "Musk–Tea Trade",
     "description": "青藏麝香经拉萨北上丝路抵撒马尔罕，同时茶叶由川滇入藏再西传中亚"},
]

existing_edge_keys = {(e['source'], e['target']) for e in data['edges']}
added = 0
for e in new_city_edges:
    key = (e['source'], e['target'])
    if key not in existing_edge_keys:
        edge = {
            "source": e['source'],
            "target": e['target'],
            "relation": e['relation'],
            "relation_en": e['relation_en'],
            "description": e.get('description', ''),
            "description_en": e.get('description_en', ''),
        }
        data['edges'].append(edge)
        existing_edge_keys.add(key)
        added += 1

print(f'  + 新城市关系边: {added} 条')

# ============================================================
# 4. 验证并保存
# ============================================================
# 验证无孤立边
valid_ids = set()
for cat in ['cities', 'figures', 'goods', 'events']:
    for node in data['nodes'][cat]:
        valid_ids.add(node['id'])
for r in data.get('routes', []):
    valid_ids.add(r['id'])

orphans = 0
for e in data['edges']:
    if e['source'] not in valid_ids or e['target'] not in valid_ids:
        orphans += 1
        if orphans <= 5:
            print(f'  ❌ 孤立: {e["source"]} -> {e["target"]}')

if orphans == 0:
    print('✅ 无孤立引用，数据完整')

# 更新版本
data['meta']['version'] = '1.2.0'
data['meta']['last_updated'] = '2026-06-06'

with open(DATA_PATH, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n=== 修复完成 ===')
print(f'城市: {len(data["nodes"]["cities"])} (+{len(new_cities)})')
print(f'人物: {len(data["nodes"]["figures"])}')
print(f'物产: {len(data["nodes"]["goods"])}')
print(f'事件: {len(data["nodes"]["events"])}')
print(f'关系边: {len(data["edges"])} (+{added+fixed})')
