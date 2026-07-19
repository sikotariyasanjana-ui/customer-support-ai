import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from agents.router import route_query
from database.crud import save_chat_history, get_chat_history, clear_chat_history
from llm.gemini import get_llm
from rag.retriever import load_retriever

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    agent: Optional[str] = None
    user_email: Optional[str] = "demo_user@example.com"

class ChatResponse(BaseModel):
    agent: str
    response: str
    timestamp: datetime = datetime.utcnow()

class HistoryItem(BaseModel):
    id: str
    agent: str
    question: str
    answer: str
    timestamp: datetime


_retriever = None

def get_rag_retriever():
    global _retriever
    if _retriever is None:
        try:
            _retriever = load_retriever()
        except Exception as e:
            print(f"⚠️ Warning: Could not load RAG retriever: {e}")
            _retriever = False
    return _retriever if _retriever is not False else None


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    agent_name = request.agent or "FAQ Agent"

    # Get routed response (contains matching agent and default response)
    routed_response = route_query(request.message)
    routed_agent = routed_response.get("agent", agent_name)
    routed_text = routed_response.get("response", "I'm sorry, I couldn't process your request.")

    # Determine if Gemini is available
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

    answer_text = routed_text

    if api_key:
        try:
            # Query the local FAISS retriever for context documents
            context = ""
            try:
                retriever = get_rag_retriever()
                if retriever:
                    docs = retriever.invoke(request.message)
                    context = "\n\n".join([doc.page_content for doc in docs])
            except Exception as embed_err:
                print(f"⚠️ RAG embedding retrieval failed: {embed_err}. Proceeding with general knowledge fallback.")

            system_instruction = f"""You are the '{routed_agent}' in an intelligent multi-agent customer support team.
Your job is to answer the user's question politely and professionally.

Here is the retrieved knowledge base context (use this as your source of truth):
{context}

If the context does not contain the answer, answer the question to the best of your ability using your general knowledge, but mention that this is general support knowledge."""

            import requests
            model_name = os.getenv("GEMINI_MODEL", "gemini-flash-latest")
            
            headers = {
                "Content-Type": "application/json",
                "x-goog-api-key": api_key
            }
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"

            body = {
                "contents": [
                    {
                        "parts": [{"text": request.message}]
                    }
                ],
                "systemInstruction": {
                    "parts": [{"text": system_instruction}]
                }
            }

            response = requests.post(url, json=body, headers=headers)
            if response.status_code != 200:
                raise Exception(f"HTTP Chat Error {response.status_code}: {response.text}")
            
            resp_data = response.json()
            try:
                answer_text = resp_data["candidates"][0]["content"]["parts"][0]["text"].strip()
            except KeyError:
                raise Exception(f"Unexpected response format: {resp_data}")
        except Exception as e:
            print(f"⚠️ Error querying Gemini: {e}. Falling back to default response.")
            answer_text = f"⚠️ Gemini Error: {str(e)}"

    # Save to chat history in MongoDB
    try:
        await save_chat_history(
            user_email=request.user_email,
            agent=routed_agent,
            question=request.message,
            answer=answer_text
        )
    except Exception as e:
        print(f"⚠️ Error saving chat history: {e}")

    return ChatResponse(
        agent=routed_agent,
        response=answer_text
    )


@router.get("/history", response_model=List[HistoryItem])
async def get_history(user_email: Optional[str] = "demo_user@example.com"):
    try:
        history = await get_chat_history(user_email)
        results = []
        for h in history:
            results.append(HistoryItem(
                id=str(h["_id"]),
                agent=h.get("agent", "AI Chatbot"),
                question=h.get("question", ""),
                answer=h.get("answer", ""),
                timestamp=h.get("timestamp", datetime.utcnow())
            ))
        return results
    except Exception as e:
        print(f"Error fetching history: {e}")
        return []


@router.delete("/history")
async def delete_history(user_email: Optional[str] = "demo_user@example.com"):
    try:
        await clear_chat_history(user_email)
        return {"success": True, "message": "Chat history cleared successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))