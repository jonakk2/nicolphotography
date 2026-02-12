<script>
  import { onMount } from 'svelte';

  let visible = false;

  onMount(() => {
    const consent = localStorage.getItem('cookie-consent');
    if (consent === null) {
      visible = true;
    } else if (consent === 'accepted') {
      loadAnalytics();
    }
  });

  function accept() {
    localStorage.setItem('cookie-consent', 'accepted');
    visible = false;
    loadAnalytics();
  }

  function reject() {
    localStorage.setItem('cookie-consent', 'rejected');
    visible = false;
  }

  function loadAnalytics() {
    if (typeof window === 'undefined') return;
    if (document.getElementById('ga-script')) return;

    const GA_ID = window.__GA_ID__;
    if (!GA_ID) return;

    const script = document.createElement('script');
    script.id = 'ga-script';
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${GA_ID}`;
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA_ID);
  }
</script>

{#if visible}
  <div class="cookie-banner">
    <div class="cookie-content">
      <p>Tento web používá cookies pro měření návštěvnosti (Google Analytics). Žádné osobní údaje nesdílíme s třetími stranami.</p>
      <div class="cookie-actions">
        <button class="cookie-btn accept" on:click={accept}>Přijmout</button>
        <button class="cookie-btn reject" on:click={reject}>Odmítnout</button>
        <a href="/ochrana-udaju" class="cookie-link">Více info</a>
      </div>
    </div>
  </div>
{/if}

<style>
  .cookie-banner {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 9999;
    background-color: rgba(26, 32, 39, 0.97);
    backdrop-filter: blur(10px);
    padding: 1.25rem 1.5rem;
    box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.15);
  }

  .cookie-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 1.5rem;
    flex-wrap: wrap;
  }

  .cookie-content p {
    flex: 1;
    min-width: 280px;
    color: rgba(255, 255, 255, 0.85);
    font-size: 0.9rem;
    line-height: 1.5;
    margin: 0;
  }

  .cookie-actions {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex-shrink: 0;
  }

  .cookie-btn {
    padding: 0.6rem 1.25rem;
    border: none;
    border-radius: 4px;
    font-size: 0.9rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .cookie-btn.accept {
    background-color: var(--color-secondary, #6b8f3c);
    color: white;
  }

  .cookie-btn.accept:hover {
    background-color: var(--color-accent, #7da344);
  }

  .cookie-btn.reject {
    background-color: transparent;
    color: rgba(255, 255, 255, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.3);
  }

  .cookie-btn.reject:hover {
    border-color: rgba(255, 255, 255, 0.6);
    color: white;
  }

  .cookie-link {
    color: rgba(255, 255, 255, 0.5);
    font-size: 0.85rem;
    text-decoration: underline;
    transition: color 0.3s ease;
  }

  .cookie-link:hover {
    color: rgba(255, 255, 255, 0.8);
  }

  @media (max-width: 600px) {
    .cookie-content {
      flex-direction: column;
      text-align: center;
    }

    .cookie-actions {
      justify-content: center;
    }
  }
</style>
