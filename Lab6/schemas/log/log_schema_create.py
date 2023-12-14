from pydantic import BaseModel


class LogSchemaCreate(BaseModel):
    action: int
    id_user: int
