from flask import Blueprint
from controllers.authController import login_user, dashboard, get_current_user

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/login', methods=['POST'])(login_user)
auth_bp.route('/dashboard', methods=['GET'])(dashboard)
auth_bp.route('/current_user', methods=['GET'])(get_current_user)
