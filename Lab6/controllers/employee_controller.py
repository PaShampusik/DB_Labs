from fastapi import APIRouter, Depends, Path
from schemas.employee.employee_schema_create import EmployeeSchemaCreate
from schemas.user.user_schema import UserSchema
from services.employee_service import EmployeeService
from services.auth_service import AuthService
from schemas.employee.employee_schema_update import EmployeeSchemaUpdate


router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.get("/")
async def get_all_admins(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EmployeeService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_admin_by_id(
    id: int = Path(example=1, description="ID искомого админа"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EmployeeService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_admin(
    create_schema: EmployeeSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EmployeeService),
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_admin(
    update_schema: EmployeeSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого админа"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EmployeeService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_admin(
    id: int = Path(example=1, description="ID удаляемого админа"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EmployeeService),
):
    return await service.delete(id, account=account)
