from fastapi import FastAPI

from app.exceptions import register_exception_handlers
from app.routes.chat import router

app = FastAPI()

register_exception_handlers(app)

app.include_router(router)



