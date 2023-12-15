from fastapi import APIRouter, Depends, Path
from schemas.order.order_schema_create import OrderSchemaCreate
from schemas.user.user_schema import UserSchema
from schemas.order.order_schema_update import OrderSchemaUpdate
from services.order_service import OrderService
from services.auth_service import AuthService


router = APIRouter(prefix="/api/order", tags=["order"])


@router.get("/")
async def get_all_orders(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(OrderService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_order_by_id(
    id: int = Path(example=1, description="ID искомого заказа"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(OrderService),
):
    return await service.get_by_id(id, account=account)


@router.post("/{id}_order")
async def order_by_id(
    create_schema: OrderSchemaUpdate,
    service=Depends(OrderService),
):
    return await service.order_by_id(create_schema)


@router.post("/")
async def create_order(
    create_schema: OrderSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(OrderService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_order(
    update_schema: OrderSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого заказа"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(OrderService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_order(
    id: int = Path(example=1, description="ID удаляемого заказа"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(OrderService),
):
    return await service.delete(id, account=account)
