#!/usr/bin/env python3
"""
数据增强脚本 v2 — v1.2.0
新增: 6物产 + 5事件 + 52关系边
"""

import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'silk-road.json')

with open(DATA_PATH, 'r') as f:
    data = json.load(f)

# ============================================================
# 1. 新增物产 (6 goods)
# ============================================================
new_goods = [
    {
        "id": "lapis-lazuli",
        "name": "青金石",
        "name_en": "Lapis Lazuli",
        "category": "宝石 / 颜料",
        "category_en": "Gemstone / Pigment",
        "origin": "巴达赫尚（今阿富汗）",
        "origin_en": "Badakhshan (Afghanistan)",
        "direction": "西→东",
        "direction_en": "West → East",
        "description": "产自阿富汗巴达赫尚矿山的深蓝色宝石，是丝路上最古老的长途贸易品之一。早在公元前3000年已运抵埃及和美索不达米亚。佛教壁画中的群青色（Ultramarine）即由此研磨而成，敦煌莫高窟、克孜尔千佛洞大量使用。",
        "description_en": "Deep blue gemstone from the Badakhshan mines in Afghanistan, one of the oldest long-distance trade goods on the Silk Road. Reached Egypt and Mesopotamia by 3000 BCE. Ground into ultramarine pigment for Buddhist murals at Dunhuang and Kizil.",
        "significance": 4,
        "tags": ["宝石", "颜料", "佛教艺术"]
    },
    {
        "id": "black-pepper",
        "name": "胡椒",
        "name_en": "Black Pepper",
        "category": "香料 / 调味品",
        "category_en": "Spice / Condiment",
        "origin": "印度马拉巴尔海岸 / 东南亚",
        "origin_en": "Malabar Coast (India) / SE Asia",
        "direction": "西→东 / 南→北",
        "direction_en": "West → East / South → North",
        "description": "海上丝路香料贸易之王。产自印度西南海岸和东南亚，经阿拉伯商人转运至中国和欧洲。唐代时已是广州港最大宗进口品之一，明代郑和船队大量采购。在欧洲被称为'黑色黄金'，一粒胡椒曾等价于一粒黄金。",
        "description_en": "The king of maritime Silk Road spice trade. Grown on India's Malabar Coast and Southeast Asia, shipped by Arab merchants to China and Europe. One of the largest imports at Tang-era Guangzhou. Called 'black gold' in Europe — peppercorn was once worth its weight in gold.",
        "significance": 5,
        "tags": ["香料", "海上丝路", "贸易大宗"]
    },
    {
        "id": "sandalwood",
        "name": "檀香",
        "name_en": "Sandalwood",
        "category": "香料 / 木材 / 宗教",
        "category_en": "Incense / Timber / Religious",
        "origin": "印度南部 / 东南亚岛屿",
        "origin_en": "Southern India / SE Asian Islands",
        "direction": "南→北",
        "direction_en": "South → North",
        "description": "印度和东南亚出产的珍贵香木，佛教法事中焚香礼佛的重要供品。唐代广州港大宗进口，长安大寺院均设檀香库。除礼佛外，檀香木还用于雕刻佛像、制作扇骨和高级家具。",
        "description_en": "Precious fragrant wood from India and Southeast Asia, essential for Buddhist incense ceremonies. Imported in bulk through Tang-era Guangzhou; major Chang'an temples maintained sandalwood stores. Also carved into Buddha statues, fans, and luxury furniture.",
        "significance": 4,
        "tags": ["香料", "佛教", "木材", "工艺品"]
    },
    {
        "id": "musk",
        "name": "麝香",
        "name_en": "Musk",
        "category": "香料 / 药材",
        "category_en": "Perfume / Medicine",
        "origin": "青藏高原 / 中国西北",
        "origin_en": "Tibetan Plateau / NW China",
        "direction": "东→西",
        "direction_en": "East → West",
        "description": "产自青藏高原麝鹿的珍贵香料，是丝路上最名贵的动物性香料。经河西走廊和西域传入波斯、阿拉伯和欧洲，用于制作高级香水、药品和宗教仪式用香。波斯和阿拉伯商人称之为'中国麝香'，价比黄金。",
        "description_en": "Precious animal-derived fragrance from the musk deer of the Tibetan Plateau, the most valuable animal perfume on the Silk Road. Carried via the Hexi Corridor and Western Regions to Persia, Arabia, and Europe. Used in luxury perfumes, medicines, and religious incense. Known to Persian and Arab merchants as 'Chinese Musk,' valued above gold.",
        "significance": 3,
        "tags": ["香料", "药材", "奢侈品"]
    },
    {
        "id": "persian-carpet",
        "name": "波斯地毯",
        "name_en": "Persian Carpet",
        "category": "工艺品 / 纺织品",
        "category_en": "Craft / Textile",
        "origin": "波斯（今伊朗）",
        "origin_en": "Persia (Iran)",
        "direction": "西→东",
        "direction_en": "West → East",
        "description": "波斯工匠手工编织的精美地毯，以繁复花纹和矿物染料闻名。经陆上丝路传入中国，深受皇室贵族喜爱。唐代长安西市有专售波斯地毯的商铺，日本正仓院至今藏有唐代传入的波斯绒毯。",
        "description_en": "Exquisite hand-woven carpets by Persian artisans, famed for intricate patterns and mineral dyes. Imported to China via the overland Silk Road and beloved by royalty. Tang-era Chang'an's West Market had dedicated Persian carpet shops; the Shōsōin treasury in Japan still preserves a Persian rug imported during the Tang dynasty.",
        "significance": 3,
        "tags": ["工艺品", "纺织品", "奢侈品"]
    },
    {
        "id": "rhubarb",
        "name": "大黄",
        "name_en": "Rhubarb",
        "category": "药材",
        "category_en": "Medicine",
        "origin": "中国西北 / 青藏高原",
        "origin_en": "NW China / Tibetan Plateau",
        "direction": "东→西",
        "direction_en": "East → West",
        "description": "中国西北出产的药用大黄根茎，是丝路上最重要的药材出口品之一。自汉代起经西域传入波斯和阿拉伯，因其强力通便功效被欧洲视为万能良药。俄帝国在恰克图专设大黄贸易通道，大黄是少数直到近代仍在沿丝路大宗交易的药材。",
        "description_en": "Medicinal rhubarb root from Northwest China, one of the Silk Road's most important pharmaceutical exports. Reached Persia and Arabia via the Western Regions from Han times onward. Europe prized it as a panacea for its purgative properties. Russia established a dedicated rhubarb trade route at Kyakhta — one of the few Silk Road medicines still traded in bulk into the modern era.",
        "significance": 3,
        "tags": ["药材", "贸易大宗"]
    },
]

