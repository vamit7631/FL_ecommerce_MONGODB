class Buyer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "phone_number": self.phone_number,
            "email": self.email,
            "password": self.password
        }
