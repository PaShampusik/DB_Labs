from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.order_status_entity import OrderStatus
from schemas.order_status.order_status_schema import OrderStatusSchema
from schemas.order_status.order_status_schema_create import OrderStatusSchemaCreate
from schemas.order_status.order_status_schema_update import OrderStatusSchemaUpdate
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class ClientRepository(BaseRepo):
    @property
    def model(self) -> type[OrderStatus]:
        return OrderStatus

    @property
    def schema(self) -> type[OrderStatusSchema]:
        return OrderStatusSchema

    @property
    def create_schema(self) -> type[OrderStatusSchemaCreate]:
        return OrderStatusSchemaCreate

    @property
    def update_schema(self) -> type[OrderStatusSchemaUpdate]:
        return OrderStatusSchemaUpdate
