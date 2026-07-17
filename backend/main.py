from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.mongodb import connect_db, close_db

from api.health import router as health_router
from api.product import router as product_router
from api.feedback import router as feedback_router
from api.complaint import router as complaint_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Backend...")

    await connect_db()

    yield

    await close_db()

    print("Backend Stopped")


app = FastAPI(
    title="Customer Support AI",
    version="1.0",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return {"message": "Customer Support AI Backend Running"}


# Include Routers AFTER app is created
app.include_router(health_router, prefix="/api/health", tags=["Health"])
app.include_router(product_router, prefix="/api/products", tags=["Products"])
app.include_router(feedback_router, prefix="/api/feedback", tags=["Feedback"])
app.include_router(complaint_router, prefix="/api/complaints", tags=["Complaints"])