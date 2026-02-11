<script>
  import NavBar from '../../lib/NavBar.svelte';
  import Footer from '../../lib/Footer.svelte';
  import images from '../../imageData/images.json';
</script>

<div class="minimal-theme">
  <NavBar />

  <!-- Hero - Ultra minimal -->
  <section class="hero">
    <h1>Nicol</h1>
    <p class="subtitle">Fotografka</p>
  </section>

  <!-- Featured Image - Full width -->
  <section class="featured">
    <img src="./src/images/portfolio/golden-hour.png" alt="Featured" />
  </section>

  <!-- Intro -->
  <section class="intro">
    <p>Zachycuji přirozené momenty a autentické emoce. Portrétní a rodinná fotografie v Olomouckém kraji.</p>
  </section>

  <!-- Gallery - Clean grid -->
  <section class="gallery">
    {#each images.slice(0, 6) as img}
      <div class="gallery-item">
        <img src={img.src} alt={img.alt} />
      </div>
    {/each}
  </section>

  <!-- View more -->
  <section class="more">
    <a href="/akce">Zobrazit portfolio →</a>
  </section>

  <!-- About -->
  <section class="about">
    <div class="about-image">
      <img src="./src/images/portfolio/nicol-portret.png" alt="Nicol" />
    </div>
    <div class="about-text">
      <h2>O mně</h2>
      <p>Jsem Nicol. Fotografka, která věří, že každý moment má svou vlastní krásu. Miluji práci s přirozeným světlem a autentické emoce.</p>
      <a href="/about">Více →</a>
    </div>
  </section>

  <!-- Services - Simple list -->
  <section class="services">
    <h2>Služby</h2>
    <ul>
      <li><a href="/cenik">Portréty</a></li>
      <li><a href="/cenik">Rodiny</a></li>
      <li><a href="/cenik">Páry</a></li>
      <li><a href="/cenik">Vánoční focení</a></li>
    </ul>
  </section>

  <!-- Contact -->
  <section class="contact">
    <h2>Kontakt</h2>
    <p>Pojďme vytvořit něco krásného.</p>
    <a href="/kontakt" class="contact-btn">Napsat →</a>
  </section>

  <!-- Instagram -->
  <section class="instagram">
    <a href="https://www.instagram.com/n.i.c.o.l_photography/" target="_blank" rel="noopener">
      @n.i.c.o.l_photography
    </a>
  </section>

  <Footer />
</div>

<style>
  .minimal-theme {
    --text: #111;
    --text-light: #666;
    --bg: #fff;

    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', -apple-system, sans-serif;
  }

  /* Hero */
  .hero {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(5rem, 20vw, 15rem);
    font-weight: 400;
    letter-spacing: -0.03em;
    margin: 0;
    line-height: 1;
  }

  .hero .subtitle {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.4em;
    color: var(--text-light);
    margin-top: 2rem;
  }

  /* Featured */
  .featured {
    padding: 0;
  }

  .featured img {
    width: 100%;
    height: 90vh;
    object-fit: cover;
  }

  /* Intro */
  .intro {
    max-width: 800px;
    margin: 0 auto;
    padding: 10rem 2rem;
    text-align: center;
  }

  .intro p {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    line-height: 1.5;
    font-weight: 400;
  }

  /* Gallery */
  .gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2px;
    padding: 0 2rem;
  }

  .gallery-item {
    aspect-ratio: 1;
    overflow: hidden;
  }

  .gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
  }

  .gallery-item:hover img {
    transform: scale(1.05);
  }

  /* More */
  .more {
    text-align: center;
    padding: 6rem 2rem;
  }

  .more a {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: var(--text);
    text-decoration: none;
    border-bottom: 1px solid var(--text);
    padding-bottom: 0.5rem;
  }

  /* About */
  .about {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 100vh;
  }

  .about-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .about-text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 4rem 8rem;
  }

  .about-text h2 {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    color: var(--text-light);
    margin-bottom: 2rem;
  }

  .about-text p {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    line-height: 1.6;
    margin-bottom: 3rem;
  }

  .about-text a {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: var(--text);
    text-decoration: none;
  }

  /* Services */
  .services {
    padding: 10rem 2rem;
    text-align: center;
  }

  .services h2 {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    color: var(--text-light);
    margin-bottom: 4rem;
  }

  .services ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .services li {
    margin: 1.5rem 0;
  }

  .services a {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 5vw, 4rem);
    color: var(--text);
    text-decoration: none;
    transition: opacity 0.3s ease;
  }

  .services a:hover {
    opacity: 0.5;
  }

  /* Contact */
  .contact {
    padding: 10rem 2rem;
    text-align: center;
    background: #f5f5f5;
  }

  .contact h2 {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    color: var(--text-light);
    margin-bottom: 2rem;
  }

  .contact p {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    margin-bottom: 3rem;
  }

  .contact-btn {
    display: inline-block;
    padding: 1.25rem 3rem;
    background: var(--text);
    color: white;
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    transition: opacity 0.3s ease;
  }

  .contact-btn:hover {
    opacity: 0.8;
  }

  /* Instagram */
  .instagram {
    padding: 6rem 2rem;
    text-align: center;
  }

  .instagram a {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: var(--text-light);
    text-decoration: none;
  }

  .instagram a:hover {
    color: var(--text);
  }

  /* Responsive */
  @media (max-width: 768px) {
    .gallery {
      grid-template-columns: repeat(2, 1fr);
    }

    .about {
      grid-template-columns: 1fr;
    }

    .about-image {
      height: 60vh;
    }

    .about-text {
      padding: 4rem 2rem;
    }
  }
</style>
