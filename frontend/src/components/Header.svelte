<script>
  import "./header.css";
  import { onMount } from "svelte";
  import {
    User,
    Settings,
    HelpCircle,
    LogOut,
    ChevronDown,
    Search,
    Bell,
    MessageSquare,
    Home,
    UserCircle,
    Mail,
    CheckCheck,
  } from "lucide-svelte";

  export let title = "Dashboard";
  export let user = {
    name: "John Doe",
    email: "john.doe@company.com",
    avatar: "JD",
    role: "Administrator",
    department: "IT",
  };
  export let notifications = [
    { id: 1, text: "New message from Alice", read: false, time: "5m ago" },
    {
      id: 2,
      text: "Project deadline tomorrow",
      read: false,
      time: "1h ago",
    },
    { id: 3, text: "Meeting at 3 PM", read: true, time: "2h ago" },
  ];

  let showUserMenu = false;
  let showNotifications = false;
  let unreadCount = notifications.filter((n) => !n.read).length;

  // Close dropdowns when clicking outside
  function handleClickOutside(event) {
    if (
      !event.target.closest(".user-menu") &&
      !event.target.closest(".notifications-menu")
    ) {
      showUserMenu = false;
      showNotifications = false;
    }
  }

  onMount(() => {
    document.addEventListener("click", handleClickOutside);
    return () => document.removeEventListener("click", handleClickOutside);
  });

  function markAsRead(id) {
    notifications = notifications.map((n) =>
      n.id === id ? { ...n, read: true } : n,
    );
    unreadCount = notifications.filter((n) => !n.read).length;
  }

  function markAllAsRead() {
    notifications = notifications.map((n) => ({ ...n, read: true }));
    unreadCount = 0;
  }
</script>

<header
  class="bg-white border-b border-gray-200 h-16 fixed top-0 right-0 left-64 z-10 transition-all duration-300"
>
  <div class="h-full px-6 flex items-center justify-between">
    <div class="flex items-center gap-4">
      <h1 class="text-xl font-semibold text-gray-900">{title}</h1>
    </div>

    <!-- Right section -->
    <div class="flex items-center gap-3">
      <!-- Search Bar -->
      <div class="relative group">
        <span class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-orange-500 transition-colors">
          <Search size={18} />
        </span>
        <input
          type="text"
          placeholder="Search..."
          class="w-80 pl-10 pr-12 py-2 text-sm border border-gray-200 rounded-lg focus:outline-none focus:border-orange-500 focus:ring-2 focus:ring-orange-100 transition-all"
          aria-label="Search"
        />
        <span
          class="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded"
        >
          ⌘K
        </span>
      </div>

      <!-- User Menu -->
      <div class="relative user-menu">
        <button
          class="flex items-center gap-3 pl-3 pr-2 py-1.5 rounded-lg hover:bg-gray-100 transition-colors border border-transparent hover:border-gray-200"
          on:click={() => {
            showUserMenu = !showUserMenu;
            showNotifications = false;
          }}
          aria-expanded={showUserMenu}
          aria-haspopup="true"
        >
          <div class="flex items-center gap-3">
            <div
              class="w-8 h-8 bg-gradient-to-br from-orange-400 to-orange-600 rounded-lg flex items-center justify-center text-white font-medium text-sm"
            >
              {user.avatar ||
                user.name
                  .split(" ")
                  .map((n) => n[0])
                  .join("")}
            </div>
            <div class="hidden md:block text-left">
              <p class="text-sm font-medium text-gray-900">
                {user.name}
              </p>
              <p class="text-xs text-gray-500">{user.role}</p>
            </div>
          </div>
          <ChevronDown size={16} class="text-gray-400 transition-transform {showUserMenu ? 'rotate-180' : ''}"/>
        </button>

        <!-- User Dropdown Menu -->
        {#if showUserMenu}
          <div class="absolute right-0 mt-2 w-64 bg-white rounded-lg shadow-lg border border-gray-200 py-1 z-50">
            <!-- User Info -->
            <div class="px-4 py-3 border-b border-gray-100">
              <p class="text-sm font-medium text-gray-900">
                {user.name}
              </p>
              <p class="text-xs text-gray-500 mt-0.5">
                {user.email}
              </p>
              <p class="text-xs text-gray-400 mt-1">
                {user.department}
              </p>
            </div>

            <!-- Menu Items -->
            <a href="/profile" class="flex items-center gap-3 px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 transition-colors">
              <UserCircle size={16} class="text-gray-500" />
              Profile
            </a>

            <a href="/settings" class="flex items-center gap-3 px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 transition-colors">
              <Settings size={16} class="text-gray-500" />
              Settings
            </a>

            <a href="/help" class="flex items-center gap-3 px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 transition-colors">
              <HelpCircle size={16} class="text-gray-500" />
              Help & Support
            </a>

            <hr class="my-1 border-gray-200" />

            <button class="w-full flex items-center gap-3 px-4 py-2 text-sm text-red-600 hover:bg-red-50 transition-colors"
              on:click={() => console.log("Logout")}
            >
              <LogOut size={16} />
              Logout
            </button>
          </div>
        {/if}
      </div>
    </div>
  </div>
</header>

<!-- Add margin top to main content to account for fixed header -->
<style>
  :global(main) {
    margin-top: 4rem;
  }
</style>
