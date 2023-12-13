from sqlalchemy import REAL, DateTime, ForeignKey, String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from sqlalchemy import ForeignKey, String
from datetime import datetime


class Finance(BaseEntity):
    __tablename__ = "finance"
    action: Mapped[int] = mapped_column(Integer, nullable=False)
    sum: Mapped[int] = mapped_column(Integer, nullable=False)
    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
