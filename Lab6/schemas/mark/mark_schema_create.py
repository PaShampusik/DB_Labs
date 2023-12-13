from base.base_schema import BaseSchema


class MarkSchemaCreate(BaseSchema):
    id: int
    name: str
    place_of_production: str
