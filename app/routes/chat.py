from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from app.llm_service import get_llm_response
router = APIRouter(tags=["Chat"])

@router.get("/")
def home():
    return {"message":"Welcome to PromptBridge"}

@router.post("/chat", response_model=ChatResponse)
async def api_response(request:ChatRequest):
   answer = await get_llm_response(request.prompt)
   return ChatResponse(response=answer)