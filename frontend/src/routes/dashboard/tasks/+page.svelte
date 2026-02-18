<script>
  import { onMount } from 'svelte';
  import { api } from '$lib/api';
  import { Plus, Trash2 } from 'lucide-svelte';

  let tasks = [];
  let loading = true;
  let error = '';

  let showModal = false;
  let newTitle = '';

  const statusOptions = ['PENDING', 'SUCCESS', 'FAILED'];

  // ===============================
  // FETCH TASKS
  // ===============================
  async function fetchTasks() {
    loading = true;
    try {
      const res = await api.get('/tasks');
      tasks = res.data.tasks;
    } catch (err) {
      error = err.response?.data?.error || 'Failed to fetch tasks';
    } finally {
      loading = false;
    }
  }

  // ===============================
  // CREATE TASK
  // ===============================
  async function createTask() {
    if (!newTitle.trim()) return;

    try {
      const res = await api.post('/tasks', {
        title: newTitle
      });
      tasks = [...tasks, res.data.task];
      newTitle = '';
      showModal = false;
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
    } catch (err) {
      error = err.response?.data?.error || 'Failed to delete task';
    }
  }

  onMount(fetchTasks);
</script>

<div class="space-y-6">

  <!-- Header -->
  <div class="flex justify-between items-center">
    <h1 class="text-2xl font-semibold text-gray-900">Tasks</h1>
    <button
      class="flex items-center gap-2 bg-orange-500 text-white px-4 py-2 rounded-lg hover:bg-orange-600 transition"
      on:click={() => showModal = true}
    >
      <Plus size={18} />
      New Task
    </button>
  </div>

  {#if error}
    <p class="text-red-500 text-sm">{error}</p>
  {/if}

  <!-- Loading -->
  {#if loading}
    <div class="py-12 text-center text-gray-500">Loading tasks...</div>
  {:else}

    <!-- Table -->
    <div class="bg-white rounded-xl border border-gray-200 overflow-hidden">
      <table class="w-full text-sm">
        <thead class="bg-gray-50 text-gray-600">
          <tr>
            <th class="px-4 py-3 text-left">Title</th>
            <th class="px-4 py-3 text-left">Status</th>
            <th class="px-4 py-3 text-left">Created</th>
            <th class="px-4 py-3 text-right">Actions</th>
          </tr>
        </thead>
        <tbody>
          {#each tasks as task}
            <tr class="border-t">
              <td class="px-4 py-3">{task.title}</td>

              <td class="px-4 py-3">
                <select
                  bind:value={task.status}
                  on:change={(e) => updateStatus(task.id, e.target.value)}
                  class="border rounded px-2 py-1 text-xs"
                >
                  {#each statusOptions as s}
                    <option value={s}>{s}</option>
                  {/each}
                </select>
              </td>

              <td class="px-4 py-3 text-gray-500 text-xs">
                {new Date(task.created_at).toLocaleString()}
              </td>

              <td class="px-4 py-3 text-right">
                <button
                  class="text-red-500 hover:text-red-700"
                  on:click={() => deleteTask(task.id)}
                >
                  <Trash2 size={16} />
                </button>
              </td>
            </tr>
          {/each}

          {#if tasks.length === 0}
            <tr>
              <td colspan="4" class="text-center py-8 text-gray-400">
                No tasks found.
              </td>
            </tr>
          {/if}
        </tbody>
      </table>
    </div>
  {/if}

  <!-- Modal Create Task -->
  {#if showModal}
    <div class="fixed inset-0 bg-black/40 flex items-center justify-center">
      <div class="bg-white w-full max-w-md p-6 rounded-xl">
        <h2 class="text-lg font-semibold mb-4">Create Task</h2>

        <input
          type="text"
          bind:value={newTitle}
          placeholder="Task title"
          class="w-full border px-3 py-2 rounded-lg mb-4"
        />

        <div class="flex justify-end gap-3">
          <button
            class="px-4 py-2 text-gray-600"
            on:click={() => showModal = false}
          >
            Cancel
          </button>

          <button
            class="px-4 py-2 bg-orange-500 text-white rounded-lg"
            on:click={createTask}
          >
            Save
          </button>
        </div>
      </div>
    </div>
  {/if}

</div>
