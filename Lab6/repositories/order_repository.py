from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.order_entity import Order
from schemas.order.order_schema import OrderSchema
from schemas.order.order_schema_create import OrderSchemaCreate
from schemas.order.order_schema_update import OrderSchemaUpdate
from schemas.user.user_schema import UserSchema
from schemas.product.product_schema import ProductSchema
from schemas.order_status.order_status_schema import OrderStatusSchema
from schemas.wheel.wheel_schema import WheelSchema
from utils.not_found_exception import NotFoundException


class OrderRepository(BaseRepo):
    @property
    def model(self) -> type[Order]:
        return Order

    @property
    def schema(self) -> type[OrderSchema]:
        return OrderSchema

    @property
    def create_schema(self) -> type[OrderSchemaCreate]:
        return OrderSchemaCreate

    @property
    def update_schema(self) -> type[OrderSchemaUpdate]:
        return OrderSchemaUpdate

    async def create_response(self, row: Row):
        fields_dict = row._asdict()

        user = UserSchema.from_orm(fields_dict)
        user.id = fields_dict["user_id"]

        product = ProductSchema.from_orm(fields_dict)
        product.id = fields_dict["product_id"]

        status = OrderStatusSchema.from_orm(fields_dict)
        status.id = fields_dict["status_id"]

        return self.schema(user=user, product=product, status=status, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN user ON user.id = {self.model.__tablename__}.user_id
                JOIN product ON product.id = {self.model.__tablename__}.product_id
                JOIN order_status ON order_status.id = {self.model.__tablename__}.status_id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> OrderSchema:
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
