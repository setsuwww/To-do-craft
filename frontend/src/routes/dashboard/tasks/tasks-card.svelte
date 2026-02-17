<script context="module">
    export interface Task {
        id: number;
        title: string;
        description: string;
        status: "FAILED" | "PENDING" | "SUCCESS";
    }
</script>

<script lang="ts">
    import { createEventDispatcher } from "svelte";

    export let task: Task;

    const statuses = ["FAILED", "PENDING", "SUCCESS"] as const;

    // Typed Event Dispatcher
    const dispatch = createEventDispatcher<{
        updateStatus: { id: number; status: Task["status"] };
        edit: { task: Task };
        delete: { id: number };
    }>();

    const toggleStatus = () => {
        const currentIndex = statuses.indexOf(task.status);
        const nextIndex = (currentIndex + 1) % statuses.length;
        const newStatus = statuses[nextIndex];
        dispatch("updateStatus", { id: task.id, status: newStatus });
    };

    const handleEdit = () => dispatch("edit", { task });
    const handleDelete = () => dispatch("delete", { id: task.id });
</script>

<div
    class="bg-white p-4 rounded-lg shadow hover:shadow-md transition flex flex-col justify-between"
>
    <div>
        <h3 class="font-semibold text-gray-800 text-lg truncate">
            {task.title}
        </h3>
        <p class="text-gray-500 text-sm mt-1 truncate">{task.description}</p>
    </div>

    <div class="mt-4 flex items-center justify-between">
        <button
            class={`px-2 py-1 rounded-full text-xs font-semibold
        ${task.status === "SUCCESS" ? "bg-green-100 text-green-800" : ""}
        ${task.status === "PENDING" ? "bg-yellow-100 text-yellow-800" : ""}
        ${task.status === "FAILED" ? "bg-red-100 text-red-800" : ""}
        hover:opacity-80 transition`}
            on:click={toggleStatus}
            title="Click to toggle status"
        >
            {task.status}
        </button>

        <div class="flex gap-2">
            <button
                class="px-2 py-1 text-sm text-white bg-blue-600 rounded hover:bg-blue-500 transition"
                on:click={handleEdit}
            >
                Edit
            </button>
            <button
                class="px-2 py-1 text-sm text-white bg-red-600 rounded hover:bg-red-500 transition"
                on:click={handleDelete}
            >
                Delete
            </button>
        </div>
    </div>
</div>
