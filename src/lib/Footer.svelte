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
          <img src="/images/logo/iconka_nicolka.webp" alt="NJ Photography Logo" />
          <span>Nicol Juráňová photography</span>
        </a>
        <p>Zachycuji příběhy, které vydrží navždy. Fotografka specializující se na portréty, rodinné a párové focení v Olomouckém kraji.</p>
      </div>

      <!-- Quick Links -->
      <div class="footer-section">
        <h4>Rychlé odkazy</h4>
        <ul class="footer-links">
          <li><a href="/">Domů</a></li>
          <li><a href="/akce">Portfolio</a></li>
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
          <li><a href="/cenik">Vánoční focení</a></li>
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
      <p>&copy; {currentYear} Nicol Juráňová photography. Všechna práva vyhrazena. | <a href="/ochrana-udaju">Ochrana osobních údajů</a></p>
    </div>
  </div>
</footer>

<style>
  .footer {
    background-color: var(--color-primary);
    color: white;
    padding: 4rem 0 0;
  }

  .footer-content {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1.5fr;
    gap: 3rem;
    padding-bottom: 3rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }

  .footer-logo {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    text-decoration: none;
    margin-bottom: 1rem;
  }

  .footer-logo img {
    height: 40px;
    width: auto;
    border-radius: 50%;
  }

  .footer-logo span {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 600;
    color: white;
  }

  .footer-brand p {
    color: rgba(255, 255, 255, 0.7);
    line-height: 1.7;
    font-size: 0.95rem;
  }

  .footer-section h4 {
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 1.25rem;
    color: white;
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
    font-size: 0.95rem;
    transition: color 0.3s ease;
  }

  .footer-links a:hover {
    color: var(--color-secondary);
  }

  .footer-contact p {
    margin-bottom: 0.5rem;
    color: rgba(255, 255, 255, 0.7);
    font-size: 0.95rem;
  }

  .footer-contact a {
    color: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .footer-contact a:hover {
    color: var(--color-secondary);
  }

  .footer-socials {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
  }

  .footer-socials a {
    width: 40px;
    height: 40px;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.2rem;
    transition: all 0.3s ease;
  }

  .footer-socials a:hover {
    background-color: var(--color-secondary);
    transform: translateY(-3px);
  }

  .footer-bottom {
    padding: 1.5rem 0;
    text-align: center;
  }

  .footer-bottom p {
    color: rgba(255, 255, 255, 0.5);
    font-size: 0.9rem;
    margin: 0;
  }

  @media (max-width: 992px) {
    .footer-content {
      grid-template-columns: 1fr 1fr;
    }
  }

  @media (max-width: 576px) {
    .footer-content {
      grid-template-columns: 1fr;
      text-align: center;
    }

    .footer-logo {
      justify-content: center;
    }

    .footer-socials {
      justify-content: center;
    }
  }
</style>
