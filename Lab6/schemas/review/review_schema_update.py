from base.base_schema import BaseSchema
from schemas.user.user_schema import UserSchema


class ReviewSchemaUpdate(BaseSchema):
    id: int
    user_id: int
    text: str
    rating: int
