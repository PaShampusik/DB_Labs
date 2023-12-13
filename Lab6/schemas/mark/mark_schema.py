from base.base_schema import BaseSchema


class MarkSchema(BaseSchema):
    id: int
    name: str
    place_of_production: str
