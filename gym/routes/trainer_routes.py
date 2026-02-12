from flask import Blueprint, request, jsonify
from services.trainer_service import TrainerService
from flask_jwt_extended import jwt_required, get_jwt_identity

trainer_bp = Blueprint("trainer", __name__)

def is_admin():
    return get_jwt_identity()["role"] == "admin"

@trainer_bp.route("/trainers", methods=["POST"])
@jwt_required()
def add():
    if not is_admin():
        return jsonify({"error": "Admin only"}), 403
    TrainerService.create(request.json)
    return jsonify({"message": "Trainer added"})

@trainer_bp.route("/trainers", methods=["GET"])
@jwt_required()
def view():
    return jsonify([t.to_dict() for t in TrainerService.get_all()])
