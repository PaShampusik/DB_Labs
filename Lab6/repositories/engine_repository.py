from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.engine_entity import Engine
from schemas.engine.engine_schema import EngineSchema
from schemas.engine.engine_schema_create import EngineSchemaCreate
from schemas.engine.engine_schema_update import EngineSchemaUpdate
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class EngineRepository(BaseRepo):
    @property
    def model(self) -> type[Engine]:
        return Engine

    @property
    def schema(self) -> type[EngineSchemaCreate]:
        return EngineSchema

    @property
    def create_schema(self) -> type[EngineSchemaCreate]:
        return EngineSchema

    @property
    def update_schema(self) -> type[EngineSchemaUpdate]:
        return EngineSchemaUpdate
