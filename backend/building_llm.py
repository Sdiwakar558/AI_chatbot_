
from langchain_groq.chat_models import ChatGroq
from backend.return_env_data import Env_data

class Build_llm:
    @staticmethod
    def llm(temperature=0.9):
        chat_model = ChatGroq(
            model= "llama-3.3-70b-versatile",
            temperature = temperature,

            api_key =Env_data.groq_api(),
        )
        return chat_model