from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class FinanceSchemaCreate(BaseModel):
    action: int
    sum: int
    time: datetime
