#!/usr/bin/env python3
"""v0.7.0 海上丝路增强: +3城 +2人物 +2物产 +2事件"""

import json

DATA_PATH = '/Users/scarlett/silk-road/data/silk-road.json'

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# ─── 新增城市 ───
new_cities = [
    {
        "id": "jeddah",
        "name": "吉达",
        "name_en": "Jeddah",
        "modern_name": "吉达",
        "country": "沙特阿拉伯",
        "lat": 21.5433,
        "lng": 39.1728,
        "description": "红海东岸最重要的港口城市，麦加的海上门户。每年无数朝圣者和商人经此往返于印度洋与地中海之间。明代郑和船队曾抵达吉达，中国使节在此换乘前往麦加。",
        "description_en": "The Red Sea's most vital port and maritime gateway to Mecca. Pilgrims and merchants transited between the Indian Ocean and Mediterranean here. Zheng He's fleet reached Jeddah, where Chinese envoys transferred for Mecca.",
        "significance": 4,
        "dynasties": ["唐", "宋", "元", "明"],
        "role": "红海贸易枢纽",
        "era": "唐—明"
    },
    {
        "id": "mogadishu",
        "name": "摩加迪沙",
        "name_en": "Mogadishu",
        "modern_name": "摩加迪沙",
        "country": "索马里",
        "lat": 2.0469,
        "lng": 45.3182,
        "description": "东非海岸重要贸易港口，以象牙、乳香、没药和黄金贸易闻名。郑和船队第四次至第七次下西洋均到访此地，费信《星槎胜览》中记载了木骨都束（摩加迪沙）的风土。",
        "description_en": "Major East African trade port known for ivory, frankincense, myrrh and gold. Zheng He's fleet visited on voyages 4-7. Fei Xin's 'Xingcha Shenglan' documented Mogadishu's customs and trade.",
        "significance": 4,
        "dynasties": ["宋", "元", "明"],
        "role": "东非贸易港",
        "era": "宋—明"
    },
    {
        "id": "surat",
        "name": "苏拉特",
        "name_en": "Surat",
        "modern_name": "苏拉特",
        "country": "印度",
        "lat": 21.1702,
        "lng": 72.8311,
        "description": "印度西海岸最大港口之一，莫卧儿帝国时期最重要的对外贸易门户。位于卡利卡特以北，波斯湾与印度洋航线在此交汇，中国瓷器、丝绸在此转口至波斯和阿拉伯。",
        "description_en": "One of India's largest western ports and the Mughal Empire's primary foreign trade gateway. Chinese porcelain and silk transshipped here to Persia and Arabia, linking Indian Ocean and Persian Gulf routes.",
        "significance": 4,
        "dynasties": ["元", "明"],
        "role": "印度西海岸枢纽",
        "era": "元—明"
    }
]

# ─── 新增人物 ───
new_figures = [
    {
        "id": "yighmish",
        "name": "亦黑迷失",
        "name_en": "Yighmish",
        "type": "航海家 / 外交使节",
        "era": "元",
        "era_range": "约1240-1300",
        "description": "回鹘航海家与外交官，忽必烈汗的重要海上使节。多次率船队从泉州出使南海和印度洋，到达过马八儿（印度科罗曼德海岸）、僧伽剌（斯里兰卡）等十余国。其航海活动为元代海上贸易铺平了道路。",
        "description_en": "Uyghur navigator and diplomat, Kublai Khan's key maritime envoy. Led multiple fleets from Quanzhou to Southeast Asia and the Indian Ocean, reaching over ten countries including Coromandel and Sri Lanka. His voyages paved the way for Yuan maritime trade.",
        "significance": 4
    },
    {
        "id": "yang-tingbi",
        "name": "杨庭璧",
        "name_en": "Yang Tingbi",
        "type": "外交使节 / 航海家",
        "era": "元",
        "era_range": "约1280-1340",
        "description": "元朝海上使节，多次奉命出使南海和印度洋。到达过马八儿（科罗曼德海岸）、俱蓝（奎隆）、苏门答腊等地，为元朝与印度洋诸国建立了外交联系，促进了海上丝路的官方往来。",
        "description_en": "Yuan dynasty maritime envoy who traveled repeatedly to Southeast Asia and the Indian Ocean. Reached Coromandel, Quilon, and Sumatra, establishing diplomatic ties between Yuan China and Indian Ocean kingdoms.",
        "significance": 3
    }
]

