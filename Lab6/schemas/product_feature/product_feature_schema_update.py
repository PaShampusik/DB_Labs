from base.base_model import BaseModel


class ProductFeatureSchemaUpdate(BaseModel):
    product_id: int
    feature_id: int
