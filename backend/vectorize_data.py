from langchain_community.vectorstores import FAISS

class Vectorize_data:

    @staticmethod
    def store_data(data,embedding_model,path):
        vector_db=FAISS.from_documents(data,embedding_model)
        vector_db.save_local(path)