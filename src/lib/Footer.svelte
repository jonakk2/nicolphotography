<script>
  import { faInstagram, faFacebook } from '@fortawesome/free-brands-svg-icons';
  import { Fa } from 'svelte-fa';
  const currentYear = new Date().getFullYear();
</script>

<footer class="footer">
  <div class="container">
    <div class="footer-content">
      <!-- Brand -->
      <div class="footer-section footer-brand">
        <a href="/" class="footer-logo">
          <img src="/images/logo/iconka_nicolka.webp" alt="NJ Photography Logo" loading="lazy" />
          <span>Nicol Juráňová</span>
        </a>
        <p>Fotografka z Hranic na Moravě a Olomouckého kraje. Portréty, rodiny, páry i zvířátka — přirozeně a v přírodě.</p>
      </div>

      <!-- Quick Links -->
      <div class="footer-section">
        <h4>Rychlé odkazy</h4>
        <ul class="footer-links">
          <li><a href="/">Domů</a></li>
          <li><a href="/portfolio">Portfolio</a></li>
          <li><a href="/cenik">Ceník</a></li>
          <li><a href="/about">O mně</a></li>
          <li><a href="/kontakt">Kontakt</a></li>
        </ul>
      </div>

      <!-- Services -->
      <div class="footer-section">
        <h4>Služby</h4>
        <ul class="footer-links">
          <li><a href="/cenik">Portrétní fotografie</a></li>
          <li><a href="/cenik">Rodinné focení</a></li>
          <li><a href="/cenik">Párové focení</a></li>
          <li><a href="/cenik">S domácími mazlíčky</a></li>
        </ul>
      </div>

      <!-- Contact -->
      <div class="footer-section">
        <h4>Kontakt</h4>
        <div class="footer-contact">
          <p>
            <a href="mailto:njuranova2003@gmail.com">njuranova2003@gmail.com</a>
          </p>
          <p>
            <a href="tel:+420771161818">+420 771 161 818</a>
          </p>
          <p>Hranice na Moravě a okolí</p>
        </div>
        <div class="footer-socials">
          <a href="https://www.instagram.com/n.i.c.o.l_photography/" target="_blank" rel="noopener" aria-label="Instagram">
            <Fa icon={faInstagram} />
          </a>
          <a href="https://www.facebook.com/profile.php?id=61572752776606" target="_blank" rel="noopener" aria-label="Facebook">
            <Fa icon={faFacebook} />
          </a>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <p>&copy; {currentYear} Nicol Juráňová photography. Všechna práva vyhrazena. | <a href="/ochrana-udaju">Ochrana osobních údajů</a> | <a href="/obchodni-podminky">Obchodní podmínky</a></p>
    </div>
  </div>
</footer>

<style>
  .footer {
    background-color: #0b0b0b;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    color: #e5e5e5;
    padding: 4rem 0 0;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }

  .footer-content {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1.5fr;
    gap: 3rem;
    padding-bottom: 3rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }

  .footer-logo {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    text-decoration: none;
    margin-bottom: 1rem;
  }

  .footer-logo img {
    height: 42px;
    width: auto;
    border-radius: 50%;
    border: 1px solid rgba(201, 168, 124, 0.4);
  }

  .footer-logo span {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.35rem;
    font-weight: 600;
    color: #ffffff;
    letter-spacing: 0.02em;
  }

  .footer-brand p {
    color: rgba(255, 255, 255, 0.65);
    line-height: 1.7;
    font-size: 0.92rem;
    max-width: 320px;
  }

  .footer-section h4 {
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 1.25rem;
    color: #c9a87c;
  }

  .footer-links {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .footer-links li {
    margin-bottom: 0.75rem;
  }

  .footer-links a {
    color: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    font-size: 0.92rem;
    transition: all 0.25s ease;
  }

  .footer-links a:hover {
    color: #c9a87c;
    padding-left: 3px;
  }

  .footer-contact p {
    margin-bottom: 0.5rem;
    color: rgba(255, 255, 255, 0.7);
    font-size: 0.92rem;
  }

  .footer-contact a {
    color: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    transition: color 0.25s ease;
  }

  .footer-contact a:hover {
    color: #c9a87c;
  }

  .footer-socials {
    display: flex;
    gap: 0.75rem;
    margin-top: 1.25rem;
  }

  .footer-socials a {
    width: 38px;
    height: 38px;
    background-color: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #e5e5e5;
    font-size: 1.1rem;
    transition: all 0.25s ease;
  }

  .footer-socials a:hover {
    background-color: #c9a87c;
    color: #0a0a0a;
    border-color: #c9a87c;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(201, 168, 124, 0.35);
  }

  .footer-bottom {
    padding: 1.5rem 0;
    text-align: center;
  }

  .footer-bottom p {
    color: rgba(255, 255, 255, 0.45);
    font-size: 0.85rem;
    margin: 0;
    line-height: 1.6;
  }

  .footer-bottom a {
    color: rgba(255, 255, 255, 0.55);
    text-decoration: underline;
    text-underline-offset: 2px;
    transition: color 0.2s ease;
  }

  .footer-bottom a:hover {
    color: #c9a87c;
  }

  @media (max-width: 992px) {
    .footer-content {
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
    }
  }

  @media (max-width: 576px) {
    .footer-content {
      grid-template-columns: 1fr;
      text-align: center;
      gap: 2rem;
    }

    .footer-logo {
      justify-content: center;
    }

    .footer-brand p {
      margin: 0 auto;
    }

    .footer-socials {
      justify-content: center;
    }
  }
</style>
