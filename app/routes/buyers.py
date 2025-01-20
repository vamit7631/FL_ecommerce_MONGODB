from flask import Blueprint, request, jsonify
from app.services.buyer_service import create_buyer, get_buyers, get_buyer_by_id, update_buyer, delete_buyer
from app.services.auth_service import buyer_authentication_layer
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity

buyers_bp = Blueprint("buyers", __name__)

@buyers_bp.route('/', methods=['POST'])
def create():
    data = request.json
    response = create_buyer(data)
    return jsonify(response), 201

@buyers_bp.route("/", methods=["GET"])
def read_all():
    response = get_buyers()
    return jsonify(response), 200

@buyers_bp.route('/<string:buyer_id>', methods=['GET'])
def read_one(buyer_id):
    response = get_buyer_by_id(buyer_id)
    return jsonify(response), 200


@buyers_bp.route('/<string:buyer_id>', methods=['PUT'])
def update(buyer_id):
    data = request.json
    response = update_buyer(buyer_id, data)
    return jsonify(response), 200

@buyers_bp.route('/<string:buyer_id>', methods=['DELETE'])
def delete(buyer_id):
    response = delete_buyer(buyer_id)
    return jsonify(response), 204


@buyers_bp.route('/login', methods=['POST'])
def buyerlogin():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    token = buyer_authentication_layer(email, password)
    print(token,"======testing3")
    if token:
        return jsonify({"access_token": token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# @buyers_bp.route('/profile', methods=['GET'])
# def get_profile():
#     try:
#         verify_jwt_in_request()
#         identity = get_jwt_identity()
#         print(f"JWT Identity: {identity}")
#         return jsonify({"message": "Access granted", "user": identity}), 200
#     except Exception as e:
#         print(f"Error during JWT verification: {str(e)}")
#         return jsonify({"message": "Authentication failed", "error": str(e)}), 401

