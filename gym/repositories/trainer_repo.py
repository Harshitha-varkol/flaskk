from models.trainer_model import GymTrainer
from models.db import db

class TrainerRepo:
    @staticmethod
    def save(t):
        db.session.add(t)
        db.session.commit()

    @staticmethod
    def get_all():
        return GymTrainer.query.all()

    @staticmethod
    def get_by_id(id):
        return GymTrainer.query.get(id)

    @staticmethod
    def delete(t):
        db.session.delete(t)
        db.session.commit()
