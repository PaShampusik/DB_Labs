from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class Admin(BaseEntity):
    __tablename__ = "employee"
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"), nullable=False)
    unique_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
