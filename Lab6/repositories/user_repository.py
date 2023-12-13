from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.employees.user_entity import User
from schemas.user.user_schema import UserSchema
from schemas.user.user_schema_create import UserSchemaCreate
from schemas.user.user_schema_update import UserSchemaUpdate
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class UserRepository(BaseRepo):
    @property
    def model(self) -> type[User]:
        return User

    @property
    def schema(self) -> type[UserSchema]:
        return UserSchema

    @property
    def create_schema(self) -> type[UserSchemaCreate]:
        return UserSchemaCreate

    @property
    def update_schema(self) -> type[UserSchemaUpdate]:
        return UserSchemaUpdate