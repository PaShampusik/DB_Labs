from base.base_model import BaseModel


class ProductFeatureSchemaCreate(BaseModel):
    product_id: int
    feature_id: int
