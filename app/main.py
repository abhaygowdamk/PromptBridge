from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app.exceptions import register_exception_handlers
from app.routes.auth import router as auth_router
from app.routes.chat import router as chat_router
from app.routes.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="PromptBridge", lifespan=lifespan)

register_exception_handlers(app)

app.include_router(chat_router)
app.include_router(users_router)
app.include_router(auth_router)