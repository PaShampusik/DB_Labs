from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime


class Wheel(BaseEntity):
    __tablename__ = "wheel"
    type: Mapped[str] = mapped_column(str, nullable=False)
    size: Mapped[int] = mapped_column(int, nullable=False)
