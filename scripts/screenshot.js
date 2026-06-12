const { webkit } = require('playwright');
const path = require('path');
const fs = require('fs');

const OUT = '/Users/scarlett/silk-road/output/screenshots';
const LIVE = 'https://scarlettlab2026.github.io/silk-road-2026';

(async () => {
  const browser = await webkit.launch();
  const ctx = await browser.newContext({
    viewport: { width: 1280, height: 900 },
    deviceScaleFactor: 2,
  });

  async function shot(name, url, opts = {}) {
    const { fullPage = false, wait = 4000, noMap = false } = opts;
    const p = await ctx.newPage();

    // Block tiles
    await p.route('**/*', (route) => {
      const u = route.request().url();
      if (u.includes('tile.openstreetmap.org') || u.includes('cartodb')) route.abort();
      else route.continue();
    });

    // For story pages: hide map BEFORE page loads
    if (noMap) {
      await p.addStyleTag({ content: '#map, .leaflet-container { display: none !important; }' });
    }

    try {
      console.log(`  ${name}...`);
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
      await p.waitForTimeout(wait);

      if (noMap) {
        await p.evaluate(() => {
          for (let i = 1; i < 99999; i++) { clearInterval(i); clearTimeout(i); }
        });
        await p.waitForTimeout(300);
      }

      await p.screenshot({ path: path.join(OUT, name), fullPage, timeout: 30000 });
      console.log(`    OK`);
    } catch(e) {
      console.log(`    FAIL: ${e.message?.slice(0,100)}`);
    } finally {
      await p.close();
    }
  }

  await shot('01-index-map.png', LIVE, { wait: 5000 });
  await shot('02-index-full.png', LIVE, { fullPage: true, wait: 5000 });
  await shot('03-cards.png', `${LIVE}/cards.html`, { fullPage: true, wait: 3000 });
  await shot('04-video.png', `${LIVE}/video.html`, { wait: 3000 });

  const stories = [
    ['05-zhangqian.png', 'story.html'],
    ['06-zhenghe.png', 'story2.html'],
    ['07-xuanzang.png', 'story3.html'],
    ['08-faxian.png', 'story4.html'],
    ['09-marcopolo.png', 'story5.html'],
  ];
  for (const [name, url] of stories) {
    await shot(name, `${LIVE}/${url}`, { wait: 5000, noMap: true });
  }

  await shot('10-api.png', `${LIVE}/api.html`, { wait: 3000 });

  await browser.close();
  console.log(`\nDone! ${fs.readdirSync(OUT).length} files`);
})();
