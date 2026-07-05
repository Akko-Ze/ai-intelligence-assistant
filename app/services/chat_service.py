from app.core.llm import llm


class ChatService:

    def chat(self, messages):

        return llm.chat(messages)


chat_service = ChatService()