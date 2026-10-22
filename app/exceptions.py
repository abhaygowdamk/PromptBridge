from fastapi import FastAPI
from fastapi.responses import JASONResponse
from starlette.exceptions import HTTPException


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(StarletteHTTPException)
    def http_exception(request, exc):
        return JASONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )
        
