#!/usr/bin/env python3
"""向丝路数据集中扩充海上丝绸之路节点和关系边。"""

import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'silk-road.json')

with open(DATA_PATH) as f:
    data = json.load(f)

new_cities = []
new_figures = []
new_goods = []
new_events = []
new_edges = []

# ═══════════════════════════════════════════
# 🏙 海上丝路港口城市
# ═══════════════════════════════════════════

new_cities = [
    {
        "id": "guangzhou",
        "name": "广州",
        "name_en": "Guangzhou (Canton)",
        "modern_name": "广州",
        "modern_name_en": "Guangzhou",
        "country": "中国",
        "country_en": "China",
        "lat": 23.1291,
        "lng": 113.2644,
        "era": "秦汉 — 今",
        "dynasties": ["秦", "汉", "唐", "宋", "元", "明", "清"],
        "role": "南海门户",
        "role_en": "Gateway to the South China Sea",
        "description": "中国最古老的海上贸易港口之一，唐代“广州通海夷道”的起点。阿拉伯、波斯、印度商人云集，市舶司最早在此设立。海上丝路的第一站。",
        "description_en": "One of China's oldest maritime trading ports and the starting point of the Tang dynasty 'Maritime Passage to Foreign Lands.' Arab, Persian, and Indian merchants gathered here — the first stop on the Maritime Silk Road.",
        "significance": 5
    },
    {
        "id": "malacca",
        "name": "马六甲",
        "name_en": "Malacca",
        "modern_name": "马六甲",
        "modern_name_en": "Melaka",
        "country": "马来西亚",
        "country_en": "Malaysia",
        "lat": 2.1896,
        "lng": 102.2501,
        "era": "15世纪 — 今",
        "dynasties": ["明", "清"],
        "role": "海峡咽喉",
        "role_en": "Strait Chokepoint",
        "description": "马六甲海峡的贸易枢纽，郑和七次下西洋五次在此驻泊。控制着印度洋与太平洋之间的咽喉要道，谁掌握了马六甲，谁就掌握了东西方贸易。",
        "description_en": "The trading hub of the Malacca Strait — Zheng He anchored here on five of his seven voyages. Controlling the narrow passage between the Indian and Pacific Oceans, whoever held Malacca held the key to East-West trade.",
        "significance": 5
    },
    {
        "id": "calicut",
        "name": "卡利卡特",
        "name_en": "Calicut (Kozhikode)",
        "modern_name": "科泽科德",
        "modern_name_en": "Kozhikode",
        "country": "印度",
        "country_en": "India",
        "lat": 11.2588,
        "lng": 75.7804,
        "era": "宋 — 明",
        "dynasties": ["宋", "元", "明"],
        "role": "香料海岸",
        "role_en": "Spice Coast Hub",
        "description": "印度马拉巴尔海岸的贸易中心，被称为“香料之城”。郑和的船队多次抵达这里，比达·伽马早了近一个世纪。胡椒、豆蔻、肉桂在此集散，运往中国和中东。",
        "description_en": "The trading center of India's Malabar Coast, known as the 'City of Spices.' Zheng He's fleet arrived here nearly a century before Vasco da Gama. Pepper, cardamom, and cinnamon were collected here and shipped to China and the Middle East.",
        "significance": 5
    },
    {
        "id": "colombo",
        "name": "科伦坡",
        "name_en": "Colombo",
        "modern_name": "科伦坡",
        "modern_name_en": "Colombo",
        "country": "斯里兰卡",
        "country_en": "Sri Lanka",
        "lat": 6.9271,
        "lng": 79.8612,
        "era": "汉 — 今",
        "dynasties": ["汉", "唐", "宋", "元", "明"],
        "role": "宝石之岛",
        "role_en": "Isle of Gems",
        "description": "古称“狮子国”或“锡兰”，以宝石和珍珠闻名。法显归国时在此停留两年，郑和船队在此立碑。印度洋航线的必经补给站。",
        "description_en": "Known to the ancients as the 'Lion Kingdom' or 'Ceylon,' famed for its gems and pearls. Faxian stayed here for two years on his return journey, and Zheng He erected a stele here. An essential resupply point on the Indian Ocean route.",
        "significance": 4
    },
    {
        "id": "hormuz",
        "name": "霍尔木兹",
        "name_en": "Hormuz",
        "modern_name": "霍尔木兹",
        "modern_name_en": "Hormuz",
        "country": "伊朗",
        "country_en": "Iran",
        "lat": 27.0957,
        "lng": 56.4528,
        "era": "元 — 明",
        "dynasties": ["元", "明"],
        "role": "波斯湾门户",
        "role_en": "Persian Gulf Gateway",
        "description": "波斯湾入口处的贸易岛城，马可·波罗和伊本·白图泰都曾到访。郑和船队第四次至第七次下西洋均在此停泊。中东香料、珍珠、骏马由此运往东方。",
        "description_en": "An island trading city at the mouth of the Persian Gulf, visited by both Marco Polo and Ibn Battuta. Zheng He's fleet docked here on voyages four through seven. Middle Eastern spices, pearls, and horses were shipped east from here.",
        "significance": 4
    },
    {
        "id": "aden",
        "name": "亚丁",
        "name_en": "Aden",
        "modern_name": "亚丁",
        "modern_name_en": "Aden",
        "country": "也门",
        "country_en": "Yemen",
        "lat": 12.8013,
        "lng": 45.0337,
        "era": "唐 — 明",
        "dynasties": ["唐", "宋", "元", "明"],
        "role": "红海入口",
        "role_en": "Red Sea Entrance",
        "description": "红海与印度洋交汇处的天然良港，乳香和没药的主要出口港。从非洲运来的象牙、黄金、奴隶在此集散，中国瓷器、丝绸由此进入阿拉伯世界。",
        "description_en": "A natural deep-water harbor where the Red Sea meets the Indian Ocean, and the main export hub for frankincense and myrrh. Ivory, gold, and slaves from Africa were transshipped here, while Chinese porcelain and silk entered the Arab world through this port.",
        "significance": 4
    },
    {
        "id": "alexandria",
        "name": "亚历山大",
        "name_en": "Alexandria",
        "modern_name": "亚历山大",
        "modern_name_en": "Alexandria",
        "country": "埃及",
        "country_en": "Egypt",
        "lat": 31.2001,
        "lng": 29.9187,
        "era": "公元前 — 今",
        "dynasties": ["罗马", "拜占庭", "阿拉伯"],
        "role": "地中海终点",
        "role_en": "Mediterranean Terminus",
        "description": "海上丝绸之路的西端终点。中国货物经印度洋、红海抵达此处，再转运至威尼斯、热那亚和欧洲各地。亚历山大图书馆曾是古代世界最伟大的知识中心。",
        "description_en": "The western terminus of the Maritime Silk Road. Chinese goods arrived here via the Indian Ocean and Red Sea, then were transshipped to Venice, Genoa, and across Europe. The Library of Alexandria was once the greatest repository of knowledge in the ancient world.",
        "significance": 5
    },
    {
        "id": "mombasa",
        "name": "蒙巴萨",
        "name_en": "Mombasa",
        "modern_name": "蒙巴萨",
        "modern_name_en": "Mombasa",
        "country": "肯尼亚",
        "country_en": "Kenya",
        "lat": -4.0435,
        "lng": 39.6682,
        "era": "唐 — 明",
        "dynasties": ["唐", "宋", "元", "明"],
        "role": "东非门户",
        "role_en": "East African Gateway",
        "description": "海上丝路在非洲的最远到达点之一。郑和船队曾抵达东非海岸，带回长颈鹿（被中国人误认为麒麟）。中国瓷器碎片至今在蒙巴萨海滩上被发现。",
        "description_en": "One of the farthest points reached by the Maritime Silk Road in Africa. Zheng He's fleet reached the East African coast and brought back a giraffe (mistaken by the Chinese for the mythical qilin). Chinese porcelain shards are still found on Mombasa's beaches to this day.",
        "significance": 5
    },
    {
        "id": "palembang",
        "name": "巨港（三佛齐）",
        "name_en": "Palembang (Srivijaya)",
        "modern_name": "巨港",
        "modern_name_en": "Palembang",
        "country": "印度尼西亚",
        "country_en": "Indonesia",
        "lat": -2.9761,
        "lng": 104.7754,
        "era": "唐 — 明",
        "dynasties": ["唐", "宋", "元", "明"],
        "role": "南海帝国",
        "role_en": "South Sea Empire",
        "description": "三佛齐（室利佛逝）帝国的都城，7至13世纪控制马六甲海峡的超级海上强权。义净在此学习梵文，前往印度取经前在此停留六个月。",
        "description_en": "Capital of the Srivijaya empire, a maritime superpower that controlled the Malacca Strait from the 7th to 13th centuries. The Chinese monk Yijing studied Sanskrit here, staying for six months before continuing to India.",
        "significance": 4
    }
]

