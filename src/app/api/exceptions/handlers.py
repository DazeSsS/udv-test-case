from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.exceptions.exceptions import NotFoundException
from app.api.exceptions.schemas import NotFoundResponse


def set_exceptions(app: FastAPI):
    @app.exception_handler(NotFoundException)
    async def not_found_exception_handler(request: Request, exc: NotFoundException):
        return JSONResponse(
            status_code=exc.status_code,
            content=NotFoundResponse(detail=exc.detail).model_dump()
        )
