<script>
  let name = '';
  let email = '';
  let phone = '';
  let service = '';
  let message = '';
  let successMessage = '';
  let errorMessage = '';
  let isSubmitting = false;

  const services = [
    'Portrétní focení',
    'Rodinné focení',
    'Párové focení',
    'Focení s domácími mazlíčky',
    'Jiné'
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
          subject: `Nová zpráva z webu od ${name}`,
          from_name: name,
          email: email,
          phone: phone || 'Neuvedeno',
          service: service || 'Neuvedeno',
          message: message,
          botcheck: ''
        })
      });

      const data = await response.json();

      if (data.success) {
        successMessage = 'Zpráva byla úspěšně odeslána! Ozvu se vám co nejdříve.';
        name = '';
        email = '';
        phone = '';
        service = '';
        message = '';
      } else {
        throw new Error(data.message);
      }
    } catch (err) {
      console.error('Failed to send:', err);
      errorMessage = 'Nepodařilo se odeslat zprávu. Zkuste to prosím znovu nebo mě kontaktujte přímo.';
    } finally {
      isSubmitting = false;
    }
  };
</script>

<form on:submit={sendEmail} class="contact-form">
  <h2>Napište mi</h2>
  <p class="form-subtitle">Vyplňte formulář a já se vám co nejdříve ozvu</p>

  <div class="form-row">
    <div class="form-group">
      <label for="name">Jméno *</label>
      <input
        type="text"
        id="name"
        bind:value={name}
        placeholder="Vaše jméno"
        required
      />
    </div>
    <div class="form-group">
      <label for="email">Email *</label>
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
      <label for="phone">Telefon</label>
      <input
        type="tel"
        id="phone"
        bind:value={phone}
        placeholder="+420 xxx xxx xxx"
      />
    </div>
    <div class="form-group">
      <label for="service">Typ focení</label>
      <select id="service" bind:value={service}>
        <option value="">Vyberte službu</option>
        {#each services as serviceOption}
          <option value={serviceOption}>{serviceOption}</option>
        {/each}
      </select>
    </div>
  </div>

  <div class="form-group">
    <label for="message">Zpráva *</label>
    <textarea
      id="message"
      bind:value={message}
      placeholder="Popište svou představu o focení, termín, místo..."
      rows="5"
      required
    ></textarea>
  </div>

  <input type="checkbox" name="botcheck" class="hidden" style="display: none;">

  <button type="submit" class="btn submit-btn" disabled={isSubmitting}>
    {#if isSubmitting}
      Odesílám...
    {:else}
      Odeslat zprávu
    {/if}
  </button>

  {#if successMessage}
    <div class="alert alert-success">{successMessage}</div>
  {/if}

  {#if errorMessage}
    <div class="alert alert-error">{errorMessage}</div>
  {/if}
</form>

<style>
  .contact-form {
    width: 100%;
  }

  .contact-form h2 {
    margin-bottom: 0.5rem;
    font-size: 1.75rem;
  }

  .form-subtitle {
    color: var(--color-muted);
    margin-bottom: 2rem;
    font-size: 0.95rem;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .form-group {
    margin-bottom: 1rem;
  }

  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    font-size: 0.9rem;
    color: var(--color-dark);
  }

  .form-group input,
  .form-group select,
  .form-group textarea {
    width: 100%;
    padding: 0.875rem 1rem;
    border: 2px solid #e5e5e5;
    border-radius: 8px;
    font-size: 1rem;
    font-family: inherit;
    background-color: white;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
  }

  .form-group input:focus,
  .form-group select:focus,
  .form-group textarea:focus {
    outline: none;
    border-color: var(--color-secondary);
    box-shadow: 0 0 0 3px rgba(212, 165, 116, 0.1);
  }

  .form-group input::placeholder,
  .form-group textarea::placeholder {
    color: #999;
  }

  .form-group select {
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23666' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 1rem center;
    padding-right: 2.5rem;
  }

  .form-group textarea {
    resize: vertical;
    min-height: 120px;
  }

  .submit-btn {
    width: 100%;
    padding: 1rem;
    font-size: 1rem;
    margin-top: 1rem;
  }

  .submit-btn:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }

  .alert {
    padding: 1rem;
    border-radius: 8px;
    margin-top: 1.5rem;
    text-align: center;
    font-weight: 500;
  }

  .alert-success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
  }

  .alert-error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
  }

  @media (max-width: 576px) {
    .form-row {
      grid-template-columns: 1fr;
    }
  }
</style>
