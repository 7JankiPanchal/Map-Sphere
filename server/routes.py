from fastapi import APIRouter, HTTPException
from database import users_collection, places_collection
from schemas import UserCreate, UserLogin, PlaceCreate
from auth import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pw = hash_password(user.password)
    users_collection.insert_one({
        "name": user.name,
        "email": user.email,
        "password": hashed_pw
    })

    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": str(db_user["_id"])})
    return {"access_token": token}

@router.post("/places")
def save_place(place: PlaceCreate):
    places_collection.insert_one(place.dict())
    return {"message": "Place saved"}

@router.get("/places/{user_id}")
def get_places(user_id: str):
    places = list(places_collection.find({"user_id": user_id}, {"_id": 0}))
    return places
