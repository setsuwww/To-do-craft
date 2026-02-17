import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  headers: { 'Content-Type': 'application/json' },
  withCredentials: true,
});

export const fetchTasks = (search = '', status = '') => api.get('/tasks', { params: { search, status } });
export const createTask = (task) => api.post('/tasks', task);
export const updateTask = (id, data) => api.put(`/tasks/${id}`, data);
export const deleteTask = (id) => api.delete(`/tasks/${id}`);
export const toggleTaskStatus = (id) => api.patch(`/tasks/${id}/toggle`);
