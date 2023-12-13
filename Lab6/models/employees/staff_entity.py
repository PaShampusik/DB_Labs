from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class Employee(BaseEntity):
    __tablename__ = "employee"



    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
