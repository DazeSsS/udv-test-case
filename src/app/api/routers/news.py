from typing import Annotated

from fastapi import APIRouter, Depends

from app.domain.services import NewsService
from app.domain.entities import NewsDetailResponse, NewsListResponse
from app.dependencies.service_factories import ServiceFactory
from app.api.exceptions.schemas import NotFoundResponse


router = APIRouter(
    tags=['News']
)


@router.get(
    '/',
    responses={
        200: {'model': NewsListResponse},
    }
)
async def get_news(
    news_service: Annotated[NewsService, Depends(ServiceFactory.get_news_service)]
):
    news_list = await news_service.get_all_news()
    return news_list


@router.get(
    '/news/{id}',
    responses={
        200: {'model': NewsDetailResponse},
        404: {'model': NotFoundResponse},
    }
)
async def get_news_by_id(
    id: int,
    news_service: Annotated[NewsService, Depends(ServiceFactory.get_news_service)]
):
    news = await news_service.get_news_by_id(news_id=id)
    return news
