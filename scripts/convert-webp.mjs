import sharp from 'sharp';
import { readdir, stat } from 'fs/promises';
import { join, extname, basename } from 'path';

const dirs = [
  'src/images/thumbnails/portraits',
  'src/images/thumbnails/family',
  'src/images/thumbnails/couples',
  'src/images/thumbnails/animals',
  'src/images/background',
  'src/images/portfolio/about',
  'src/images/logo',
];

let converted = 0;
let skipped = 0;

async function convertDir(dir) {
  try {
    const files = await readdir(dir);
    for (const file of files) {
      const ext = extname(file).toLowerCase();
      if (['.jpg', '.jpeg', '.png'].includes(ext)) {
        const input = join(dir, file);
        const output = join(dir, basename(file, ext) + '.webp');
        try {
          const info = await stat(output).catch(() => null);
          if (info) { skipped++; continue; }
          await sharp(input).webp({ quality: 80 }).toFile(output);
          converted++;
          console.log(`Converted: ${input} -> ${output}`);
        } catch (e) {
          console.error(`Error converting ${input}: ${e.message}`);
        }
      }
    }
  } catch (e) {
    console.error(`Dir not found: ${dir}`);
  }
}

for (const dir of dirs) {
  await convertDir(dir);
}

console.log(`\nDone: ${converted} converted, ${skipped} skipped`);
