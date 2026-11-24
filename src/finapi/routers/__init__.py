from fastapi import APIRouter

from .hello import hellortr
from .v1 import v1rtr
from .v2 import v2rtr

main_router = APIRouter(prefix="/api", tags=["API"])
main_router.include_router(hellortr)
main_router.include_router(v1rtr)
main_router.include_router(v2rtr)
