from fastapi import APIRouter, Depends, Path
from schemas.product.product_schema_create import ProductSchemaCreate
from schemas.product.product_schema import ProductSchema
from schemas.product.product_schema_update import ProductSchemaUpdate
from services.product_service import ProductService
from services.auth_service import AuthService


router = APIRouter(prefix="/api/product", tags=["product"])


@router.get("/")
async def get_all_products(
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ProductService),
):
    return await service.get_all()


@router.get("/{id}")
async def get_products_by_id(
    id: int = Path(example=1, description="ID искомого товара"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ProductService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_product(
    create_schema: ProductSchemaCreate,
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ProductService),
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_product(
    update_schema: ProductSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого товара"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ProductService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_product(
    id: int = Path(example=1, description="ID удаляемого товара"),
    # account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ProductService),
):
    return await service.delete(id)
