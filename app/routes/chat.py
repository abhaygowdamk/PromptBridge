from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from app.llm_service import get_llm_response
from app.dependency import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.databse import get_db
from sqlalchemy import Depends
from models import ChatMessage

router = APIRouter(tags=["Chat"])

@router.get("/")
def home():
    return {"message":"Welcome to PromptBridge"}

@router.post("/chat", response_model=ChatResponse)
async def api_response(request:ChatRequest, current_user: User = Depends(get_current_user), db:AsyncSession=Depends(get_db())):
   answer = await get_llm_response(request.prompt)

   chat_message = ChatMessage(user_id = current_user.id, prompt = request.prompt, llm_response = answer)

   db.add(chat_message)
   await db.commit()
   await db.refresh(chat_message)

   return ChatResponse(response=answer)