# ═══════════════════════════════════════════
# 👤 海上丝路人物
# ═══════════════════════════════════════════

new_figures = [
    {
        "id": "zheng-he-figure",
        "name": "郑和",
        "name_en": "Zheng He",
        "type": "航海家 / 外交使节",
        "type_en": "Navigator / Diplomat",
        "era": "明",
        "era_range": "公元1371-1433年",
        "description": "明代伟大的航海家，原名马和。七次率领当时世界上最庞大的船队下西洋，航程遍及东南亚、印度、阿拉伯半岛和东非，比哥伦布早了近一个世纪。宝船长约137米，是当时世界上最大的木船。",
        "description_en": "The great Ming dynasty navigator. He led seven epic voyages across the Indian Ocean, reaching Southeast Asia, India, Arabia, and East Africa — nearly a century before Columbus. His treasure ships were about 137 meters long, the largest wooden vessels of their time.",
        "significance": 5
    },
    {
        "id": "wang-dayuan",
        "name": "汪大渊",
        "name_en": "Wang Dayuan",
        "type": "旅行家 / 著作家",
        "type_en": "Traveler / Writer",
        "era": "元",
        "era_range": "公元1311-1350年",
        "description": "元代民间航海家，两次从泉州出发远航，足迹遍布东南亚、印度、阿拉伯和东非。著有《岛夷志略》，记录了220多个国家和地区的地理、物产和风土人情，是中国第一部系统的海外地理著作。",
        "description_en": "A Yuan dynasty private navigator who sailed twice from Quanzhou, reaching Southeast Asia, India, Arabia, and East Africa. He wrote 'A Brief Account of Island Barbarians,' documenting over 220 countries and regions — China's first systematic work of overseas geography.",
        "significance": 4
    },
    {
        "id": "zhou-daguan",
        "name": "周达观",
        "name_en": "Zhou Daguan",
        "type": "使节 / 著作家",
        "type_en": "Envoy / Writer",
        "era": "元",
        "era_range": "公元1266-1346年",
        "description": "元代使节，随使团前往真腊（今柬埔寨），在吴哥居住一年。著有《真腊风土记》，详细记录了吴哥王朝的繁荣景象，是研究吴哥文明的唯一第一手文字史料。",
        "description_en": "A Yuan dynasty envoy who traveled to Zhenla (modern Cambodia) and lived in Angkor for a year. His book 'The Customs of Cambodia' provides the only first-hand written account of the Angkor civilization at its height.",
        "significance": 3
    }
]

