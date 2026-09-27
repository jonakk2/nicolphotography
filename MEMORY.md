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

---

## 3. Další možnosti a doporučení
1. **Lighthouse / SEO ladění:** Průběžná kontrola Core Web Vitals na produkční doméně.
2. **Instagram feed integrace:** Případné zobrazení posledních fotek z Instagramu či přímé tlačítko do feedu.
3. **Sezónní kampaně:** Speciální podzimní nebo vánoční minibalíčky v ceníku v příslušném období.
