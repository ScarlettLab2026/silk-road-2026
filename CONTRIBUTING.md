# 贡献指南 / Contributing Guide

感谢你对丝绸之路知识图谱项目的兴趣！

## 数据贡献方式

### 1. 添加新实体

在 [`data/silk-road.json`](./data/silk-road.json) 中，找到对应的节点类型（`cities`、`figures`、`goods`、`events`），按以下格式添加新条目：

**城市**
```json
{
  "id": "unique-id",
  "name": "中文名",
  "name_en": "English Name",
  "modern_name": "现代地名",
  "modern_name_en": "Modern English Name",
  "country": "所在国家",
  "country_en": "Country",
  "lat": 0.0,
  "lng": 0.0,
  "era": "活跃年代",
  "dynasties": ["相关朝代"],
  "role": "在丝路中的角色",
  "role_en": "Role on the Silk Road",
  "description": "详细描述（建议100-200字）",
  "description_en": "Description in English",
  "significance": 3
}
```

**人物**
```json
{
  "id": "unique-id",
  "name": "姓名",
  "name_en": "English Name",
  "type": "身份标签",
  "type_en": "Role Label",
  "era": "朝代",
  "era_range": "生卒年",
  "description": "...",
  "description_en": "...",
  "significance": 3
}
```

**物产**
```json
{
  "id": "unique-id",
  "name": "名称",
  "name_en": "English Name",
  "category": "分类",
  "category_en": "Category",
  "origin": "原产地",
  "origin_en": "Origin",
  "direction": "传播方向",
  "direction_en": "Direction of Spread",
  "description": "...",
  "description_en": "...",
  "significance": 3
}
```

**事件**
```json
{
  "id": "unique-id",
  "name": "事件名",
  "name_en": "Event Name",
  "year": 0,
  "display_year": "显示年份",
  "dynasty": "朝代",
  "description": "...",
  "description_en": "...",
  "significance": 3
}
```

### 2. 添加关系边

在 `edges` 数组中添加新关系：

```json
{
  "source": "entity-id-1",
  "target": "entity-id-2",
  "relation": "关系描述",
  "relation_en": "Relationship Description"
}
```

### 3. significance 评分标准

| 分值 | 含义 |
|------|------|
| 5 | 核心节点：离开此节点丝路叙事不完整 |
| 4 | 重要节点：对理解丝路有显著贡献 |
| 3 | 一般节点：区域性或辅助性实体 |
| 2 | 次要节点：周边信息 |
| 1 | 待考证：信息不够充分 |

### 4. 提交前检查

```bash
# 验证 JSON 格式
python3 -m json.tool data/silk-road.json > /dev/null && echo "JSON 有效"

# 本地预览
python3 -m http.server 8080
# 浏览器打开 http://localhost:8080
```

## 创建交互故事

想为一位丝路旅行家制作交互地图故事？使用我们的模板：

1. **复制模板**: 从 [`.github/STORY_TEMPLATE.html`](./.github/STORY_TEMPLATE.html) 复制故事骨架
2. **添加数据**: 在 `data/silk-road.json` 中补充人物、事件和关系边
3. **编写叙事**: 填写 7 章 STORY 数组（每章标题、副标题、正文、坐标、路线、关联实体）
4. **更新导航**: 在所有现有故事文件的 `#story-nav` 和 `index.html` 的故事按钮行中添加新链接
5. **更新 meta**: 将 `index.html` 中的故事计数递增
6. **提交 PR**: 参考 [`.github/pull_request_template.md`](./.github/pull_request_template.md) 检查清单

故事引擎会自动处理：地图飞越、路线绘制、城市标记、实体标签、键盘导航、暗/亮切换。你只需要提供 `STORY_CONFIG` 和 `STORY` 数据。

## 行为准则

- 确保描述文本基于可查证的历史资料
- 有争议的历史内容请注明出处或保留多个观点
- 保持中英双语同步
- 尊重不同文化和民族的历史叙事
