<script>
  let y = 0;
  let show = false;

  $: show = y > 400;

  function scrollToTop() {
    if (typeof window !== 'undefined') {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    }
  }
</script>

<svelte:window bind:scrollY={y} />

<button
  type="button"
  class="scroll-top-btn {show ? 'visible' : ''}"
  on:click={scrollToTop}
  aria-label="Přejít na začátek stránky"
  title="Zpět nahoru"
>
  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="18 15 12 9 6 15"></polyline>
  </svg>
</button>

<style>
  .scroll-top-btn {
    position: fixed;
    bottom: 2.5rem;
    right: 2rem;
    z-index: 10005;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: rgba(18, 18, 18, 0.85);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(201, 168, 124, 0.4);
    color: #c9a87c;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    opacity: 0;
    visibility: hidden;
    transform: translateY(12px);
    transition: opacity 0.3s ease, visibility 0.3s ease, transform 0.3s ease, background 0.2s ease, border-color 0.2s ease, color 0.2s ease;
  }

  .scroll-top-btn.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }

  .scroll-top-btn:hover {
    background: #c9a87c;
    border-color: #c9a87c;
    color: #0a0a0a;
    transform: translateY(-2px);
  }

  @media (max-width: 768px) {
    .scroll-top-btn {
      bottom: 5.25rem; /* nad mobilním quick-contact barem */
      right: 1.25rem;
      width: 40px;
      height: 40px;
    }
  }
</style>
