<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
  import HeroSlider from './HeroSlider.svelte';
</script>

<svelte:head>
  <title>O mně | Nicol Juráňová – Fotografka Hranice na Moravě & Olomoucký kraj</title>
  <meta name="description" content="Seznamte se s Nicol Juráňovou – fotografkou z Hranic na Moravě. Portrétní, rodinné a párové focení v přírodě s důrazem na spontánnost a přátelskou atmosféru." />
  <meta name="keywords" content="Nicol Juráňová fotografka, fotografka Hranice na Moravě, fotograf Olomoucký kraj, o mně Nicol Juráňová" />
  <link rel="canonical" href="https://nicolphotography.cz/about" />
  <meta property="og:title" content="O mně | Nicol Juráňová photography" />
  <meta property="og:description" content="Fotografka z Hranic na Moravě. Portrétní, rodinné a párové focení v přírodě v přátelské atmosféře." />
  <meta property="og:url" content="https://nicolphotography.cz/about" />
  <meta property="og:image" content="https://nicolphotography.cz/og-image.jpg" />
  <meta property="og:type" content="profile" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="O mně | Nicol Juráňová photography" />
  <meta name="twitter:description" content="Fotografka z Hranic na Moravě a Olomouckého kraje." />
  <meta name="twitter:image" content="https://nicolphotography.cz/og-image.jpg" />
</svelte:head>

<div class="about-page">
  <NavBar />

  <!-- Page Header -->
  <section class="page-header" aria-label="O mně - Nicol Juráňová">
    <HeroSlider />
    <div class="page-header-overlay" aria-hidden="true"></div>
    <div class="page-header-content">
      <h1>O mně</h1>
      <p>Poznejte příběh za objektivem</p>
    </div>
  </section>

  <!-- About Content -->
  <section class="about-content">
    <div class="container">
      <div class="about-intro">
        <div class="about-image-wrapper">
          <img src="/images/portfolio/about/IMG_3078-2.webp" alt="Nicol Juráňová - fotografka" class="about-main-image" loading="lazy" />
        </div>
        <div class="about-text">
          <span class="label">O mně</span>
          <h2>Nicol Juráňová</h2>
          <p>Mé jméno je Nicol a focení je má vášeň už pár let. Nejčastěji fotím rodiny, páry a portréty, ale neváhejte mě kontaktovat s jakýmkoliv nápadem! Působím v okolí Hranic na Moravě, ale ráda za vámi přijedu kamkoliv, kde vás srdce táhne.</p>
          <p>Zajímá vás, jak se na focení připravit, nebo chcete rovnou domluvit termín?</p>
          <div class="about-actions">
            <a href="/pruvodce" class="about-link-btn secondary">Průvodce přípravou →</a>
            <a href="/cenik" class="about-link-btn primary">Prohlédnout ceník</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Philosophy Section -->
  <section class="philosophy-section">
    <div class="container">
      <div class="philosophy-header">
        <span class="label">Jak to probíhá</span>
        <h2>Od domluvy k fotkám</h2>
      </div>
      <div class="philosophy-grid">
        <div class="philosophy-card">
          <h3>Napíšete mi</h3>
          <p>Domluvíme se na termínu, místě a typu focení. Poradím vám, co na sebe a kde to vypadá nejlíp.</p>
        </div>
        <div class="philosophy-card">
          <h3>Fotíme 1-2 hodiny</h3>
          <p>V klidu, bez stresu. Řeknu vám co dělat, ale nechám prostor i spontánním momentům — ty jsou pak nejlepší.</p>
        </div>
        <div class="philosophy-card">
          <h3>Fotky do 14 dnů</h3>
          <p>Pošlu vám galerii, vyberete si a já vybrané fotky upravím. Hotovo.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta">
    <h2>Chcete se objednat?</h2>
    <p>Napište mi, domluvíme termín a místo.</p>
    <a href="/kontakt" class="cta-btn">Kontaktovat</a>
  </section>

  <Footer />
</div>

<style>
  .about-page {
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

  /* About Content */
  .about-content {
    padding: 6rem 4rem;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .about-intro {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
  }

  .about-main-image {
    width: 100%;
    height: 500px;
    object-fit: cover;
  }

  .about-text h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 400;
    margin-bottom: 1.5rem;
    color: var(--text);
  }

  .about-text p {
    color: var(--text-muted);
    margin-bottom: 1rem;
    line-height: 1.8;
    font-size: 0.95rem;
  }

  .about-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 2rem;
  }

  .about-link-btn {
    display: inline-block;
    padding: 0.85rem 1.75rem;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    text-decoration: none;
    transition: all 0.3s ease;
    border-radius: 2px;
  }

  .about-link-btn.primary {
    background: var(--accent);
    color: var(--bg);
  }

  .about-link-btn.primary:hover {
    background: var(--text);
  }

  .about-link-btn.secondary {
    background: transparent;
    color: var(--accent);
    border: 1px solid var(--accent);
  }

  .about-link-btn.secondary:hover {
    background: var(--accent);
    color: var(--bg);
  }

  /* Philosophy */
  .philosophy-section {
    padding: 6rem 4rem;
    background: var(--bg-secondary);
  }

  .philosophy-header {
    text-align: center;
    margin-bottom: 4rem;
  }

  .philosophy-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 400;
    color: var(--text);
  }

  .philosophy-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .philosophy-card {
    padding: 2rem;
    border: 1px solid #222;
  }

  .philosophy-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    font-weight: 400;
    margin-bottom: 0.75rem;
    color: var(--text);
  }

  .philosophy-card p {
    color: var(--text-muted);
    font-size: 0.9rem;
    line-height: 1.7;
  }

  /* CTA */
  .cta {
    padding: 6rem 4rem;
    text-align: center;
    background: var(--bg-secondary);
    border-top: 1px solid #222;
  }

  .cta h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 400;
    margin-bottom: 1rem;
    color: var(--text);
  }

  .cta p {
    color: var(--text-muted);
    font-size: 1.1rem;
    margin-bottom: 2rem;
  }

  .cta-btn {
    display: inline-block;
    padding: 1rem 3rem;
    background: var(--accent);
    color: var(--bg);
    text-decoration: none;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    transition: all 0.3s ease;
  }

  .cta-btn:hover {
    background: var(--text);
  }

  /* Responsive */
  @media (max-width: 768px) {
    .about-content {
      padding: 4rem 1.5rem;
    }

    .about-intro {
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    .about-main-image {
      height: 350px;
    }

    .philosophy-section {
      padding: 4rem 1.5rem;
    }

    .philosophy-grid {
      grid-template-columns: 1fr;
    }

    .cta {
      padding: 4rem 1.5rem;
    }
  }
</style>
