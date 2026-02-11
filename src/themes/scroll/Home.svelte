<script>
  import { onMount } from 'svelte';
  import NavBar from '../../lib/NavBar.svelte';
  import Footer from '../../lib/Footer.svelte';
  import images from '../../imageData/images.json';

  let scrollY = 0;
  let innerHeight = 0;

  onMount(() => {
    innerHeight = window.innerHeight;

    // Intersection Observer for fade-in animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
      observer.observe(el);
    });

    return () => observer.disconnect();
  });
</script>

<svelte:window bind:scrollY />

<div class="scroll-theme">
  <NavBar />

  <!-- Hero with Parallax -->
  <section class="hero">
    <div class="hero-bg" style="transform: translateY({scrollY * 0.5}px)">
      <img src="/images/portfolio/golden-hour.png" alt="" />
    </div>
    <div class="hero-content" style="transform: translateY({scrollY * 0.2}px); opacity: {1 - scrollY / 600}">
      <h1 class="split-text">
        <span style="transform: translateX({-scrollY * 0.1}px)">Nicol</span>
        <span style="transform: translateX({scrollY * 0.1}px)">Photography</span>
      </h1>
      <p>Olomoucký kraj</p>
    </div>
    <div class="scroll-hint" style="opacity: {1 - scrollY / 200}">
      <span>Scroll</span>
      <div class="scroll-line"></div>
    </div>
  </section>

  <!-- Horizontal Scroll Gallery -->
  <section class="horizontal-section">
    <div class="sticky-container">
      <div class="horizontal-content" style="transform: translateX({-scrollY * 0.3 + 300}px)">
        <div class="intro-text">
          <h2>Portfolio</h2>
          <p>Vybrané práce z mého portfolia. Portréty, rodiny, páry a vánoční focení.</p>
        </div>
        {#each images as img, i}
          <div class="h-gallery-item">
            <img src={img.src} alt={img.alt} />
            <span class="item-number">{String(i + 1).padStart(2, '0')}</span>
          </div>
        {/each}
        <div class="gallery-end">
          <a href="/akce">Zobrazit vše</a>
        </div>
      </div>
    </div>
  </section>

  <!-- About with reveal -->
  <section class="about">
    <div class="about-image animate-on-scroll">
      <img src="/images/portfolio/nicol-portret.png" alt="Nicol" />
    </div>
    <div class="about-content">
      <div class="animate-on-scroll delay-1">
        <span class="label">O mně</span>
        <h2>Jsem Nicol</h2>
      </div>
      <p class="animate-on-scroll delay-2">Fotografka z Olomouckého kraje, která věří, že každý moment má svou vlastní krásu.</p>
      <p class="animate-on-scroll delay-3">Miluji práci s přirozeným světlem, zejména golden hour. Specializuji se na portréty, rodinné a párové focení.</p>
      <a href="/about" class="animate-on-scroll delay-4">Více o mně →</a>
    </div>
  </section>

  <!-- Services with stagger animation -->
  <section class="services">
    <h2 class="animate-on-scroll">Služby</h2>
    <div class="services-grid">
      <div class="service-card animate-on-scroll delay-1">
        <div class="service-icon">
          <img src="/images/portfolio/portret-zena.png" alt="Portréty" />
        </div>
        <h3>Portréty</h3>
        <p>Osobní i profesionální portréty s důrazem na přirozené světlo.</p>
      </div>
      <div class="service-card animate-on-scroll delay-2">
        <div class="service-icon">
          <img src="/images/portfolio/rodina-vanoce.jpg" alt="Rodiny" />
        </div>
        <h3>Rodiny</h3>
        <p>Rodinné momenty zachycené v přírodě.</p>
      </div>
      <div class="service-card animate-on-scroll delay-3">
        <div class="service-icon">
          <img src="/images/portfolio/par-makove-pole.png" alt="Páry" />
        </div>
        <h3>Páry</h3>
        <p>Romantické focení při západu slunce.</p>
      </div>
      <div class="service-card animate-on-scroll delay-4">
        <div class="service-icon">
          <img src="/images/portfolio/vanocni-foceni.png" alt="Vánoce" />
        </div>
        <h3>Vánoce</h3>
        <p>Kouzelná atmosféra zimního focení.</p>
      </div>
    </div>
    <a href="/cenik" class="services-link animate-on-scroll">Zobrazit ceník →</a>
  </section>

  <!-- Text reveal section -->
  <section class="text-reveal">
    <h2 class="animate-on-scroll">
      <span>Zachycuji</span>
      <span>příběhy,</span>
      <span>které</span>
      <span>vydrží</span>
      <span>navždy.</span>
    </h2>
  </section>

  <!-- Contact with animation -->
  <section class="contact">
    <div class="contact-bg">
      <img src="/images/portfolio/kroj-foceni.png" alt="" />
    </div>
    <div class="contact-content animate-on-scroll">
      <h2>Pojďme spolupracovat</h2>
      <p>Máte projekt na mysli? Ráda si vyslechnu vaše představy.</p>
      <a href="/kontakt" class="contact-btn">Kontaktovat</a>
    </div>
  </section>

  <!-- Instagram marquee -->
  <section class="instagram-marquee">
    <div class="marquee-track">
      <span>@n.i.c.o.l_photography</span>
      <span>•</span>
      <span>@n.i.c.o.l_photography</span>
      <span>•</span>
      <span>@n.i.c.o.l_photography</span>
      <span>•</span>
      <span>@n.i.c.o.l_photography</span>
      <span>•</span>
    </div>
  </section>

  <Footer />
</div>

<style>
  .scroll-theme {
    --bg: #faf9f7;
    --text: #1a1a1a;
    --text-muted: #666;
    --accent: #c9a87c;

    background: var(--bg);
    color: var(--text);
    overflow-x: hidden;
  }

  /* Animations */
  .animate-on-scroll {
    opacity: 0;
    transform: translateY(40px);
    transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .animate-on-scroll.visible {
    opacity: 1;
    transform: translateY(0);
  }

  .delay-1 { transition-delay: 0.1s; }
  .delay-2 { transition-delay: 0.2s; }
  .delay-3 { transition-delay: 0.3s; }
  .delay-4 { transition-delay: 0.4s; }

  .label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    color: var(--accent);
    display: block;
    margin-bottom: 1rem;
  }

  /* Hero */
  .hero {
    height: 100vh;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .hero-bg {
    position: absolute;
    inset: -20%;
    z-index: 0;
  }

  .hero-bg img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.4);
  }

  .hero-content {
    position: relative;
    z-index: 1;
    text-align: center;
    color: white;
  }

  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 10vw, 8rem);
    font-weight: 400;
    line-height: 1;
    margin: 0;
  }

  .split-text span {
    display: block;
    transition: transform 0.1s ease-out;
  }

  .hero p {
    margin-top: 2rem;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.4em;
    opacity: 0.7;
  }

  .scroll-hint {
    position: absolute;
    bottom: 3rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    color: white;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
  }

  .scroll-line {
    width: 1px;
    height: 50px;
    background: white;
    margin-top: 1rem;
    animation: scrollPulse 2s infinite;
  }

  @keyframes scrollPulse {
    0%, 100% { transform: scaleY(0.5); opacity: 0.3; }
    50% { transform: scaleY(1); opacity: 1; }
  }

  /* Horizontal Section */
  .horizontal-section {
    height: 300vh;
    position: relative;
  }

  .sticky-container {
    position: sticky;
    top: 0;
    height: 100vh;
    overflow: hidden;
    display: flex;
    align-items: center;
  }

  .horizontal-content {
    display: flex;
    gap: 3rem;
    padding: 0 4rem;
    will-change: transform;
  }

  .intro-text {
    min-width: 400px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .intro-text h2 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    margin-bottom: 1rem;
  }

  .intro-text p {
    color: var(--text-muted);
    line-height: 1.7;
  }

  .h-gallery-item {
    min-width: 400px;
    height: 70vh;
    position: relative;
    overflow: hidden;
  }

  .h-gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .item-number {
    position: absolute;
    bottom: 1.5rem;
    right: 1.5rem;
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    color: white;
    background: rgba(0,0,0,0.5);
    padding: 0.5rem 1rem;
  }

  .gallery-end {
    min-width: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .gallery-end a {
    color: var(--text);
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    border-bottom: 1px solid var(--text);
    padding-bottom: 0.5rem;
  }

  /* About */
  .about {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 100vh;
    padding: 4rem;
    gap: 4rem;
    align-items: center;
  }

  .about-image img {
    width: 100%;
    height: 80vh;
    object-fit: cover;
  }

  .about-content {
    max-width: 500px;
  }

  .about-content h2 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    margin-bottom: 2rem;
  }

  .about-content p {
    color: var(--text-muted);
    line-height: 1.8;
    margin-bottom: 1.5rem;
  }

  .about-content a {
    color: var(--text);
    text-decoration: none;
    font-size: 0.85rem;
    letter-spacing: 0.1em;
  }

  /* Services */
  .services {
    padding: 8rem 4rem;
    text-align: center;
    background: white;
  }

  .services h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    margin-bottom: 4rem;
  }

  .services-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .service-card {
    text-align: center;
  }

  .service-icon {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    overflow: hidden;
    margin: 0 auto 1.5rem;
  }

  .service-icon img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
  }

  .service-card:hover .service-icon img {
    transform: scale(1.1);
  }

  .service-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    margin-bottom: 0.5rem;
  }

  .service-card p {
    color: var(--text-muted);
    font-size: 0.9rem;
  }

  .services-link {
    display: inline-block;
    margin-top: 4rem;
    color: var(--text);
    text-decoration: none;
    font-size: 0.85rem;
    letter-spacing: 0.1em;
    border-bottom: 1px solid var(--text);
    padding-bottom: 0.25rem;
  }

  /* Text reveal */
  .text-reveal {
    padding: 15rem 4rem;
    text-align: center;
    background: var(--text);
    color: white;
  }

  .text-reveal h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 6vw, 5rem);
    font-weight: 400;
    line-height: 1.3;
  }

  .text-reveal h2 span {
    display: inline-block;
    opacity: 0;
    transform: translateY(20px);
    animation: revealWord 0.6s forwards;
  }

  .text-reveal.visible h2 span:nth-child(1) { animation-delay: 0s; }
  .text-reveal.visible h2 span:nth-child(2) { animation-delay: 0.1s; }
  .text-reveal.visible h2 span:nth-child(3) { animation-delay: 0.2s; }
  .text-reveal.visible h2 span:nth-child(4) { animation-delay: 0.3s; }
  .text-reveal.visible h2 span:nth-child(5) { animation-delay: 0.4s; }

  @keyframes revealWord {
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  /* Contact */
  .contact {
    position: relative;
    min-height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .contact-bg {
    position: absolute;
    inset: 0;
    z-index: 0;
  }

  .contact-bg img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.3);
  }

  .contact-content {
    position: relative;
    z-index: 1;
    text-align: center;
    color: white;
    max-width: 600px;
  }

  .contact-content h2 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    margin-bottom: 1rem;
  }

  .contact-content p {
    opacity: 0.8;
    margin-bottom: 2rem;
  }

  .contact-btn {
    display: inline-block;
    padding: 1rem 2.5rem;
    border: 1px solid white;
    color: white;
    text-decoration: none;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    transition: all 0.3s ease;
  }

  .contact-btn:hover {
    background: white;
    color: var(--text);
  }

  /* Instagram marquee */
  .instagram-marquee {
    padding: 2rem 0;
    overflow: hidden;
    background: var(--bg);
  }

  .marquee-track {
    display: flex;
    gap: 3rem;
    animation: marquee 20s linear infinite;
    white-space: nowrap;
  }

  .marquee-track span {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    color: var(--text-muted);
  }

  @keyframes marquee {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
  }

  /* Responsive */
  @media (max-width: 1024px) {
    .services-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 768px) {
    .about {
      grid-template-columns: 1fr;
    }

    .about-image img {
      height: 50vh;
    }

    .services-grid {
      grid-template-columns: 1fr;
    }

    .service-icon {
      width: 150px;
      height: 150px;
    }

    .horizontal-section {
      height: auto;
    }

    .sticky-container {
      position: relative;
      height: auto;
      flex-direction: column;
    }

    .horizontal-content {
      flex-direction: column;
      transform: none !important;
    }

    .h-gallery-item {
      min-width: 100%;
      height: 60vh;
    }
  }
</style>
