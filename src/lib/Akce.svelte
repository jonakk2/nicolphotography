<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
  import Lightbox from './Lightbox.svelte';
  import HeroSlider from './HeroSlider.svelte';
  import images from '../imageData/images.json';

  // Category definitions
  const categories = [
    {
      id: 'portraits',
      name: 'Portréty',
      cover: '/images/thumbnails/portraits/nahled_portrety.webp',
      desc: 'Osobní i profesionální portréty',
      position: '50% 18%'
    },
    {
      id: 'family',
      name: 'Rodiny',
      cover: '/images/thumbnails/family/nahled_rodinne.webp',
      desc: 'Rodinné momenty plné lásky',
      position: '50% 32%'
    },
    {
      id: 'couples',
      name: 'Páry',
      cover: '/images/thumbnails/couples/nahled_parove.webp',
      desc: 'Romantické focení párů',
      position: '50% 22%'
    },
    {
      id: 'animals',
      name: 'S domácími mazlíčky',
      cover: '/images/thumbnails/animals/nahled_sdomacimimazlicky.webp',
      desc: 'Focení s vašimi mazlíčky',
      position: '50% 25%'
    }
  ];

  // Gallery state
  let galleryOpen = false;
  let lightboxOpen = false;
  let currentCategory = null;
  let currentImageIndex = 0;
  let categoryImages = [];

  function openCategory(category) {
    currentCategory = category;
    categoryImages = images.filter(img => img.category === category.id);
    currentImageIndex = 0;
    galleryOpen = true;
    lightboxOpen = false;
    document.body.style.overflow = 'hidden';
  }

  function openLightbox(index) {
    currentImageIndex = index;
    lightboxOpen = true;
  }

  function closeLightbox() {
    lightboxOpen = false;
  }

  function closeGallery() {
    galleryOpen = false;
    lightboxOpen = false;
    currentCategory = null;
    document.body.style.overflow = '';
  }

  function handleKeydown(e) {
    if (e.key === 'Escape' && galleryOpen && !lightboxOpen) {
      closeGallery();
    }
  }
</script>

<svelte:head>
  <title>Portfolio | Nicol Juráňová photography</title>
  <meta name="description" content="Prohlédněte si ukázky focení od Nicol Juráňové - portréty, rodinné focení, párové focení a focení s domácími mazlíčky v přírodě." />
  <link rel="canonical" href="https://nicolphotography.cz/portfolio" />
  <meta property="og:title" content="Portfolio | Nicol Juráňová photography" />
  <meta property="og:description" content="Prohlédněte si ukázky focení - portréty, rodinné focení, párové focení a focení s domácími mazlíčky v přírodě." />
  <meta property="og:url" content="https://nicolphotography.cz/portfolio" />
  <meta property="og:image" content="https://nicolphotography.cz/hlavicka.png" />
  <meta property="og:type" content="website" />
</svelte:head>

<svelte:window on:keydown={handleKeydown} />

