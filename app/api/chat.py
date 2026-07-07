from fastapi import APIRouter
import logging
from app.models.chat import ChatResponse, ChatRequest
from app.services.chat_service import chat_service
from app.models.response import ApiResponse


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ApiResponse)
def chat(request: ChatRequest) -> ApiResponse:
    logger.info("received chat request")
    answer = chat_service.chat(request.messages)

    return ApiResponse(
        code=0,
        message="success",
        data=ChatResponse(answer=answer)
    )