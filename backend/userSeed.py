from app import app
from models.userModel import db, User

def seed_user():
    with app.app_context():

        existing_user = User.query.filter_by(email="admin@gmail.com").first()
        if existing_user:
            print("User already exists.")
            return

        user = User(email="admin@gmail.com")
        user.set_password("admin123")

        db.session.add(user)
        db.session.commit()

        print("Admin user created successfully.")

if __name__ == "__main__":
    seed_user()
