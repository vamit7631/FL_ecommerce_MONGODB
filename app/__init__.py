from flask import Flask 
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from app.config import Config
from app.middleware import auth_middleware

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object(Config)
    
    # Initialize MongoDB
    mongo.init_app(app)

    jwt.init_app(app)

    # auth_middleware(app)
    # Register Blueprints
    from app.routes import buyers_bp, sellers_bp, products_bp
    app.register_blueprint(buyers_bp, url_prefix="/api/buyers")
    app.register_blueprint(sellers_bp, url_prefix="/api/sellers")
    app.register_blueprint(products_bp, url_prefix="/api/products")    

    
    return app