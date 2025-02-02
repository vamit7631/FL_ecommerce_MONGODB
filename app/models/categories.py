class ProductCategory:
    def __init__(self, categoryName, categorySlug, categoryDesc, parentCategory):
        self.categoryName = categoryName
        self.categorySlug = categorySlug
        self.categoryDesc = categoryDesc
        self.parentCategory = parentCategory

    def to_dict(self):
        return {
            "categoryName" : self.categoryName,
            "categorySlug" : self.categorySlug,
            "categoryDesc" : self.categoryDesc,
            "parentCategory" : self.parentCategory
        }
        
