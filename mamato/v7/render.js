// Esporta ogni artboard di posters.html in PNG a risoluzione nativa.
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2400, height: 2200 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'posters.html'));
  await page.waitForSelector('body[data-ready="1"]');
  await page.waitForTimeout(300);
  const ids = await page.$$eval('.board', els => els.map(e => e.id));
  const only = process.argv[2];
  for (const id of ids) {
    if (only && !id.startsWith(only)) continue;
    await page.locator('#' + id).screenshot({ path: path.join(__dirname, 'export', `mamato-v7-${id}.png`) });
  }
  await browser.close();
})();
