import re 

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PHONE_REGEX = r'^\d{10}$'  # Assumes 10-digit phone number

def validate_buyer_data(data):
    """
    Validates buyer data before processing.
    Returns an error response if invalid, otherwise returns None.
    """
    if not data.get("email") or not re.match(EMAIL_REGEX, data["email"]):
        return {"message": "Invalid email format"}, 400

    if not data.get("phone_number") or not re.match(PHONE_REGEX, data["phone_number"]):
        return {"message": "Invalid phone number format (must be 10 digits)"}, 400

    if not data.get("password") or len(data["password"]) < 6:
        return {"message": "Password must be at least 6 characters long"}, 400

    return None  # No validation errors

