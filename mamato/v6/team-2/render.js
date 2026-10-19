// Render every .board in posters.html to export/<id>.png (or img/ for ids starting with "alt-").
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2400, height: 2200 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'posters.html'));
  await page.waitForSelector('body[data-ready="1"]', { timeout: 20000 });
  await page.waitForTimeout(300);
  const ids = await page.$$eval('.board', els => els.map(e => e.id));
  const only = process.argv[2];
  for (const id of ids) {
    if (only && !id.includes(only)) continue;
    const dir = id.startsWith('alt-') ? 'img' : 'export';
    await page.locator('#' + id).screenshot({ path: path.join(__dirname, dir, id + '.png') });
  }
  await browser.close();
})();
