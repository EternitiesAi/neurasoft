const {test} = require('node:test');
const assert = require('node:assert/strict');
const {searchPages} = require('../assets/search.js');

const pages = [
  {url:'/luna/',title:'Luna',description:'A continuing system',text:'A self-model connects memory and learning.'},
  {url:'/study/',title:'Learning from consequences',description:'An isolated comparison',text:'Conditioned choice.'},
  {url:'/glossary/',title:'Glossary',description:'Terms',text:'A consequence is an effect of an action.'},
];
test('search reaches public body text', () => assert.deepEqual(searchPages(pages,'self-model').map(p=>p.url), ['/luna/']));
test('hyphen variants and case normalize', () => assert.deepEqual(searchPages(pages,'SELF—MODEL').map(p=>p.url), ['/luna/']));
test('title matches rank above body-only matches', () => assert.equal(searchPages(pages,'learning')[0].url, '/study/'));
test('all query words must match', () => assert.deepEqual(searchPages(pages,'learning consequence').map(p=>p.url), ['/study/']));
test('no match is empty, without interpreting HTML', () => assert.deepEqual(searchPages(pages,'<script>alert(1)</script>'), []));
test('stable empty query and result limit', () => assert.deepEqual(searchPages(pages,'',2), pages.slice(0,2)));

test('official acronym and ordinary luna query reach the same public page', () => {
  const named = [{url:'/luna/', title:'L.U.N.A', description:'Lifeform of Unified Noetic Agency', text:''}];
  for (const query of ['luna', 'L.U.N.A', 'l.u.n.a.']) assert.equal(searchPages(named, query)[0]?.url, '/luna/');
});
