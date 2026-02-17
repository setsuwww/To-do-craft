<script context="module" lang="ts">
  import { redirect } from '@sveltejs/kit';

  export function load() {
    const token = typeof localStorage !== 'undefined' ? localStorage.getItem('token') : null;
    if (!token) throw redirect(307, '/login');
  }
</script>
