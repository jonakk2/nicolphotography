import sharp from 'sharp';
import { readdir, readFile, writeFile, mkdir } from 'fs/promises';
import { join, basename, extname } from 'path';

const MAPPINGS = [
  {
    folder: 'nove_fotky/Ruby - pes',
    category: 'animals',
    alt: 'Focení s pejskem v přírodě'
  },
  {
    folder: 'nove_fotky/portrety - misa',
    category: 'portraits',
    alt: 'Portrét v přírodě'
  },
  {
    folder: 'nove_fotky/rodinne_foceni',
    category: 'family',
    alt: 'Rodinné focení v přírodě'
  }
];

const IMAGES_JSON_PATH = 'src/imageData/images.json';

async function run() {
  const imagesRaw = await readFile(IMAGES_JSON_PATH, 'utf-8');
  const imagesList = JSON.parse(imagesRaw);
  const existingSrcs = new Set(imagesList.map(img => img.src));

  let addedCount = 0;

  for (const item of MAPPINGS) {
    const portfolioDir = join('public', 'images', 'portfolio', item.category);
    const thumbDir = join('public', 'images', 'thumbnails', item.category);

    await mkdir(portfolioDir, { recursive: true });
    await mkdir(thumbDir, { recursive: true });

    const files = await readdir(item.folder);

    for (const file of files) {
      const ext = extname(file).toLowerCase();
      if (!['.jpg', '.jpeg', '.png'].includes(ext)) continue;

      const base = basename(file, ext);
      const inputPath = join(item.folder, file);

      const targetWebJpg = join(portfolioDir, `${base}.jpg`);
      const targetWebWebp = join(portfolioDir, `${base}.webp`);
      const targetThumbJpg = join(thumbDir, `${base}.jpg`);
      const targetThumbWebp = join(thumbDir, `${base}.webp`);

      // 1. Process portfolio web image (max 1920x1280)
      const imagePipeline = sharp(inputPath).rotate();
      await imagePipeline
        .clone()
        .resize({ width: 1920, height: 1280, fit: 'inside', withoutEnlargement: true })
        .jpeg({ quality: 85, progressive: true })
        .toFile(targetWebJpg);

      await imagePipeline
        .clone()
        .resize({ width: 1920, height: 1280, fit: 'inside', withoutEnlargement: true })
        .webp({ quality: 85 })
        .toFile(targetWebWebp);

      // 2. Process thumbnail (400x300, 4:3 cover crop)
      await imagePipeline
        .clone()
        .resize({ width: 400, height: 300, fit: 'cover', position: 'attention' })
        .jpeg({ quality: 80, progressive: true })
        .toFile(targetThumbJpg);

      await imagePipeline
        .clone()
        .resize({ width: 400, height: 300, fit: 'cover', position: 'attention' })
        .webp({ quality: 80 })
        .toFile(targetThumbWebp);

      const webSrc = `/images/portfolio/${item.category}/${base}.jpg`;
      const thumbSrc = `/images/thumbnails/${item.category}/${base}.webp`;

      if (!existingSrcs.has(webSrc)) {
        imagesList.push({
          src: webSrc,
          thumb: thumbSrc,
          alt: item.alt,
          category: item.category
        });
        existingSrcs.add(webSrc);
        addedCount++;
        console.log(`✓ Přidána fotografie: ${file} (${item.category})`);
      } else {
        console.log(`- Již existuje: ${webSrc}`);
      }
    }
  }

  await writeFile(IMAGES_JSON_PATH, JSON.stringify(imagesList, null, 2) + '\n');
  console.log(`\nDokončeno! Přidáno ${addedCount} nových fotografií. Celkem v portfoliu: ${imagesList.length} fotografií.`);
}

run().catch(err => {
  console.error('Chyba při zpracování fotografií:', err);
  process.exit(1);
});
