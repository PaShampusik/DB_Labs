from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime


class Model(BaseEntity):
    __tablename__ = "model"
    name: Mapped[str] = mapped_column(str, nullable=False)
    year: Mapped[datetime] = mapped_column(datetime, nullable=False)
    mark_id: Mapped[int] = mapped_column(ForeignKey("mark.id"), nullable= False)
