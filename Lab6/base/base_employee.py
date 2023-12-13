from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class BaseEmployee(BaseEntity):
    __abstract__ = True
    id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    login: Mapped[str] = mapped_column(String(20), nullable=False)
    password: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(String(17), nullable=False)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    is_staff: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, nullable=False)


