from models.mens_model import Mens
from extensions.db import db

def create_mens(data):
    item = Mens(**data)
    db.session.add(item)
    db.session.commit()
    return {"message": "Mens item added"}

def get_all_mens():
    return Mens.query.all()

def get_mens(id):
    return Mens.query.get(id)

def update_mens(id, data):
    item = Mens.query.get(id)
    for k, v in data.items():
        setattr(item, k, v)
    db.session.commit()
    return {"message": "Mens item updated"}

def delete_mens(id):
    item = Mens.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return {"message": "Mens item deleted"}
