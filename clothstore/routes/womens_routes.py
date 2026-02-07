from flask import Blueprint, request, jsonify
from services.womens_service import *

womens_bp = Blueprint("womens", __name__)

@womens_bp.route("/api/womens", methods=["POST"])
def add_womens():
    return create_womens(request.json)

@womens_bp.route("/api/womens", methods=["GET"])
def all_womens():
    items = get_all_womens()
    return jsonify([{
        "id": w.id,
        "name": w.name,
        "price": w.price,
        "brand": w.brand,
        "size": w.size,
        "stock": w.stock
    } for w in items])

@womens_bp.route("/api/womens/<int:id>", methods=["GET"])
def one_womens(id):
    w = get_womens(id)
    return jsonify({
        "id": w.id,
        "name": w.name,
        "price": w.price,
        "brand": w.brand,
        "size": w.size,
        "stock": w.stock
    })

@womens_bp.route("/api/womens/<int:id>", methods=["PUT"])
def edit_womens(id):
    return update_womens(id, request.json)

@womens_bp.route("/api/womens/<int:id>", methods=["DELETE"])
def remove_womens(id):
    return delete_womens(id)
