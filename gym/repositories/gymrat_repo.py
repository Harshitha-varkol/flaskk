from models.gymrat_model import GymRat
from models.db import db

class GymRatRepo:
    @staticmethod
    def save(r):
        db.session.add(r)
        db.session.commit()

    @staticmethod
    def get_all():
        return GymRat.query.all()

    @staticmethod
    def get_by_id(id):
        return GymRat.query.get(id)

    @staticmethod
    def delete(r):
        db.session.delete(r)
        db.session.commit()
