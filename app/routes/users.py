from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import UserRequest, UserUpdate, UserResponse


router = APIRouter(prefix="/user", tags=["users"])

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(request: UserRequest, user:User, db:AsyncSession = Depends(get_db)):
    user = User(user.name=data.name, user.email=data.email)
    db.add(user)

    try:
        await db.commit()
    except IntigrityError:
        await db.rollback()
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Email already registered"
        )
    db.refresh(User)
    return user

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id:int, db:AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "User not found"
        )
    return user

@router.get("", response_model=list[UserResponse])
async def list_users(db:AsyncSession=Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()

@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(user_id:int, update:UserUpdate, db:AsyncSession=Depends(get_db)):
    user = await db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="User Not Found"
        )

    if update.name is not None:
        user.name = update.name
    if update.email is not None:
        user.email = update.email
    
    db.add(user)

    try:
        await db.commit()

    except IntigrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail = "Email Already Registered"
        )
    await db.refresh(user)
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id:int, db: AsyncSession=Depends(get_db)):
    user = await db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User not Found"
        )

    await db.delete(user)
    await db.commit()



