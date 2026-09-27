<script>
  export let forceScrolled = false;
  let isScrolled = false;
  let menuOpen = false;

  function toggleMenu() {
    menuOpen = !menuOpen;
  }

  function closeMenu() {
    menuOpen = false;
  }

  if (typeof window !== 'undefined') {
    window.addEventListener('scroll', () => {
      isScrolled = window.scrollY > 40;
    });
  }
</script>

<nav class="navbar" class:scrolled={isScrolled || forceScrolled}>
  <div class="nav-container">
    <a href="/" class="nav-brand" on:click={closeMenu}>
      <img src="/images/logo/iconka_nicolka.webp" class="nav-logo" alt="NJ Photography Logo" />
      <span class="brand-text">Nicol Juráňová</span>
    </a>

    <button class="mobile-toggle" class:active={menuOpen} on:click={toggleMenu} aria-label={menuOpen ? 'Zavřít menu' : 'Otevřít menu'}>
      <span></span>
      <span></span>
      <span></span>
    </button>

    <ul class="nav-links" class:active={menuOpen}>
      <li><a href="/" on:click={closeMenu}>Domů</a></li>
      <li><a href="/portfolio" on:click={closeMenu}>Portfolio</a></li>
      <li><a href="/cenik" on:click={closeMenu}>Ceník</a></li>
      <li><a href="/pruvodce" on:click={closeMenu}>Průvodce</a></li>
      <li><a href="/about" on:click={closeMenu}>O mně</a></li>
      <li><a href="/kontakt" class="nav-cta" on:click={closeMenu}>Kontakt</a></li>
    </ul>
  </div>
</nav>

<style>
  .navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    padding: 1.25rem 0;
    transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    background-color: transparent;
  }

  .navbar.scrolled {
    background-color: rgba(10, 10, 10, 0.88);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding: 0.85rem 0;
  }

  .nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .nav-brand {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    text-decoration: none;
  }

  .nav-logo {
    height: 40px;
    width: auto;
    border-radius: 50%;
    border: 1px solid rgba(201, 168, 124, 0.4);
  }

  .brand-text {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.35rem;
    font-weight: 500;
    letter-spacing: 0.03em;
    color: #f5f5f5;
    transition: color 0.3s ease;
  }

  .nav-brand:hover .brand-text {
    color: #c9a87c;
  }

  .nav-links {
    display: flex;
    align-items: center;
    gap: 2rem;
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .nav-links a {
    font-size: 0.88rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: rgba(255, 255, 255, 0.82);
    text-decoration: none;
    transition: color 0.25s ease;
    position: relative;
    padding: 0.25rem 0;
  }

  .nav-links a:hover {
    color: #c9a87c;
  }

  .nav-links a::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 0;
    height: 1.5px;
    background-color: #c9a87c;
    transition: width 0.25s ease;
  }

  .nav-links a:hover::after {
    width: 100%;
  }

  .nav-cta {
    background-color: #c9a87c !important;
    color: #0a0a0a !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.35rem !important;
    border-radius: 9999px !important;
    letter-spacing: 0.06em;
    box-shadow: 0 2px 10px rgba(201, 168, 124, 0.25);
    transition: all 0.25s ease !important;
  }

  .nav-cta:hover {
    background-color: #dfc299 !important;
    color: #0a0a0a !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 18px rgba(201, 168, 124, 0.45);
  }

  .nav-cta::after {
    display: none !important;
  }

  .mobile-toggle {
    display: none;
    flex-direction: column;
    gap: 6px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
    z-index: 1001;
  }

  .mobile-toggle span {
    width: 26px;
    height: 2px;
    background-color: #ffffff;
    border-radius: 2px;
    transition: all 0.3s ease;
  }

  .mobile-toggle.active span:nth-child(1) {
    transform: rotate(45deg) translate(6px, 6px);
    background-color: #c9a87c;
  }

  .mobile-toggle.active span:nth-child(2) {
    opacity: 0;
  }

  .mobile-toggle.active span:nth-child(3) {
    transform: rotate(-45deg) translate(5px, -5px);
    background-color: #c9a87c;
  }

  @media (max-width: 768px) {
    .nav-links {
      display: none;
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      background-color: rgba(12, 12, 12, 0.98);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      flex-direction: column;
      padding: 2rem 1.5rem;
      gap: 1.5rem;
      border-bottom: 1px solid rgba(201, 168, 124, 0.2);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
      align-items: center;
    }

    .nav-links.active {
      display: flex;
    }

    .nav-links a {
      color: rgba(255, 255, 255, 0.9) !important;
      font-size: 1.05rem;
      letter-spacing: 0.1em;
    }

    .nav-links a:hover {
      color: #c9a87c !important;
    }

    .nav-cta {
      width: 100%;
      text-align: center;
      margin-top: 0.5rem;
      padding: 0.75rem 1.5rem !important;
    }

    .mobile-toggle {
      display: flex;
    }
  }
</style>
