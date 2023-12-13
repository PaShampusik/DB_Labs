from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.product_feature_entity import ProductFeature
from schemas.product_feature.product_feature_schema import ProductFeatureSchema
from schemas.product_feature.product_feature_schema_create import ProductFeatureSchemaCreate
from schemas.product_feature.product_feature_schema_update import ProductFeatureSchemaUpdate
from schemas.feature.feature_schema import FeatureSchema
from schemas.product.product_schema import ProductSchema
from utils.not_found_exception import NotFoundException


class ProductFeatureRepository(BaseRepo):
    @property
    def model(self) -> type[ProductFeature]:
        return ProductFeature

    @property
    def schema(self) -> type[ProductFeatureSchema]:
        return ProductFeatureSchema

    @property
    def create_schema(self) -> type[ProductFeatureSchemaCreate]:
        return ProductFeatureSchemaCreate

    @property
    def update_schema(self) -> type[ProductFeatureSchemaUpdate]:
        return ProductFeatureSchemaUpdate

    async def create_response(self, row: Row):
        fields_dict = row._asdict()

        feature = FeatureSchema.from_orm(fields_dict)
        feature.id = fields_dict["feature_id"]

        product = ProductSchema.from_orm(fields_dict)
        product.id = fields_dict["product_id"]

        return self.schema(feature = feature, product=product, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN product ON product.id = {self.model.__tablename__}.product_id
                JOIN feature ON feature.id = {self.model.__tablename__}.feature_id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> ProductFeatureSchema:
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
