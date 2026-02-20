from bson import ObjectId
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


# ---------------------------
# Helper to convert ObjectId
# ---------------------------
def object_id_str(obj_id):
    return str(obj_id)


# ---------------------------
# User DB Model
# ---------------------------
class UserModel:
    @staticmethod
    def create_user(name: str, email: str, hashed_password: str) -> Dict[str, Any]:
        return {
            "name": name,
            "email": email,
            "password": hashed_password,
            "created_at": datetime.utcnow()
        }

    @staticmethod
    def serialize(user) -> Dict[str, Any]:
        return {
            "id": object_id_str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "created_at": user.get("created_at")
        }


# ---------------------------
# Place DB Model (Geospatial)
# ---------------------------
class PlaceModel:
    @staticmethod
    def create_place(user_id: str, name: str, latitude: float, longitude: float):
        return {
            "user_id": user_id,
            "name": name,
            "location": {
                "type": "Point",
                "coordinates": [longitude, latitude]  # GeoJSON format
            },
            "created_at": datetime.utcnow()
        }

    @staticmeth
