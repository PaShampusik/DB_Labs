from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.model_entity import Model
from repositories.mark_repository import MarkRepository
from schemas.model.model_schema import ModelSchema
from schemas.mark.mark_schema import MarkSchema
from schemas.model.model_schema_create import ModelSchemaCreate
from schemas.model.model_schema_update import ModelSchemaUpdate
from utils.not_found_exception import NotFoundException


class ModelRepository(BaseRepo):
    @property
    def model(self) -> type[Model]:
        return Model

    @property
    def schema(self) -> type[ModelSchema]:
        return ModelSchema

    @property
    def create_schema(self) -> type[ModelSchemaCreate]:
        return ModelSchemaCreate

    @property
    def update_schema(self) -> type[ModelSchemaUpdate]:
        return ModelSchemaUpdate

    async def create_response(self, session: AsyncSession, row: Row):
        fields_dict = row._asdict()

        mark_repo = MarkRepository()
        mark = await mark_repo.get_by_id(session, fields_dict["mark_id"])

        return self.schema(mark=mark, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(f"""SELECT * FROM {self.model.__tablename__};""")
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(session, obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> ModelSchema:
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
        return await self.create_response(session, res)
