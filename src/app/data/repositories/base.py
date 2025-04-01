from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generic, TypeVar, Optional

from database import Base 


ModelType = TypeVar("ModelType", bound=Base)


class SQLAlchemyRepository(Generic[ModelType]):
    def __init__(self, session: AsyncSession, model: type[ModelType]):
        self.session = session
        self.model = model

    async def get_all(self) -> list[ModelType]:
        query = select(self.model)
        result = await self.session.scalars(query)
        return result.all()

    async def get_by_id(self, id: int) -> ModelType | None:
        result = await self.session.get(self.model, id)
        return result

    async def add(self, item: ModelType) -> ModelType:
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def delete(self, item: ModelType) -> None:
        await self.session.delete(item)
        await self.session.commit()
