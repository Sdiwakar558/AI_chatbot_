from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
V_DB_Path = "../vectorstore/db_faiss"

class Embedded_data:

    @staticmethod
    def embed_model():
        embeding_model = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")
        return embeding_model


    @staticmethod
    def save_data_VDB(source_chunk_data):
        embeding_model = Embedded_data.embed_model()
        db = FAISS.from_documents(source_chunk_data,embeding_model)
        db.save_local(V_DB_Path)
    @staticmethod
    def load_data_VDB():
        embeding_model = Embedded_data.embed_model()
        db= FAISS.load_local(V_DB_Path,embeding_model,allow_dangerous_deserialization=True)
        return db
