#!/usr/bin/env python3
"""v0.6.0 数据增强: +4城 +3人物 +3物产 +2事件 +新边"""

import json
from copy import deepcopy

DATA_PATH = '/Users/scarlett/silk-road/data/silk-road.json'

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# ─── 新增城市 ───
new_cities = [
    {
        "id": "damascus",
        "name": "大马士革",
        "name_en": "Damascus",
        "modern_name": "大马士革",
        "country": "叙利亚",
        "lat": 33.5138,
        "lng": 36.2765,
        "description": "倭马亚王朝首都，连接巴格达与地中海东岸的关键贸易枢纽，丝绸之路西段最重要的城市之一。阿拉伯帝国时期，来自东方的丝绸、瓷器、纸张在此集散转运至欧洲。",
        "description_en": "Umayyad capital, key trade hub linking Baghdad to the Mediterranean. Eastern silk, porcelain, and paper transshipped here to Europe during the Islamic Golden Age.",
        "significance": 5,
        "dynasties": ["唐", "宋", "元"],
        "role": "地中海东岸枢纽",
        "era": "唐—元"
    },
    {
        "id": "kucha",
        "name": "龟兹",
        "name_en": "Kucha",
        "modern_name": "新疆库车",
        "country": "中国",
        "lat": 41.7176,
        "lng": 82.9630,
        "description": "丝路北道最重要的佛教文化中心，鸠摩罗什出生地，克孜尔千佛洞所在地。龟兹乐舞驰名西域，琵琶、箜篌等乐器经此传入中原，深刻影响了隋唐音乐。",
        "description_en": "Northern Silk Road Buddhist center, birthplace of Kumarajiva, home to Kizil Caves. Kucha music and dance spread eastward, introducing the pipa and konghou to Tang China.",
        "significance": 5,
        "dynasties": ["汉", "晋", "唐"],
        "role": "北道佛国",
        "era": "汉—唐"
    },
    {
        "id": "gaochang",
        "name": "高昌",
        "name_en": "Gaochang",
        "modern_name": "新疆吐鲁番东",
        "country": "中国",
        "lat": 42.8627,
        "lng": 89.5313,
        "description": "丝路北道重要绿洲王国，位于吐鲁番盆地。玄奘西行途经高昌，国王鞠文泰与之结为兄弟并资助其西行。回鹘高昌王国时期佛教与摩尼教并盛。",
        "description_en": "Northern route oasis kingdom in the Turpan Basin. Xuanzang stopped here and King Qu Wentai sponsored his journey westward. Buddhist and Manichaean cultures flourished under the Uyghur kingdom.",
        "significance": 4,
        "dynasties": ["晋", "唐", "宋"],
        "role": "北道绿洲王国",
        "era": "晋—宋"
    },
    {
        "id": "venice",
        "name": "威尼斯",
        "name_en": "Venice",
        "modern_name": "威尼斯",
        "country": "意大利",
        "lat": 45.4408,
        "lng": 12.3155,
        "description": "中世纪欧洲丝路贸易的终点站与最大集散地。马可波罗的故乡，他的东方游记正是从威尼斯启程又在此写就。威尼斯商人通过地中海—红海—印度洋链条获取东方货物。",
        "description_en": "Medieval Europe's Silk Road terminus and entrepôt. Hometown of Marco Polo, whose travels began and were written here. Venetian merchants sourced Eastern goods via the Mediterranean-Red Sea-Indian Ocean chain.",
        "significance": 4,
        "dynasties": ["元", "明"],
        "role": "欧洲贸易终点",
        "era": "元—明"
    }
]

# ─── 新增人物 ───
new_figures = [
    {
        "id": "du-huan",
        "name": "杜环",
        "name_en": "Du Huan",
        "type": "旅行家 / 著作家",
        "era": "唐",
        "era_range": "751-762",
        "description": "唐代旅行家，怛罗斯之战中被大食军队俘虏，随军游历中亚、西亚、北非，到达过摩邻国（今肯尼亚或摩洛哥），历时11年后从海路乘商船回到广州。著《经行记》，是最早记载非洲的中国人。",
        "description_en": "Tang traveler captured at the Battle of Talas. Traveled through Central Asia, West Asia and North Africa over 11 years, reaching as far as modern Kenya/Morocco. Wrote 'Jingxingji', the earliest Chinese account of Africa.",
        "significance": 5
    },
    {
        "id": "qiu-chuji",
        "name": "丘处机",
        "name_en": "Qiu Chuji",
        "type": "道教宗师 / 旅行家",
        "era": "元",
        "era_range": "1148-1227",
        "description": "全真教长春真人，73岁高龄应成吉思汗之召，从山东莱州出发，经燕京、漠北、西域，远赴阿富汗兴都库什山觐见。弟子李志常著《长春真人西游记》，详录丝路沿途风土。",
        "description_en": "Daoist master who at 73 traveled from Shandong to Afghanistan to meet Genghis Khan. His disciple Li Zhichang's 'Travels of Master Changchun' records Silk Road geography and customs in vivid detail.",
        "significance": 4
    },
    {
        "id": "ma-huan",
        "name": "马欢",
        "name_en": "Ma Huan",
        "type": "翻译官 / 著作家",
        "era": "明",
        "era_range": "1380-1460",
        "description": "郑和船队的通事（翻译官），通晓阿拉伯语和波斯语，三次随郑和下西洋。著《瀛涯胜览》，以亲历者视角记录了占城、爪哇、马六甲、锡兰、卡利卡特、忽鲁谟斯、天方等20个国家和地区的风土人情。",
        "description_en": "Zheng He's Arabic-Persian interpreter who sailed on three voyages. His book 'Yingya Shenglan' records firsthand observations of 20 countries from Champa to Mecca, a cornerstone of pre-modern Chinese maritime literature.",
        "significance": 4
    }
]

