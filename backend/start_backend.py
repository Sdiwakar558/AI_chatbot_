from backend.read_source import Read_file_cunk
from langchain.chains import RetrievalQA
from backend.custom_template import Prompt_template
from backend.embed_data import Embedded_data
from backend.building_llm import Build_llm
from datetime import datetime


class CallBackend:
    def __init__(self):
        pass
        # self.user_input= user_input
        # self.source_data_folder = Env_data.source_file_path()
    def call_dependencies(self,prompts):
        pdf_data =Read_file_cunk.read_source_file()
        pdf_data_chunk =Read_file_cunk.chunking_data(pdf_data)
        Embedded_data.save_data_VDB(pdf_data_chunk)
        load_VDB = Embedded_data.load_data_VDB()
        # prompts = input("user input:-  ")
        qa_chain  = RetrievalQA.from_chain_type(
            llm =Build_llm.llm(),
            chain_type = "stuff",
            retriever=load_VDB.as_retriever(search_kwargs={'k': 5}),
            return_source_documents = True,
            chain_type_kwargs={'prompt':Prompt_template.promt_templates()}
        )
        response = qa_chain.invoke({'query':prompts})
        return response["result"]

# if __name__ =="__main__":
#     prompts = input("User input:-    ")
#     curr_date1 = datetime.now()
#     print(CallBackend().call_dependencies(prompts))
#     print(f"{datetime.now() - curr_date1} sec")
