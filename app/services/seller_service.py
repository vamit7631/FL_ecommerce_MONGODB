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