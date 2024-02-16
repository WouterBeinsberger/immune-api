from flask import Blueprint, jsonify
from app.auth import generate_token

token_bp = Blueprint("token", __name__)

@token_bp.route("/token", methods=["GET"])
def generate_token_route():
    token = generate_token()
    return jsonify({"token": token}), 200
