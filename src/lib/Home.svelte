<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
  import { Carousel } from 'flowbite-svelte';
  import images from '../imageData/images.json';

  let image;

  const services = [
    {
      icon: "👤",
      title: "Portrétní fotografie",
      description: "Zachytím vaši jedinečnou osobnost. Ať už jde o profesní portréty nebo osobní focení, vždy s přirozeným světlem."
    },
    {
      icon: "👨‍👩‍👧‍👦",
      title: "Rodinné focení",
      description: "Přirozené rodinné portréty plné lásky a radosti. Focení v přírodě, kde se všichni cítí uvolněně."
    },
    {
      icon: "💑",
      title: "Párové focení",
      description: "Zachytím váš příběh lásky. Romantické focení v přírodě, v makovém poli nebo při západu slunce."
    },
    {
      icon: "🎄",
      title: "Vánoční focení",
      description: "Kouzelná atmosféra vánočního focení v přírodě. S vůní jehličí a čerstvým vzduchem ve tvářích."
    }
  ];

  const testimonials = [
    {
      name: "Marie S.",
      event: "Rodinné focení",
      text: "Nicolka je úžasná! Děti se při focení cítily naprosto přirozeně a fotky jsou kouzelné. Doporučuji všem!"
    },
    {
      name: "Dominik H.",
      event: "Párové focení",
      text: "Focení v makovém poli bylo nezapomenutelné. Nicolka přesně věděla, jak nás navést k přirozeným pózám."
    }
  ];
</script>

<NavBar />

<!-- Page Header -->
<section class="page-header">
  <div class="page-header-overlay"></div>
  <div class="page-header-content">
    <h1>Zachycuji příběhy,<br/>které vydrží navždy</h1>
    <p>Portrétní a rodinná fotografka z Olomouckého kraje</p>
    <div class="hero-buttons">
      <a href="/kontakt" class="btn">Domluvit focení</a>
      <a href="/akce" class="btn btn-outline">Prohlédnout portfolio</a>
    </div>
  </div>
</section>

<!-- About Preview -->
<section class="about-preview">
  <div class="container">
    <div class="about-grid">
      <div class="about-image">
        <img src="./src/images/portfolio/nicol-portret.png" alt="Nicol - fotografka" />
      </div>
      <div class="about-text">
        <span class="section-label">O mně</span>
        <h2>Ahoj, jsem Nicol</h2>
        <p>Jsem holka, která si chce splnit jeden ze svých velkých snů. Fotografie je pro mě způsob, jak zachytit emoce a momenty, které by jinak zmizely.</p>
        <p>Specializuji se na portrétní a rodinnou fotografii. Miluji práci s přirozeným světlem, especially golden hour, kdy je světlo nejkrásnější.</p>
        <p>Působím v Olomouckém kraji a okolí, ale ráda přijedu kamkoliv, kde je krásná příroda a vy.</p>
        <a href="/about" class="link-arrow">Více o mně →</a>
      </div>
    </div>
  </div>
</section>

