from fastapi import APIRouter, Depends, Path
from schemas.mark.mark_schema_create import MarkSchemaCreate
from schemas.mark.mark_schema import MarkSchema
from schemas.mark.mark_schema_update import MarkSchemaUpdate
from services.mark_service import MarkService
from services.auth_service import AuthService


router = APIRouter(prefix="/api/mark", tags=["mark"])


@router.get("/")
async def get_all_marks(
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(MarkService),
):
    return await service.get_all()


@router.get("/{id}")
async def get_marks_by_id(
    id: int = Path(example=1, description="ID искомой марки"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(MarkService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_mark(
    create_schema: MarkSchemaCreate,
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(MarkService),
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_mark(
    update_schema: MarkSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемой марки"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(MarkService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_mark(
    id: int = Path(example=1, description="ID удаляемой марки"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(MarkService),
):
    return await service.delete(id)
