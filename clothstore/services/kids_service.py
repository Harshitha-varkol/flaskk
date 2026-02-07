from models.kids_model import Kids
from extensions.db import db

def create_kids(data):
    if isinstance(data, list):
        for record in data:
            db.session.add(Kids(**record))
        db.session.commit()
        return {"message": "Bulk kids items added"}
    else:
        item = Kids(**data)
        db.session.add(item)
        db.session.commit()
        return {"message": "Kids item added"}


def get_all_kids():
    return Kids.query.all()

def get_kids(id):
    return Kids.query.get(id)

def update_kids(id, data):
    item = Kids.query.get(id)
    for k, v in data.items():
        setattr(item, k, v)
    db.session.commit()
    return {"message": "Kids item updated"}

def delete_kids(id):
    item = Kids.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return {"message": "Kids item deleted"}
