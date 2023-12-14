from fastapi import APIRouter, Depends, Path
from schemas.employee.employee_schema_create import EmployeeSchemaCreate
from schemas.user.user_schema import UserSchema
from services.engine_service import EngineService
from services.auth_service import AuthService
from schemas.employee.employee_schema_update import EmployeeSchemaUpdate


router = APIRouter(prefix="/api/engine", tags=["engine"])


@router.get("/")
async def get_all_engines(
    #account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EngineService),
):
    return await service.get_all()


@router.get("/{id}")
async def get_engine_by_id(
    id: int = Path(example=1, description="ID искомого ДВС"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EngineService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_engine(
    create_schema: EmployeeSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EngineService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_engine(
    update_schema: EmployeeSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого ДВС"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EngineService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_engine(
    id: int = Path(example=1, description="ID удаляемого ДВС"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(EngineService),
):
    return await service.delete(id, account=account)
