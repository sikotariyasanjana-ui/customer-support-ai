from fastapi import APIRouter

from database.models import Feedback
from database.crud import save_feedback

router = APIRouter()


@router.post("/")
async def create_feedback(feedback: Feedback):

    result = await save_feedback(feedback)

    return {
        "message": "Feedback Saved Successfully",
        "id": str(result.inserted_id)
    }