<script>
  import { goto } from '$app/navigation';
  import { api } from '$lib/api';

  let email = '';
  let password = '';
  let error = '';

  async function handleLogin() {
    error = '';
    try {
      const res = await api.post('/login', { email, password });
      const data = res.data;

      localStorage.setItem('access_token', data.access_token);
      goto('/dashboard');
    }
    catch (err) { if (err.response) {
        error = err.response.data.error || 'Login failed';
      }
      else { error = 'Network error'; }
    }
  }
</script>

<form on:submit|preventDefault={handleLogin}>
  <input type="email" bind:value={email} placeholder="Email" required />
  <input type="password" bind:value={password} placeholder="Password" required />
  <button type="submit">Login</button>
  {#if error}<p>{error}</p>{/if}
</form>
