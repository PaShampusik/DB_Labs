from sqlalchemy import String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime


class Employee(BaseEntity):
    __tablename__ = "employee"

    hire_date: Mapped[datetime] = mapped_column(TIMESTAMP)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
