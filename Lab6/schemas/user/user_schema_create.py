from typing import Optional
from base.base_schema import BaseSchema


class StaffSchemaCreate(BaseSchema):
    id: int
    login: str
    password: str
    phone: str
    email: str

