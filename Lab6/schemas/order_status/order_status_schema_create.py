from base.base_schema import BaseSchema


class OrderStatusSchemaCreate(BaseSchema):
    id: int
    status: int
