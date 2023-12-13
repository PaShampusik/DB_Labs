from base.base_schema import BaseSchema


class FeatureSchemaCreate(BaseSchema):
    id: int
    name: str
