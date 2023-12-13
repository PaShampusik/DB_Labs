from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.finance_entity import Finance
from schemas.finance.finance_schema import FinanceSchema
from schemas.finance.finance_schema_create import FinanceSchemaCreate
from schemas.finance.finance_schema_update import FinanceSchemaUpdate
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class FinanceRepository(BaseRepo):
    @property
    def model(self) -> type[Finance]:
        return Finance

    @property
    def schema(self) -> type[FinanceSchema]:
        return FinanceSchema

    @property
    def create_schema(self) -> type[FinanceSchemaCreate]:
        return FinanceSchemaCreate

    @property
    def update_schema(self) -> type[FinanceSchemaUpdate]:
        return FinanceSchemaUpdate
