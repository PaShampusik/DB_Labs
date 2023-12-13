from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer, DateTime


class Wheel(BaseEntity):
    __tablename__ = "wheel"
    type: Mapped[str] = mapped_column(String, nullable=False)
    size: Mapped[int] = mapped_column(Integer, nullable=False)
