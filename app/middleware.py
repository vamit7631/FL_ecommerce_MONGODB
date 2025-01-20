from flask import Flask, request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, JWTManager, get_jwt

def auth_middleware(app):
    @app.before_request
    def check_authentication():
        excluded_routes = ["/api/buyers/login"]
        if request.path in excluded_routes:
            return

        print(f"Request Headers: {request.headers}") 
        try:
            print("Attempting JWT verification...")
            verify_jwt_in_request()
            identity = get_jwt_identity()

            print(f"JWT Verified: {identity}")
        except Exception as e:
            return jsonify({"message": "Authentication failed", "error": str(e)}), 401