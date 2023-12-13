from pydantic import BaseModel


class LogSchemaUpdate(BaseModel):
    id: int
    action: int
    id_user: int
