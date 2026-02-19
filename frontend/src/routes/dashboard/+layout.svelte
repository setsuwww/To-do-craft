<script>
    import "../../app.css";
    import Sidebar from "../../components/Sidebar.svelte";
    import Header from "../../components/Header.svelte";

    import {
        LayoutDashboard,
        Layout,
        CalendarDays,
        ListTodo,
        Tag,
        History,
    } from "lucide-svelte";

    const menuItems = [
        { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
        { name: "Tasks", href: "/dashboard/tasks", icon: ListTodo },
        { name: "Boards", href: "/dashboard/boards", icon: Layout },
        { name: "Categories", href: "/dashboard/categories", icon: Tag },
        { name: "Schedules", href: "/dashboard/schedules", icon: CalendarDays },
        { name: "Histories", href: "/dashboard/histories", icon: History },
    ];

    let isSidebarCollapsed = false;

    const toggleSidebar = () => {
        isSidebarCollapsed = !isSidebarCollapsed;
    };
</script>

<div class="flex min-h-screen bg-gray-100">
    <!-- Sidebar dengan jarak dari tepi -->
    <Sidebar
        isCollapsed={isSidebarCollapsed}
        onToggle={toggleSidebar}
        items={menuItems}
    />

    <!-- Main Content - sejajar dengan sidebar -->
    <main class="transition-all duration-300 flex-1 p-4">
        <div class="bg-gray-200/60 rounded-2xl border border-gray-200 shadow-sm p-4">
            <slot />
        </div>
    </main>
</div>

<style>
    /* Smooth transition for main content margin */
    main {
        transition-property: margin-left;
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
        transition-duration: 300ms;
    }
</style>
