from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class User(BaseEntity):
    __tablename__ = "user"

    login: Mapped[str] = mapped_column(String(30), nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    phone: Mapped[str] = mapped_column(String(17), nullable=False)
    email: Mapped[str] = mapped_column(String(17), nullable=False)
    is_staff: Mapped[bool] = mapped_column(bool, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(bool, nullable=False)
