from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .taskModel import Task, TaskStatus
from .userModel import User
