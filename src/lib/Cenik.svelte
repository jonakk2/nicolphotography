<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';

  const faqs = [
    {
      question: "Jak dlouho trvá dodání fotografií?",
      answer: "Standardní doba dodání je do 14 dnů od focení."
    },
    {
      question: "Mohu si vybrat místo focení?",
      answer: "Samozřejmě! Ráda se přizpůsobím vašim představám. Nejčastěji fotíme v přírodě v okolí Olomouckého kraje."
    },
    {
      question: "Co když bude špatné počasí?",
      answer: "V případě nepříznivého počasí můžeme termín přesunout na jiný den."
    },
    {
      question: "Jak probíhá rezervace?",
      answer: "Stačí mě kontaktovat přes formulář nebo telefonicky. Domluvíme si termín a místo focení."
    }
  ];
</script>

<svelte:head>
  <title>Ceník focení | Nicol Juráňová photography</title>
  <meta name="description" content="Ceník focení v přírodě - portréty, páry, rodiny i focení se zvířátky. 1-2 hodiny focení od 1 500 Kč. Nicol Juráňová, Olomoucký kraj." />
  <link rel="canonical" href="https://nicolphotography.cz/cenik" />
  <meta property="og:title" content="Ceník focení | Nicol Juráňová photography" />
  <meta property="og:description" content="Focení v přírodě od 1 500 Kč. Portréty, páry, rodiny i focení se zvířátky. Olomoucký kraj." />
  <meta property="og:url" content="https://nicolphotography.cz/cenik" />
  <meta property="og:image" content="https://nicolphotography.cz/hlavicka.png" />
  <meta property="og:type" content="website" />
  {@html `<script type="application/ld+json">${JSON.stringify({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Jak dlouho trvá dodání fotografií?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Standardní doba dodání je do 14 dnů od focení."
        }
      },
      {
        "@type": "Question",
        "name": "Mohu si vybrat místo focení?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Samozřejmě! Ráda se přizpůsobím vašim představám. Nejčastěji fotíme v přírodě v okolí Olomouckého kraje."
        }
      },
      {
        "@type": "Question",
        "name": "Co když bude špatné počasí?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "V případě nepříznivého počasí můžeme termín přesunout na jiný den."
        }
      },
      {
        "@type": "Question",
        "name": "Jak probíhá rezervace?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Stačí mě kontaktovat přes formulář nebo telefonicky. Domluvíme si termín a místo focení."
        }
      }
    ]
  })}</script>`}
</svelte:head>

