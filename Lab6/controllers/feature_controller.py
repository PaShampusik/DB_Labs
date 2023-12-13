from fastapi import APIRouter, Depends, Path
from schemas.feature.feature_schema_create import FeatureSchemaCreate
from schemas.user.user_schema import UserSchema
from services.feature_service import FeatureService
from services.auth_service import AuthService
from schemas.feature.feature_schema_update import FeatureSchemaUpdate


router = APIRouter(prefix="/api/feature", tags=["feature"])


@router.get("/")
async def get_all_features(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FeatureService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_feature_by_id(
    id: int = Path(example=1, description="ID искомой фичи"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FeatureService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_feature(
    create_schema: FeatureSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FeatureService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_feature(
    update_schema: FeatureSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемой фичи"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FeatureService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_feature(
    id: int = Path(example=1, description="ID удаляемой фичи"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FeatureService),
):
    return await service.delete(id, account=account)