# ─── 新增物产 ───
new_goods = [
    {
        "id": "pearls",
        "name": "珍珠",
        "name_en": "Pearls",
        "category": "珍宝",
        "origin": "波斯湾 / 南海",
        "direction": "西→东 / 南→北",
        "description": "波斯湾和南海是全球最著名的天然珍珠产地。阿拉伯商人将波斯湾珍珠经印度洋和南海贩运至中国，合浦（广西北海）珍珠也经海上丝路出口。珍珠在宋元明时期是中国宫廷和贵族最珍视的奢侈品之一。",
        "description_en": "The Persian Gulf and South China Sea produced the world's finest natural pearls. Arab merchants shipped Gulf pearls to China via the Indian Ocean, while Hepu pearls from Guangxi were exported along the same routes. Pearls ranked among the most prized luxuries in Song-Yuan-Ming China.",
        "significance": 4
    },
    {
        "id": "sappanwood",
        "name": "苏木",
        "name_en": "Sappanwood",
        "category": "染料 / 药材",
        "origin": "东南亚",
        "direction": "南→北",
        "description": "苏木（苏枋木）产自东南亚热带地区，是古代最重要的红色染料之一，也可入药。宋代以后大量经海上丝路输入中国，用于染制官服、丝绸和漆器。明代郑和下西洋时苏木是主要贸易品之一。",
        "description_en": "Native to tropical Southeast Asia, sappanwood was one of the most important red dyes in the ancient world, also used medicinally. Mass-imported to China via the maritime Silk Road from the Song dynasty onward, dyeing official robes, silk, and lacquerware. A key trade item on Zheng He's voyages.",
        "significance": 3
    }
]

# ─── 新增事件 ───
new_events = [
    {
        "id": "yighmish-voyages",
        "name": "亦黑迷失出使",
        "name_en": "Yighmish's Maritime Missions",
        "year": 1284,
        "display_year": "1284-1295年",
        "dynasty": "元",
        "description": "1284年起，忽必烈汗派遣回鹘航海家亦黑迷失多次率船队从泉州出海，出使南海和印度洋诸国。到达马八儿（印度东海岸）、僧伽剌（斯里兰卡）、占城、爪哇等十余国，获取了大量海外地理信息，为元代海上贸易扩张奠定了基础。",
        "description_en": "From 1284, Kublai Khan dispatched the Uyghur navigator Yighmish on multiple maritime missions from Quanzhou to Southeast Asia and the Indian Ocean. He reached over ten kingdoms, gathering extensive geographic intelligence that laid the groundwork for Yuan maritime trade expansion.",
        "significance": 4
    },
    {
        "id": "wang-dayuan-voyages",
        "name": "汪大渊下西洋",
        "name_en": "Wang Dayuan's Maritime Travels",
        "year": 1330,
        "display_year": "1330-1339年",
        "dynasty": "元",
        "description": "元代民间航海家汪大渊两次从泉州搭乘商船出海，历时近十年，游历南海、印度洋各地，最远到达东非沿岸和红海。归国后著《岛夷志略》，记录了220多个国家和地区的风土物产，是研究14世纪海上丝路的珍贵一手资料。",
        "description_en": "The Yuan-era private navigator Wang Dayuan sailed twice from Quanzhou on merchant ships over nearly a decade, reaching as far as East Africa and the Red Sea. His book 'Daoyi Zhilue' records over 220 countries and regions — an invaluable firsthand account of 14th-century maritime Silk Road.",
        "significance": 5
    }
]

