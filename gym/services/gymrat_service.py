from repositories.gymrat_repo import GymRatRepo
from models.gymrat_model import GymRat

class GymRatService:
    @staticmethod
    def create(data):
        r = GymRat(
            _name=data["name"],
            _age=data["age"],
            _membership_type=data["membership_type"],
            trainer_id=data["trainer_id"]
        )
        GymRatRepo.save(r)

    @staticmethod
    def get_all():
        return GymRatRepo.get_all()

    @staticmethod
    def delete(id):
        r = GymRatRepo.get_by_id(id)
        GymRatRepo.delete(r)
