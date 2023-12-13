from base.base_schema import BaseSchema


class ProductFeatureSchemaCreate(BaseSchema):
    product_id: int
    feature_id: int
