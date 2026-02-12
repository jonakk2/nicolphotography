<script>
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';
</script>

<svelte:head>
  <title>Stránka nenalezena | Nicol Juráňová photography</title>
</svelte:head>

<NavBar forceScrolled={true} />

<section class="not-found">
  <div class="not-found-content">
    <h1>404</h1>
    <p class="subtitle">Stránka nenalezena</p>
    <p class="description">Omlouváme se, ale stránka, kterou hledáte, neexistuje nebo byla přesunuta.</p>
    <a href="/" class="back-btn">Zpět na hlavní stránku</a>
  </div>
</section>

<Footer />

<style>
  .not-found {
    min-height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem;
    background-color: var(--color-light, #f5f3ef);
  }

  .not-found-content {
    max-width: 500px;
  }

  h1 {
    font-family: 'Playfair Display', serif;
    font-size: 8rem;
    color: var(--color-secondary, #6b8f3c);
    line-height: 1;
    margin-bottom: 0.5rem;
  }

  .subtitle {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: var(--color-primary, #1a202c);
    margin-bottom: 1rem;
  }

  .description {
    color: var(--color-muted, #6b7280);
    font-size: 1rem;
    line-height: 1.7;
    margin-bottom: 2rem;
  }

  .back-btn {
    display: inline-block;
    background-color: var(--color-secondary, #6b8f3c);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    text-decoration: none;
    font-weight: 500;
    transition: background-color 0.3s ease;
  }

  .back-btn:hover {
    background-color: var(--color-accent, #7da344);
  }
</style>
