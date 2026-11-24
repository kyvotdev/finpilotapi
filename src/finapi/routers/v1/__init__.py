from fastapi import APIRouter

v1rtr = APIRouter(
    prefix="/v1",
    tags=["API", "V1"],
)
