from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from app.data.types import CreatedAt, ID


class News(Base):
    __tablename__ = 'news'

    id: Mapped[ID]
    title: Mapped[str] = mapped_column(String(128))
    body: Mapped[str] = mapped_column(Text)
    deleted: Mapped[bool] = mapped_column(server_default='false')
    date: Mapped[CreatedAt]

    comments: Mapped[list['Comment']] = relationship(back_populates='news')
