from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ---------------------------
# User Model
# ---------------------------
class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.utcnow()


# ---------------------------
# Chat History Model
# ---------------------------
class ChatHistory(BaseModel):
    user_email: str
    question: str
    answer: str
    timestamp: datetime = datetime.utcnow()


# ---------------------------
# Complaint Model
# ---------------------------
class Complaint(BaseModel):
    user_email: str
    subject: str
    complaint: str
    status: str = "Pending"
    created_at: datetime = datetime.utcnow()


# ---------------------------
# Feedback Model
# ---------------------------
class Feedback(BaseModel):
    user_email: str
    rating: int
    comment: Optional[str] = None
    created_at: datetime = datetime.utcnow()


# ---------------------------
# Product Model
# ---------------------------
class Product(BaseModel):
    product_name: str
    category: str
    price: float
    description: str


# ---------------------------
# FAQ Model
# ---------------------------
class FAQ(BaseModel):
    question: str
    answer: str


# ---------------------------
# Log Model
# ---------------------------
class Log(BaseModel):
    event: str
    details: str
    timestamp: datetime = datetime.utcnow()