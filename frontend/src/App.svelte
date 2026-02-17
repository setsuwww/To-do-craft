<script>
  import { Router } from 'svelte-spa-router';
  import Login from './routes/Login.svelte';
  import Home from './routes/Home.svelte';
  import Register from './routes/Register.svelte';

  const routes = {
    '/': Home,
    '/login': Login,
    '/register': Register
  };
</script>

<Router {routes} />
