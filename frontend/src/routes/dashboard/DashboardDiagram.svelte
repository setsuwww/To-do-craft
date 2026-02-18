<script>
  import { BarChart3, MoreVertical } from 'lucide-svelte';

  export let chartData = [];
  export let chartLabels = [];
</script>

<div class="bg-white rounded-2xl border border-gray-100 p-6">
  <div class="flex items-center justify-between mb-6">
    <div>
      <h2 class="text-lg font-semibold text-gray-900">Task Overview</h2>
      <p class="text-sm text-gray-500 mt-1">Weekly task completion</p>
    </div>

    <div class="flex items-center gap-2">
      <button class="p-2 hover:bg-gray-100 rounded-lg">
        <BarChart3 size={18} class="text-gray-500" />
      </button>
      <button class="p-2 hover:bg-gray-100 rounded-lg">
        <MoreVertical size={18} class="text-gray-500" />
      </button>
    </div>
  </div>

  <div class="relative h-64 mt-4">
    <div class="absolute bottom-0 left-0 w-full h-full flex items-end justify-between px-2">
      {#each chartData as value, index}
        <div class="relative group w-12">
          <div
            class="w-full bg-orange-500 rounded-lg transition-all duration-300"
            style="height: {value}%"
          >
            <div class="absolute -top-8 left-1/2 -translate-x-1/2 bg-gray-900 text-white text-xs py-1 px-2 rounded opacity-0 group-hover:opacity-100 transition-opacity">
              {value} tasks
            </div>
          </div>
          <span class="absolute -bottom-6 left-1/2 -translate-x-1/2 text-xs text-gray-500 pb-4">
            {chartLabels[index]}
          </span>
        </div>
      {/each}
    </div>
  </div>
</div>
