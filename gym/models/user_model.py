from models.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String(50), unique=True)
    _password = db.Column(db.String(200))
    _role = db.Column(db.String(20))

    def get_username(self): return self._username
    def get_password(self): return self._password
    def get_role(self): return self._role
