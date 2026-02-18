<script>
  import { onMount } from 'svelte';
  import { api } from '$lib/api';
  import {
    Plus,
    Trash2,
    Search,
    Filter,
    X,
    CheckCircle,
    Clock,
    AlertCircle,
    Calendar,
    MoreVertical,
    Edit2,
    Copy,
    Archive,
    LayoutGrid,
    List
  } from 'lucide-svelte';

  let tasks = [];
  let filteredTasks = [];
  let loading = true;
  let error = '';

  // Modal state
  let showModal = false;
  let newTitle = '';
  let newDescription = '';
  let newStatus = 'PENDING';
  let newDueDate = '';

  // Filter & Search state
  let searchQuery = '';
  let statusFilter = 'ALL';
  let sortBy = 'newest';
  let showFilters = false;
  let viewMode = 'grid'; // 'grid' or 'list'

  const statusOptions = [
    { value: 'PENDING', label: 'Pending', icon: Clock },
    { value: 'SUCCESS', label: 'Success', icon: CheckCircle },
    { value: 'FAILED', label: 'Failed', icon: AlertCircle }
  ];

  // Stats
  let totalTasks = 0;
  let pendingCount = 0;
  let successCount = 0;
  let failedCount = 0;

  // ===============================
  // FETCH TASKS
  // ===============================
  async function fetchTasks() {
    loading = true;
    try {
      const res = await api.get('/tasks');
      tasks = res.data.tasks;
      updateStatsAndFilters();
    } catch (err) {
      error = err.response?.data?.error || 'Failed to fetch tasks';
    } finally {
      loading = false;
    }
  }

  // ===============================
  // UPDATE STATS AND FILTERS
  // ===============================
  function updateStatsAndFilters() {
    totalTasks = tasks.length;
    pendingCount = tasks.filter(t => t.status === 'PENDING').length;
    successCount = tasks.filter(t => t.status === 'SUCCESS').length;
    failedCount = tasks.filter(t => t.status === 'FAILED').length;
    applyFilters();
  }

  // ===============================
  // APPLY FILTERS AND SEARCH
  // ===============================
  function applyFilters() {
    let filtered = [...tasks];

    // Apply status filter
    if (statusFilter !== 'ALL') {
      filtered = filtered.filter(t => t.status === statusFilter);
    }

    // Apply search
    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase();
      filtered = filtered.filter(t =>
        t.title.toLowerCase().includes(query) ||
        (t.description && t.description.toLowerCase().includes(query))
      );
    }

    // Apply sorting
    filtered.sort((a, b) => {
      const dateA = new Date(a.created_at);
      const dateB = new Date(b.created_at);
      return sortBy === 'newest' ? dateB - dateA : dateA - dateB;
    });

    filteredTasks = filtered;
  }

  // ===============================
  // CREATE TASK
  // ===============================
  async function createTask() {
    if (!newTitle.trim()) return;

    try {
      const res = await api.post('/tasks', {
        title: newTitle,
        description: newDescription,
        status: newStatus,
        due_date: newDueDate || null
      });
      tasks = [...tasks, res.data.task];
      resetModal();
      updateStatsAndFilters();
    } catch (err) {
      error = err.response?.data?.error || 'Failed to create task';
    }
  }

  // ===============================
  // UPDATE STATUS
  // ===============================
  async function updateStatus(id, status) {
    try {
      await api.put(`/tasks/${id}`, { status });
      tasks = tasks.map(t =>
        t.id === id ? { ...t, status } : t
      );
      updateStatsAndFilters();
    } catch (err) {
      error = err.response?.data?.error || 'Failed to update task';
    }
  }

  // ===============================
  // DELETE TASK
  // ===============================
  async function deleteTask(id) {
    if (!confirm('Delete this task?')) return;

    try {
      await api.delete(`/tasks/${id}`);
      tasks = tasks.filter(t => t.id !== id);
      updateStatsAndFilters();
    } catch (err) {
      error = err.response?.data?.error || 'Failed to delete task';
    }
  }

  // ===============================
  // RESET MODAL
  // ===============================
  function resetModal() {
    newTitle = '';
    newDescription = '';
    newStatus = 'PENDING';
    newDueDate = '';
    showModal = false;
  }

  // ===============================
  // GET STATUS STYLE
  // ===============================
  function getStatusStyle(status) {
    switch(status) {
      case 'PENDING':
        return 'bg-gray-100 text-gray-700';
      case 'SUCCESS':
        return 'bg-gray-100 text-gray-700';
      case 'FAILED':
        return 'bg-gray-100 text-gray-700';
      default:
        return 'bg-gray-100 text-gray-700';
    }
  }

  // ===============================
  // GET STATUS ICON COLOR
  // ===============================
  function getStatusIconColor(status) {
    switch(status) {
      case 'PENDING':
        return 'text-gray-500';
      case 'SUCCESS':
        return 'text-gray-600';
      case 'FAILED':
        return 'text-gray-500';
      default:
        return 'text-gray-400';
    }
  }

  onMount(fetchTasks);

  // Watch for filter changes
  $: if (tasks.length) {
    applyFilters();
  }
