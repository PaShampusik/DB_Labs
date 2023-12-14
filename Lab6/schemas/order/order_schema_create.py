from base.base_model import BaseModel
from datetime import datetime
from schemas.user.user_schema import UserSchema
from schemas.product.product_schema import ProductSchema
from schemas.order_status.order_status_schema import OrderStatusSchema


class OrderSchemaCreate(BaseModel):
    sum: int
    time: datetime
    user_id: int
    product_id: int
    status_id: int

    user: UserSchema
    product: ProductSchema
    status: OrderStatusSchema
