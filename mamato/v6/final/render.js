// Renders every .board of posters.html to export/<id>.png at native size.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2400, height: 2200 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'posters.html'));
  await page.waitForSelector('body[data-ready="1"]');
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  const ids = await page.$$eval('.board', els => els.map(e => e.id));
  for (const id of ids) await page.locator('#' + id).screenshot({ path: path.join(process.env.OUT || path.join(__dirname, 'export'), (process.env.NAME_PREFIX||'') + id + '.png') });
  const missing = await page.evaluate(() => [...document.fonts].filter(f => f.status !== 'loaded').map(f => f.family + ' ' + f.style + ' ' + f.status));
  console.log('rendered', ids.join(', '), '| fonts not loaded (unused ok):', missing.length);
  await browser.close();
})();
