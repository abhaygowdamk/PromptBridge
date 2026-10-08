from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from google.genai import errors

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(StarletteHTTPException)
    def http_exception(request, exc):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

    @app.exception_handler(RequestValidationError)
    def validation_exception(request, exc):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": exc.errors()},
        )

    @app.exception_handler(errors.APIError)
    def llm_exception(request, exc):
        return JSONResponse(
            status_code=status.HTTP_502_BAD_GATEWAY,
            content={"message": f"LLM call failed: {exc.message}"},
        )