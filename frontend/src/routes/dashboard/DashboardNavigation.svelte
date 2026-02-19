<script>
  import { goto } from '$app/navigation';
  import {
    Plus,
    Layout,
    FolderOpen,
    Clock,
    ArrowRight,
    CheckCircle
  } from 'lucide-svelte';

  export let recentActivities = [];
</script>

<div class="space-y-6">

  <!-- Quick Actions -->
  <div class="bg-white rounded-2xl border border-gray-100 p-6">
    <div class="mb-4">
      <h2 class="text-lg font-semibold text-gray-900">Quick action</h2>
      <p class="text-sm text-gray-500 mt-1">Simplify your action</p>
    </div>

    <div class="space-y-4 mt-10">
      <button class="w-full flex justify-between p-3 bg-orange-50 text-orange-700 rounded-xl"
        on:click={() => goto('/dashboard/tasks')}>
        <span class="flex items-center gap-2">
          <Plus size={18} />
          New Task
        </span>
        <ArrowRight size={18} />
      </button>

      <button class="w-full flex justify-between p-3 bg-gray-50 rounded-xl"
        on:click={() => goto('/dashboard/boards')}>
        <span class="flex items-center gap-2">
          <Layout size={18} />
          New Board
        </span>
        <ArrowRight size={18} />
      </button>

      <button class="w-full flex justify-between p-3 bg-gray-50 rounded-xl"
        on:click={() => goto('/dashboard/categories')}>
        <span class="flex items-center gap-2">
          <FolderOpen size={18} />
          New Category
        </span>
        <ArrowRight size={18} />
      </button>

      <button class="w-full flex justify-between p-3 bg-gray-50 rounded-xl"
        on:click={() => goto('/dashboard/schedules')}>
        <span class="flex items-center gap-2">
          <Clock size={18} />
          New Schedule
        </span>
        <ArrowRight size={18} />
      </button>
    </div>
  </div>
</div>
