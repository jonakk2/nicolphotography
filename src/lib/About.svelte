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
        <div class="image-decoration"></div>
      </div>
      <div class="about-text">
        <span class="section-label">O mně</span>
        <h2>Nicol Juráňová</h2>
        <p>Dobrý den, vítejte na mém webu. Mé jméno je Nicol Juráňová a focením se zabývám již pár let. Nejčastěji fotím rodinné, párové nebo portrétové fotografie s pozadím, které vytvořila sama příroda. Pokud ale máte v hlavě i jiný nápad na focení, sem s ním!</p>
        <p>Jsem zastáncem spíše spontánních fotek, hlavně když jde o focení s dětmi, nemusíte se ale bát, během focení své klienty instruuji a zakládám si na přátelské a uvolněné atmosféře.</p>
        <p>V případě zájmu se mi ozvěte a společně se dohodneme na termínu. Budu se těšit!</p>
      </div>
    </div>
  </div>
</section>

<!-- Philosophy Section -->
<section class="philosophy-section">
  <div class="container">
    <div class="philosophy-grid">
      <div class="philosophy-card">
        <span class="philosophy-number">01</span>
        <h3>Autenticita</h3>
        <p>Věřím, že nejkrásnější fotografie jsou ty přirozené. Nesnažím se vytvářet umělé pózy, ale zachycuji skutečné emoce a momenty.</p>
      </div>
      <div class="philosophy-card">
        <span class="philosophy-number">02</span>
        <h3>Příběh</h3>
        <p>Každá fotografie má svůj příběh. Mým cílem je tento příběh najít a předat ho tak, aby vám přinášel radost i po letech.</p>
      </div>
      <div class="philosophy-card">
        <span class="philosophy-number">03</span>
        <h3>Pohodlí</h3>
        <p>Chci, abyste se při focení cítili přirozeně a uvolněně. Vytváříme společně atmosféru, ve které můžete být sami sebou.</p>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta-section">
  <div class="container">
    <h2>Pojďme vytvořit něco krásného</h2>
    <p>Ráda se s vámi sejdu a probereme vaše představy</p>
    <a href="/kontakt" class="btn btn-light">Kontaktovat</a>
  </div>
</section>

<Footer />

<style>
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
    padding: 6rem 0;
    background-color: white;
  }

  .about-intro {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
  }

  .about-image-wrapper {
    position: relative;
  }

  .about-main-image {
    width: 100%;
    height: 500px;
    object-fit: cover;
    border-radius: 8px;
    position: relative;
    z-index: 1;
  }

  .image-decoration {
    position: absolute;
    top: 20px;
    left: 20px;
    right: -20px;
    bottom: -20px;
    border: 3px solid var(--color-secondary);
    border-radius: 8px;
    z-index: 0;
  }

  .section-label {
    display: inline-block;
    color: var(--color-secondary);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    font-weight: 600;
    margin-bottom: 0.5rem;
  }

  .about-text h2 {
    margin-bottom: 1.5rem;
  }

  .about-text p {
    color: var(--color-muted);
    margin-bottom: 1rem;
    line-height: 1.8;
  }

  /* Philosophy */
  .philosophy-section {
    padding: 6rem 0;
    background-color: var(--color-light);
  }

  .philosophy-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
  }

  .philosophy-card {
    background: white;
    padding: 2.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  }

  .philosophy-number {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 700;
    color: var(--color-secondary);
    opacity: 0.3;
    display: block;
    margin-bottom: 1rem;
  }

  .philosophy-card h3 {
    margin-bottom: 1rem;
    font-size: 1.5rem;
  }

  .philosophy-card p {
    color: var(--color-muted);
    line-height: 1.7;
  }

  /* CTA */
  .cta-section {
    padding: 6rem 0;
    background: linear-gradient(135deg, var(--color-primary) 0%, #1a252f 100%);
    text-align: center;
    color: white;
  }

  .cta-section h2 {
    color: white;
    margin-bottom: 1rem;
  }

  .cta-section p {
    opacity: 0.9;
    margin-bottom: 2rem;
    font-size: 1.1rem;
  }

  .btn-light {
    background-color: white;
    border-color: white;
    color: var(--color-primary);
  }

  .btn-light:hover {
    background-color: transparent;
    color: white;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .about-intro {
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    .about-text {
      padding-left: 0;
    }

    .about-main-image {
      height: 350px;
    }

    .image-decoration {
      display: none;
    }
  }
</style>
