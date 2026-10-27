const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const origin=process.argv[2]||'http://127.0.0.1:8745';
const out=path.resolve(__dirname,'../artifacts/shape-browser');
fs.mkdirSync(out,{recursive:true});
(async()=>{
 const browser=await chromium.launch({headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 try{
  await page.goto(origin+'/articles/the-shape-of-someone/');
  const desk=page.locator('[data-continuity]');
  let states=0;
  for(const mode of ['archive','learning','revision']){
   await desk.locator('[data-continuity-mode="'+mode+'"]').click();
   for(const remove of [false,true])for(const evidence of [false,true]){
    await desk.locator('[data-remove-history]').setChecked(remove);
    await desk.locator('[data-new-evidence]').setChecked(evidence);
    const key=mode+'-'+(Number(remove)+2*Number(evidence));
    const expected=await desk.locator('[data-continuity-case="'+key+'"] [data-choice]').textContent();
    assert.equal(await desk.locator('[data-current-choice]').textContent(),expected);states++;
   }
  }
  await desk.locator('[data-continuity-mode="archive"]').focus();
  await page.keyboard.press('Enter');
  assert.equal(await desk.locator('[data-continuity-mode="archive"]').getAttribute('aria-pressed'),'true');
  await desk.locator('[data-continuity-mode="revision"]').click();
  await desk.locator('[data-remove-history]').uncheck();
  await desk.locator('[data-new-evidence]').check();
  await desk.screenshot({path:path.join(out,'desk-desktop.png')});
  await page.evaluate(()=>scrollTo(0,0));
  await page.screenshot({path:path.join(out,'article-desktop.png')});
  await page.setViewportSize({width:390,height:844});
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await desk.screenshot({path:path.join(out,'desk-mobile.png')});
  await page.goto(origin+'/assets/papers/when-history-changes-the-agent/');
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  for(const href of ['when-history-changes-the-agent.pdf','research-bundle.zip','analytic-checks.json']){
   assert.equal((await page.request.get(origin+'/assets/papers/when-history-changes-the-agent/'+href)).status(),200);
  }
  const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
  const plain=await nojs.newPage();await plain.goto(origin+'/articles/the-shape-of-someone/');
  await plain.locator('[data-continuity-stories] summary').filter({hasText:'Revise a choice'}).click();
  assert(await plain.locator('[data-continuity-case="revision-2"]').isVisible());
  await nojs.close();
  const packet=await (await page.request.get(origin+'/articles/the-shape-of-someone/grok-packet.json')).json();
  assert.equal(packet.publish,'auto');assert.equal(packet.social_publication_status,'prepared-not-confirmed');
  assert.deepEqual(packet.social_request.platforms,['x','linkedin']);
  assert.deepEqual(errors,[]);
  const report={origin,interactionStates:states,keyboard:true,mobileOverflow:false,noJavaScriptFallback:true,paperDownloads:true,releasedSocialPacket:true,pageErrors:errors};
  fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
