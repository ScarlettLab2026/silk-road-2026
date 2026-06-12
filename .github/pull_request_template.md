## Story Contribution Checklist

Thanks for contributing a new Silk Road interactive story! Please verify:

### Before Submitting

- [ ] **New story file**: Created `storyN.html` using `.github/STORY_TEMPLATE.html`
- [ ] **Unique accent color**: Picked a color not used by existing stories (#d4a853, #5d8a7c, #c47a38, #5ea3b8, #c2714e, #b08040, #3a7ca5)
- [ ] **Nav updated**: Added new story link to `#story-nav` in ALL existing story files
- [ ] **Index updated**: Added new story button to the header row in `index.html` with correct border-radius (first story has `16px 0 0 16px`, last has `0 16px 16px 0`, middle have `0`)
- [ ] **Meta updated**: Incremented story count in `index.html` meta descriptions (e.g. "7 interactive stories" → "8 interactive stories")

### Data Checklist

- [ ] **Figure added**: New figure in `data/silk-road.json` under `nodes.figures` with `id`, `name`, `name_en`, `type`, `era`, `description`, `significance` (1-5)
- [ ] **Event added**: New event in `data/silk-road.json` under `nodes.events` connected to the figure
- [ ] **Edges added**: Relationships connecting the figure and event to relevant cities/goods/events
- [ ] **City data verified**: All cities referenced in STORY have correct `lat`/`lng` in the dataset
- [ ] **JSON valid**: Run `python3 -m json.tool data/silk-road.json` — no errors

### Quality Checklist

- [ ] **7 chapters**: Each chapter has `title`, `subtitle`, `body`, `lat`, `lng`, `zoom`, `route`, `marker`, `showCities`, `highlight`
- [ ] **Routes are cumulative**: Each chapter's `route` array includes all previous chapter cities (e.g. ch3 route = ch2 route + new city)
- [ ] **Bilingual descriptions**: Figure and event have both `name`/`name_en` and `description`/`description_en`
- [ ] **Mobile tested**: Viewed on mobile viewport (375px) — nav wraps, card readable
- [ ] **English mode checked**: Switched to English — key names and descriptions appear correctly

### Verification

1. Start local server: `python3 -m http.server 8080`
2. Open `localhost:8080/storyN.html`
3. Click through all 7 chapters — map flies, routes draw, badges render
4. Test keyboard navigation: ArrowRight/ArrowLeft/Space
5. Test restart button
6. Test light/dark theme toggle
7. Open `localhost:8080` — new story appears in header row
8. Click new story from index — navigates correctly
