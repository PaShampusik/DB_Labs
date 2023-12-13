from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_employee import BaseEmployee


class Staff(BaseEmployee):
    __tablename__ = "employee"

    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"), nullable=False)
