# 掘金文章：六故事引擎

**标题：** 我从JSON里驱动了6个交互故事：丝路知识图谱的故事引擎设计

---

三周前我在丝路项目里加了第一个交互故事（张骞凿空西域）。这周，第六个故事（杜环经行记）上线了。

六个故事共享同一套引擎、同一份JSON数据、同一个Leaflet地图实例。每个故事不到400行代码，新增一个故事只需要写STORY数组。

这篇文章讲一下这个"故事引擎"的设计思路。

## 数据架构：一份JSON喂饱一切

核心原则没变过：**单一数据源 → 多种呈现形态。**

```json
{
  "nodes": {
    "cities": [40个],
    "figures": [23个],
    "goods": [30个],
    "events": [23个]
  },
  "edges": [326条],
  "routes": [8条]
}
```

故事引擎不需要额外数据。一个故事只需要一个STORY数组：

```javascript
const STORY = [
  {
    title: '怛罗斯之俘',
    subtitle: '公元751年 · 怛罗斯',
    body: '天宝十年，大唐安西节度使高仙芝率军...',
    lat: 42.8, lng: 71.3, zoom: 5,
    route: ['samarkand'],         // 路线城市ID，从JSON查坐标
    marker: null,                  // 当前高亮城市
    showCities: ['samarkand', 'kashgar', 'balkh'],  // 显示的城市
    highlight: ['du-huan', 'battle-of-talas']        // 关联实体标签
  },
  // ... 7章
];
```

**每章就是一个对象。** `route` 引用 JSON 中的城市 ID，引擎自动查坐标画线。`highlight` 引用人物/物产/事件 ID，引擎自动渲染关联标签。

## 故事引擎核心：四个函数

整个引擎就四个核心函数：

### 1. renderChapter(idx) — 一章的完整渲染

```javascript
function renderChapter(idx) {
  const ch = STORY[idx];
  
  // ① 更新叙事卡片 DOM
  updateCard(ch);
  
  // ② 地图飞越
  map.flyTo([ch.lat, ch.lng], ch.zoom, { 
    duration: 1.8, easeLinearity: 0.25 
  });
  
  // ③ 重绘路线（累计）
  drawRoute(ch.route);  // 不是只画本章！是累计所有已走过的
  
  // ④ 渲染城市标记
  drawCityMarkers(ch.showCities, ch.marker);
  
  // ⑤ 渲染关联实体标签
  drawBadges(ch.highlight);
}
```

### 2. 路线累计绘制 — 最重要的设计决策

这是最容易踩的坑。如果每章只画自己那一段：

```javascript
// ❌ 错误做法：每章独立画一小段
chapter.route = ['samarkand'];          // 第1章
chapter.route = ['samarkand', 'baghdad']; // 第2章
// 结果：路线上跳下窜，断断续续
```

正确做法是**路线在STORY定义里就是累计的**：

```javascript
// ✅ STORY中的route本身就是累计的
第1章 route: ['samarkand']
第3章 route: ['samarkand', 'baghdad']  
第7章 route: ['samarkand', 'baghdad', 'damascus', 'mombasa', 'mecca', 'guangzhou']
```

这样用户进度越深，地图上的路线越长——直观感受"这个人已经走了多远"。杜环的故事到第7章时，整条路线从怛罗斯一直延伸到广州，横跨三大洲。

### 3. 地图飞越 + 卡片淡入的同步

```javascript
// 飞越和卡片切换要错开200ms，否则视觉上会"跳"
map.flyTo([ch.lat, ch.lng], ch.zoom, { duration: 1.8 });

card.classList.add('fading');  // 旧卡片淡出
setTimeout(() => {
  updateCardContent(ch);        // 更新内容
  card.classList.remove('fading'); // 新卡片淡入
}, 200);
```

`easeLinearity: 0.25` 这个参数让飞越有一个加速→减速的弧线，视觉上更像"飞"。

### 4. 关联实体的自动标签渲染

每章的 `highlight` 数组里的实体 ID，引擎自动从 JSON 中查找并渲染标签：

```javascript
// STORY定义
highlight: ['du-huan', 'battle-of-talas', 'paper-spread-west']

// 引擎自动：查JSON → 确定类型 → 给颜色 → 渲染标签
// 🏷 杜环 [旅行家]  🏷 怛罗斯之战 [事件]  🏷 造纸术西传 [事件]
```

颜色规则：人物=蓝 `#5b9bd5`，物产=绿 `#6aad6a`，事件=红 `#c75b3a`。

## 六个故事，六套配色

每个故事有自己的主题色（CSS变量 `--accent`），其余代码完全共享：

| 故事 | 配色 | 色值 | 情感 |
|------|------|------|------|
| 张骞 | 沙漠金 | `#d4a853` | 帝国使命 |
| 法显 | 古佛青 | `#5d8a7c` | 信仰坚韧 |
| 玄奘 | 佛金色 | `#c47a38` | 精神追寻 |
| 郑和 | 海洋蓝 | `#5ea3b8` | 航海探索 |
| 马可波罗 | 威尼斯红 | `#c2714e` | 异域好奇 |
| 杜环 | 沙漠铜 | `#b08040` | 生存漂泊 |

每个故事文件约370行（CSS + HTML + JS），新增一个故事只需：
1. 复制上一个故事文件
2. 改 `--accent` 色值
3. 改写 STORY 数组（7个对象）
4. 更新导航条加一个 `<a>` 标签

从决定做杜环到上线，**30分钟**。引擎成熟后，新故事就是填数据。

## 技术栈

| 层 | 选型 | 理由 |
|----|------|------|
| 地图 | Leaflet.js | flyTo动画开箱即用 |
| 底图 | CartoDB dark_all | 免费、暗色适配 |
| 路线 | L.polyline + dashArray | 虚线双层叠加（底层半透明+顶层高亮） |
| 卡片 | 纯 CSS absolute + backdrop-filter | 无需UI框架 |
| 数据 | 单JSON (43KB) | fetch即用 |
| 部署 | GitHub Pages | push上线 |

全程零框架。六个故事文件加起来不到 2,500 行。

## 写完六个故事后的感悟

做引擎的时候想的是技术问题：飞越时长多少最舒适、路线累计怎么实现、标签系统怎么设计。

做完六个故事回头看，发现引擎在解决一个更大的问题：**让每个走过这条路的人，无论什么身份，都有一个容器来承载他的故事。**

前五个故事的主人公都是"大人物"——帝国使节、高僧、将军、富商。杜环是第一个"普通人"——一个连名字都没在正史里单独出现过的战俘。但他的故事，从技术上讲，和前五个人**完全一样**地被呈现了出来。一样的7章叙事、一样的地图飞越、一样的标签系统、一样的路线累计。

这可能才是开源和数据驱动的真正意义：**它不区别对待。张骞和杜环，在引擎里是平等的。**

---

在线体验：
🔗 丝路知识图谱：https://scarlettlab2026.github.io/silk-road-2026
🏜 杜环经行记：https://scarlettlab2026.github.io/silk-road-2026/story6.html
📂 GitHub：https://github.com/ScarlettLab2026/silk-road-2026
