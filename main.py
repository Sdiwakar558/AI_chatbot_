from fastapi import FastAPI,Query
from zstandard import backend

from backend.start_backend import CallBackend
app = FastAPI()
@app.get("/")
async  def root(query:str):
    if not query:
        return {"message":"No query found"}
    else:
        return {"message":"query found"}
@app.get("/backend")
async def call_backend(query:str):
    try:
        if not query:
            return {"message":"No query found"}
        else:
            backend_instance = CallBackend()
            llm_response =backend_instance.call_dependencies(query)
            return {"message":llm_response}
    except Exception as e:
        print(e)