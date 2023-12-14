from typing import Optional, Type

from fastapi import HTTPException, status
from schemas.model.model_schema_create import ModelSchemaCreate
from base.base_service import AsyncSession, BaseService
from repositories.model_repository import ModelRepository
from schemas.model.model_schema import ModelSchema
from base.base_repository import BaseRepo


class ModelService(BaseService):
    @property
    def repository(self) -> type[ModelRepository]:
        return ModelRepository()

    async def get_all(
        self, session: AsyncSession | None = None, account: ModelSchema | None = None
    ):
        await self.check_staff(account)
        return await super().get_all(session, account)

    async def get_by_id(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: ModelSchema | None = None,
    ):
        await self.check_staff(account)
        return await super().get_by_id(id, session, account)

    async def create(
        self,
        schema_create: BaseRepo.create_schema,
        session: AsyncSession | None = None,
        account: ModelSchema | None = None,
    ):
        await self.check_admin(account)
        return await super().create(schema_create, session, account)

    async def update(
        self,
        id: int,
        schema_update: BaseRepo.update_schema,
        session: AsyncSession | None = None,
        account: ModelSchema | None = None,
    ):
        await self.check_staff(account)
        return await super().update(id, schema_update, session, account)

    async def delete(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: ModelSchema | None = None,
    ):
        await self.check_admin(account)
        return await super().delete(id, session, account)
