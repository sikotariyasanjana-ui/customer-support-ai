from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read from .env
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# MongoDB client
client = AsyncIOMotorClient(MONGODB_URI)

# Database
db = client[DATABASE_NAME]

# Collections
users_collection = db["users"]
chat_history_collection = db["chat_history"]
complaints_collection = db["complaints"]
feedback_collection = db["feedback"]
products_collection = db["products"]
faqs_collection = db["faqs"]
logs_collection = db["logs"]


async def connect_db():
    """
    Test MongoDB connection
    """
    try:
        await client.admin.command("ping")
        print("✅ MongoDB Connected Successfully")
    except Exception as e:
        print("❌ MongoDB Connection Failed")
        print(e)


async def close_db():
    """
    Close MongoDB connection
    """
    client.close()
    print("🔒 MongoDB Connection Closed")