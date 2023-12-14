from base.base_schema import BaseSchema
from base.base_model import BaseModel


class WheelSchemaCreate(BaseModel):
    type: str
    size: int
