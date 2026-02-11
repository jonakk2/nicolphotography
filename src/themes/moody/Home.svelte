<script>
  import NavBar from '../../lib/NavBar.svelte';
  import Footer from '../../lib/Footer.svelte';
  import images from '../../imageData/images.json';

  // Category definitions with cover images
  const categories = [
    {
      id: 'portraits',
      name: 'Portréty',
      cover: '/images/thumbnails/portraits/nahled_portrety.webp',
      desc: 'Osobní i profesionální portréty'
    },
    {
      id: 'family',
      name: 'Rodiny',
      cover: '/images/thumbnails/family/nahled_rodinne.webp',
      desc: 'Rodinné momenty plné lásky'
    },
    {
      id: 'couples',
      name: 'Páry',
      cover: '/images/thumbnails/couples/nahled_parove.webp',
      desc: 'Romantické focení párů'
    },
    {
      id: 'animals',
      name: 'S domácími mazlíčky',
      cover: '/images/thumbnails/animals/nahled_sdomacimimazlicky.webp',
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
  <title>Nicol Juráňová photography | Fotografka Olomoucký kraj</title>
  <meta name="description" content="Nicol Juráňová - fotografka z Olomouckého kraje. Portrétní, rodinné a párové focení v přírodě. Spontánní fotky plné emocí." />
  <link rel="canonical" href="https://nicolphotography.cz/" />
</svelte:head>

<svelte:window on:keydown={handleKeydown} />

<div class="moody-theme">
  <NavBar />

  <!-- Page Header -->
  <section class="page-header">
    <div class="page-header-overlay"></div>
    <div class="page-header-content">
      <h1>Nicol Juráňová</h1>
      <p>Pokud máte na fotkách nejraději<br/>jako pozadí naši krásnou přírodu,<br/>pak jste tady správně.</p>
      <a href="/kontakt" class="hero-cta">Spojme se</a>
    </div>
  </section>

  <!-- About - Dramatic split -->
  <section class="about">
    <div class="about-image">
      <img src="/images/portfolio/about/IMG_3078-2.webp" alt="Nicol Juráňová" loading="lazy" />
    </div>
    <div class="about-content">
      <span class="label">O mně</span>
      <h2>Vítejte na<br/>mém <em>webu</em></h2>
      <p>Mé jméno je Nicol Juráňová a focením se zabývám již pár let. Nejčastěji fotím rodinné, párové nebo portrétové fotografie s pozadím, které vytvořila sama příroda.</p>
      <a href="/about" class="link">Více o mně →</a>
    </div>
  </section>

  <!-- Values -->
  <section class="values">
    <div class="values-grid">
      <div class="value-card">
        <span class="value-number">01</span>
        <h3>Autenticita</h3>
        <p>Věřím, že nejkrásnější fotografie jsou ty přirozené. Nesnažím se vytvářet umělé pózy, ale zachycuji skutečné emoce a momenty.</p>
      </div>
      <div class="value-card">
        <span class="value-number">02</span>
        <h3>Příběh</h3>
        <p>Každá fotografie má svůj příběh. Mým cílem je tento příběh najít a předat ho tak, aby vám přinášel radost i po letech.</p>
      </div>
      <div class="value-card">
        <span class="value-number">03</span>
        <h3>Pohodlí</h3>
        <p>Chci, abyste se při focení cítili přirozeně a uvolněně. Vytváříme společně atmosféru, ve které můžete být sami sebou.</p>
      </div>
    </div>
  </section>

  <!-- Portfolio Categories -->
  <section class="portfolio">
    <div class="portfolio-header">
      <span class="label">Portfolio</span>
      <h2>Moje práce</h2>
    </div>
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

  <!-- Gallery Modal (grid of thumbnails) -->
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

  <!-- Lightbox Modal (single large image) -->
  {#if lightboxOpen && categoryImages.length > 0}
    <div class="lightbox" role="dialog" aria-modal="true" aria-label="Fotka" on:click={closeLightbox} on:keydown={handleKeydown}>
      <button class="lightbox-close" on:click={closeLightbox} aria-label="Zpět na galerii">×</button>

      <div class="lightbox-header">
        <h3>{currentCategory.name}</h3>
        <span>{currentImageIndex + 1} / {categoryImages.length}</span>
      </div>

      <div class="lightbox-content" role="presentation" on:click|stopPropagation on:keydown|stopPropagation>
        <button class="lightbox-nav prev" on:click={prevImage} aria-label="Předchozí fotka">‹</button>

        <div class="lightbox-image">
          <img src={categoryImages[currentImageIndex].src} alt={categoryImages[currentImageIndex].alt} />
        </div>

        <button class="lightbox-nav next" on:click={nextImage} aria-label="Další fotka">›</button>
      </div>
    </div>
  {/if}

  <!-- Pricing -->
  <section class="pricing">
    <div class="pricing-header">
      <span class="label">Ceník</span>
      <h2>Focení v přírodě</h2>
    </div>
    <div class="pricing-card">
      <div class="pricing-main">
        <span class="pricing-duration">1-2 hodiny focení</span>
        <div class="pricing-price">
          <span class="price-amount">1 500</span>
          <span class="price-currency">Kč</span>
        </div>
        <ul class="pricing-features">
          <li>10 upravených fotografií</li>
          <li>Online galerie</li>
          <li>Dodání do 14 dnů</li>
        </ul>
        <a href="/kontakt" class="pricing-cta">Mám zájem</a>
      </div>
      <p class="pricing-note">Portréty, páry, rodiny i focení se zvířátky - vše za jednotnou cenu.</p>
    </div>
  </section>

  <!-- CTA - Dramatic -->
  <section class="cta">
    <div class="cta-content">
      <h2>Pojďme vytvořit<br/>něco krásného</h2>
      <p class="cta-text">Pokud máte v hlavě i jiný nápad na focení, sem s ním! Budu se těšit.</p>
      <a href="/kontakt" class="cta-btn">Kontaktovat</a>
    </div>
    <div class="cta-image">
      <img src="/images/background/pojdmevytvoritnecokrasneho.webp" alt="Rodinné focení v přírodě" loading="lazy" />
    </div>
  </section>

  <Footer />
</div>

<style>
  .moody-theme {
    --bg: #0a0a0a;
    --bg-secondary: #141414;
    --text: #ffffff;
    --text-muted: #888888;
    --accent: #c9a87c;

    background-color: var(--bg);
    color: var(--text);
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
    background-image: url('/images/background/hlavicka.webp');
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
    margin-bottom: 2rem;
    line-height: 1.8;
  }

  .hero-cta {
    display: inline-block;
    padding: 1rem 2.5rem;
    border: 1px solid white;
    color: white;
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    transition: all 0.3s ease;
  }

  .hero-cta:hover {
    background: white;
    color: var(--color-primary);
  }


  /* About */
  .about {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 100vh;
  }

  .about-image {
    position: relative;
    overflow: hidden;
  }

  .about-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: grayscale(30%);
  }

  .about-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 4rem 6rem;
    background: var(--bg-secondary);
  }

  .about-content h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 4vw, 3.5rem);
    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 2rem;
  }

  .about-content h2 em {
    color: var(--accent);
    font-style: italic;
  }

  .about-content p {
    color: var(--text-muted);
    line-height: 1.9;
    max-width: 400px;
    margin-bottom: 2rem;
  }

  .link {
    color: var(--accent);
    text-decoration: none;
    font-size: 0.85rem;
    letter-spacing: 0.1em;
    transition: transform 0.3s ease;
    display: inline-block;
  }

  .link:hover {
    transform: translateX(10px);
  }

  /* Values */
  .values {
    padding: 6rem 4rem;
    background: var(--bg);
  }

  .values-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .value-card {
    padding: 2.5rem 2rem;
    background: var(--bg-secondary);
    border: 1px solid #222;
  }

  .value-number {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    color: var(--accent);
    display: block;
    margin-bottom: 1.5rem;
    opacity: 0.5;
  }

  .value-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    font-weight: 400;
    margin-bottom: 1rem;
    color: var(--text);
  }

  .value-card p {
    color: var(--text-muted);
    font-size: 0.9rem;
    line-height: 1.8;
  }

  /* Portfolio Categories */
  .portfolio {
    padding: 8rem 4rem;
    background: var(--bg);
  }

  .portfolio-header {
    text-align: center;
    margin-bottom: 4rem;
  }

  .portfolio-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 400;
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
    transition: all 0.3s ease;
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
    line-height: 1;
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
    line-height: 1;
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
    letter-spacing: 0.1em;
  }

  .lightbox-content {
    display: flex;
    align-items: center;
    gap: 2rem;
    max-width: 90vw;
    max-height: 70vh;
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

  .lightbox-image {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .lightbox-image img {
    max-width: 70vw;
    max-height: 60vh;
    object-fit: contain;
  }

  .lightbox-caption {
    margin-top: 1rem;
    font-size: 0.9rem;
    color: var(--text-muted);
    text-align: center;
  }

  /* Pricing */
  .pricing {
    padding: 8rem 4rem;
    background: var(--bg-secondary);
  }

  .pricing-header {
    text-align: center;
    margin-bottom: 4rem;
  }

  .pricing-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 400;
  }

  .pricing-card {
    max-width: 500px;
    margin: 0 auto;
    text-align: center;
  }

  .pricing-main {
    padding: 3rem;
    border: 1px solid var(--accent);
    background: var(--bg);
  }

  .pricing-duration {
    display: block;
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 1.5rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }

  .pricing-price {
    margin-bottom: 2rem;
  }

  .price-amount {
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    color: var(--accent);
    font-weight: 400;
  }

  .price-currency {
    font-size: 1.5rem;
    color: var(--text-muted);
    margin-left: 0.5rem;
  }

  .pricing-features {
    list-style: none;
    padding: 0;
    margin: 0 0 2rem 0;
  }

  .pricing-features li {
    padding: 0.75rem 0;
    border-bottom: 1px solid #222;
    color: var(--text);
    font-size: 0.95rem;
  }

  .pricing-features li:last-child {
    border-bottom: none;
  }

  .pricing-cta {
    display: inline-block;
    padding: 1rem 3rem;
    background: var(--accent);
    color: var(--bg);
    text-decoration: none;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    transition: all 0.3s ease;
  }

  .pricing-cta:hover {
    background: var(--text);
  }

  .pricing-note {
    margin-top: 2rem;
    color: var(--text-muted);
    font-size: 0.9rem;
    font-style: italic;
  }

  /* CTA */
  .cta {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 60vh;
  }

  .cta-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 4rem 6rem;
    background: var(--bg);
  }

  .cta-content h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 400;
    line-height: 1.3;
    margin-bottom: 2rem;
  }

  .cta-btn {
    padding: 1rem 2.5rem;
    background: var(--accent);
    color: var(--bg);
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    transition: all 0.3s ease;
  }

  .cta-btn:hover {
    background: var(--text);
  }

  .cta-text {
    color: var(--text-muted);
    font-size: 1rem;
    line-height: 1.7;
    margin-bottom: 2rem;
  }

  .cta-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  /* Responsive */
  @media (max-width: 1024px) {
    .values-grid {
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }
  }

  @media (max-width: 768px) {
    .about {
      grid-template-columns: 1fr;
    }

    .about-content {
      padding: 3rem 2rem;
    }

    .about-image {
      height: 50vh;
    }

    .values {
      padding: 4rem 2rem;
    }

    .portfolio {
      padding: 4rem 1.5rem;
    }

    .category-grid {
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }

    .pricing {
      padding: 4rem 1.5rem;
    }

    .pricing-main {
      padding: 2rem;
    }

    .price-amount {
      font-size: 3rem;
    }

    .cta {
      grid-template-columns: 1fr;
    }

    .cta-content {
      padding: 3rem 2rem;
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
      max-height: 50vh;
    }

    .lightbox-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 0.5rem;
    }
  }
</style>