# ============================================================
# 2. 新增事件 (5 events)
# ============================================================
new_events = [
    {
        "id": "marco-polo-journey",
        "name": "马可波罗东游",
        "name_en": "Marco Polo's Journey to the East",
        "year": 1271,
        "end_year": 1295,
        "display_year": "1271 — 1295年",
        "dynasty": "元",
        "description": "威尼斯商人马可·波罗随父亲和叔叔从威尼斯出发，经君士坦丁堡、波斯、帕米尔高原，于1275年抵达元大都（今北京）。在忽必烈汗朝中任职17年，游历中国各地。1295年回到威尼斯后将东方见闻口述成书《马可波罗行纪》，激起欧洲对东方的强烈向往，成为大航海时代的启蒙读物。",
        "description_en": "Venetian merchant Marco Polo traveled with his father and uncle from Venice via Constantinople, Persia, and the Pamir Plateau, reaching Khanbaliq (Beijing) in 1275. He served Kublai Khan for 17 years, traveling extensively across China. Returning to Venice in 1295, his dictated 'Travels of Marco Polo' ignited European fascination with the East and became foundational reading for the Age of Discovery.",
        "significance": 5,
        "tags": ["旅行家", "东西交流", "元朝"]
    },
    {
        "id": "paper-spread-west",
        "name": "造纸术西传",
        "name_en": "Paper Spreads Westward",
        "year": 751,
        "end_year": 1200,
        "display_year": "751 — 12世纪",
        "dynasty": "唐 — 宋",
        "description": "751年怛罗斯之战后，被俘唐军中的造纸工匠将造纸术传入撒马尔罕。撒马尔罕迅速成为伊斯兰世界造纸中心。随后经巴格达（794年）、大马士革、开罗，12世纪传入西班牙和西西里，造纸术在不到500年内完成从长安到欧洲的万里接力。",
        "description_en": "After the Battle of Talas (751), captured Tang papermakers transmitted paper-making technology to Samarkand, which quickly became the Islamic world's paper center. From there it spread to Baghdad (794), Damascus, Cairo, and reached Spain and Sicily by the 12th century — a 10,000-li relay from Chang'an to Europe in under 500 years.",
        "significance": 5,
        "tags": ["技术传播", "造纸术", "文化交流"]
    },
    {
        "id": "tea-trade-boom",
        "name": "茶叶贸易兴盛",
        "name_en": "Tea Trade Boom",
        "year": 780,
        "end_year": 1400,
        "display_year": "8 — 14世纪",
        "dynasty": "唐 — 明",
        "description": "中唐以后饮茶风气从寺院和文人圈扩散至全社会，茶圣陆羽著《茶经》（780年）。茶叶成为丝路大宗贸易品，经茶马古道入藏、西藏传入印度，经海上丝路输入日本和朝鲜，又经陆路入西域和蒙古。宋代设榷茶制度，茶叶成为继丝绸和瓷器之后的第三大出口品。",
        "description_en": "After the mid-Tang, tea drinking spread from monasteries and literati to the whole of society. Lu Yu wrote the 'Classic of Tea' (780). Tea became a major Silk Road commodity, entering Tibet via the Tea-Horse Road and reaching India, Japan, and Korea by sea. The Song dynasty established a tea monopoly — tea ranked behind only silk and porcelain as China's third-largest export.",
        "significance": 4,
        "tags": ["贸易", "茶叶", "茶马古道"]
    },
    {
        "id": "islam-eastward-spread",
        "name": "伊斯兰教沿丝路东传",
        "name_en": "Islam Spreads Eastward along the Silk Road",
        "year": 650,
        "end_year": 1400,
        "display_year": "7 — 14世纪",
        "dynasty": "唐 — 元",
        "description": "伊斯兰教在7世纪阿拉伯半岛兴起后，沿陆海两条丝路东传。陆路经波斯和中亚进入西域，喀什、于阗陆续伊斯兰化；海路经阿拉伯商人船队抵达广州、泉州、扬州。唐设蕃坊聚居穆斯林商人。元代大量色目穆斯林入仕，伊斯兰教与佛教、道教、景教在丝路上并存，形成罕见的宗教多元格局。",
        "description_en": "After Islam's rise in 7th-century Arabia, it spread eastward along both Silk Roads. Overland, it reached the Western Regions via Persia and Central Asia, gradually Islamizing Kashgar and Khotan. By sea, Arab merchant fleets reached Guangzhou, Quanzhou, and Yangzhou. The Tang established foreign quarters for Muslim traders. Under the Yuan, many Central Asian Muslims served the court — Islam, Buddhism, Daoism, and Nestorian Christianity coexisted in a rare moment of religious pluralism along the Silk Road.",
        "significance": 5,
        "tags": ["宗教", "文化交流", "海上丝路"]
    },
    {
        "id": "ibn-battuta-journey",
        "name": "伊本·白图泰远游",
        "name_en": "Ibn Battuta's Travels",
        "year": 1325,
        "end_year": 1354,
        "display_year": "1325 — 1354年",
        "dynasty": "元 — 明",
        "description": "摩洛哥穆斯林旅行家伊本·白图泰从丹吉尔出发，穿越北非、中东、中亚、印度，1346年经海路抵达中国泉州，游历广州、杭州、大都。其《伊本·白图泰游记》记录了元代中国港口繁荣的穆斯林社区和海上贸易盛况。他一生旅行约12万公里，是古代旅行最远的人之一，被称为'伊斯兰的马可·波罗'。",
        "description_en": "Moroccan Muslim traveler Ibn Battuta departed Tangier, crossing North Africa, the Middle East, Central Asia, and India, reaching Quanzhou by sea in 1346. He visited Guangzhou, Hangzhou, and Khanbaliq. His 'Rihla' (Travels) documents the thriving Muslim communities and maritime trade in Yuan China. Traveling approximately 120,000 km in his lifetime, he is among the most widely traveled people in pre-modern history — called the 'Islamic Marco Polo.'",
        "significance": 5,
        "tags": ["旅行家", "海上丝路", "东西交流"]
    },
]

