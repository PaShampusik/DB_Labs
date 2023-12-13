from typing import Optional, Type

from fastapi import HTTPException, status
from base.base_service import AsyncSession, BaseRepository, BaseService
from repositories.review_repository import ReviewRepository
from base.base_repository import BaseRepo
from schemas.review.review_schema import ReviewSchema


class ReviewService(BaseService):
    @property
    def repository(self) -> ReviewRepository:
        return ReviewRepository()

    async def get_all(
        self, session: AsyncSession | None = None, account: ReviewSchema | None = None
    ):
        await self.check_staff(account)
        return await super().get_all(session, account)

    async def get_by_id(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: ReviewSchema | None = None,
    ):
        await self.check_staff(account)
        return await super().get_by_id(id, session, account)

    async def create(
        self,
        schema_create: BaseRepo.create_schema,
        session: AsyncSession | None = None,
        account: ReviewSchema | None = None,
    ):
        await self.check_admin(account)
        return await super().create(schema_create, session, account)

    async def update(
        self,
        id: int,
        schema_update: BaseRepo.update_schema,
        session: AsyncSession | None = None,
        account: ReviewSchema | None = None,
    ):
        await self.check_staff(account)
        return await super().update(id, schema_update, session, account)

    async def delete(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: ReviewSchema | None = None,
    ):
        await self.check_admin(account)
        return await super().delete(id, session, account)
