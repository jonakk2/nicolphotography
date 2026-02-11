<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
  import images from '../imageData/images.json';

  // Category definitions
  const categories = [
    {
      id: 'portraits',
      name: 'Portréty',
      cover: './src/images/thumbnails/portraits/nahled_portrety.webp',
      desc: 'Osobní i profesionální portréty'
    },
    {
      id: 'family',
      name: 'Rodiny',
      cover: './src/images/thumbnails/family/nahled_rodinne.webp',
      desc: 'Rodinné momenty plné lásky'
    },
    {
      id: 'couples',
      name: 'Páry',
      cover: './src/images/thumbnails/couples/nahled_parove.webp',
      desc: 'Romantické focení párů'
    },
    {
      id: 'animals',
      name: 'S domácími mazlíčky',
      cover: './src/images/thumbnails/animals/nahled_sdomacimimazlicky.webp',
      desc: 'Focení s vašimi mazlíčky'
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

  function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % categoryImages.length;
  }

  function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + categoryImages.length) % categoryImages.length;
  }

  function handleKeydown(e) {
    if (e.key === 'Escape') {
      if (lightboxOpen) {
        closeLightbox();
      } else if (galleryOpen) {
        closeGallery();
      }
    }
    if (lightboxOpen) {
      if (e.key === 'ArrowRight') nextImage();
      if (e.key === 'ArrowLeft') prevImage();
    }
  }
</script>

<svelte:head>
  <title>Portfolio | Nicol Juráňová photography</title>
  <meta name="description" content="Prohlédněte si ukázky focení od Nicol Juráňové - portréty, rodinné focení, párové focení a focení s domácími mazlíčky v přírodě." />
  <link rel="canonical" href="https://nicolphotography.cz/akce" />
  <meta property="og:title" content="Portfolio | Nicol Juráňová photography" />
  <meta property="og:description" content="Prohlédněte si ukázky focení - portréty, rodinné focení, párové focení a focení s domácími mazlíčky v přírodě." />
  <meta property="og:url" content="https://nicolphotography.cz/akce" />
  <meta property="og:image" content="https://nicolphotography.cz/hlavicka.png" />
  <meta property="og:type" content="website" />
</svelte:head>

<svelte:window on:keydown={handleKeydown} />

<div class="portfolio-page">
  <NavBar />

  <!-- Hero -->
  <section class="page-header">
    <div class="page-header-overlay"></div>
    <div class="page-header-content">
      <h1>Moje práce</h1>
      <p>Prohlédněte si ukázky z mého focení</p>
    </div>
  </section>

  <!-- Categories -->
  <section class="categories">
    <div class="category-grid">
      {#each categories as category}
        <button class="category-tile" on:click={() => openCategory(category)}>
          <img src={category.cover} alt={category.name} loading="lazy" />
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
    <div class="gallery-modal" role="dialog" aria-modal="true">
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

  <!-- Lightbox Modal -->
  {#if lightboxOpen && categoryImages.length > 0}
    <div class="lightbox" role="dialog" aria-modal="true" on:click={closeLightbox}>
      <button class="lightbox-close" on:click={closeLightbox} aria-label="Zpět">×</button>

      <div class="lightbox-header">
        <h3>{currentCategory.name}</h3>
        <span>{currentImageIndex + 1} / {categoryImages.length}</span>
      </div>

      <div class="lightbox-content" on:click|stopPropagation>
        <button class="lightbox-nav prev" on:click={prevImage} aria-label="Předchozí">‹</button>

        <div class="lightbox-image">
          <img src={categoryImages[currentImageIndex].src} alt={categoryImages[currentImageIndex].alt} />
        </div>

        <button class="lightbox-nav next" on:click={nextImage} aria-label="Další">›</button>
      </div>
    </div>
  {/if}

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
    height: 50vh;
    min-height: 400px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-image: url('./src/images/background/hlavicka.webp');
    background-size: cover;
    background-position: center;
    color: white;
  }

  .page-header-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.6));
  }

  .page-header-content {
    position: relative;
    z-index: 1;
    text-align: center;
  }

  .page-header h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.5rem, 5vw, 4rem);
    color: white;
    margin-bottom: 1rem;
  }

  .page-header p {
    font-size: 1.2rem;
    opacity: 0.9;
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
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
    max-width: 1400px;
    margin: 0 auto;
  }

  .gallery-thumb {
    aspect-ratio: 4/3;
    overflow: hidden;
    cursor: pointer;
    border: none;
    padding: 0;
    background: none;
    transition: transform 0.3s ease;
  }

  .gallery-thumb:hover {
    transform: scale(1.02);
  }

  .gallery-thumb img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: grayscale(20%);
    transition: filter 0.3s ease;
  }

  .gallery-thumb:hover img {
    filter: grayscale(0%);
  }

  /* Lightbox */
  .lightbox {
    position: fixed;
    inset: 0;
    z-index: 10000;
    background: rgba(0, 0, 0, 0.95);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem;
  }

  .lightbox-close {
    position: absolute;
    top: 2rem;
    right: 2rem;
    background: none;
    border: none;
    color: var(--text);
    font-size: 2.5rem;
    cursor: pointer;
    opacity: 0.7;
    transition: opacity 0.3s ease;
  }

  .lightbox-close:hover {
    opacity: 1;
  }

  .lightbox-header {
    position: absolute;
    top: 2rem;
    left: 2rem;
    display: flex;
    align-items: center;
    gap: 2rem;
  }

  .lightbox-header h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--text);
  }

  .lightbox-header span {
    font-size: 0.8rem;
    color: var(--text-muted);
  }

  .lightbox-content {
    display: flex;
    align-items: center;
    gap: 2rem;
    max-width: 90vw;
    max-height: 80vh;
  }

  .lightbox-nav {
    background: none;
    border: 1px solid rgba(255,255,255,0.2);
    color: var(--text);
    width: 50px;
    height: 50px;
    border-radius: 50%;
    font-size: 2rem;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .lightbox-nav:hover {
    background: var(--accent);
    border-color: var(--accent);
    color: var(--bg);
  }

  .lightbox-image img {
    max-width: 70vw;
    max-height: 75vh;
    object-fit: contain;
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
      grid-template-columns: repeat(2, 1fr);
      gap: 0.5rem;
    }

    .lightbox-content {
      flex-direction: column;
      gap: 1rem;
    }

    .lightbox-nav {
      width: 40px;
      height: 40px;
      font-size: 1.5rem;
    }

    .lightbox-image img {
      max-width: 90vw;
      max-height: 60vh;
    }
  }
</style>
