from flask import Blueprint, jsonify, request
from app.auth import generate_token
# from app.config import valid_token
# from app.utils.auth_utils import valid_token

token_bp = Blueprint("token", __name__)

@token_bp.route("/token", methods=["GET"])
def generate_token_route():
    token = generate_token()
    return jsonify({"token": token}), 200
