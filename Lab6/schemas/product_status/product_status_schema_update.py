from base.base_schema import BaseSchema


class ProductStatusSchemaUpdate(BaseSchema):
    id: int
    status: int