# ═══════════════════════════════════════════
# 📦 海上丝路物产
# ═══════════════════════════════════════════

new_goods = [
    {
        "id": "frankincense",
        "name": "乳香",
        "name_en": "Frankincense",
        "category": "香料",
        "category_en": "Spice / Aromatic",
        "origin": "阿拉伯半岛 / 东非",
        "origin_en": "Arabian Peninsula / East Africa",
        "direction": "东传",
        "direction_en": "Eastward",
        "description": "从乳香树的树脂中提取的珍贵香料，用于宗教仪式、医药和化妆品。主要产于阿曼、也门和索马里，通过海上丝路大量输入中国。宋代香药贸易中乳香占据最大份额。",
        "description_en": "A precious aromatic resin from the Boswellia tree, used in religious ceremonies, medicine, and cosmetics. Mainly produced in Oman, Yemen, and Somalia, it was imported in vast quantities to China via the Maritime Silk Road — frankincense dominated Song dynasty incense trade.",
        "significance": 4
    },
    {
        "id": "myrrh",
        "name": "没药",
        "name_en": "Myrrh",
        "category": "香料 / 药材",
        "category_en": "Spice / Medicine",
        "origin": "阿拉伯半岛 / 东非",
        "origin_en": "Arabian Peninsula / East Africa",
        "direction": "东传",
        "direction_en": "Eastward",
        "description": "与乳香齐名的珍贵树脂，用作防腐、镇痛和宗教仪式。唐代《新修本草》首次记载没药的药用价值，海上贸易使其成为中国药材中的重要一味。",
        "description_en": "A precious resin alongside frankincense, used for preservation, pain relief, and religious rituals. First recorded in Chinese medicine during the Tang dynasty, maritime trade made it an important ingredient in traditional Chinese pharmacology.",
        "significance": 3
    },
    {
        "id": "ivory",
        "name": "象牙",
        "name_en": "Ivory",
        "category": "奢侈品",
        "category_en": "Luxury Good",
        "origin": "非洲 / 印度",
        "origin_en": "Africa / India",
        "direction": "东传",
        "direction_en": "Eastward",
        "description": "非洲和印度的大象象牙通过海上丝路大量输入中国，用于制作精美的雕刻品、朝笏和装饰品。宋代广州市舶司的进口清单中象牙是最大宗商品之一。",
        "description_en": "Elephant tusks from Africa and India were imported in large quantities via the Maritime Silk Road for exquisite carvings, court tablets, and ornaments. Ivory was one of the largest commodities in Guangzhou's customs records during the Song dynasty.",
        "significance": 3
    },
    {
        "id": "coral",
        "name": "红珊瑚",
        "name_en": "Red Coral",
        "category": "珍宝",
        "category_en": "Treasure",
        "origin": "地中海 / 红海",
        "origin_en": "Mediterranean / Red Sea",
        "direction": "东传",
        "direction_en": "Eastward",
        "description": "地中海和红海出产的珍贵红珊瑚，是佛教七宝之一。通过海上丝路输入，用于制作佛珠、首饰和朝珠。被视为富贵和吉祥的象征。",
        "description_en": "Precious red coral from the Mediterranean and Red Sea, counted among the Seven Treasures of Buddhism. Imported via the Maritime Silk Road for prayer beads, jewelry, and court ornaments — a symbol of wealth and good fortune.",
        "significance": 3
    },
    {
        "id": "clove",
        "name": "丁香",
        "name_en": "Clove",
        "category": "香料",
        "category_en": "Spice",
        "origin": "马鲁古群岛（香料群岛）",
        "origin_en": "Maluku Islands (Spice Islands)",
        "direction": "东传",
        "direction_en": "Eastward",
        "description": "原产于印度尼西亚马鲁古群岛的珍贵香料。汉代已有使用丁香的记载，用于口含除臭和调味。欧洲人对香料的渴望最终促成了大航海时代的开启。",
        "description_en": "A precious spice native to Indonesia's Maluku Islands (the legendary Spice Islands). Already used in Han dynasty China as a breath freshener and seasoning. Europe's craving for cloves and other spices eventually launched the Age of Discovery.",
        "significance": 4
    }
]

