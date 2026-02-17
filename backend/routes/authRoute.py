from flask import Blueprint
from controllers.authController import login_user, dashboard

auth_bp = Blueprint('auth', __name__)
auth_bp.route('/login', methods=['POST'])(login_user)
auth_bp.route('/dashboard', methods=['GET'])(dashboard)
