import os
from langchain_community.document_loaders import PyPDFLoader
from backend.return_env_data import Env_data
from langchain.text_splitter import RecursiveCharacterTextSplitter
class Read_file_cunk: 
    @staticmethod
    def read_source_file():
        source_file_path = Env_data.source_file_path()
        try:
            for file in os.listdir(source_file_path):
                if file.endswith(".pdf"):
                    file_path = os.path.join(source_file_path,file)
                    loader = PyPDFLoader(file_path)
                    document_loader = loader.load()
                    return document_loader
        except Exception as e:
            raise e
    @staticmethod
    def chunking_data(loaded_pdf,chunk_size = 500,chunk_overlap = 50):
        text_spliter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        split_text= text_spliter.split_documents(loaded_pdf)
        return split_text