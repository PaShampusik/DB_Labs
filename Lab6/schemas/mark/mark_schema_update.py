from base.base_schema import BaseSchema


class MarkSchemaUpdate(BaseSchema):
    id: int
    name: str
    place_of_production: str
