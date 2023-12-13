from fastapi import APIRouter, Depends, Path
from schemas.user.user_schema_create import UserSchemaCreate
from schemas.user.user_schema import UserSchema
from schemas.user.user_schema_update import UserSchemaUpdate
from services.user_service import UserService
from services.auth_service import AuthService


router = APIRouter(prefix="/api/user", tags=["user"])


@router.get("/")
async def get_all_users(
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.get_all()


@router.get("/{id}")
async def get_users_by_id(
    id: int = Path(example=1, description="ID искомого пользователя"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_user(
    create_schema: UserSchemaCreate,
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_user(
    update_schema: UserSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого пользователя"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_user(
    id: int = Path(example=1, description="ID удаляемого пользователя"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.delete(id)
