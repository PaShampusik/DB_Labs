from datetime import datetime
from base.base_schema import BaseSchema
from schemas.mark.mark_schema import MarkSchema


class ModelSchema(BaseSchema):
    id: int
    name: str
    year: datetime
    mark_id: int

    mark: MarkSchema
