from flask import Blueprint, request, jsonify
from services.kids_service import *

kids_bp = Blueprint("kids", __name__)

@kids_bp.route("/api/kids", methods=["POST"])
def add_kids():
    return create_kids(request.json)

@kids_bp.route("/api/kids", methods=["GET"])
def all_kids():
    items = get_all_kids()
    return jsonify([{
        "id": k.id,
        "name": k.name,
        "price": k.price,
        "brand": k.brand,
        "size": k.size,
        "stock": k.stock
    } for k in items])

@kids_bp.route("/api/kids/<int:id>", methods=["GET"])
def one_kids(id):
    k = get_kids(id)
    return jsonify({
        "id": k.id,
        "name": k.name,
        "price": k.price,
        "brand": k.brand,
        "size": k.size,
        "stock": k.stock
    })

@kids_bp.route("/api/kids/<int:id>", methods=["PUT"])
def edit_kids(id):
    return update_kids(id, request.json)

@kids_bp.route("/api/kids/<int:id>", methods=["DELETE"])
def remove_kids(id):
    return delete_kids(id)
