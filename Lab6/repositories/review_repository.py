from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.review_entity import Review
from schemas.review.review_schema import ReviewSchema
from schemas.user.user_schema import UserSchema
from schemas.review.review_schema_create import ReviewSchemaCreate
from schemas.review.review_schema_update import ReviewSchemaUpdate
from utils.not_found_exception import NotFoundException


class ReviewRepository(BaseRepo):
    @property
    def model(self) -> type[Review]:
        return Review

    @property
    def schema(self) -> type[ReviewSchema]:
        return ReviewSchema

    @property
    def create_schema(self) -> type[ReviewSchemaCreate]:
        return ReviewSchemaCreate

    @property
    def update_schema(self) -> type[ReviewSchemaUpdate]:
        return ReviewSchemaUpdate

    async def create_response(self, row: Row):
        fields_dict = row._asdict()

        user = UserSchema.from_orm(fields_dict)
        user.id = fields_dict["user_id"]

        return self.schema(user=user, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN user ON user.id = {self.model.__tablename__}.user_id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> ReviewSchema:
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                WHERE public.{self.model.__tablename__}.id = {id};"""
        )
        res = (await session.execute(statement)).fetchone()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return await self.create_response(res)
