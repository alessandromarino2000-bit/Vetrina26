const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1500,height:900}});
await p.goto('file://'+process.argv[2]);await p.waitForSelector('body[data-ready="1"]');await p.waitForTimeout(300);
await p.screenshot({path:process.argv[3],fullPage:true});await b.close();})();
