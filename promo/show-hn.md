# Show HN 发帖套件

## 发帖步骤

1. 打开 https://news.ycombinator.com
2. 注册账号（邮箱+用户名+密码，30秒）
3. 点右上角 **submit**
4. **Title** 填标题
5. **URL** 填网站链接
6. 点 submit
7. 帖子发布后，立刻在评论区发第一条评论（First Comment）

---

## Title（标题）

```
Show HN: Silk Road Knowledge Graph — interactive map of 2,000 years of East-West exchange
```

备选（更短）：
```
Show HN: I mapped 6 historical journeys across the Silk Road — interactive and open source
```

---

## URL

```
https://scarlettlab2026.github.io/silk-road-2026
```

---

## First Comment（发布后立刻在评论区粘贴）

```
I visited the Mogao Caves in Dunhuang last month. On those thousand-year-old murals, I saw Persian merchants, Indian monks, and Roman envoys — all meeting in one cave because of one road.

When I came back, I tried to learn more. The knowledge was scattered across dozens of Wikipedia pages. To trace how papermaking reached Europe, I needed 5 different pages open. To understand Zhang Qian's route, I needed 10 tabs.

So I built this — a structured knowledge graph of the Silk Road, rendered as an interactive website.

What it does:
- 40 cities pinned on real coordinates across Eurasia, the Indian Ocean, and East Africa
- 326 relationships connecting cities, figures, goods, and events
- 6 interactive stories where the map flies from city to city as you read (Zhang Qian, Faxian, Xuanzang, Zheng He, Marco Polo, and Du Huan — a Tang dynasty war captive who became the first Chinese person to document Africa)
- 8 animated trade routes (silk, paper, gunpowder, Buddhism, etc.) with golden dots traveling across the map
- Bilingual Chinese/English — one-click toggle
- Full-text search across 116 entities

Tech: Pure vanilla JS, zero frameworks. One JSON file (43KB) is the single source of truth. Add a city to the JSON, and it instantly appears on the map, the graph, the timeline, and the stories. Hosted on GitHub Pages at zero cost.

Everything is open source: data under CC BY-SA 4.0, code under MIT.

I'd love feedback on:
- The interactive stories (do they work well? are they engaging?)
- Performance (the site is all client-side)
- What other stories or routes would you want to see?

GitHub: https://github.com/ScarlettLab2026/silk-road-2026
```

---

## 如果有人在评论区问问题，常见回答参考

**Q: Why not use a framework?**
A: Wanted to keep the dependency count at zero and make it trivially deployable (just HTML files on GitHub Pages). The entire site is ~2,500 lines of code across 6 story files + one main page.

**Q: How did you collect the data?**
A: Manually compiled from historical sources, academic papers, and Wikipedia. Cross-referenced Chinese and English materials. The JSON file is CC BY-SA 4.0 — anyone can use it.

**Q: Can I add my own data?**
A: Yes! The JSON schema is straightforward — cities, figures, goods, events, and edges. PRs welcome.

**Q: Does it work on mobile?**
A: It's functional but not optimized. The map and graph views work. The sidebar gets narrow. Desktop recommended for the full experience.

---

## 发帖时间建议

- 最佳：周二/周三太平洋时间 7:00 AM（北京时间约 22:00-23:00）
- HN 流量曲线：太平洋时间 6:00-10:00 AM 最高
- 避免：周末、周五下午
