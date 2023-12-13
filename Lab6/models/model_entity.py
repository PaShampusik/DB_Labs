from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime
from sqlalchemy import ForeignKey, String, DateTime


class Model(BaseEntity):
    __tablename__ = "model"
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    year: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    mark_id: Mapped[int] = mapped_column(ForeignKey("mark.id"), nullable=False)
