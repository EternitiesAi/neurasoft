/* Optional build-time raster export. Requires an existing Sharp installation.
   SVG remains the editable original; no runtime dependency is added to the site. */
const path = require('node:path');
const sharp = require('sharp');
const base = path.resolve(__dirname, '../assets/articles/something-it-is-like-to-be/cover');
sharp(base + '.svg').png().toFile(base + '.png').then(() => console.log('Cover PNG exported from original SVG.'));
