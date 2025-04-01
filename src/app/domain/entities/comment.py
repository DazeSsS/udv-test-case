from datetime import datetime

from app.domain.entities import BaseSchema


class CommentCreate(BaseSchema):
    news_id: int
    title: str
    comment: str


class CommentResponse(CommentCreate):
    id: int
    date: datetime
