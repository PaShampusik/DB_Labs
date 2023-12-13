from base.base_schema import BaseSchema


class ProductFeatureSchemaUpdate(BaseSchema):
    product_id: int
    feature_id: int
