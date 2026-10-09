<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
  import HeroSlider from './HeroSlider.svelte';

  const colorPalette = [
    { name: 'Přírodní béžová', hex: '#d9cdb8', desc: 'Svetry, plátěné kalhoty, šaty' },
    { name: 'Teplá krémová', hex: '#ede6d8', desc: 'Základní trika, košile, halenky' },
    { name: 'Karamel & Hnědá', hex: '#9d6b41', desc: 'Kožené doplňky, boty, kabáty' },
    { name: 'Olivová & Šalvěj', hex: '#727d65', desc: 'Skvěle ladí s trávou a lesem' },
    { name: 'Zemitá terakota', hex: '#a65b44', desc: 'Jemný teplý akcent pro fotky' },
    { name: 'Tlumená džínovina', hex: '#586b7a', desc: 'Klasické džíny bez děr a nápisů' }
  ];

  const steps = [
    {
      step: '01',
      title: 'Pohodlí je na prvním místě',
      text: 'Oblečte se tak, abyste se cítili přirozeně a sebevědomě. Pokud vás bude někde škrtit sukně nebo kousat svetr, bude to na fotkách vidět v mimice.'
    },
    {
      step: '02',
      title: 'Slaďte se, ale nekopírujte',
      text: 'Nemusíte mít všichni stejná bílá trička a modré džíny. Mnohem hezčí je vybrat 2 až 3 tóny ze zemitých barev a ty mezi členy rodiny či páru prostřídat.'
    },
    {
      step: '03',
      title: 'Pozor na velká loga a neony',
      text: 'Křiklavé barvy (neonová růžová, svítivě žlutá) vrhají na obličej barevné odlesky. Velké nápisy a loga na tričkách zase strhávají pozornost od vašich tváří.'
    },
    {
      step: '04',
      title: 'Vrstvy a textury dělají divy',
      text: 'Klobouk, pletený cardigan, šátek, rozepnutá lněná košile. Vrstvení dodává fotkám hloubku a navíc umožňuje během chvilky změnit vzhled bez zdlouhavého převlékání.'
    }
  ];

  const faqs = [
    {
      question: "Co když bude pršet nebo špatné počasí?",
      answer: "Pokud v den focení prší nebo je vyloženě nevlídno, bezplatně se domluvíme na náhradním termínu. Zatažená obloha ale naopak vůbec nevadí — měkké rozptýlené světlo vytváří nádherné, přirozené a jemné tóny!"
    },
    {
      question: "Necítím se před objektivem dobře a neumím pózovat, zvládnu to?",
      answer: "Naprosto přirozený pocit, který má většina klientů před prvním focením! Žádné strnulé pózy u mě nečekejte. Celé focení probíhá formou pohodové procházky v přírodě a přátelského povídání. Přirozeně vás navedu tak, abyste se cítili uvolněně a na fotkách to byli opravdu vy."
    },
    {
      question: "Co když děti nebudou chtít spolupracovat nebo budou unavené?",
      answer: "Děti jsou děti a nikdy po nich nechci, aby hodinu stály na značce a usmívaly se do objektivu. Focení vedeme formou hry, běhání, foukání bublin nebo hledání šišek. Nejkrásnější momenty vznikají právě tehdy, když zapomenou, že je někdo fotí."
    },
    {
      question: "Jak a kdy dostaneme hotové fotografie?",
      answer: "Do několika dnů od focení vám zašlu odkaz na soukromou online galerii s náhledy, kde si v klidu domova naklikáte své oblíbené snímky. Vybrané fotky pečlivě barevně vyladím, jemně vyretušuji a předám v plném rozlišení pro tisk i web do 14 dnů."
    },
    {
      question: "Můžeme vzít s sebou pejska nebo jiné zvířátko?",
      answer: "Jednoznačně ano! Domácí mazlíčci jsou součástí rodiny a focení s nimi je vždy plné radosti a spontánnosti. Jen mi to prosím dejte vědět předem, abychom vybrali vhodné a klidné místo."
    },
    {
      question: "Dostaneme i neupravené RAW snímky?",
      answer: "Neupravené soubory neposkytuji. Výběr nejlepších okamžiků, citlivé tónování barev a retuš tvoří polovinu mého autorského rukopisu. Dostanete ode mě pouze dokončené, perfektně vyladěné fotografie."
    }
  ];
</script>

