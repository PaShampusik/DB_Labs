from base.base_schema import BaseSchema
from datetime import datetime
from schemas.user.user_schema import UserSchema

class EmployeeSchema(BaseSchema):
    id: int
    user_id: int
    hire_date: datetime

    user: UserSchema