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
    padding: 6rem 2rem 4rem;
    background-color: #0a0a0a;
    color: #ffffff;
  }

  .not-found-content {
    max-width: 550px;
  }

  h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(5rem, 12vw, 8rem);
    color: #c9a87c;
    line-height: 1;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
  }

  .subtitle {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.5rem, 3vw, 2rem);
    color: #ffffff;
    margin-bottom: 1rem;
    font-weight: 400;
  }

  .description {
    color: #888888;
    font-size: 1.05rem;
    line-height: 1.7;
    margin-bottom: 2.5rem;
  }

  .back-btn {
    display: inline-block;
    background-color: #c9a87c;
    color: #0a0a0a;
    padding: 1rem 2.5rem;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    text-decoration: none;
    transition: all 0.3s ease;
  }

  .back-btn:hover {
    background-color: #ffffff;
    color: #0a0a0a;
  }
</style>
