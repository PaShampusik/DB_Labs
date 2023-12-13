from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class Log(BaseEntity):
    __tablename__ = "log"
    action: Mapped[int] = mapped_column(int, nullable=False)
    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
