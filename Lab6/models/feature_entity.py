from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class Feature(BaseEntity):
    __tablename__ = "feature"
    name: Mapped[str] = mapped_column(String, nullable=False)