# ═══════════════════════════════════════════
# ⚡ 海上丝路事件
# ═══════════════════════════════════════════

new_events = [
    {
        "id": "maritime-trade-office",
        "name": "市舶司设立",
        "name_en": "Establishment of Maritime Trade Offices",
        "year": 714,
        "display_year": "公元714年（唐开元二年）",
        "dynasty": "唐",
        "description": "唐玄宗在广州设立中国历史上第一个市舶司，专门管理海上贸易、征收关税和接待外国使节。此后宋元明各朝在广州、泉州、明州（宁波）、杭州等地广设市舶司，海上丝路进入官方管理时代。",
        "description_en": "Emperor Xuanzong of Tang established China's first maritime trade office in Guangzhou (714 CE) to regulate sea trade, collect customs, and receive foreign envoys. Subsequent dynasties set up similar offices in Quanzhou, Ningbo, and Hangzhou — the Maritime Silk Road entered an era of official administration.",
        "significance": 4
    },
    {
        "id": "guangzhou-maritime-route",
        "name": "广州通海夷道",
        "name_en": "Guangzhou Maritime Route to Foreign Lands",
        "year": 750,
        "display_year": "公元8世纪中",
        "dynasty": "唐",
        "description": "唐代地理学家贾耽在《皇华四达记》中详细记录的海上航线：从广州出发，经南海、马六甲海峡、印度洋至波斯湾和东非。这是人类历史上最早有精确记录的远洋航线之一，全程约14000公里。",
        "description_en": "The maritime route meticulously recorded by Tang geographer Jia Dan: departing Guangzhou, crossing the South China Sea, through the Malacca Strait, across the Indian Ocean to the Persian Gulf and East Africa. One of the earliest precisely documented transoceanic routes in human history — approximately 14,000 km.",
        "significance": 5
    }
]

