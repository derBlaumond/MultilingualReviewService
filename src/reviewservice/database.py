from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "reviews_db"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
reviews_collection = db["reviews"]