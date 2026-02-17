<script>
    import "../../app.css";
    import Sidebar from "../../components/Sidebar.svelte";
    import Header from "../../components/Header.svelte";

    let isSidebarCollapsed = false;

    const menuItems = [
        { name: "Dashboard", href: "/dashboard" },
        { name: "Boards", href: "/boards" },
        { name: "Schedules", href: "/schedules" },
        { name: "Tasks", href: "/tasks" },
        { name: "Categories", href: "/categories" },
        { name: "Histories", href: "/histories" },
    ];

    let currentUser = {
        name: "Mbud",
        email: "mbud@jembut.com",
        avatar: "M",
        role: "Product Manager",
        department: "Product",
    };

    const toggleSidebar = () => {
        isSidebarCollapsed = !isSidebarCollapsed;
    };
</script>

<div class="flex min-h-screen">
    <!-- Sidebar -->
    <Sidebar
        isCollapsed={isSidebarCollapsed}
        onToggle={toggleSidebar}
        items={menuItems}
    />

    <!-- Main Content -->
    <div class="flex-1 flex flex-col">
        <Header
            title="Analytics Dashboard"
            user={currentUser}
            notifications={[
                { id: 1, text: "New comment on your post", read: false, time: "2m ago",},
                { id: 2, text: "Meeting reminder", read: true, time: "1h ago" },
            ]}
        />

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
