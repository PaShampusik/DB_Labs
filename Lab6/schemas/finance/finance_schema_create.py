from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class FinanceSchemaCreate(BaseModel):
    id: int
    action: int
    sum: float
    time: datetime
