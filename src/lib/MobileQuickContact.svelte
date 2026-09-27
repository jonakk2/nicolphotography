<script>
  import { onMount } from 'svelte';

  let visible = false;

  onMount(() => {
    const handleScroll = () => {
      // Show on mobile when scrolled down past hero
      if (typeof window !== 'undefined') {
        visible = window.scrollY > 350;
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  });
</script>

{#if visible}
  <div class="mobile-quick-bar" aria-label="Rychlý kontakt">
    <a href="tel:+420771161818" class="quick-btn phone" aria-label="Zavolat fotografce">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
      </svg>
      <span>Zavolat</span>
    </a>
    <a href="/kontakt" class="quick-btn cta" aria-label="Napsat poptávku">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
        <polyline points="22,6 12,13 2,6"/>
      </svg>
      <span>Domluvit focení</span>
    </a>
  </div>
{/if}

<style>
  .mobile-quick-bar {
    display: none;
  }

  @media (max-width: 768px) {
    .mobile-quick-bar {
      position: fixed;
      bottom: 1.25rem;
      left: 1.25rem;
      right: 1.25rem;
      z-index: 990;
      display: flex;
      gap: 0.75rem;
      padding: 0.5rem;
      background-color: rgba(15, 15, 15, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(201, 168, 124, 0.25);
      border-radius: 9999px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      animation: slideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .quick-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.45rem;
      padding: 0.65rem 1rem;
      border-radius: 9999px;
      font-size: 0.88rem;
      font-weight: 500;
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .quick-btn.phone {
      flex: 1;
      background-color: rgba(255, 255, 255, 0.08);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .quick-btn.cta {
      flex: 1.6;
      background-color: #c9a87c;
      color: #0a0a0a;
      font-weight: 600;
      box-shadow: 0 2px 10px rgba(201, 168, 124, 0.3);
    }

    .quick-btn.cta:active {
      transform: scale(0.98);
      background-color: #dfc299;
    }
  }

  @keyframes slideUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
</style>
