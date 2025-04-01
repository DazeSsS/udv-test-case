from fastapi import APIRouter, status
from .news import router as news_router


api_router = APIRouter()

api_router.include_router(news_router)
