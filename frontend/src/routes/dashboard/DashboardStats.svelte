<script>
  import { TrendingUp, TrendingDown } from 'lucide-svelte';
  export let stats = [];
</script>

<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
  {#each stats as stat}
    {@const IconComponent = stat.icon}
    <div class="group bg-white rounded-2xl border border-gray-100 p-6 hover:shadow-lg transition-all duration-300">
      <div class="flex items-start justify-between">
        <div class="flex-1">
          <p class="text-sm text-gray-500 mb-1">{stat.title}</p>
          <p class="text-3xl font-bold text-gray-900">{stat.value}</p>

          <div class="flex items-center gap-1 mt-3">
            {#if stat.trendUp}
              <TrendingUp size={14} class="text-green-500" />
              <span class="text-xs font-medium text-green-600">{stat.trend}</span>
            {:else}
              <TrendingDown size={14} class="text-red-500" />
              <span class="text-xs font-medium text-red-600">{stat.trend}</span>
            {/if}
            <span class="text-xs text-gray-400 ml-1">vs last week</span>
          </div>
        </div>

        <div class="w-12 h-12 rounded-xl bg-gray-100 flex items-center justify-center">
          <IconComponent size={24} class="text-gray-700" />
        </div>
      </div>
    </div>
  {/each}
</div>
