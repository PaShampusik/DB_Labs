from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer, DateTime


class Product(BaseEntity):
    __tablename__ = "product"
    exterior_color: Mapped[str] = mapped_column(String, nullable=False)
    exterior_color: Mapped[str] = mapped_column(String, nullable=False)
    feature_id: Mapped[int] = mapped_column(
        ForeignKey("product_feature.id"), nullable=False
    )
    light_id: Mapped[int] = mapped_column(ForeignKey("light.id"), nullable=False)
    engine_id: Mapped[int] = mapped_column(ForeignKey("engine.id"), nullable=False)
    wheel_id: Mapped[int] = mapped_column(ForeignKey("wheel.id"), nullable=False)
    model_id: Mapped[int] = mapped_column(ForeignKey("model.id"), nullable=False)
    status_id: Mapped[int] = mapped_column(
        ForeignKey("product_status.id"), nullable=False
    )
