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
    Archive
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

  const statusOptions = [
    { value: 'PENDING', label: 'Pending', color: 'yellow', icon: Clock },
    { value: 'SUCCESS', label: 'Success', color: 'green', icon: CheckCircle },
    { value: 'FAILED', label: 'Failed', color: 'red', icon: AlertCircle }
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
    const option = statusOptions.find(s => s.value === status);
    switch(status) {
      case 'PENDING':
        return 'bg-yellow-100 text-yellow-700 border-yellow-200';
      case 'SUCCESS':
        return 'bg-green-100 text-green-700 border-green-200';
      case 'FAILED':
        return 'bg-red-100 text-red-700 border-red-200';
      default:
        return 'bg-gray-100 text-gray-700 border-gray-200';
    }
  }

  onMount(fetchTasks);

  // Watch for filter changes
  $: if (tasks.length) {
    applyFilters();
  }
</script>

<div class="space-y-8">
  <!-- Header Section with Stats -->
  <div class="bg-gradient-to-r from-orange-500 to-orange-600 -mt-6 -mx-6 p-6 mb-2">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-white tracking-tight">Tasks</h1>
        <p class="text-orange-100 text-sm mt-1">Manage and track your tasks efficiently</p>
      </div>
      <button
        class="flex items-center gap-2 bg-white text-orange-600 px-4 py-2 rounded-xl hover:bg-orange-50 transition-all transform hover:scale-105 shadow-lg"
        on:click={() => showModal = true}
      >
        <Plus size={18} />
        New Task
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
      <div class="bg-white/10 backdrop-blur-sm rounded-xl p-4 border border-white/20">
        <p class="text-orange-100 text-sm">Total Tasks</p>
        <p class="text-2xl font-bold text-white mt-1">{totalTasks}</p>
      </div>
      <div class="bg-white/10 backdrop-blur-sm rounded-xl p-4 border border-white/20">
        <p class="text-orange-100 text-sm">Pending</p>
        <p class="text-2xl font-bold text-white mt-1">{pendingCount}</p>
      </div>
      <div class="bg-white/10 backdrop-blur-sm rounded-xl p-4 border border-white/20">
        <p class="text-orange-100 text-sm">Success</p>
        <p class="text-2xl font-bold text-white mt-1">{successCount}</p>
      </div>
      <div class="bg-white/10 backdrop-blur-sm rounded-xl p-4 border border-white/20">
        <p class="text-orange-100 text-sm">Failed</p>
        <p class="text-2xl font-bold text-white mt-1">{failedCount}</p>
      </div>
    </div>
  </div>

  <!-- Search & Filter Bar -->
  <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
    <div class="flex flex-col sm:flex-row gap-4">
      <!-- Search -->
      <div class="flex-1 relative">
        <Search size={18} class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
        <input
          type="text"
          placeholder="Search tasks..."
          bind:value={searchQuery}
          class="w-full pl-10 pr-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500 focus:ring-2 focus:ring-orange-100 transition-all"
        />
        {#if searchQuery}
          <button
            class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
            on:click={() => searchQuery = ''}
          >
            <X size={16} />
          </button>
        {/if}
      </div>

      <!-- Filter Button -->
      <button
        class="flex items-center gap-2 px-4 py-2 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors relative"
        on:click={() => showFilters = !showFilters}
      >
        <Filter size={18} class={showFilters ? 'text-orange-500' : 'text-gray-500'} />
        <span class="text-sm font-medium">Filters</span>
      </button>
    </div>

    <!-- Filter Panel -->
    {#if showFilters}
      <div class="mt-4 pt-4 border-t border-gray-100 grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Status</label>
          <select
            bind:value={statusFilter}
            class="w-full px-3 py-2 border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500"
          >
            <option value="ALL">All Status</option>
            {#each statusOptions as option}
              <option value={option.value}>{option.label}</option>
            {/each}
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Sort By</label>
          <select
            bind:value={sortBy}
            class="w-full px-3 py-2 border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500"
          >
            <option value="newest">Newest First</option>
            <option value="oldest">Oldest First</option>
          </select>
        </div>
      </div>
    {/if}
  </div>

  {#if error}
    <div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg flex items-center gap-2">
      <AlertCircle size={18} />
      {error}
    </div>
  {/if}

  <!-- Loading State -->
  {#if loading}
    <div class="flex items-center justify-center py-12">
      <div class="w-8 h-8 border-3 border-orange-500 border-t-transparent rounded-full animate-spin"></div>
    </div>
  {:else}
    <!-- Tasks Grid - 4 Columns -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      {#each filteredTasks as task}
        {@const StatusIcon = statusOptions.find(s => s.value === task.status)?.icon || Clock}
        <div class="group bg-white rounded-xl border border-gray-200 hover:shadow-xl hover:border-orange-200 transition-all duration-300 overflow-hidden">
          <!-- Card Header with Status Bar -->
          <div class="h-2 bg-gradient-to-r from-{task.status === 'PENDING' ? 'yellow' : task.status === 'SUCCESS' ? 'green' : 'red'}-400 to-{task.status === 'PENDING' ? 'yellow' : task.status === 'SUCCESS' ? 'green' : 'red'}-500"></div>

          <div class="p-5">
            <!-- Title and Actions -->
            <div class="flex items-start justify-between">
              <h3 class="font-semibold text-gray-900 line-clamp-2 flex-1">{task.title}</h3>
              <div class="flex items-center gap-1">
                <button
                  class="p-1.5 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-lg transition-colors opacity-0 group-hover:opacity-100"
                  on:click={() => deleteTask(task.id)}
                  title="Delete"
                >
                  <Trash2 size={16} />
                </button>
                <button
                  class="p-1.5 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-lg transition-colors opacity-0 group-hover:opacity-100"
                  title="More"
                >
                  <MoreVertical size={16} />
                </button>
              </div>
            </div>

            <!-- Description if any -->
            {#if task.description}
              <p class="text-sm text-gray-500 mt-2 line-clamp-2">{task.description}</p>
            {/if}

            <!-- Status Badge & Due Date -->
            <div class="flex items-center justify-between mt-4">
              <!-- Status Dropdown -->
              <div class="relative">
                <select
                  bind:value={task.status}
                  on:change={(e) => updateStatus(task.id, e.target.value)}
                  class={`appearance-none pl-7 pr-8 py-1.5 text-xs font-medium rounded-lg border ${getStatusStyle(task.status)} focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-${task.status === 'PENDING' ? 'yellow' : task.status === 'SUCCESS' ? 'green' : 'red'}-500 cursor-pointer`}
                >
                  {#each statusOptions as option}
                    <option value={option.value}>{option.label}</option>
                  {/each}
                </select>
                <StatusIcon size={14} class="absolute left-2 top-1/2 -translate-y-1/2 pointer-events-none" />
              </div>

              <!-- Due Date if any -->
              {#if task.due_date}
                <div class="flex items-center gap-1 text-xs text-gray-500">
                  <Calendar size={12} />
                  {new Date(task.due_date).toLocaleDateString()}
                </div>
              {/if}
            </div>

            <!-- Footer with Created Date -->
            <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-100">
              <span class="text-xs text-gray-400">
                Created {new Date(task.created_at).toLocaleDateString()}
              </span>

              <!-- Quick Actions -->
              <div class="flex items-center gap-1">
                <button class="p-1 text-gray-400 hover:text-orange-500 hover:bg-orange-50 rounded transition-colors" title="Edit">
                  <Edit2 size={14} />
                </button>
                <button class="p-1 text-gray-400 hover:text-blue-500 hover:bg-blue-50 rounded transition-colors" title="Copy">
                  <Copy size={14} />
                </button>
                <button class="p-1 text-gray-400 hover:text-purple-500 hover:bg-purple-50 rounded transition-colors" title="Archive">
                  <Archive size={14} />
                </button>
              </div>
            </div>
          </div>
        </div>
      {:else}
        <!-- Empty State -->
        <div class="col-span-full flex flex-col items-center justify-center py-12 text-center">
          <div class="w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mb-4">
            <Clock size={32} class="text-gray-400" />
          </div>
          <h3 class="text-lg font-semibold text-gray-900 mb-1">No tasks found</h3>
          <p class="text-gray-500 text-sm mb-4">
            {searchQuery || statusFilter !== 'ALL' ? 'Try adjusting your filters' : 'Get started by creating your first task'}
          </p>
          <button
            class="flex items-center gap-2 bg-orange-500 text-white px-4 py-2 rounded-lg hover:bg-orange-600 transition"
            on:click={() => showModal = true}
          >
            <Plus size={18} />
            Create Task
          </button>
        </div>
      {/each}
    </div>

    <!-- Results Info -->
    {#if filteredTasks.length > 0}
      <div class="text-sm text-gray-500 text-center">
        Showing {filteredTasks.length} of {totalTasks} tasks
      </div>
    {/if}
  {/if}

  <!-- Modal Create Task -->
  {#if showModal}
    <div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4" on:click|self={resetModal}>
      <div class="bg-white w-full max-w-lg rounded-2xl shadow-2xl animate-in fade-in zoom-in duration-200">
        <!-- Modal Header -->
        <div class="bg-gradient-to-r from-orange-500 to-orange-600 px-6 py-4 rounded-t-2xl">
          <h2 class="text-lg font-semibold text-white">Create New Task</h2>
          <p class="text-orange-100 text-sm mt-1">Fill in the details below</p>
        </div>

        <!-- Modal Body -->
        <div class="p-6 space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Title *</label>
            <input
              type="text"
              bind:value={newTitle}
              placeholder="Enter task title"
              class="w-full px-3 py-2 border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500 focus:ring-2 focus:ring-orange-100 transition-all"
              autofocus
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
            <textarea
              bind:value={newDescription}
              placeholder="Enter task description (optional)"
              rows="3"
              class="w-full px-3 py-2 border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500 focus:ring-2 focus:ring-orange-100 transition-all resize-none"
            ></textarea>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Status</label>
              <select
                bind:value={newStatus}
                class="w-full px-3 py-2 border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500"
              >
                {#each statusOptions as option}
                  <option value={option.value}>{option.label}</option>
                {/each}
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Due Date</label>
              <input
                type="date"
                bind:value={newDueDate}
                class="w-full px-3 py-2 border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500"
              />
            </div>
          </div>
        </div>

        <!-- Modal Footer -->
        <div class="px-6 py-4 bg-gray-50 rounded-b-2xl flex justify-end gap-3">
          <button
            class="px-4 py-2 text-gray-600 hover:bg-gray-200 rounded-lg transition-colors"
            on:click={resetModal}
          >
            Cancel
          </button>
          <button
            class="px-4 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            on:click={createTask}
            disabled={!newTitle.trim()}
          >
            <Plus size={18} />
            Create Task
          </button>
        </div>
      </div>
    </div>
  {/if}
</div>

<!-- Add to global styles or keep here -->
<style>
  :global(.line-clamp-2) {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  :global(.animate-in) {
    animation: animate-in 0.2s ease-out;
  }

  :global(.fade-in) {
    opacity: 0;
    animation: fade-in 0.2s ease-out forwards;
  }

  :global(.zoom-in) {
    transform: scale(0.95);
    animation: zoom-in 0.2s ease-out forwards;
  }

  @keyframes animate-in {
    from {
      opacity: 0;
      transform: scale(0.95);
    }
    to {
      opacity: 1;
      transform: scale(1);
    }
  }

  @keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  @keyframes zoom-in {
    from { transform: scale(0.95); }
    to { transform: scale(1); }
  }
</style>
