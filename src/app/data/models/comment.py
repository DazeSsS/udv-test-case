from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from app.data.types import CreatedAt, ID


class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[ID]
    news_id: Mapped[int] = mapped_column(ForeignKey('news.id', ondelete='CASCADE'))
    title: Mapped[str] = mapped_column(String(128))
    comment: Mapped[str] = mapped_column(String(512))
    date: Mapped[CreatedAt]

    news: Mapped['News'] = relationship(back_populates='comments')
