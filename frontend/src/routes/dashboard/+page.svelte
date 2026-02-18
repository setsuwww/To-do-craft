<script>
  import DashboardStats from './DashboardStats.svelte';
  import DashboardDiagram from './DashboardDiagram.svelte';
  import DashboardNavigation from './DashboardNavigation.svelte';
  import { CheckCircle, Layout, Calendar, FolderOpen } from 'lucide-svelte';

  const stats = [
    { title: "Total Tasks", value: 128, icon: CheckCircle, trend: "+12%", trendUp: true },
    { title: "Active Boards", value: 6, icon: Layout, trend: "+2", trendUp: true },
    { title: "Schedules Today", value: 4, icon: Calendar, trend: "-1", trendUp: false },
    { title: "Categories", value: 12, icon: FolderOpen, trend: "+3", trendUp: true },
  ];

  const chartData = [30, 50, 40, 70, 60, 80, 65];
  const chartLabels = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];

  const recentActivities = [
    { id: 1, action: 'Task completed', time: '5m ago', user: 'You' },
    { id: 2, action: 'Board created', time: '1h ago', user: 'John' }
  ];
</script>

<div class="space-y-8">
  <DashboardStats {stats} />

  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
    <div class="lg:col-span-2">
      <DashboardDiagram {chartData} {chartLabels} />
    </div>

    <DashboardNavigation {recentActivities} />
  </div>
</div>
