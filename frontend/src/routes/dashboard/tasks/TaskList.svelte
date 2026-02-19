<script>
  import { createEventDispatcher } from 'svelte';
  import { Edit2, Trash2, Calendar } from 'lucide-svelte';

  export let tasks = [];
  export let statusOptions = [];

  const dispatch = createEventDispatcher();

  function getStatusIconColor(status) {
    switch(status) {
      case 'PENDING': return 'text-gray-500';
      case 'SUCCESS': return 'text-green-500';
      case 'FAILED': return 'text-red-500';
      default: return 'text-gray-400';
    }
  }

  function getStatusLabel(status) {
    switch(status) {
      case 'PENDING': return 'Pending';
      case 'SUCCESS': return 'Success';
      case 'FAILED': return 'Failed';
      default: return status;
    }
  }
</script>

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
      {#each tasks as task}
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
              <span class={`text-xs font-semibold ${getStatusIconColor(task.status)}`}>
                {getStatusLabel(task.status)}
              </span>
              <select
                value={task.status}
                on:change={(e) => dispatch('updateStatus', { id: task.id, status: e.target.value })}
                class="text-xs bg-transparent border-0 p-0 pr-5 focus:ring-0 cursor-pointer text-gray-600"
              >
                {#each statusOptions as option}
                  <option value={option.value} selected={task.status === option.value}>
                    {option.label}
                  </option>
                {/each}
              </select>
            </div>
          </td>
          <td class="px-4 py-3">
            {#if task.due_date}
              <div class="flex items-center gap-1 text-xs text-gray-500">
                <Calendar size={14} />
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
              <button
                class="text-gray-400 hover:text-orange-500 transition-colors"
                title="Edit"
                on:click={() => dispatch('editTask', task)}
              >
                <Edit2 size={16} />
              </button>
              <button
                class="text-gray-400 hover:text-red-500 transition-colors"
                title="Delete"
                on:click={() => dispatch('deleteTask', task.id)}
              >
                <Trash2 size={16} />
              </button>
            </div>
          </td>
        </tr>
      {/each}
    </tbody>
  </table>

  {#if tasks.length === 0}
    <div class="text-center py-8">
      <p class="text-sm text-gray-500">No tasks found</p>
    </div>
  {/if}
</div>
