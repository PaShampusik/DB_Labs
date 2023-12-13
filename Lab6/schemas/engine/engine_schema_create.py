from base.base_schema import BaseSchema


class EngineSchemaCreate(BaseSchema):
    id: int
    name: str
    volume: str
