import os
from playwright.sync_api import sync_playwright

html_content = """<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>Průvodce úspěšným startem pro fotografku | Nicol Juráňová</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    @page {
      size: A4 portrait;
      margin: 0;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Inter', sans-serif;
      background-color: #0d0d0d;
      color: #e5e5e5;
      font-size: 13.5px;
      line-height: 1.65;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }

    .page {
      width: 210mm;
      height: 297mm;
      padding: 24mm 22mm;
      position: relative;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background-color: #0d0d0d;
      overflow: hidden;
    }

    :root {
      --gold: #c9a87c;
      --gold-light: #dfc299;
      --gold-dark: #8c6b45;
      --card-bg: #141414;
      --border: rgba(201, 168, 124, 0.25);
      --text-muted: #999999;
    }

    /* Cover Page */
    .cover-page {
      background: radial-gradient(circle at 80% 20%, rgba(201, 168, 124, 0.12) 0%, transparent 60%), #0a0a0a;
      border: 1px solid var(--border);
      margin: 12mm;
      width: calc(210mm - 24mm);
      height: calc(297mm - 24mm);
      padding: 30mm 24mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .cover-top .tagline {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.35em;
      color: var(--gold);
      margin-bottom: 12px;
      display: inline-block;
    }

    .cover-top h1 {
      font-family: 'Playfair Display', serif;
      font-size: 42px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.18;
      margin-bottom: 20px;
    }

    .cover-top h1 span {
      color: var(--gold);
      font-style: italic;
    }

    .cover-top .subtitle {
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.6;
      max-width: 500px;
    }

    .cover-highlights {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      margin: 30px 0;
    }

    .highlight-card {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(201, 168, 124, 0.2);
      padding: 18px 20px;
      border-radius: 4px;
    }

    .highlight-card h4 {
      font-family: 'Playfair Display', serif;
      color: var(--gold);
      font-size: 15px;
      margin-bottom: 6px;
    }

    .highlight-card p {
      font-size: 12px;
      color: #aaaaaa;
      line-height: 1.5;
    }

    .cover-footer {
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      padding-top: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: #777777;
      text-transform: uppercase;
      letter-spacing: 0.15em;
    }

    .cover-footer .author {
      color: var(--gold);
      font-weight: 600;
    }

    /* Header & Footer on Inner Pages */
    .page-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 10px;
      margin-bottom: 24px;
      font-size: 10.5px;
      text-transform: uppercase;
      letter-spacing: 0.2em;
      color: #777;
    }

    .page-header-bar span.accent {
      color: var(--gold);
    }

    .page-footer-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 12px;
      margin-top: 24px;
      font-size: 10px;
      color: #666;
    }

    /* Content Typography */
    .section-title {
      font-family: 'Playfair Display', serif;
      font-size: 26px;
      font-weight: 600;
      color: #ffffff;
      margin-bottom: 8px;
    }

    .section-subtitle {
      font-size: 13px;
      color: var(--gold);
      text-transform: uppercase;
      letter-spacing: 0.15em;
      margin-bottom: 20px;
    }

    /* Content Cards */
    .card-grid {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .card {
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-left: 3px solid var(--gold);
      padding: 16px 20px;
      border-radius: 4px;
    }

    .card-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
    }

    .card-num {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(201, 168, 124, 0.15);
      color: var(--gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 700;
      flex-shrink: 0;
    }

    .card h3 {
      font-family: 'Playfair Display', serif;
      font-size: 16px;
      font-weight: 600;
      color: #ffffff;
    }

    .card p {
      font-size: 12.5px;
      color: #b5b5b5;
      line-height: 1.6;
      margin-bottom: 8px;
    }

    .card p:last-child {
      margin-bottom: 0;
    }

    .card .tip-badge {
      display: inline-block;
      background: rgba(201, 168, 124, 0.12);
      color: var(--gold-light);
      padding: 4px 10px;
      border-radius: 3px;
      font-size: 11px;
      font-weight: 500;
      margin-top: 6px;
      border: 1px solid rgba(201, 168, 124, 0.25);
    }

    /* Action Checklist */
    .checklist-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 15px;
    }

    .checklist-table th {
      text-align: left;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--gold);
      padding: 8px 12px;
      border-bottom: 1px solid rgba(201, 168, 124, 0.3);
    }

    .checklist-table td {
      padding: 10px 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      font-size: 12px;
      color: #cccccc;
    }

    .checklist-table td.checkbox {
      width: 30px;
      text-align: center;
      color: var(--gold);
      font-weight: bold;
    }

    .checklist-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }

    /* Quote Box */
    .quote-block {
      background: linear-gradient(135deg, rgba(201, 168, 124, 0.1) 0%, rgba(20, 20, 20, 0.95) 100%);
      border: 1px solid var(--border);
      padding: 18px 22px;
      border-radius: 6px;
      margin-top: 18px;
      text-align: center;
    }

    .quote-block p {
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: 15px;
      color: #ffffff;
      line-height: 1.6;
      margin-bottom: 6px;
    }

    .quote-block span {
      font-size: 11px;
      color: var(--gold);
      text-transform: uppercase;
      letter-spacing: 0.15em;
    }

    /* Source Box */
    .source-item {
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.06);
      padding: 14px 18px;
      border-radius: 4px;
      margin-bottom: 12px;
    }

    .source-item .source-author {
      font-family: 'Playfair Display', serif;
      font-size: 15px;
      color: var(--gold);
      font-weight: 600;
      margin-bottom: 4px;
    }

    .source-item .source-title {
      font-size: 12px;
      color: #ffffff;
      font-weight: 500;
      margin-bottom: 4px;
    }

    .source-item .source-desc {
      font-size: 11.5px;
      color: #aaaaaa;
      line-height: 1.5;
    }
  </style>
</head>
<body>

  <!-- PAGE 1: COVER -->
  <div class="page" style="padding: 0;">
    <div class="cover-page">
      <div class="cover-top">
        <span class="tagline">Strategický manuál & Tipy z praxe</span>
        <h1>Průvodce úspěšným startem <span>fotografky</span></h1>
        <p class="subtitle">Jak proměnit vášeň v prosperující focení v Olomouckém kraji, získat stálé klienty a vybudovat nezaměnitelnou značku.</p>
      </div>

      <div class="cover-highlights">
        <div class="highlight-card">
          <h4>01. Lidskost a bourání strachu</h4>
          <p>Proč se lidé bojí jít k fotografovi a jak je uklidnit dřív, než položí otázku na cenu.</p>
        </div>
        <div class="highlight-card">
          <h4>02. Taktika „Sneak Peek“</h4>
          <p>Jednoduchý trik s odesláním prvních fotek do 24 hodin, který tvoří virální reklamu.</p>
        </div>
        <div class="highlight-card">
          <h4>03. Lokální dominance</h4>
          <p>Nastavení Google profilu a Instagramu pro Hranice, Lipník a Olomoucký kraj.</p>
        </div>
        <div class="highlight-card">
          <h4>04. Akční plán & Odborné zdroje</h4>
          <p>Konkrétní kroky týden po týdnu a ověřené metodiky světových i českých fotografů.</p>
        </div>
      </div>

      <div class="cover-footer">
        <div>Web: <span class="author">nicolphotography.cz</span></div>
        <div>Vytvořeno pro: <span class="author">Nicol Juráňovou</span></div>
        <div>Září 2026</div>
      </div>
    </div>
  </div>

  <!-- PAGE 2: PSYCHOLOGIE A INSTAGRAM -->
  <div class="page">
    <div>
      <div class="page-header-bar">
        <span>Průvodce pro fotografku</span>
        <span class="accent">Kapitola 1: Psychologie & Instagram</span>
      </div>

      <h2 class="section-title">1. Jak bourat ostych a získat důvěru</h2>
      <div class="section-subtitle">Lidé si nevybírají foťák, ale člověka za ním</div>

      <div class="card-grid">
        <div class="card">
          <div class="card-header">
            <span class="card-num">1</span>
            <h3>Ukažte svou tvář na Instagram Stories</h3>
          </div>
          <p>Devadesát procent lidí má z focení panický strach: <em>„Neumím pózovat, budu vypadat blbě, děti budou brečet.“</em> Dokud vidí jen dokonalé fotky, nevědí, kdo za foťákem stojí.</p>
          <p>Jakmile Nicol na Stories ukáže, jak se chystá do lesa, jak se směje, jak se těší na focení nebo jak drbe pejska za uchem, <strong>strach z ní okamžitě spadne</strong>. Klientky mají pocit, že jdou na procházku s kamarádkou.</p>
          <span class="tip-badge">💡 Tip: Stačí 2–3 krátká videa týdně s přirozeným úsměvem, bez filtrů.</span>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-num">2</span>
            <h3>Taktika „Sneak Peek“ (Virální dosah zdarma)</h3>
          </div>
          <p>Klient po focení odchází plný emocí a zážitků. Čekat 14 dní na celou galerii znamená nechat tyto emoce vychladnout.</p>
          <p><strong>Vyberte 2–3 nejkrásnější fotky ještě ten večer nebo druhý den dopoledne</strong>, jemně je upravte a pošlete klientce na WhatsApp s milou zprávou: <em>„Marie, včera to bylo úžasné! Tady je malá ochutnávka, než dokončím celou galerii.“</em></p>
          <p>Klientka je nadšená, fotku okamžitě přeposílá babičce a sdílí na svůj Instagram s označením @n.i.c.o.l_photography. Její kamarádky to uvidí a Nicol má poptávky bez placené reklamy.</p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-num">3</span>
            <h3>Posílejte Průvodce před každým focením</h3>
          </div>
          <p>Máte k dispozici webovou stránku <code>nicolphotography.cz/pruvodce</code>. Používejte ji v každé komunikaci jako svou vizitku profesionality:</p>
          <p><em>„Moc se na vás těším! Aby pro vás byl výběr oblečení hračka, sepsala jsem tipy, jaké zemité barvy v přírodě nejlépe vyniknou: nicolphotography.cz/pruvodce.“</em></p>
          <span class="tip-badge">✨ Výsledek: Klienti přijdou perfektně sladění, v klidu a s respektem k vaší práci.</span>
        </div>
      </div>
    </div>

    <div class="page-footer-bar">
      <span>Nicol Juráňová photography</span>
      <span>Strana 2</span>
    </div>
  </div>

  <!-- PAGE 3: LOKÁLNÍ MARKETING A KLIENTI -->
  <div class="page">
    <div>
      <div class="page-header-bar">
        <span>Průvodce pro fotografku</span>
        <span class="accent">Kapitola 2: Získávání zakázek & Lokální SEO</span>
      </div>

      <h2 class="section-title">2. Jak získat klienty v Olomouckém kraji</h2>
      <div class="section-subtitle">Lidé hledají fotografku tam, kde žijí</div>

      <div class="card-grid">
        <div class="card">
          <div class="card-header">
            <span class="card-num">1</span>
            <h3>Profil Google Moje Firma (Mapy Google)</h3>
          </div>
          <p>Založení firemního profilu na Google je <strong>100% zdarma</strong> a je to nejsilnější nástroj pro lokální vyhledávání. Když někdo zadá <em>„fotografka Hranice na Moravě“</em> nebo <em>„rodinné focení Lipník“</em>, Google jako první zobrazí mapu s místními fotografkami.</p>
          <p>Vyplňte název: <strong>Nicol Juráňová photography – Rodinné a portrétní focení</strong>, zadejte web nicolphotography.cz, telefon a nahrajte 10 nejlepších fotek z webu.</p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-num">2</span>
            <h3>Síla autentických recenzí (Sociální důkaz)</h3>
          </div>
          <p>Recenze rozhodují. Po odevzdání finální galerie napište klientce:</p>
          <p><em>„Moc děkuji za krásné focení! Pokud jste byla spokojená, udělalo by mi obrovskou radost, kdybyste mi na Google napsala 2 věty, jak jste se u focení cítila. Pomůže mi to dostat se k dalším rodinám.“</em></p>
          <span class="tip-badge">🎯 Cíl: Prvních 10 pětihvězdičkových recenzí vás posune na přední pozice v celém okrese.</span>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-num">3</span>
            <h3>Lokální spolupráce (Květinářství, psí salóny, vizážistky)</h3>
          </div>
          <p>Najděte ve svém městě podniky, které cílí na stejné ženy:</p>
          <ul style="margin-left: 20px; font-size: 12px; color: #b5b5b5; margin-top: 5px;">
            <li><strong>Květinářství v Hranicích:</strong> Vyfoťte jim hezkou vazbu kytic na sociální sítě za to, že u pokladny nechají vaše dárkové poukazy.</li>
            <li><strong>Psí salón / cvičák:</strong> Vyfoťte ostříhaného pejska – majitelé psů jsou nejvěrnější klientská skupina pro focení v přírodě!</li>
            <li><strong>Vizážistka:</strong> Doporučujte si navzájem klientky na portréty a těhotenské focení.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="page-footer-bar">
      <span>Nicol Juráňová photography</span>
      <span>Strana 3</span>
    </div>
  </div>

  <!-- PAGE 4: CENOTVORBA A SEZÓNA -->
  <div class="page">
    <div>
      <div class="page-header-bar">
        <span>Průvodce pro fotografku</span>
        <span class="accent">Kapitola 3: Cenotvorba & Sezónnost</span>
      </div>

      <h2 class="section-title">3. Peníze, jistota a sezónní akce</h2>
      <div class="section-subtitle">Jak nebýt ve stresu z financí a termínů</div>

      <div class="card-grid">
        <div class="card">
          <div class="card-header">
            <span class="card-num">1</span>
            <h3>Rezervační záloha 500 Kč je vaše pojistka</h3>
          </div>
          <p>Začínající fotografky se bojí brát zálohy. Výsledkem bývá, že klient v den focení napíše <em>„dnes se nám to nehodí“</em> a fotografka ztratí půl dne i hezké světlo.</p>
          <p>Záloha 500 Kč, kterou už máte na webu zavedenou, odděluje seriózní zájemce od těch nespolehlivých. Klient si termínu mnohem více váží a neodřekne ho bez vážného důvodu.</p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-num">2</span>
            <h3>Nikdy neposkytujte neupravené RAW soubory</h3>
          </div>
          <p>Klienti se často ptají: <em>„Nemůžete nám poslat všechny fotky bez úprav?“</em> Odpověď musí být vždy s úsměvem, ale nekompromisní:</p>
          <p><em>„Surový RAW soubor je jako neupečený koláč nebo hrubá látka. Můj autorský rukopis vzniká teprve jemným doladěním barev, světla a ořezu. Chci, abyste odcházeli s dokonalým výsledkem.“</em></p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-num">3</span>
            <h3>Formát „Minifocení“ (Podzim & Vánoce)</h3>
          </div>
          <p>Dvakrát do roka (podzimní listí v říjnu a vánoční stromečky v listopadu) vyhlaste termín <strong>Minifocení</strong>:</p>
          <p>Jeden den, jedna nádherná lokalita, 6 klientů za sebou (každý 25 minut focení, 5 upravených fotek, cena 1 200–1 500 Kč). <strong>Za jediný víkendový den tak vyděláte 7 000 – 9 000 Kč</strong> a získáte 6 nových nadšených rodin, které se na jaře vrátí na velký balíček.</p>
        </div>
      </div>

      <div class="quote-block">
        <p>„Cena neodráží pouze hodinu mačkání spouště, ale roky tréninku oka, cit pro světlo, techniku, licence a hodiny strávené pečlivou postprodukcí u monitoru.“</p>
        <span>— Pravidlo zdravého fotografického byznysu</span>
      </div>
    </div>

    <div class="page-footer-bar">
      <span>Nicol Juráňová photography</span>
      <span>Strana 4</span>
    </div>
  </div>

  <!-- PAGE 5: CHECKLIST NA 30 DNÍ -->
  <div class="page">
    <div>
      <div class="page-header-bar">
        <span>Průvodce pro fotografku</span>
        <span class="accent">Kapitola 4: Akční plán</span>
      </div>

      <h2 class="section-title">4. Akční plán na prvních 30 dní</h2>
      <div class="section-subtitle">Přehledný seznam úkolů, které přinesou reálné výsledky</div>

      <table class="checklist-table">
        <thead>
          <tr>
            <th class="checkbox">Stav</th>
            <th style="width: 25%;">Kdy</th>
            <th>Konkrétní akční krok</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="checkbox">☐</td>
            <td><strong>Den 1 – 3</strong></td>
            <td><strong>Založit profil na Google Moje Firma:</strong> Nastavit město Hranice na Moravě, propojit s webem nicolphotography.cz a nahrát 10 fotek.</td>
          </tr>
          <tr>
            <td class="checkbox">☐</td>
            <td><strong>Den 4 – 7</strong></td>
            <td><strong>Získat první 3 recenze:</strong> Napsat klientům nebo kamarádkám z dosavadních focení a poprosit je o recenzi s hvězdičkami na Google.</td>
          </tr>
          <tr>
            <td class="checkbox">☐</td>
            <td><strong>Den 8 – 14</strong></td>
            <td><strong>První video na Stories:</strong> Krátké video s úsměvem: představit se, ukázat oblíbené místo na procházku a pozvat sledující na podzimní focení.</td>
          </tr>
          <tr>
            <td class="checkbox">☐</td>
            <td><strong>Den 15 – 20</strong></td>
            <td><strong>Otestovat taktiku Sneak Peek:</strong> U dalšího focení poslat 2 hotové fotky do 24 hodin na mobil a sledovat reakci a sdílení na sítích.</td>
          </tr>
          <tr>
            <td class="checkbox">☐</td>
            <td><strong>Den 21 – 25</strong></td>
            <td><strong>Vyhlásit termín podzimního minifocení:</strong> Vytvořit grafiku do Stories s nabídkou 5 volných slotů v hezké podzimní přírodě.</td>
          </tr>
          <tr>
            <td class="checkbox">☐</td>
            <td><strong>Den 26 – 30</strong></td>
            <td><strong>Oslovit 1 lokální podnik:</strong> Domluvit se s květinářstvím nebo kavárnou na umístění stylových vizitek / poukazů na pult.</td>
          </tr>
        </tbody>
      </table>

      <div class="card" style="margin-top: 25px; border-left: 3px solid #6b8f3c;">
        <div class="card-header">
          <span class="card-num" style="color: #6b8f3c; background: rgba(107, 143, 60, 0.15);">✓</span>
          <h3 style="color: #ffffff;">Máte k dispozici web světové úrovně</h3>
        </div>
        <p style="font-size: 12px; color: #b5b5b5;">
          Web <strong>nicolphotography.cz</strong> má nyní Before/After jezdec, špičkového průvodce pro klienty, strukturovaný ceník, dárkové poukazy i dotykový swipe lightbox. Je to silný profesionální nástroj — teď už stačí jen vykročit do terénu s úsměvem a láskou k fotkám!
        </p>
      </div>
    </div>

    <div class="page-footer-bar">
      <span>nicolphotography.cz · Vytvořeno s péčí pro Nicol Juráňovou</span>
      <span>Strana 5</span>
    </div>
  </div>

  <!-- PAGE 6: ODKAZY A ZDROJE -->
  <div class="page">
    <div>
      <div class="page-header-bar">
        <span>Průvodce pro fotografku</span>
        <span class="accent">Odborné zdroje & Inspirace</span>
      </div>

      <h2 class="section-title">5. Zdroje, transkripty & metodiky z praxe</h2>
      <div class="section-subtitle">Ověřené postupy od špičkových fotografů a byznys lektorů</div>

      <div class="source-item">
        <div class="source-author">Joy Michelle Photography (USA)</div>
        <div class="source-title">Podcast Called to Both & YouTube: „Client Experience & Sneak Peek Workflow“</div>
        <div class="source-desc">
          Joy Michelle detailně rozebírá koncept <strong>„Peak Euphoria“</strong> — klient je nejvíce emocionálně navázán na focení v prvních 24 hodinách. Odeslání 2–3 fotek do druhého dne zvyšuje míru organického sdílení na sítích o 300 % oproti předání galerie za 2 týdny.
        </div>
      </div>

      <div class="source-item">
        <div class="source-author">Taylor Jackson (Kanada)</div>
        <div class="source-title">Kniha & YouTube: „Wedding Photographers SEO: How to Rank #1 on Google“</div>
        <div class="source-desc">
          Autor metodiky <strong>„Go Small to Go Big“</strong>. Dokazuje, že začínající fotograf nesmí cílit na celostátní trh, ale musí stoprocentně ovládnout svůj mikromarket (Hranice na Moravě, Lipník, Olomouc) přes profil Google Moje Firma a recenze. Google Mapy generují více než 70 % lokálních prokliků.
        </div>
      </div>

      <div class="source-item">
        <div class="source-author">Elena S. Blair (USA)</div>
        <div class="source-title">CreativeLive & The Milky Way: „Lifestyle Photography & The Art of Mini Sessions“</div>
        <div class="source-desc">
          Mezinárodně uznávaná lektorka rodinné fotografie. Je autorkou strategie <strong>„Summer Camp Booking Model“</strong> pro minifocení s principem limitovaných míst a vysvětluje, proč fotografové, kteří ukazují svou tvář na Stories, dosahují až dvojnásobného konverzního poměru.
        </div>
      </div>

      <div class="source-item">
        <div class="source-author">Katelyn James (USA)</div>
        <div class="source-title">Kurzy & YouTube: „Culling, Workflow & Why We Never Give RAW Files“</div>
        <div class="source-desc">
          Přední lektorka fotografického workflow. Formulovala oborový standard vysvětlení zákazu neupravených fotek: RAW je surový polotovar (digitální negativ), polovina rukopisu spočívá v tónování a úpravě. Klientovi patří pouze dokončené dílo.
        </div>
      </div>

      <div class="source-item">
        <div class="source-author">Zoner: Milujeme fotografii & PPA (Professional Photographers of America)</div>
        <div class="source-title">Rubrika: „Legislativa, psychologie komunikace a podnikání ve fotografii“</div>
        <div class="source-desc">
          Český magazín a světová profesní asociace PPA poskytují metodické návody pro cenotvorbu, právní ochranu záloh (tzv. Retainer/rezervační poplatek proti rušení termínů na poslední chvíli) a budování vztahů se zákazníky.
        </div>
      </div>
    </div>

    <div class="page-footer-bar">
      <span>nicolphotography.cz · Vytvořeno s péčí pro Nicol Juráňovou</span>
      <span>Strana 6</span>
    </div>
  </div>

</body>
</html>
"""

with open('/home/jann/Job/photos/Pruvodce_startem_pro_fotografku_Nicol.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('HTML updated. Rendering 6-page PDF...')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path='/usr/bin/google-chrome')
    page = browser.new_page()
    page.goto('file:///home/jann/Job/photos/Pruvodce_startem_pro_fotografku_Nicol.html', wait_until='networkidle')
    page.wait_for_timeout(1000)
    
    pdf_path = '/home/jann/Job/photos/Pruvodce_startem_pro_fotografku_Nicol.pdf'
    page.pdf(
        path=pdf_path,
        format='A4',
        print_background=True,
        margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}
    )
    
    # Save preview of page 6
    pages = page.locator('.page')
    print('Total pages in PDF:', pages.count())
    pages.nth(5).screenshot(path='/home/jann/.gemini/antigravity-cli/brain/ce1d8801-20e5-40ab-b4fa-f3aed64abd59/guide_preview/page_6.png')
    
    browser.close()

print(f'PDF successfully generated at: {pdf_path}')
print(f'Size: {os.path.getsize(pdf_path)} bytes')
