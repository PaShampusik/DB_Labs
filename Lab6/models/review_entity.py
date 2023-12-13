from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class Review(BaseEntity):
    __tablename__ = "review"
    text: Mapped[str] = mapped_column(str, nullable=False)
    rating: Mapped[int] = mapped_column(int, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
