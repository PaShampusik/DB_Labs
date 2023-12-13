from sqlalchemy import REAL, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class Finance(BaseEntity):
    __tablename__ = "finance"
    action: Mapped[int] = mapped_column(int, nullable=False)
    sum: Mapped[int] = mapped_column(int, nullable=False)
    time: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)