const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const origin = process.argv[2] || 'http://127.0.0.1:8749';
const out = path.resolve(__dirname,'../artifacts/voyager-browser',new URL(origin).hostname);
fs.mkdirSync(out,{recursive:true});
(async()=>{
 const browser=await chromium.launch({headless:true});
 try {
  const page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(origin+'/articles/project-voyager/');
  const lab=page.locator('[data-voyager]');
  assert(await lab.locator('[data-v-controls]').isVisible());
  const old=async()=>parseFloat(await lab.locator('[data-v-old-value]').textContent());
  const fresh=async()=>parseFloat(await lab.locator('[data-v-new-value]').textContent());
  const snapshots={};
  for(const preset of ['open','rehearse','grip']) {
   await lab.locator('[data-v-preset="'+preset+'"]').click();
   for(let i=0;i<2;i++) await lab.locator('[data-v-step]').click();
   assert.equal(await fresh(),0,'Correction must not appear before step 12');
   await lab.locator('[data-v-step]').click();
   snapshots[preset]={old:await old(),correction:await fresh()};
   await lab.locator('[data-v-all]').click();
   assert(await lab.locator('[data-v-step]').isDisabled());
   assert.equal(await lab.locator('[data-v-step-label]').textContent(),'Step 32 / 32');
  }
  assert(snapshots.open.old<snapshots.grip.old);
  assert(snapshots.open.correction>snapshots.grip.correction);
  assert(snapshots.open.correction>85);
  assert(snapshots.grip.correction<15);
  // Boundary: with no rehearsal or interference, both traces remain once admitted.
  await lab.locator('#v-rehearsal').fill('0');
  await lab.locator('#v-interference').fill('0');
  await lab.locator('[data-v-all]').click();
  assert.equal(await old(),100);assert.equal(await fresh(),100);
  // Boundary: total rehearsal blocks the new input by construction.
  await lab.locator('#v-rehearsal').fill('100');
  assert.equal(await lab.locator('[data-v-step-label]').textContent(),'Step 0 / 32');
  await lab.locator('[data-v-all]').click();assert.equal(await fresh(),0);
  // Keyboard, reset, semantics and visible geometry.
  await lab.locator('[data-v-preset="rehearse"]').focus();await page.keyboard.press('Enter');
  assert.equal(await lab.locator('[data-v-preset="rehearse"]').getAttribute('aria-pressed'),'true');
  for(let i=0;i<3;i++)await lab.locator('[data-v-step]').click();
  await lab.screenshot({path:path.join(out,'interactive-desktop.png')});
  await page.evaluate(()=>scrollTo(0,0));await page.screenshot({path:path.join(out,'hero-desktop.png')});
  await page.evaluate(()=>document.activeElement.blur());
  for(const width of [390,320]) {
   await page.setViewportSize({width,height:844});
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Mobile horizontal overflow');
   await lab.screenshot({path:path.join(out,`interactive-${width}.png`)});
   await page.evaluate(()=>scrollTo(0,0));await page.screenshot({path:path.join(out,`hero-${width}.png`)});
   if(width===390)await page.screenshot({path:path.join(out,'article-mobile-full.png'),fullPage:true});
  }
  const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
  const plain=await nojs.newPage();await plain.goto(origin+'/articles/project-voyager/');
  assert(await plain.locator('[data-v-fallback]').isVisible());
  assert(!(await plain.locator('[data-v-controls]').isVisible()));
  await plain.locator('.v-method summary').click();
  assert(await plain.locator('.v-method a').isVisible());await nojs.close();
  const packet=await(await page.request.get(origin+'/articles/project-voyager/grok-packet.json')).json();
  assert.equal(packet.publish,'auto');assert.equal(packet.social_publication_status,'prepared-not-confirmed');
  assert.equal(packet.images.length,3);
  for(const url of [packet.markdown_url,...packet.images.map(i=>i.url),'https://neurasoft.us/assets/articles/project-voyager/research-snapshot.md']) {
   assert.equal((await page.request.get(url.replace('https://neurasoft.us',origin))).status(),200);
  }
  const inbox=await(await page.request.get(origin+'/articles/inbox.json')).json();
  assert(inbox.articles.some(a=>a.title==='Project Voyager'));
  assert.deepEqual(errors,[]);
  const report={origin,passed:true,snapshots,boundaryCases:2,keyboard:true,controlReset:true,mobileWidths:[390,320],noJavaScriptFallback:true,socialPacket:'prepared-not-confirmed',pageErrors:errors};
  fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
