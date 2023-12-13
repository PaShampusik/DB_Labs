import uvicorn
from fastapi import FastAPI
from controllers import (
    employee_controller,
)
#from controllers import log_controller

app = FastAPI(
    root_path="/",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


app.include_router(employee_controller.router)


if __name__ == "__main__":
    uvicorn.run(app, loop="auto")