# ============================================================
# 3. 新增关系边 (52 edges)
# ============================================================
new_edges = [
    # --- 青金石相关 ---
    {"source": "lapis-lazuli", "target": "balkh", "relation": "原产地", "relation_en": "Origin",
     "description": "阿富汗巴达赫尚（蓝氏城/巴里黑附近）是世界最古老的青金石矿产地，开采已逾6000年"},
    {"source": "lapis-lazuli", "target": "khotan", "relation": "贸易中转", "relation_en": "Trade Transit",
     "description": "于阗是青金石从阿富汗进入西域和中原的关键中转站"},
    {"source": "lapis-lazuli", "target": "dunhuang", "relation": "消费 / 艺术使用", "relation_en": "Consumption / Artistic Use",
     "description": "敦煌莫高窟壁画大量使用青金石研磨的群青颜料，飞天衣袂的蓝色即由此而来"},
    {"source": "lapis-lazuli", "target": "kashgar", "relation": "集散 / 贸易", "relation_en": "Trade Hub",
     "description": "喀什是青金石北传天山以北草原丝路的重要集散地"},
    {"source": "lapis-lazuli", "target": "buddhism", "relation": "宗教艺术颜料", "relation_en": "Religious Art Pigment",
     "description": "青金石研磨的群青是佛教壁画中最珍贵的蓝色颜料，象征佛法庄严"},

    # --- 胡椒相关 ---
    {"source": "black-pepper", "target": "calicut", "relation": "原产地", "relation_en": "Origin",
     "description": "印度西南海岸的卡利卡特（古里）是胡椒核心产区，郑和船队的重要靠泊港"},
    {"source": "black-pepper", "target": "guangzhou", "relation": "进口港", "relation_en": "Import Port",
     "description": "唐代广州港是胡椒最大进口港，阿拉伯商船每年运来大量胡椒"},
    {"source": "black-pepper", "target": "quanzhou", "relation": "进口港", "relation_en": "Import Port",
     "description": "宋元时期泉州超越广州成为胡椒第一大进口港，赵汝适《诸蕃志》详记胡椒来源"},
    {"source": "black-pepper", "target": "malacca", "relation": "贸易中转", "relation_en": "Trade Transit",
     "description": "马六甲是东南亚胡椒和香料贸易的咽喉中转港"},
    {"source": "black-pepper", "target": "zheng-he", "relation": "大量采购", "relation_en": "Bulk Purchase",
     "description": "郑和下西洋时大量采购胡椒，明廷曾以胡椒折抵官员俸禄"},
    {"source": "black-pepper", "target": "spices", "relation": "核心品类", "relation_en": "Core Category",
     "description": "胡椒占海上香料贸易量最大份额，堪称'香料之王'"},

    # --- 檀香相关 ---
    {"source": "sandalwood", "target": "calicut", "relation": "产地 / 贸易港", "relation_en": "Origin / Trade Port",
     "description": "印度南部的卡利卡特是檀香木的重要产地和输出港"},
    {"source": "sandalwood", "target": "malacca", "relation": "集散地", "relation_en": "Trade Hub",
     "description": "马六甲汇聚印度檀香和印尼檀香，再北上输入中国"},
    {"source": "sandalwood", "target": "guangzhou", "relation": "进口港", "relation_en": "Import Port",
     "description": "唐代广州港大量进口檀香木，长安寺院专设檀香库储备法事用香"},
    {"source": "sandalwood", "target": "buddhism", "relation": "宗教用途", "relation_en": "Religious Use",
     "description": "檀香是佛教法事中最常用的焚香供品，也是雕刻佛像的上等材料"},

    # --- 麝香相关 ---
    {"source": "musk", "target": "changan", "relation": "集散 / 出口起点", "relation_en": "Trade Hub / Export Origin",
     "description": "青藏高原产的麝香在长安汇集，经丝路西传波斯和阿拉伯"},
    {"source": "musk", "target": "samarkand", "relation": "贸易中转", "relation_en": "Trade Transit",
     "description": "撒马尔罕是麝香从中国经中亚传入波斯的重要中转站"},
    {"source": "musk", "target": "baghdad", "relation": "消费 / 加工", "relation_en": "Consumption / Processing",
     "description": "阿拔斯王朝的巴格达宫廷和贵族消费大量'中国麝香'，用于调香和制药"},
    {"source": "musk", "target": "dunhuang", "relation": "贸易通道", "relation_en": "Trade Route",
     "description": "敦煌是麝香经河西走廊西传的必经关口，藏经洞文书中有麝香贸易记录"},

    # --- 波斯地毯相关 ---
    {"source": "persian-carpet", "target": "isfahan", "relation": "原产地", "relation_en": "Origin",
     "description": "伊斯法罕是波斯地毯的核心产地，以繁复花纹和植物染料著称"},
    {"source": "persian-carpet", "target": "baghdad", "relation": "集散 / 贸易", "relation_en": "Trade Hub",
     "description": "巴格达是波斯地毯在阿拔斯时期的集散中心"},
    {"source": "persian-carpet", "target": "changan", "relation": "消费市场", "relation_en": "Consumer Market",
     "description": "唐代长安西市有专售波斯地毯的商铺，深受皇室和贵族喜爱"},
    {"source": "persian-carpet", "target": "samarkand", "relation": "贸易中转", "relation_en": "Trade Transit",
     "description": "波斯地毯经撒马尔罕沿丝路东传至中国，粟特商人充当关键中间人"},

    # --- 大黄相关 ---
    {"source": "rhubarb", "target": "changan", "relation": "集散起点", "relation_en": "Collection / Export Origin",
     "description": "西北所产大黄在长安集散，经丝路西传至波斯和欧洲"},
    {"source": "rhubarb", "target": "samarkand", "relation": "贸易中转", "relation_en": "Trade Transit",
     "description": "撒马尔罕是大黄西传波斯和阿拉伯的关键中转站"},
    {"source": "rhubarb", "target": "dunhuang", "relation": "陆路通道", "relation_en": "Overland Route",
     "description": "敦煌是西北大黄沿河西走廊西传的必经关口"},

    # --- 马可波罗东游事件 ---
    {"source": "marco-polo-journey", "target": "marco-polo", "relation": "主角", "relation_en": "Protagonist",
     "description": "马可·波罗是这次横跨欧亚旅行的核心人物"},
    {"source": "marco-polo-journey", "target": "venice", "relation": "出发地与归来地", "relation_en": "Departure and Return",
     "description": "马可·波罗从威尼斯出发，24年后回到威尼斯"},
    {"source": "marco-polo-journey", "target": "kashgar", "relation": "途经", "relation_en": "Passed Through",
     "description": "马可·波罗翻越帕米尔高原后经喀什进入中国"},
    {"source": "marco-polo-journey", "target": "dunhuang", "relation": "途经", "relation_en": "Passed Through",
     "description": "马可·波罗途经敦煌进入河西走廊，对中国城市繁荣惊叹不已"},
    {"source": "marco-polo-journey", "target": "mongol-pax", "relation": "时代背景", "relation_en": "Historical Context",
     "description": "蒙古和平时期欧亚交通畅通，马可·波罗得以安全横穿整个亚洲"},

    # --- 造纸术西传事件 ---
    {"source": "paper-spread-west", "target": "paper", "relation": "技术本体", "relation_en": "Technology Itself",
     "description": "造纸术从中国向西方传播的技术转移链条"},
    {"source": "paper-spread-west", "target": "battle-of-talas", "relation": "触发事件", "relation_en": "Trigger Event",
     "description": "怛罗斯之战的俘虏成为造纸术西传的关键推动者"},
    {"source": "paper-spread-west", "target": "samarkand", "relation": "第一个传播节点", "relation_en": "First Transmission Node",
     "description": "撒马尔罕是中国境外第一个造纸中心，751年后迅速崛起"},
    {"source": "paper-spread-west", "target": "baghdad", "relation": "传播节点", "relation_en": "Transmission Node",
     "description": "巴格达于794年建立造纸作坊，百年内取代羊皮纸和莎草纸"},
    {"source": "paper-spread-west", "target": "damascus", "relation": "传播节点", "relation_en": "Transmission Node",
     "description": "大马士革是造纸术传入欧洲前的最后一站，'大马士纸'流行于地中海"},

    # --- 茶叶贸易兴盛事件 ---
    {"source": "tea-trade-boom", "target": "tea", "relation": "贸易本体", "relation_en": "Trade Commodity",
     "description": "茶叶从中唐起从寺院饮品变为全民消费品，并走向国际贸易"},
    {"source": "tea-trade-boom", "target": "changan", "relation": "消费中心", "relation_en": "Consumer Hub",
     "description": "长安是中晚唐茶叶消费和贸易的中心城市"},
    {"source": "tea-trade-boom", "target": "lhasa", "relation": "主要输入地", "relation_en": "Major Import Region",
     "description": "吐蕃（拉萨）是茶叶消费重镇，茶马古道以茶易马，藏人'宁可三日无粮，不可一日无茶'"},
    {"source": "tea-trade-boom", "target": "guangzhou", "relation": "出口港", "relation_en": "Export Port",
     "description": "广州是茶叶海上输出的主要港口，日本和朝鲜的茶种由此运出"},
    {"source": "tea-trade-boom", "target": "buddhism", "relation": "文化推动", "relation_en": "Cultural Driver",
     "description": "禅宗寺院将饮茶从修行方式推广至社会，'茶禅一味'由此而来"},

    # --- 伊斯兰教东传事件 ---
    {"source": "islam-eastward-spread", "target": "kashgar", "relation": "首批伊斯兰化", "relation_en": "First Islamization",
     "description": "喀什是西域最早伊斯兰化的城市之一，喀喇汗王朝以此为都传教"},
    {"source": "islam-eastward-spread", "target": "khotan", "relation": "伊斯兰化节点", "relation_en": "Islamization Node",
     "description": "于阗佛教王国在与喀喇汗王朝长期战争后于11世纪伊斯兰化，标志西域宗教格局巨变"},
    {"source": "islam-eastward-spread", "target": "guangzhou", "relation": "海路抵达", "relation_en": "Arrival by Sea",
     "description": "阿拉伯和波斯穆斯林商人最早在唐代经海路抵达广州，设蕃坊、建怀圣寺"},
    {"source": "islam-eastward-spread", "target": "quanzhou", "relation": "海路重镇", "relation_en": "Key Maritime City",
     "description": "宋元时期泉州成为最大穆斯林海商聚集地，清净寺是中国最古老清真寺之一"},
    {"source": "islam-eastward-spread", "target": "baghdad", "relation": "宗教扩散起点", "relation_en": "Religious Diffusion Origin",
     "description": "阿拔斯王朝的巴格达是伊斯兰文明中心，宗教沿丝路扩散至中亚和中国的起点之一"},

    # --- 伊本·白图泰事件 ---
    {"source": "ibn-battuta-journey", "target": "ibn-battuta", "relation": "主角", "relation_en": "Protagonist",
     "description": "伊本·白图泰从摩洛哥出发，经海路抵达中国，留下了伊斯兰世界最重要的东方游记"},
    {"source": "ibn-battuta-journey", "target": "quanzhou", "relation": "中国第一站", "relation_en": "First Stop in China",
     "description": "伊本·白图泰称泉州为'刺桐港'，誉之为'世界最大港口'"},
    {"source": "ibn-battuta-journey", "target": "guangzhou", "relation": "游历", "relation_en": "Visited",
     "description": "伊本·白图泰游历广州，记录当地繁荣的穆斯林社区和蕃坊生活"},
    {"source": "ibn-battuta-journey", "target": "calicut", "relation": "途经", "relation_en": "Passed Through",
     "description": "伊本·白图泰途经卡利卡特，记录印度西海岸与中国之间的繁荣贸易"},

    # --- 补充：增强法显相关连接 ---
    {"source": "faxian", "target": "sri-lanka", "relation": "停留抄经", "relation_en": "Stayed for Sutra Copying",
     "description": "法显在斯里兰卡（师子国）停留两年，抄写大量佛经，见到当地商人供奉汉地白绢扇而思乡落泪"},
    {"source": "faxian", "target": "taxila", "relation": "参学", "relation_en": "Studied",
     "description": "法显在犍陀罗的塔克西拉参访佛迹，记录当地佛教盛况"},
    {"source": "faxian", "target": "sumatra", "relation": "归途遇险", "relation_en": "Perilous Return",
     "description": "法显在苏门答腊换船滞留五月，海上遭遇风暴九死一生，最终返回中国"},

    # --- 补充：增强班超相关连接 ---
    {"source": "ban-chao", "target": "kashgar", "relation": "经营西域据点", "relation_en": "Western Regions Base",
     "description": "班超以疏勒（喀什）为经营西域的核心基地，驻扎长达十余年"},
    {"source": "ban-chao", "target": "gan-ying", "relation": "派遣使节", "relation_en": "Dispatched Envoy",
     "description": "班超派遣属吏甘英出使大秦（罗马），甘英抵达条支（波斯湾沿岸）后被安息商人劝阻返回"},
    {"source": "ban-chao", "target": "loulan", "relation": "经略", "relation_en": "Controlled",
     "description": "班超曾在楼兰（鄯善）夜袭匈奴使团，'不入虎穴焉得虎子'由此而来"},

    # --- 补充：增强杜环相关连接 ---
    {"source": "du-huan", "target": "mecca", "relation": "游历记录", "relation_en": "Travel Record",
     "description": "杜环可能是第一位到达阿拉伯半岛并留下文字记录的中原人，其《经行记》记录了伊斯兰教早期面貌"},
    {"source": "du-huan", "target": "damascus", "relation": "游历记录", "relation_en": "Travel Record",
     "description": "杜环被俘后在阿拉伯世界游历，可能到过大马士革，记录了倭马亚王朝的繁华"},
]

