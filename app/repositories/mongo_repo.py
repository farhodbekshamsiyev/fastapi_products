from app.repositories.base_repo import ProductRepository
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["shop_inventory"]
# Not tested yet
# This is a MongoDB repository for managing products in a shop inventory system.

class MongoProductRepository(ProductRepository):
    def __init__(self):
        self.collection = db["products"]

    def create(self, data: dict):
        result = self.collection.insert_one(data)
        return {**data, "_id": str(result.inserted_id)}

    def list_all(self):
        return [{**item, "_id": str(item["_id"])} for item in self.collection.find()]

    def get(self, product_id: str):
        item = self.collection.find_one({"_id": ObjectId(product_id)})
        if item:
            item["_id"] = str(item["_id"])
        return item

    def update(self, product_id: str, data: dict):
        result = self.collection.update_one({"_id": ObjectId(product_id)}, {"$set": data})
        if result.modified_count:
            return self.get(product_id)
        return None

    def delete(self, product_id: str):
        result = self.collection.delete_one({"_id": ObjectId(product_id)})
        return result.deleted_count > 0

    def get_products_by_catalog(self, catalog_id: str):
        return [{**item, "_id": str(item["_id"])} for item in self.collection.find({"catalog_id": catalog_id})]

    def assign_product_to_catalog(self, product_id: str, catalog_id: str):
        result = self.collection.update_one({"_id": ObjectId(product_id)}, {"$set": {"catalog_id": catalog_id}})
        if result.modified_count:
            return self.get(product_id)
        return None

def get_mongo_repo():
    yield MongoProductRepository()
