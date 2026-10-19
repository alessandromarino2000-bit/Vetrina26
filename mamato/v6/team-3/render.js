// Renders every .board of posters.html to export/<id>.png (team-3 / Cinema)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2400, height: 2200 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'posters.html'));
  await page.waitForSelector('body[data-ready="1"]', { timeout: 20000 });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  const ids = await page.$$eval('.board', els => els.map(e => e.id));
  for (const id of ids) {
    await page.locator('#' + id).screenshot({ path: path.join(__dirname, 'export', `${id}.png`) });
  }
  console.log(await page.$$eval('.stack', els => els.map(e => e.parentElement.id+': stack top '+e.offsetTop)));
  // font check
  const fonts = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight + ' ' + f.style));
  console.log('loaded fonts:', [...new Set(fonts)].join(' | '));
  await browser.close();
})();
