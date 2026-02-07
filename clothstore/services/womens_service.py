from models.womens_model import Womens
from extensions.db import db

def create_womens(data):
    item = Womens(**data)
    db.session.add(item)
    db.session.commit()
    return {"message": "Womens item added"}

def get_all_womens():
    return Womens.query.all()

def get_womens(id):
    return Womens.query.get(id)

def update_womens(id, data):
    item = Womens.query.get(id)
    for k, v in data.items():
        setattr(item, k, v)
    db.session.commit()
    return {"message": "Womens item updated"}

def delete_womens(id):
    item = Womens.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return {"message": "Womens item deleted"}
