from app import mongo
from bson import ObjectId

def createProductItem(data):
    print("store Data")
    productItem = {
        "productName": data.get("productName"),
        "category": data.get("category"),
        "stockAvailability": data.get("stockAvailability"),
    }
    result = mongo.db.products.insert_one(productItem)
    return {"message": "Product created", "id": str(result.inserted_id)}

def getAllProductItem():
    products = list(mongo.db.products.find())
    for product in products:
        product["_id"] = str(product["_id"])
    return products

def getProductDetailsById(product_id):
    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    if product:
        product["_id"] = str(product["_id"])
        return product
    return {"error": "Product not found"}

def deleteProductDetailsById(product_id):
    response = mongo.db.products.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count:
        return {"message": "Product deleted"}
    return {"error": "Product not found"}