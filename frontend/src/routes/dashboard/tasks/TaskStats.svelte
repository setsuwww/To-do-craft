<script>
  export let totalTasks = 0;
  export let pendingCount = 0;
  export let successCount = 0;
  export let failedCount = 0;
</script>

<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
  <div class="bg-white rounded-lg border border-gray-200 p-4 shadow-sm">
    <p class="text-sm text-gray-500">Total Tasks</p>
    <p class="text-2xl font-semibold text-gray-900 mt-1">{totalTasks}</p>
  </div>
  <div class="bg-white rounded-lg border border-gray-200 p-4 shadow-sm">
    <p class="text-sm text-gray-500">Pending</p>
    <p class="text-2xl font-semibold text-gray-900 mt-1">{pendingCount}</p>
  </div>
  <div class="bg-white rounded-lg border border-gray-200 p-4 shadow-sm">
    <p class="text-sm text-gray-500">Success</p>
    <p class="text-2xl font-semibold text-gray-900 mt-1">{successCount}</p>
  </div>
  <div class="bg-white rounded-lg border border-gray-200 p-4 shadow-sm">
    <p class="text-sm text-gray-500">Failed</p>
    <p class="text-2xl font-semibold text-gray-900 mt-1">{failedCount}</p>
  </div>
</div>
