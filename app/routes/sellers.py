from flask import Blueprint, request, jsonify
from app.services.seller_service import create_seller, get_sellers, get_seller_by_id, update_seller, delete_seller

sellers_bp = Blueprint('sellers', __name__)

@sellers_bp.route('/', methods=['POST'])
def create():
    data = request.json
    response = create_seller(data)
    return jsonify(response), 201

@sellers_bp.route('/', methods=['GET'])
def read_all():
    response = get_sellers()
    return jsonify(response), 200

@sellers_bp.route('/<string:seller_id>', methods=['GET'])
def read_one(seller_id):
    response = get_seller_by_id(seller_id)
    return jsonify(response), 200

@sellers_bp.route('/<string:seller_id>', methods=['PUT'])
def update(seller_id):
    data = request.json
    response = update_seller(seller_id, data)
    return jsonify(response), 200

@sellers_bp.route('/<string:seller_id>', methods=['DELETE'])
def delete(seller_id):
    response = delete_seller(seller_id)
    return jsonify(response), 204
