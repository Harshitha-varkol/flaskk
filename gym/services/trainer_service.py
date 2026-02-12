from repositories.trainer_repo import TrainerRepo
from models.trainer_model import GymTrainer

class TrainerService:
    @staticmethod
    def create(data):
        t = GymTrainer(
            _name=data["name"],
            _specialization=data["specialization"],
            _experience_years=data["experience_years"],
            _phone=data["phone"]
        )
        TrainerRepo.save(t)

    @staticmethod
    def get_all():
        return TrainerRepo.get_all()

    @staticmethod
    def delete(id):
        t = TrainerRepo.get_by_id(id)
        TrainerRepo.delete(t)
