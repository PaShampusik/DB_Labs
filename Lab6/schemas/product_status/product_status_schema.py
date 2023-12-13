from base.base_schema import BaseSchema


class ProductStatusSchema(BaseSchema):
    id: int
    status: int
