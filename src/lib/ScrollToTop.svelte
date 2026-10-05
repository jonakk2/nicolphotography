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
  <svg 
    viewBox="0 0 24 24" 
    width="22" 
    height="22" 
    fill="none" 
    stroke="#c9a87c" 
    stroke-width="2.6" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    aria-hidden="true"
  >
    <polyline points="18 15 12 9 6 15"></polyline>
  </svg>
</button>

<style>
  .scroll-top-btn {
    position: fixed;
    bottom: 2.5rem;
    right: 2rem;
    z-index: 10005;
    width: 46px;
    height: 46px;
    min-width: 46px;
    min-height: 46px;
    padding: 0 !important;
    margin: 0 !important;
    box-sizing: border-box;
    border-radius: 50%;
    background: rgba(18, 18, 18, 0.92);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(201, 168, 124, 0.45);
    color: #c9a87c !important;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    opacity: 0;
    visibility: hidden;
    transform: translateY(12px);
    transition: opacity 0.3s ease, visibility 0.3s ease, transform 0.3s ease, background 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    flex-shrink: 0;
    -webkit-tap-highlight-color: transparent;
  }

  .scroll-top-btn.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }

  .scroll-top-btn svg {
    width: 22px !important;
    height: 22px !important;
    min-width: 22px;
    min-height: 22px;
    stroke: #c9a87c !important;
    stroke-width: 2.6;
    display: block;
    flex-shrink: 0;
    pointer-events: none;
    transition: stroke 0.2s ease;
  }

  .scroll-top-btn:hover {
    background: #c9a87c !important;
    border-color: #c9a87c !important;
    color: #0a0a0a !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(201, 168, 124, 0.4);
  }

  .scroll-top-btn:hover svg {
    stroke: #0a0a0a !important;
  }

  @media (max-width: 768px) {
    .scroll-top-btn {
      bottom: 5.25rem; /* nad mobilním quick-contact barem */
      right: 1.25rem;
      width: 42px;
      height: 42px;
      min-width: 42px;
      min-height: 42px;
    }

    .scroll-top-btn svg {
      width: 20px !important;
      height: 20px !important;
      min-width: 20px;
      min-height: 20px;
    }
  }
</style>
