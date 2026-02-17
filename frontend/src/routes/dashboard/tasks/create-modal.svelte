<script>
  import { createEventDispatcher } from 'svelte';
  import { createTask } from '$lib/taskService';

  const dispatch = createEventDispatcher();

  let title = '';
  let description = '';
  let status = 'PENDING';

  const statuses = ['FAILED', 'PENDING', 'SUCCESS'];

  const handleSubmit = async () => {
    try {
      await createTask({ title, description, status });
      dispatch('close');
    } catch (err) {
      console.error(err);
      alert('Failed to create task');
    }
  };

  const handleCancel = () => dispatch('close');
</script>

<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
  <div class="bg-white rounded-lg shadow-lg w-11/12 max-w-md p-6">
    <h2 class="text-lg font-bold mb-4">Create Task</h2>

    <div class="flex flex-col gap-3">
      <input
        type="text"
        placeholder="Title"
        class="border rounded px-3 py-2"
        bind:value={title}
      />

      <textarea
        placeholder="Description"
        class="border rounded px-3 py-2 resize-none"
        rows="4"
        bind:value={description}
      ></textarea>

      <select class="border rounded px-3 py-2" bind:value={status}>
        {#each statuses as s}
          <option value={s}>{s}</option>
        {/each}
      </select>
    </div>

    <div class="mt-4 flex justify-end gap-3">
      <button class="px-4 py-2 rounded border hover:bg-gray-100" on:click={handleCancel}>
        Cancel
      </button>
      <button class="px-4 py-2 rounded bg-orange-600 text-white hover:bg-orange-500" on:click={handleSubmit}>
        Create
      </button>
    </div>
  </div>
</div>
