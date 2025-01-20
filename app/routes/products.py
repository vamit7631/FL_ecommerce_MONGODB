from flask import Blueprint, request, jsonify
from app.services.product_service import createProductItem, getAllProductItem, getProductDetailsById

products_bp = Blueprint('products', __name__)


@products_bp.route('/' , methods=['POST'])
def productCreate():
    data = request.json
    response = createProductItem(data)
    return jsonify(response), 201


@products_bp.route('/', methods=['GET'])
def getAllProducts():
    response = getAllProductItem()
    return jsonify(response), 200

@products_bp.route('/<string:product_id>', methods=['GET'])
def getProductItem(product_id):
    response = getProductDetailsById(product_id)
    return jsonify(response), 200