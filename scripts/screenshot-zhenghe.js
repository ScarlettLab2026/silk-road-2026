const { webkit } = require('playwright');
const path = require('path');

const OUT = '/Users/scarlett/silk-road/output/screenshots';
const LIVE = 'https://scarlettlab2026.github.io/silk-road-2026';

(async () => {
  const browser = await webkit.launch();
  const ctx = await browser.newContext({
    viewport: { width: 1280, height: 900 },
    deviceScaleFactor: 2,
  });

  async function shot(name, url, opts = {}) {
    const { wait = 4000, noMap = false, darkMode = true, blockTiles = false } = opts;
    const p = await ctx.newPage();

    // Block tile requests for pages with maps
    if (blockTiles) {
      await p.route('**/*', (route) => {
        const u = route.request().url();
        // Block Leaflet entirely + tiles to prevent WebKit hang
        if (u.includes('unpkg.com/leaflet') || u.includes('cartodb') || u.includes('openstreetmap') || (u.includes('.png') && u.includes('tile'))) {
          route.abort();
        } else {
          route.continue();
        }
      });
    }

    if (noMap) {
      await p.addStyleTag({ content: '#map, .leaflet-container, .leaflet-pane, .leaflet-tile, .leaflet-control-container { display: none !important; }' });
    }

    try {
      console.log(`  📸 ${name}...`);
      await p.goto(url, { waitUntil: 'load', timeout: 30000 });
      await p.waitForTimeout(wait);

      if (darkMode) {
        await p.evaluate(() => {
          const html = document.documentElement;
          if (html.classList.contains('light')) html.classList.remove('light');
        });
        await p.waitForTimeout(500);
      }

      const screenshotOpts = { path: path.join(OUT, name), timeout: 45000 };
      screenshotOpts.fullPage = true;
      await p.screenshot(screenshotOpts);
      console.log(`    ✅ ${name}`);
    } catch (e) {
      console.log(`    ❌ ${name}: ${e.message?.slice(0, 120)}`);
    } finally {
      await p.close();
    }
  }

  // ─── 图1: 封面 郑和卡片 (暗色模式) ───
  await shot('zhenghe-01-card-cover.png', `${LIVE}/cards.html`, { wait: 5000 });

  // ─── 图2: 郑和卡片 (亮色模式) ───
  const p2 = await ctx.newPage();
  try {
    await p2.goto(`${LIVE}/cards.html`, { waitUntil: 'load', timeout: 20000 });
    await p2.waitForTimeout(4000);
    await p2.evaluate(() => document.documentElement.classList.add('light'));
    await p2.waitForTimeout(1000);
    await p2.screenshot({ path: path.join(OUT, 'zhenghe-02-card-light.png'), fullPage: true, timeout: 45000 });
    console.log('    ✅ zhenghe-02-card-light.png');
  } catch (e) {
    console.log(`    ❌ light card: ${e.message?.slice(0, 120)}`);
  } finally {
    await p2.close();
  }

  // ─── 图3: story2 郑和 (blockTiles, 地图黑底 + 叙事卡) ───
  await shot('zhenghe-03-story-chapter.png', `${LIVE}/story2.html`, { wait: 5000, blockTiles: true });

  // ─── 图4: story2 noMap 纯叙事卡 ───
  await shot('zhenghe-04-story-narrative.png', `${LIVE}/story2.html`, { wait: 4000, noMap: true, blockTiles: true });

  // ─── 图5: 主页 index (带地图) ───
  await shot('zhenghe-05-index.png', LIVE, { wait: 6000, blockTiles: true });

  // ─── 图6: 主页 index noMap ───
  await shot('zhenghe-06-index-content.png', LIVE, { wait: 4000, noMap: true, blockTiles: true });

  await browser.close();
  console.log(`\n🎉 Done! Screenshots saved to ${OUT}/`);
})();
