from base.base_model import BaseModel


class OrderStatusSchemaCreate(BaseModel):
    status: int
