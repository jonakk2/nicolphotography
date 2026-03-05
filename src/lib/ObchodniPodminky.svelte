<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
</script>

<svelte:head>
  <title>Obchodní podmínky | Nicol Juráňová photography</title>
  <meta name="description" content="Obchodní podmínky fotografických služeb Nicol Juráňová photography. Informace o rezervaci, záloze, cenách a dodání fotografií." />
  <link rel="canonical" href="https://nicolphotography.cz/obchodni-podminky" />
  <meta property="og:title" content="Obchodní podmínky | Nicol Juráňová photography" />
  <meta property="og:description" content="Obchodní podmínky fotografických služeb Nicol Juráňová photography." />
  <meta property="og:url" content="https://nicolphotography.cz/obchodni-podminky" />
  <meta property="og:image" content="https://nicolphotography.cz/hlavicka.png" />
  <meta property="og:type" content="website" />
</svelte:head>

<NavBar forceScrolled={true} />

<section class="terms-page">
  <div class="container">
    <h1>Obchodní podmínky</h1>

    <h2>1. Úvodní ustanovení</h2>
    <p>Tyto obchodní podmínky upravují smluvní vztah mezi fotografkou Nicol Juráňovou, IČO: 24396338 (dále jen "fotografka") a klientem (dále jen "klient") při poskytování fotografických služeb.</p>

    <h2>2. Objednávka a rezervace</h2>
    <p>Objednávka focení je závazná po potvrzení termínu ze strany fotografky a uhrazení rezervační zálohy.</p>
    <ul>
      <li>Rezervační záloha činí <strong>500 Kč</strong>.</li>
      <li>Záloha je <strong>nevratná</strong> a slouží k potvrzení rezervace termínu.</li>
      <li>Záloha se odečítá z celkové ceny focení.</li>
      <li>Zálohu je nutné uhradit do 3 dnů od potvrzení termínu, jinak rezervace propadá.</li>
    </ul>

    <h2>3. Ceny služeb</h2>
    <p>Aktuální ceník je uveden na stránce <a href="/cenik">Ceník</a>. Ceny jsou konečné (fotografka není plátcem DPH).</p>
    <ul>
      <li>Základní balíček: 1 500 Kč (1-2 hodiny focení, 10 upravených fotografií).</li>
      <li>Každá další upravená fotografie nad 10 kusů: 200 Kč.</li>
    </ul>

    <h2>4. Platba</h2>
    <p>Doplatek celkové ceny je splatný nejpozději při předání hotových fotografií. Platbu je možné provést bankovním převodem.</p>

    <h2>5. Průběh focení</h2>
    <ul>
      <li>Focení probíhá na předem dohodnutém místě a v dohodnutém čase.</li>
      <li>V případě nepříznivého počasí se termín po vzájemné dohodě přesune na jiný den.</li>
      <li>Délka focení je 1-2 hodiny.</li>
    </ul>

    <h2>6. Dodání fotografií</h2>
    <ul>
      <li>Fotografie jsou dodány v digitální podobě prostřednictvím online galerie.</li>
      <li>Standardní doba dodání je do <strong>14 dnů</strong> od focení.</li>
      <li>Klient si z galerie vybere fotografie k úpravě (dle dohodnutého počtu).</li>
      <li>Upravené fotografie jsou dodány v plném rozlišení ve formátu JPEG.</li>
    </ul>

    <h2>7. Autorská práva</h2>
    <ul>
      <li>Fotografka si ponechává autorská práva ke všem fotografiím dle zákona č. 121/2000 Sb.</li>
      <li>Klient získává licenci k osobnímu nekomerčnímu použití fotografií (tisk, sdílení na sociálních sítích).</li>
      <li>Komerční využití fotografií vyžaduje písemný souhlas fotografky.</li>
      <li>Fotografka si vyhrazuje právo použít fotografie pro vlastní prezentaci (portfolio, sociální sítě, web).</li>
    </ul>

    <h2>8. Zrušení ze strany klienta</h2>
    <ul>
      <li>Zrušení více než 7 dní před termínem: záloha propadá, bez dalších poplatků.</li>
      <li>Zrušení méně než 7 dní před termínem: záloha propadá.</li>
      <li>Nedostavení se bez omluvy: záloha propadá.</li>
      <li>Přesunutí termínu je možné po dohodě, záloha zůstává platná.</li>
    </ul>

    <h2>9. Zrušení ze strany fotografky</h2>
    <p>Pokud fotografka nemůže focení z vážných důvodů uskutečnit, nabídne klientovi náhradní termín nebo vrátí zálohu v plné výši.</p>

    <h2>10. Reklamace</h2>
    <p>Případné reklamace je nutné uplatnit do 14 dnů od dodání fotografií na email <a href="mailto:njuranova2003@gmail.com">njuranova2003@gmail.com</a>.</p>

    <h2>11. Závěrečná ustanovení</h2>
    <p>Tyto obchodní podmínky jsou platné od 1. 3. 2026. Fotografka si vyhrazuje právo podmínky změnit. Odesláním objednávky klient potvrzuje, že se s těmito podmínkami seznámil a souhlasí s nimi.</p>

    <p class="contact-info">Kontakt: <a href="mailto:njuranova2003@gmail.com">njuranova2003@gmail.com</a></p>
  </div>
</section>

<Footer />

<style>
  .terms-page {
    padding-top: 6rem;
    padding-bottom: 4rem;
    min-height: 100vh;
    background-color: var(--color-light);
  }

  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }

  h1 {
    margin-bottom: 2rem;
  }

  h2 {
    font-size: 1.25rem;
    margin-top: 2.5rem;
    margin-bottom: 0.75rem;
  }

  p {
    margin-bottom: 1rem;
    line-height: 1.8;
    color: #444;
  }

  ul {
    margin-bottom: 1rem;
    padding-left: 1.5rem;
  }

  li {
    margin-bottom: 0.5rem;
    line-height: 1.7;
    color: #444;
  }

  a {
    color: var(--color-secondary);
  }

  .contact-info {
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid #ddd;
    font-weight: 500;
  }
</style>
