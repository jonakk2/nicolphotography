<script>
  // Reusable Hero Auto-Slider for Nicol Juráňová Photography
  export let speed = 52; // Seconds per full marquee cycle

  const sliderImages = [
    { src: '/images/slider/IMG_0185.webp', alt: 'Přirozené rodinné a párové focení v přírodě' },
    { src: '/images/slider/IMG_1012.webp', alt: 'Autentické portréty s přirozeným světlem' },
    { src: '/images/slider/IMG_1324.webp', alt: 'Příběh a emoce zachycené v krajině' },
    { src: '/images/slider/IMG_5037.webp', alt: 'Uvolněná atmosféra při venkovním focení' },
    { src: '/images/slider/IMG_8256.webp', alt: 'Párové focení při západu slunce' },
    { src: '/images/slider/IMG_8999.webp', alt: 'Krásné okamžiky uprostřed přírody' },
    { src: '/images/slider/IMG_9363.webp', alt: 'Rodinné vzpomínky, které vydrží navždy' }
  ];
</script>

<div class="hero-slider-container" style="--slider-speed: {speed}s;" aria-hidden="true">
  <!-- Track 1 -->
  <div class="hero-slider-track">
    {#each sliderImages as img}
      <div class="hero-slider-slide">
        <img src={img.src} alt={img.alt} loading="eager" decoding="async" />
      </div>
    {/each}
  </div>

  <!-- Track 2 (Seamless loop twin) -->
  <div class="hero-slider-track" aria-hidden="true">
    {#each sliderImages as img}
      <div class="hero-slider-slide">
        <img src={img.src} alt={img.alt} loading="eager" decoding="async" />
      </div>
    {/each}
  </div>
</div>

<style>
  .hero-slider-container {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    display: flex;
    pointer-events: auto;
    z-index: 0;
    -webkit-mask-image: linear-gradient(to right, transparent 0%, black 10%, black 90%, transparent 100%);
    mask-image: linear-gradient(to right, transparent 0%, black 10%, black 90%, transparent 100%);
  }

  .hero-slider-track {
    display: flex;
    flex-shrink: 0;
    width: max-content;
    height: 100%;
    animation: heroMarquee var(--slider-speed, 52s) linear infinite;
    will-change: transform;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    transform: translate3d(0, 0, 0);
  }

  .hero-slider-container:hover .hero-slider-track {
    animation-play-state: paused;
  }

  @keyframes heroMarquee {
    0% {
      transform: translate3d(0, 0, 0);
    }
    100% {
      transform: translate3d(-100%, 0, 0);
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .hero-slider-track {
      animation: none;
    }
  }

  .hero-slider-slide {
    flex: 0 0 520px;
    width: 520px;
    height: 100%;
    margin-right: 18px;
    position: relative;
    overflow: hidden;
    border-radius: 4px;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    transform: translateZ(0);
  }

  @media (min-width: 1200px) {
    .hero-slider-slide {
      flex: 0 0 650px;
      width: 650px;
      margin-right: 22px;
    }
  }

  @media (max-width: 768px) {
    .hero-slider-slide {
      flex: 0 0 350px;
      width: 350px;
      margin-right: 12px;
    }
  }

  .hero-slider-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    display: block;
    filter: brightness(0.8) contrast(1.05);
    pointer-events: none;
    user-select: none;
    -webkit-user-select: none;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    transform: translateZ(0);
  }
</style>
