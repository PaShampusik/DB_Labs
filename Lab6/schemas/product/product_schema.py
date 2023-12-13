from datetime import datetime
from base.base_schema import BaseSchema
from schemas.engine.engine_schema import EngineSchema
from schemas.wheel.wheel_schema import WheelSchema
from schemas.light.light_schema import LightSchema
from schemas.model.model_schema import ModelSchema


class ProductSchema(BaseSchema):
    id: int
    model_id: int
    status_id: int
    wheel_id: int
    light_id: int
    engine_id: int
    feature_id: int
    exterior_color: str
    interior_material: str

    engine: EngineSchema
    wheel: WheelSchema
    light: LightSchema
    model: ModelSchema
