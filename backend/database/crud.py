from datetime import datetime
from database.mongodb import (
    products_collection,
    complaints_collection,
    feedback_collection,
    users_collection,
    chat_history_collection
)

async def get_products():
    cursor = products_collection.find()
    return await cursor.to_list(length=100)


async def get_complaints():
    cursor = complaints_collection.find()
    return await cursor.to_list(length=100)


async def save_feedback(feedback):
    return await feedback_collection.insert_one(
        feedback.model_dump()
    )


async def add_product(product):
    return await products_collection.insert_one(
        product.model_dump()
    )


async def create_complaint(complaint):
    return await complaints_collection.insert_one(
        complaint.model_dump()
    )


# ---------------------------
# User CRUD
# ---------------------------
async def get_user_by_email(email: str):
    return await users_collection.find_one({"email": email})


async def create_user(user_data: dict):
    user_data["created_at"] = datetime.utcnow()
    return await users_collection.insert_one(user_data)


# ---------------------------
# Chat History CRUD
# ---------------------------
async def save_chat_history(user_email: str, agent: str, question: str, answer: str):
    chat_entry = {
        "user_email": user_email,
        "agent": agent,
        "question": question,
        "answer": answer,
        "timestamp": datetime.utcnow()
    }
    return await chat_history_collection.insert_one(chat_entry)


async def get_chat_history(user_email: str = None):
    query = {"user_email": user_email} if user_email else {}
    cursor = chat_history_collection.find(query).sort("timestamp", -1)
    return await cursor.to_list(length=100)


async def clear_chat_history(user_email: str = None):
    query = {"user_email": user_email} if user_email else {}
    return await chat_history_collection.delete_many(query)