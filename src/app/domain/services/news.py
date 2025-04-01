from app.api.exceptions.exceptions import NotFoundException
from app.data.repositories import NewsRepository
from app.domain.entities import (
    NewsDetailResponse,
    NewsListItem,
    NewsListResponse,
    NewsResponse,
)


class NewsService:
    def __init__(
        self,
        news_repo: NewsRepository,
    ):
        self.news_repo = news_repo

    async def get_all_news(self) -> NewsListResponse:
        active_news = await self.news_repo.get_all_active_news()

        news_list_items = []
        for news, comments_count in active_news:
            news_dict = NewsResponse.model_validate(news).model_dump()
            news_dict['comments_count'] = comments_count
            news_list_items.append(NewsListItem(**news_dict))

        return NewsListResponse(
            news=news_list_items,
            news_count=len(news_list_items)
        )

    async def get_news_by_id(self, news_id: int) -> NewsDetailResponse:
        news = await self.news_repo.get_news_by_id(id=news_id)

        if not news or news.deleted:
            raise NotFoundException('News', news_id)

        news_response = NewsResponse.model_validate(news).model_dump()
        comments = news.comments
        return NewsDetailResponse(
            **news_response,
            comments=comments,
            comments_count=len(comments)
        )
