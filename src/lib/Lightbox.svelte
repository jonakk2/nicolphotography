<script>
  import { createEventDispatcher, onMount, onDestroy } from 'svelte';

  export let images = [];
  export let currentIndex = 0;
  export let categoryName = '';
  export let isOpen = false;

  const dispatch = createEventDispatcher();

  let touchStartX = 0;
  let touchStartY = 0;
  let touchEndX = 0;
  let touchEndY = 0;
  let isImageLoading = true;

  $: currentImg = images[currentIndex] || null;
  $: if (currentImg) {
    isImageLoading = true;
  }

  function close() {
    dispatch('close');
  }

  function next() {
    if (images.length === 0) return;
    const nextIdx = (currentIndex + 1) % images.length;
    dispatch('change', { index: nextIdx });
  }

  function prev() {
    if (images.length === 0) return;
    const prevIdx = (currentIndex - 1 + images.length) % images.length;
    dispatch('change', { index: prevIdx });
  }

  function handleKeydown(e) {
    if (!isOpen) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowRight') next();
    if (e.key === 'ArrowLeft') prev();
  }

  function handleTouchStart(e) {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
  }

  function handleTouchEnd(e) {
    touchEndX = e.changedTouches[0].screenX;
    touchEndY = e.changedTouches[0].screenY;
    handleGesture();
  }

  function handleGesture() {
    const diffX = touchEndX - touchStartX;
    const diffY = touchEndY - touchStartY;

    // Horizontal swipe (next / prev)
    if (Math.abs(diffX) > 45 && Math.abs(diffX) > Math.abs(diffY)) {
      if (diffX < 0) {
        next();
      } else {
        prev();
      }
    } 
    // Vertical swipe down (pull down to close)
    else if (diffY > 80 && Math.abs(diffY) > Math.abs(diffX) * 1.5) {
      close();
    }
  }

  function onImageLoad() {
    isImageLoading = false;
  }
</script>

<svelte:window on:keydown={handleKeydown} />

{#if isOpen && currentImg}
  <div 
    class="lightbox-backdrop" 
    role="dialog" 
    aria-modal="true" 
    aria-label="Prohlížeč fotografií"
  >
    <!-- Background dismiss area -->
    <button 
      type="button" 
      class="backdrop-dismiss" 
      on:click={close} 
      aria-label="Zavřít detail fotky"
    ></button>

    <!-- Top header with counter and close button -->
    <div class="lightbox-header">
      <div class="header-info">
        {#if categoryName}
          <span class="category-tag">{categoryName}</span>
        {/if}
        <span class="counter">{currentIndex + 1} / {images.length}</span>
      </div>
      <button 
        type="button" 
        class="close-btn" 
        on:click={close} 
        aria-label="Zavřít prohlížeč"
      >
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    </div>

    <!-- Main image stage with touch listeners -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div 
      class="lightbox-stage"
      on:touchstart={handleTouchStart}
      on:touchend={handleTouchEnd}
    >
      <!-- Previous button -->
      <button 
        type="button" 
        class="nav-btn prev" 
        on:click={prev} 
        aria-label="Předchozí fotografie"
      >
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>

      <!-- Center image container -->
      <div class="image-wrapper">
        {#if isImageLoading}
          <div class="spinner-container" aria-hidden="true">
            <div class="spinner"></div>
          </div>
        {/if}
        <img 
          src={currentImg.src} 
          alt={currentImg.alt || "Fotografie Nicol Juráňová"} 
          class="lightbox-img" 
          class:loaded={!isImageLoading}
          on:load={onImageLoad}
        />
        {#if currentImg.alt && currentImg.alt !== "Portrét"}
          <p class="caption">{currentImg.alt}</p>
        {/if}
      </div>

      <!-- Next button -->
      <button 
        type="button" 
        class="nav-btn next" 
        on:click={next} 
        aria-label="Další fotografie"
      >
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>
    </div>

    <!-- Mobile swipe indicator hint -->
    <div class="mobile-hint" aria-hidden="true">
      <span>← Potažením přepínejte fotky →</span>
    </div>
  </div>
{/if}

<style>
  .lightbox-backdrop {
    position: fixed;
    inset: 0;
    z-index: 20000;
    background-color: rgba(5, 5, 5, 0.96);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    animation: fadeIn 0.25s ease-out;
  }

  .backdrop-dismiss {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    cursor: default;
    z-index: 1;
  }

  .lightbox-header {
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.25rem 2rem;
    color: #ffffff;
  }

  .header-info {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .category-tag {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: #c9a87c;
    font-weight: 500;
  }

  .counter {
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.6);
    font-variant-numeric: tabular-nums;
  }

  .close-btn {
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 50%;
    color: #ffffff;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .close-btn:hover {
    background-color: #c9a87c;
    color: #0a0a0a;
    border-color: #c9a87c;
    transform: scale(1.05);
  }

  .lightbox-stage {
    position: relative;
    z-index: 2;
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1.5rem;
    overflow: hidden;
    user-select: none;
    -webkit-user-select: none;
  }

  .nav-btn {
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(20, 20, 20, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 50%;
    color: #ffffff;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    flex-shrink: 0;
    z-index: 3;
  }

  .nav-btn:hover {
    background-color: #c9a87c;
    color: #0a0a0a;
    border-color: #c9a87c;
    transform: scale(1.08);
  }

  .image-wrapper {
    position: relative;
    max-width: 85vw;
    max-height: 82vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
    z-index: 2;
  }

  .lightbox-img {
    max-width: 100%;
    max-height: 78vh;
    object-fit: contain;
    border-radius: 4px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
    opacity: 0;
    transition: opacity 0.25s ease-in-out, transform 0.25s ease;
  }

  .lightbox-img.loaded {
    opacity: 1;
  }

  .caption {
    margin-top: 0.75rem;
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.75);
    text-align: center;
    font-weight: 300;
  }

  .spinner-container {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .spinner {
    width: 38px;
    height: 38px;
    border: 3px solid rgba(255, 255, 255, 0.1);
    border-top-color: #c9a87c;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }

  .mobile-hint {
    position: relative;
    z-index: 2;
    text-align: center;
    padding: 0.85rem 1rem;
    font-size: 0.75rem;
    color: rgba(255, 255, 255, 0.4);
    letter-spacing: 0.05em;
    display: none;
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  @media (max-width: 768px) {
    .lightbox-header {
      padding: 1rem 1.25rem;
    }

    .lightbox-stage {
      padding: 0 0.5rem;
    }

    .nav-btn {
      width: 40px;
      height: 40px;
      background-color: rgba(10, 10, 10, 0.6);
    }

    .image-wrapper {
      max-width: 96vw;
      max-height: 80vh;
    }

    .lightbox-img {
      max-height: 72vh;
    }

    .mobile-hint {
      display: block;
    }
  }
</style>
