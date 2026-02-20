from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["mapsphere"]
users_collection = db["users"]
places_collection = db["places"]