# ─── 新增物产 ───
new_goods = [
    {
        "id": "cotton",
        "name": "棉布",
        "name_en": "Cotton Textiles",
        "category": "纺织品",
        "origin": "印度",
        "direction": "西→东",
        "description": "印度次大陆是世界上最早种植和纺织棉花的地区，棉布通过海上丝路和陆路传入中国。宋代以后棉织技术在中国推广，元代黄道婆改进棉纺技术，棉布逐渐取代麻布成为主要衣料。",
        "description_en": "Indian cotton textiles spread to China via maritime and overland Silk Roads. Cotton cultivation and weaving gradually replaced hemp as China's primary clothing material after the Song dynasty.",
        "significance": 4
    },
    {
        "id": "walnut",
        "name": "胡桃",
        "name_en": "Walnut",
        "category": "农作物",
        "origin": "西域/中亚",
        "direction": "西→东",
        "description": "原产中亚和波斯，张骞出使西域后引入中国，故称'胡桃'。汉唐时期在黄河流域广泛种植，成为中国重要的坚果作物和经济林木。",
        "description_en": "Native to Central Asia and Persia, introduced to China after Zhang Qian's mission westward, hence the Chinese name 'Hu Tao' (foreign peach). Widely cultivated in China since the Han-Tang period.",
        "significance": 3
    },
    {
        "id": "pipa",
        "name": "琵琶",
        "name_en": "Pipa (Lute)",
        "category": "乐器 / 文化",
        "origin": "波斯/中亚",
        "direction": "西→东",
        "description": "起源于波斯和中亚的曲项琵琶（乌德琴），经龟兹、于阗等西域城邦传入中国，与本土乐器融合演变为中国琵琶。唐代琵琶达到全盛，成为宫廷乐舞的核心乐器，敦煌壁画中大量出现琵琶演奏场景。",
        "description_en": "Originating from the Persian barbat (oud), the pipa traveled east through Kucha and Khotan, evolving into a uniquely Chinese instrument. It peaked during the Tang dynasty and appears extensively in Dunhuang murals.",
        "significance": 4
    }
]

# ─── 新增事件 ───
new_events = [
    {
        "id": "gan-ying-mission",
        "name": "甘英使大秦",
        "name_en": "Gan Ying's Mission to Rome",
        "year": 97,
        "display_year": "97年",
        "dynasty": "东汉",
        "description": "公元97年，班超派副使甘英出使大秦（罗马帝国）。甘英穿越安息（帕提亚），抵达条支（波斯湾沿岸），为安息商人以'航海需三年'为由劝阻，未能渡海到达罗马。但此行将中国人的地理认知向西推进到了波斯湾，是古代中国使者到达的最西端。",
        "description_en": "In 97 CE, Ban Chao sent envoy Gan Ying to Rome. He reached the Persian Gulf (Tiaozhi) but was dissuaded from crossing by Parthian merchants. Though he never reached Rome, he extended Chinese geographical knowledge to the Persian Gulf — the furthest west any ancient Chinese envoy reached.",
        "significance": 4
    },
    {
        "id": "du-huan-travels",
        "name": "杜环经行记",
        "name_en": "Du Huan's Travels",
        "year": 751,
        "display_year": "751-762年",
        "dynasty": "唐",
        "description": "751年怛罗斯之战中，唐军随军书记杜环被大食（阿拉伯帝国）俘虏，随后11年游历中亚、西亚和北非。到达过摩邻国（今肯尼亚或摩洛哥沿岸），成为第一个抵达非洲并留下文字记载的中国人。762年乘商船从海路回到广州，著《经行记》（原书已佚，《通典》引用了片段）。",
        "description_en": "Captured at the Battle of Talas (751), Du Huan traveled through the Abbasid Caliphate for 11 years, reaching as far as Africa. He returned by sea to Guangzhou in 762 and wrote 'Jingxingji' — the first Chinese account of Africa. The original text is lost but fragments survive in the 'Tongdian' encyclopedia.",
        "significance": 5
    }
]

