<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
  import ContactForm from './ContactForm.svelte';
</script>

<svelte:head>
  <title>Kontakt | Nicol Juráňová photography</title>
  <meta name="description" content="Kontaktujte Nicol Juráňovou a domluvte si termín focení. Portrétní, rodinné a párové focení v Olomouckém kraji." />
  <link rel="canonical" href="https://nicolphotography.cz/kontakt" />
  <meta property="og:title" content="Kontakt | Nicol Juráňová photography" />
  <meta property="og:description" content="Kontaktujte Nicol Juráňovou a domluvte si termín focení v Olomouckém kraji." />
  <meta property="og:url" content="https://nicolphotography.cz/kontakt" />
  <meta property="og:image" content="https://nicolphotography.cz/hlavicka.png" />
  <meta property="og:type" content="website" />
</svelte:head>

<NavBar />

<!-- Page Header -->
<section class="page-header">
  <div class="page-header-overlay"></div>
  <div class="page-header-content">
    <h1>Kontakt</h1>
    <p>Pojďme společně naplánovat vaše focení</p>
  </div>
</section>

<!-- Contact Section -->
<section class="contact-section">
  <div class="container">
    <div class="contact-grid">
      <!-- Contact Info -->
      <div class="contact-info">
        <span class="section-label">Napište mi</span>
        <h2>Těším se na spolupráci</h2>
        <p>Máte otázky nebo chcete domluvit focení? Neváhejte mě kontaktovat. Odpovídám obvykle do 24 hodin.</p>

        <div class="contact-details">
          <div class="contact-item">
            <div class="contact-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
              </svg>
            </div>
            <div>
              <h4>Email</h4>
              <a href="mailto:njuranova2003@gmail.com">njuranova2003@gmail.com</a>
            </div>
          </div>

          <div class="contact-item">
            <div class="contact-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
            </div>
            <div>
              <h4>Telefon</h4>
              <a href="tel:+420771161818">+420 771 161 818</a>
            </div>
          </div>

          <div class="contact-item">
            <div class="contact-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                <circle cx="12" cy="10" r="3"/>
              </svg>
            </div>
            <div>
              <h4>Lokalita</h4>
              <span>Hranice na Moravě</span>
            </div>
          </div>
        </div>

        <div class="social-links">
          <h4>Sledujte mě</h4>
          <div class="social-icons">
            <a href="https://www.instagram.com/n.i.c.o.l_photography/" target="_blank" rel="noopener" aria-label="Instagram">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
            </a>
            <a href="https://www.facebook.com/profile.php?id=61572752776606" target="_blank" rel="noopener" aria-label="Facebook">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
              </svg>
            </a>
          </div>
        </div>
      </div>

      <!-- Contact Form -->
      <div class="contact-form-wrapper">
        <ContactForm />
      </div>
    </div>
  </div>
</section>

<!-- Map placeholder -->
<section class="map-section">
  <div class="map-placeholder">
    <p>Působím v okolí Hranic na Moravě, ale ráda k Vám přijedu kamkoliv v Olomouckém kraji.</p>
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
    background-image: url('/images/background/hlavicka.webp');
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
  }

  /* Contact Section */
  .contact-section {
    padding: 6rem 0;
    background-color: white;
  }

  .contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: start;
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

  .contact-info h2 {
    margin-bottom: 1rem;
  }

  .contact-info > p {
    color: var(--color-muted);
    margin-bottom: 2rem;
    line-height: 1.7;
  }

  .contact-details {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-bottom: 2.5rem;
  }

  .contact-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
  }

  .contact-icon {
    width: 50px;
    height: 50px;
    background-color: var(--color-light);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: var(--color-secondary);
  }

  .contact-item h4 {
    font-size: 0.9rem;
    color: var(--color-muted);
    margin-bottom: 0.25rem;
    font-weight: 500;
  }

  .contact-item a,
  .contact-item span {
    color: var(--color-dark);
    font-size: 1rem;
  }

  .contact-item a:hover {
    color: var(--color-secondary);
  }

  .social-links h4 {
    font-size: 1rem;
    margin-bottom: 1rem;
    color: var(--color-primary);
  }

  .social-icons {
    display: flex;
    gap: 1rem;
  }

  .social-icons a {
    width: 45px;
    height: 45px;
    background-color: var(--color-light);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--color-primary);
    transition: all 0.3s ease;
  }

  .social-icons a:hover {
    background-color: var(--color-secondary);
    color: white;
  }

  /* Contact Form Wrapper */
  .contact-form-wrapper {
    background-color: var(--color-light);
    padding: 2.5rem;
    border-radius: 12px;
  }

  /* Map Section */
  .map-section {
    background-color: var(--color-light);
  }

  .map-placeholder {
    padding: 4rem 2rem;
    text-align: center;
    background: linear-gradient(135deg, var(--color-primary) 0%, #1a252f 100%);
    color: white;
  }

  .map-placeholder p {
    max-width: 600px;
    margin: 0 auto;
    font-size: 1.2rem;
    opacity: 0.9;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .contact-grid {
      grid-template-columns: 1fr;
      gap: 3rem;
    }

    .contact-form-wrapper {
      padding: 1.5rem;
    }
  }
</style>
