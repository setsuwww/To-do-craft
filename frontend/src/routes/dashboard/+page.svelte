<script>
  import { onMount } from 'svelte';
  import { api } from '$lib/api';

  let message = '';

  onMount(async () => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      message = 'You are not logged in';
      return;
    }

    try {
      const res = await api.get('/dashboard');
      message = res.data.message;
    } catch (err) {
      console.error("DEBUG: error =", err.response?.data || err);
      message = err.response?.data?.error || 'Failed to fetch dashboard';
    }
  });
</script>

<h1>Dashboard</h1>
<p>{message}</p>
