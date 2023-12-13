from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime


class ProductStatus(BaseEntity):
    __tablename__ = "product_status"
    status: Mapped[int] = mapped_column(int, nullable=False)
