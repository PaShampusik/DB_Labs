from base.base_schema import BaseSchema


class WheelSchemaUpdate(BaseSchema):
    id: int
    type: str
    size: int
