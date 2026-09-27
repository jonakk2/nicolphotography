# Nicol Juráňová Photography — Projektová pravidla (GEMINI.md)

Tento projekt je prezentační portfolio web fotografky **Nicol Juráňové** (Olomoucký kraj) běžící na doméně `https://nicolphotography.cz`.

## 1. Technický stack
- **Framework:** Svelte 4 / 5 + Vite (`package.json`)
- **Stylování:** Tailwind CSS + PostCSS (`tailwind.config.js`, `src/app.css`)
- **Hosting / Deploy:** Vercel (`vercel.json`) / Static export
- **Zpracování fotek:** `process_images.py` (optimalizace rozlišení a formátů)
- **Klíčové komponenty v `src/lib/`:**
  - `Home.svelte` (úvodní hero sekce, přehled služeb, ukázky prací)
  - `About.svelte` (o fotografce, osobní přístup, styl focení)
  - `Cenik.svelte` (cenové balíčky: portréty, rodiny, páry, rezervační poplatky)
  - `Kontakt.svelte` & `ContactForm.svelte` (kontaktní údaje, mapa, formulář)
  - `Akce.svelte` (speciální nabídky, sezónní focení)
  - `NavBar.svelte` & `Footer.svelte` (navigace a patička)
  - `ObchodniPodminky.svelte` & `PrivacyPolicy.svelte` (právní náležitosti a GDPR)

## 2. Zásady designu a textů (NO AI SLOP)
- **Přirozený lidský tón:** Texty musí působit osobně, přátelsky a autenticky. Vyvarovat se generických AI frází („v dnešním uspěchaném světě“, „zachytíme vaše vzácné okamžiky“).
- **Vizuální elegance:** Fotografie musí být středobodem webu. Teplé, vkusné tóny, jemná typografie, vzdušný layout, plynulé animace.
- **Rychlost a optimalizace:** Web nesmí lagovat kvůli obřím obrázkům. Všechny fotky musí být ve WebP/AVIF s patřičným `srcset` a lazy loadingem.
- **Responzivita:** 100% funkčnost a přehlednost na mobilních zařízeních (většina klientů přichází z Instagramu na mobilu).

## 3. Vývojové příkazy
- `npm run dev` — lokální vývojový server Vite
- `npm run build` — produkční build do `dist/`
