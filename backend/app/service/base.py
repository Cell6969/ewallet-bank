from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generic, TypeVar
from app.database.sql import BaseModel

TModel = TypeVar("TModel", bound=BaseModel)

class BaseService(Generic[TModel]):
    def __init__(self, model:type[TModel], session:AsyncSession):
        self.session = session
        self.model = model

    async def _get(self, id: UUID|int) -> TModel | None:
        return await self.session.get(self.model, id)
    
    async def _add(self, entity:TModel) -> TModel:
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)

        return entity
    
    async def _update(self, entity:TModel) -> TModel:
        return await self._add(entity=entity)
    
    async def _delete(self, entity:TModel) -> None:
        await self.session.delete(entity)
        await self.session.commit()