from fastapi import APIRouter, Depends, Path
from schemas.user.user_schema_create import UserSchemaCreate
from schemas.user.user_schema import UserSchema
from schemas.user.user_schema_update import UserSchemaUpdate
from services.wheel_service import WheelService
from services.auth_service import AuthService


router = APIRouter(prefix="/api/wheel", tags=["wheel"])


@router.get("/")
async def get_all_wheels(
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(WheelService),
):
    return await service.get_all()


@router.get("/{id}")
async def get_wheel_by_id(
    id: int = Path(example=1, description="ID искомых колес"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(WheelService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_wheel(
    create_schema: UserSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(WheelService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_wheel(
    update_schema: UserSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемых колес"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(WheelService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_wheel(
    id: int = Path(example=1, description="ID удаляемых колес"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(WheelService),
):
    return await service.delete(id, account=account)
