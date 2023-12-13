from pydantic import BaseModel


class LogSchemaCreate(BaseModel):
    id: int
    action: int
    id_user: int
