from base.base_schema import BaseSchema
from schemas.user.user_schema import UserSchema


class ReviewSchema(BaseSchema):
    id: int
    user_id: int
    text: int
    rating: int

    user: UserSchema
