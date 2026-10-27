from fastapi import FastAPI
from app.exceptions import register_exception_handlers
from app.routes.chat import router as chat_router
from contextlib import asynccontextmanager
from app.database import engine, Base
from app import models
from app.routes.users import router as users_router
from app.routes.auth import router as auth_router

@assynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="PromptBridge", lifespan=lifespan)

register_exception_handlers(app)

app.include_router(chat_router)
app.include_router(users_router)
app.include_router(auth_router)