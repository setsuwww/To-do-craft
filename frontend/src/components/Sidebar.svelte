<script>
  import { page } from "$app/stores";
  import { onMount } from "svelte";
  import { api } from "$lib/api";

  export let items = [];
  export let isCollapsed = false;
  export let onToggle = () => {};

  import { LogOut, ChevronLeft, ChevronRight, User } from "lucide-svelte";

  const isActive = (href) => $page.url.pathname === href;

  onMount(async () => {
    try {
      const res = await api.get("/current_user");
      user = res.data;
    } catch (err) {
      console.error("Failed to fetch user:", err.response?.data || err);
    }
  });
</script>

<aside
  class="bg-white flex flex-col transition-all duration-300
       border border-gray-200 rounded-2xl shadow-sm ml-2
       h-[calc(100vh-1rem)] sticky top-2
       {isCollapsed ? 'w-20' : 'w-64'}"
>
  <div class="flex items-center h-16 px-4 border-b border-gray-200">
    <div class="flex items-center gap-2 flex-1">
      {#if !isCollapsed}
        <div
          class="w-8 h-8 bg-orange-500 rounded-lg flex items-center justify-center"
        >
          <span class="text-white font-bold text-lg">T</span>
        </div>
        <span class="font-semibold text-gray-900">Todocraft</span>
      {:else}
        <div
          class="w-8 h-8 bg-orange-500 rounded-lg flex items-center justify-center mx-auto"
        >
          <span class="text-white font-bold text-lg">T</span>
        </div>
      {/if}
    </div>

    <button
      class="w-8 h-8 flex items-center justify-center rounded-lg text-gray-500 hover:bg-gray-100 transition-colors"
      on:click={onToggle}
      aria-label={isCollapsed ? "Expand" : "Collapse"}
    >
      {#if isCollapsed}
        <ChevronRight size={18} />
      {:else}
        <ChevronLeft size={18} />
      {/if}
    </button>
  </div>

  <!-- Navigation -->
  <nav class="flex-1 py-4 px-3 space-y-1 overflow-y-auto">
    {#each items as item}
      <a
        href={item.href}
        class="flex items-center gap-3 px-3 py-2 rounded-lg transition-colors group
          {isActive(item.href)
          ? 'text-gray-900'
          : 'text-gray-400 hover:bg-orange-50 hover:text-orange-600'}
          {isCollapsed ? 'justify-center' : ''}"
        title={isCollapsed ? item.name : ""}
      >
        <div class={isActive(item.href) ? "p-1 bg-gradient-to-b from-orange-500 to-orange-300 rounded-md" : "p-1 bg-orange-100 text-orange-700 rounded-md"}>
          <item.icon
            size={20}
            class={isActive(item.href)
              ? "text-white"
              : "text-orange-400 group-hover:text-orange-600"}
          />
        </div>
        {#if !isCollapsed}
          <span class="flex-1 text-sm">{item.name}</span>
        {/if}
      </a>
    {/each}
  </nav>

  <!-- Footer -->
  <div class="p-4 border-t border-gray-200">
    {#if !isCollapsed}
      <div class="flex items-center gap-3">
        <div
          class="w-9 h-9 bg-gray-100 rounded-lg flex items-center justify-center"
        >
          <User size={18} class="text-gray-600" />
        </div>
        <div class="flex-1 min-w-0">
          <p class="text-sm font-medium text-gray-900 truncate">John Doe</p>
          <p class="text-xs text-gray-500 truncate">john@example.com</p>
        </div>
        <button
          class="p-2 text-gray-400 hover:text-gray-600 rounded-lg hover:bg-gray-100 transition-colors"
        >
          <LogOut size={16} />
        </button>
      </div>
    {:else}
      <button
        class="w-full flex justify-center p-2 text-gray-400 hover:text-gray-600 rounded-lg hover:bg-gray-100 transition-colors"
        title="Logout"
      >
        <LogOut size={18} />
      </button>
    {/if}
  </div>
</aside>
