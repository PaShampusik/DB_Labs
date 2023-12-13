from datetime import datetime
from base.base_schema import BaseSchema
from schemas.mark.mark_schema import MarkSchema


class ModelSchemaCreate(BaseSchema):
    id: int
    name: str
    year: datetime
    mark_id: int

    mark: MarkSchema
