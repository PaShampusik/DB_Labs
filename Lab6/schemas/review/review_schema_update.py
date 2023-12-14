from base.base_model import BaseModel


class ReviewSchemaUpdate(BaseModel):
    id: int
    user_id: int
    text: str
    rating: int
