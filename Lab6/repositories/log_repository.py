from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.log_entity import Log
from schemas.log.log_schema import LogSchema
from schemas.user.user_schema import UserSchema
from schemas.log.log_schema_create import LogSchemaCreate
from schemas.log.log_schema_update import LogSchemaUpdate
from utils.not_found_exception import NotFoundException


class LogRepository(BaseRepo):
    @property
    def model(self) -> type[Log]:
        return Log

    @property
    def schema(self) -> type[LogSchema]:
        return LogSchema

    @property
    def create_schema(self) -> type[LogSchemaCreate]:
        return LogSchemaCreate

    @property
    def update_schema(self) -> type[LogSchemaUpdate]:
        return LogSchemaUpdate

    async def create_response(self, row: Row):
        fields_dict = row._asdict()

        user = UserSchema.from_orm(fields_dict)
        user.id = fields_dict["id_user"]

        return self.schema(user=user, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN public.user ON public.user.id = {self.model.__tablename__}.id_user;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> LogSchema:
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
