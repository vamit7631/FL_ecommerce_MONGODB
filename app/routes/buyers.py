from flask import Blueprint, request, jsonify
from app.services.buyer_service import create_buyer, get_buyers, get_buyer_by_id, update_buyer, delete_buyer

buyers_bp = Blueprint("buyers", __name__)

@buyers_bp.route('/', methods=['POST'])
def create():
    data = request.json
    response = create_buyer(data)
    return jsonify(response), 201

@buyers_bp.route("/", methods=["GET"])
def read_all():
    print("Amit Verma")
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