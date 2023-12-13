from datetime import datetime
from base.base_schema import BaseSchema


class FinanceSchema(BaseSchema):
    id: int
    action: int
    sum: int
    time: datetime
