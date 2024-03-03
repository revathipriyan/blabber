from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @classmethod
    def create_user(cls, username, password):
        new_user = cls(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
