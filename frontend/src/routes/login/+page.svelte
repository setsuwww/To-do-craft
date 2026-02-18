<script>
  import '../../app.css'
  import { goto } from '$app/navigation';
  import { api } from '$lib/api';

  let email = '';
  let password = '';
  let error = '';
  let loading = false;

  async function handleLogin() {
    error = '';
    loading = true;

    try {
      const res = await api.post('/login', { email, password });
      localStorage.setItem('access_token', res.data.access_token);
      goto('/dashboard');
    } catch (err) {
      if (err.response) {
        error = err.response.data.error || 'Login failed';
      } else {
        error = 'Network error';
      }
    } finally {
      loading = false;
    }
  }
</script>

<div class="min-h-screen flex items-center justify-center bg-gray-100">
  <div class="bg-white w-full max-w-md p-8 rounded-xl shadow-sm border border-gray-200">

    <h1 class="text-2xl font-semibold text-gray-800 mb-6 text-center">
      Sign In
    </h1>

    <form on:submit|preventDefault={handleLogin} class="space-y-4">

      <div>
        <label for="email" class="block text-sm text-gray-600 mb-1">Email</label>
        <input
          type="email"
          bind:value={email}
          placeholder="example@email.com"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400 focus:outline-none"
        />
      </div>

      <div>
        <label for="password" class="block text-sm text-gray-600 mb-1">Password</label>
        <input
          type="password"
          bind:value={password}
          placeholder="••••••••"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400 focus:outline-none"
        />
      </div>

      {#if error}
        <p class="text-sm text-red-500">{error}</p>
      {/if}

      <button
        type="submit"
        disabled={loading}
        class="w-full py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600 transition disabled:opacity-60"
      >
        {loading ? 'Signing in...' : 'Login'}
      </button>

    </form>
  </div>
</div>
