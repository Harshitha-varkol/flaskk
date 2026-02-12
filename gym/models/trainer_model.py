from models.db import db

class GymTrainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(100))
    _specialization = db.Column(db.String(100))
    _experience_years = db.Column(db.Integer)
    _phone = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self._name,
            "specialization": self._specialization,
            "experience_years": self._experience_years,
            "phone": self._phone
        }
