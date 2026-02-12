from models.user_model import User
from models.db import db

class UserRepo:
    @staticmethod
    def find_by_username(u):
        return User.query.filter_by(_username=u).first()

    @staticmethod
    def save(u):
        db.session.add(u)
        db.session.commit()
