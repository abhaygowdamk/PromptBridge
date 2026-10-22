from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse
from app.llm_service import get_llm_response

router = APIRouter(tags=["chat"])

@router.get("/")
def home():
    return {"Message":"PromptBridge"}

@router.post("/chat", response_model=ChatResponse)
def prmot_request(request: ChatRequest):
    answer = get_llm_response(request.prompt)
    return ChatResponse(response=answer)

