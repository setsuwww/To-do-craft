from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  # nanti SvelteKit frontend
app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

# Dummy database
USERS = {}

@app.post("/register")
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if email in USERS:
        return jsonify({"error": "User already exists"}), 400

    USERS[email] = {"password": password}
    return jsonify({"success": True})

@app.post("/login")
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = USERS.get(email)
    if not user or user["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@app.get("/profile")
@jwt_required()
def profile():
    user = get_jwt_identity()
    return jsonify(user=user)

if __name__ == "__main__":
    app.run(debug=True)