# ============================================================
# 4. 写入数据
# ============================================================

# Add goods
existing_good_ids = {g['id'] for g in data['nodes']['goods']}
for g in new_goods:
    if g['id'] not in existing_good_ids:
        data['nodes']['goods'].append(g)
        print(f'  + 物产: {g["name"]} ({g["id"]})')
    else:
        print(f'  ! 物产重复跳过: {g["id"]}')

# Add events
existing_event_ids = {e['id'] for e in data['nodes']['events']}
for e in new_events:
    if e['id'] not in existing_event_ids:
        data['nodes']['events'].append(e)
        print(f'  + 事件: {e["name"]} ({e["id"]})')
    else:
        print(f'  ! 事件重复跳过: {e["id"]}')

# Add edges (deduplicate by source+target)
existing_edge_keys = {(e['source'], e['target']) for e in data['edges']}
added_edges = 0
for e in new_edges:
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
        added_edges += 1
    else:
        print(f'  ! 边重复跳过: {e["source"]} -> {e["target"]}')

print(f'  + 关系边: {added_edges} 条')

# Update version
data['meta']['version'] = '1.2.0'
data['meta']['last_updated'] = '2026-06-06'

# Write
with open(DATA_PATH, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print()
print(f'=== 数据增强完成 ===')
print(f'版本: {data["meta"]["version"]}')
print(f'城市: {len(data["nodes"]["cities"])}')
print(f'人物: {len(data["nodes"]["figures"])}')
print(f'物产: {len(data["nodes"]["goods"])}')
print(f'事件: {len(data["nodes"]["events"])}')
print(f'关系边: {len(data["edges"])}')
print(f'传播路线: {len(data["routes"])}')
