from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity
from datetime import datetime


class ProductFeature(BaseEntity):
    __tablename__ = "product_feature"
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    feature_id: Mapped[int] = mapped_column(ForeignKey("feature.id"), nullable=False)
