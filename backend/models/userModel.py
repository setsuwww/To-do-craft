from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)         # <-- baru
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.USER)  # <-- baru

    # simpan password dengan hash
    def set_password(self, plain_password):
        self.password = generate_password_hash(plain_password)

    # cek password
    def check_password(self, plain_password):
        return check_password_hash(self.password, plain_password)
