from base.base_model import BaseModel


class ProductSchemaCreate(BaseModel):
    model_id: int
    status_id: int
    wheel_id: int
    light_id: int
    engine_id: int
    feature_id: int
    exterior_color: str
    interior_material: str
