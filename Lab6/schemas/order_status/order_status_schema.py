from base.base_schema import BaseSchema


class OrderStatusSchema(BaseSchema):
    id: int
    status: int
