class Product:
    def __init__(productName, productTitle, category, stockAvailability):
        self.productName = productName
        self.category = category
        self.stockAvailability = stockAvailability
    
    def to_dict(self):
        return {
            "productName" : self.productName,
            "category" : self.category,
            "stockAvailability" : self.stockAvailability
        }
