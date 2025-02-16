from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "gutendex")

# Create MongoDB Client
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Collections
books_collection = db["books"]
authors_collection = db["authors"]
subjects_collection = db["subjects"]
bookshelves_collection = db["bookshelves"]
languages_collection = db["languages"]
formats_collection = db["formats"]
