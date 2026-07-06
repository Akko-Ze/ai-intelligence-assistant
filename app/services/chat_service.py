from app.core.llm import llm
import logging


logger = logging.getLogger(__name__)


class ChatService:

    def chat(self, messages):
        logger.info("start chat service")
        answer = llm.chat(messages)
        logger.info("chat service completed")

        return answer


chat_service = ChatService()
