from models.db import db

class GymRat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(100))
    _age = db.Column(db.Integer)
    _membership_type = db.Column(db.String(50))
    trainer_id = db.Column(db.Integer, db.ForeignKey("gym_trainer.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self._name,
            "age": self._age,
            "membership_type": self._membership_type,
            "trainer_id": self.trainer_id
        }
