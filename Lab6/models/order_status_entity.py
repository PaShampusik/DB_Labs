from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer, DateTime


class OrderStatus(BaseEntity):
    __tablename__ = "order_status"
    status: Mapped[int] = mapped_column(Integer, nullable=False)
