<script>
  let name = '';
  let email = '';
  let phone = '';
  let service = '';
  let timeframe = '';
  let locationPref = '';
  let message = '';
  let successMessage = '';
  let errorMessage = '';
  let isSubmitting = false;

  const services = [
    'Portrétní focení',
    'Rodinné focení',
    'Párové focení',
    'Focení s domácími mazlíčky',
    'Jiné přání'
  ];

  const timeframes = [
    'Co nejdříve',
    'V příštích 2-4 týdnech',
    'Jaro / Léto',
    'Podzimní focení',
    'Zimní / Vánoční focení',
    'Zatím nezávazně plánuji'
  ];

  const locations = [
    'Okolí Hranic na Moravě',
    'Olomouc a okolí',
    'Mám vlastní tip / u nás doma',
    'Rád/a si nechám doporučit hezké místo'
  ];

  const sendEmail = async (e) => {
    e.preventDefault();
    isSubmitting = true;
    errorMessage = '';
    successMessage = '';

    try {
      const response = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          access_key: '457c855c-6bc1-49a9-a26d-b2212ad21ed2',
          subject: `Nová poptávka focení: ${name} (${service || 'Obecná'})`,
          from_name: name,
          email: email,
          phone: phone || 'Neuvedeno',
          service: service || 'Neuvedeno',
          timeframe: timeframe || 'Neuvedeno',
          location: locationPref || 'Neuvedeno',
          message: message,
          botcheck: ''
        })
      });

      const data = await response.json();

      if (data.success) {
        successMessage = 'Děkuji za zprávu! Ozvu se vám co nejdříve (obvykle do 24 hodin), abychom doladili detaily.';
        name = '';
        email = '';
        phone = '';
        service = '';
        timeframe = '';
        locationPref = '';
        message = '';
      } else {
        throw new Error(data.message);
      }
    } catch (err) {
      console.error('Failed to send:', err);
      errorMessage = 'Nepodařilo se odeslat zprávu. Zkuste to prosím znovu nebo mi napište přímo na njuranova2003@gmail.com.';
    } finally {
      isSubmitting = false;
    }
  };
</script>

<form on:submit={sendEmail} class="contact-form">
  <h2>Napište mi</h2>
  <p class="form-subtitle">Vyplňte krátký formulář a společně naplánujeme vaše focení</p>

  <div class="form-row">
    <div class="form-group">
      <label for="name">Jméno a příjmení *</label>
      <input
        type="text"
        id="name"
        bind:value={name}
        placeholder="Vaše jméno"
        required
      />
    </div>
    <div class="form-group">
      <label for="email">E-mail *</label>
      <input
        type="email"
        id="email"
        bind:value={email}
        placeholder="vas@email.cz"
        required
      />
    </div>
  </div>

  <div class="form-row">
    <div class="form-group">
      <label for="phone">Telefonní číslo</label>
      <input
        type="tel"
        id="phone"
        bind:value={phone}
        placeholder="+420 xxx xxx xxx"
      />
    </div>
    <div class="form-group">
      <label for="service">O jaké focení máte zájem?</label>
      <select id="service" bind:value={service}>
        <option value="">Vyberte typ focení</option>
        {#each services as serviceOption}
          <option value={serviceOption}>{serviceOption}</option>
        {/each}
      </select>
    </div>
  </div>

  <div class="form-row">
    <div class="form-group">
      <label for="timeframe">Přibližný termín / období</label>
      <select id="timeframe" bind:value={timeframe}>
        <option value="">Kdy byste chtěli fotit?</option>
        {#each timeframes as tf}
          <option value={tf}>{tf}</option>
        {/each}
      </select>
    </div>
    <div class="form-group">
      <label for="location">Preferované místo</label>
      <select id="location" bind:value={locationPref}>
        <option value="">Kde byste chtěli fotit?</option>
        {#each locations as loc}
          <option value={loc}>{loc}</option>
        {/each}
      </select>
    </div>
  </div>

  <div class="form-group">
    <label for="message">Vaše představa a dotazy *</label>
    <textarea
      id="message"
      bind:value={message}
      placeholder="Napište mi cokoliv o vašem nápadu — počet osob, pejska, specifické přání nebo termíny..."
      rows="4"
      required
    ></textarea>
  </div>

  <input type="checkbox" name="botcheck" class="hidden" style="display: none;">

  <button type="submit" class="btn submit-btn" disabled={isSubmitting}>
    {#if isSubmitting}
      Odesílám zprávu...
    {:else}
      Odeslat nezávaznou poptávku
    {/if}
  </button>

  {#if successMessage}
    <div class="alert alert-success">
      <span class="alert-icon">✓</span>
      <p>{successMessage}</p>
    </div>
  {/if}

  {#if errorMessage}
    <div class="alert alert-error">
      <p>{errorMessage}</p>
    </div>
  {/if}
</form>

<style>
  .contact-form {
    width: 100%;
  }

  .contact-form h2 {
    margin-bottom: 0.5rem;
    font-size: 1.85rem;
    font-weight: 500;
  }

  .form-subtitle {
    color: #888888;
    margin-bottom: 2rem;
    font-size: 0.95rem;
    line-height: 1.5;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.25rem;
    margin-bottom: 1rem;
  }

  .form-group {
    margin-bottom: 1.25rem;
  }

  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    font-size: 0.88rem;
    letter-spacing: 0.02em;
    color: #cccccc;
  }

  .form-group input,
  .form-group select,
  .form-group textarea {
    width: 100%;
    padding: 0.85rem 1.1rem;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 6px;
    font-size: 0.95rem;
    font-family: inherit;
    background-color: #0d0d0d;
    color: #ffffff;
    transition: all 0.25s ease;
  }

  .form-group input:focus,
  .form-group select:focus,
  .form-group textarea:focus {
    outline: none;
    border-color: #c9a87c;
    box-shadow: 0 0 0 3px rgba(201, 168, 124, 0.15);
  }

  .form-group input::placeholder,
  .form-group textarea::placeholder {
    color: #666666;
  }

  .form-group select {
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23c9a87c' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 1rem center;
    padding-right: 2.5rem;
  }

  .form-group textarea {
    resize: vertical;
    min-height: 110px;
  }

  .submit-btn {
    width: 100%;
    padding: 1rem;
    font-size: 0.95rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    margin-top: 0.5rem;
    background-color: #c9a87c;
    color: #0a0a0a;
    border: none;
    border-radius: 9999px;
    cursor: pointer;
    transition: all 0.25s ease;
  }

  .submit-btn:hover:not(:disabled) {
    background-color: #dfc299;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(201, 168, 124, 0.35);
  }

  .submit-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  .alert {
    padding: 1.25rem 1.5rem;
    border-radius: 8px;
    margin-top: 1.5rem;
    text-align: left;
    display: flex;
    align-items: center;
    gap: 1rem;
    line-height: 1.5;
  }

  .alert p {
    margin: 0;
    font-size: 0.92rem;
  }

  .alert-icon {
    font-size: 1.25rem;
    font-weight: bold;
  }

  .alert-success {
    background-color: rgba(34, 197, 94, 0.1);
    color: #4ade80;
    border: 1px solid rgba(74, 222, 128, 0.3);
  }

  .alert-error {
    background-color: rgba(239, 68, 68, 0.1);
    color: #f87171;
    border: 1px solid rgba(248, 113, 113, 0.3);
  }

  @media (max-width: 640px) {
    .form-row {
      grid-template-columns: 1fr;
      gap: 0;
    }
  }
</style>
