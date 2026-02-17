<script>
  import { goto } from '$app/navigation';
  let email = '';
  let password = '';
  let error = '';

  async function handleLogin() {
    error = '';
    const res = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (!res.ok) {
      error = data.error;
      return;
    }

    localStorage.setItem('token', data.access_token);
    goto('/');
  }
</script>

<div class="min-h-screen flex items-center justify-center bg-orange-100 p-6">
  <form class="bg-white p-8 rounded-2xl shadow-xl space-y-5 w-full max-w-md" on:submit|preventDefault={handleLogin}>
    <h1 class="text-2xl font-semibold text-center text-gray-800">Login</h1>

    <input bind:value={email} type="email" placeholder="Email" class="w-full p-3 border rounded" required />
    <input bind:value={password} type="password" placeholder="Password" class="w-full p-3 border rounded" required />

    <label class="flex items-center gap-2">
      <input type="checkbox" class="accent-orange-500" /> Remember me
    </label>

    <button type="submit" class="w-full bg-orange-500 hover:bg-orange-600 text-white p-3 rounded">
      Login
    </button>

    {#if error}
      <p class="text-red-500 text-center">{error}</p>
    {/if}

    <p class="text-center text-sm">
      Belum punya akun? <a href="/register" class="text-orange-500 hover:underline">Register</a>
    </p>
  </form>
</div>
