from flask import Blueprint, request, jsonify
from services.mens_service import *

mens_bp = Blueprint("mens", __name__)

@mens_bp.route("/api/mens", methods=["POST"])
def add_mens():
    return create_mens(request.json)

@mens_bp.route("/api/mens", methods=["GET"])
def all_mens():
    items = get_all_mens()
    return jsonify([{
        "id": m.id,
        "name": m.name,
        "price": m.price,
        "brand": m.brand,
        "size": m.size,
        "stock": m.stock
    } for m in items])

@mens_bp.route("/api/mens/<int:id>", methods=["GET"])
def one_mens(id):
    m = get_mens(id)
    return jsonify({
        "id": m.id,
        "name": m.name,
        "price": m.price,
        "brand": m.brand,
        "size": m.size,
        "stock": m.stock
    })

@mens_bp.route("/api/mens/<int:id>", methods=["PUT"])
def edit_mens(id):
    return update_mens(id, request.json)

@mens_bp.route("/api/mens/<int:id>", methods=["DELETE"])
def remove_mens(id):
    return delete_mens(id)