# ─── 新增关系边 ───
new_edges = [
    # ── 吉达 ──
    {"source": "jeddah", "target": "aden", "relation": "红海南北航线", "relation_en": "Red Sea north-south route"},
    {"source": "jeddah", "target": "alexandria", "relation": "红海→地中海贸易链", "relation_en": "Red Sea to Mediterranean trade chain"},
    {"source": "jeddah", "target": "hormuz", "relation": "红海→波斯湾航线", "relation_en": "Red Sea to Persian Gulf route"},
    {"source": "jeddah", "target": "frankincense", "relation": "乳香贸易中转", "relation_en": "frankincense trade hub"},
    {"source": "jeddah", "target": "myrrh", "relation": "没药贸易中转", "relation_en": "myrrh trade hub"},

    # ── 摩加迪沙 ──
    {"source": "mogadishu", "target": "mombasa", "relation": "东非沿岸航线", "relation_en": "East African coastal route"},
    {"source": "mogadishu", "target": "aden", "relation": "索马里→也门航线", "relation_en": "Somalia to Yemen route"},
    {"source": "mogadishu", "target": "ivory", "relation": "象牙输出港", "relation_en": "ivory export port"},
    {"source": "mogadishu", "target": "frankincense", "relation": "索马里乳香产地", "relation_en": "Somali frankincense source"},
    {"source": "mogadishu", "target": "zheng-he-figure", "relation": "郑和四次到访", "relation_en": "visited by Zheng He four times"},

    # ── 苏拉特 ──
    {"source": "surat", "target": "calicut", "relation": "印度西海岸航线", "relation_en": "Indian west coast route"},
    {"source": "surat", "target": "hormuz", "relation": "印度→波斯湾航线", "relation_en": "India to Persian Gulf route"},
    {"source": "surat", "target": "malacca", "relation": "印度→马六甲航线", "relation_en": "India to Malacca route"},
    {"source": "surat", "target": "cotton", "relation": "印度棉布出口港", "relation_en": "Indian cotton export port"},
    {"source": "surat", "target": "porcelain", "relation": "中国瓷器转口港", "relation_en": "Chinese porcelain transshipment"},

    # ── 亦黑迷失 ──
    {"source": "yighmish", "target": "quanzhou", "relation": "船队出发港", "relation_en": "fleet departure port"},
    {"source": "yighmish", "target": "calicut", "relation": "出使马八儿", "relation_en": "mission to Coromandel coast"},
    {"source": "yighmish", "target": "colombo", "relation": "出使僧伽剌", "relation_en": "mission to Sri Lanka"},
    {"source": "yighmish", "target": "palembang", "relation": "途经三佛齐", "relation_en": "passed through Srivijaya"},
    {"source": "yighmish", "target": "beijing", "relation": "受忽必烈派遣", "relation_en": "dispatched by Kublai Khan"},

    # ── 杨庭璧 ──
    {"source": "yang-tingbi", "target": "quanzhou", "relation": "出使出发港", "relation_en": "departure port"},
    {"source": "yang-tingbi", "target": "calicut", "relation": "出使俱蓝", "relation_en": "mission to Quilon"},
    {"source": "yang-tingbi", "target": "malacca", "relation": "途经马六甲", "relation_en": "passed through Malacca"},
    {"source": "yang-tingbi", "target": "yighmish", "relation": "同为元代海上使节", "relation_en": "fellow Yuan maritime envoy"},

    # ── 珍珠 ──
    {"source": "pearls", "target": "hormuz", "relation": "波斯湾珍珠原产地", "relation_en": "Persian Gulf pearl origin"},
    {"source": "pearls", "target": "guangzhou", "relation": "合浦珍珠经广州出口", "relation_en": "Hepu pearls exported via Guangzhou"},
    {"source": "pearls", "target": "calicut", "relation": "印度洋珍珠贸易", "relation_en": "Indian Ocean pearl trade"},
    {"source": "pearls", "target": "changan", "relation": "中国宫廷奢侈品", "relation_en": "Chinese court luxury item"},

    # ── 苏木 ──
    {"source": "sappanwood", "target": "palembang", "relation": "三佛齐苏木集散地", "relation_en": "Srivijaya sappanwood hub"},
    {"source": "sappanwood", "target": "malacca", "relation": "苏木贸易转运", "relation_en": "sappanwood transshipment"},
    {"source": "sappanwood", "target": "quanzhou", "relation": "输入中国主要港口", "relation_en": "primary Chinese import port"},
    {"source": "sappanwood", "target": "zheng-he-figure", "relation": "郑和船队主要贸易品", "relation_en": "key trade item on Zheng He's fleet"},

    # ── 亦黑迷失出使 ──
    {"source": "yighmish-voyages", "target": "yighmish", "relation": "主角", "relation_en": "protagonist"},
    {"source": "yighmish-voyages", "target": "quanzhou", "relation": "出发港", "relation_en": "departure port"},
    {"source": "yighmish-voyages", "target": "calicut", "relation": "到达印度东海岸", "relation_en": "reached Coromandel coast"},
    {"source": "yighmish-voyages", "target": "beijing", "relation": "受命于元大都", "relation_en": "commissioned from Khanbaliq"},

    # ── 汪大渊下西洋 ──
    {"source": "wang-dayuan-voyages", "target": "wang-dayuan", "relation": "主角", "relation_en": "protagonist"},
    {"source": "wang-dayuan-voyages", "target": "quanzhou", "relation": "出发港", "relation_en": "departure port"},
    {"source": "wang-dayuan-voyages", "target": "malacca", "relation": "记录满剌加", "relation_en": "documented Malacca"},
    {"source": "wang-dayuan-voyages", "target": "calicut", "relation": "记录古里佛", "relation_en": "documented Calicut"},
    {"source": "wang-dayuan-voyages", "target": "hormuz", "relation": "记录甘埋里", "relation_en": "documented Hormuz"},
    {"source": "wang-dayuan-voyages", "target": "aden", "relation": "记录哑靼", "relation_en": "documented Aden"},
    {"source": "wang-dayuan-voyages", "target": "mombasa", "relation": "记录层摇罗", "relation_en": "documented Mombasa coast"},
    {"source": "wang-dayuan-voyages", "target": "mogadishu", "relation": "记录木骨都束", "relation_en": "documented Mogadishu"},
]

