<script>
  import { createEventDispatcher } from "svelte";
  import {
    Clock,
    CheckCircle,
    Trash2,
    Calendar,
    PenSquare,
  } from "lucide-svelte";

  export let task;
  export let statusOptions = [];

  const dispatch = createEventDispatcher();

  function getStatusIcon(status) {
    switch (status) {
      case "PENDING":
        return Clock;
      case "SUCCESS":
        return CheckCircle;
      case "FAILED":
        return Trash2;
      default:
        return Clock;
    }
  }

  function getStatusIconColor(status) {
    switch (status) {
      case "PENDING":
        return "text-gray-500";
      case "SUCCESS":
        return "text-green-500";
      case "FAILED":
        return "text-red-500";
      default:
        return "text-gray-400";
    }
  }

  const StatusIcon = getStatusIcon(task.status);
</script>

<div
  class="group bg-white rounded-lg border border-gray-300 ring ring-white outline outline-offset-1 outline-gray-300"
>
  <div class="p-4">
    <!-- Title and Actions -->
    <div class="flex flex-col items-start justify-between space-y-2">
      <h3 class="font-medium text-gray-900 text-sm line-clamp-2 flex-1 pr-2">
        {task.title}
      </h3>
      {#if task.description}
        <p class="text-xs text-gray-500 line-clamp-2">{task.description}</p>
      {/if}
    </div>

    <!-- Description -->

    <div class="flex items-center justify-between mt-3">
      <div class="flex items-center gap-1.5">
        <StatusIcon size={12} class={getStatusIconColor(task.status)} />
        <select value={task.status}
          on:change={(e) =>
            dispatch("updateStatus", { id: task.id, status: e.target.value })}
          class="text-xs bg-transparent border-0 p-0 pr-5 focus:ring-0 cursor-pointer text-gray-600 font-medium"
        >
          {#each statusOptions as option}
            <option
              value={option.value}
              selected={task.status === option.value}
            >
              {option.label}
            </option>
          {/each}
        </select>
      </div>

      {#if task.due_date}
        <div class="flex items-center gap-1 text-xs text-gray-400">
          <Calendar size={12} />
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
        <button
          class="p-1 text-gray-300 hover:text-blue-500 transition-colors"
          title="Edit"
          on:click={() => dispatch("editTask", task)}
        >
          <PenSquare size={14} />
        </button>
        <button
          class="text-gray-300 hover:text-red-500 transition-colors"
          title="Delete"
          on:click={() => dispatch("deleteTask", task.id)}
        >
          <Trash2 size={14} />
        </button>
      </div>
    </div>
  </div>
</div>
