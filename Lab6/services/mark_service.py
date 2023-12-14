from typing import Optional, Type

from fastapi import HTTPException, status
from schemas.mark.mark_schema_create import MarkSchemaCreate
from base.base_service import AsyncSession, BaseService
from repositories.mark_repository import MarkRepository
from schemas.mark.mark_schema import MarkSchema
from base.base_repository import BaseRepo


class MarkService(BaseService):
    @property
    def repository(self) -> type[MarkRepository]:
        return MarkRepository()

    async def get_all(
        self, session: AsyncSession | None = None, account: MarkSchema | None = None
    ):
        await self.check_staff(account)
        return await super().get_all(session, account)

    async def get_by_id(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: MarkSchema | None = None,
    ):
        await self.check_staff(account)
        return await super().get_by_id(id, session, account)

    async def create(
        self,
        schema_create: BaseRepo.create_schema,
        session: AsyncSession | None = None,
        account: MarkSchema | None = None,
    ):
        await self.check_admin(account)
        return await super().create(schema_create, session, account)

    async def update(
        self,
        id: int,
        schema_update: BaseRepo.update_schema,
        session: AsyncSession | None = None,
        account: MarkSchema | None = None,
    ):
        await self.check_staff(account)
        return await super().update(id, schema_update, session, account)

    async def delete(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: MarkSchema | None = None,
    ):
        await self.check_admin(account)
        return await super().delete(id, session, account)
