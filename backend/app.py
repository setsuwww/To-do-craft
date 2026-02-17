from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# model import
from models import db

# route import
from routes.userRoute import user_bp
from routes.authRoute import auth_bp
from routes.taskRoute import task_bp

load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET")

db.init_app(app)
jwt = JWTManager(app)


app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
