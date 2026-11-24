from fastapi import FastAPI

from finapi.core.config import stg
from finapi.core.logging import setup_logging
from finapi.routers import main_router

setup_logging()

app = FastAPI(
    description="will be in future",
    version="0.1.0",
    docs_url="/docs" if stg.SWAGGER_DOCS else None,
    redoc_url="/redoc" if stg.REDOC_DOCS else None,
)
app.include_router(main_router)
