<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';

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
      isScrolled = window.scrollY > 50;
    });
  }
</script>

<nav class="navbar" class:scrolled={isScrolled || forceScrolled}>
  <div class="nav-container">
    <a href="/" class="nav-brand">
      <img src="./src/images/logo/podpis_kribala.webp" class="nav-logo" alt="NJ Photography Logo" />
      <span class="brand-text">Nicol Juráňová photography</span>
    </a>

    <button class="mobile-toggle" class:active={menuOpen} on:click={toggleMenu} aria-label="Otevřít menu">
      <span></span>
      <span></span>
      <span></span>
    </button>

    <ul class="nav-links" class:active={menuOpen}>
      <li><a href="/" on:click={closeMenu}>Domů</a></li>
      <li><a href="/akce" on:click={closeMenu}>Portfolio</a></li>
      <li><a href="/cenik" on:click={closeMenu}>Ceník</a></li>
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
    padding: 1rem 0;
    transition: all 0.3s ease;
    background-color: transparent;
  }

  .navbar.scrolled {
    background-color: rgba(255, 255, 255, 0.98);
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
    padding: 0.75rem 0;
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
  }

  .brand-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--color-primary);
  }

  .navbar:not(.scrolled) .brand-text {
    color: white;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
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
    font-size: 0.95rem;
    font-weight: 500;
    color: var(--color-primary);
    text-decoration: none;
    transition: color 0.3s ease;
    position: relative;
  }

  .navbar:not(.scrolled) .nav-links a {
    color: white;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  }

  .nav-links a::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 0;
    height: 2px;
    background-color: var(--color-secondary);
    transition: width 0.3s ease;
  }

  .nav-links a:hover::after {
    width: 100%;
  }

  .nav-cta {
    background-color: var(--color-secondary);
    color: white !important;
    padding: 0.6rem 1.25rem;
    border-radius: 4px;
    text-shadow: none !important;
  }

  .nav-cta:hover {
    background-color: var(--color-accent);
  }

  .nav-cta::after {
    display: none;
  }

  .mobile-toggle {
    display: none;
    flex-direction: column;
    gap: 5px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
  }

  .mobile-toggle span {
    width: 25px;
    height: 2px;
    background-color: var(--color-primary);
    transition: all 0.3s ease;
  }

  .navbar:not(.scrolled) .mobile-toggle span {
    background-color: white;
  }

  .mobile-toggle.active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
  }

  .mobile-toggle.active span:nth-child(2) {
    opacity: 0;
  }

  .mobile-toggle.active span:nth-child(3) {
    transform: rotate(-45deg) translate(5px, -5px);
  }

  @media (max-width: 768px) {
    .nav-links {
      display: none;
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      background-color: white;
      flex-direction: column;
      padding: 1.5rem;
      gap: 1rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }

    .nav-links.active {
      display: flex;
    }

    .nav-links a {
      color: var(--color-primary) !important;
      text-shadow: none !important;
    }

    .mobile-toggle {
      display: flex;
    }
  }
</style>
