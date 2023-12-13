from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from sqlalchemy import ForeignKey, String


class Engine(BaseEntity):
    __tablename__ = "engine"
    name: Mapped[str] = mapped_column(String, nullable=False)
    volume: Mapped[str] = mapped_column(String, nullable=False)
