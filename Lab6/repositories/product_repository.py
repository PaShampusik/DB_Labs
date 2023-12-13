from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.product_entity import Product
from schemas.product.product_schema import ProductSchema
from schemas.product.product_schema_create import ProductSchemaCreate
from schemas.product.product_schema_update import ProductSchemaUpdate
from schemas.light.light_schema import LightSchema
from schemas.engine.engine_schema import EngineSchema
from schemas.model.model_schema import ModelSchema
from schemas.wheel.wheel_schema import WheelSchema
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

    async def create_response(self, row: Row):
        fields_dict = row._asdict()

        light = LightSchema.from_orm(fields_dict)
        light.id = fields_dict["light_id"]

        engine = EngineSchema.from_orm(fields_dict)
        engine.id = fields_dict["engine_id"]

        wheel = WheelSchema.from_orm(fields_dict)
        wheel.id = fields_dict["wheel_id"]

        model = ModelSchema.from_orm(fields_dict)
        model.id = fields_dict["model_id"]

        return self.schema(
            light=light, engine=engine, wheel=wheel, model=model, **fields_dict
        )

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN light ON light.id = {self.model.__tablename__}.light_id
                JOIN engine ON engine.id = {self.model.__tablename__}.product_id
                JOIN wheel ON wheel.id = {self.model.__tablename__}.wheel_id
                JOIN model ON model.id = {self.model.__tablename__}.model_id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> ProductSchema:
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
