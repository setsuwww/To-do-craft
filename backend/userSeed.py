from app import app
from models.userModel import db, User, UserRole

with app.app_context():
    user = User(name="Rifqi", email="rifqi@gmail.com", role=UserRole.ADMIN)
    user.set_password("password123")

    admin = User(name="Keisya", email="keisya@gmail.com", role=UserRole.USER)
    admin.set_password("password123")

    db.session.add(admin)
    db.session.add(user)
    db.session.commit()
    print("Users seeded successfully!")
