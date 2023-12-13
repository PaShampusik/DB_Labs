from typing import Optional, Type

from fastapi import HTTPException, status
from schemas.order.order_schema_create import OrderSchemaCreate
from base.base_service import AsyncSession, BaseService
from repositories.order_repository import OrderRepository
from schemas.order.order_schema import OrderSchema
from base.base_repository import BaseRepo


class OrderService(BaseService):
    @property
    def repository(self) -> type[OrderRepository]:
        return OrderRepository()

    async def get_all(
        self, session: AsyncSession | None = None, account: OrderSchema | None = None
    ):
        await self.check_staff(account)
        return await super().get_all(session, account)

    async def get_by_id(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: OrderSchema | None = None,
    ):
        await self.check_staff(account)
        return await super().get_by_id(id, session, account)

    async def create(
        self,
        schema_create: BaseRepo.create_schema,
        session: AsyncSession | None = None,
        account: OrderSchema | None = None,
    ):
        await self.check_admin(account)
        return await super().create(schema_create, session, account)

    async def update(
        self,
        id: int,
        schema_update: BaseRepo.update_schema,
        session: AsyncSession | None = None,
        account: OrderSchema | None = None,
    ):
        await self.check_staff(account.id)
        return await super().update(id, schema_update, session, account)

    async def delete(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: OrderSchema | None = None,
    ):
        await self.check_admin(account.id)
        return await super().delete(id, session, account)
