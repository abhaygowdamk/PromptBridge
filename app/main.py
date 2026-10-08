from fastapi import FastAPI

from app.schemas import ChatRequest, ChatResponse
from app.llm_service import get_llm_response
from app.exceptions import register_exception_handlers

app = FastAPI(title="PromptBridge")
register_exception_handlers(app)


@app.get("/")
def root():
    return {"message": "PromptBridge is running!"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = get_llm_response(request.prompt)
    return ChatResponse(response=answer)