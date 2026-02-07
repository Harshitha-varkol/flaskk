from extensions.db import db

class Mens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    brand = db.Column(db.String(100))
    size = db.Column(db.String(20))
    stock = db.Column(db.Integer)
