from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.json
    if data.get("username") == "admin" and data.get("password") == "admin":
        token = create_access_token(identity="admin")
        return jsonify(access_token=token)
    return jsonify({"error": "Invalid credentials"}), 401