<svelte:head>
  <title>Jak se připravit na focení | Tipy & Průvodce | Nicol Juráňová</title>
  <meta name="description" content="Kompletní průvodce pro klienty: co si vzít na sebe, jaké barvy vybrat do přírody, jak probíhá focení s dětmi a proč fotíme při zlaté hodince." />
  <meta name="keywords" content="jak se obléct na focení, tipy na rodinné focení, focení v přírodě oblečení, zlatá hodinka focení, Nicol Juráňová tipy" />
  <link rel="canonical" href="https://nicolphotography.cz/pruvodce" />
  <meta property="og:title" content="Jak se připravit na focení | Tipy & Průvodce | Nicol Juráňová" />
  <meta property="og:description" content="Užitečné rady a tipy: co si obléct, jaké barvy ladí v přírodě a jak probíhá focení s dětmi." />
  <meta property="og:url" content="https://nicolphotography.cz/pruvodce" />
  <meta property="og:image" content="https://nicolphotography.cz/og-image.jpg" />
  <meta property="og:type" content="article" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Jak se připravit na focení | Nicol Juráňová" />
  <meta name="twitter:description" content="Užitečné tipy a doporučení pro přirozené focení v přírodě." />
  <meta name="twitter:image" content="https://nicolphotography.cz/og-image.jpg" />
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

