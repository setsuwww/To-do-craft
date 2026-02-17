import adapter from '@sveltejs/adapter-auto';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		// adapter-auto only supports some environments, see https://svelte.dev/docs/kit/adapter-auto for a list.
		// If your environment is not supported, or you settled on a specific environment, switch out the adapter.
		// See https://svelte.dev/docs/kit/adapters for more information about adapters.
		adapter: adapter()
	}
};

export default config;

// Dashboard	Ringkasan umum: statistik, grafik, recent activity
// Boards	Daftar board project, card-board interaktif
// Schedules	Kalender, jadwal tugas, timeline
// Tasks	Daftar tasks, status, priority, filter/search
// Categories	Daftar kategori untuk tugas/boards, opsi CRUD
// Histories	Riwayat aktivitas user, log update, task history