# ─── 新增关系边 ───
new_edges = [
    # ── 大马士革 ──
    {"source": "damascus", "target": "baghdad", "relation": "伊拉克→叙利亚商路", "relation_en": "Iraq-Syria trade route"},
    {"source": "damascus", "target": "constantinople", "relation": "黎凡特→安纳托利亚", "relation_en": "Levant to Anatolia"},
    {"source": "damascus", "target": "samarkand", "relation": "倭马亚王朝东部边界", "relation_en": "Umayyad eastern frontier"},
    {"source": "damascus", "target": "alexandria", "relation": "叙利亚→埃及商路", "relation_en": "Syria-Egypt trade route"},
    {"source": "damascus", "target": "frankincense", "relation": "乳香消费中心", "relation_en": "major frankincense market"},

    # ── 龟兹 ──
    {"source": "kucha", "target": "kashgar", "relation": "塔里木北道 → 疏勒", "relation_en": "northern Tarim route to Kashgar"},
    {"source": "kucha", "target": "dunhuang", "relation": "北道东段 → 河西走廊", "relation_en": "eastern section to Hexi Corridor"},
    {"source": "kucha", "target": "kumarajiva", "relation": "出生地", "relation_en": "birthplace"},
    {"source": "kucha", "target": "xuanzang", "relation": "途经讲经", "relation_en": "visited and lectured"},
    {"source": "kucha", "target": "pipa", "relation": "龟兹乐舞 → 琵琶东传", "relation_en": "Kucha music: pipa's entry point to China"},
    {"source": "kucha", "target": "buddhism", "relation": "西域佛教中心", "relation_en": "Central Asian Buddhist hub"},

    # ── 高昌 ──
    {"source": "gaochang", "target": "dunhuang", "relation": "北道门户 → 河西咽喉", "relation_en": "northern route to Dunhuang"},
    {"source": "gaochang", "target": "turpan", "relation": "吐鲁番盆地邻城", "relation_en": "neighboring oasis in Turpan Basin"},
    {"source": "gaochang", "target": "kucha", "relation": "北道 → 龟兹", "relation_en": "northern route to Kucha"},
    {"source": "gaochang", "target": "xuanzang", "relation": "高昌王资助西行", "relation_en": "King of Gaochang sponsored his journey"},
    {"source": "gaochang", "target": "buddhism", "relation": "回鹘佛教中心", "relation_en": "Uyghur Buddhist center"},

    # ── 威尼斯 ──
    {"source": "venice", "target": "marco-polo", "relation": "故乡", "relation_en": "hometown"},
    {"source": "venice", "target": "constantinople", "relation": "地中海贸易链 → 东罗马", "relation_en": "Mediterranean trade to Byzantium"},
    {"source": "venice", "target": "alexandria", "relation": "威尼斯→亚历山大商路", "relation_en": "Venice-Alexandria trade route"},
    {"source": "venice", "target": "silk", "relation": "欧洲丝绸最大集散地", "relation_en": "Europe's largest silk entrepôt"},
    {"source": "venice", "target": "glass", "relation": "威尼斯玻璃闻名欧洲", "relation_en": "Venetian glass renown across Europe"},

    # ── 杜环 ──
    {"source": "du-huan", "target": "battle-of-talas", "relation": "被俘", "relation_en": "captured at"},
    {"source": "du-huan", "target": "baghdad", "relation": "游历阿拔斯都城", "relation_en": "visited Abbasid capital"},
    {"source": "du-huan", "target": "guangzhou", "relation": "乘商船归国", "relation_en": "returned by merchant ship"},
    {"source": "du-huan", "target": "mombasa", "relation": "可能到达摩邻国（东非）", "relation_en": "possibly reached East Africa (Molin)"},
    {"source": "du-huan", "target": "paper", "relation": "见证造纸术在撒马尔罕传播", "relation_en": "witnessed papermaking spread in Samarkand"},

    # ── 丘处机 ──
    {"source": "qiu-chuji", "target": "beijing", "relation": "燕京出发", "relation_en": "departed from Yanjing"},
    {"source": "qiu-chuji", "target": "samarkand", "relation": "经中亚大城", "relation_en": "passed through"},
    {"source": "qiu-chuji", "target": "suyab", "relation": "途经碎叶", "relation_en": "passed through Suyab"},
    {"source": "qiu-chuji", "target": "li-bai", "relation": "同属道教文化圈（时代不同）", "relation_en": "shared Daoist cultural tradition"},

    # ── 马欢 ──
    {"source": "ma-huan", "target": "zheng-he-figure", "relation": "随行翻译官", "relation_en": "interpreter on Zheng He's fleet"},
    {"source": "ma-huan", "target": "malacca", "relation": "记录满剌加风俗", "relation_en": "documented Malacca customs"},
    {"source": "ma-huan", "target": "calicut", "relation": "记录古里国", "relation_en": "documented Calicut"},
    {"source": "ma-huan", "target": "hormuz", "relation": "记录忽鲁谟斯", "relation_en": "documented Hormuz"},
    {"source": "ma-huan", "target": "quanzhou", "relation": "随船队从泉州出发", "relation_en": "departed from Quanzhou with the fleet"},

    # ── 棉布 ──
    {"source": "cotton", "target": "calicut", "relation": "印度棉布原产地", "relation_en": "Indian cotton origin"},
    {"source": "cotton", "target": "guangzhou", "relation": "海上丝路传入", "relation_en": "introduced via maritime route"},
    {"source": "cotton", "target": "malacca", "relation": "转运集散", "relation_en": "transshipment hub"},

    # ── 胡桃 ──
    {"source": "walnut", "target": "zhang-qian", "relation": "张骞从西域带回", "relation_en": "brought back by Zhang Qian"},
    {"source": "walnut", "target": "changan", "relation": "传入中国后广泛种植", "relation_en": "widely cultivated after introduction"},

    # ── 琵琶 ──
    {"source": "pipa", "target": "kucha", "relation": "经龟兹传入中原", "relation_en": "entered China through Kucha"},
    {"source": "pipa", "target": "changan", "relation": "唐代宫廷乐舞核心乐器", "relation_en": "core instrument of Tang court music"},
    {"source": "pipa", "target": "sogdian-silver", "relation": "粟特音乐文化影响", "relation_en": "influenced by Sogdian musical culture"},
    {"source": "pipa", "target": "dunhuang", "relation": "敦煌壁画中大量出现", "relation_en": "appears extensively in Dunhuang murals"},

    # ── 甘英使大秦 ──
    {"source": "gan-ying-mission", "target": "ban-chao", "relation": "班超派遣", "relation_en": "dispatched by Ban Chao"},
    {"source": "gan-ying-mission", "target": "nisapur", "relation": "途经安息（帕提亚）", "relation_en": "passed through Parthia"},
    {"source": "gan-ying-mission", "target": "an-shi-rebellion", "relation": "途经两河流域", "relation_en": "passed through Mesopotamia"},

    # ── 杜环经行记 ──
    {"source": "du-huan-travels", "target": "du-huan", "relation": "作者", "relation_en": "author"},
    {"source": "du-huan-travels", "target": "battle-of-talas", "relation": "怛罗斯之战被俘为起因", "relation_en": "triggered by capture at Talas"},
    {"source": "du-huan-travels", "target": "baghdad", "relation": "游历阿拔斯帝国", "relation_en": "traveled through Abbasid Caliphate"},
    {"source": "du-huan-travels", "target": "guangzhou", "relation": "海路归国终点", "relation_en": "returned by sea to"},
    {"source": "du-huan-travels", "target": "paper", "relation": "记载撒马尔罕造纸业", "relation_en": "documented Samarkand paper industry"},
]

