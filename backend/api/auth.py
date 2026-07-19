from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from database.crud import get_user_by_email, create_user
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserRegister(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


@router.post("/register")
async def register(user: UserRegister):
    existing = await get_user_by_email(user.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = pwd_context.hash(user.password)
    user_data = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }
    await create_user(user_data)

    return {
        "success": True,
        "message": "User registered successfully",
        "name": user.name,
        "email": user.email
    }


@router.post("/login")
async def login(user: UserLogin):
    db_user = await get_user_by_email(user.email)
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    return {
        "success": True,
        "message": "Login successful",
        "access_token": "demo-token-" + db_user["email"],
        "token_type": "bearer",
        "user": {
            "name": db_user.get("name", "User"),
            "email": db_user["email"]
        }
    }


@router.get("/me")
async def get_me():
    # Helper endpoint for current user session checks
    return {
        "name": "User",
        "email": "user@example.com"
    }