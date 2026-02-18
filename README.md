# ToDoCraft

**ToDoCraft** adalah aplikasi manajemen tugas modern yang dirancang untuk produktivitas tim dan individu. Aplikasi ini menyediakan fitur lengkap seperti
**Tasks, Board, Schedules, Categories, Histories, Analytics**, serta sistem **Autentikasi dan admin user**. UI modern dan interaktif memudahkan pengelolaan tugas secara efisien.

---

## Fitur Utama

### Task Management
- CRUD task (Create, Read, Update, Delete)
- Set status: Pending, In Progress, Completed, Failed
- Assign task ke kategori tertentu
- Update task secara real-time
- Task description, due date, priority

### Board & Kanban
- Kanban board untuk melihat progress task
- Drag & drop task antar status
- Multiple board support

### Schedule
- Calendar view untuk jadwal tugas
- Reminder dan due date highlight

### Category & Tags
- Buat kategori & tag untuk task
- Filter task berdasarkan kategori atau tag

### History & Audit
- Log aktivitas task (dibuat, diubah, dihapus)
- Melacak perubahan status dan siapa yang mengubahnya

### Dashboard Analytics
- Grafik progress task per kategori
- Status task overview (Pending, Success, Failed)
- Statistik harian/mingguan/bulanan

### User Management
- Register, Login, Logout
- Admin dashboard untuk mengelola user
- Role-based access: Admin & User
- JWT-based authentication

---

## Stack Teknologi

- **Frontend:** SvelteKit, Tailwindcss, Axios
- **Backend:** Flask, & Python ekosistem
- **Database:** MySQL

---

## Instalasi

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
cp .env.example .env

python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
