from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from sqlalchemy import ForeignKey, String


class Mark(BaseEntity):
    __tablename__ = "mark"
    name: Mapped[str] = mapped_column(String, nullable=False)
    place_of_production: Mapped[str] = mapped_column(String, nullable=False)
