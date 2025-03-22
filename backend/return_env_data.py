import os
from dotenv import load_dotenv

class Env_data:
    load_dotenv(r"C:\Users\diwashar\PycharmProjects\Api_for_llm\.env")
    @staticmethod
    def groq_api():
        GROQ_API_KEY= os.getenv("GROQ_API_KEY")
        return GROQ_API_KEY
    @staticmethod
    def pinecone_api():
        PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
        return PINECONE_API_KEY
    @staticmethod
    def tavily_api():
        TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
        return TAVILY_API_KEY
    @staticmethod
    def root_folder_path():
        ROOT_FOLDER_DIRECTORY = os.getenv("ROOT_FOLDER_DIRECTORY")
        return ROOT_FOLDER_DIRECTORY

    @staticmethod
    def source_file_path():
        SOURCE_FILE_PATH = os.getenv("SOURCE_FILE_PATH")
        return SOURCE_FILE_PATH
