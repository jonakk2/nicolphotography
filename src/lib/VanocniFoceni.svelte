<script>
  import { onMount } from 'svelte';
  import NavBar from './NavBar.svelte';
  import Footer from './Footer.svelte';

  // Available days for Christmas mini-sessions
  const days = [
    { date: '2026-11-14', label: 'Sobota 14. 11.', spots: 'Volné termíny' }
  ];

  // Daily time slots (30 min sessions + 15 min buffer)
  const slotTimes = [
    '09:30'
  ];

  let selectedDay = days[0];
  let selectedSlot = null;

  let customerName = '';
  let customerPhone = '';
  let customerEmail = '';
  let customerNote = '';

  let bookedSlots = [];
  let isLoadingSlots = false;
  let isSubmitting = false;
  let bookingSuccess = false;
  let bookingResult = null;
  let bookingError = '';

  const crmSlotsUrl = import.meta.env.VITE_CRM_SLOTS_URL || 'http://localhost:8092/api/v1/PhotoInquiry/slots?serviceType=vanocni';
  const crmApiUrl = import.meta.env.VITE_CRM_API_URL || 'http://localhost:8092/api/v1/PhotoInquiry/create';

  onMount(async () => {
    await fetchBookedSlots();
  });

  async function fetchBookedSlots() {
    isLoadingSlots = true;
    try {
      const res = await fetch(crmSlotsUrl);
      if (res.ok) {
        const data = await res.json();
        if (data.bookedSlots) {
          bookedSlots = data.bookedSlots;
        }
      }
    } catch (e) {
      console.warn('Nepodařilo se načíst obsazené sloty z CRM:', e);
    } finally {
      isLoadingSlots = false;
    }
  }

  function isSlotBooked(dayDate, time) {
    const key = `${dayDate} ${time}`;
    return bookedSlots.some(s => s.startsWith(key));
  }

  function selectSlot(time) {
    if (isSlotBooked(selectedDay.date, time)) return;
    selectedSlot = time;
    bookingError = '';
    // Smooth scroll to form on mobile
    if (typeof window !== 'undefined' && window.innerWidth < 768) {
      setTimeout(() => {
        const formEl = document.getElementById('booking-form-box');
        if (formEl) formEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }, 50);
    }
  }

  async function handleBookingSubmit(e) {
    e.preventDefault();
    if (!selectedSlot) {
      bookingError = 'Vyberte si prosím časový termín focení.';
      return;
    }

    isSubmitting = true;
    bookingError = '';

    const slotDateTime = `${selectedDay.date} ${selectedSlot}:00`;

    const payload = {
      name: customerName,
      phone: customerPhone,
      email: customerEmail,
      service: 'Vánoční focení 2026 – venkovní scenérie',
      serviceType: 'vanocni',
      slotStart: slotDateTime,
      durationMinutes: 30,
      message: customerNote ? `Vánoční focení: ${customerNote}` : 'Rezervace vánočního minifocení z webu.'
    };

    try {
      const res = await fetch(crmApiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      const data = await res.json();
      if (data.success) {
        bookedSlots = [...bookedSlots, `${selectedDay.date} ${selectedSlot}`];
        bookingSuccess = true;
        bookingResult = {
          dayLabel: selectedDay.label,
          time: selectedSlot,
          name: customerName,
          email: customerEmail,
          phone: customerPhone
        };
      } else {
        throw new Error(data.message || 'Chyba při rezervaci termínu.');
      }
    } catch (err) {
      console.warn('CRM nedostupné, odesílám přes Web3Forms zálohu:', err);
      try {
        const fbResponse = await fetch('https://api.web3forms.com/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            access_key: '457c855c-6bc1-49a9-a26d-b2212ad21ed2',
            subject: `🎄 Rezervace Vánočního focení: ${customerName} (${selectedDay.label} v ${selectedSlot})`,
            from_name: customerName,
            email: customerEmail,
            phone: customerPhone,
            message: `Rezervovaný termín: ${selectedDay.label} v ${selectedSlot}\nPoznámka: ${customerNote || 'Žádná'}`
          })
        });

        const fbData = await fbResponse.json();
        if (fbData.success) {
          bookedSlots = [...bookedSlots, `${selectedDay.date} ${selectedSlot}`];
          bookingSuccess = true;
          bookingResult = {
            dayLabel: selectedDay.label,
            time: selectedSlot,
            name: customerName,
            email: customerEmail,
            phone: customerPhone
          };
        } else {
          throw new Error('Nepodařilo se odeslat rezervaci.');
        }
      } catch (fbErr) {
        bookingError = 'Omlouváme se, rezervaci se nepodařilo odeslat. Napište mi prosím přímo na info@nicolphotography.cz nebo zavolejte.';
      }
    } finally {
      isSubmitting = false;
    }
  }

  function resetBooking() {
    bookingSuccess = false;
    selectedSlot = null;
    customerName = '';
    customerPhone = '';
    customerEmail = '';
    customerNote = '';
  }

  // FAQ Accordion
  let openFaq = null;
  function toggleFaq(index) {
    openFaq = openFaq === index ? null : index;
  }

  const faqs = [
    {
      q: 'Co si máme vzít na sebe na vánoční focení?',
      a: 'Doporučuji teplé, přírodní a neutrální tóny – krémovou, béžovou, hnědou, tmavě zelenou nebo decentní vínovou/bordó. Skvěle vypadají pletené svetry, šály či flanelové košile. Prosím vyvarujte se velkým nápisům, logům a křiklavým neonovým barvám, které odvádějí pozornost z vašich tváří.'
    },
    {
      q: 'Můžeme s sebou vzít pejska?',
      a: 'Určitě ano! Venku v přírodě se pejsci cítí uvolněně a přirozeně. Určitě ho vezměte s sebou, jen mi to prosím předem připište do poznámky v rezervaci.'
    },
    {
      q: 'Kdy a jak obdržíme hotové fotografie?',
      a: 'Do 48 hodin od focení vám pošlu odkaz na soukromou online galerii s neupravenými náhledy, kde si v klidu domova vyberete svých 8 oblíbených fotografií. Hotové, pečlivě vyretušované snímky vám předám do 14 dnů od vašeho výběru – spolehlivě včas pod stromeček!'
    },
    {
      q: 'Jak funguje záloha a storno termínu?',
      a: 'Rezervační poplatek činí 500 Kč a hradí se převodem po potvrzení termínu. Zbývajících 1 000 Kč se doplácí v hotovosti nebo přes QR kód v den focení. Pokud by někdo z rodiny onemocněl, po včasné dohodě ráda najdu náhradní termín.'
    }
  ];
