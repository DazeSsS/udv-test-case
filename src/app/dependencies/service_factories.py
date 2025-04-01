from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from app.data.repositories import NewsRepository
from app.domain.services import NewsService


class ServiceFactory:
    @staticmethod
    def get_news_service(session: Annotated[AsyncSession, Depends(get_async_session)]) -> NewsService:
        news_repo = NewsRepository(session)
        return NewsService(news_repo)
