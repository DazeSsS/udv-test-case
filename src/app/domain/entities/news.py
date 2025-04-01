from datetime import datetime
from pydantic import computed_field

from app.domain.entities import BaseSchema, CommentResponse


class NewsCreate(BaseSchema):
    title: str
    body: str


class NewsResponse(NewsCreate):
    id: int
    date: datetime
    deleted: bool


class NewsListItem(NewsResponse):
    comments_count: int


class NewsListResponse(BaseSchema):
    news: list[NewsListItem]
    news_count: int


class NewsDetailResponse(NewsResponse):
    comments: list[CommentResponse]
    comments_count: int
