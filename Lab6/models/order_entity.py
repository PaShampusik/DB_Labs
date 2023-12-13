from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime


class Order(BaseEntity):
    __tablename__ = "order"
    sum: Mapped[int] = mapped_column(int, nullable=False)
    time: Mapped[datetime] = mapped_column(datetime, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    status_id: Mapped[int] = mapped_column(ForeignKey("order_status.id"), nullable=False)
