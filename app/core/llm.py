from openai import OpenAI
from app.core.config import settings


class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.LLM_API_KEY,
            base_url=settings.LLM_BASE_URL
        )


    def chat(self, messages: list[dict]) -> str:
        response = self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=messages
        )

        return response.choices[0].message.content


llm = LLMClient()