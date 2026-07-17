from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


@router.post("/register")
async def register(user: UserRegister):

    return {
        "success": True,
        "message": "User registered successfully",
        "username": user.username,
        "email": user.email
    }


@router.post("/login")
async def login(user: UserLogin):

    return {
        "success": True,
        "message": "Login successful",
        "email": user.email
    }