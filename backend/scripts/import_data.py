import json
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "gutendex"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
books_collection = db["books"]

with open("data/gutendex_dump.json", "r", encoding="utf-8") as f:
    books_data = json.load(f)

books_collection.insert_many(books_data)
print("Data imported successfully!")
