from flask import Blueprint, request, jsonify
from services.gymrat_service import GymRatService
from flask_jwt_extended import jwt_required, get_jwt_identity

gymrat_bp = Blueprint("gymrat", __name__)

def is_admin():
    return get_jwt_identity()["role"] == "admin"

@gymrat_bp.route("/rats", methods=["POST"])
@jwt_required()
def add():
    if not is_admin():
        return jsonify({"error": "Admin only"}), 403
    GymRatService.create(request.json)
    return jsonify({"message": "GymRat added"})

@gymrat_bp.route("/rats", methods=["GET"])
@jwt_required()
def view():
    return jsonify([r.to_dict() for r in GymRatService.get_all()])
