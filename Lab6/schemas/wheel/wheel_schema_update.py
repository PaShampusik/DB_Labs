from base.base_schema import BaseSchema
from base.base_model import BaseModel


class WheelSchemaUpdate(BaseModel):
    type: str
    size: int
