from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Task, TaskStatus

@jwt_required()
def get_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return jsonify({
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "description": t.description,
                "status": t.status.value,
                "created_at": t.created_at.isoformat(),
                "updated_at": t.updated_at.isoformat()
            }
            for t in tasks
        ]
    })

@jwt_required()
def create_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()

    return jsonify({
        "task": {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status.value,
            "created_at": task.created_at.isoformat(),
            "updated_at": task.updated_at.isoformat()
        }
    }), 201

@jwt_required()
def update_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if "title" in data: task.title = data["title"]
    if "description" in data: task.description = data["description"]
    if "status" in data:
        try:
            task.status = TaskStatus(data["status"])
        except ValueError:
            return jsonify({"error": "Invalid status"}), 400

    db.session.commit()
    return jsonify({"message": "Task updated"})

@jwt_required()
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})
