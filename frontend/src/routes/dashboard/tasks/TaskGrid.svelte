<script>
  import { createEventDispatcher } from 'svelte';
  import TaskCard from './TaskCard.svelte';

  export let tasks = [];
  export let statusOptions = [];
  export let searchQuery = '';
  export let statusFilter = 'ALL';

  const dispatch = createEventDispatcher();
</script>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
  {#each tasks as task}
    <TaskCard
      {task}
      {statusOptions}
      on:updateStatus={(e) => dispatch('updateStatus', e.detail)}
      on:deleteTask={(e) => dispatch('deleteTask', e.detail)}
    />
  {:else}
    <!-- Empty State -->
    <div class="col-span-full flex flex-col items-center justify-center py-12 text-center">
      <div class="w-16 h-16 bg-gray-50 rounded-full flex items-center justify-center mb-3">
        <span class="text-2xl text-gray-400">⏰</span>
      </div>
      <h3 class="text-sm font-medium text-gray-900 mb-1">No tasks found</h3>
      <p class="text-xs text-gray-500 mb-3">
        {searchQuery || statusFilter !== 'ALL' ? 'Try adjusting your filters' : 'Get started by creating your first task'}
      </p>
      <button
        class="text-sm text-orange-600 hover:text-orange-700 font-medium flex items-center gap-1"
        on:click={() => dispatch('createClick')}
      >
        <span class="text-lg">+</span>
        Create Task
      </button>
    </div>
  {/each}
</div>
