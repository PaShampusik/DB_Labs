from fastapi import APIRouter, Depends, Path
from schemas.log.log_schema_create import LogSchemaCreate
from schemas.user.user_schema import UserSchema
from schemas.log.log_schema_update import LogSchemaUpdate
from services.log_service import LogService
from services.auth_service import AuthService


router = APIRouter(prefix="/api/log", tags=["log"])


@router.get("/")
async def get_all_log(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LogService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_log_by_id(
    id: int = Path(example=1, description="ID искомого лога"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LogService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_log(
    create_schema: LogSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LogService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_log(
    update_schema: LogSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого лога"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LogService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_log(
    id: int = Path(example=1, description="ID удаляемого лога"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LogService),
):
    return await service.delete(id, account=account)
