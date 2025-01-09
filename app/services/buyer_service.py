from app import mongo
from bson import ObjectId

def create_buyer(data):
    buyer = {
        "name": data.get("name"),
        "email": data.get("email"),
    }
    result = mongo.db.buyers.insert_one(buyer)
    return {"message": "Buyer created", "id": str(result.inserted_id)}

def get_buyers():
    print("testdata")
    buyers = list(mongo.db.buyers.find())
    for buyer in buyers:
        buyer["_id"] = str(buyer["_id"])
    return buyers

def get_buyer_by_id(buyer_id):
    buyer = mongo.db.buyers.find_one({"_id": ObjectId(buyer_id)})
    if buyer:
        buyer["_id"] = str(buyer["_id"])
        return buyer
    return {"error": "Buyer not found"}


def update_buyer(buyer_id, data):
    result = mongo.db.buyers.update_one(
        {"_id": ObjectId(buyer_id)},
        {"$set": data}
    )
    if result.matched_count:
        return {"message": "Buyer updated"}
    return {"error": "Buyer not found"}


def delete_buyer(buyer_id):
    result = mongo.db.buyers.delete_one({"_id": ObjectId(buyer_id)})
    if result.deleted_count:
        return {"message": "Buyer deleted"}
    return {"error": "Buyer not found"}