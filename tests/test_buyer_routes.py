from app.routes.buyers import get_buyer_by_id

def test_get_buyers(client):
    response = client.get("/api/buyers/")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_buyer(client):
    response = client.post("/api/buyers/", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 201
    response_data = response.get_json()

    assert "id" in response_data  # Check if 'id' is present
    assert "message" in response_data
    assert response_data["message"] == "Buyer created"

# tests/test_buyer_routes.py

def test_read_one_buyer(client, mocker):
    # Mock the function `get_buyer_by_id` to return a predefined buyer object
    mock_response = {
        "id": "677fdf2d9d595a27d46cfe4e",
        "name": "Alice",
        "email": "alice@example.com"
    }
    mocker.patch("app.routes.buyers.get_buyer_by_id", return_value=mock_response)  # Correct path

    # Make the GET request
    response = client.get("/api/buyers/677fdf2d9d595a27d46cfe4e")
    
    # Assert the response status and data
    assert response.status_code == 200
    response_data = response.get_json()  # Use `.get_json()` for Flask
    assert response_data["id"] == "677fdf2d9d595a27d46cfe4e"
    assert response_data["name"] == "Alice"
    assert response_data["email"] == "alice@example.com"


def test_update_buyer(client, mocker):
    # Mock the function `get_buyer_by_id` to return a predefined buyer object
    updated_data = {
        "name": "Alice Updated",
        "email": "alice_updated@example.com"
    }
    mock_response = {
        "id": "677fdf2d9d595a27d46cfe4e",  # Keep the original buyer ID
        "name": "Alice Updated",
        "email": "alice_updated@example.com"
    }

    mocker.patch("app.routes.buyers.update_buyer", return_value=mock_response)

    response = client.put(
        "/api/buyers/677fdf2d9d595a27d46cfe4e", 
        json=updated_data
    )

    assert response.status_code == 200
    
    # Assert the response JSON matches the updated buyer data
    response_data = response.get_json()
    assert response_data["id"] == "677fdf2d9d595a27d46cfe4e"
    assert response_data["name"] == "Alice Updated"
    assert response_data["email"] == "alice_updated@example.com"

def test_delete_buyer(client, mocker):
    # Mock the `delete_buyer` function to simulate successful deletion
    mock_response = {"message": "Buyer deleted successfully"}  # Customize this as needed
    
    # Mock `delete_buyer` method to return the mock response when called
    mocker.patch("app.routes.buyers.delete_buyer", return_value=mock_response)
    
    # Send DELETE request to the `/api/buyers/<buyer_id>` endpoint
    response = client.delete("/api/buyers/677fdf2d9d595a27d46cfe4e")
    
    # Assert the response status code is 204 (No Content)
    assert response.status_code == 204