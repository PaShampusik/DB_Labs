from base.base_schema import BaseSchema


class OrderStatusSchemaUpdate(BaseSchema):
    id: int
    status: int
