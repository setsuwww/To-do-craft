from flask import request, jsonify
from models.taskModel import Task, db, TaskStatus
from flask_jwt_extended import jwt_required

# Ambil semua task, optional filter status & search
@jwt_required()
def get_tasks():
    status = request.args.get('status')
    search = request.args.get('search', '')

    query = Task.query
    if status in TaskStatus._value2member_map_:
        query = query.filter(Task.status == TaskStatus(status))
    if search:
        query = query.filter(Task.title.ilike(f"%{search}%"))

    tasks = query.order_by(Task.created_at.desc()).all()
    return jsonify([{
        "id": t.id,
        "title": t.title,
        "status": t.status.value,
        "created_at": t.created_at.isoformat(),
        "updated_at": t.updated_at.isoformat()
    } for t in tasks]), 200

# Buat task baru
@jwt_required()
def create_task():
    data = request.get_json()
    title = data.get('title')
    status = data.get('status', 'PENDING')

    if not title or status not in TaskStatus._value2member_map_:
        return jsonify({"error": "Title is required and status must be valid"}), 400

    task = Task(title=title, status=TaskStatus(status))
    db.session.add(task)
    db.session.commit()

    return jsonify({
        "id": task.id,
        "title": task.title,
        "status": task.status.value,
        "created_at": task.created_at.isoformat(),
        "updated_at": task.updated_at.isoformat()
    }), 201

# Update task
@jwt_required()
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    title = data.get('title')
    status = data.get('status')

    if title:
        task.title = title
    if status in TaskStatus._value2member_map_:
        task.status = TaskStatus(status)

    db.session.commit()

    return jsonify({
        "id": task.id,
        "title": task.title,
        "status": task.status.value,
        "created_at": task.created_at.isoformat(),
        "updated_at": task.updated_at.isoformat()
    }), 200

# Delete task
@jwt_required()
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200

# Toggle status PENDING -> SUCCESS -> FAILED -> PENDING
@jwt_required()
def toggle_task_status(task_id):
    task = Task.query.get_or_404(task_id)
    cycle = ['PENDING', 'SUCCESS', 'FAILED']
    idx = cycle.index(task.status.value)
    task.status = TaskStatus(cycle[(idx + 1) % len(cycle)])
    db.session.commit()
    return jsonify({"id": task.id, "status": task.status.value}), 200
