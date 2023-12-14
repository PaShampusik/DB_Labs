from base.base_model import BaseModel
from datetime import datetime
from schemas.user.user_schema import UserSchema


class EmployeeSchemaCreate(BaseModel):
    user_id: int
    hire_date: datetime