<div class="guide-page">
  <NavBar />

  <!-- Hero -->
  <section class="page-header" aria-label="Průvodce focením - Nicol Juráňová">
    <HeroSlider />
    <div class="page-header-overlay" aria-hidden="true"></div>
    <div class="page-header-content">
      <span class="label">Průvodce zážitkem</span>
      <h1>Jak se připravit na focení</h1>
      <p>Všechno, co potřebujete vědět o oblečení, světle a průběhu focení v přírodě — v klidu a bez stresu.</p>
    </div>
  </section>

  <!-- Intro Note -->
  <section class="intro-section">
    <div class="container narrow">
      <div class="quote-box">
        <p class="intro-quote">
          „Nejčastější věta před focením bývá: <em>‚My se vůbec neumíme tvářit a děti určitě nebudou stát v klidu.‘</em> Můžu vás uklidnit — ani jedno po vás nechci. Nejhezčí fotky vznikají, když se soustředíte na sebe navzájem, ne na můj objektiv.“
        </p>
        <span class="quote-author">— Nicol Juráňová</span>
      </div>
    </div>
  </section>

  <!-- Wardrobe & Colors -->
  <section class="wardrobe-section">
    <div class="container">
      <div class="section-heading text-center">
        <span class="label">Co na sebe</span>
        <h2>Barvy, které milují přírodu</h2>
        <p>Pro focení venku nejlépe fungují tlumené, teplé a neutrální tóny. Skvěle splývají s loukami, lesy i zapadajícím sluncem.</p>
      </div>

      <!-- Color Palette Swatches -->
      <div class="palette-grid">
        {#each colorPalette as color}
          <div class="swatch-card">
            <div class="color-circle" style="background-color: {color.hex};"></div>
            <div class="color-info">
              <h4>{color.name}</h4>
              <p>{color.desc}</p>
            </div>
          </div>
        {/each}
      </div>

      <!-- Wardrobe Tips Grid -->
      <div class="tips-grid">
        {#each steps as step}
          <div class="tip-card">
            <span class="step-num">{step.step}</span>
            <h3>{step.title}</h3>
            <p>{step.text}</p>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- Golden Hour & Timing -->
  <section class="golden-hour-section">
    <div class="container">
      <div class="split-layout">
        <div class="split-text">
          <span class="label">Světlo je klíč</span>
          <h2>Kouzlo zlaté hodinky</h2>
          <p>
            Nejraději fotím přibližně <strong>hodinu až hodinu a půl před západem slunce</strong>. Slunce je nízko nad obzorem, nehází ostré stíny pod očima a příroda dostává zlatavý, teplý nádech.
          </p>
          <p>
            <strong>Co když bude zataženo?</strong> Mraky fungují jako obří difuzér — světlo je měkké, jemné a barvy v přírodě působí hluboce a sytě.
          </p>
          <p>
            <strong>A co když bude pršet?</strong> V případě deště nebo silného větru termín bezplatně přesuneme na jiný vyhovující den.
          </p>
        </div>
        <div class="split-image">
          <img src="/images/portfolio/golden-hour.png" alt="Zlatá hodinka focení v přírodě" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <!-- Children & Pets -->
  <section class="kids-pets-section">
    <div class="container">
      <div class="section-heading text-center">
        <span class="label">S dětmi & se zvířátky</span>
        <h2>Focení formou hry</h2>
      </div>

      <div class="guidance-grid">
        <div class="guidance-card">
          <div class="card-icon">👨‍👩‍👧‍👦</div>
          <h3>Jak fotíme s dětmi</h3>
          <p>Děti nebudu nutit sedět a dívat se do kamery. Nechám je běhat, házet kamínky, foukat do pampelišek nebo se tulit k rodičům. Když děti vnímají focení jako procházku, mají na fotkách skutečné jiskry v očích.</p>
          <div class="practical-tip">
            <strong>Doporučení:</strong> Vezměte s sebou oblíbenou drobnou svačinku (křupky, nakrájené jablko — ideálně ne čokoládu, ať nemáme špinavé pusinky).
          </div>
        </div>

        <div class="guidance-card">
          <div class="card-icon">🐾</div>
          <h3>Focení se čtyřnohými parťáky</h3>
          <p>Pejsci jsou plnohodnotní členové rodiny! Před focením je dobré pejska trochu proběhnout, aby se zbavil přebytečné energie. Na místě pak střídáme akční momentky v běhu s klidným mazlením.</p>
          <div class="practical-tip">
            <strong>Doporučení:</strong> Nezapomeňte oblíbené pamlsky a hračku pro upoutání pozornosti do objektivu.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Checklist: What to bring -->
  <section class="checklist-section">
    <div class="container narrow">
      <div class="checklist-box">
        <span class="label">Seznam do batohu</span>
        <h2>Co si vzít s sebou</h2>
        <ul class="checklist-items">
          <li><span>✓</span> Pohodlné boty na přesun (podpatky nebo hezké botky můžete obout až přímo na místě)</li>
          <li><span>✓</span> Vlhčené a papírové kapesníčky</li>
          <li><span>✓</span> Kartáč na vlasy, gumičku a balzám na rty</li>
          <li><span>✓</span> Deka na sezení, pokud chcete fotky v trávě (ráda vezmu i svou stylovou neutrální)</li>
          <li><span>✓</span> Dobrou náladu — o zbytek se postarám já</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="faq-section">
    <div class="container narrow">
      <div class="faq-header text-center">
        <span class="label">Časté otázky</span>
        <h2>Odpovědi na vaše obavy</h2>
        <p class="faq-sub">Vše, na co se mě klienti před prvním focením nejčastěji ptají.</p>
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
    </div>
  </section>

  <!-- CTA Box -->
  <section class="guide-cta">
    <div class="container text-center">
      <h2>Máte představu a chuť fotit?</h2>
      <p>Napište mi nezávaznou zprávu. Společně vybereme ideální místo a čas podle ročního období.</p>
      <div class="cta-buttons">
        <a href="/kontakt" class="btn">Domluvit termín</a>
        <a href="/cenik" class="btn btn-outline">Prohlédnout ceník</a>
      </div>
    </div>
  </section>

  <Footer />
</div>

<style>
  .guide-page {
    --bg: #0a0a0a;
    --bg-secondary: #121212;
    --text: #ffffff;
    --text-muted: #8e8e8e;
    --accent: #c9a87c;
    --accent-hover: #dfc299;

    background-color: var(--bg);
    color: var(--text);
    min-height: 100vh;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }

  .container.narrow {
    max-width: 860px;
  }

  .label {
    color: var(--accent);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    display: block;
    margin-bottom: 0.75rem;
  }

  /* Header */
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
    text-align: center;
    color: white;
  }

  .page-header-overlay {
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, rgba(13, 13, 13, 0.75) 0%, rgba(13, 13, 13, 0.55) 55%, rgba(13, 13, 13, 0.35) 100%);
    pointer-events: none;
    z-index: 1;
  }

  .page-header-content {
    position: relative;
    z-index: 2;
    max-width: 800px;
  }

  .page-header-content h1 {
    font-size: clamp(2.2rem, 5vw, 3.5rem);
    margin-bottom: 1.25rem;
  }

  .page-header-content p {
    font-size: 1.15rem;
    color: rgba(255,255,255,0.8);
    line-height: 1.7;
    margin: 0;
  }

  /* Intro */
  .intro-section {
    padding: 5rem 1.5rem 2rem;
  }

  .quote-box {
    background-color: var(--bg-secondary);
    border-left: 3px solid var(--accent);
    padding: 2.5rem;
    border-radius: 4px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
  }

  .intro-quote {
    font-size: 1.2rem;
    line-height: 1.8;
    color: #e5e5e5;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    margin: 0 0 1rem;
  }

  .quote-author {
    color: var(--accent);
    font-size: 0.9rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }

  /* Wardrobe Section */
  .wardrobe-section {
    padding: 5rem 0;
  }

  .section-heading h2 {
    font-size: clamp(1.8rem, 4vw, 2.75rem);
    margin-bottom: 1rem;
  }

  .section-heading p {
    color: var(--text-muted);
    max-width: 600px;
    margin: 0 auto 3.5rem;
    font-size: 1rem;
    line-height: 1.6;
  }

  .palette-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1.5rem;
    margin-bottom: 4rem;
  }

  .swatch-card {
    background-color: var(--bg-secondary);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 8px;
    padding: 1.5rem 1rem;
    text-align: center;
    transition: transform 0.25s ease, border-color 0.25s ease;
  }

  .swatch-card:hover {
    transform: translateY(-4px);
    border-color: var(--accent);
  }

  .color-circle {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    margin: 0 auto 1.25rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    border: 2px solid rgba(255,255,255,0.1);
  }

  .color-info h4 {
    font-size: 0.95rem;
    margin-bottom: 0.4rem;
    color: #ffffff;
  }

  .color-info p {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin: 0;
    line-height: 1.4;
  }

  .tips-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
  }

  .tip-card {
    background-color: var(--bg-secondary);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 8px;
    padding: 2.25rem 2rem;
    position: relative;
  }

  .step-num {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    color: var(--accent);
    opacity: 0.6;
    display: block;
    margin-bottom: 0.75rem;
  }

  .tip-card h3 {
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
    color: #ffffff;
  }

  .tip-card p {
    color: var(--text-muted);
    line-height: 1.7;
    margin: 0;
    font-size: 0.95rem;
  }

  /* Golden hour */
  .golden-hour-section {
    padding: 5rem 0;
    background-color: var(--bg-secondary);
  }

  .split-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
  }

  .split-text h2 {
    font-size: clamp(1.8rem, 3.5vw, 2.5rem);
    margin-bottom: 1.5rem;
  }

  .split-text p {
    color: rgba(255,255,255,0.8);
    line-height: 1.8;
    margin-bottom: 1.25rem;
    font-size: 1rem;
  }

  .split-image img {
    border-radius: 8px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    border: 1px solid rgba(201, 168, 124, 0.2);
  }

  /* Kids & pets */
  .kids-pets-section {
    padding: 6rem 0;
  }

  .guidance-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2.5rem;
    margin-top: 3rem;
  }

  .guidance-card {
    background-color: var(--bg-secondary);
    border: 1px solid rgba(201, 168, 124, 0.15);
    border-radius: 8px;
    padding: 2.5rem;
  }

  .card-icon {
    font-size: 2.5rem;
    margin-bottom: 1.25rem;
  }

  .guidance-card h3 {
    font-size: 1.35rem;
    margin-bottom: 1rem;
    color: #ffffff;
  }

  .guidance-card p {
    color: var(--text-muted);
    line-height: 1.7;
    margin-bottom: 1.5rem;
    font-size: 0.95rem;
  }

  .practical-tip {
    background-color: rgba(201, 168, 124, 0.08);
    border-left: 2px solid var(--accent);
    padding: 1rem 1.25rem;
    font-size: 0.88rem;
    color: #e5e5e5;
    line-height: 1.5;
    border-radius: 2px;
  }

  /* Checklist */
  .checklist-section {
    padding: 3rem 0 6rem;
  }

  .checklist-box {
    background: linear-gradient(145deg, #141414 0%, #1a1a1a 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px;
    padding: 3rem;
    box-shadow: 0 8px 30px rgba(0,0,0,0.5);
  }

  .checklist-box h2 {
    font-size: 2rem;
    margin-bottom: 2rem;
  }

  .checklist-items {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
  }

  .checklist-items li {
    display: flex;
    align-items: center;
    gap: 1rem;
    font-size: 1rem;
    color: rgba(255,255,255,0.85);
  }

  .checklist-items span {
    color: var(--accent);
    font-weight: bold;
    font-size: 1.1rem;
  }

  /* FAQ Section */
  .faq-section {
    padding: 6rem 0 5rem;
  }

  .faq-header {
    margin-bottom: 3.5rem;
  }

  .faq-header h2 {
    font-size: clamp(1.8rem, 4vw, 2.5rem);
    margin-bottom: 0.75rem;
  }

  .faq-sub {
    color: var(--text-muted);
    font-size: 1.05rem;
  }

  .faq-accordion {
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
  .guide-cta {
    padding: 6rem 1.5rem;
    background-color: var(--bg-secondary);
    border-top: 1px solid rgba(255,255,255,0.06);
  }

  .guide-cta h2 {
    font-size: clamp(1.8rem, 3.5vw, 2.5rem);
    margin-bottom: 1rem;
  }

  .guide-cta p {
    color: var(--text-muted);
    max-width: 550px;
    margin: 0 auto 2.5rem;
    font-size: 1.05rem;
  }

  .cta-buttons {
    display: flex;
    justify-content: center;
    gap: 1.25rem;
    flex-wrap: wrap;
  }

  @media (max-width: 900px) {
    .split-layout {
      grid-template-columns: 1fr;
      gap: 2.5rem;
    }

    .tips-grid {
      grid-template-columns: 1fr;
    }

    .guidance-grid {
      grid-template-columns: 1fr;
    }

    .checklist-box {
      padding: 2rem 1.5rem;
    }
  }
</style>
