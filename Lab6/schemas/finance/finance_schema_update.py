from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class FinanceSchemaUpdate(BaseModel):
    action: int
    sum: int
    time: Optional[datetime]