</script>

<svelte:head>
  <title>Vánoční focení 2026 – venkovní scenérie | Nicol Juráňová photography</title>
  <meta name="description" content="Rezervujte si svůj termín pro vánoční focení 2026 v kouzelné přírodě Olomouckého kraje. Pohodová sváteční atmosféra na čerstvém vzduchu, 8 fotek do 14 dnů pod stromeček." />
  <link rel="canonical" href="https://nicolphotography.cz/vanocni-foceni" />
</svelte:head>

<div class="xmas-page">
  <NavBar forceScrolled={true} />

  <!-- Hero Header -->
  <section class="xmas-hero">
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <span class="xmas-badge">✨ Limitovaná sezónní nabídka 2026</span>
      <h1>Vánoční focení 2026 – venkovní scenérie</h1>
      <p class="hero-subtitle">
        Zastavte se na chvíli v předvánočním shonu. Přijďte si pro společné vzpomínky na čerstvý vzduch, voňavý čaj z termosky na zahřátí a přirozené úsměvy v kouzelné scenérii na zahradě před kamenným domem.
      </p>
      <div class="hero-highlights">
        <div class="hl-item">
          <span class="hl-icon">⏱️</span>
          <span><strong>30 minut</strong> pohodového focení</span>
        </div>
        <div class="hl-item">
          <span class="hl-icon">📸</span>
          <span><strong>8 fotografií</strong> v plném rozlišení</span>
        </div>
        <div class="hl-item">
          <span class="hl-icon">🎁</span>
          <span><strong>Garance do Vánoc</strong> (do 14 dnů)</span>
        </div>
        <div class="hl-item">
          <span class="hl-icon">🏷️</span>
          <span><strong>1 500 Kč</strong> (záloha 500 Kč)</span>
        </div>
      </div>
      <a href="#booking-section" class="btn btn-gold">Vybrat termín & rezervovat online</a>
    </div>
  </section>

  <!-- Package Details -->
  <section class="details-section">
    <div class="container">
      <div class="section-title">
        <span class="sub">Co vás čeká</span>
        <h2>Kouzlo Vánoc bez nucených póz</h2>
        <p>Vánoční focení na zahradě je navrženo tak, aby bylo svižné, nenáročné a plné radosti pro celou rodinu.</p>
      </div>

      <div class="cards-grid">
        <div class="card">
          <div class="card-icon">🏡</div>
          <h3>Vánoční scéna na zahradě</h3>
          <p>Kouzelná venkovní scéna na zahradě před kamenným domem. Teplé vlněné deky, sváteční lucernička, jemná světýlka a vůně jehličí. Žádné umělé ateliérové pozadí, ale autentická severská atmosféra.</p>
        </div>
        <div class="card">
          <div class="card-icon">☕</div>
          <h3>Pohoda pro děti i pejsky</h3>
          <p>Půlhodinka na čerstvém vzduchu je ideální délka, aby děti neztratily pozornost a tatínci nebyli unavení. Čeká na vás teplý čaj z termosky, drobné cukroví a volnost pro pejsky.</p>
        </div>
        <div class="card">
          <div class="card-icon">🖼️</div>
          <h3>Pohodlný online výběr</h3>
          <p>Sami si v teple domova v klidu vyberete svých 8 nejoblíbenějších záběrů. Upravené fotografie v plném rozlišení obdržíte v soukromé online galerii do 14 dnů – spolehlivě včas pod stromeček.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Booking Section -->
  <section id="booking-section" class="booking-section">
    <div class="container">
      <div class="section-title">
        <span class="sub">Online rezervace</span>
        <h2>Vyberte si svůj volný termín</h2>
        <p>Klikněte na preferovaný den a vyberte volný časový slot. Termín se po vyplnění ihned zarezervuje v kalendáři.</p>
      </div>

      {#if bookingSuccess}
        <!-- Success State -->
        <div class="success-box">
          <div class="success-icon">🎄</div>
          <h2>Termín máte zarezervovaný!</h2>
          <p class="success-sub">Děkuji za vaši rezervaci. Záznam byl úspěšně vytvořen v mém kalendáři.</p>
          
          <div class="summary-card">
            <div class="sum-row">
              <span>Termín:</span>
              <strong>{bookingResult.dayLabel}, {bookingResult.time}</strong>
            </div>
            <div class="sum-row">
              <span>Místo:</span>
              <span>Zahrada před kamenným domem (přesnou adresu pošlu v potvrzení)</span>
            </div>
            <div class="sum-row">
              <span>Balíček:</span>
              <span>Vánoční focení 2026 – venkovní scenérie (8 upravených fotografií)</span>
            </div>
            <div class="sum-row">
              <span>Cena / Záloha:</span>
              <span>1 500 Kč (rezervační záloha 500 Kč)</span>
            </div>
            <div class="sum-row">
              <span>Kontakt:</span>
              <span>{bookingResult.name} ({bookingResult.phone})</span>
            </div>
          </div>

          <div class="next-steps">
            <h4>Co se stane dál?</h4>
            <p>Do 24 hodin se vám ozvu s podrobnými instrukcemi, informacemi k platbě zálohy (500 Kč) a tipy, jak se na focení obléknout.</p>
          </div>

          <button class="btn btn-outline" on:click={resetBooking}>Rezervovat další termín</button>
        </div>
      {:else}
        <!-- Booking Interface -->
        <div class="booking-wrapper">
          <!-- Step 1: Select Day -->
          <div class="step-card">
            <div class="step-header">
              <span class="step-num">1</span>
              <div>
                <h3>Zvolte si den focení</h3>
                <span class="step-hint">Listopad 2026</span>
              </div>
            </div>

            <div class="days-list">
              {#each days as day}
                <button
                  type="button"
                  class="day-btn"
                  class:active={selectedDay.date === day.date}
                  on:click={() => { selectedDay = day; selectedSlot = null; }}
                >
                  <span class="day-label">{day.label}</span>
                  <span class="day-spots">{day.spots}</span>
                </button>
              {/each}
            </div>
            <p class="single-term-note">
              ✨ <em>Další termíny budou postupně vypisovány podle zájmu.</em>
            </p>
          </div>

          <!-- Step 2: Select Slot & Fill Form -->
          <div class="step-card" id="booking-form-box">
            <div class="step-header">
              <span class="step-num">2</span>
              <div>
                <h3>Časový slot pro {selectedDay.label}</h3>
                <span class="step-hint">Zvolte čas (focení trvá 30 minut)</span>
              </div>
            </div>

            <div class="slots-grid">
              {#each slotTimes as time}
                {@const isBooked = isSlotBooked(selectedDay.date, time)}
                <button
                  type="button"
                  class="slot-btn"
                  class:booked={isBooked}
                  class:selected={selectedSlot === time}
                  disabled={isBooked}
                  on:click={() => selectSlot(time)}
                >
                  <span class="slot-time">{time}</span>
                  <span class="slot-status">{isBooked ? 'Obsazeno' : 'Volno'}</span>
                </button>
              {/each}
            </div>

            <!-- Form -->
            {#if selectedSlot}
              <form class="slot-form" on:submit={handleBookingSubmit}>
                <div class="selected-summary">
                  <span>Vybraný termín:</span>
                  <strong>{selectedDay.label} v {selectedSlot}</strong>
                </div>

                <div class="form-row">
                  <div class="form-group">
                    <label for="c-name">Jméno a příjmení *</label>
                    <input
                      id="c-name"
                      type="text"
                      bind:value={customerName}
                      placeholder="např. Lucie Nováková"
                      required
                    />
                  </div>
                  <div class="form-group">
                    <label for="c-phone">Telefonní číslo *</label>
                    <input
                      id="c-phone"
                      type="tel"
                      bind:value={customerPhone}
                      placeholder="+420 777 000 000"
                      required
                    />
                  </div>
                </div>

                <div class="form-group">
                  <label for="c-email">E-mailová adresa *</label>
                  <input
                    id="c-email"
                    type="email"
                    bind:value={customerEmail}
                    placeholder="lucie@email.cz"
                    required
                  />
                </div>

                <div class="form-group">
                  <label for="c-note">Kdo na focení dorazí? (děti, mazlíčci, poznámka)</label>
                  <textarea
                    id="c-note"
                    bind:value={customerNote}
                    rows="3"
                    placeholder="např. 2 dospělí a 2 děti (4 a 7 let), rádi bychom vzali i jorkšíra..."
                  ></textarea>
                </div>

                {#if bookingError}
                  <div class="error-banner">
                    ⚠️ {bookingError}
                  </div>
                {/if}

                <button type="submit" class="btn btn-gold btn-block" disabled={isSubmitting}>
                  {#if isSubmitting}
                    Ukládám rezervaci...
                  {:else}
                    Závazně rezervovat termín ({selectedSlot})
                  {/if}
                </button>
                <p class="form-disclaimer">
                  🔒 Rezervace je nezávazná do uhrazení rezervačního poplatku 500 Kč. Žádné skryté poplatky.
                </p>
              </form>
            {:else}
              <div class="select-prompt">
                <span class="prompt-icon">👆</span>
                <p>Klikněte prosím výše na jeden ze zelených časových slotů, který vám nejvíce vyhovuje.</p>
              </div>
            {/if}
          </div>
        </div>
      {/if}
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="faq-section">
    <div class="container">
      <div class="section-title">
        <span class="sub">Časté otázky</span>
        <h2>Vše, co potřebujete vědět</h2>
      </div>

      <div class="faq-list">
        {#each faqs as faq, i}
          <div class="faq-item" class:open={openFaq === i}>
            <button class="faq-question" on:click={() => toggleFaq(i)}>
              <span>{faq.q}</span>
              <span class="faq-toggle">{openFaq === i ? '−' : '+'}</span>
            </button>
            {#if openFaq === i}
              <div class="faq-answer">
                <p>{faq.a}</p>
              </div>
            {/if}
          </div>
        {/each}
      </div>
    </div>
  </section>

  <Footer />
</div>

<style>
  .xmas-page {
    background-color: #0d0d0d;
    color: #e5e5e5;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    min-height: 100vh;
  }

  .container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }

  /* Hero */
  .xmas-hero {
    position: relative;
    padding: 9rem 1.5rem 6rem;
    background: radial-gradient(circle at 50% 20%, rgba(192, 57, 43, 0.18) 0%, rgba(10, 10, 10, 0.95) 70%),
                linear-gradient(180deg, #161210 0%, #0d0d0d 100%);
    text-align: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }

  .hero-content {
    max-width: 780px;
    margin: 0 auto;
  }

  .xmas-badge {
    display: inline-block;
    background: rgba(201, 168, 124, 0.15);
    border: 1px solid rgba(201, 168, 124, 0.4);
    color: #e5b982;
    padding: 0.4rem 1.1rem;
    border-radius: 50px;
    font-size: 0.88rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    margin-bottom: 1.5rem;
  }

  .xmas-hero h1 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2.75rem;
    line-height: 1.2;
    color: #f7f7f7;
    margin-bottom: 1.25rem;
  }

  @media (min-width: 768px) {
    .xmas-hero h1 {
      font-size: 3.5rem;
    }
  }

  .hero-subtitle {
    font-size: 1.15rem;
    line-height: 1.7;
    color: #b3b3b3;
    margin-bottom: 2.25rem;
  }

  .hero-highlights {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-bottom: 2.5rem;
    text-align: left;
  }

  @media (min-width: 768px) {
    .hero-highlights {
      grid-template-columns: repeat(4, 1fr);
    }
  }

  .hl-item {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 0.85rem 1rem;
    border-radius: 10px;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 0.92rem;
  }

  .hl-icon {
    font-size: 1.35rem;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.95rem 2rem;
    border-radius: 8px;
    font-weight: 500;
    font-size: 1rem;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.25s ease;
    border: none;
  }

  .btn-gold {
    background: linear-gradient(135deg, #c9a87c 0%, #b89261 100%);
    color: #121212;
    box-shadow: 0 4px 20px rgba(201, 168, 124, 0.35);
  }

  .btn-gold:hover {
    background: linear-gradient(135deg, #d8b88d 0%, #c49e6d 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(201, 168, 124, 0.5);
  }

  .btn-block {
    width: 100%;
  }

  .btn-outline {
    background: transparent;
    border: 1px solid #c9a87c;
    color: #c9a87c;
  }

  .btn-outline:hover {
    background: #c9a87c;
    color: #121212;
  }

  /* Section Titles */
  .section-title {
    text-align: center;
    max-width: 680px;
    margin: 0 auto 3rem;
  }

  .section-title .sub {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: #c9a87c;
    display: block;
    margin-bottom: 0.5rem;
  }

  .section-title h2 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2.25rem;
    color: #f7f7f7;
    margin-bottom: 0.75rem;
  }

  .section-title p {
    color: #a8a8a8;
    line-height: 1.6;
    font-size: 1rem;
  }

  /* Details Section */
  .details-section {
    padding: 5rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  }

  .cards-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  @media (min-width: 768px) {
    .cards-grid {
      grid-template-columns: repeat(3, 1fr);
    }
  }

  .card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    padding: 2rem 1.75rem;
    border-radius: 12px;
    transition: transform 0.3s ease, border-color 0.3s ease;
  }

  .card:hover {
    transform: translateY(-4px);
    border-color: rgba(201, 168, 124, 0.4);
  }

  .card-icon {
    font-size: 2.25rem;
    margin-bottom: 1.25rem;
  }

  .card h3 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.35rem;
    color: #f5f5f5;
    margin-bottom: 0.75rem;
  }

  .card p {
    color: #a0a0a0;
    line-height: 1.6;
    font-size: 0.95rem;
  }

  /* Booking Section */
  .booking-section {
    padding: 5rem 0;
    background: #111010;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  }

  .booking-wrapper {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  @media (min-width: 860px) {
    .booking-wrapper {
      grid-template-columns: 1fr 1.35fr;
    }
  }

  .step-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 1.75rem;
  }

  .step-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.07);
  }

  .step-num {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: #c9a87c;
    color: #121212;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
  }

  .step-header h3 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.25rem;
    color: #f5f5f5;
    margin: 0;
  }

  .step-hint {
    font-size: 0.85rem;
    color: #8c8c8c;
  }

  /* Days List */
  .days-list {
    display: flex;
    flex-direction: column;
    gap: 0.65rem;
  }

  .day-btn {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.95rem 1.15rem;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    color: #ddd;
    cursor: pointer;
    font-size: 0.95rem;
    transition: all 0.2s ease;
    text-align: left;
  }

  .day-btn:hover {
    background: rgba(255, 255, 255, 0.07);
    border-color: rgba(201, 168, 124, 0.3);
  }

  .day-btn.active {
    background: rgba(201, 168, 124, 0.12);
    border-color: #c9a87c;
    color: #fff;
  }

  .day-label {
    font-weight: 500;
  }

  .day-spots {
    font-size: 0.78rem;
    color: #c9a87c;
    background: rgba(201, 168, 124, 0.12);
    padding: 0.2rem 0.55rem;
    border-radius: 20px;
  }

  .single-term-note {
    margin-top: 1rem;
    font-size: 0.85rem;
    color: #8c8c8c;
    line-height: 1.5;
  }

  .single-term-note em {
    color: #b5b5b5;
  }

  /* Slots Grid */
  .slots-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-bottom: 1.75rem;
  }

  .slot-btn {
    min-width: 140px;
    padding: 0.85rem 1.25rem;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 8px;
    color: #fff;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.25rem;
    transition: all 0.2s ease;
  }

  .slot-btn:hover:not(:disabled) {
    border-color: #c9a87c;
    background: rgba(201, 168, 124, 0.08);
  }

  .slot-btn.selected {
    background: #c9a87c;
    border-color: #c9a87c;
    color: #121212;
  }

  .slot-btn.selected .slot-status {
    color: #121212;
  }

  .slot-btn.booked {
    opacity: 0.35;
    background: rgba(255, 255, 255, 0.02);
    border-color: rgba(255, 255, 255, 0.05);
    cursor: not-allowed;
    text-decoration: line-through;
  }

  .slot-time {
    font-size: 1.05rem;
    font-weight: 600;
  }

  .slot-status {
    font-size: 0.72rem;
    color: #2ecc71;
    letter-spacing: 0.03em;
  }

  .slot-btn.booked .slot-status {
    color: #e74c3c;
    text-decoration: none;
  }

  .select-prompt {
    text-align: center;
    padding: 2.5rem 1rem;
    background: rgba(255, 255, 255, 0.02);
    border: 1px dashed rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    color: #8c8c8c;
  }

  .prompt-icon {
    font-size: 2rem;
    display: block;
    margin-bottom: 0.5rem;
  }

  /* Form */
  .slot-form {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(201, 168, 124, 0.35);
    border-radius: 10px;
    padding: 1.5rem;
  }

  .selected-summary {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(201, 168, 124, 0.12);
    padding: 0.75rem 1rem;
    border-radius: 6px;
    margin-bottom: 1.25rem;
    font-size: 0.95rem;
  }

  .selected-summary strong {
    color: #e5b982;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  @media (min-width: 580px) {
    .form-row {
      grid-template-columns: 1fr 1fr;
    }
  }

  .form-group {
    margin-bottom: 1.15rem;
    text-align: left;
  }

  .form-group label {
    display: block;
    font-size: 0.88rem;
    color: #c9a87c;
    margin-bottom: 0.4rem;
  }

  .form-group input,
  .form-group textarea {
    width: 100%;
    background: rgba(0, 0, 0, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 6px;
    padding: 0.75rem 0.9rem;
    color: #fff;
    font-size: 0.95rem;
    transition: border-color 0.2s ease;
    box-sizing: border-box;
  }

  .form-group input:focus,
  .form-group textarea:focus {
    outline: none;
    border-color: #c9a87c;
  }

  .form-disclaimer {
    font-size: 0.78rem;
    color: #777;
    text-align: center;
    margin-top: 0.85rem;
    margin-bottom: 0;
  }

  .error-banner {
    background: rgba(231, 76, 60, 0.15);
    border: 1px solid rgba(231, 76, 60, 0.4);
    color: #ff7675;
    padding: 0.75rem 1rem;
    border-radius: 6px;
    font-size: 0.9rem;
    margin-bottom: 1.15rem;
  }

  /* Success View */
  .success-box {
    max-width: 650px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(201, 168, 124, 0.4);
    border-radius: 14px;
    padding: 2.5rem 2rem;
    text-align: center;
  }

  .success-icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
  }

  .success-box h2 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2rem;
    color: #f7f7f7;
    margin-bottom: 0.5rem;
  }

  .success-sub {
    color: #a8a8a8;
    margin-bottom: 2rem;
  }

  .summary-card {
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 2rem;
    text-align: left;
  }

  .sum-row {
    display: flex;
    justify-content: space-between;
    padding: 0.6rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    font-size: 0.92rem;
  }

  .sum-row:last-child {
    border-bottom: none;
  }

  .sum-row span:first-child {
    color: #8c8c8c;
  }

  .sum-row strong,
  .sum-row span:last-child {
    color: #e5b982;
  }

  .next-steps {
    text-align: left;
    background: rgba(201, 168, 124, 0.08);
    border-left: 3px solid #c9a87c;
    padding: 1rem 1.25rem;
    border-radius: 0 8px 8px 0;
    margin-bottom: 2rem;
  }

  .next-steps h4 {
    margin: 0 0 0.35rem 0;
    color: #f5f5f5;
    font-size: 0.98rem;
  }

  .next-steps p {
    margin: 0;
    color: #b0b0b0;
    font-size: 0.88rem;
    line-height: 1.5;
  }

  /* FAQ */
  .faq-section {
    padding: 5rem 0;
  }

  .faq-list {
    max-width: 780px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
  }

  .faq-item {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 8px;
    overflow: hidden;
    transition: border-color 0.2s ease;
  }

  .faq-item.open {
    border-color: rgba(201, 168, 124, 0.4);
  }

  .faq-question {
    width: 100%;
    padding: 1.25rem 1.5rem;
    background: none;
    border: none;
    color: #f0f0f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    text-align: left;
    font-size: 1.05rem;
    font-weight: 500;
  }

  .faq-toggle {
    font-size: 1.35rem;
    color: #c9a87c;
    margin-left: 1rem;
  }

  .faq-answer {
    padding: 0 1.5rem 1.25rem;
    color: #a8a8a8;
    line-height: 1.6;
    font-size: 0.95rem;
  }
</style>
