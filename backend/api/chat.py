from fastapi import APIRouter
from pydantic import BaseModel

from agents.router import route_query

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    answer = route_query(request.message)

    return ChatResponse(response=answer)