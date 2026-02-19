<script>
  import { onMount } from 'svelte';
  import { api } from '$lib/api';
  import TaskStats from './TaskStats.svelte';
  import TaskSearchFilter from './TaskSearchFilter.svelte';
  import TaskGrid from './TaskGrid.svelte';
  import TaskList from './TaskList.svelte';
  import TaskModal from './TaskModal.svelte';
  import { Clock } from 'lucide-svelte';

  let tasks = [];
  let filteredTasks = [];
  let loading = true;
  let error = '';

  let showModal = false;
  let newTitle = '';
  let newDescription = '';
  let newStatus = 'PENDING';
  let newDueDate = '';

  let searchQuery = '';
  let statusFilter = 'ALL';
  let sortBy = 'newest';
  let showFilters = false;
  let viewMode = 'grid';

  export const statusOptions = [
    { value: 'PENDING', label: 'Pending', icon: Clock },
    { value: 'SUCCESS', label: 'Success', icon: Clock },
    { value: 'FAILED', label: 'Failed', icon: Clock }
  ];

  let totalTasks = 0;
  let pendingCount = 0;
  let successCount = 0;
  let failedCount = 0;

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

  function updateStatsAndFilters() {
    totalTasks = tasks.length;
    pendingCount = tasks.filter(t => t.status === 'PENDING').length;
    successCount = tasks.filter(t => t.status === 'SUCCESS').length;
    failedCount = tasks.filter(t => t.status === 'FAILED').length;
    applyFilters();
  }

  function applyFilters() {
    let filtered = [...tasks];

    if (statusFilter !== 'ALL') {
      filtered = filtered.filter(t => t.status === statusFilter);
    }

    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase();
      filtered = filtered.filter(t =>
        t.title.toLowerCase().includes(query) ||
        (t.description && t.description.toLowerCase().includes(query))
      );
    }

    filtered.sort((a, b) => {
      const dateA = new Date(a.created_at);
      const dateB = new Date(b.created_at);
      return sortBy === 'newest' ? dateB - dateA : dateA - dateB;
    });

    filteredTasks = filtered;
  }

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

  function resetModal() {
    newTitle = '';
    newDescription = '';
    newStatus = 'PENDING';
    newDueDate = '';
    showModal = false;
  }

  onMount(fetchTasks);

  $: if (tasks.length) {
    applyFilters();
  }
</script>

<div class="space-y-6">
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-2xl font-semibold text-gray-900">Tasks</h1>
      <p class="text-sm text-gray-500 mt-1">Manage and organize your tasks</p>
    </div>
    <button
      class="flex items-center gap-2 bg-white text-gray-700 px-4 py-2 rounded-lg border border-gray-200 hover:border-orange-500 hover:text-orange-500 transition-all shadow-sm"
      on:click={() => showModal = true}
    >
      <span class="text-lg">+</span>
      New Task
    </button>
  </div>

  <TaskStats {totalTasks} {pendingCount} {successCount} {failedCount}/>

  <TaskSearchFilter
    bind:searchQuery
    bind:statusFilter
    bind:sortBy
    bind:showFilters
    bind:viewMode
    {statusOptions}
  />

  {#if error}
    <div class="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-lg text-sm flex items-center gap-2">
      <span class="text-red-600">⚠</span>
      {error}
    </div>
  {/if}

  <!-- Loading State -->
  {#if loading}
    <div class="flex items-center justify-center py-12">
      <div class="w-6 h-6 border-2 border-gray-300 border-t-orange-500 rounded-full animate-spin"></div>
    </div>
  {:else}

    {#if viewMode === 'grid'}
      <TaskGrid tasks={filteredTasks} {statusOptions}
        on:updateStatus={(e) => updateStatus(e.detail.id, e.detail.status)}
        on:deleteTask={(e) => deleteTask(e.detail)}
        onCreateClick={() => showModal = true}
        {searchQuery} {statusFilter}
      />
    {:else}
      <TaskList tasks={filteredTasks} {statusOptions}
        on:updateStatus={(e) => updateStatus(e.detail.id, e.detail.status)}
        on:deleteTask={(e) => deleteTask(e.detail)}
      />
    {/if}

    {#if filteredTasks.length > 0}
      <div class="text-xs text-gray-400 text-center">
        Showing {filteredTasks.length} of {totalTasks} tasks
      </div>
    {/if}
  {/if}

  <!-- Modal -->
  <TaskModal
    bind:showModal
    bind:newTitle
    bind:newDescription
    bind:newStatus
    bind:newDueDate
    {statusOptions}
    on:create={createTask}
    on:reset={resetModal}
  />
</div>
