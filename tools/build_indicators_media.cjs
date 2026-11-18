/* Cover for "What held, what failed, and what we have not tested."
   Each square is one row of the article's results table, in row order. The marks encode the verdicts stated there
   (held, mixed, untested, failed/corrected/retired); they are not a chart of any measured quantity. */
const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
const dir = path.resolve(__dirname, '../assets/articles/what-held-and-what-failed');
fs.mkdirSync(dir, {recursive: true});
const paper = '#f3f2e8', ink = '#243c32', sage = '#365d47', copper = '#a8623f', muted = '#596458', line = '#cbd2c2';
// row order from the table: F failed/corrected/retired, M mixed, H held, U untested
const rows = ['F','M','H','F','F','F','F','F','F','M','F','M','M','F','U'];
const size = 86, gap = 26, x0 = 600, y0 = 170;
const squares = rows.map((v, i) => {
  const x = x0 + (i % 5) * (size + gap), y = y0 + Math.floor(i / 5) * (size + gap);
  const n = `<text x="${x + 8}" y="${y + 18}" font-family="Consolas,monospace" font-size="11" fill="${v === 'H' ? paper : muted}">${String(i + 1).padStart(2, '0')}</text>`;
  if (v === 'H') return `<rect x="${x}" y="${y}" width="${size}" height="${size}" fill="${sage}"/>${n}`;
  if (v === 'M') return `<rect x="${x}" y="${y}" width="${size}" height="${size}" fill="none" stroke="${sage}" stroke-width="2"/><path d="M${x} ${y + size}L${x + size} ${y}V${y + size}Z" fill="${sage}" opacity=".55"/>${n}`;
  if (v === 'U') return `<rect x="${x}" y="${y}" width="${size}" height="${size}" fill="none" stroke="${muted}" stroke-width="1.5" stroke-dasharray="5 6"/>${n}`;
  return `<rect x="${x}" y="${y}" width="${size}" height="${size}" fill="none" stroke="${copper}" stroke-width="2"/><path d="M${x + 14} ${y + size - 14}L${x + size - 14} ${y + 14}" stroke="${copper}" stroke-width="2"/>${n}`;
}).join('');
const key = [['H', 'held, narrowly', 1], ['M', 'mixed', 4], ['F', 'failed, corrected or retired', 9], ['U', 'not yet tested', 1]].map(([v, label, count], i) => {
  const x = 66, y = 388 + i * 40, s = 22;
  const mark = v === 'H' ? `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="${sage}"/>`
    : v === 'M' ? `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="none" stroke="${sage}" stroke-width="1.5"/><path d="M${x} ${y + s}L${x + s} ${y}V${y + s}Z" fill="${sage}" opacity=".55"/>`
    : v === 'U' ? `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="none" stroke="${muted}" stroke-width="1.2" stroke-dasharray="3 4"/>`
    : `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="none" stroke="${copper}" stroke-width="1.5"/><path d="M${x + 4} ${y + s - 4}L${x + s - 4} ${y + 4}" stroke="${copper}" stroke-width="1.5"/>`;
  return `${mark}<text x="${x + 38}" y="${y + 17}" font-family="Arial,sans-serif" font-size="18" fill="${ink}">${count} ${label}</text>`;
}).join('');
const cover = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="${paper}"/><path d="M66 96H1134" stroke="${line}"/><text x="66" y="62" font-family="Arial,sans-serif" font-size="14" letter-spacing="4" fill="${muted}">NEURASOFT / RESEARCH RECORD</text><text x="1134" y="62" text-anchor="end" font-family="Arial,sans-serif" font-size="14" letter-spacing="2" fill="${muted}">18 NOVEMBER 2026</text><g font-family="Georgia,serif" fill="${ink}"><text x="66" y="196" font-size="52">What held.</text><text x="66" y="258" font-size="52">What failed.</text><text x="66" y="320" font-size="52" font-style="italic">What is untested.</text></g>${key}${squares}<path d="M66 566H1134" stroke="${line}"/><text x="66" y="596" font-family="Arial,sans-serif" font-size="13" letter-spacing="1" fill="${muted}">EACH SQUARE IS ONE ROW OF THE RESULTS TABLE, IN ORDER. THE MARKS ARE VERDICTS, NOT MEASUREMENTS.</text></svg>`;
(async () => {
  fs.writeFileSync(path.join(dir, 'cover.svg'), cover);
  await sharp(Buffer.from(cover)).png().toFile(path.join(dir, 'cover.png'));
  console.log('Indicators: cover SVG and PNG written.');
})().catch((e) => { console.error(e); process.exitCode = 1; });
