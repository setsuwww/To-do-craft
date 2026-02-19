<script>
  import { createEventDispatcher } from 'svelte';

  export let showModal = false;
  export let newTitle = '';
  export let newDescription = '';
  export let newStatus = 'PENDING';
  export let newDueDate = '';
  export let statusOptions = [];

  const dispatch = createEventDispatcher();

  function closeModal() {
    showModal = false;
    dispatch('reset');
  }
</script>

{#if showModal}
  <div class="fixed inset-0 bg-black/20 flex items-center justify-center z-50 p-4" on:click|self={closeModal}>
    <div class="bg-white w-full max-w-md rounded-lg shadow-lg border border-gray-200">
      <!-- Modal Header -->
      <div class="px-4 py-3 border-b border-gray-200">
        <h2 class="text-sm font-semibold text-gray-900">Create New Task</h2>
      </div>

      <!-- Modal Body -->
      <div class="p-4 space-y-3">
        <div>
          <label class="block text-xs text-gray-500 mb-1">Title</label>
          <input
            type="text"
            bind:value={newTitle}
            placeholder="Enter task title"
            class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded focus:outline-none focus:border-orange-500"
            autofocus
          />
        </div>

        <div>
          <label class="block text-xs text-gray-500 mb-1">Description</label>
          <textarea
            bind:value={newDescription}
            placeholder="Optional"
            rows="2"
            class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded focus:outline-none focus:border-orange-500 resize-none"
          ></textarea>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs text-gray-500 mb-1">Status</label>
            <select
              bind:value={newStatus}
              class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded focus:outline-none focus:border-orange-500"
            >
              {#each statusOptions as option}
                <option value={option.value}>{option.label}</option>
              {/each}
            </select>
          </div>

          <div>
            <label class="block text-xs text-gray-500 mb-1">Due Date</label>
            <input
              type="date"
              bind:value={newDueDate}
              class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded focus:outline-none focus:border-orange-500"
            />
          </div>
        </div>
      </div>

      <!-- Modal Footer -->
      <div class="px-4 py-3 bg-gray-50 border-t border-gray-200 flex justify-end gap-2">
        <button
          class="px-3 py-1.5 text-xs text-gray-600 hover:bg-gray-200 rounded transition-colors"
          on:click={closeModal}
        >
          Cancel
        </button>
        <button
          class="px-3 py-1.5 text-xs bg-orange-500 text-white rounded hover:bg-orange-600 transition-colors disabled:opacity-50 flex items-center gap-1"
          on:click={() => dispatch('create')}
          disabled={!newTitle.trim()}
        >
          <span class="text-sm">+</span>
          Create
        </button>
      </div>
    </div>
  </div>
{/if}
