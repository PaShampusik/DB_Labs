from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.product_status_entity import ProductStatus
from schemas.product_status.product_status_schema import ProductStatusSchema
from schemas.product_status.product_status_schema_create import (
    ProductStatusSchemaCreate,
)
from schemas.product_status.product_status_schema_update import (
    ProductStatusSchemaUpdate,
)
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class ProducStatusRepository(BaseRepo):
    @property
    def model(self) -> type[ProductStatus]:
        return ProductStatus

    @property
    def schema(self) -> type[ProductStatusSchema]:
        return ProductStatusSchema

    @property
    def create_schema(self) -> type[ProductStatusSchemaCreate]:
        return ProductStatusSchemaCreate

    @property
    def update_schema(self) -> type[ProductStatusSchemaUpdate]:
        return ProductStatusSchemaUpdate
