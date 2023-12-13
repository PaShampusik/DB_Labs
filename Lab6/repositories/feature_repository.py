from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.feature_entity import Feature
from schemas.feature.feature_schema import FeatureSchema
from schemas.feature.feature_schema_create import FeatureSchemaCreate
from schemas.feature.feature_schema_update import FeatureSchemaUpdate
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class FeatureRepository(BaseRepo):
    @property
    def model(self) -> type[Feature]:
        return Feature

    @property
    def schema(self) -> type[FeatureSchemaCreate]:
        return FeatureSchema

    @property
    def create_schema(self) -> type[FeatureSchemaCreate]:
        return FeatureSchema

    @property
    def update_schema(self) -> type[FeatureSchemaUpdate]:
        return FeatureSchemaUpdate
