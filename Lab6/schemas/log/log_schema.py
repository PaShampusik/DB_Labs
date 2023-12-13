from base.base_schema import BaseSchema
from schemas.user.user_schema import UserSchema

class LogSchema(BaseSchema):
    id: int
    action: int
    id_user: int

    user: UserSchema
