<script>
    import "../../app.css";
    import Sidebar from "../../components/Sidebar.svelte";
    import Header from "../../components/Header.svelte";

    import {
        LayoutDashboard,
        Layout,
        Calendar,
        ListTodo,
        Tag,
        History,
    } from "lucide-svelte";

    const menuItems = [
        { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
        { name: "Tasks", href: "/dashboard/tasks", icon: ListTodo },
        { name: "Boards", href: "/dashboard/boards", icon: Layout },
        { name: "Categories", href: "/dashboard/categories", icon: Tag },
        { name: "Schedules", href: "/dashboard/schedules", icon: Calendar },
        { name: "Histories", href: "/dashboard/histories", icon: History },
    ];

    let isSidebarCollapsed = false;

    const toggleSidebar = () => {
        isSidebarCollapsed = !isSidebarCollapsed;
    };
</script>

<div class="flex min-h-screen">
    <Sidebar
        isCollapsed={isSidebarCollapsed}
        onToggle={toggleSidebar}
        items={menuItems}
    />

    <div class="flex-1 flex flex-col">
        <Header title="Dashboard"/>

        <main class="flex-1 bg-gray-100 p-6">
            <slot />
        </main>
    </div>
</div>

<style>
    main {
        min-height: calc(100vh - 64px); /* jika header tinggi 16 h = 64px */
    }
</style>
