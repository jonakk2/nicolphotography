<script>
  import NavBar from '../../lib/NavBar.svelte';
  import Footer from '../../lib/Footer.svelte';
  import Lightbox from '../../lib/Lightbox.svelte';
  import BeforeAfter from '../../lib/BeforeAfter.svelte';
  import images from '../../imageData/images.json';

  // Hero auto-slider images from Nicol's portfolio
  const sliderImages = [
    { src: '/images/slider/IMG_0185.webp', alt: 'Přirozené rodinné a párové focení v přírodě' },
    { src: '/images/slider/IMG_1012.webp', alt: 'Autentické portréty s přirozeným světlem' },
    { src: '/images/slider/IMG_1324.webp', alt: 'Příběh a emoce zachycené v krajině' },
    { src: '/images/slider/IMG_5037.webp', alt: 'Uvolněná atmosféra při venkovním focení' },
    { src: '/images/slider/IMG_8256.webp', alt: 'Párové focení při západu slunce' },
    { src: '/images/slider/IMG_8999.webp', alt: 'Krásné okamžiky uprostřed přírody' },
    { src: '/images/slider/IMG_9363.webp', alt: 'Rodinné vzpomínky, které vydrží navždy' }
  ];

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

  // Testimonials for social proof
  const testimonials = [
    {
      name: 'Marie S.',
      type: 'Rodinné focení',
      location: 'Hranice',
      text: 'Nicolka je skvělá! Děti se při focení cítily naprosto přirozeně a fotky jsou kouzelné. Žádné nucené pózy, prostě čistá radost. Určitě se k ní vrátíme.'
    },
    {
      name: 'Dominik & Klára',
      type: 'Párové focení',
      location: 'Olomouc',
      text: 'Focení při západu slunce v makovém poli bylo nezapomenutelné. Nicol přesně věděla, jak nás navést, abychom se necítili trapně. Fotky předčily naše očekávání.'
    },
    {
      name: 'Veronika P.',
      type: 'Focení s pejskem',
      location: 'Lipník nad Bečvou',
      text: 'Měla jsem trochu strach, jak to náš divoký pes zvládne, ale Nicol měla neuvěřitelnou trpělivost. Výsledné momentky jsou nádherné a hotové byly do 10 dnů.'
    }
  ];

  // Instagram showcase posts
  const instagramPosts = [
    { src: '/images/portfolio/portraits/IMG_8731.webp', alt: 'Portrétní focení v přírodě' },
    { src: '/images/portfolio/couples/IMG_4716.jpg', alt: 'Párové focení při západu slunce' },
    { src: '/images/portfolio/family/IMG_8974.webp', alt: 'Rodinné focení' },
    { src: '/images/portfolio/animals/IMG_8428.webp', alt: 'Focení s pejskem v trávě' },
    { src: '/images/portfolio/portraits/IMG_8575.webp', alt: 'Dívčí portrét ve zlaté hodince' },
    { src: '/images/portfolio/family/IMG_9363.webp', alt: 'Spontánní dětský smích v přírodě' }
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
  <title>Nicol Juráňová photography | Fotografka Olomoucký kraj</title>
  <meta name="description" content="Nicol Juráňová - fotografka z Hranic na Moravě. Fotím portréty, rodiny a páry venku v přírodě." />
  <link rel="canonical" href="https://nicolphotography.cz/" />
</svelte:head>

<svelte:window on:keydown={handleKeydown} />

<div class="moody-theme">
  <NavBar />

  <!-- Page Header with Auto-Slider -->
  <section class="page-header" aria-label="Ukázky fotografií Nicol Juráňové">
    <div class="hero-slider-container">
      <div class="hero-slider-track">
        {#each [...sliderImages, ...sliderImages] as img, i}
          <div class="hero-slider-slide">
            <img src={img.src} alt={img.alt} loading={i < 4 ? "eager" : "lazy"} />
          </div>
        {/each}
      </div>
    </div>
    <div class="hero-slider-vignette-left" aria-hidden="true"></div>
    <div class="hero-slider-vignette-right" aria-hidden="true"></div>
    <div class="page-header-overlay" aria-hidden="true"></div>
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
      <h2>Nicol<br/><em>Juráňová</em></h2>
      <p>Focením se zabývám několik let. Nejradši fotím venku — rodinné, párové i portrétové fotky. Zakládám si na uvolněné atmosféře, kde se nemusíte přetvařovat.</p>
      <a href="/about" class="link">Více o mně →</a>
    </div>
  </section>

  <!-- How it works -->
  <section class="values">
    <div class="values-grid">
      <div class="value-card">
        <h3>Žádné nucené pózy</h3>
        <p>Fotím spontánně. Řeknu vám kam se postavit a co dělat, ale nečekejte strnulé úsměvy do kamery. Tyhle fotky pak vypadají nejlíp.</p>
      </div>
      <div class="value-card">
        <h3>Venku je to nejhezčí</h3>
        <p>Focení probíhá v přírodě — louky, lesy, cesty. Olomoucký kraj má spoustu krásných míst a ráda vám poradím s výběrem.</p>
      </div>
      <div class="value-card">
        <h3>Fotky do 14 dnů</h3>
        <p>Po focení dostanete online galerii, vyberete si fotky a já je upravím. Žádné měsíce čekání.</p>
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

  <!-- Lightbox Component -->
  <Lightbox
    isOpen={lightboxOpen}
    images={categoryImages}
    currentIndex={currentImageIndex}
    categoryName={currentCategory ? currentCategory.name : ''}
    on:close={closeLightbox}
    on:change={(e) => (currentImageIndex = e.detail.index)}
  />

  <!-- Seasonal Christmas Mini-Sessions Banner -->
  <section class="xmas-banner-section">
    <div class="xmas-banner-card">
      <div class="xmas-banner-content">
        <span class="xmas-banner-badge">✨ Limitovaná sezónní nabídka</span>
        <h2>Vánoční focení 2026 – venkovní scenérie</h2>
        <p>Vánoční atmosféra uprostřed přírody, horký čaj z termosky, teplá deka a přirozené okamžiky bez spěchu. 30 minut na čerstvém vzduchu, 8 precizně upravených fotografií a garance dodání do Vánoc pod stromeček.</p>
        <div class="xmas-banner-meta">
          <span>📅 Listopad & Prosinec 2026</span>
          <span>📍 Příroda (Olomoucký kraj)</span>
          <span>🏷️ 1 500 Kč (záloha 500 Kč)</span>
        </div>
      </div>
      <div class="xmas-banner-action">
        <a href="/vanocni-foceni" class="btn-xmas-cta">
          <span>Vybrat termín & rezervovat</span>
          <span class="cta-arrow">→</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Testimonials / Social Proof -->
  <section class="testimonials">
    <div class="testimonials-header">
      <span class="label">Reference</span>
      <h2>Co říkají klienti</h2>
      <p class="testimonials-sub">Největší radost mám, když se před foťákem uvolníte a odnesete si nejen fotky, ale i příjemný zážitek.</p>
    </div>
    <div class="testimonials-grid">
      {#each testimonials as t}
        <div class="testimonial-card">
          <div class="stars" aria-label="5 hvězdiček z 5">★★★★★</div>
          <p class="quote">„{t.text}“</p>
          <div class="author-info">
            <span class="author-name">{t.name}</span>
            <span class="author-meta">{t.type} · {t.location}</span>
          </div>
        </div>
      {/each}
    </div>
  </section>

  <!-- Before / After Edit Showcase -->
  <section class="retouch-section">
    <div class="retouch-header">
      <span class="label">Můj styl úpravy</span>
      <h2>Přirozené barvy bez filtrů</h2>
      <p class="retouch-sub">Posuňte jezdcem pro srovnání. Fotografie ladím citlivě do teplých přírodních tónů — bez voskové retuše a s důrazem na skutečné emoce.</p>
    </div>
    <BeforeAfter />
  </section>

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
          <li>Online galerie k výběru</li>
          <li>Dodání do 14 dnů</li>
        </ul>
        <a href="/kontakt" class="pricing-cta">Mám zájem</a>
      </div>
      <p class="pricing-note">Portréty, páry, rodiny i focení se zvířátky — vše za jednotnou cenu.</p>
      <div class="pricing-extra-links">
        <a href="/cenik" class="extra-link">Kompletní ceník a dárkové poukazy →</a>
        <a href="/pruvodce" class="extra-link">Průvodce: Jak se připravit a co na sebe →</a>
      </div>
    </div>
  </section>

  <!-- Instagram Social Showcase -->
  <section class="instagram-section">
    <div class="instagram-header">
      <span class="label">Sledujte mě na Instagramu</span>
      <h2>@n.i.c.o.l_photography</h2>
      <p class="instagram-sub">Aktuální střípky z focení v přírodě, zákulisí a nové volné termíny.</p>
    </div>

    <div class="instagram-grid">
      {#each instagramPosts as post}
        <a
          href="https://www.instagram.com/n.i.c.o.l_photography/"
          target="_blank"
          rel="noopener noreferrer"
          class="instagram-item"
          aria-label={post.alt}
        >
          <img src={post.src} alt={post.alt} loading="lazy" />
          <div class="instagram-overlay">
            <span class="ig-icon" aria-hidden="true">📸</span>
            <span class="ig-hover-text">Zobrazit na Instagramu</span>
          </div>
        </a>
      {/each}
    </div>

    <div class="instagram-footer">
      <a
        href="https://www.instagram.com/n.i.c.o.l_photography/"
        target="_blank"
        rel="noopener noreferrer"
        class="btn-instagram"
      >
        <svg class="ig-svg-icon" viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
          <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
        </svg>
        Sledovat @n.i.c.o.l_photography
      </a>
    </div>
  </section>

  <!-- CTA - Dramatic -->
  <section class="cta">
    <div class="cta-content">
      <h2>Chcete se<br/>objednat?</h2>
      <p class="cta-text">Napište mi, domluvíme termín a místo. Pokud máte vlastní nápad na focení, klidně sem s ním.</p>
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

  /* Page Header / Hero Auto-Slider */
  .page-header {
    position: relative;
    height: 56vh;
    min-height: 480px;
    max-height: 680px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #0d0d0d;
    overflow: hidden;
    color: white;
  }

  .hero-slider-container {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    pointer-events: auto;
    z-index: 0;
  }

  .hero-slider-track {
    display: flex;
    gap: 16px;
    width: max-content;
    height: 100%;
    animation: heroSliderScroll 50s linear infinite;
    will-change: transform;
  }

  .hero-slider-container:hover .hero-slider-track {
    animation-play-state: paused;
  }

  @keyframes heroSliderScroll {
    0% {
      transform: translate3d(0, 0, 0);
    }
    100% {
      transform: translate3d(-50%, 0, 0);
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .hero-slider-track {
      animation: none;
    }
  }

  .hero-slider-slide {
    flex: 0 0 auto;
    height: 100%;
    width: 320px;
    position: relative;
    overflow: hidden;
    border-radius: 4px;
  }

  @media (min-width: 1024px) {
    .hero-slider-slide {
      width: 380px;
    }
  }

  .hero-slider-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    display: block;
    filter: brightness(0.78) contrast(1.05);
    transition: filter 0.4s ease, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .hero-slider-slide:hover img {
    filter: brightness(0.95) contrast(1.05);
    transform: scale(1.03);
  }

  /* Left and right edge fades */
  .hero-slider-vignette-left,
  .hero-slider-vignette-right {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 18vw;
    min-width: 90px;
    pointer-events: none;
    z-index: 1;
  }

  .hero-slider-vignette-left {
    left: 0;
    background: linear-gradient(to right, rgba(13, 13, 13, 0.95) 0%, transparent 100%);
  }

  .hero-slider-vignette-right {
    right: 0;
    background: linear-gradient(to left, rgba(13, 13, 13, 0.95) 0%, transparent 100%);
  }

  .page-header-overlay {
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, rgba(13, 13, 13, 0.72) 0%, rgba(13, 13, 13, 0.5) 55%, rgba(13, 13, 13, 0.3) 100%);
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
    margin-bottom: 2rem;
    line-height: 1.8;
    text-shadow: 0 2px 12px rgba(0, 0, 0, 0.85);
  }

  .hero-cta {
    display: inline-block;
    padding: 1rem 2.5rem;
    border: 1px solid rgba(255, 255, 255, 0.85);
    background: rgba(0, 0, 0, 0.35);
    backdrop-filter: blur(8px);
    color: white;
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
  }

  .hero-cta:hover {
    background: white;
    color: var(--color-primary, #1a1a1a);
    box-shadow: 0 6px 20px rgba(255, 255, 255, 0.25);
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

  /* Testimonials */
  .testimonials {
    padding: 7rem 2rem;
    background-color: #0d0d0d;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  }

  .testimonials-header {
    text-align: center;
    max-width: 650px;
    margin: 0 auto 3.5rem;
  }

  .testimonials-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 4vw, 2.75rem);
    font-weight: 400;
    margin-bottom: 1rem;
    color: var(--text);
  }

  .testimonials-sub {
    color: var(--text-muted);
    font-size: 1rem;
    line-height: 1.6;
    margin: 0;
  }

  .testimonials-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .testimonial-card {
    background-color: #141414;
    border: 1px solid rgba(201, 168, 124, 0.15);
    border-radius: 8px;
    padding: 2.25rem 2rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.3s ease;
  }

  .testimonial-card:hover {
    border-color: rgba(201, 168, 124, 0.4);
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  }

  .stars {
    color: var(--accent);
    font-size: 1.1rem;
    letter-spacing: 0.15em;
    margin-bottom: 1.25rem;
  }

  .quote {
    color: rgba(255, 255, 255, 0.88);
    font-size: 0.95rem;
    line-height: 1.7;
    margin: 0 0 1.5rem;
    font-style: italic;
    flex: 1;
  }

  .author-info {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 1rem;
  }

  .author-name {
    font-weight: 600;
    color: #ffffff;
    font-size: 0.95rem;
  }

  .author-meta {
    font-size: 0.8rem;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  @media (max-width: 900px) {
    .testimonials-grid {
      grid-template-columns: 1fr;
      max-width: 550px;
      gap: 1.5rem;
    }

    .testimonials {
      padding: 5rem 1.5rem;
    }
  }

  /* Retouch Showcase */
  .retouch-section {
    padding: 7rem 1.5rem;
    background-color: #0b0b0b;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
  }

  .retouch-header {
    text-align: center;
    max-width: 650px;
    margin: 0 auto 3.5rem;
  }

  .retouch-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 4vw, 2.75rem);
    font-weight: 400;
    margin-bottom: 1rem;
    color: var(--text);
  }

  .retouch-sub {
    color: var(--text-muted);
    font-size: 1rem;
    line-height: 1.6;
    margin: 0;
  }

  .pricing-extra-links {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-top: 2rem;
  }

  .extra-link {
    color: var(--accent);
    font-size: 0.9rem;
    text-decoration: none;
    letter-spacing: 0.02em;
    transition: all 0.2s ease;
  }

  .extra-link:hover {
    color: #ffffff;
    text-decoration: underline;
    text-underline-offset: 3px;
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

  /* Instagram Social Showcase */
  .instagram-section {
    padding: 6rem 2rem 5rem;
    background-color: #0b0b0b;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    text-align: center;
  }

  .instagram-header {
    max-width: 650px;
    margin: 0 auto 3rem;
  }

  .instagram-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.8rem, 3.5vw, 2.5rem);
    font-weight: 400;
    margin-bottom: 0.75rem;
    color: var(--text);
  }

  .instagram-sub {
    color: var(--text-muted);
    font-size: 1rem;
    line-height: 1.6;
    margin: 0;
  }

  .instagram-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 0.75rem;
    max-width: 1400px;
    margin: 0 auto 2.5rem;
  }

  .instagram-item {
    position: relative;
    aspect-ratio: 1 / 1;
    overflow: hidden;
    border-radius: 4px;
    display: block;
    background: #141414;
  }

  .instagram-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease, filter 0.4s ease;
  }

  .instagram-overlay {
    position: absolute;
    inset: 0;
    background: rgba(10, 10, 10, 0.7);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    opacity: 0;
    transition: opacity 0.3s ease;
    backdrop-filter: blur(2px);
  }

  .ig-icon {
    font-size: 1.5rem;
  }

  .ig-hover-text {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--accent);
    font-weight: 500;
  }

  .instagram-item:hover img {
    transform: scale(1.06);
  }

  .instagram-item:hover .instagram-overlay {
    opacity: 1;
  }

  .instagram-footer {
    margin-top: 1.5rem;
  }

  .btn-instagram {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.9rem 2rem;
    background: transparent;
    color: var(--accent);
    border: 1px solid var(--accent);
    text-decoration: none;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    border-radius: 2px;
    transition: all 0.3s ease;
  }

  .btn-instagram:hover {
    background: var(--accent);
    color: var(--bg);
  }

  .ig-svg-icon {
    transition: transform 0.2s ease;
  }

  .btn-instagram:hover .ig-svg-icon {
    transform: scale(1.1);
  }

  @media (max-width: 1024px) {
    .instagram-grid {
      grid-template-columns: repeat(3, 1fr);
    }
  }

  @media (max-width: 600px) {
    .instagram-grid {
      grid-template-columns: repeat(2, 1fr);
      gap: 0.5rem;
    }

    .instagram-section {
      padding: 4.5rem 1rem 3.5rem;
    }
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
  }

  /* Christmas Banner Section */
  .xmas-banner-section {
    padding: 2rem 2rem 5rem;
    max-width: 1300px;
    margin: 0 auto;
  }

  .xmas-banner-card {
    background: radial-gradient(circle at 90% 10%, rgba(192, 57, 43, 0.22) 0%, rgba(20, 16, 15, 0.95) 60%),
                linear-gradient(135deg, rgba(30, 24, 20, 0.9) 0%, rgba(15, 13, 12, 0.95) 100%);
    border: 1px solid rgba(201, 168, 124, 0.35);
    border-radius: 16px;
    padding: 3rem 2.5rem;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    transition: border-color 0.3s ease;
  }

  @media (min-width: 900px) {
    .xmas-banner-card {
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      padding: 3.5rem 4rem;
    }
    .xmas-banner-content {
      max-width: 65%;
    }
  }

  .xmas-banner-badge {
    display: inline-block;
    background: rgba(201, 168, 124, 0.15);
    border: 1px solid rgba(201, 168, 124, 0.4);
    color: #e5b982;
    padding: 0.35rem 0.95rem;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: 1rem;
    letter-spacing: 0.04em;
  }

  .xmas-banner-card h2 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2.15rem;
    color: #f7f7f7;
    margin-bottom: 1rem;
    line-height: 1.25;
  }

  .xmas-banner-card p {
    color: #b5b5b5;
    font-size: 1.05rem;
    line-height: 1.65;
    margin-bottom: 1.5rem;
  }

  .xmas-banner-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem 1.5rem;
    font-size: 0.9rem;
    color: #c9a87c;
  }

  .xmas-banner-action {
    flex-shrink: 0;
  }

  .btn-xmas-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1.15rem 2.25rem;
    background: linear-gradient(135deg, #c9a87c 0%, #b89261 100%);
    color: #121212;
    font-weight: 600;
    font-size: 1.05rem;
    border-radius: 8px;
    text-decoration: none;
    box-shadow: 0 4px 25px rgba(201, 168, 124, 0.4);
    transition: all 0.25s ease;
    white-space: nowrap;
  }

  .btn-xmas-cta:hover {
    background: linear-gradient(135deg, #d8b88d 0%, #c49e6d 100%);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(201, 168, 124, 0.55);
  }

  .cta-arrow {
    transition: transform 0.2s ease;
  }

  .btn-xmas-cta:hover .cta-arrow {
    transform: translateX(4px);
  }
</style>
