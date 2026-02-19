<script>
  import { createEventDispatcher } from 'svelte';
  import { Search, X, Filter, LayoutGrid, List } from 'lucide-svelte';

  export let searchQuery = '';
  export let statusFilter = 'ALL';
  export let sortBy = 'newest';
  export let showFilters = false;
  export let viewMode = 'grid';
  export let statusOptions = [];

  const dispatch = createEventDispatcher();

  function handleSearch() {
    dispatch('search', searchQuery);
  }

  function handleViewChange(mode) {
    dispatch('viewChange', mode);
  }
</script>

<div class="bg-white rounded-lg border border-gray-200 p-4 shadow-sm space-y-3">
  <div class="flex flex-col sm:flex-row gap-3 items-start sm:items-center">
    <!-- Search -->
    <div class="flex-1 relative">
      <Search size={16} class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
      <input
        type="text"
        placeholder="Search tasks..."
        bind:value={searchQuery}
        class="w-full pl-9 pr-8 py-2 text-sm border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 transition-all bg-gray-50/30"
        on:input={handleSearch}
      />
      {#if searchQuery}
        <button
          class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
          on:click={() => { searchQuery = ''; handleSearch(); }}
        >
          <X size={14} />
        </button>
      {/if}
    </div>

    <div class="flex gap-2 items-center">
      <!-- Filter Button -->
      <button
        class="flex items-center gap-2 px-3 py-2 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors text-sm"
        on:click={() => showFilters = !showFilters}
      >
        <Filter size={16} class={showFilters ? 'text-orange-500' : 'text-gray-500'} />
        <span class="text-gray-700">Filters</span>
      </button>

      <!-- View Toggle -->
      <div class="flex border border-gray-200 rounded-lg overflow-hidden">
        <button
          class="p-2 {viewMode === 'grid' ? 'bg-gray-100 text-gray-900' : 'bg-white text-gray-500 hover:bg-gray-50'}"
          on:click={() => { viewMode = 'grid'; handleViewChange('grid'); }}
          title="Grid view"
        >
          <LayoutGrid size={16} />
        </button>
        <button
          class="p-2 {viewMode === 'list' ? 'bg-gray-100 text-gray-900' : 'bg-white text-gray-500 hover:bg-gray-50'}"
          on:click={() => { viewMode = 'list'; handleViewChange('list'); }}
          title="List view"
        >
          <List size={16} />
        </button>
      </div>
    </div>
  </div>

  <!-- Filter Panel -->
  {#if showFilters}
    <div class="mt-4 pt-4 border-t border-gray-100 grid grid-cols-1 sm:grid-cols-2 gap-4">
      <div>
        <label for="statusFilter" class="block text-xs font-medium text-gray-500 uppercase tracking-wider mb-2">Status</label>
        <select
          bind:value={statusFilter}
          class="w-full px-3 py-2 text-sm border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500 bg-white"
        >
          <option value="ALL">All Status</option>
          {#each statusOptions as option}
            <option value={option.value}>{option.label}</option>
          {/each}
        </select>
      </div>
      <div>
        <label for="sortBy" class="block text-xs font-medium text-gray-500 uppercase tracking-wider mb-2">Sort By</label>
        <select
          bind:value={sortBy}
          class="w-full px-3 py-2 text-sm border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500 bg-white"
        >
          <option value="newest">Newest First</option>
          <option value="oldest">Oldest First</option>
        </select>
      </div>
    </div>
  {/if}
</div>