# ─── 合并 ───
data['nodes']['cities'].extend(new_cities)
data['nodes']['figures'].extend(new_figures)
data['nodes']['goods'].extend(new_goods)
data['nodes']['events'].extend(new_events)
data['edges'].extend(new_edges)

# ─── 验证 ───
node_ids = set()
for cat in ['cities', 'figures', 'goods', 'events']:
    for n in data['nodes'][cat]:
        if n['id'] in node_ids:
            print(f'⚠️  DUPLICATE: {n["id"]}')
        node_ids.add(n['id'])

for i, e in enumerate(data['edges']):
    if e['source'] not in node_ids:
        print(f'⚠️  Edge {i}: source "{e["source"]}" NOT FOUND')
    if e['target'] not in node_ids:
        print(f'⚠️  Edge {i}: target "{e["target"]}" NOT FOUND')

print(f'\n✅ 城市: {len(data["nodes"]["cities"])} (海上: +3)')
print(f'✅ 人物: {len(data["nodes"]["figures"])} (+2)')
print(f'✅ 物产: {len(data["nodes"]["goods"])} (+2)')
print(f'✅ 事件: {len(data["nodes"]["events"])} (+2)')
print(f'✅ 关系边: {len(data["edges"])} (+{len(new_edges)})')

# ─── 更新版本 ───
data['meta']['version'] = '0.7.0'
data['meta']['last_updated'] = '2026-06-04'

# ─── 保存 ───
with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'✅ 版本: {data["meta"]["version"]}')
print('✅ 已保存')
