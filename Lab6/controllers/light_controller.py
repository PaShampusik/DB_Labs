from fastapi import APIRouter, Depends, Path
from schemas.light.light_schema_create import LightSchemaCreate
from schemas.user.user_schema import UserSchema
from schemas.light.light_schema_update import LightSchemaUpdate
from services.light_service import LightService
from services.auth_service import AuthService


router = APIRouter(prefix="/api/light", tags=["light"])


@router.get("/")
async def get_all_light(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LightService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_light_by_id(
    id: int = Path(example=1, description="ID искомых фар"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LightService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_light(
    create_schema: LightSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LightService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_light(
    update_schema: LightSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемых фар"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LightService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_light(
    id: int = Path(example=1, description="ID удаляемых фар"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(LightService),
):
    return await service.delete(id, account=account)
