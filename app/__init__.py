from flask import Flask 
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object(Config)
    
    # Initialize MongoDB
    mongo.init_app(app)
    
    # Register Blueprints
    from app.routes import buyers_bp, sellers_bp
    app.register_blueprint(buyers_bp, url_prefix="/api/buyers")
    app.register_blueprint(sellers_bp, url_prefix="/api/sellers")
    
    return app