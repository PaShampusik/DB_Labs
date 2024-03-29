from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.product_entity import Product
from repositories.model_repository import ModelRepository
from schemas.mark.mark_schema import MarkSchema
from schemas.product.product_schema import ProductSchema
from schemas.product.product_schema_create import ProductSchemaCreate
from schemas.product.product_schema_update import ProductSchemaUpdate
from schemas.light.light_schema import LightSchema
from schemas.engine.engine_schema import EngineSchema
from schemas.model.model_schema import ModelSchema
from schemas.wheel.wheel_schema import WheelSchema
from services.model_service import ModelService
from utils.not_found_exception import NotFoundException


class ProductRepository(BaseRepo):
    @property
    def model(self) -> type[Product]:
        return Product

    @property
    def schema(self) -> type[ProductSchema]:
        return ProductSchema

    @property
    def create_schema(self) -> type[ProductSchemaCreate]:
        return ProductSchemaCreate

    @property
    def update_schema(self) -> type[ProductSchemaUpdate]:
        return ProductSchemaUpdate

    async def create_response(self, session: AsyncSession, row: Row):
        fields_dict = row._asdict()

        light = LightSchema.from_orm(fields_dict)
        light.id = fields_dict["light_id"]

        model_repo = ModelRepository()
        model = await model_repo.get_by_id(session, fields_dict["model_id"])

        engine = EngineSchema.from_orm(fields_dict)
        engine.id = fields_dict["engine_id"]

        wheel = WheelSchema.from_orm(fields_dict)
        wheel.id = fields_dict["wheel_id"]

        model_repo = ModelRepository()
        model = await model_repo.get_by_id(session, fields_dict["model_id"])

        return self.schema(
            light=light, engine=engine, wheel=wheel, model=model, **fields_dict
        )

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN public.light ON public.light.id = {self.model.__tablename__}.light_id
                JOIN public.engine ON public.engine.id = {self.model.__tablename__}.engine_id
                JOIN public.wheel ON public.wheel.id = {self.model.__tablename__}.wheel_id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(session, obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> ProductSchema:
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN public.light ON public.light.id = {self.model.__tablename__}.light_id
                JOIN public.engine ON public.engine.id = {self.model.__tablename__}.engine_id
                JOIN public.wheel ON public.wheel.id = {self.model.__tablename__}.wheel_id
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
