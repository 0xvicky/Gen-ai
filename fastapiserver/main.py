from fastapi import FastAPI
from fastapiserver.model.model import Prompt
from fastapiserver.services.ai_service import Get_ai_response
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Modi fucn youi kubit"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/chat")
def chat(promptObj:Prompt):
    res =  Get_ai_response(promptObj.prompt)
    return {"message": res}