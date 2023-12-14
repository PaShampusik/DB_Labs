from base.base_model import BaseModel


class ReviewSchemaCreate(BaseModel):
    user_id: int
    text: str
    rating: int
