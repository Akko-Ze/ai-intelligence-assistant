from fastapi import APIRouter
import logging
from app.models.chat import ChatResponse, ChatRequest
from app.services.chat_service import chat_service


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    answer = chat_service.chat(request.messages)

    logger.info("received chat request")

    return ChatResponse(
        answer=answer
    )