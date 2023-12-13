from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.wheel_entity import Wheel
from schemas.wheel.wheel_schema import WheelSchema
from schemas.wheel.wheel_schema_create import WheelSchemaCreate
from schemas.wheel.wheel_schema_update import WheelSchemaUpdate
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class EngineRepository(BaseRepo):
    @property
    def model(self) -> type[Wheel]:
        return Wheel

    @property
    def schema(self) -> type[WheelSchemaCreate]:
        return WheelSchema

    @property
    def create_schema(self) -> type[WheelSchemaCreate]:
        return WheelSchema

    @property
    def update_schema(self) -> type[WheelSchemaUpdate]:
        return WheelSchemaUpdate
