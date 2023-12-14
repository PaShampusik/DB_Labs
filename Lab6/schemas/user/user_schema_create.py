from typing import Optional
from base.base_schema import BaseSchema
from pydantic import BaseModel


class UserSchemaCreate(BaseModel):
    login: str
    password: str
    phone: str
    email: str
    is_staff: bool
    is_superuser: bool
