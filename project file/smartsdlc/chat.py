from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_services import generate_chat_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    reply = generate_chat_response(request.message)
    return {"response": reply}
