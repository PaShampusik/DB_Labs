from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.light_entity import Light
from schemas.light.light_schema import LightSchema
from schemas.light.light_schema_create import LightSchemaCreate
from schemas.light.light_schema_update import LightSchemaUpdate
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class LightRepository(BaseRepo):
    @property
    def model(self) -> type[Light]:
        return Light

    @property
    def schema(self) -> type[LightSchema]:
        return LightSchema

    @property
    def create_schema(self) -> type[LightSchemaCreate]:
        return LightSchemaCreate

    @property
    def update_schema(self) -> type[LightSchemaUpdate]:
        return LightSchemaUpdate
