<script>
  export let beforeImage = '/images/portfolio/golden-hour.png';
  export let afterImage = '/images/portfolio/golden-hour.png';
  export let beforeLabel = 'Původní záběr z foťáku';
  export let afterLabel = 'Upravená fotografie';

  let sliderPosition = 50; // percentage
  let isDragging = false;
  let containerRef;

  function updateSlider(clientX) {
    if (!containerRef) return;
    const rect = containerRef.getBoundingClientRect();
    const x = clientX - rect.left;
    let pos = (x / rect.width) * 100;
    if (pos < 5) pos = 5;
    if (pos > 95) pos = 95;
    sliderPosition = pos;
  }

  function handleMouseDown(e) {
    isDragging = true;
    updateSlider(e.clientX);
  }

  function handleMouseMove(e) {
    if (!isDragging) return;
    updateSlider(e.clientX);
  }

  function handleMouseUp() {
    isDragging = false;
  }

  function handleTouchStart(e) {
    isDragging = true;
    updateSlider(e.touches[0].clientX);
  }

  function handleTouchMove(e) {
    if (!isDragging) return;
    updateSlider(e.touches[0].clientX);
  }

  function handleTouchEnd() {
    isDragging = false;
  }

  function handleKeyDown(e) {
    if (e.key === 'ArrowLeft') {
      sliderPosition = Math.max(5, sliderPosition - 5);
    } else if (e.key === 'ArrowRight') {
      sliderPosition = Math.min(95, sliderPosition + 5);
    }
  }
</script>

<svelte:window 
  on:mousemove={handleMouseMove} 
  on:mouseup={handleMouseUp}
  on:touchmove={handleTouchMove}
  on:touchend={handleTouchEnd}
/>

<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div 
  class="before-after-container" 
  bind:this={containerRef}
  on:mousedown={handleMouseDown}
  on:touchstart={handleTouchStart}
  role="region"
  aria-label="Porovnání před a po úpravě fotografie"
>
  <!-- After Image (Full background) -->
  <img src={afterImage} alt="Upravená fotografie" class="image-after" loading="lazy" />
  <span class="badge badge-after">{afterLabel}</span>

  <!-- Before Image (Clipped overlay) -->
  <div class="image-before-wrapper" style="width: {sliderPosition}%;">
    <img 
      src={beforeImage} 
      alt="Původní záběr z foťáku" 
      class="image-before" 
      loading="lazy" 
    />
    <span class="badge badge-before">{beforeLabel}</span>
  </div>

  <!-- Divider Line & Handle -->
  <div 
    class="slider-handle" 
    style="left: {sliderPosition}%;"
    tabindex="0"
    role="slider"
    aria-valuenow={Math.round(sliderPosition)}
    aria-valuemin="5"
    aria-valuemax="95"
    aria-label="Posuvník pro porovnání úpravy"
    on:keydown={handleKeyDown}
  >
    <div class="handle-line"></div>
    <div class="handle-circle">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <polyline points="8 16 4 12 8 8"></polyline>
        <polyline points="16 8 20 12 16 16"></polyline>
      </svg>
    </div>
  </div>
</div>

<style>
  .before-after-container {
    position: relative;
    width: 100%;
    max-width: 900px;
    height: 520px;
    margin: 0 auto;
    overflow: hidden;
    border-radius: 8px;
    border: 1px solid rgba(201, 168, 124, 0.25);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.7);
    cursor: ew-resize;
    user-select: none;
    -webkit-user-select: none;
    background-color: #0d0d0d;
  }

  .image-after {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    pointer-events: none;
  }

  .image-before-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    overflow: hidden;
    pointer-events: none;
    z-index: 2;
  }

  .image-before {
    position: absolute;
    top: 0;
    left: 0;
    width: 900px;
    max-width: none;
    height: 100%;
    object-fit: cover;
    pointer-events: none;
    /* Simulate flat RAW camera profile */
    filter: contrast(0.85) brightness(1.08) saturate(0.72) sepia(0.08);
  }

  .badge {
    position: absolute;
    top: 1.25rem;
    z-index: 5;
    background: rgba(10, 10, 10, 0.75);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #ffffff;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    padding: 0.4rem 0.85rem;
    border-radius: 9999px;
    pointer-events: none;
  }

  .badge-before {
    left: 1.25rem;
  }

  .badge-after {
    right: 1.25rem;
    color: #c9a87c;
    border-color: rgba(201, 168, 124, 0.4);
  }

  .slider-handle {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 40px;
    margin-left: -20px;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: ew-resize;
    outline: none;
  }

  .handle-line {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 2px;
    background-color: #ffffff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.8);
  }

  .handle-circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #c9a87c;
    color: #0a0a0a;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    transition: transform 0.15s ease, background-color 0.15s ease;
    border: 2px solid #ffffff;
  }

  .slider-handle:hover .handle-circle,
  .slider-handle:focus-visible .handle-circle {
    transform: scale(1.1);
    background-color: #dfc299;
  }

  @media (max-width: 768px) {
    .before-after-container {
      height: 380px;
    }

    .image-before {
      width: 100vw;
    }

    .badge {
      font-size: 0.7rem;
      padding: 0.35rem 0.65rem;
      top: 0.75rem;
    }

    .badge-before {
      left: 0.75rem;
    }

    .badge-after {
      right: 0.75rem;
    }
  }
</style>
