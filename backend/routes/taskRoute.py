from flask import Blueprint

from controllers.taskController import (
    get_tasks,
    create_task,
    update_task,
    delete_task,
    toggle_task_status
)

task_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

task_bp.route('', methods=['GET'])(get_tasks)
task_bp.route('', methods=['POST'])(create_task)
task_bp.route('/<int:task_id>', methods=['PUT'])(update_task)
task_bp.route('/<int:task_id>', methods=['DELETE'])(delete_task)
task_bp.route('/<int:task_id>/toggle', methods=['PATCH'])(toggle_task_status)
