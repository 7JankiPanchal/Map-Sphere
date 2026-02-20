from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class PlaceCreate(BaseModel):
    user_id: str
    name: str
    latitude: float
    longitude: float
