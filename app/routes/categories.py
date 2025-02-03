from flask import jsonify, Blueprint, request
from app.services.category_service import createCategories, getAllCategoriesItems, getSelectedCategoryItem, deleteSelectedCategoryItem, updateSelectedCategoryItem

categories_bp = Blueprint("categories", __name__)

@categories_bp.route("/", methods=['POST'])
def createCategory():
    data = request.json
    response = createCategories(data)
    return jsonify(response), 201

@categories_bp.route("/", methods=["GET"])
def getAllCategories():
    response = getAllCategoriesItems()
    return jsonify(response), 200


@categories_bp.route("/<string:category_id>", methods=["GET"])
def getSelectedCategory(category_id):
    response = getSelectedCategoryItem(category_id)
    return jsonify(response), 200

@categories_bp.route("/<string:category_id>", methods=["PUT"])
def updateSelectedCategory(category_id):
    data = request.json
    response = updateSelectedCategoryItem(category_id, data)
    return jsonify(response), 200

@categories_bp.route("/<string:category_id>", methods=["DELETE"])
def deleteSelectedCategory(category_id):
    response = deleteSelectedCategoryItem(category_id)
    return jsonify(response), 200