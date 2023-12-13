import uvicorn
from fastapi import FastAPI
from controllers import (
    employee_controller,
    engine_controller,
    feature_controller,
    finance_controller,
    light_controller,
    log_controller,
    mark_controller,
    model_controller,
    order_controller,
    product_controller,
    user_controller,
    review_controller,
    wheel_controller,
)

# from controllers import

app = FastAPI(
    root_path="/",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


app.include_router(employee_controller.router)
app.include_router(user_controller.router)
app.include_router(engine_controller.router)
app.include_router(feature_controller.router)
app.include_router(finance_controller.router)
app.include_router(light_controller.router)
app.include_router(log_controller.router)
app.include_router(mark_controller.router)
app.include_router(model_controller.router)
app.include_router(order_controller.router)
app.include_router(product_controller.router)
app.include_router(review_controller.router)
app.include_router(wheel_controller.router)


if __name__ == "__main__":
    uvicorn.run(app, loop="auto")
