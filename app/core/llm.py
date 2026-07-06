from openai import OpenAI
from app.core.config import settings
import logging


logger = logging.getLogger(__name__)


class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.LLM_API_KEY,
            base_url=settings.LLM_BASE_URL
        )


    def chat(self, messages: list[dict]) -> str:
        logger.info("calling LLM model=%s", settings.LLM_MODEL)
        response = self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=messages
        )
        logger.info("LLM request completed")

        return response.choices[0].message.content


llm = LLMClient()