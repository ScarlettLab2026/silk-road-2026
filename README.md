# 🐫 Silk Road · Interactive Knowledge Graph

> **An open-source, interactive map of 2,000 years of East-West exchange.** 40 cities. 30 trade goods. 326 connections. 6 interactive stories. One JSON file drives it all.

**[🌐 Live Demo](https://ScarlettLab2026.github.io/silk-road-2026)** · **[📂 Browse Data](./data/silk-road.json)** · **[🤝 Contribute](./CONTRIBUTING.md)**

---

## What is this?

We broke down 2,000 years of Silk Road history into a structured knowledge graph. Every city, figure, trade good, and historical event is connected — and you can explore all of it interactively.

**🗺️ Interactive Map** — 40 cities on real geographic coordinates across Eurasia, the Indian Ocean, and East Africa

**🕸️ Relationship Graph** — D3.js force-directed graph with 326 edges. Drag nodes, discover hidden connections

**⏳ Dynasty Timeline** — Filter by dynasty (Han → Tang → Yuan → Ming). Map and data sync instantly

**🎬 8 Animated Trade Routes** — Watch silk, paper, gunpowder, Buddhism, and tea travel across the map as golden pulse dots with voice narration

**📖 6 Interactive Stories** — Follow 6 travelers chapter by chapter. The map flies to each location as the story unfolds:

| Story | Traveler | Route | Era | Color |
|-------|----------|-------|-----|-------|
| 📖 凿空西域 | **Zhang Qian** | Chang'an → Samarkand | 138 BCE | `#d4a853` Desert Gold |
| 🪷 白绢扇归 | **Faxian** | Chang'an → India → Sri Lanka, at age 60 | 399 CE | `#5d8a7c` Ancient Green |
| 🧘 万里求法 | **Xuanzang** | Chang'an → Nalanda → Chang'an, 17 years | 629 CE | `#c47a38` Buddhist Gold |
| 🚢 鲸波万里 | **Zheng He** | Nanjing → East Africa, 7 voyages | 1405 CE | `#5ea3b8` Ocean Blue |
| 🏛 东方见闻录 | **Marco Polo** | Venice → Khanbaliq → Venice, 24 years | 1271 CE | `#c2714e` Venetian Red |
| 🏜 万里俘踪 | **Du Huan** | Talas → Baghdad → Africa → Guangzhou, 11 years as a war captive | 751 CE | `#b08040` Desert Bronze |

**🔍 Full-text Search** — Search across 116 entities in Chinese and English

**🌓 Bilingual** — Chinese / English toggle. All data, UI, and story text in both languages

## Data Scale

| Type | Count | Examples |
|------|-------|----------|
| 🏙 Cities | **40** | Chang'an, Samarkand, Baghdad, Venice, Mombasa, Lhasa |
| 👤 Figures | **23** | Zhang Qian, Faxian, Xuanzang, Zheng He, Marco Polo, Du Huan |
| 📦 Goods | **30** | Silk, paper, porcelain, tea, lapis lazuli, black pepper, musk |
| ⚡ Events | **23** | Zhang Qian's Mission, Battle of Talas, Islam Eastward Spread, Tea Trade Boom |
| 🔗 Edges | **326** | Every figure→city, goods→route, event→figure connection |
| 🎬 Routes | **8** | Silk Westward, Paper to Europe, Buddhism Eastward, Tea-Horse Road |
| 📖 Stories | **6** | 7 chapters each, interactive map flyover narration |

## Tech Stack

- **Data:** Single JSON file (43 KB) — the single source of truth
- **Frontend:** Vanilla HTML/CSS/JS — zero frameworks
- **Map:** [Leaflet.js](https://leafletjs.com/) + CartoDB dark tiles
- **Graph:** [D3.js v7](https://d3js.org/) force simulation
- **Animation:** Canvas + requestAnimationFrame
- **Deployment:** GitHub Pages — push to deploy, zero hosting cost

## Why this approach?

**Single data source → Multiple content forms.** Add one city to the JSON, and it instantly appears on the map, in the relationship graph, on the timeline, in the knowledge cards, and in the API output. No duplication, no drift.

```
JSON Data ──→ Map + Graph + Timeline + Cards + Stories + API
     ↑                                                      │
     └──────────── Community contributions ←────────────────┘
```

## Try It

```bash
git clone https://github.com/ScarlettLab2026/silk-road-2026.git
cd silk-road-2026
python3 -m http.server 8080
# Open http://localhost:8080
```

Or just visit the [live demo](https://ScarlettLab2026.github.io/silk-road-2026).

## Contribute

We welcome:
- New cities, figures, goods, or events
- Richer descriptions (Chinese + English)
- Historical corrections and fact-checking
- Translation improvements
- New interactive story suggestions

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details. All data is [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), all code is [MIT](./LICENSE).

## Support

- ❤️ [Aifadian](https://afdian.com/a/scarlettlab)
- ⭐ [GitHub Sponsors](https://github.com/sponsors/ScarlettLab2026)

---

<p align="center">
  <i>From Chang'an to Rome, from Quanzhou to Mombasa — every step made history.</i>
</p>
