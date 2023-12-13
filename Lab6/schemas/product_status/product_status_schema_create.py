from base.base_schema import BaseSchema


class ProductStatusSchemaCreate(BaseSchema):
    id: int
    status: int
