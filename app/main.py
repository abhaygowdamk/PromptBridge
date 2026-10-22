from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.llm_service import get_llm_response
from app.exceptions import register_exception_handlers


app = FastAPI()

register_exception_handlers(app)

@app.get("/")
def home():
    return {"Message":"PromptBridge"}

@app.post("/chat", response_model=ChatResponse)
def prmot_request(request: ChatRequest):
    answer = get_llm_response(request.prompt)
    return ChatResponse(response=answer)

