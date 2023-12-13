from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.mark_entity import Mark
from schemas.mark.mark_schema import MarkSchema
from schemas.mark.mark_schema_create import MarkSchemaCreate
from schemas.mark.mark_schema_update import MarkSchemaUpdate
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class MarkRepository(BaseRepo):
    @property
    def model(self) -> type[Mark]:
        return Mark

    @property
    def schema(self) -> type[MarkSchemaCreate]:
        return MarkSchema

    @property
    def create_schema(self) -> type[MarkSchemaCreate]:
        return MarkSchema

    @property
    def update_schema(self) -> type[MarkSchemaUpdate]:
        return MarkSchemaUpdate