<!-- Services -->
<section class="services">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Služby</span>
      <h2>Co pro vás mohu udělat</h2>
    </div>
    <div class="services-grid">
      {#each services as service}
        <div class="service-card">
          <span class="service-icon">{service.icon}</span>
          <h3>{service.title}</h3>
          <p>{service.description}</p>
        </div>
      {/each}
    </div>
    <div class="services-cta">
      <a href="/cenik" class="btn">Zobrazit ceník</a>
    </div>
  </div>
</section>

<!-- Gallery Preview -->
<section class="gallery-preview">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Portfolio</span>
      <h2>Moje práce</h2>
    </div>
    <div class="gallery-grid-preview">
      {#each images.slice(0, 6) as img}
        <div class="gallery-item-preview">
          <img src={img.src} alt={img.alt} loading="lazy" />
        </div>
      {/each}
    </div>
    <div class="gallery-cta">
      <a href="/akce" class="btn">Zobrazit celé portfolio</a>
    </div>
  </div>
</section>

<!-- Testimonials -->
<section class="testimonials">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Reference</span>
      <h2>Co říkají klienti</h2>
    </div>
    <div class="testimonials-grid">
      {#each testimonials as testimonial}
        <div class="testimonial-card">
          <p class="testimonial-text">"{testimonial.text}"</p>
          <div class="testimonial-author">
            <strong>{testimonial.name}</strong>
            <span>{testimonial.event}</span>
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>

<!-- Instagram CTA -->
<section class="instagram-section">
  <div class="container">
    <div class="instagram-content">
      <span class="section-label">Instagram</span>
      <h2>Sledujte mě na Instagramu</h2>
      <p>Další fotky, zákulisí focení a novinky najdete na mém Instagramu</p>
      <a href="https://www.instagram.com/n.i.c.o.l_photography/" target="_blank" rel="noopener" class="btn instagram-btn">
        @n.i.c.o.l_photography
      </a>
    </div>
  </div>
</section>

<!-- CTA Section -->
<section class="cta-section">
  <div class="container">
    <h2>Připraveni vytvořit vzpomínky?</h2>
    <p>Kontaktujte mě a společně naplánujeme vaše focení</p>
    <a href="/kontakt" class="btn btn-light">Nezávazná konzultace</a>
  </div>
</section>

<Footer />

<style>
  /* Page Header */
  .page-header {
    position: relative;
    height: 50vh;
    min-height: 400px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-image: url('./src/images/background/hlavicka.webp');
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
    max-width: 800px;
    padding: 0 1.5rem;
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
    margin-bottom: 2rem;
  }

  .hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  .hero-buttons .btn {
    background-color: var(--color-secondary);
    border-color: var(--color-secondary);
  }

  .hero-buttons .btn-outline {
    background-color: transparent;
    border-color: white;
    color: white;
  }

  .hero-buttons .btn-outline:hover {
    background-color: white;
    color: var(--color-primary);
  }

  /* About Preview */
  .about-preview {
    padding: 6rem 0;
    background-color: white;
  }

  .about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
  }

  .about-image img {
    width: 100%;
    height: 500px;
    object-fit: cover;
    object-position: top;
    border-radius: 8px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  }

  .about-text h2 {
    margin-bottom: 1.5rem;
  }

  .about-text p {
    color: var(--color-muted);
    margin-bottom: 1rem;
    line-height: 1.8;
  }

  .section-label {
    display: inline-block;
    color: var(--color-secondary);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    font-weight: 600;
    margin-bottom: 0.5rem;
  }

  .link-arrow {
    display: inline-block;
    margin-top: 1rem;
    color: var(--color-secondary);
    font-weight: 500;
    transition: transform 0.3s ease;
  }

  .link-arrow:hover {
    transform: translateX(5px);
  }

  /* Services */
  .services {
    padding: 6rem 0;
    background-color: var(--color-light);
  }

  .services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
  }

  .service-card {
    background: white;
    padding: 2.5rem 2rem;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .service-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
  }

  .service-icon {
    font-size: 3rem;
    display: block;
    margin-bottom: 1.5rem;
  }

  .service-card h3 {
    margin-bottom: 1rem;
    font-size: 1.25rem;
  }

  .service-card p {
    color: var(--color-muted);
    font-size: 0.95rem;
    line-height: 1.7;
  }

  .services-cta {
    text-align: center;
    margin-top: 3rem;
  }

  /* Gallery Preview */
  .gallery-preview {
    padding: 6rem 0;
    background-color: white;
  }

  .gallery-grid-preview {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-top: 3rem;
  }

  .gallery-item-preview {
    aspect-ratio: 1;
    overflow: hidden;
    border-radius: 8px;
  }

  .gallery-item-preview img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
  }

  .gallery-item-preview:hover img {
    transform: scale(1.1);
  }

  .gallery-cta {
    text-align: center;
    margin-top: 3rem;
  }

  /* Testimonials */
  .testimonials {
    padding: 6rem 0;
    background-color: var(--color-light);
  }

  .testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
  }

  .testimonial-card {
    background: white;
    padding: 2.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  }

  .testimonial-text {
    font-style: italic;
    font-size: 1.1rem;
    line-height: 1.8;
    color: var(--color-dark);
    margin-bottom: 1.5rem;
  }

  .testimonial-author strong {
    display: block;
    color: var(--color-primary);
  }

  .testimonial-author span {
    color: var(--color-muted);
    font-size: 0.9rem;
  }

  /* Instagram Section */
  .instagram-section {
    padding: 5rem 0;
    background-color: white;
  }

  .instagram-content {
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
  }

  .instagram-content h2 {
    margin-bottom: 1rem;
  }

  .instagram-content p {
    color: var(--color-muted);
    margin-bottom: 2rem;
  }

  .instagram-btn {
    background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
    border: none;
  }

  .instagram-btn:hover {
    opacity: 0.9;
    background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
    color: white;
  }

  /* CTA Section */
  .cta-section {
    padding: 6rem 0;
    background: linear-gradient(135deg, var(--color-primary) 0%, #1a252f 100%);
    text-align: center;
    color: white;
  }

  .cta-section h2 {
    color: white;
    margin-bottom: 1rem;
  }

  .cta-section p {
    opacity: 0.9;
    margin-bottom: 2rem;
    font-size: 1.1rem;
  }

  .btn-light {
    background-color: white;
    border-color: white;
    color: var(--color-primary);
  }

  .btn-light:hover {
    background-color: transparent;
    color: white;
  }

  /* Section title with underline */
  .section-title {
    text-align: center;
  }

  .section-title h2::after {
    content: '';
    display: block;
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, var(--color-secondary), var(--color-accent));
    margin: 1rem auto 0;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .about-grid {
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    .about-image img {
      height: 350px;
    }


    .gallery-grid-preview {
      grid-template-columns: repeat(2, 1fr);
    }
  }
</style>
