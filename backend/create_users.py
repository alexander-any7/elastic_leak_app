from app2 import db, User, bcrypt, app

with app.app_context():
    db.create_all()
    if User.query.filter_by(username="email@email.com").first():
        print("❗ The user already exists.")
    else:
        pw_hash = bcrypt.generate_password_hash("password").decode("utf-8")
        user = User(username="email@email.com", password_hash=pw_hash)
        db.session.add(user)
        db.session.commit()
        print("✅ User created successfully.")
