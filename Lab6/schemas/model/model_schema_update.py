from datetime import datetime
from base.base_model import BaseModel
from schemas.mark.mark_schema import MarkSchema


class ModelSchemaUpdate(BaseModel):
    name: str
    year: datetime
    mark_id: int

    mark: MarkSchema
