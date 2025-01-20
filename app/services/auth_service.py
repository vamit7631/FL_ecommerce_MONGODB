from app import mongo
from bson import ObjectId
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

def buyer_authentication_layer(email, password):
    buyer = mongo.db.buyers.find_one({"email": email})
    if buyer and check_password_hash(buyer["password"], password):
        print(f"Creating token with identity: {{'id': {str(buyer['_id'])}, 'email': {email}}}")

        token = create_access_token(identity=str(buyer["_id"]))
        print(f"Generated Token: {token}")
        return token
    return None
