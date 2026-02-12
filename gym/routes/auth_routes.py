from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    d = request.json
    AuthService.register(d["username"], d["password"], d["role"])
    return jsonify({"message": "User created"})

@auth_bp.route("/login", methods=["POST"])
def login():
    d = request.json
    user = AuthService.authenticate(d["username"], d["password"])
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity={
        "username": user.get_username(),
        "role": user.get_role()
    })
    return jsonify({"token": token})
