<script>
  import NavBar from '../../lib/NavBar.svelte';
  import Footer from '../../lib/Footer.svelte';
  import images from '../../imageData/images.json';
</script>

<div class="editorial-theme">
  <NavBar />

  <!-- Hero - Asymmetric -->
  <section class="hero">
    <div class="hero-text">
      <span class="hero-label">Fotografka / Olomoucký kraj</span>
      <h1>
        <span class="line">Příběhy</span>
        <span class="line indent">zachycené</span>
        <span class="line">světlem</span>
      </h1>
    </div>
    <div class="hero-image">
      <img src="/images/portfolio/golden-hour.png" alt="Golden hour" />
      <div class="hero-image-caption">
        <span>01</span>
        <p>Golden Hour / Vysočina 2024</p>
      </div>
    </div>
    <a href="/kontakt" class="hero-cta">
      <span>Domluvit</span>
      <span>focení</span>
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">
        <path d="M5 12h14M12 5l7 7-7 7"/>
      </svg>
    </a>
  </section>

  <!-- About - Editorial split -->
  <section class="about">
    <div class="about-left">
      <div class="about-image-1">
        <img src="/images/portfolio/nicol-portret.png" alt="Nicol" />
      </div>
      <div class="about-stats">
        <div class="stat">
          <span class="stat-num">40+</span>
          <span class="stat-label">klientů</span>
        </div>
        <div class="stat">
          <span class="stat-num">3</span>
          <span class="stat-label">roky</span>
        </div>
      </div>
    </div>
    <div class="about-right">
      <span class="section-num">01</span>
      <h2>O mně</h2>
      <p class="large-text">Jsem Nicol — fotografka, která věří, že každý okamžik má svou vlastní krásu.</p>
      <p>Specializuji se na portrétní a rodinnou fotografii. Miluji práci s přirozeným světlem, zejména golden hour. Působím v Olomouckém kraji, ale ráda přijedu kamkoliv.</p>
      <a href="/about" class="text-link">Celý příběh</a>
    </div>
  </section>

  <!-- Gallery - Magazine layout -->
  <section class="gallery">
    <div class="gallery-header">
      <span class="section-num">02</span>
      <h2>Vybrané<br/>práce</h2>
    </div>
    <div class="gallery-layout">
      <div class="gallery-col-left">
        <div class="gallery-item large">
          <img src={images[0]?.src} alt={images[0]?.alt} />
          <span class="item-label">{images[0]?.title || 'Portrét'}</span>
        </div>
        <div class="gallery-item">
          <img src={images[3]?.src} alt={images[3]?.alt} />
          <span class="item-label">{images[3]?.title || 'Focení'}</span>
        </div>
      </div>
      <div class="gallery-col-right">
        <div class="gallery-item">
          <img src={images[1]?.src} alt={images[1]?.alt} />
          <span class="item-label">{images[1]?.title || 'Focení'}</span>
        </div>
        <div class="gallery-item large">
          <img src={images[2]?.src} alt={images[2]?.alt} />
          <span class="item-label">{images[2]?.title || 'Rodina'}</span>
        </div>
      </div>
    </div>
    <a href="/akce" class="gallery-more">
      Zobrazit celé portfolio
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M5 12h14M12 5l7 7-7 7"/>
      </svg>
    </a>
  </section>

  <!-- Services - Horizontal scroll feel -->
  <section class="services">
    <div class="services-header">
      <span class="section-num">03</span>
      <h2>Služby</h2>
    </div>
    <div class="services-list">
      <a href="/cenik" class="service-item">
        <span class="service-num">01</span>
        <h3>Portrétní fotografie</h3>
        <p>Osobní i profesionální portréty s důrazem na přirozené světlo.</p>
        <span class="service-arrow">→</span>
      </a>
      <a href="/cenik" class="service-item">
        <span class="service-num">02</span>
        <h3>Rodinné focení</h3>
        <p>Rodinné momenty zachycené v přírodě, plné lásky a radosti.</p>
        <span class="service-arrow">→</span>
      </a>
      <a href="/cenik" class="service-item">
        <span class="service-num">03</span>
        <h3>Párové focení</h3>
        <p>Romantické focení při západu slunce nebo v makovém poli.</p>
        <span class="service-arrow">→</span>
      </a>
      <a href="/cenik" class="service-item">
        <span class="service-num">04</span>
        <h3>Vánoční focení</h3>
        <p>Kouzelná atmosféra zimního focení v přírodě.</p>
        <span class="service-arrow">→</span>
      </a>
    </div>
  </section>

  <!-- Instagram CTA -->
  <section class="instagram">
    <div class="instagram-content">
      <span class="section-num">04</span>
      <h2>Sledujte<br/>@n.i.c.o.l_photography</h2>
      <a href="https://www.instagram.com/n.i.c.o.l_photography/" target="_blank" rel="noopener" class="instagram-link">
        Otevřít Instagram
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M7 17L17 7M17 7H7M17 7V17"/>
        </svg>
      </a>
    </div>
    <div class="instagram-images">
      {#each images.slice(0, 4) as img}
        <img src={img.src} alt={img.alt} />
      {/each}
    </div>
  </section>

  <!-- Contact CTA -->
  <section class="contact-cta">
    <div class="cta-text">
      <h2>Máte projekt<br/>na mysli?</h2>
      <p>Ráda si vyslechnu vaše představy a společně vytvoříme něco krásného.</p>
    </div>
    <a href="/kontakt" class="cta-button">
      <span>Napište mi</span>
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">
        <path d="M5 12h14M12 5l7 7-7 7"/>
      </svg>
    </a>
  </section>

  <Footer />
</div>

<style>
  .editorial-theme {
    --bg: #faf9f7;
    --text: #1a1a1a;
    --text-muted: #666;
    --accent: #c9a87c;
    --border: #e5e5e5;

    background-color: var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
  }

  .section-num {
    font-family: 'Playfair Display', serif;
    font-size: 0.75rem;
    color: var(--text-muted);
    display: block;
    margin-bottom: 1rem;
  }

  /* Hero */
  .hero {
    min-height: 100vh;
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 8rem 4rem 4rem;
    position: relative;
  }

  .hero-text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-right: 4rem;
  }

  .hero-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    color: var(--text-muted);
    margin-bottom: 2rem;
  }

  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 7vw, 6rem);
    font-weight: 400;
    line-height: 1.1;
    margin: 0;
  }

  .hero h1 .line {
    display: block;
  }

  .hero h1 .indent {
    margin-left: 15%;
    font-style: italic;
  }

  .hero-image {
    position: relative;
  }

  .hero-image img {
    width: 100%;
    height: 80vh;
    object-fit: cover;
  }

  .hero-image-caption {
    position: absolute;
    bottom: -2rem;
    right: 0;
    display: flex;
    align-items: center;
    gap: 1rem;
    font-size: 0.75rem;
    color: var(--text-muted);
  }

  .hero-image-caption span {
    font-family: 'Playfair Display', serif;
  }

  .hero-cta {
    position: absolute;
    bottom: 4rem;
    left: 4rem;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    text-decoration: none;
    color: var(--text);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    border-bottom: 1px solid var(--text);
    padding-bottom: 1rem;
  }

  .hero-cta svg {
    margin-top: 0.5rem;
  }

  /* About */
  .about {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    padding: 8rem 4rem;
    border-top: 1px solid var(--border);
  }

  .about-left {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .about-image-1 img {
    width: 80%;
    height: auto;
    object-fit: cover;
  }

  .about-stats {
    display: flex;
    gap: 4rem;
    padding-left: 20%;
  }

  .stat {
    display: flex;
    flex-direction: column;
  }

  .stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
  }

  .stat-label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: var(--text-muted);
  }

  .about-right {
    display: flex;
    flex-direction: column;
    justify-content: center;
    max-width: 500px;
  }

  .about-right h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    margin-bottom: 2rem;
  }

  .about-right .large-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    line-height: 1.4;
    margin-bottom: 1.5rem;
  }

  .about-right p {
    color: var(--text-muted);
    line-height: 1.8;
    margin-bottom: 2rem;
  }

  .text-link {
    color: var(--text);
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    border-bottom: 1px solid var(--text);
    padding-bottom: 0.25rem;
    display: inline-block;
  }

  /* Gallery */
  .gallery {
    padding: 8rem 4rem;
    border-top: 1px solid var(--border);
  }

  .gallery-header {
    margin-bottom: 4rem;
  }

  .gallery-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 400;
    line-height: 1.2;
  }

  .gallery-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }

  .gallery-col-left,
  .gallery-col-right {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .gallery-col-right {
    margin-top: 6rem;
  }

  .gallery-item {
    position: relative;
    overflow: hidden;
  }

  .gallery-item img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    transition: transform 0.6s ease;
  }

  .gallery-item.large img {
    height: 550px;
  }

  .gallery-item:hover img {
    transform: scale(1.05);
  }

  .item-label {
    position: absolute;
    bottom: 1.5rem;
    left: 1.5rem;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: white;
    background: rgba(0,0,0,0.5);
    padding: 0.5rem 1rem;
  }

  .gallery-more {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 4rem;
    color: var(--text);
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    border-bottom: 1px solid var(--text);
    padding-bottom: 0.5rem;
  }

  /* Services */
  .services {
    padding: 8rem 4rem;
    background: white;
  }

  .services-header {
    margin-bottom: 4rem;
  }

  .services-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 0.2em;
  }

  .services-list {
    display: flex;
    flex-direction: column;
  }

  .service-item {
    display: grid;
    grid-template-columns: 80px 250px 1fr 50px;
    align-items: center;
    gap: 2rem;
    padding: 2.5rem 0;
    border-top: 1px solid var(--border);
    text-decoration: none;
    color: var(--text);
    transition: all 0.3s ease;
  }

  .service-item:last-child {
    border-bottom: 1px solid var(--border);
  }

  .service-item:hover {
    padding-left: 1rem;
  }

  .service-num {
    font-family: 'Playfair Display', serif;
    font-size: 0.9rem;
    color: var(--text-muted);
  }

  .service-item h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 400;
  }

  .service-item p {
    color: var(--text-muted);
    font-size: 0.9rem;
  }

  .service-arrow {
    font-size: 1.5rem;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .service-item:hover .service-arrow {
    opacity: 1;
  }

  /* Instagram */
  .instagram {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 4rem;
    padding: 8rem 4rem;
    border-top: 1px solid var(--border);
  }

  .instagram-content h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 400;
    line-height: 1.3;
    margin-bottom: 2rem;
  }

  .instagram-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text);
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    border-bottom: 1px solid var(--text);
    padding-bottom: 0.25rem;
  }

  .instagram-images {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
  }

  .instagram-images img {
    width: 100%;
    aspect-ratio: 1;
    object-fit: cover;
  }

  /* Contact CTA */
  .contact-cta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8rem 4rem;
    background: var(--text);
    color: white;
  }

  .contact-cta h2 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 1rem;
  }

  .contact-cta p {
    color: rgba(255,255,255,0.7);
    max-width: 400px;
  }

  .cta-button {
    display: flex;
    align-items: center;
    gap: 1rem;
    color: white;
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    border: 1px solid white;
    padding: 1.5rem 2.5rem;
    transition: all 0.3s ease;
  }

  .cta-button:hover {
    background: white;
    color: var(--text);
  }

  /* Responsive */
  @media (max-width: 1024px) {
    .service-item {
      grid-template-columns: 60px 1fr 40px;
    }

    .service-item p {
      display: none;
    }
  }

  @media (max-width: 768px) {
    .hero {
      grid-template-columns: 1fr;
      padding: 6rem 2rem 4rem;
    }

    .hero-text {
      padding-right: 0;
      margin-bottom: 2rem;
    }

    .hero-image img {
      height: 50vh;
    }

    .hero-cta {
      position: relative;
      bottom: auto;
      left: auto;
      margin-top: 2rem;
    }

    .about {
      grid-template-columns: 1fr;
      padding: 4rem 2rem;
    }

    .gallery {
      padding: 4rem 2rem;
    }

    .gallery-layout {
      grid-template-columns: 1fr;
    }

    .gallery-col-right {
      margin-top: 0;
    }

    .services {
      padding: 4rem 2rem;
    }

    .instagram {
      grid-template-columns: 1fr;
      padding: 4rem 2rem;
    }

    .instagram-images {
      grid-template-columns: repeat(2, 1fr);
    }

    .contact-cta {
      flex-direction: column;
      gap: 2rem;
      padding: 4rem 2rem;
      text-align: center;
    }
  }
</style>
