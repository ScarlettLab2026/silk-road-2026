# Reddit r/dataisbeautiful 发帖套件

## 发帖步骤

1. 打开 https://www.reddit.com
2. 注册账号（邮箱+用户名+密码，1分钟）
3. 加入 r/dataisbeautiful 社区
4. 点 **Create Post**
5. 选 **Images & Video** 标签页
6. 上传截图（建议用 D3 关系网络图或路线动画）
7. Title 填标题（注意加 [OC] 标签）
8. 点 Post
9. 发布后在评论区发第一条解释评论

---

## Title（标题）

```
[OC] 2,000 years of Silk Road history visualized — 40 cities, 326 connections, 6 interactive journeys
```

备选：
```
[OC] I visualized the entire Silk Road as an interactive knowledge graph — 6 travelers, 326 connections
```

---

## 截图选择

上传这张图作为帖子主体（选一张最惊艳的）：

| 选项 | 截图内容 | 为什么 |
|------|---------|--------|
| 🥇 首选 | D3关系网络图（全节点） | 视觉冲击力最强，金色节点+深色背景 |
| 🥈 备选 | 传播路线动画（光点在路上） | 动态感，但不如图1直观 |
| 🥉 备选 | 6故事导航条+地图全景 | 展示故事矩阵 |

截图在 screenshots.html 或直接截 index.html 的关系图视图。

---

## First Comment（发布后在评论区粘贴）

```
Data source: I manually compiled a structured JSON dataset covering 40 Silk Road cities, 23 historical figures, 30 trade goods, 23 events, and 326 relationships. Cross-referenced Chinese and English historical sources.

Tools: Leaflet.js (map), D3.js (force-directed graph), Canvas (route animations), vanilla JS. Zero frameworks. Hosted on GitHub Pages.

The whole site is driven by a single 43KB JSON file — add one city, and it shows up on the map, the graph, the timeline, and the interactive stories simultaneously.

Interactive version: https://scarlettlab2026.github.io/silk-road-2026
GitHub (open source): https://github.com/ScarlettLab2026/silk-road-2026

There are 6 interactive stories where the map flies from city to city as you read. My favorite is Du Huan — a Tang dynasty soldier captured at the Battle of Talas (751 CE) who spent 11 years as a captive traveling across the Abbasid Caliphate and became the first Chinese person to document Africa and Islam. His entire book is lost except for 1,511 words preserved in another text.

Edit: Thanks for the awards! The data is CC BY-SA 4.0 if anyone wants to use it for their own projects.
```

---

## 规则注意事项

r/dataisbeautiful 有严格的规则：

- ✅ 必须用 [OC] 标签（你自己做的）
- ✅ 必须是"数据可视化"（截图要展示数据的视觉呈现，不能只截网站首页）
- ✅ 必须在评论里解释数据来源和工具
- ❌ 不能直接发链接贴（必须是图片/GIF贴）
- ❌ 标题不能要赞（"upvote if..."）

---

## 发帖时间建议

- 最佳：周二/周三 UTC 12:00-15:00（美国东部上午）
- 北京时间约 20:00-23:00
