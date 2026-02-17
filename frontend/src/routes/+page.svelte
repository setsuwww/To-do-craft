<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let token = null;

  onMount(() => {
    token = localStorage.getItem('token');
    if (!token) goto('/login');
  });
</script>

<main class="min-h-screen flex flex-col items-center justify-center bg-orange-100 p-6">
  <h1 class="text-3xl font-bold mb-4 text-gray-800">Welcome!</h1>
  <p class="text-gray-600 mb-6">You are logged in.</p>
  <a href="/logout" class="bg-orange-500 hover:bg-orange-600 text-white px-6 py-3 rounded-xl transition">
    Logout
  </a>
</main>
