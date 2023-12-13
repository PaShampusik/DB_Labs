from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class Light(BaseEntity):
    __tablename__ = "light"
    name: Mapped[str] = mapped_column(str, nullable=False)
