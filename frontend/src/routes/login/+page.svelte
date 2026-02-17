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

      // Simpan token di localStorage
      localStorage.setItem('access_token', data.access_token);

      // Redirect ke dashboard
      goto('/dashboard');
    } catch (err) {
      if (err.response) {
        error = err.response.data.error || 'Login failed';
      } else {
        error = 'Network error';
      }
    }
  }
</script>

<div class="min-h-screen flex items-center justify-center bg-orange-100 p-6">
  <form
    class="bg-white p-8 rounded-lg shadow-2xl space-y-5 w-full max-w-sm border-4 border-black"
    on:submit|preventDefault={handleLogin}
  >
    <h1 class="text-3xl font-bold text-center text-gray-800 mb-4 font-mono">Login</h1>

    <!-- Email -->
    <div class="flex flex-col gap-1">
      <label for="email" class="font-mono font-semibold text-gray-700">Email</label>
      <input
        id="email"
        type="email"
        bind:value={email}
        placeholder="you@email.com"
        required
        class="border-2 border-black px-3 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-black font-mono"
      />
    </div>

    <!-- Password -->
    <div class="flex flex-col gap-1">
      <label for="password" class="font-mono font-semibold text-gray-700">Password</label>
      <input
        id="password"
        type="password"
        bind:value={password}
        placeholder="••••••••"
        required
        class="border-2 border-black px-3 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-black font-mono"
      />
    </div>

    <!-- Remember Me -->
    <label class="flex items-center gap-2 cursor-pointer font-mono">
      <input type="checkbox" class="accent-orange-500 w-4 h-4" />
      Remember me
    </label>

    <!-- Submit Button -->
    <button
      type="submit"
      class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 rounded-lg border-2 border-black shadow-md font-mono transition"
    >
      Login
    </button>

    {#if error}
      <p class="text-red-600 text-center font-mono">{error}</p>
    {/if}

    <p class="text-center font-mono text-sm">
      Belum punya akun?
      <a href="/register" class="text-orange-600 font-bold hover:underline">Register</a>
    </p>
  </form>
</div>
