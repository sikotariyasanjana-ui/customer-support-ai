import os
import sys

# Ensure backend directory is in sys.path to allow absolute imports when running from the root folder
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your routers
from api.health import router as health_router
from api.product import router as product_router
from api.complaint import router as complaint_router
from api.feedback import router as feedback_router
from api.auth import router as auth_router
from api.chat import router as chat_router

# Create FastAPI app
app = FastAPI(
    title="Customer Support AI API",
    description="Backend API for Customer Support AI Project",
    version="1.0.0"
)

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    import os
    import sys
    from database.mongodb import chat_history_collection
    
    # Read backend requirements file if present
    reqs = ""
    try:
        if os.path.exists("requirements.txt"):
            with open("requirements.txt", "r") as f:
                reqs = f.read()
        elif os.path.exists("backend/requirements.txt"):
            with open("backend/requirements.txt", "r") as f:
                reqs = f.read()
    except Exception as e:
        reqs = f"Error: {e}"

    # Get count of chat history documents
    history_count = -1
    try:
        history_count = await chat_history_collection.count_documents({})
    except Exception as e:
        history_count = f"Error counting: {e}"

    # Diagnose MONGO_URI configuration
    uri_debug = {}
    raw_uri = os.getenv("MONGODB_URI") or os.getenv("MONGO_URI") or ""
    if raw_uri:
        uri_debug["has_uri"] = True
        uri_debug["length"] = len(raw_uri)
        uri_debug["has_brackets"] = "<" in raw_uri or ">" in raw_uri
        uri_debug["has_placeholder"] = "db_password" in raw_uri
        # Safe extraction of password area for validation
        try:
            parts = raw_uri.split("://")
            if len(parts) > 1:
                cred_parts = parts[1].split("@")[0].split(":")
                if len(cred_parts) > 1:
                    pass_str = cred_parts[1]
                    uri_debug["password_brackets_check"] = pass_str.startswith("<") or pass_str.endswith(">")
                    uri_debug["password_length"] = len(pass_str)
        except Exception as e:
            uri_debug["parse_error"] = str(e)
    else:
        uri_debug["has_uri"] = False

    # Diagnose GEMINI_API_KEY
    gemini_debug = {}
    gemini_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY") or ""
    if gemini_key:
        gemini_debug["has_key"] = True
        gemini_debug["length"] = len(gemini_key)
        gemini_debug["prefix"] = gemini_key[:6]
        gemini_debug["suffix"] = gemini_key[-6:]
    else:
        gemini_debug["has_key"] = False

    return {
        "message": "Customer Support AI Backend Running Successfully",
        "cwd": os.getcwd(),
        "sys_path": sys.path,
        "requirements": reqs,
        "chat_history_count": history_count,
        "uri_diagnostics": uri_debug,
        "gemini_diagnostics": gemini_debug
    }

# -----------------------------
# Include API Routers
# -----------------------------
app.include_router(
    health_router,
    prefix="/api/health",
    tags=["Health"]
)

app.include_router(
    product_router,
    prefix="/api/products",
    tags=["Products"]
)

app.include_router(
    complaint_router,
    prefix="/api/complaints",
    tags=["Complaints"]
)

app.include_router(
    feedback_router,
    prefix="/api/feedback",
    tags=["Feedback"]
)

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Auth"]
)

app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"]
)

# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )