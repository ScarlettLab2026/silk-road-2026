# 掘金文章：丝路知识图谱技术架构

**标题：** 我用一份 JSON 驱动了十个交互故事——丝路知识图谱的工程化实践

---

做了两个月的丝绸之路交互知识图谱。现在数据长这样：

- 46 座城市、23 个人物、30 种物产、24 个历史事件
- 358 条关系边、8 条传播路线
- 10 个交互故事，每个 7 章
- 全部由一个 JSON 文件驱动

这篇文章聊工程实现。

## 架构：一份数据，多种输出

```
data/silk-road.json (4478行)
    ├── index.html          ← 地图+关系图+时间轴+搜索
    ├── story{1..10}.html    ← 10 个交互故事
    ├── css/story-common.css    ← 共享样式
    └── js/story-engine.js      ← 共享叙事引擎
```

加一条数据 → 地图刷新 + 关系图刷新 + 关联故事自动更新。

## 共享引擎：九个故事 → 十个故事，一份代码

早期每个故事页面各自独立，六七份拷贝，改一个 bug 要改六个文件。

v1.5.0 做了全站重构：

- `css/story-common.css`：所有故事的共享样式。暗亮主题用 CSS 自定义属性驱动，一个 `data-theme` 属性切换全站配色。
- `js/story-engine.js`：读取 `STORY[]` 数组，驱动地图飞越、叙事卡片弹出、路线累计绘制、进度条、章节切换。

每个故事页面现在只需定义：

```javascript
const STORY_CONFIG = {
  accent: '#8b6ba7',        // 主题色
  accentRgb: '139,107,167', // 主题色 RGB
  mapCenter: [42, 65],      // 地图初始中心
  mapZoom: 3.2,             // 初始缩放
};

const STORY = [
  {
    title: '大都出发',
    body: '元大都。汗八里——大汗之城……',
    lat: 39.90, lng: 116.41, zoom: 5,
    route: ['beijing'],
    showCities: ['beijing'],
    highlight: ['rab-ban-sauma']
  },
  // ... 7 章
];
```

**代码量从每个故事 ~450 行降到 ~130 行**。新增一个故事，核心工作只剩下写叙事文本。

## 累计路线绘制

这是我最满意的交互细节。

每个故事的路线不是一次性画完的。随着章节推进，路线**逐步延伸**：

```javascript
// story-engine.js 核心逻辑
function drawRoute(cities) {
  // 取 JSON 中的城市坐标，但保持章节间累计
  const coords = cities.map(id => getCityLatLng(id));
  if (polyline) map.removeLayer(polyline);

  // 渐进式绘制
  polyline = L.polyline(coords, {
    color: STORY_CONFIG.accent,
    weight: 3,
    dashArray: '8 6',       // 虚线，暗示这是一条"路"而非国界
    opacity: 0.8
  }).addTo(map);

  map.fitBounds(polyline.getBounds().pad(0.2), { animate: true });
}
```

用户不会看到断续的线段——看到的是一个人如何一步步走完整条路。这个设计来自杜环故事的灵感：他被俘后辗转多个国家，每一段路都是被迫的，但拼在一起就是一生。

## 暗亮模式：CSS 自定义属性 + localStorage

全站支持暗/亮模式切换：

```css
:root {
  --bg: #121016;
  --card-bg: rgba(22,20,24,0.93);
  --accent: #8b6ba7;
  --text: #e8e4dc;
}

[data-theme="light"] {
  --bg: #f5f0e8;
  --card-bg: rgba(255,252,248,0.93);
  --text: #2c2416;
}
```

切换时只需改 `document.documentElement` 的 `data-theme` 属性。每个组件自动继承。偏好存 `localStorage`，刷新不失忆。

## 移动端三断点

```css
/* ≥1024px: 侧边卡片不遮挡地图 */
/* 768-1023px: 卡片收窄，字号缩小 */
@media (max-width: 1023px) {
  #narrative { max-width: 340px; }
}

/* <768px: 卡片底部弹出，覆盖地图上方 */
@media (max-width: 767px) {
  #narrative {
    bottom: 0; left: 0; right: 0;
    max-width: none; border-radius: 16px 16px 0 0;
  }
}
```

三断点覆盖桌面、平板、手机。触控区域最小 44px，过苹果 HIG。

## 单一数据源

`data/silk-road.json` 4478 行，结构：

```json
{
  "meta": { "title": "丝绸之路交互知识图谱", "version": "1.7.0" },
  "nodes": {
    "cities": [{ "id": "beijing", "name": "元大都", "lat": 39.9, … }],
    "figures": [{ "id": "rab-ban-sauma", "name": "拉班·扫马", … }],
    "goods": [{ "id": "silk", "name": "丝绸", … }],
    "events": [{ "id": "battle-talas", "name": "怛罗斯之战", … }]
  },
  "edges": [{ "source": "rab-ban-sauma", "target": "paris", "relation": "出使法兰西" }],
  "routes": [{ "id": "silk-road", "name": "陆上丝绸之路", "path": ["changan", …] }]
}
```

一个 JSON，驱动全站。开源，CC BY-SA 4.0。

## 纯静态，零服务器

整个站点是纯 HTML/CSS/JS。托管在 GitHub Pages，push 即部署。

- Leaflet（地图）
- D3.js（关系图，仅在 index.html 使用）
- 无构建步骤，无框架，无运行时依赖

总共不到 ¥0/月。

## 九个故事怎么选出来的

选角标准：**旅程覆盖新地理区域 + 身份类型不重复**。

| 人物 | 走到的最远点 | 身份 |
|------|------------|------|
| 张骞 | 撒马尔罕 | 帝国使节 |
| 班超 | 波斯湾 | 投笔从戎的将军 |
| 法显 | 斯里兰卡 | 老僧 |
| 玄奘 | 那烂陀 | 名僧 |
| 杜环 | 非洲/麦加 | 战俘 |
| 马可波罗 | 泉州 | 商人 |
| 拉班扫马 | 巴黎/波尔多 | 景教修士 |
| 汪大渊 | 东非 | 民间航海家 |
| 郑和 | 东非 | 帝国舰队司令 |

每一期新增一个故事，地图上的路线就多一条线。

## 开源

GitHub: https://github.com/ScarlettLab2026/silk-road-2026
在线: https://scarlettlab2026.github.io/silk-road-2026

欢迎贡献人物、故事、或翻译。有想看到的丝路人物？评论区告诉我。

#开源 #前端 #数据可视化 #丝绸之路 #知识图谱
