from base.base_model import BaseModel


class OrderStatusSchemaUpdate(BaseModel):
    id: int
    status: int
