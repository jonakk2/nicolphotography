<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
</script>

<svelte:head>
  <title>Ochrana osobních údajů | Nicol Juráňová photography</title>
  <meta name="description" content="Zásady ochrany osobních údajů webu Nicol Juráňová photography. Informace o zpracování dat dle GDPR." />
  <link rel="canonical" href="https://nicolphotography.cz/ochrana-udaju" />
  <meta property="og:title" content="Ochrana osobních údajů | Nicol Juráňová photography" />
  <meta property="og:description" content="Zásady ochrany osobních údajů webu Nicol Juráňová photography." />
  <meta property="og:url" content="https://nicolphotography.cz/ochrana-udaju" />
  <meta property="og:image" content="https://nicolphotography.cz/hlavicka.png" />
  <meta property="og:type" content="website" />
</svelte:head>

<NavBar forceScrolled={true} />

<section class="privacy-page">
  <div class="container">
    <h1>Ochrana osobních údajů</h1>

    <h2>1. Správce osobních údajů</h2>
    <p>Správcem osobních údajů je Nicol Juráňová, IČO: 24396338, se sídlem v Olomouckém kraji, email: <a href="mailto:njuranova2003@gmail.com">njuranova2003@gmail.com</a>.</p>

    <h2>2. Jaké údaje zpracováváme</h2>
    <p>Prostřednictvím kontaktního formuláře na tomto webu zpracováváme:</p>
    <ul>
      <li>Jméno a příjmení</li>
      <li>E-mailová adresa</li>
      <li>Telefonní číslo (pokud je uvedeno)</li>
      <li>Obsah zprávy</li>
    </ul>

    <h2>3. Účel zpracování</h2>
    <p>Vaše osobní údaje zpracováváme za účelem:</p>
    <ul>
      <li>Odpovědi na vaše dotazy</li>
      <li>Domluvení termínu focení</li>
      <li>Komunikace ohledně objednaných služeb</li>
    </ul>

    <h2>4. Právní základ zpracování</h2>
    <p>Zpracování probíhá na základě vašeho souhlasu (čl. 6 odst. 1 písm. a) GDPR) a pro plnění smlouvy (čl. 6 odst. 1 písm. b) GDPR).</p>

    <h2>5. Doba uchovávání</h2>
    <p>Osobní údaje uchováváme po dobu nezbytnou pro vyřízení vašeho požadavku, nejdéle však 3 roky od posledního kontaktu.</p>

    <h2>6. Vaše práva</h2>
    <p>Máte právo:</p>
    <ul>
      <li>Na přístup ke svým osobním údajům</li>
      <li>Na opravu nepřesných údajů</li>
      <li>Na výmaz údajů</li>
      <li>Na omezení zpracování</li>
      <li>Na přenositelnost údajů</li>
      <li>Podat stížnost u Úřadu pro ochranu osobních údajů</li>
    </ul>

    <h2>7. Cookies</h2>
    <p>Tento web používá pouze technicky nezbytné cookies pro zajištění správného fungování stránek. Nepoužíváme analytické ani marketingové cookies.</p>

    <h2>8. Kontakt</h2>
    <p>V případě dotazů ohledně zpracování osobních údajů nás kontaktujte na <a href="mailto:njuranova2003@gmail.com">njuranova2003@gmail.com</a>.</p>

    <p class="last-updated">Poslední aktualizace: únor 2026</p>
  </div>
</section>

<Footer />

<style>
  .privacy-page {
    padding: 8rem 0 4rem;
    background-color: white;
  }

  .privacy-page h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    margin-bottom: 2rem;
  }

  .privacy-page h2 {
    font-size: 1.3rem;
    margin-top: 2rem;
    margin-bottom: 0.75rem;
  }

  .privacy-page p,
  .privacy-page li {
    color: var(--color-muted);
    line-height: 1.8;
    margin-bottom: 0.5rem;
  }

  .privacy-page ul {
    padding-left: 1.5rem;
    margin-bottom: 1rem;
  }

  .privacy-page a {
    color: var(--color-secondary);
  }

  .last-updated {
    margin-top: 3rem;
    font-style: italic;
    font-size: 0.9rem;
  }
</style>
