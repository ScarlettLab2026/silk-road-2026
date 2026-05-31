# 🐫 丝绸之路 · 交互知识图谱

> 一个开放、结构化、双语（中/英）的丝绸之路知识图谱项目。从数据出发，渲染出多种内容形态。

**[🌐 在线预览](https://ScarlettLab2026.github.io/silk-road-2026)** · **[📂 浏览数据](./data/silk-road.json)** · **[🤝 贡献指南](./CONTRIBUTING.md)**

---

## 这是什么？

这是一个关于「丝绸之路」的结构化开放数据集和交互式网站。我们将丝路上的人、地、物、事拆解为**实体**和**关系**，用一张活的图谱把它们连在一起。

路线 → 城市 → 人物 → 物产 → 事件 → 技术传播路径 → 文化交流轨迹 —— 全都关联在一起。

### 核心特点

- **单一数据源**（[silk-road.json](./data/silk-road.json)），所有内容从同一份数据渲染
- **双语支持**，中文和 English 可一键切换
- **交互式地图**（Leaflet.js），直观展示地理关系
- **朝代时间轴**，按历史时期筛选
- **知识图谱**，实体间的关联关系可视化
- **开源开放**，数据遵循 CC BY-SA 4.0 协议

## 当前数据规模

| 类型 | 数量 |
|------|------|
| 🏙 城市 | 15 |
| 👤 人物 | 10 |
| 📦 物产 | 10 |
| ⚡ 事件 | 9 |
| 🔗 关系边 | 68 |

> *数据持续扩充中。欢迎贡献！*

## 技术栈

- **数据层**：JSON（结构化知识图谱）
- **前端**：纯 HTML/CSS/JS + [Leaflet.js](https://leafletjs.com/) 地图
- **部署**：GitHub Pages（静态站点，零成本）

## 本地运行

```bash
# 克隆仓库
git clone https://github.com/ScarlettLab2026/silk-road-2026.git
cd silk-road2026

# 启动本地服务器（任选一种）
python3 -m http.server 8080
# 或
npx serve .

# 浏览器打开 http://localhost:8080
```

## 项目愿景

我们的目标不是做一个网站，而是养一个**活的系统**：

```
知识图谱 ──→ 自动生成多种内容 ──→ 多渠道分发 ──→ 反馈回流 ──→ 图谱增强
                                                        ↑
                                              ←─────────┘
```

每一步的产出，都会成为下一步的燃料。每一次新增数据，所有输出形态同步受益。

## 路线图

- [x] 基础知识图谱 (v0.1.0)
- [x] 交互式网页（地图 + 时间轴 + 详情面板）
- [x] 更多城市与节点（楼兰、和田、木鹿、布哈拉、赫拉特、泉州、元大都）(v0.2.0)
- [x] 更多人物（班超、法显、鸠摩罗什、伊本·白图泰、拉班·扫马、李白）(v0.2.0)
- [x] 更多物产与事件（茶叶、西域马、佛教、和田玉、班超定西域、法显西行、景教碑、安史之乱）(v0.2.0)
- [ ] 人物关系网络图（D3.js 力导向图）
- [ ] 物产传播路径动画
- [ ] 数据 API（JSON endpoint）
- [ ] 知识问答卡片（社交媒体分享用）
- [ ] 短视频脚本自动生成
- [ ] 社区贡献机制（Pull Request 模板）

## 如何贡献

1. Fork 本仓库
2. 在 `data/silk-road.json` 中添加或修改实体/关系
3. 确保 JSON 格式有效（可用 `python3 -m json.tool data/silk-road.json` 验证）
4. 提交 Pull Request 并描述你的修改

欢迎贡献：
- 新的城市、人物、物产、事件节点
- 实体之间新的关联关系
- 更丰富的描述文本（中/英双语）
- 纠错与勘误
- 翻译质量改进

## 许可证

- 数据：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- 代码：[MIT](./LICENSE)

---

<p align="center">
  <i>凿空西域，连通世界。从长安到罗马，每一步都在创造历史。</i>
</p>

---

# 🐫 Silk Road · Interactive Knowledge Graph

> An open, structured, bilingual (ZH/EN) knowledge graph of the Silk Road. Data first — multiple content forms rendered from one source.

## What is this?

A structured open dataset and interactive website about the Silk Road. We break down the people, places, goods, and events into **entities** and **relationships**, connected in a living knowledge graph.

Routes → Cities → Figures → Goods → Events → Technology transfer paths → Cultural exchange trajectories — all interconnected.

## Data Scale

| Type | Count |
|------|-------|
| 🏙 Cities | 15 |
| 👤 Figures | 10 |
| 📦 Goods | 10 |
| ⚡ Events | 9 |
| 🔗 Edges | 68 |

## Contributing

We welcome contributions of new nodes, richer descriptions, corrections, and translations.

## License

- Data: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- Code: [MIT](./LICENSE)

---

<p align="center">
  <i>From Chang'an to Rome — opening the way, connecting the world.</i>
</p>
