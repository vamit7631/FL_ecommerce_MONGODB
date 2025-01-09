class Seller:
    def __init__(self, name, store_name):
        self.name = name
        self.store_name = store_name

    def to_dict(self):
        return {
            "name": self.name,
            "store_name": self.store_name,
        }
