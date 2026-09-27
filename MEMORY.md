# Trvalá paměť projektu Nicol Photography (MEMORY.md)

*Stav rozpracovanosti a historie vylepšování webu.*

---

## 1. Základní informace
- **Klient:** Nicol Juráňová (fotografka, Olomoucký kraj, Hranice na Moravě)
- **Web:** `https://nicolphotography.cz`
- **Cesta k projektu:** `/home/jann/Job/photos`
- **Session:** `#agy-nicol`

---

## 2. Historie a dosavadní změny
- **2026-09-27 (Komplexní audit a balík vylepšení):**
  - **Audit a sjednocení témat:** Proveden kompletní audit a odstraněn vizuální konflikt mezi světlým globálním CSS a tmavým moody tématem.
  - **Sjednocení `src/app.css`:** Převod na moody dark tokeny (`#0a0a0a`, `#141414`, `#c9a87c`, text `#f5f5f5`).
  - **Modernizace `NavBar.svelte`:** Opraveno scrollování — zrušeno bílé pozadí, nasazen tmavý glassmorphism (`backdrop-blur`, poloprůhledné černé sklo), zlaté akcenty a tmavé mobilní menu.
  - **Patička `Footer.svelte`:** Převod z námořnické modři do tmavého moody tónu ladícího se zbytkem webu.
  - **Nový dotykový `Lightbox.svelte`:** Vytvořena znovupoužitelná přístupná komponenta s podporou mobilních **swipe gest** (posun prstem vlevo/vpravo, stažení dolů pro zavření), spinnerem načítání a čistými přechody. Integrována do `moody/Home.svelte` i `Akce.svelte`.
  - **Sociální důkaz (Social Proof):** Na úvodní stránku vrácena a vylepšena sekce autentických referencí klientů (rodiny, páry, zvířátka) s hodnocením 5 hvězdiček.
  - **Zpřehlednění kontaktního formuláře (`ContactForm.svelte`):** Přidán výběr preferovaného termínu/období a lokality, elegantní tmavé vstupy.
  - **Mobilní Sticky Quick Action bar (`MobileQuickContact.svelte`):** Na smartphonech se po odscrollování zobrazuje plovoucí lišta pro rychlé zavolání nebo domluvení focení.
  - **Čisté routování:** Zavedena kanonická cesta `/portfolio` se zachováním zpětné kompatibility pro `/akce`.
  - **Sestavení bez chyb:** Odstraněna veškerá a11y varování překladače, čistý build za 1.3 s.

  - **Interaktivní Before/After Slider (`BeforeAfter.svelte`):** Prezentace jemného retušování s plynulým posuvníkem (myš i dotyk) na úvodní stránce.
  - **Průvodce „Jak se připravit na focení“ (`Pruvodce.svelte`):** Kompletní klientský rádce s doporučenou paletou zemitých barev (vzorníky), tipy na zlatou hodinku, focení dětí a psů a interaktivním kontrolním seznamem. Zavedena nová routa `/pruvodce` a odkaz v navigaci.
  - **Strukturované balíčky a Dárkové poukazy (`Cenik.svelte`):** Přehledné rozdělení na *Balíček Klasik* a *Rodinný příběh* (badge Nejoblíbenější), dedikovaná karta na dárkový poukaz a upoutávka na Průvodce.
  - **Interaktivní FAQ akordeon & FAQPage Schema.org:** Implementován elegantní rozbalovací akordeon (odpovědi na počasí, pózování, termíny, RAW fotky, mazlíčky) na `/cenik` i `/pruvodce` včetně rich snippetů pro vyhledávače.
  - **Instagram Social Showcase:** Stylová mřížka 6 curated momentek na úvodní stránce s přímým odkazem na Instagram profil `@n.i.c.o.l_photography`.
  - **Chytré předvyplnění formuláře (Auto Pre-fill):** Proklik z balíčku v Ceníku automaticky nastaví správnou službu a zprávu v poptávkovém formuláři (`/kontakt?balicek=...`).
  - **Globální tlačítko Scroll-to-top (`ScrollToTop.svelte`):** Plovoucí zlaté tlačítko s plynulým posunem nahoru (zobrazí se po odscrollování > 400px), vyladěno pro koexistenci s cookie lištou i mobilním quick-contact barem.
  - **Portfolio konverzní CTA banner (`Akce.svelte`):** Na konec portfolia přidána výzva k akci s přímými tlačítky na rezervaci termínu a ceník.
  - **Obohacení stránky O mně (`About.svelte`):** Doplněn autentický popis fotografického stylu v Olomouckém kraji a akční odkazy na Průvodce a Ceník.
  - **Live Deploy a Browser Validace:** Vše otestováno přes Playwright headless Chrome s 0 chybami a nasazeno na ostrou produkci `https://nicolphotography.cz/` (commit `0e4ff01`).

---

## 3. Další možnosti a doporučení
1. **Lighthouse / Core Web Vitals:** Průběžná kontrola rychlosti a SEO na produkční doméně.
2. **Sezónní minibalíčky:** Speciální podzimní nebo vánoční akce v ceníku v příslušném období roku.



