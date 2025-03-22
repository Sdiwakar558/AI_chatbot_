from langchain.chains import RetrievalQA

from backend.custom_template import Prompt_template
from backend.building_llm import Build_llm
from backend.embed_data import Embedded_data
# from custom_template import Prompt_template
class QA_Chain:
    @staticmethod
    def qa_chain_details(llm_model=Build_llm.llm(),chain_type='stuff'):
        # DB_PATH ="../vectorstore/db"
        user_prompts = Prompt_template.promt_templates(input("User Query:-   "))
        vectorstore = Embedded_data.load_data_VDB()
        qa_chain = RetrievalQA(
            llm=llm_model,
            chain_type=chain_type,
            Retriver = vectorstore.as_retriever(search_kwargs ={'k':5}),
            Return_source_documents =True,
            chain_type_kwarg = {"prompt":user_prompts},
        )
        return qa_chain
