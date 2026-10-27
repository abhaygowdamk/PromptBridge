from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import LoginRequest, TokenResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import User
from sqlalchemy import select
from app.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(data:LoginRequest, db:AsyncSession=Depends(get_db)):
    result = await db.execute(select(User).where(data.email == User.email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Email or Password "
        )

        token = create_access_token(user_id)
        return {"access_token":token, "token_type": "bearer"}

        


