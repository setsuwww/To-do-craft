<script>
  import { goto } from '$app/navigation';
  localStorage.removeItem('token');
  goto('/login');
</script>
