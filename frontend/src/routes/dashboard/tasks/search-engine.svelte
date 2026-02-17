<script>
  export let search = '';
  export let statusFilter = '';
  export let onSearchChange = () => {};
  export let onStatusChange = () => {};

  const statuses = ['', 'FAILED', 'PENDING', 'SUCCESS'];
</script>

<div class="flex gap-2 mb-4 flex-wrap">
  <!-- Search -->
  <input
    type="text"
    placeholder="Search tasks..."
    class="flex-1 min-w-[200px] border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
    bind:value={search}
    on:input={() => onSearchChange(search)}
  />

  <!-- Status Filter -->
  <select
    class="border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
    bind:value={statusFilter}
    on:change={() => onStatusChange(statusFilter)}
  >
    {#each statuses as s}
      <option value={s}>{s || 'All'}</option>
    {/each}
  </select>
</div>
