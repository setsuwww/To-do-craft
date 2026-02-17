from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.userModel import User

def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify({"access_token": access_token})

@jwt_required()
def dashboard():
    current_user_id = get_jwt_identity()
    print("DEBUG: current_user_id =", current_user_id)
    if not current_user_id:
        return jsonify({"error": "JWT token invalid or missing"}), 422

    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": f"Hello {user.email}, welcome to your dashboard"})
