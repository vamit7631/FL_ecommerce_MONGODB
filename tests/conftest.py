import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def app():
    # Set up the Flask app in testing mode
    app = create_app()
    app.config.update({
        "TESTING": True,
        "MONGO_URI": "mongodb://localhost:27017/ecommerceApp"  # Use a test database
    })
    yield app

@pytest.fixture
def client(app):
    # Return a test client for making requests
    return app.test_client()

@pytest.fixture
def runner(app):
    # Return a test runner for CLI commands
    return app.test_cli_runner()