# ─── 合并 ───
data['nodes']['cities'].extend(new_cities)
data['nodes']['figures'].extend(new_figures)
data['nodes']['goods'].extend(new_goods)
data['nodes']['events'].extend(new_events)
data['edges'].extend(new_edges)

# ─── 更新 meta ───
data['meta']['version'] = '0.6.0'
data['meta']['last_updated'] = '2026-06-04'

# ─── 验证 ───
node_ids = set()
for cat in ['cities', 'figures', 'goods', 'events']:
    for n in data['nodes'][cat]:
        if n['id'] in node_ids:
            print(f'⚠️  DUPLICATE ID: {n["id"]}')
        node_ids.add(n['id'])

for i, e in enumerate(data['edges']):
    if e['source'] not in node_ids:
        print(f'⚠️  Edge {i}: source "{e["source"]}" not found')
    if e['target'] not in node_ids:
        print(f'⚠️  Edge {i}: target "{e["target"]}" not found')

print(f'✅ 城市: {len(data["nodes"]["cities"])}')
print(f'✅ 人物: {len(data["nodes"]["figures"])}')
print(f'✅ 物产: {len(data["nodes"]["goods"])}')
print(f'✅ 事件: {len(data["nodes"]["events"])}')
print(f'✅ 关系边: {len(data["edges"])}')
print(f'✅ 版本: {data["meta"]["version"]}')

# ─── 保存 ───
with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('✅ 已保存到 data/silk-road.json')