<div class="cenik-page">
  <NavBar />

  <!-- Hero -->
  <section class="page-header">
    <div class="page-header-overlay"></div>
    <div class="page-header-content">
      <h1>Focení v přírodě</h1>
      <p>Jednoduchý a transparentní ceník</p>
    </div>
  </section>

  <!-- Pricing -->
  <section class="pricing">
    <div class="pricing-card">
      <span class="pricing-type">Portréty, páry, rodiny i focení se zvířátky</span>

      <div class="pricing-duration">1-2 hodiny focení</div>

      <div class="pricing-price">
        <span class="price-amount">1 500</span>
        <span class="price-currency">Kč</span>
      </div>

      <ul class="pricing-features">
        <li>
          <span class="check">✓</span>
          10 upravených fotografií
        </li>
        <li>
          <span class="check">✓</span>
          Online galerie k výběru
        </li>
        <li>
          <span class="check">✓</span>
          Dodání do 14 dnů
        </li>
        <li>
          <span class="check">✓</span>
          Focení v přírodě
        </li>
      </ul>

      <a href="/kontakt" class="pricing-cta">Mám zájem</a>
    </div>

    <div class="pricing-extra">
      <div class="extra-card">
        <span class="extra-label">Další fotky</span>
        <div class="extra-price">
          <span class="extra-amount">200</span>
          <span class="extra-currency">Kč / fotka</span>
        </div>
        <p>Každá další upravená fotografie nad 10 kusů</p>
      </div>
    </div>
  </section>

  <!-- What's included -->
  <section class="included">
    <div class="included-header">
      <span class="label">Co je v ceně</span>
      <h2>Vše, co potřebujete</h2>
    </div>
    <div class="included-grid">
      <div class="included-item">
        <span class="included-number">01</span>
        <h3>Konzultace</h3>
        <p>Společně probereme vaše představy, místo a termín focení.</p>
      </div>
      <div class="included-item">
        <span class="included-number">02</span>
        <h3>Focení</h3>
        <p>1-2 hodiny focení v přírodě, uvolněná a přátelská atmosféra.</p>
      </div>
      <div class="included-item">
        <span class="included-number">03</span>
        <h3>Úpravy</h3>
        <p>Pečlivá úprava barev a retuše vybraných fotografií.</p>
      </div>
      <div class="included-item">
        <span class="included-number">04</span>
        <h3>Galerie</h3>
        <p>Online galerie pro snadné stažení a sdílení fotografií.</p>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="faq">
    <div class="faq-header">
      <span class="label">FAQ</span>
      <h2>Časté otázky</h2>
    </div>
    <div class="faq-grid">
      {#each faqs as faq}
        <div class="faq-item">
          <h3>{faq.question}</h3>
          <p>{faq.answer}</p>
        </div>
      {/each}
    </div>
  </section>

  <!-- CTA -->
  <section class="cta">
    <h2>Máte zájem o focení?</h2>
    <p>Napište mi a domluvíme se na termínu.</p>
    <a href="/kontakt" class="cta-btn">Kontaktovat</a>
  </section>

  <Footer />
</div>

<style>
  .cenik-page {
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

  /* Pricing */
  .pricing {
    padding: 6rem 4rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3rem;
  }

  .pricing-card {
    background: var(--bg-secondary);
    border: 1px solid var(--accent);
    padding: 3rem 4rem;
    text-align: center;
    max-width: 500px;
    width: 100%;
  }

  .pricing-type {
    display: block;
    color: var(--text-muted);
    font-size: 0.9rem;
    margin-bottom: 2rem;
  }

  .pricing-duration {
    font-size: 1.2rem;
    color: var(--text);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 1rem;
  }

  .pricing-price {
    margin-bottom: 2.5rem;
  }

  .price-amount {
    font-family: 'Playfair Display', serif;
    font-size: 5rem;
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
    margin: 0 0 2.5rem 0;
    text-align: left;
  }

  .pricing-features li {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 0;
    border-bottom: 1px solid #222;
    color: var(--text);
    font-size: 1rem;
  }

  .pricing-features li:last-child {
    border-bottom: none;
  }

  .check {
    color: var(--accent);
    font-size: 1.2rem;
  }

  .pricing-cta {
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

  .pricing-cta:hover {
    background: var(--text);
  }

  .pricing-extra {
    text-align: center;
  }

  .extra-card {
    background: var(--bg-secondary);
    padding: 2rem 3rem;
    border: 1px solid #222;
  }

  .extra-label {
    display: block;
    color: var(--text-muted);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 1rem;
  }

  .extra-price {
    margin-bottom: 0.5rem;
  }

  .extra-amount {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    color: var(--accent);
  }

  .extra-currency {
    font-size: 1rem;
    color: var(--text-muted);
    margin-left: 0.5rem;
  }

  .extra-card p {
    color: var(--text-muted);
    font-size: 0.9rem;
  }

  /* Included */
  .included {
    padding: 6rem 4rem;
    background: var(--bg-secondary);
  }

  .included-header {
    text-align: center;
    margin-bottom: 4rem;
  }

  .included-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 400;
  }

  .included-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .included-item {
    padding: 2rem;
    border: 1px solid #222;
  }

  .included-number {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    color: var(--accent);
    opacity: 0.5;
    display: block;
    margin-bottom: 1rem;
  }

  .included-item h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    font-weight: 400;
    margin-bottom: 0.75rem;
  }

  .included-item p {
    color: var(--text-muted);
    font-size: 0.9rem;
    line-height: 1.7;
  }

  /* FAQ */
  .faq {
    padding: 6rem 4rem;
  }

  .faq-header {
    text-align: center;
    margin-bottom: 4rem;
  }

  .faq-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 400;
  }

  .faq-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
    max-width: 1000px;
    margin: 0 auto;
  }

  .faq-item {
    padding: 2rem;
    background: var(--bg-secondary);
    border: 1px solid #222;
  }

  .faq-item h3 {
    font-size: 1.1rem;
    font-weight: 500;
    margin-bottom: 1rem;
    color: var(--text);
  }

  .faq-item p {
    color: var(--text-muted);
    font-size: 0.95rem;
    line-height: 1.7;
  }

  /* CTA */
  .cta {
    padding: 6rem 4rem;
    text-align: center;
    background: var(--bg-secondary);
  }

  .cta h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 400;
    margin-bottom: 1rem;
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
  @media (max-width: 1024px) {
    .included-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 768px) {
    .pricing {
      padding: 4rem 1.5rem;
    }

    .pricing-card {
      padding: 2rem;
    }

    .price-amount {
      font-size: 4rem;
    }

    .included {
      padding: 4rem 1.5rem;
    }

    .included-grid {
      grid-template-columns: 1fr;
    }

    .faq {
      padding: 4rem 1.5rem;
    }

    .faq-grid {
      grid-template-columns: 1fr;
    }

    .cta {
      padding: 4rem 1.5rem;
    }
  }
</style>
