from app import mongo
from bson import ObjectId

def create_seller(data):
    print("store Data")
    seller = {
        "name": data.get("name"),
        "store_name": data.get("store_name"),
    }
    result = mongo.db.sellers.insert_one(seller)
    return {"message": "Seller created", "id": str(result.inserted_id)}

def get_sellers():
    sellers = list(mongo.db.sellers.find())
    for seller in sellers:
        seller["_id"] = str(seller["_id"])
    return sellers

def get_seller_by_id(seller_id):
    seller = mongo.db.sellers.find_one({"_id": ObjectId(seller_id)})
    if seller:
        seller["_id"] = str(seller["_id"])
        return seller
    return {"error": "Seller not found"}

def update_seller(seller_id, data):
    result = mongo.db.sellers.update_one(
        {"_id": ObjectId(seller_id)},
        {"$set": data}
    )
    if result.matched_count:
        return {"message": "Seller updated"}
    return {"error": "Seller not found"}

def delete_seller(seller_id):
    response = mongo.db.sellers.delete_one({"_id": ObjectId(seller_id)})
    if result.deleted_count:
        return {"message": "Seller deleted"}
    return {"error": "Seller not found"}