from fastapi import APIRouter

from app.models.chat import ChatResponse, ChatRequest
from app.services.chat_service import chat_service


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    answer = chat_service.chat(request.messages)
    return ChatResponse(
        answer=answer
    )