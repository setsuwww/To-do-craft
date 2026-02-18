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
    <h2 class="text-lg font-semibold text-gray-900 mb-4">Quick Actions</h2>

    <div class="space-y-3">
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

  <!-- Recent Activity -->
  <div class="bg-white rounded-2xl border border-gray-100 p-6">
    <h2 class="text-lg font-semibold text-gray-900 mb-4">Recent Activity</h2>

    <div class="space-y-4">
      {#each recentActivities as activity}
        <div class="flex items-start gap-3">
          <div class="w-8 h-8 bg-gray-100 rounded-lg flex items-center justify-center">
            <CheckCircle size={16} />
          </div>
          <div class="flex-1">
            <p class="text-sm text-gray-900">{activity.action}</p>
            <p class="text-xs text-gray-500">
              {activity.time} • by {activity.user}
            </p>
          </div>
        </div>
      {/each}
    </div>
  </div>

</div>
