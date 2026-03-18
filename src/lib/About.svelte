<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
</script>

<svelte:head>
  <title>O mně | Nicol Juráňová photography</title>
  <meta name="description" content="Seznamte se s Nicol Juráňovou - fotografkou z Olomouckého kraje. Portrétní, rodinné a párové focení v přírodě s důrazem na spontánnost a přátelskou atmosféru." />
  <link rel="canonical" href="https://nicolphotography.cz/about" />
  <meta property="og:title" content="O mně | Nicol Juráňová photography" />
  <meta property="og:description" content="Seznamte se s Nicol Juráňovou - fotografkou z Olomouckého kraje. Portrétní, rodinné a párové focení v přírodě." />
  <meta property="og:url" content="https://nicolphotography.cz/about" />
  <meta property="og:image" content="https://nicolphotography.cz/hlavicka.png" />
  <meta property="og:type" content="website" />
</svelte:head>

<div class="about-page">
  <NavBar />

  <!-- Page Header -->
  <section class="page-header">
    <div class="page-header-overlay"></div>
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
          <p>Jmenuju se Nicol a fotím lidi v přírodě. Rodinné focení, párové, portréty — nejčastěji někde venku v okolí Hranic na Moravě. Ale pokud máte vlastní nápad, klidně sem s ním.</p>
          <p>Při focení s dětmi hodně improvizuju — nejlepší fotky vznikají spontánně. U dospělých vás navádím, ale žádné strnulé pózy nečekejte. Chci, abyste na fotkách vypadali jako vy.</p>
          <p>Pokud máte zájem, ozvěte se a domluvíme termín.</p>
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