# ═══════════════════════════════════════════
# 🔗 关系边
# ═══════════════════════════════════════════

new_edges = [
    # ── 海上丝路港口链 ──
    {"source": "quanzhou", "target": "guangzhou", "relation": "海上姊妹港", "relation_en": "Sister maritime ports"},
    {"source": "guangzhou", "target": "palembang", "relation": "南海航线", "relation_en": "South China Sea route"},
    {"source": "palembang", "target": "malacca", "relation": "马六甲海峡航线", "relation_en": "Malacca Strait route"},
    {"source": "malacca", "target": "colombo", "relation": "印度洋东段", "relation_en": "Eastern Indian Ocean route"},
    {"source": "colombo", "target": "calicut", "relation": "印度洋香料航线", "relation_en": "Indian Ocean spice route"},
    {"source": "calicut", "target": "hormuz", "relation": "阿拉伯海航线", "relation_en": "Arabian Sea route"},
    {"source": "hormuz", "target": "aden", "relation": "波斯湾-红海航线", "relation_en": "Persian Gulf-Red Sea route"},
    {"source": "aden", "target": "alexandria", "relation": "红海-地中海转运", "relation_en": "Red Sea-Mediterranean transshipment"},
    {"source": "aden", "target": "mombasa", "relation": "东非航线", "relation_en": "East African route"},
    {"source": "calicut", "target": "mombasa", "relation": "印度洋西段", "relation_en": "Western Indian Ocean route"},

    # ── 海陆连接 ──
    {"source": "changan", "target": "guangzhou", "relation": "内河水陆联运", "relation_en": "Inland river-route connection"},
    {"source": "changan", "target": "quanzhou", "relation": "内河水陆联运", "relation_en": "Inland river-route connection"},
    {"source": "alexandria", "target": "constantinople", "relation": "地中海航线", "relation_en": "Mediterranean shipping route"},
    {"source": "hormuz", "target": "baghdad", "relation": "波斯湾-两河流域", "relation_en": "Persian Gulf-Mesopotamia route"},
    {"source": "aden", "target": "constantinople", "relation": "红海-地中海中转", "relation_en": "Red Sea-Mediterranean transit"},

    # ── 郑和 ──
    {"source": "zheng-he-figure", "target": "quanzhou", "relation": "驻泊港", "relation_en": "Anchorage port"},
    {"source": "zheng-he-figure", "target": "malacca", "relation": "重要驻泊地（五次停留）", "relation_en": "Key anchorage (stayed on 5 of 7 voyages)"},
    {"source": "zheng-he-figure", "target": "calicut", "relation": "多次抵达", "relation_en": "Arrived multiple times"},
    {"source": "zheng-he-figure", "target": "hormuz", "relation": "后四次均抵此", "relation_en": "Docked on voyages 4-7"},
    {"source": "zheng-he-figure", "target": "aden", "relation": "访问", "relation_en": "Visited"},
    {"source": "zheng-he-figure", "target": "mombasa", "relation": "东非最远到达点", "relation_en": "Farthest point in East Africa"},
    {"source": "zheng-he-figure", "target": "zheng-he", "relation": "主角", "relation_en": "Protagonist"},
    {"source": "zheng-he-figure", "target": "colombo", "relation": "立碑纪念", "relation_en": "Erected a commemorative stele"},

    # ── 汪大渊 ──
    {"source": "wang-dayuan", "target": "quanzhou", "relation": "出发地", "relation_en": "Departure point"},
    {"source": "wang-dayuan", "target": "palembang", "relation": "记录三佛齐风土", "relation_en": "Documented Srivijaya"},
    {"source": "wang-dayuan", "target": "calicut", "relation": "记录", "relation_en": "Documented"},
    {"source": "wang-dayuan", "target": "hormuz", "relation": "记录波斯湾贸易", "relation_en": "Documented Persian Gulf trade"},
    {"source": "wang-dayuan", "target": "aden", "relation": "抵达并记录", "relation_en": "Reached and documented"},

    # ── 周达观 ──
    {"source": "zhou-daguan", "target": "guangzhou", "relation": "出发地", "relation_en": "Departure point"},

    # ── 伊本·白图泰（已有）海上连接 ──
    {"source": "ibn-battuta", "target": "quanzhou", "relation": "称其为世界最大港", "relation_en": "Called it the world's largest port"},
    {"source": "ibn-battuta", "target": "calicut", "relation": "多次到访", "relation_en": "Visited multiple times"},
    {"source": "ibn-battuta", "target": "alexandria", "relation": "抵达", "relation_en": "Arrived"},

    # ── 法显（已有）海上归国连接 ──
    {"source": "faxian", "target": "colombo", "relation": "归国途中停留两年", "relation_en": "Stayed 2 years on return journey"},
    {"source": "faxian", "target": "palembang", "relation": "经海路归国经停", "relation_en": "Stopped on maritime return route"},

    # ── 义净（已有）海上连接 ──
    {"source": "yijing", "target": "guangzhou", "relation": "出发地", "relation_en": "Departure point"},
    {"source": "yijing", "target": "palembang", "relation": "停留学习梵文六个月", "relation_en": "Stayed 6 months to study Sanskrit"},

    # ── 物产与港口 ──
    {"source": "frankincense", "target": "aden", "relation": "主要出口港", "relation_en": "Main export port"},
    {"source": "frankincense", "target": "guangzhou", "relation": "主要进口港", "relation_en": "Main import port"},
    {"source": "myrrh", "target": "aden", "relation": "主要出口港", "relation_en": "Main export port"},
    {"source": "ivory", "target": "mombasa", "relation": "东非出口港", "relation_en": "East African export port"},
    {"source": "ivory", "target": "guangzhou", "relation": "主要进口港", "relation_en": "Main import port"},
    {"source": "coral", "target": "alexandria", "relation": "地中海产地", "relation_en": "Mediterranean origin"},
    {"source": "clove", "target": "malacca", "relation": "经马六甲转运", "relation_en": "Transshipped via Malacca"},
    {"source": "spices", "target": "calicut", "relation": "集散中心", "relation_en": "Distribution center"},
    {"source": "spices", "target": "malacca", "relation": "转运枢纽", "relation_en": "Transshipment hub"},

    # ── 事件与节点 ──
    {"source": "maritime-trade-office", "target": "guangzhou", "relation": "首个设立地", "relation_en": "First established here"},
    {"source": "guangzhou-maritime-route", "target": "guangzhou", "relation": "起点", "relation_en": "Starting point"},
    {"source": "guangzhou-maritime-route", "target": "malacca", "relation": "途经", "relation_en": "Via"},
    {"source": "guangzhou-maritime-route", "target": "hormuz", "relation": "终点之一", "relation_en": "One of the endpoints"},
    {"source": "zheng-he", "target": "zheng-he-figure", "relation": "主角", "relation_en": "Protagonist"},
    {"source": "zheng-he", "target": "malacca", "relation": "重要节点", "relation_en": "Key node"},
    {"source": "zheng-he", "target": "mombasa", "relation": "最远到达", "relation_en": "Farthest point reached"},
    {"source": "zheng-he", "target": "guangzhou", "relation": "途经", "relation_en": "Via"},

    # ── 现有节点海上补充 ──
    {"source": "tea", "target": "guangzhou", "relation": "海上出口港", "relation_en": "Maritime export port"},
    {"source": "porcelain", "target": "quanzhou", "relation": "海上出口港", "relation_en": "Maritime export port"},
    {"source": "porcelain", "target": "aden", "relation": "阿拉伯世界入口", "relation_en": "Entry to Arab world"},
    {"source": "silk", "target": "alexandria", "relation": "海上西传终点", "relation_en": "Maritime western terminus"},
]

