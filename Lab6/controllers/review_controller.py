from fastapi import APIRouter, Depends, Path
from schemas.review.review_schema_create import ReviewSchemaCreate
from schemas.review.review_schema import ReviewSchema
from schemas.review.review_schema_update import ReviewSchemaUpdate
from services.review_service import ReviewService
from services.auth_service import AuthService


router = APIRouter(prefix="/api/review", tags=["review"])


@router.get("/")
async def get_all_reviews(
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ReviewService),
):
    return await service.get_all()


@router.get("/{id}")
async def get_review_by_id(
    id: int = Path(example=1, description="ID искомого пользователя"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ReviewService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_review(
    create_schema: ReviewSchemaCreate,
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ReviewService),
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_review(
    update_schema: ReviewSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого пользователя"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ReviewService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_review(
    id: int = Path(example=1, description="ID удаляемого пользователя"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ReviewService),
):
    return await service.delete(id)
