const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:2400,height:2200}});
await p.goto('file:///home/user/Vetrina26/mamato/v6/final/posters.html');await p.waitForSelector('body[data-ready="1"]');
const r=await p.$$eval('.board',bs=>bs.map(bd=>{const B=bd.getBoundingClientRect();let top=1e9,bot=0;
 bd.querySelectorAll('.mast img,.tag,.copy *').forEach(e=>{const q=e.getBoundingClientRect();if(q.height){top=Math.min(top,q.top-B.top);bot=Math.max(bot,q.bottom-B.top)}});
 const col=[...bd.querySelectorAll('.col')].map(c=>{const l=c.lastElementChild.getBoundingClientRect();return Math.round(l.bottom-B.top)});
 return {id:bd.id,top:Math.round(top),bot:Math.round(bot),colBottoms:col,text:bd.querySelector('.copy').innerText.replace(/\n+/g,' | ')}}));
console.log(JSON.stringify(r,null,1));await b.close();})();
