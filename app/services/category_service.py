from app import mongo
from bson import ObjectId

def createCategories(data):
    categoryDetails =  {
            "categoryName" : data.get("categoryName"),
            "categorySlug" : data.get("categorySlug"),
            "categoryDesc" : data.get("categoryDesc"),
            "parentCategory" : data.get("parentCategory")
        }
    result = mongo.db.categories.insert_one(categoryDetails)
    return {"message": "Category created", "id": str(result.inserted_id)}

def getAllCategoriesItems():
    categories = list(mongo.db.categories.find())
    for category in categories:
        category["_id"] = str(category["_id"])
    return categories

def getSelectedCategoryItem(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    if category:
        category["_id"] = str(category["_id"])
        return category
    return {"error": "Category not found"}
