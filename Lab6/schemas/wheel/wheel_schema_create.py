from base.base_schema import BaseSchema


class WheelSchemaCreate(BaseSchema):
    id: int
    type: str
    size: int
