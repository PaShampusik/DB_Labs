from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from sqlalchemy import ForeignKey, String


class Light(BaseEntity):
    __tablename__ = "light"
    name: Mapped[str] = mapped_column(String, nullable=False)
