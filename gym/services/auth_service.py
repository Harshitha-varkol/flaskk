from repositories.user_repo import UserRepo
from models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:
    @staticmethod
    def register(username, password, role):
        hashed = generate_password_hash(password)
        user = User(_username=username, _password=hashed, _role=role)
        UserRepo.save(user)

    @staticmethod
    def authenticate(username, password):
        user = UserRepo.find_by_username(username)
        if user and check_password_hash(user.get_password(), password):
            return user
        return None
