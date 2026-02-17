<script>
  import { onMount } from 'svelte';
  import TasksCard from './tasks-card.svelte';
  import SearchEngine from './search-engine.svelte';
  import CreateModal from './create-modal.svelte';
  import EditModal from './edit-modal.svelte';
  import { fetchTasks, updateTask } from '$lib/taskService';

  let tasks = [];
  let search = '';
  let statusFilter = '';

  let showCreateModal = false;
  let showEditModal = false;
  let editingTask = null;

  // Load tasks from backend
  const loadTasks = async () => {
    try {
      const res = await fetchTasks(search, statusFilter);
      tasks = res.data || [];
    } catch (err) {
      console.error(err);
      tasks = [];
    }
  };

  // Handle status toggle from TasksCard
  const handleStatusChange = async (taskId, newStatus) => {
    try {
      await updateTask(taskId, { status: newStatus });
      tasks = tasks.map(t => t.id === taskId ? { ...t, status: newStatus } : t);
    } catch (err) {
      console.error(err);
    }
  };

  const openEditModal = (task) => {
    editingTask = task;
    showEditModal = true;
  };

  onMount(loadTasks);
</script>

<!-- Page Header -->
<div class="flex justify-between items-center mb-6">
  <h1 class="text-2xl font-bold text-gray-900">Tasks</h1>
  <button
    class="px-4 py-2 bg-orange-600 text-white font-medium rounded hover:bg-orange-500 transition"
    on:click={() => showCreateModal = true}
  >
    + Create Task
  </button>
</div>

<!-- Search & Filter -->
<SearchEngine
  {search}
  {statusFilter}
  onSearchChange={(s) => { search = s; loadTasks(); }}
  onStatusChange={(s) => { statusFilter = s; loadTasks(); }}
/>

<!-- Tasks Grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 mt-4">
  {#each tasks as task (task.id)}
    <TasksCard
      {task}
      on:updateStatus={({ detail }) => handleStatusChange(detail.id, detail.status)}
      on:edit={() => openEditModal(task)}
    />
  {/each}
</div>

<!-- Create Modal -->
{#if showCreateModal}
  <CreateModal on:close={() => { showCreateModal = false; loadTasks(); }} />
{/if}

<!-- Edit Modal -->
{#if showEditModal && editingTask}
  <EditModal
    task={editingTask}
    on:close={() => { showEditModal = false; editingTask = null; loadTasks(); }}
  />
{/if}
