from fastapi import APIRouter

from database.models import Complaint
from database.crud import (
    create_complaint,
    get_complaints
)

router = APIRouter()


@router.post("/")
async def submit_complaint(complaint: Complaint):

    result = await create_complaint(complaint)

    return {
        "message": "Complaint Submitted Successfully",
        "id": str(result.inserted_id)
    }


@router.get("/")
async def all_complaints():

    complaints = await get_complaints()

    for complaint in complaints:
        complaint["_id"] = str(complaint["_id"])

    return complaints