<div class="portfolio-page">
  <NavBar />

  <!-- Hero with Auto-Slider -->
  <section class="page-header" aria-label="Portfolio Nicol Juráňová">
    <HeroSlider />
    <div class="page-header-overlay" aria-hidden="true"></div>
    <div class="page-header-content">
      <span class="label">Portfolio</span>
      <h1>Moje práce</h1>
      <p>Prohlédněte si ukázky z mého focení</p>
    </div>
  </section>

  <!-- Categories -->
  <section class="categories">
    <div class="category-grid">
      {#each categories as category}
        <button class="category-tile" on:click={() => openCategory(category)}>
          <img src={category.cover} alt={category.name} style="object-position: {category.position || '50% 20%'};" loading="lazy" />
          <div class="category-overlay">
            <h3>{category.name}</h3>
            <p>{category.desc}</p>
            <span class="category-count">
              {images.filter(img => img.category === category.id).length} fotek
            </span>
          </div>
        </button>
      {/each}
    </div>
  </section>

  <!-- Gallery Modal -->
  {#if galleryOpen && categoryImages.length > 0}
    <div class="gallery-modal" role="dialog" aria-modal="true" aria-label="Galerie {currentCategory.name}">
      <button class="gallery-close" on:click={closeGallery} aria-label="Zavřít">×</button>

      <div class="gallery-header">
        <h3>{currentCategory.name}</h3>
        <span>{categoryImages.length} fotek</span>
      </div>

      <div class="gallery-grid">
        {#each categoryImages as img, i}
          <button
            class="gallery-thumb"
            on:click={() => openLightbox(i)}
            aria-label="Zobrazit fotku {i + 1}"
          >
            <img src={img.thumb || img.src} alt={img.alt} loading="lazy" />
          </button>
        {/each}
      </div>
    </div>
  {/if}

  <!-- Lightbox Component -->
  <Lightbox
    isOpen={lightboxOpen}
    images={categoryImages}
    currentIndex={currentImageIndex}
    categoryName={currentCategory ? currentCategory.name : ''}
    on:close={closeLightbox}
    on:change={(e) => (currentImageIndex = e.detail.index)}
  />

  <!-- Portfolio CTA -->
  <section class="portfolio-cta">
    <div class="portfolio-cta-content">
      <span class="label">Máte zájem o focení?</span>
      <h2>Líbí se vám můj styl?</h2>
      <p>Ať už plánujete rodinnou procházku, romantické párové focení nebo portrét při západu slunce, ráda pro vás zachytím přirozené momenty plné emocí.</p>
      <div class="portfolio-cta-buttons">
        <a href="/kontakt" class="cta-btn primary">Domluvit termín</a>
        <a href="/cenik" class="cta-btn secondary">Zobrazit ceník</a>
      </div>
    </div>
  </section>

  <Footer />
</div>

<style>
  .portfolio-page {
    --bg: #0a0a0a;
    --bg-secondary: #141414;
    --text: #ffffff;
    --text-muted: #888888;
    --accent: #c9a87c;

    background-color: var(--bg);
    color: var(--text);
    min-height: 100vh;
  }

  .label {
    color: var(--accent);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    display: block;
    margin-bottom: 1rem;
  }

  /* Page Header */
  .page-header {
    position: relative;
    height: 54vh;
    min-height: 440px;
    max-height: 640px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #0d0d0d;
    overflow: hidden;
    color: white;
  }

  .page-header-overlay {
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, rgba(13, 13, 13, 0.72) 0%, rgba(13, 13, 13, 0.52) 55%, rgba(13, 13, 13, 0.32) 100%);
    pointer-events: none;
    z-index: 1;
  }

  .page-header-content {
    position: relative;
    z-index: 2;
    text-align: center;
    max-width: 660px;
    padding: 0 1.5rem;
  }

  .page-header h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.5rem, 5vw, 4.2rem);
    color: white;
    margin-bottom: 1rem;
    text-shadow: 0 4px 24px rgba(0, 0, 0, 0.75);
  }

  .page-header p {
    font-size: clamp(1.05rem, 2vw, 1.25rem);
    opacity: 0.95;
    text-shadow: 0 2px 12px rgba(0, 0, 0, 0.85);
  }

  /* Categories */
  .categories {
    padding: 6rem 4rem;
  }

  .category-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .category-tile {
    position: relative;
    aspect-ratio: 4/3;
    overflow: hidden;
    cursor: pointer;
    border: none;
    padding: 0;
    background: none;
  }

  .category-tile img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.8s ease, filter 0.5s ease;
    filter: grayscale(30%) brightness(0.7);
  }

  .category-tile:hover img {
    transform: scale(1.1);
    filter: grayscale(0%) brightness(0.5);
  }

  .category-overlay {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 2rem;
  }

  .category-overlay h3 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    font-weight: 400;
    margin-bottom: 0.5rem;
    color: var(--text);
  }

  .category-overlay p {
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 1rem;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
  }

  .category-tile:hover .category-overlay p {
    opacity: 1;
    transform: translateY(0);
  }

  .category-count {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: var(--accent);
    padding: 0.5rem 1rem;
    border: 1px solid var(--accent);
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease 0.1s;
  }

  .category-tile:hover .category-count {
    opacity: 1;
    transform: translateY(0);
  }

  /* Gallery Modal */
  .gallery-modal {
    position: fixed;
    inset: 0;
    z-index: 9999;
    background: var(--bg);
    overflow-y: auto;
    padding: 6rem 4rem 4rem;
  }

  .gallery-close {
    position: fixed;
    top: 2rem;
    right: 2rem;
    background: none;
    border: none;
    color: var(--text);
    font-size: 2.5rem;
    cursor: pointer;
    opacity: 0.7;
    transition: opacity 0.3s ease;
    z-index: 10001;
  }

  .gallery-close:hover {
    opacity: 1;
  }

  .gallery-header {
    position: fixed;
    top: 2rem;
    left: 4rem;
    display: flex;
    align-items: center;
    gap: 2rem;
    z-index: 10001;
  }

  .gallery-header h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--text);
  }

  .gallery-header span {
    font-size: 0.8rem;
    color: var(--text-muted);
    letter-spacing: 0.1em;
  }

  .gallery-grid {
    columns: 3 320px;
    column-gap: 1.25rem;
    max-width: 1400px;
    margin: 0 auto;
  }

  .gallery-thumb {
    display: inline-block;
    width: 100%;
    margin-bottom: 1.25rem;
    break-inside: avoid;
    border-radius: 6px;
    overflow: hidden;
    cursor: pointer;
    border: none;
    padding: 0;
    background: #141414;
    transition: transform 0.35s ease, box-shadow 0.35s ease;
  }

  .gallery-thumb:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.45);
  }

  .gallery-thumb img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 6px;
    filter: grayscale(12%);
    transition: filter 0.3s ease, transform 0.5s ease;
  }

  .gallery-thumb:hover img {
    filter: grayscale(0%);
    transform: scale(1.02);
  }

  /* Portfolio CTA */
  .portfolio-cta {
    padding: 6rem 2rem;
    background-color: var(--bg-secondary);
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    text-align: center;
  }

  .portfolio-cta-content {
    max-width: 700px;
    margin: 0 auto;
  }

  .portfolio-cta-content h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 4vw, 2.75rem);
    font-weight: 400;
    margin-bottom: 1.25rem;
    color: var(--text);
  }

  .portfolio-cta-content p {
    color: var(--text-muted);
    font-size: 1.05rem;
    line-height: 1.7;
    margin-bottom: 2.5rem;
  }

  .portfolio-cta-buttons {
    display: flex;
    justify-content: center;
    gap: 1.25rem;
    flex-wrap: wrap;
  }

  .cta-btn {
    display: inline-block;
    padding: 1rem 2.5rem;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    text-decoration: none;
    transition: all 0.3s ease;
  }

  .cta-btn.primary {
    background: var(--accent);
    color: var(--bg);
  }

  .cta-btn.primary:hover {
    background: var(--text);
  }

  .cta-btn.secondary {
    background: transparent;
    color: var(--accent);
    border: 1px solid var(--accent);
  }

  .cta-btn.secondary:hover {
    background: var(--accent);
    color: var(--bg);
  }

  /* Responsive */
  @media (max-width: 768px) {
    .categories {
      padding: 4rem 1.5rem;
    }

    .category-grid {
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }

    .gallery-modal {
      padding: 5rem 1.5rem 2rem;
    }

    .gallery-header {
      left: 1.5rem;
    }

    .gallery-grid {
      columns: 2 140px;
      column-gap: 0.75rem;
    }

    .gallery-thumb {
      margin-bottom: 0.75rem;
      border-radius: 4px;
    }

    .gallery-thumb img {
      border-radius: 4px;
    }
  }
</style>
