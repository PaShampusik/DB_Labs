from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.employees.staff_entity import Employee
from schemas.employee.employee_schema import EmployeeSchema
from schemas.user.user_schema import UserSchema
from schemas.employee.employee_schema_create import EmployeeSchemaCreate
from schemas.employee.employee_schema_update import EmployeeSchemaUpdate
from utils.not_found_exception import NotFoundException


class EmployeeRepository(BaseRepo):
    @property
    def model(self) -> type[Employee]:
        return Employee

    @property
    def schema(self) -> type[EmployeeSchema]:
        return EmployeeSchema

    @property
    def create_schema(self) -> type[EmployeeSchemaCreate]:
        return EmployeeSchemaCreate

    @property
    def update_schema(self) -> type[EmployeeSchemaUpdate]:
        return EmployeeSchemaUpdate

    async def create_response(self, row: Row):
        fields_dict = row._asdict()

        user = UserSchema.from_orm(fields_dict)
        user.id = fields_dict["user_id"]

        return self.schema(user=user, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN public.user ON public.user.id = {self.model.__tablename__}.user_id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> EmployeeSchema:
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN public.user ON public.user.id = public.{self.model.__tablename__}.user_id
                WHERE public.{self.model.__tablename__}.id = {id};"""
        )
        res = (await session.execute(statement)).fetchone()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return await self.create_response(res)

    async def check_admin_role(self, session: AsyncSession, user_id: int):
        return await self.get_by_user_id(session, user_id) is not None
