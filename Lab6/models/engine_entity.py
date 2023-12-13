from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class Engine(BaseEntity):
    __tablename__ = "engine"
    name: Mapped[str] = mapped_column(str, nullable=False)
    volume: Mapped[str] = mapped_column(str, nullable=False)