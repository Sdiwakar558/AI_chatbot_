from langchain_core.prompts import PromptTemplate
# from embed_data import Embedding_model
class Prompt_template:
    @staticmethod
    def promt_templates():
        custom_template = """
        use the following context to answer the question and don't generate it from you
        {context}
        Question :{question}
        Answer:
        """
        prompt = PromptTemplate(template=custom_template,input_variables= ["context","question"])
        return prompt


