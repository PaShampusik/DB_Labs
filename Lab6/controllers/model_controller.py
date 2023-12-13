from fastapi import APIRouter, Depends, Path
from schemas.model.model_schema_create import ModelSchemaCreate
from schemas.model.model_schema import ModelSchema
from schemas.model.model_schema_update import ModelSchemaUpdate
from services.model_service import ModelService
from services.auth_service import AuthService


router = APIRouter(prefix="/api/model", tags=["model"])


@router.get("/")
async def get_all_models(
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ModelService),
):
    return await service.get_all()


@router.get("/{id}")
async def get_model_by_id(
    id: int = Path(example=1, description="ID искомой модели"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ModelService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_model(
    create_schema: ModelSchemaCreate,
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ModelService),
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_model(
    update_schema: ModelSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемой модели"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ModelService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_model(
    id: int = Path(example=1, description="ID удаляемой модели"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ModelService),
):
    return await service.delete(id)