</script>

<div class="space-y-6">
  <!-- Simple Header -->
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-2xl font-semibold text-gray-900">Tasks</h1>
      <p class="text-sm text-gray-500 mt-1">Manage and organize your tasks</p>
    </div>
    <button
      class="flex items-center gap-2 bg-white text-gray-700 px-4 py-2 rounded-lg border border-gray-200 hover:border-orange-500 hover:text-orange-500 transition-all shadow-sm"
      on:click={() => showModal = true}
    >
      <Plus size={18} />
      New Task
    </button>
  </div>

  <!-- Stats Cards - Monochrome -->
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

  <!-- Search & Filter Bar - Minimal -->
  <div class="bg-white rounded-lg border border-gray-200 p-4 shadow-sm">
    <div class="flex flex-col sm:flex-row gap-3">
      <!-- Search -->
      <div class="flex-1 relative">
        <Search size={16} class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
        <input
          type="text"
          placeholder="Search tasks..."
          bind:value={searchQuery}
          class="w-full pl-9 pr-8 py-2 text-sm border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 transition-all bg-gray-50/30"
        />
        {#if searchQuery}
          <button
            class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
            on:click={() => searchQuery = ''}
          >
            <X size={14} />
          </button>
        {/if}
      </div>

      <div class="flex gap-2">
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
            on:click={() => viewMode = 'grid'}
            title="Grid view"
          >
            <LayoutGrid size={16} />
          </button>
          <button
            class="p-2 {viewMode === 'list' ? 'bg-gray-100 text-gray-900' : 'bg-white text-gray-500 hover:bg-gray-50'}"
            on:click={() => viewMode = 'list'}
            title="List view"
          >
            <List size={16} />
          </button>
        </div>
      </div>
    </div>

    <!-- Filter Panel - Minimal -->
    {#if showFilters}
      <div class="mt-4 pt-4 border-t border-gray-100 grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label class="block text-xs font-medium text-gray-500 uppercase tracking-wider mb-2">Status</label>
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
          <label class="block text-xs font-medium text-gray-500 uppercase tracking-wider mb-2">Sort By</label>
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

  {#if error}
    <div class="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-lg text-sm flex items-center gap-2">
      <AlertCircle size={16} />
      {error}
    </div>
  {/if}

  <!-- Loading State -->
  {#if loading}
    <div class="flex items-center justify-center py-12">
      <div class="w-6 h-6 border-2 border-gray-300 border-t-orange-500 rounded-full animate-spin"></div>
    </div>
  {:else}
    <!-- Tasks Grid/List View -->
    {#if viewMode === 'grid'}
      <!-- Grid View - 4 Columns -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {#each filteredTasks as task}
          {@const StatusIcon = statusOptions.find(s => s.value === task.status)?.icon || Clock}
          <div class="group bg-white rounded-lg border border-gray-200 hover:border-orange-200 hover:shadow-md transition-all duration-200">
            <div class="p-4">
              <!-- Title and Actions -->
              <div class="flex items-start justify-between">
                <h3 class="font-medium text-gray-900 text-sm line-clamp-2 flex-1 pr-2">{task.title}</h3>
                <button
                  class="text-gray-300 hover:text-red-500 transition-colors opacity-0 group-hover:opacity-100"
                  on:click={() => deleteTask(task.id)}
                  title="Delete"
                >
                  <Trash2 size={14} />
                </button>
              </div>

              <!-- Description if any -->
              {#if task.description}
                <p class="text-xs text-gray-500 mt-2 line-clamp-2">{task.description}</p>
              {/if}

              <!-- Status & Due Date -->
              <div class="flex items-center justify-between mt-3">
                <div class="flex items-center gap-1.5">
                  <StatusIcon size={12} class={getStatusIconColor(task.status)} />
                  <select
                    bind:value={task.status}
                    on:change={(e) => updateStatus(task.id, e.target.value)}
                    class="text-xs bg-transparent border-0 p-0 pr-5 focus:ring-0 cursor-pointer text-gray-600 font-medium"
                  >
                    {#each statusOptions as option}
                      <option value={option.value}>{option.label}</option>
                    {/each}
                  </select>
                </div>

                {#if task.due_date}
                  <div class="flex items-center gap-1 text-xs text-gray-400">
                    <Calendar size={10} />
                    {new Date(task.due_date).toLocaleDateString()}
                  </div>
                {/if}
              </div>

              <!-- Footer -->
              <div class="flex items-center justify-between mt-3 pt-2 border-t border-gray-100">
                <span class="text-xs text-gray-400">
                  {new Date(task.created_at).toLocaleDateString()}
                </span>

                <div class="flex items-center gap-1">
                  <button class="p-1 text-gray-300 hover:text-orange-500 transition-colors" title="Edit">
                    <Edit2 size={12} />
                  </button>
                  <button class="p-1 text-gray-300 hover:text-blue-500 transition-colors" title="Copy">
                    <Copy size={12} />
                  </button>
                </div>
              </div>
            </div>
          </div>
        {:else}
          <!-- Empty State -->
          <div class="col-span-full flex flex-col items-center justify-center py-12 text-center">
            <div class="w-16 h-16 bg-gray-50 rounded-full flex items-center justify-center mb-3">
              <Clock size={24} class="text-gray-400" />
            </div>
            <h3 class="text-sm font-medium text-gray-900 mb-1">No tasks found</h3>
            <p class="text-xs text-gray-500 mb-3">
              {searchQuery || statusFilter !== 'ALL' ? 'Try adjusting your filters' : 'Get started by creating your first task'}
            </p>
            <button
              class="text-sm text-orange-600 hover:text-orange-700 font-medium flex items-center gap-1"
              on:click={() => showModal = true}
            >
              <Plus size={14} />
              Create Task
            </button>
          </div>
        {/each}
      </div>
    {:else}
      <!-- List View -->
      <div class="bg-white rounded-lg border border-gray-200 overflow-hidden shadow-sm">
        <table class="w-full text-sm">
          <thead class="bg-gray-50 text-xs text-gray-500 uppercase tracking-wider">
            <tr>
              <th class="px-4 py-3 text-left font-medium">Title</th>
              <th class="px-4 py-3 text-left font-medium">Status</th>
              <th class="px-4 py-3 text-left font-medium">Due Date</th>
              <th class="px-4 py-3 text-left font-medium">Created</th>
              <th class="px-4 py-3 text-right font-medium">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100">
            {#each filteredTasks as task}
              {@const StatusIcon = statusOptions.find(s => s.value === task.status)?.icon || Clock}
              <tr class="hover:bg-gray-50 transition-colors">
                <td class="px-4 py-3">
                  <div>
                    <p class="font-medium text-gray-900">{task.title}</p>
                    {#if task.description}
                      <p class="text-xs text-gray-500 mt-0.5 line-clamp-1">{task.description}</p>
                    {/if}
                  </div>
                </td>
                <td class="px-4 py-3">
                  <div class="flex items-center gap-1.5">
                    <StatusIcon size={12} class={getStatusIconColor(task.status)} />
                    <select
                      bind:value={task.status}
                      on:change={(e) => updateStatus(task.id, e.target.value)}
                      class="text-xs bg-transparent border-0 p-0 pr-5 focus:ring-0 cursor-pointer text-gray-600"
                    >
                      {#each statusOptions as option}
                        <option value={option.value}>{option.label}</option>
                      {/each}
                    </select>
                  </div>
                </td>
                <td class="px-4 py-3">
                  {#if task.due_date}
                    <div class="flex items-center gap-1 text-xs text-gray-500">
                      <Calendar size={12} />
                      {new Date(task.due_date).toLocaleDateString()}
                    </div>
                  {:else}
                    <span class="text-xs text-gray-400">—</span>
                  {/if}
                </td>
                <td class="px-4 py-3 text-xs text-gray-500">
                  {new Date(task.created_at).toLocaleDateString()}
                </td>
                <td class="px-4 py-3 text-right">
                  <div class="flex items-center justify-end gap-2">
                    <button class="text-gray-400 hover:text-orange-500 transition-colors" title="Edit">
                      <Edit2 size={14} />
                    </button>
                    <button class="text-gray-400 hover:text-blue-500 transition-colors" title="Copy">
                      <Copy size={14} />
                    </button>
                    <button
                      class="text-gray-400 hover:text-red-500 transition-colors"
                      on:click={() => deleteTask(task.id)}
                      title="Delete"
                    >
                      <Trash2 size={14} />
                    </button>
                  </div>
                </td>
              </tr>
            {/each}
          </tbody>
        </table>

        {#if filteredTasks.length === 0}
          <div class="text-center py-8">
            <p class="text-sm text-gray-500">No tasks found</p>
          </div>
        {/if}
      </div>
    {/if}

    <!-- Results Info -->
    {#if filteredTasks.length > 0}
      <div class="text-xs text-gray-400 text-center">
        Showing {filteredTasks.length} of {totalTasks} tasks
      </div>
    {/if}
  {/if}

  <!-- Modal Create Task - Minimal -->
  {#if showModal}
    <div class="fixed inset-0 bg-black/20 flex items-center justify-center z-50 p-4" on:click|self={resetModal}>
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
            on:click={resetModal}
          >
            Cancel
          </button>
          <button
            class="px-3 py-1.5 text-xs bg-orange-500 text-white rounded hover:bg-orange-600 transition-colors disabled:opacity-50 flex items-center gap-1"
            on:click={createTask}
            disabled={!newTitle.trim()}
          >
            <Plus size={12} />
            Create
          </button>
        </div>
      </div>
    </div>
  {/if}
</div>

<style>
  :global(.line-clamp-2) {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  :global(.line-clamp-1) {
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>
