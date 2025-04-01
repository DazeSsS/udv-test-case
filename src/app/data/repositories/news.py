from sqlalchemy import func, select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.repositories.base import SQLAlchemyRepository
from app.data.models import Comment, News


class NewsRepository(SQLAlchemyRepository[News]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, News)
    
    async def get_all_active_news(self) -> list[tuple[News, int]]:
        query = (
            select(News, func.count(Comment.id).label('comments_count'))
            .join(Comment, News.comments, isouter=True) 
            .where(News.deleted == False)
            .group_by(News.id)
            .order_by(News.date.desc())
        )
        result = await self.session.execute(query)
        return result.all()

    async def get_news_by_id(self, id: int) -> News:
        query = (
            select(News)
            .where(News.id == id)
            .options(selectinload(News.comments))
        )

        result = await self.session.scalar(query)
        return result