# ═══════════════════════════════════════════
# 合并
# ═══════════════════════════════════════════

existing_ids = set()
for t in data['nodes']:
    for item in data['nodes'][t]:
        existing_ids.add(item['id'])

# 去重：跳过已存在的 id
for city in new_cities:
    if city['id'] not in existing_ids:
        data['nodes']['cities'].append(city)
        existing_ids.add(city['id'])
    else:
        print(f"⏭ 跳过重复城市: {city['id']}")

for fig in new_figures:
    if fig['id'] not in existing_ids:
        data['nodes']['figures'].append(fig)
        existing_ids.add(fig['id'])
    else:
        print(f"⏭ 跳过重复人物: {fig['id']}")

for good in new_goods:
    if good['id'] not in existing_ids:
        data['nodes']['goods'].append(good)
        existing_ids.add(good['id'])
    else:
        print(f"⏭ 跳过重复物产: {good['id']}")

for event in new_events:
    if event['id'] not in existing_ids:
        data['nodes']['events'].append(event)
        existing_ids.add(event['id'])
    else:
        print(f"⏭ 跳过重复事件: {event['id']}")

# 去重边
existing_edge_keys = set(
    (e['source'], e['target']) for e in data['edges']
)
added_edges = 0
for edge in new_edges:
    key = (edge['source'], edge['target'])
    if key not in existing_edge_keys:
        data['edges'].append(edge)
        existing_edge_keys.add(key)
        added_edges += 1
    else:
        print(f"⏭ 跳过重复边: {edge['source']} -> {edge['target']}")

# 更新版本号
data['meta']['version'] = '0.4.0'
data['meta']['last_updated'] = '2026-06-03'

# 保存
with open(DATA_PATH, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 统计
print(f"\n✅ 海上丝绸之路数据扩充完成！")
print(f"  新增城市: {len([c for c in new_cities if c['id'] in existing_ids])}")
print(f"  新增人物: {len([f for f in new_figures if f['id'] in existing_ids])}")
print(f"  新增物产: {len([g for g in new_goods if g['id'] in existing_ids])}")
print(f"  新增事件: {len([e for e in new_events if e['id'] in existing_ids])}")
print(f"  新增关系边: {added_edges}")
print(f"  版本: 0.3.0 → 0.4.0")
