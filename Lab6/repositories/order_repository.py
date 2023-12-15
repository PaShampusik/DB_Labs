from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.order_entity import Order
from repositories.product_repository import ProductRepository
from schemas.order.order_schema import OrderSchema
from schemas.order.order_schema_create import OrderSchemaCreate
from schemas.order.order_schema_update import OrderSchemaUpdate
from schemas.user.user_schema import UserSchema
from schemas.product.product_schema import ProductSchema
from schemas.order_status.order_status_schema import OrderStatusSchema
from schemas.wheel.wheel_schema import WheelSchema
from utils.not_found_exception import NotFoundException
from services.product_service import ProductService


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

    async def create_response(self, session: AsyncSession, row: Row):
        fields_dict = row._asdict()

        user = UserSchema.from_orm(fields_dict)
        user.id = fields_dict["user_id"]

        product_repo = ProductRepository()
        product = await product_repo.get_by_id(session, fields_dict["product_id"])

        status = OrderStatusSchema.from_orm(fields_dict)
        status.id = fields_dict["status_id"]
        fields_dict.pop("status")
        return self.schema(user=user, product=product, status=status, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM public.{self.model.__tablename__}
                JOIN public.user ON public.user.id = public.{self.model.__tablename__}.user_id
                JOIN public.order_status ON public.order_status.id = public.{self.model.__tablename__}.status_id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(session, obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> OrderSchema:
        statement = text(
            f"""SELECT * FROM public.{self.model.__tablename__}
                JOIN public.user ON public.user.id = public.{self.model.__tablename__}.user_id
                JOIN public.order_status ON public.order_status.id = public.{self.model.__tablename__}.status_id
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

    async def get_by_id_order(
        self, session: AsyncSession, id: int, schema: OrderSchema
    ) -> OrderSchema:
        statement = text(
            f"""CALL public.get_order_by_id(
                '{schema.order_id}'
                );"""
        )
        await session.execute(statement)
