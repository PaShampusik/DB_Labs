from pydantic import BaseModel


class LogSchemaUpdate(BaseModel):
    action: int
    id_user: int
