from base.base_schema import BaseSchema
from schemas.product.product_schema import ProductSchema
from schemas.feature.feature_schema import FeatureSchema


class ProductFeatureSchema(BaseSchema):
    product_id: int
    feature_id: int

    product: ProductSchema
    feature: FeatureSchema
