<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';

  const faqs = [
    {
      question: "Co když bude pršet nebo špatné počasí?",
      answer: "Pokud v den focení prší nebo je vyloženě nevlídno, bezplatně se domluvíme na náhradním termínu. Zatažená obloha ale naopak vůbec nevadí — měkké rozptýlené světlo vytváří nádherné, přirozené a jemné tóny!"
    },
    {
      question: "Necítím se před objektivem dobře a neumím pózovat, zvládnu to?",
      answer: "Naprosto přirozený pocit, který má 9 z 10 mých klientů před prvním focením! Žádné strnulé pózy u mě nečekejte. Celé focení probíhá formou pohodové procházky v přírodě a přátelského povídání. Přirozeně vás navedu tak, abyste se cítili uvolněně a na fotkách to byli opravdu vy."
    },
    {
      question: "Jak probíhá výběr a kdy dostaneme hotové fotky?",
      answer: "Do několika dnů od focení vám zašlu odkaz na soukromou online náhledovou galerii, kde si v klidu domova naklikáte své favority. Vybrané snímky pečlivě upravím a předám v plném rozlišení pro tisk i sociální sítě do 14 dnů."
    },
    {
      question: "Dostaneme i neupravené RAW snímky?",
      answer: "Neupravené soubory neposkytuji. Výběr nejlepších okamžiků, citlivé tónování barev a retuš tvoří polovinu mého autorského rukopisu. Dostanete ode mě pouze dokončené, perfektně vyladěné fotografie."
    },
    {
      question: "Můžeme vzít s sebou pejska nebo jiné zvířátko?",
      answer: "Jednoznačně ano! Domácí mazlíčci jsou součástí rodiny a focení s nimi je vždy plné energie a spontánnosti. Jen mi to prosím dejte vědět předem, abychom vybrali vhodné a klidné místo."
    },
    {
      question: "Jak probíhá rezervace a platba?",
      answer: "Stačí si vybrat balíček a odeslat poptávku přes formulář nebo mi zavolat. K potvrzení termínu slouží rezervační záloha 500 Kč, která se následně odečítá z celkové ceny focení. Doplatek probíhá po focení nebo při předání galerie."
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
    "mainEntity": faqs.map(f => ({
      "@type": "Question",
      "name": f.question,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": f.answer
      }
    }))
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
    <div class="pricing-grid">
      <!-- Package 1: Klasik -->
      <div class="pricing-card">
        <span class="pricing-type">Portréty, páry i zvířátka</span>
        <h3 class="package-name">Balíček „Klasik“</h3>
        <div class="pricing-duration">1-2 hodiny focení v přírodě</div>

        <div class="pricing-price">
          <span class="price-amount">1 500</span>
          <span class="price-currency">Kč</span>
        </div>

        <ul class="pricing-features">
          <li>
            <span class="check">✓</span>
            10 pečlivě upravených fotografií
          </li>
          <li>
            <span class="check">✓</span>
            Online galerie k pohodlnému výběru
          </li>
          <li>
            <span class="check">✓</span>
            Plné rozlišení pro tisk i web
          </li>
          <li>
            <span class="check">✓</span>
            Dodání do 14 dnů
          </li>
        </ul>

        <div class="deposit-note">
          Rezervační záloha: <strong>500 Kč</strong>
          <span>(odečítá se z celkové ceny)</span>
        </div>

        <a href="/kontakt?balicek=klasik" class="pricing-cta">Objednat Klasik</a>
      </div>

      <!-- Package 2: Rodinný příběh -->
      <div class="pricing-card featured">
        <div class="popular-badge">Nejoblíbenější pro rodiny</div>
        <span class="pricing-type">Rodiny, těhotenské & více vzpomínek</span>
        <h3 class="package-name">Rodinný příběh</h3>
        <div class="pricing-duration">1-2 hodiny bez spěchu</div>

        <div class="pricing-price">
          <span class="price-amount">2 800</span>
          <span class="price-currency">Kč</span>
        </div>

        <ul class="pricing-features">
          <li>
            <span class="check">✓</span>
            <strong>20 upravených fotografií</strong> (dvojnásobek momentek)
          </li>
          <li>
            <span class="check">✓</span>
            <strong>Dárkový tisk 5 fotek (13×18 cm)</strong> zdarma
          </li>
          <li>
            <span class="check">✓</span>
            Online galerie pro celou rodinu
          </li>
          <li>
            <span class="check">✓</span>
            Dostatek času pro děti a pejsky
          </li>
          <li>
            <span class="check">✓</span>
            Dodání do 14 dnů
          </li>
        </ul>

        <div class="deposit-note">
          Rezervační záloha: <strong>500 Kč</strong>
          <span>(odečítá se z celkové ceny)</span>
        </div>

        <a href="/kontakt?balicek=rodinny" class="pricing-cta featured-cta">Objednat Rodinný příběh</a>
      </div>
    </div>

    <!-- Extra + Gift Voucher Row -->
    <div class="pricing-bottom-row">
      <!-- Gift Voucher Card -->
      <div class="voucher-card">
        <div class="voucher-icon">🎁</div>
        <div class="voucher-content">
          <h3>Dárkový poukaz na focení</h3>
          <p>Potěšte své blízké originálním dárkem k narozeninám, výročí nebo pod stromeček. Poukaz lze vystavit na libovolný balíček nebo hodnotu s platností 1 rok.</p>
          <div class="voucher-options">
            <span>✓ Tištěný na prémiovém papíře s mašlí</span>
            <span>✓ Expresní PDF e-mailem do 24 hodin</span>
          </div>
        </div>
        <a href="/kontakt?balicek=poukaz" class="btn voucher-btn">Objednat poukaz</a>
      </div>

      <!-- Extra Photos -->
      <div class="extra-card">
        <span class="extra-label">Doplňkové fotky</span>
        <div class="extra-price">
          <span class="extra-amount">200</span>
          <span class="extra-currency">Kč / fotka</span>
        </div>
        <p>Každá další upravená fotografie nad rámec zvoleného balíčku</p>
      </div>
    </div>

    <!-- Guide Teaser Banner -->
    <div class="guide-teaser">
      <div class="guide-teaser-text">
        <h4>Váháte, co si vzít na sebe nebo jak to u nás probíhá?</h4>
        <p>Připravila jsem pro vás přehledného průvodce s doporučenými barvami, zlatou hodinkou a tipy pro focení s dětmi.</p>
      </div>
      <a href="/pruvodce" class="btn btn-outline guide-teaser-btn">Přečíst Průvodce focením →</a>
    </div>
  </section>

  <!-- What's included -->
  <section class="included">
    <div class="included-header">
      <span class="label">Co je v ceně</span>
      <h2>Jak to celé funguje</h2>
    </div>
    <div class="included-grid">
      <div class="included-item">
        <h3>Domluva</h3>
        <p>Napíšete mi, probereme termín, místo a co chcete fotit. Poradím i s oblečením.</p>
      </div>
      <div class="included-item">
        <h3>Focení</h3>
        <p>1-2 hodiny venku v přírodě. Bez stresu, v klidu.</p>
      </div>
      <div class="included-item">
        <h3>Výběr</h3>
        <p>Pošlu vám online galerii, ze které si vyberete fotky k úpravě.</p>
      </div>
      <div class="included-item">
        <h3>Hotové fotky</h3>
        <p>Vybrané fotky upravím a pošlu vám je v plném rozlišení. Do 14 dnů.</p>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="faq">
    <div class="faq-header">
      <span class="label">Odpovědi na vaše otázky</span>
      <h2>Časté dotazy před focením</h2>
      <p class="faq-sub">Vše, co potřebujete vědět o průběhu, počasí i předání fotografií.</p>
    </div>
    <div class="faq-accordion">
      {#each faqs as faq, i}
        <details class="faq-item" open={i === 0}>
          <summary class="faq-summary">
            <span class="faq-question-text">{faq.question}</span>
            <span class="faq-icon" aria-hidden="true"></span>
          </summary>
          <div class="faq-content">
            <p>{faq.answer}</p>
          </div>
        </details>
      {/each}
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

  /* Pricing */
  .pricing {
    padding: 6rem 2rem;
    max-width: 1100px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3.5rem;
  }

  .pricing-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2.5rem;
    width: 100%;
    align-items: stretch;
  }

  .pricing-card {
    background: var(--bg-secondary);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 3.5rem 2.5rem 3rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    transition: transform 0.3s ease, border-color 0.3s ease;
  }

  .pricing-card:hover {
    border-color: var(--accent);
    transform: translateY(-4px);
  }

  .pricing-card.featured {
    border: 2px solid var(--accent);
    background: linear-gradient(180deg, #161616 0%, #111111 100%);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
  }

  .popular-badge {
    position: absolute;
    top: -14px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--accent);
    color: var(--bg);
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    padding: 0.35rem 1.25rem;
    border-radius: 9999px;
    white-space: nowrap;
  }

  .package-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.85rem;
    color: #ffffff;
    margin: 0 0 0.5rem;
  }

  .pricing-type {
    display: block;
    color: var(--text-muted);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.75rem;
  }

  .pricing-duration {
    font-size: 0.95rem;
    color: var(--accent);
    letter-spacing: 0.05em;
    margin-bottom: 1.5rem;
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
    font-size: 1.35rem;
    color: var(--text-muted);
    margin-left: 0.35rem;
  }

  .pricing-features {
    list-style: none;
    padding: 0;
    margin: 0 0 2rem 0;
    text-align: left;
    flex: 1;
  }

  .pricing-features li {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    padding: 0.85rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    color: var(--text);
    font-size: 0.95rem;
    line-height: 1.4;
  }

  .pricing-features li:last-child {
    border-bottom: none;
  }

  .check {
    color: var(--accent);
    font-size: 1.1rem;
    flex-shrink: 0;
  }

  .deposit-note {
    margin-bottom: 2rem;
    padding: 0.85rem 1.25rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(201, 168, 124, 0.06);
    font-size: 0.88rem;
    color: var(--text);
    border-radius: 4px;
  }

  .deposit-note strong {
    color: var(--accent);
  }

  .deposit-note span {
    display: inline-block;
    color: var(--text-muted);
    font-size: 0.8rem;
    margin-left: 0.35rem;
  }

  .pricing-cta {
    display: block;
    width: 100%;
    padding: 0.95rem 1.5rem;
    background: transparent;
    color: #ffffff;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 9999px;
    text-decoration: none;
    font-size: 0.88rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    transition: all 0.3s ease;
  }

  .pricing-cta:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: #ffffff;
    color: #ffffff;
  }

  .pricing-cta.featured-cta {
    background: var(--accent);
    color: var(--bg);
    border-color: var(--accent);
    box-shadow: 0 4px 15px rgba(201, 168, 124, 0.3);
  }

  .pricing-cta.featured-cta:hover {
    background: #dfc299;
    border-color: #dfc299;
    color: var(--bg);
  }

  /* Bottom Row: Voucher + Extra */
  .pricing-bottom-row {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 2rem;
    width: 100%;
  }

  .voucher-card {
    background: var(--bg-secondary);
    border: 1px solid rgba(201, 168, 124, 0.25);
    border-radius: 8px;
    padding: 2.25rem 2.5rem;
    display: flex;
    align-items: center;
    gap: 2rem;
  }

  .voucher-icon {
    font-size: 3rem;
    flex-shrink: 0;
  }

  .voucher-content {
    flex: 1;
  }

  .voucher-content h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    margin: 0 0 0.5rem;
    color: #ffffff;
  }

  .voucher-content p {
    color: var(--text-muted);
    font-size: 0.9rem;
    line-height: 1.5;
    margin: 0 0 1rem;
  }

  .voucher-options {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    font-size: 0.82rem;
    color: var(--accent);
  }

  .voucher-btn {
    flex-shrink: 0;
    white-space: nowrap;
  }

  .extra-card {
    background: var(--bg-secondary);
    padding: 2.25rem 2rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  /* Guide Teaser Banner */
  .guide-teaser {
    width: 100%;
    background: linear-gradient(135deg, rgba(201, 168, 124, 0.12) 0%, rgba(20, 20, 20, 0.95) 100%);
    border: 1px solid rgba(201, 168, 124, 0.3);
    border-radius: 8px;
    padding: 2.5rem 3rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
  }

  .guide-teaser-text h4 {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    color: #ffffff;
    margin: 0 0 0.5rem;
  }

  .guide-teaser-text p {
    color: var(--text-muted);
    font-size: 0.95rem;
    margin: 0;
    line-height: 1.5;
  }

  .guide-teaser-btn {
    flex-shrink: 0;
    white-space: nowrap;
    border-color: var(--accent);
    color: var(--accent);
  }

  .guide-teaser-btn:hover {
    background: var(--accent);
    color: var(--bg);
  }

  @media (max-width: 900px) {
    .pricing-grid {
      grid-template-columns: 1fr;
    }

    .pricing-bottom-row {
      grid-template-columns: 1fr;
    }

    .voucher-card {
      flex-direction: column;
      text-align: center;
    }

    .voucher-options {
      justify-content: center;
    }

    .guide-teaser {
      flex-direction: column;
      text-align: center;
      padding: 2rem 1.5rem;
    }
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
    margin-bottom: 0.75rem;
  }

  .faq-sub {
    color: var(--text-muted);
    font-size: 1.05rem;
  }

  .faq-accordion {
    max-width: 860px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .faq-item {
    background: var(--bg-secondary);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    overflow: hidden;
    transition: border-color 0.25s ease, background-color 0.25s ease;
  }

  .faq-item[open] {
    border-color: rgba(201, 168, 124, 0.4);
    background: #161616;
  }

  .faq-summary {
    list-style: none;
    padding: 1.35rem 1.75rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.5rem;
    user-select: none;
    transition: background-color 0.2s ease;
  }

  .faq-summary::-webkit-details-marker {
    display: none;
  }

  .faq-summary:hover {
    background-color: rgba(255, 255, 255, 0.02);
  }

  .faq-question-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 500;
    color: var(--text);
    text-align: left;
  }

  .faq-icon {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
    position: relative;
    display: inline-block;
  }

  .faq-icon::before,
  .faq-icon::after {
    content: '';
    position: absolute;
    background-color: var(--accent);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    transition: transform 0.25s ease, opacity 0.25s ease;
  }

  .faq-icon::before {
    width: 14px;
    height: 2px;
  }

  .faq-icon::after {
    width: 2px;
    height: 14px;
  }

  .faq-item[open] .faq-icon::after {
    transform: translate(-50%, -50%) rotate(90deg);
    opacity: 0;
  }

  .faq-content {
    padding: 0 1.75rem 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
  }

  .faq-content p {
    color: #b8b8b8;
    font-size: 0.95rem;
    line-height: 1.75;
    margin: 1rem 0 0;
    text-align: left;
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

    .faq-summary {
      padding: 1.15rem 1.25rem;
    }

    .faq-content {
      padding: 0 1.25rem 1.25rem;
    }

    .cta {
      padding: 4rem 1.5rem;
    }
  }
</style>
