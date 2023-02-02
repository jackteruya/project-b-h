from fastapi import FastAPI

from application.routers import router

app = FastAPI(
    root_path="",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

app.include_router(router)
